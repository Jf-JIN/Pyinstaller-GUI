import os
import json
import locale
from const.Const_language_chinese import *
from const.Const_language_english import *

# 语言包, 必包含英语
_LANGUAGE_DEFAULT = LANGUAGE_CHINESE
_LANGUAGE_ENGLISH = LANGUAGE_ENGLISH

# 语言包显示后缀
_MARK_BUILD_IN_DEFAULT = '<内置>'
_MARK_BUILD_IN_ENGLISH = '<build-in>'
# 语言包显示标志
_DISPLAY_MARK_BUILD_IN_DEFAULT = '简体中文<内置>'
_DISPLAY_MARK_BUILD_IN_ENGLISH = 'English<build-in>'
# 语言包文件后缀
_SUFFIX_LANGUAGE_FILE_NAME = '.lpkg'
# 语言包文件夹名称
_LANGUAGE_FOLDER_NAME = '.Languages'
# 语言包示例文件名
_EXAMPLE_LANGUAGE_PACKAGE_NAME = 'english_example.lpkg'
# 系统语言标识
_SYSTEM_LANGUAGE_STR = 'chinese'
_SYSTEM_LANGUAGE_STR_STARTSWITH = 'zh'
# 语言包大类键名
_KEY_MULTI = 'multiInfo'
_KEY_SINGLE = 'singleInfo'


class MultiPartLanguage():
    """
    控件语言单元

    属性(保护):
    - display_text: 控件显示文本
    - tool_tip: 控件提示文本

    方法:
    - set_display_text(text: str): 设置控件显示文本
    - set_tool_tip(text: str): 设置控件提示文本
    """

    def __init__(self) -> None:
        self.__display_text: str = ''
        self.__tool_tip: str = ''

    @property
    def display_text(self) -> str:
        return self.__display_text

    @property
    def tool_tip(self) -> str:
        return self.__tool_tip

    def set_display_text(self, text: str) -> None:
        self.__display_text = str(text)

    def set_tool_tip(self, text: str) -> None:
        self.__tool_tip = str(text)


class SinglePartLanguage():
    """
    部分内容语言单元

    属性(保护):
    - display_text: 部分内容显示文本

    方法:
    - set_display_text(text: str): 设置部分内容显示文本
    """

    def __init__(self) -> None:
        self.__display_text: str = ''

    @property
    def display_text(self) -> str:
        return self.__display_text

    def set_display_text(self, text: str) -> None:
        self.__display_text = str(text)


