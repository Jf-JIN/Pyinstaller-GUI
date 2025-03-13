import os
import json
import locale

from typing import Callable, TypeAlias
from DToolslib import SingletonMeta
from PyQt5.QtWidgets import QWidget, QAbstractButton, QLabel, QGroupBox, QTabWidget, QComboBox
from const.Const_Parameter import *

_log = Log.LanguageManager


class _WidgetsLanguageItem():
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


class _TabWidgetLanguageItem(_WidgetsLanguageItem):
    """
    TabWidget语言单元

    属性(保护):
    - tab_text: TabWidget标签文本

    方法:
    - set_tab_text(text: str): 设置TabWidget标签文本
    """

    def __init__(self, widget_name: str, tab_widget_name: str) -> None:
        super().__init__(widget_name)
        self.__tab_widget = tab_widget_name

    @property
    def tab_widget(self) -> str:
        return self.__tab_widget


class _OtherLanguageItem:
    """

    """

    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__text: str = ''
        self.__connections: list = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def text(self) -> str:
        return self.__text

    def set_text(self, text: str | list) -> None:
        self.__text = text

    def bind(self, func: Callable) -> None:
        if not callable(func):
            return
        if func not in self.__connections:
            self.__connections.append(func)
            func(self.__text)

    def unbind(self, func) -> None:
        if func in self.__connections:
            self.__connections.remove(func)

    def update(self) -> None:
        for func in self.__connections:
            func(self.__text)

    def clear(self) -> None:
        self.__connections.clear()


