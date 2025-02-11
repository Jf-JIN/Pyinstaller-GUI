import os
import json
import locale
import logging
from typing import Self


class WidgetsLanguage():
    """
    控件语言单元

    属性(保护):
    - display_text: 控件显示文本
    - tool_tip: 控件提示文本

    方法:
    - set_display_text(text: str): 设置控件显示文本
    - set_tool_tip(text: str): 设置控件提示文本
    """

    def __init__(self, widget_name: str) -> None:
        self.__widget_name: str = widget_name
        self.__display_text: str = ''
        self.__tool_tip: str = ''

    @property
    def name(self) -> str:
        return self.__widget_name

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


class LanguageManager():
    """
    语言管理器

    参数:
    - exe_folder_path(str): 可执行文件所在文件夹路径
    - language_package_name(str(str)): 语言包名称, 默认为 None

    属性:
    - 与语言包内的键名相同

    方法:
    - open_language_package: 打开语言包
    """
    __instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        if not cls.__instance:
            cls.__instance: Self = super().__new__(cls)
            cls.__instance.__isInitialized = False
        return cls.__instance

    def __init__(
        self,
        chinese_language_package: dict,
        english_language_package: dict,
        exe_folder_path: str,
        language_package_name: str = '',
        language_package_folder_name: str = '.Languages',
        language_example_package_name: str = 'english_example',
        chinese_language_package_title: str = '简体中文',
        chinese_language_package_label: str = '<内置>',
        english_language_package_title: str = 'English',
        english_language_package_label: str = '<built-in>',
        suffix_language_package: str = '.lpkg',
    ) -> None:
        # 单例模式
        if self.__isInitialized:
            return
        self.__isInitialized: bool = True
        self.__exe_folder_path: str = exe_folder_path
        """ 可执行文件所在文件夹路径 """
        self.__language_package_name: str = language_package_name
        """ 语言包名称, 默认为 '' """
        self.__chinese_language_package: dict = chinese_language_package
        """ 中文语言包 """
        self.__chinese_language_package_title: str = chinese_language_package_title
        """ 中文语言包标题, 用于在UI显示的 """
        self.__chinese_language_package_label: str = chinese_language_package_label
        """ 中文语言包标签, 用于区分于外置语言包 """
        self.__chinese_language_package_full_title: str = self.__chinese_language_package_title + self.__chinese_language_package_label
        """ 中文语言包全标题, 用于在UI显示的 """
        self.__english_language_package: dict = english_language_package
        """ 英文语言包 """
        self.__english_language_package_title: str = english_language_package_title
        """ 英文语言包标题, 用于在UI显示的 """
        self.__english_language_package_label: str = english_language_package_label
        """ 英文语言包标签, 用于区分于外置语言包 """
        self.__english_language_package_full_title: str = self.__english_language_package_title + self.__english_language_package_label
        """ 英文语言包全标题, 用于在UI显示的 """
        self.__default_language_package = None
        """ 默认语言包 """
        self.__default_language_package_full_title = ''
        """ 默认语言包全标题, 用于在UI显示的 """

        self.__language_package_full_title: str = ''
        """ 语言包标题, 用于在UI显示的 """
        self.__suffix_language_package: str = suffix_language_package
        """ 语言包后缀 """
        self.__expand_language_package_folder_path = os.path.join(self.__exe_folder_path, language_package_folder_name)
        """ 语言包文件夹路径 """
        self.__language_example_package_name = language_example_package_name
        """ 用于提供示例的语言包名称 """

        self.__parameter_init()

    @property
    def language_title(self) -> str:
        """ 获取语言包标题 """
        return self.__language_package_full_title

    def get(self, key: str) -> str:
        """ 获取语言单元内容 """
        return self.__others_dict.get(key, self.__default_language_package['UIString'].get(key, ''))

    def open_language_package(self, pkg_name: str) -> None:
        """
        打开语言包文件并加载对应的语言包.

        参数:
        - pkg_name(str): 语言包的名称.
        """
        if not isinstance(pkg_name, str) or not pkg_name:
            print('pkg_name 必须为字符串类型且不为空.')
            return
        # 外置语言包
        if self.__chinese_language_package_label not in pkg_name and self.__english_language_package_label not in pkg_name:
            package_path = os.path.join(self.__expand_language_package_folder_path, pkg_name+self.__suffix_language_package)
            if not os.path.exists(package_path):
                logging.warning(f'Language package "{pkg_name}" does not exist.')
                return
            try:
                self.__current_language_package = self.__open_file(package_path)
            except:
                logging.warning(f'Failed to open language package "{pkg_name}".')
                return
        # 英语包
        elif self.__english_language_package_label in pkg_name:
            self.__current_language_package = self.__english_language_package
            self.__language_package_full_title = self.__english_language_package_full_title
        # 默认包
        else:
            self.__current_language_package = self.__chinese_language_package
            self.__language_package_full_title = self.__chinese_language_package_full_title
        self.__set_language_data()

    def __init_language_package_data(self):
        """ 初始化语言包数据 """
        # 检查语言包文件夹是否存在
        if not os.path.exists(self.__expand_language_package_folder_path):
            os.makedirs(self.__expand_language_package_folder_path)
        # 检查语言包文件夹是否为空, 并写入示例文件
        if len(os.listdir(self.__expand_language_package_folder_path)) == 0:
            self.__write_example_file()
        # 确认默认语言包
        self.__select_default_language_package()
        # 使用外置语言包
        if self.__language_package_name and self.__language_package_name not in [
            'default',
            self.__chinese_language_package_full_title,
            self.__english_language_package_full_title
        ]:
            self.__language_package_path = os.path.join(self.__expand_language_package_folder_path, self.__language_package_name+self.__suffix_language_package)
            if os.path.exists(self.__language_package_path):
                try:
                    self.__current_language_package = self.__open_file(self.__language_package_path)
                    self.__set_current_package(
                        self.__current_language_package,
                        self.__language_package_name
                    )
                    return
                except:
                    logging.warning('Language package file is not a valid json file. Please check the file.')
        # 使用内置英语语言包
        elif self.__language_package_name == self.__english_language_package_full_title:
            self.__set_current_package(
                self.__english_language_package,
                self.__english_language_package_full_title
            )
            return
        # 使用内置中文语言包
        elif self.__language_package_name == self.__chinese_language_package_full_title:
            self.__set_current_package(
                self.__chinese_language_package,
                self.__chinese_language_package_full_title
            )
            return
        # 使用默认语言包
        self.__set_current_package(
            self.__default_language_package,
            self.__default_language_package_full_title
        )

    def __set_current_package(self, language_package: dict, full_title: str) -> None:
        self.__current_language_package = language_package
        self.__language_package_full_title = full_title
        logging.info(f'Language package is set to {full_title}.')

    def __open_file(self, file_path: str) -> dict:
        with open(file_path, 'r', encoding='utf-8') as file:
            content: dict = json.load(file)
        return content

    def __write_example_file(self) -> None:
        """ 写入示例文件 """
        package_path = os.path.join(self.__expand_language_package_folder_path, self.__language_example_package_name+self.__suffix_language_package)
        with open(package_path, 'w', encoding='utf-8') as file:
            json.dump(self.__english_language_package, file, indent=4, ensure_ascii=False)

    def __parameter_init(self) -> None:
        """ 参数初始化 """
        self.__init_language_package_data()
        self.__set_language_data()

    def __set_language_data(self) -> None:
        """
        初始化管理器内语言单元属性
        """
        self.__set_widget_list()
        self.__set_others_dict()

    def __set_widget_list(self) -> None:
        """ 初始化管理器内控件语言单元属性 """
        self.__list_widges = []
        widgets_dict: dict = self.__current_language_package.get('Widgets', self.__default_language_package['Widgets'])
        for key, value in widgets_dict.items():
            key: str
            value: dict
            if not key or key == '':
                continue
            widget_item = WidgetsLanguage(key)
            widget_item.set_display_text(value.get('display_text', self.__default_language_package['Widgets'][key]['display_text']))
            widget_item.set_tool_tip(value.get('tool_tip', self.__default_language_package['Widgets'][key]['tool_tip']))
            self.__list_widges.append(widget_item)

    def __set_others_dict(self) -> None:
        """ 初始化管理器内部分内容语言单元属性 """
        self.__others_dict: dict = self.__current_language_package.get('UIString', self.__default_language_package['UIString'])

    def __select_default_language_package(self) -> None:
        """
        选择默认的语言包, 当系统为中文界面, 则默认使用中文语言包, 否则使用英文语言包.
        """
        # lang: str = locale.getlocale()[0] # exe 中无法识别
        lang: str = locale.getdefaultlocale()[0]  # exe 中可以识别
        if lang is not None and ('chinese' in lang.lower() or lang.startswith('zh')):
            self.__default_language_package = self.__chinese_language_package
            self.__default_language_package_full_title = self.__chinese_language_package_title+self.__chinese_language_package_label
        else:
            self.__default_language_package = self.__english_language_package
            self.__default_language_package_full_title = self.__english_language_package_title+self.__english_language_package_label