class LanguageManager():
    """
    语言管理器

    参数:
    - exe_folder_path(str): 可执行文件所在文件夹路径
    - language_package_name(str(str)): 语言包名称, 默认为 None

    属性:
    - cbb_init_display: 当前语言包的初始化显示内容, 用于菜单显示
    - list_multi_parts: 多部分内容语言单元列表
    - list_single_parts: 单部分内容语言单元列表
    - 与语言包内的键名相同

    方法:
    - open_language_package: 打开语言包
    """

    def __init__(self, exe_folder_path: str, language_package_name: str = None) -> None:
        self.__exe_folder_path = exe_folder_path
        self.__language_package_name = language_package_name
        if not language_package_name or language_package_name == 'default':
            self.__select_default_language_package()
        self.__expand_language_package_folder_path = os.path.join(self.__exe_folder_path, _LANGUAGE_FOLDER_NAME)
        self.__language_example_package_name = _EXAMPLE_LANGUAGE_PACKAGE_NAME
        self.__check_load_file_int()
        self.__parameter_init()

    def open_language_package(self, pkg_name: str) -> None:
        """
        打开语言包文件并加载对应的语言包. 

        参数: 
        - pkg_name(str): 语言包的名称. 
        """
        if not pkg_name:
            return
        if _MARK_BUILD_IN_ENGLISH in pkg_name:
            self.__current_language_package = LANGUAGE_ENGLISH
            self.__set_object_text()
            return
        elif _MARK_BUILD_IN_DEFAULT in pkg_name:
            self.__current_language_package = _LANGUAGE_DEFAULT
            self.__set_object_text()
            return
        elif not os.path.exists(os.path.join(self.__expand_language_package_folder_path, pkg_name+_SUFFIX_LANGUAGE_FILE_NAME)):
            return
        else:
            package_path = os.path.join(self.__expand_language_package_folder_path, pkg_name+_SUFFIX_LANGUAGE_FILE_NAME)
        try:
            self.__current_language_package = self.__open_file(package_path)
            self.__set_object_text()
        except:
            return

    @property
    def cbb_init_display(self):
        """ 
        获取当前语言包的初始化显示内容, 用于菜单显示
        """
        return self.__cbb_init_display

    @property
    def list_multi_parts(self):
        """ 
        获取当前语言包的所有控件
        """
        return self.__list_multi_parts

    @property
    def list_single_parts(self):
        """ 
        获取当前语言包的所有部分内容
        """
        return self.__list_single_parts

    def __open_file(self, file_path) -> dict:
        """
        打开文件并加载内容. 

        参数: 
        - file_path(str): 文件路径. 

        返回值: 
        - content(dict): 文件内容. 
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            content: dict = json.load(file)
        return content

    def __write_example_file(self) -> None:
        """
        写入示例文件
        """
        package_path = os.path.join(self.__expand_language_package_folder_path, self.__language_example_package_name)
        with open(package_path, 'w', encoding='utf-8') as file:
            json.dump(LANGUAGE_ENGLISH, file, indent=4, ensure_ascii=False)

    def __parameter_init(self) -> None:
        """
        参数初始化
        """
        self.__list_multi_parts = []
        self.__list_single_parts = []
        self.__object_init()
        self.__update_object_list()
        self.__set_object_text()

    def __object_init(self) -> None:
        """
        初始化管理器内语言单元属性
        """
        self.__multi_parts_object_init()
        self.__single_parts_object_init()

    def __multi_parts_object_init(self) -> None:
        """
        初始化管理器内控件语言单元属性
        """
        multi_parts_dict: dict = self.__current_language_package.get([_KEY_MULTI])
        if not multi_parts_dict:
            return
        for key in multi_parts_dict.keys():
            setattr(self, key, MultiPartLanguage())

    def __single_parts_object_init(self) -> None:
        """
        初始化管理器内部分内容语言单元属性
        """
        single_parts_dict: dict = self.__current_language_package.get([_KEY_SINGLE])
        if not single_parts_dict:
            return
        for key in single_parts_dict.keys():
            setattr(self, key, SinglePartLanguage())

    def __update_object_list(self) -> None:
        self.__update_list_multi_parts()
        self.__update_list_single_parts()

    def __update_list_single_parts(self) -> None:
        """
        更新部分内容语言单元对象列表. 
        """
        self.__list_single_parts = [[key, value] for key, value in self.__dict__.items()
                                    if isinstance(value, SinglePartLanguage)]

    def __update_list_multi_parts(self) -> None:
        """
        更新控件语言单元对象列表. 
        """
        self.__list_multi_parts = [[key, value] for key, value in self.__dict__.items()
                                   if isinstance(value, MultiPartLanguage)]

    def __set_object_text(self) -> None:
        """
        设置对象的文本内容. 
        """
        self.__set_widget_object_text(self.__current_language_package)
        self.__set_single_parts_object_text(self.__current_language_package)

    def __set_widget_object_text(self, lang_dict: dict) -> None:
        """
        设置控件语言单元对象的文本内容. 

        参数: 
        - lang_dict(dict): 语言字典, 包含控件语言单元对象的文本内容. 
        """
        if _KEY_MULTI not in lang_dict:
            return
        multi_parts_dict: dict = lang_dict[_KEY_MULTI]
        for key, value in multi_parts_dict.items():
            value: dict
            if not key or key == '':
                continue
            if hasattr(self, key):
                object: MultiPartLanguage = getattr(self, key)
            else:
                return
            if 'display_text' in value:
                object.set_display_text(value['display_text'])
            if 'tool_tip' in value:
                object.set_tool_tip(value['tool_tip'])

    def __set_single_parts_object_text(self, lang_dict: dict) -> None:
        """
        设置部分内容语言单元对象的文本内容. 

        参数: 
        - lang_dict(dict): 语言字典, 包含部分内容语言单元对象的文本内容. 
        """
        if _KEY_SINGLE not in lang_dict:
            return
        single_parts_dict: dict = lang_dict[_KEY_SINGLE]
        for key, value in single_parts_dict.items():
            value: dict
            if not key or key == '':
                continue
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                return

    def __check_load_file_int(self) -> None:
        """
        检查并加载语言包文件. 
        """
        if not os.path.exists(self.__expand_language_package_folder_path):
            os.makedirs(self.__expand_language_package_folder_path)
            self.__write_example_file()
        else:
            if len(os.listdir(self.__expand_language_package_folder_path)) == 0:
                self.__write_example_file()
        if self.__language_package_name:
            self.__language_package_path = os.path.join(self.__expand_language_package_folder_path, self.__language_package_name+_SUFFIX_LANGUAGE_FILE_NAME)
            if not os.path.exists(self.__language_package_path):
                self.__select_default_language_package()
            else:
                try:
                    self.__current_language_package = self.__open_file(self.__language_package_path)
                except:
                    self.__select_default_language_package()
                    # QMessageBox.information(None, '提示', '语言包读取错误, 请检查语言包. 当前为默认语言包')
        else:
            self.__select_default_language_package()

    def __select_default_language_package(self) -> None:
        """
        选择默认的语言包, 当系统为中文界面, 则默认使用中文语言包, 否则使用英文语言包. 
        """
        # lang: str = locale.getlocale()[0] # exe 中无法识别
        lang: str = locale.getdefaultlocale()[0]  # exe 中可以识别
        if lang is not None and (_SYSTEM_LANGUAGE_STR in lang.lower() or lang.startswith(_SYSTEM_LANGUAGE_STR_STARTSWITH)):
            self.__current_language_package = _LANGUAGE_DEFAULT
            self.__cbb_init_display = _DISPLAY_MARK_BUILD_IN_DEFAULT
        else:
            self.__current_language_package = LANGUAGE_ENGLISH
            self.__cbb_init_display = _DISPLAY_MARK_BUILD_IN_ENGLISH