class LanguageManager(metaclass=SingletonMeta):
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

    def __init__(
        self,
        chinese_language_package: dict = {},
        english_language_package: dict = {},
        exe_folder_path: str = '',
        language_package_name: str = '',
        language_package_folder_name: str = '',
        language_example_package_name: str = 'english_example',
        chinese_language_package_title: str = '简体中文',
        chinese_language_package_label: str = '<内置>',
        english_language_package_title: str = 'English',
        english_language_package_label: str = '<built-in>',
        suffix_language_package: str = '.lpkg',
        display_tooltip: bool = True,
    ) -> None:
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
        self.__default_language_package_full_title: str = ''
        """ 默认语言包全标题, 用于在UI显示的 """

        self.__language_package_full_title: str = ''
        """ 语言包标题, 用于在UI显示的 """
        self.__suffix_language_package: str = suffix_language_package
        """ 语言包后缀 """
        language_package_folder_name = '.Languages' if not language_package_folder_name else f'.Languages_{language_package_folder_name}'
        self.__expand_language_package_folder_path: str = os.path.join(self.__exe_folder_path, language_package_folder_name)
        """ 语言包文件夹路径 """
        self.__language_example_package_name: str = language_example_package_name
        """ 用于提供示例的语言包名称 """

        self.__isEnabledTooltip: bool = display_tooltip if isinstance(display_tooltip, bool) else True
        """ 用于加载工具提示 """
        self.__parameter_init()

    @property
    def language_title(self) -> str:
        """ 获取语言包标题 """
        return self.__language_package_full_title

    @property
    def english_language_package_title(self) -> str:
        """ 获取英文语言包标题 """
        return self.__english_language_package_title+self.__english_language_package_label

    @property
    def chinese_language_package_title(self) -> str:
        """ 获取中文语言包标题 """
        return self.__chinese_language_package_title+self.__chinese_language_package_label

    @property
    def language_package_folder_path(self) -> str:
        """ 获取语言包文件夹路径 """
        return self.__expand_language_package_folder_path

    @property
    def expand_language_packages_list(self) -> list:
        return self.__expand_packages_name_list

    @staticmethod
    def getWord(key: str) -> str:
        language_manager = LanguageManager()
        return language_manager.get_word(key)

    @staticmethod
    def getItem(key: str) -> _OtherLanguageItem:
        language_manager = LanguageManager()
        return language_manager.get_item(key)

    @staticmethod
    def bindLanguage(key: str, func: Callable) -> None:
        """ 绑定语言单元 """
        language_manager = LanguageManager()
        language_manager.bind(key, func)

    @staticmethod
    def bindList(key_list: list, func: Callable) -> None:
        """ 绑定语言单元列表 """
        language_manager = LanguageManager()
        language_manager.bind_list(key_list, func)

    @staticmethod
    def EnableTooltip(enable: bool) -> None:
        """ 显示或隐藏提示 """
        instance = LanguageManager()
        instance.enable_tooltip(enable)

    def get_word(self, key: str) -> str:
        """ 获取语言单元内容 """
        item: _OtherLanguageItem = self.__others_dict.get(key, None)
        if item is None:
            return ''
        return item.text

    def get_item(self, key: str) -> _OtherLanguageItem:
        """ 获取语言单元 """
        return self.__others_dict.get(key, _OtherLanguageItem('__null__'))

    def bind(self, key: str, func: Callable) -> None:
        if key not in self.__others_dict:
            _log.warning(f'key {key} is not in language package')
            return
        if not callable(func):
            _log.error(f'func {func} is not callable')
            return
        item: _OtherLanguageItem = self.__others_dict[key]
        item.bind(func)

    def bind_list(self, key_list: list, func: Callable) -> None:
        self.__list_bind_list.append([key_list, func])
        temp = []
        self.__parse_list_data(key_list, temp)
        func(*temp)

    def open_language_package(self, pkg_name: str) -> None:
        """
        打开语言包文件并加载对应的语言包.

        参数:
        - pkg_name(str): 语言包的名称.
        """
        if not isinstance(pkg_name, str) or not pkg_name:
            _log.debug(f'The value of pkg_name "{pkg_name}" must be a non-empty string.')
            return
        # 外置语言包
        if self.__chinese_language_package_label not in pkg_name and self.__english_language_package_label not in pkg_name and pkg_name != 'default':
            package_path = os.path.join(self.__expand_language_package_folder_path, pkg_name+self.__suffix_language_package)
            if not os.path.exists(package_path):
                _log.info(f'Language package "{pkg_name}" does not exist.')
                self.__update_UI_comboBox()
                return
            try:
                self.__current_language_package = self.__open_file(package_path)
            except:
                _log.info(f'Failed to open language package "{pkg_name}".')
                return
        # 英语包
        elif self.__english_language_package_label in pkg_name:
            self.__current_language_package = self.__english_language_package
            self.__language_package_full_title = self.__english_language_package_full_title
        elif self.__chinese_language_package_label in pkg_name:
            self.__current_language_package = self.__chinese_language_package
            self.__language_package_full_title = self.__chinese_language_package_full_title
        # 默认包
        else:
            self.__current_language_package = self.__default_language_package
            self.__language_package_full_title = self.__default_language_package_full_title
        self.__set_language_data()
        self.update_language_display()

    def update_language_display(self):
        """ 更新语言显示 """
        for item in self.__list_widges:
            item: _WidgetsLanguageItem | _TabWidgetLanguageItem
            display_text: str = item.display_text
            tool_tip: str = item.tool_tip
            if isinstance(item, _TabWidgetLanguageItem):
                if hasattr(self.__UI, item.tab_widget) and hasattr(self.__UI, item.name):
                    tab_widget: QTabWidget = getattr(self.__UI, item.tab_widget)
                    tab_page: QWidget = getattr(self.__UI, item.name)
                    tab_widget.setTabText(tab_widget.indexOf(tab_page), display_text)
                    if self.__isEnabledTooltip:
                        tab_page.setToolTip(tool_tip)
                    else:
                        tab_page.setToolTip('')
                continue

            if hasattr(self.__UI, item.name):
                widget: QAbstractButton | QLabel | QGroupBox | QTabWidget = getattr(self.__UI, item.name)
                if hasattr(widget, 'setText') and display_text:
                    widget.setText(display_text)
                elif hasattr(widget, 'setTitle') and display_text:
                    widget.setTitle(display_text)
                elif hasattr(widget, 'setPlainText') and display_text:
                    widget.setPlainText(display_text)
                elif hasattr(widget, 'setTabText') and display_text:
                    widget.setTabText(display_text)
                if self.__isEnabledTooltip:
                    widget.setToolTip(tool_tip)
                else:
                    widget.setToolTip('')
        for item in self.__others_dict.values():
            item: _OtherLanguageItem
            item.update()
        self.__updata_list_item()

    def __updata_list_item(self):
        for bindung in self.__list_bind_list:
            temp = []
            params = self.__parse_list_data(bindung[0], temp)
            func = bindung[1]
            func(*temp)

    def __parse_list_data(self, data: list, contain_list: list):
        for item in data:
            if isinstance(item, str):
                contain_list.append(self.get_word(item))
            elif isinstance(item, list):
                temp_list = []
                self.__parse_list_data(item, temp_list)
                contain_list.append(temp_list)
            elif isinstance(item, tuple):
                temp_list = []
                self.__parse_list_data(item, temp_list)
                contain_list.append(tuple(temp_list))
            else:
                _log.info(f'Unkowned type: <{type(item).__name__}>{item}')
                pass
        return contain_list

    def enable_tooltip(self, flag: bool):
        """ 启用或禁用工具提示 """
        self.__isEnabledTooltip = flag
        self.update_language_display()

    def set_UI_object(self, UI: QWidget):
        """ 设置UI对象 """
        self.__UI = UI

    def set_UI_comboBox(self, UI_comboBox: QComboBox):
        """ 设置UI对象 """
        self.__UI_comboBox = UI_comboBox
        self.__update_UI_comboBox()

    def __get_expand_package_list(self):
        self.__expand_packages_name_list = []
        if not os.path.exists(self.__expand_language_package_folder_path):
            return
        for item in os.listdir(self.__expand_language_package_folder_path):
            if item.endswith(self.__suffix_language_package):
                self.__expand_packages_name_list.append(os.path.splitext(item)[0])

    def __update_UI_comboBox(self):
        if self.__UI_comboBox is None:
            return
        self.__get_expand_package_list()
        self.__UI_comboBox.clear()
        self.__UI_comboBox.addItem(self.chinese_language_package_title)
        self.__UI_comboBox.addItem(self.english_language_package_title)
        self.__UI_comboBox.addItems(self.__expand_packages_name_list)
        self.open_language_package(self.__language_package_name)
        self.__UI_comboBox.setCurrentText(self.language_title)

    def __read_ref(self, link_path: str):
        if link_path == '':
            return ''
        link_list = link_path.split('/')
        data = self.__current_language_package
        for link_item in link_list:
            if link_item == '#':
                continue
            if link_item not in data:
                return ''
            data = data.get(link_item)
        return data

    def __init_language_package_data(self):
        """ 初始化语言包数据 """
        # 检查语言包文件夹是否存在
        if not os.path.exists(self.__expand_language_package_folder_path):
            os.makedirs(self.__expand_language_package_folder_path)
        # 写入示例文件
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
                    _log.warning('Language package file is not a valid json file. Please check the file.')
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
        _log.info(f'Language package is set to {full_title}.')

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
        self.__others_dict = {}
        self.__expand_packages_name_list = []
        self.__UI_comboBox: QComboBox = None
        self.__list_bind_list: list = []
        self.__init_language_package_data()
        self.__set_language_data()
        self.__get_expand_package_list()

    def __set_language_data(self) -> None:
        """
        初始化管理器内语言单元属性
        """
        self.__set_widget_list()
        self.__set_others_dict()

    def __set_widget_list(self) -> None:
        """ 初始化管理器内控件语言单元属性 """
        self.__list_widges = []
        widgets_dict: dict = self.__current_language_package.get('Widgets', self.__default_language_package.get('Widgets', {}))
        for key, value in widgets_dict.items():
            key: str
            value: dict
            if not key or key == '':
                continue
            widget_item = _WidgetsLanguageItem(key)
            if 'display_text' not in value:
                flag_valid = False
                for sub_key, sub_value in value.items():
                    sub_key: str
                    sub_value: str
                    if 'display_text' not in sub_value:
                        continue
                    widget_item = _TabWidgetLanguageItem(sub_key, key)
                    text = sub_value.get('display_text', self.__default_language_package.get('Widgets', {}).get(key, {}).get(sub_key, {}).get('display_text', ''))
                    widget_item.set_display_text(text)
                    self.__list_widges.append(widget_item)
                    flag_valid = True
                if flag_valid:
                    continue
            display_text: str = value.get('display_text', self.__default_language_package.get('Widgets', {}).get(key, {}).get('display_text', ''))
            tooltip_text: str = value.get('tooltip', self.__default_language_package.get('Widgets', {}).get(key, {}).get('tooltip', ''))
            if tooltip_text.startswith('#/'):
                tooltip_text = self.__read_ref(tooltip_text)

            widget_item.set_display_text(display_text)
            widget_item.set_tool_tip(tooltip_text)
            self.__list_widges.append(widget_item)

    def __set_others_dict(self) -> None:
        """ 初始化管理器内部分内容语言单元属性 """
        others_dict: dict = self.__current_language_package.get('UIString', self.__default_language_package.get('UIString', {}))
        for key, value in others_dict.items():
            key: str
            value: dict
            if not key or key == '':
                continue
            if not isinstance(value, str):
                value = self.__default_language_package.get('UIString', {}).get(key, '')
                _log.error(f'UIString: {key} is not str, use default value: {value}')
            if key not in self.__others_dict:
                new_item = _OtherLanguageItem(key)
                self.__others_dict[key] = new_item
            item: _OtherLanguageItem = self.__others_dict[key]
            item.set_text(value)

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


LM: TypeAlias = LanguageManager
# LM: Type[LanguageManager] = LanguageManager
