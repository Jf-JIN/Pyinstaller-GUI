
import os
import json
import copy

# 默认设置 值的格式为列表 [类型/元组, 默认值]
DEFAULT_SETTING = {
    'language': [str, 'default'],
    'multi_win': [bool, 'True'],
    'win_mode': [str, 'simple'],
    'last_command': [str, ''],
    'tb_console_font_size': [int, 18],
    'tb_command_line_font_size': [int, 18],
    'auto_open_printed_command_line_folder': [bool, False],
    'auto_open_printed_command_line_file': [bool, True]

}


class SettingManager():
    """
    设置管理器

    参数:
    - exe_folder_path(str): 可执行文件所在文件夹路径

    属性(保护):
    - setting_data(dict): 设置数据

    方法:
    - open_file_to_json(file_path: str) -> None | dict: 打开文件并将其转换为JSON格式
    - write_file_to_json(content: dict, file_path: str = None) -> None: 将字典内容写入文件并以JSON格式保存. 如果未指定文件路径, 则使用默认设置文件路径. 
    """

    def __init__(self, exe_folder_path: str) -> None:
        self.__exe_folder_path: str = exe_folder_path
        self.__setting_path: str = os.path.join(self.__exe_folder_path, '.setting')
        self.__setting_data: dict = self.__check_file()

    @property
    def setting_data(self):
        return self.__setting_data

    def open_file_to_json(self, file_path: str) -> None | dict:
        """
        打开文件并将其转换为JSON格式

        参数:
        - file_path(str): 文件路径

        返回值:
        - json_data(dict): 转换后的JSON数据
        """
        if not os.path.exists(file_path):
            return
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        return json_data

    def write_file_to_json(self, content: dict = None, file_path: str = None) -> None:
        """
        将字典内容写入文件并以JSON格式保存. 

        参数:
        - content(dict): 要写入文件的字典内容. 
        - file_path(str, 可选): 要写入的文件路径. 如果未指定, 则使用默认设置路径. 
        """
        if not file_path:
            file_path = self.__setting_path
        if not content:
            content = self.__setting_data
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(content, file, indent=4, ensure_ascii=False)

    def __check_file(self):
        # 检查是否存在 setting 文件
        if not os.path.exists(self.__setting_path):
            # 不存在文件, 则创建 setting
            temp = self.__rebuild_setting()
        else:
            # 存在文件, 则检查 json 格式, 冗余, 丢失, 类型
            # 检查 json 格式
            temp = self.__check_json(self.__setting_path)
            # 检查 冗余
            temp = self.__check_redundancy(temp)
            # 检查 丢失
            temp = self.__check_lost(temp)
            # 检查 类型
            temp = self.__check_type(temp)
        return temp

    # 检查 json 格式
    def __check_json(self, file_path: str):
        """
        检查 JSON 文件并返回解析后的数据. 

        参数:
        - file_path(str): 要检查的 JSON 文件路径. 

        返回值:
        - temp(dict): 解析后的 JSON 数据. 
        """
        try:
            data_str = self.__open_file(file_path)
            temp = json.loads(data_str)
        except:
            temp = self.__rebuild_setting()
        return temp

    # 检查 类型
    def __check_type(self, content: dict) -> dict:
        """
        检查字典内容的类型, 并根据默认设置进行修复. 

        参数:
        - content(dict): 要检查和修复类型的字典内容. 

        返回值:
        - temp(dict): 修复后的字典内容. 
        """
        temp = copy.deepcopy(content)
        flag_write = False

        def __scan(current_key: str, current_value, default_value) -> None:
            """
            递归扫描字典内容, 并根据默认设置修复类型. 

            参数:
            - current_key(str): 当前键. 
            - current_value(any): 当前值. 
            - default_value(any): 默认设置的值. 
            """
            nonlocal temp
            nonlocal flag_write
            if isinstance(default_value, dict):
                if not isinstance(current_value, dict):
                    temp[current_key] = copy.deepcopy(default_value)
                    flag_write = True
                else:
                    for key, value in default_value.items():
                        if key in current_value:
                            __scan(key, current_value[key], value)
                        else:
                            current_value[key] = copy.deepcopy(value)
                            flag_write = True
            else:
                expected_type, default = default_value
                if not isinstance(current_value, expected_type):
                    temp[current_key] = default
                    flag_write = True
        __scan('', content, DEFAULT_SETTING)
        if flag_write:
            self.write_file_to_json(temp, self.__setting_path)
        return temp

    # 检查 冗余
    def __check_redundancy(self, content: dict) -> dict:
        """
        检查字典内容中的冗余项, 并根据默认设置进行修复. 

        参数:
        - content(dict): 要检查和修复冗余项的字典内容. 

        返回值:
        - compare_dict(dict): 修复后的字典内容. 
        """
        compare_dict = copy.deepcopy(content)
        temp = {}
        flag_write = False

        def __scan(parent: dict, default: dict) -> None:
            """
            递归扫描字典内容, 并根据默认设置修复冗余项. 

            参数:
            - parent(dict): 当前父级字典. 
            - default(dict): 默认设置的字典. 
            """
            nonlocal flag_write
            keys_to_delete = []
            for key, compare_value in parent.items():
                if isinstance(compare_value, dict):
                    if key not in default:
                        keys_to_delete.append(key)
                        flag_write = True
                    else:
                        __scan(compare_value, default[key][1])
                else:
                    if key not in default:
                        keys_to_delete.append(key)
                        flag_write = True
            for key in keys_to_delete:
                del parent[key]
        __scan(compare_dict, DEFAULT_SETTING)
        if flag_write:
            self.write_file_to_json(compare_dict, self.__setting_path)
        return compare_dict

    # 检查 丢失
    def __check_lost(self, content: dict) -> dict:
        """
        检查字典内容中的丢失项, 并根据默认设置进行修复. 

        参数:
        - content(dict): 要检查和修复丢失项的字典内容. 

        返回值:
        - temp(dict): 修复后的字典内容. 
        """
        temp = {}
        flag_write = False

        def __scan(parent: dict, compare: dict, temp_dict: dict) -> None:
            """
            递归扫描字典内容, 并根据默认设置修复丢失项. 

            参数:
            - parent(dict): 当前父级字典. 
            - compare(dict): 要比较的字典. 
            - temp_dict(dict): 修复后的字典. 
            """
            nonlocal flag_write
            for key, default_value in parent.items():
                if isinstance(default_value[1], dict):
                    temp_dict[key] = {}
                    if key not in compare:
                        self.__scan_to_build(default_value[1], temp_dict[key])
                        flag_write = True
                    else:
                        temp_dict[key] = {}
                        __scan(default_value[1], compare[key], temp_dict[key])
                else:
                    if key not in compare:
                        temp_dict[key] = default_value[1]
                        flag_write = True
                    else:
                        temp_dict[key] = compare[key]

        __scan(DEFAULT_SETTING, content, temp)
        if flag_write:
            self.write_file_to_json(temp, self.__setting_path)
        return temp

    def __scan_to_build(self, parent: dict, temp_dict: dict) -> dict:
        """
        递归扫描字典内容, 并构建修复后的字典. 

        参数:
        - parent(dict): 当前父级字典. 
        - temp_dict(dict): 修复后的字典. 

        返回值:
        - temp_dict(dict): 修复后的字典. 
        """
        for key, value in parent.items():
            if isinstance(value[1], dict):
                temp_dict[key] = {}
                self.__scan_to_build(value[1], temp_dict[key])
            else:
                temp_dict[key] = value[1]
        return temp_dict

    def __rebuild_setting(self) -> dict:
        """
        重新构建设置并保存到文件中. 

        参数:
            无

        返回值:
        - temp(dict): 重新构建的设置. 
        """
        temp = {}
        self.__scan_to_build(DEFAULT_SETTING, temp)
        self.write_file_to_json(temp, self.__setting_path)
        return temp

    def __open_file(self, file_path) -> str:
        """
        打开文件并读取文件内容. 

        参数:
        - file_path(str): 文件路径. 

        返回值:
        - temp(str): 文件内容. 
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            temp = file.read()
        return temp
