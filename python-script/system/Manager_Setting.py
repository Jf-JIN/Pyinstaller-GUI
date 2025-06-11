
from typing import TypeAlias
import os
import json
import copy
import logging
import traceback
import threading
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from const.Const_Parameter import *

_log = Log.SettingManager

AES_KEY = b"This\x00is\x18ein\x20Versuch\x7fvon\x07Cytrotxt"
AES_IV = b"This-is-Versuch1"


class SettingManager():
    """
    设置管理器(单例模式)

    参数:
    - exe_folder_path(str): 可执行文件所在文件夹路径
    - default_setting_dict(dict): 默认设置字典, 样式为 {键: [类型, 默认值]}, 其中类型可以为元组, 即如(str, int)
    - default_name(str): 设置文件名

    属性(保护):
    - setting_data(dict): 设置数据
    - default_setting_data(dict): 默认设置数据

    方法:
    - open_file_to_json(file_path: str) -> None | dict: 打开文件并将其转换为JSON格式
    - write_file_to_json(content: dict, file_path: str = None) -> None: 将字典内容写入文件并以JSON格式保存. 如果未指定文件路径, 则使用默认设置文件路径. 
    """
    __instance__ = None
    __lock__ = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance__:
            with cls.__lock__:
                if not cls.__instance__:
                    cls.__instance__ = super().__new__(cls)
                    cls.__instance__.__isInitialized__ = False
        return cls.__instance__

    def __init__(self, exe_folder_path: str = '', default_setting_dict: dict = {}, default_setting_name: str = '', isEncrypted=True) -> None:
        if self.__isInitialized__:
            return
        self.__isInitialized__ = True
        self.__isEncrypted: bool = isEncrypted
        self.__exe_folder_path: str = exe_folder_path
        self.__default_setting_dict: dict = default_setting_dict or {}
        self.__setting_path: str = self.__build_setting_path(default_setting_name)
        self.__setting_data: dict = self.__initialize_settings()

    @staticmethod
    def getConfig(key):
        setting_manager = SettingManager()
        return setting_manager.get_config(key)

    @staticmethod
    def setConfig(key, value):
        setting_manager = SettingManager()
        setting_manager.set_config(key, value)

    def get_config(self, key: str):
        if key not in self.__setting_data:
            _log.warning(f"Setting key {key} not found in current setting data")
        return self.__setting_data.get(key, self.__default_setting_dict.get(key, ''))

    def set_config(self, key: str, value: str):
        if value is None:
            _log.warning(f"Setting value for key {key} is empty")
            return
        if key not in self.__setting_data:
            _log.warning(f"Setting key {key} not found in current setting data.")
            return
        if isinstance(value, str):
            value = value.replace('"', "'")
        self.__setting_data[key] = value
        self.save_settings()

    def __build_setting_path(self, suffix: str) -> str:
        """构建设置文件路径"""
        filename = ".setting" if not suffix else f".setting_{suffix}"
        return os.path.join(self.__exe_folder_path, filename)

    def __initialize_settings(self) -> dict:
        """初始化设置数据"""
        if not os.path.exists(self.__setting_path):
            _log.warning("Setting file not found, creating a new one.")
            return self.__rebuild_settings()

        try:
            loaded = self.__load_settings_file()
            validated = self.__validate_settings(loaded)
            if validated != loaded:
                self.__save_settings(validated)
            return validated
        except Exception as e:
            logging.warning(f"设置文件损坏, ✅ 重新生成默认配置")
            return self.__rebuild_settings()

    def __load_settings_file(self) -> dict:
        """加载并解析设置文件"""
        if not self.__isEncrypted:
            with open(self.__setting_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                json_data = "".join(lines[1:])  # 跳过第一行
                return json.loads(json_data)
        else:
            try:
                with open(self.__setting_path, "rb") as f:
                    f.readline()  # 跳过第一行
                    encrypted = f.read()

                cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
                decrypted = unpad(cipher.decrypt(encrypted), AES.block_size).decode()
                return json.loads(decrypted)
            except:
                raise IOError(traceback.format_exc())

    def __validate_settings(self, settings: dict) -> dict:
        """验证并修复设置数据"""
        settings = self.__remove_redundant(settings)
        settings = self.__add_missing(settings)
        settings = self.__fix_types(settings)
        return settings

    def __remove_redundant(self, settings: dict) -> dict:
        """移除冗余设置项"""
        def __traverse(current: dict, defaults: dict) -> None:
            for key in list(current.keys()):
                if key not in defaults:
                    del current[key]
                    logging.info(f"移除冗余设置项: {key}")
                    continue
                if isinstance(defaults[key], dict) and isinstance(current[key], dict):
                    __traverse(current[key], defaults[key])

        cleaned = copy.deepcopy(settings)
        __traverse(cleaned, self.__default_setting_dict)
        return cleaned

    def __add_missing(self, settings: dict) -> dict:
        """添加缺失设置项"""
        merged = copy.deepcopy(settings)

        def __traverse(current: dict, defaults: dict, path: str = "") -> None:
            for key, default in defaults.items():
                full_path = f"{path}.{key}" if path else key
                if key not in current:
                    current[key] = copy.deepcopy(default[1]) if isinstance(default, list) else copy.deepcopy(default)
                    logging.info(f"添加缺失设置项: {full_path}")
                    continue
                if isinstance(default, dict) and isinstance(current[key], dict):
                    __traverse(current[key], default, full_path)

        __traverse(merged, self.__default_setting_dict)
        return merged

    def __fix_types(self, settings: dict) -> dict:
        """修复类型不匹配的设置项"""
        fixed = copy.deepcopy(settings)

        def __traverse(current: dict, defaults: dict) -> None:
            for key, default in defaults.items():
                if key not in current:
                    continue
                if isinstance(default, dict):
                    if isinstance(current[key], dict):
                        __traverse(current[key], default)
                    else:
                        fixed_value = copy.deepcopy(default[1]) if isinstance(default, list) else copy.deepcopy(default)
                        current[key] = fixed_value
                        logging.warning(f"类型修复: {key} 替换为默认结构")
                elif isinstance(default, list):
                    expected_type, default_value = default
                    if not isinstance(current[key], expected_type):
                        current[key] = default_value
                        logging.warning(f"类型修复: {key} 替换为默认值 {default_value}")

        __traverse(fixed, self.__default_setting_dict)
        return fixed

    def __rebuild_settings(self) -> dict:
        """重建默认设置文件"""
        default_settings = self.__deep_build_defaults(self.__default_setting_dict)
        self.__save_settings(default_settings)
        return default_settings

    def __deep_build_defaults(self, defaults: dict) -> dict:
        """递归构建默认设置结构"""
        result = {}
        for key, value in defaults.items():
            if isinstance(value, dict):
                result[key] = self.__deep_build_defaults(value)
            elif isinstance(value, list):
                result[key] = copy.deepcopy(value[1])
            else:
                result[key] = copy.deepcopy(value)
        return result

    def __save_settings(self, data: dict) -> None:
        """保存设置到文件"""
        header = "The file is encrypted using AES to minimize the risk of unauthorized access and unintended modifications.\n"  # 需要写入的标识行

        if not self.__isEncrypted:
            with open(self.__setting_path, "w", encoding="utf-8") as f:
                f.write(header)  # 先写入标识行
                json.dump(data, f, indent=4, ensure_ascii=False)
        else:
            json_str = json.dumps(data)
            cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
            encrypted = cipher.encrypt(pad(json_str.encode(), AES.block_size))
            with open(self.__setting_path, "wb") as f:
                f.write(header.encode())
                f.write(encrypted)

    @property
    def setting_data(self) -> dict:
        """获取当前设置数据"""
        temp = copy.deepcopy(self.__setting_data)
        return temp

    @property
    def default_setting_dict(self) -> dict:
        """获取默认设置字典"""
        return copy.deepcopy(self.__default_setting_dict)

    def reload_settings(self) -> None:
        """重新加载设置文件"""
        self.__setting_data = self.__initialize_settings()

    def save_settings(self) -> None:
        """显式保存当前设置"""
        self.__save_settings(self.__setting_data)

    def update_setting(self, key_path: str, value) -> bool:
        """
        更新指定路径的设置值 

        参数:
        - key_path: 设置路径, 例如 "window_size.width"
        - value: 要更新的值
        """
        keys = key_path.split('.')
        current = self.__setting_data
        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                return False
            current = current[key]
        current[keys[-1]] = value
        return True

    def update_and_save_setting(self, key_path: str, value) -> None:
        self.update_setting(key_path, value)
        self.save_settings()


SM: TypeAlias = SettingManager
