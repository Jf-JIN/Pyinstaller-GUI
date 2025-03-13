
import os
import time
import sys
import json
import traceback
from subprocess import Popen, CREATE_NO_WINDOW
from subprocess import run as sprun
import shutil
# import psutil
# import win32gui
# import win32process
# import win32con
import socket
import wrapt
import inspect

from UI.UI_PyToExe_ui import *
from UI.Widget_Control_TextBrowser import *
from UI.Message_Notification import *
from const.Const_Icon import *
from const.Const_Parameter import *
from system.Manager_Language import *
from system.Manager_Setting import *
from system.Loader_Pyinstaller_Struct import *
from system.Manager_Executor_Info import *
from system.Struct_Env_Info import *
from system.Thread_Pip_Install import *
from UI.Filter_Mouse import *
from tools.wait_thread import *

from system.Manager_Data import *


from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton, QDialog, QListWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSizePolicy, QFrame, QSpacerItem, QInputDialog, QLabel, QCheckBox, QRadioButton, QListWidgetItem, QTextBrowser, QMainWindow, QTableWidgetItem, QHeaderView, QTableWidget, QMenu, QAction, QTabWidget, QWidget, QScrollArea, QLineEdit, QComboBox, QGroupBox, QGridLayout, QProgressBar, QApplication, QButtonGroup, QStyledItemDelegate, QAbstractItemView
from PyQt5.QtGui import QTextCursor, QDesktopServices, QIcon, QPixmap, QTextOption
from PyQt5.QtCore import Qt, QUrl, QByteArray, QSize, QItemSelectionModel, QEventLoop, QEvent, QObject
# import pygetwindow as gw

_MENU_FOCUS_BG_COLOR = "#E8E8E8"
_TABLE_WIDGET_COLUMN_MIN_WIDTH = 80

pb_size = 35
lb_icon_size = 40
icon_padding = 8


class PyToExeUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_parameters()
        self.init_ui()
        self.init_signal_connections()

    def init_parameters(self):
        self.app_workspace_path: str = APP_WORKSPACE_PATH
        self.setting_manager = SettingManager(self.app_workspace_path)
        self.setting: dict = self.setting_manager.setting_data
        self.data_manager = DataManager()
        self.installer = self.data_manager.pyinstaller_struct
        self.data_loader = PyinstallerStructLoader()
        self.executor_info_manager = ExecutorInfoManager()

# =====================================================================================================================================================

        self.message = MessageNotification(self, position='bottom', offset=100, move_in_point=(None, '50'), hold_duration=4000)
        self.clipboard = QApplication.clipboard()

        # self.timer_check_install.timeout.connect(self.check_all_env_installed)
        # self.timer_check_install.start(1000)

        self.first_time_get_conda_env = True
        # self.dict_mapping 是一个所有参数/控件的字典, 循环此字典, 并pop installer 的字典, 如果installer中存在控件参数, 则置控件的值, 否则置为空/默认样式
        self.dict_mapping = {
            'python_file_path': [self.le_input_py_file_path, self.update_option_display_line_edit],
            'output_methode': [self.rb_output_form_file, self.update_option_display_radio_button],
            'specpath': [self.pb_specpath, self.update_option_display_push_buttons],
            'output_file_name': [self.le_output_file_name, self.update_option_display_line_edit],
            'contents_directory': [self.rb_output_form_folder, self.update_option_display_radio_button],
            'add_file_folder_data': [self.pb_add_file_folder_data, self.update_option_display_push_buttons],
            'add_binary_data': [self.pb_add_binary_data, self.update_option_display_push_buttons],
            'imports_paths': [self.pb_imports_paths, self.update_option_display_push_buttons],
            'hidden_import': [self.pb_hidden_import, self.update_option_display_push_buttons],
            'collect_submodules': [self.pb_collect_submodules, self.update_option_display_push_buttons],
            'collect_data': [self.pb_collect_data, self.update_option_display_push_buttons],
            'collect_binaries': [self.pb_collect_binaries, self.update_option_display_push_buttons],
            'collect_all': [self.pb_collect_all, self.update_option_display_push_buttons],
            'copy_metadata': [self.pb_copy_metadata, self.update_option_display_push_buttons],
            'recursive_copy_metadata': [self.pb_recursive_copy_metadata, self.update_option_display_push_buttons],
            'additional_hooks_dir': [self.pb_additional_hooks_dir, self.update_option_display_push_buttons],
            'runtime_hook': [self.pb_runtime_hook, self.update_option_display_push_buttons],
            'exclude_module': [self.pb_exclude_module, self.update_option_display_push_buttons],
            'add_splash_screen': [self.pb_add_splash_screen, self.update_option_display_push_buttons],
            'debug_mode': [self.pb_debug_mode, self.update_option_display_push_buttons],
            'python_option': [self.pb_python_option, self.update_option_display_push_buttons],
            'strip_option': [self.cb_strip_option, self.update_option_display_check_box],
            'noupx_option': [self.cb_noupx_option, self.update_option_display_check_box],
            'upx_exclude': [self.pb_upx_exclude, self.update_option_display_push_buttons],
            'console_window_control': [self.rb_exe_console_display_show, self.update_option_display_radio_button],
            'hide_console': [self.cb_hide_console, self.update_option_display_check_box],
            'add_icon': [self.le_output_exe_icon, self.update_option_display_line_edit],
            'disable_traceback': [self.cb_disable_traceback, self.update_option_display_check_box],
            'version_file': [self.le_output_exe_version, self.update_option_display_line_edit],
            'add_xml_file': [self.pb_add_xml_file, self.update_option_display_push_buttons],
            'add_resource': [self.pb_add_resource, self.update_option_display_push_buttons],
            'uac_admin_apply': [self.cb_uac_admin_apply, self.update_option_display_check_box],
            'uac_uiaccess': [self.cb_uac_uiaccess, self.update_option_display_check_box],
            'argv_emulation': [self.cb_argv_emulation, self.update_option_display_check_box],
            'osx_bundle_identifier': [self.pb_osx_bundle_identifier, self.update_option_display_push_buttons],
            'target_architecture': [self.pb_target_architecture, self.update_option_display_push_buttons],
            'codesign_identity': [self.pb_codesign_identity, self.update_option_display_push_buttons],
            'osx_entitlements_file': [self.pb_osx_entitlements_file, self.update_option_display_push_buttons],
            'runtime_tmpdir': [self.pb_runtime_tmpdir, self.update_option_display_push_buttons],
            'ignore_signals': [self.cb_ignore_signals, self.update_option_display_check_box],
            'output_folder_path': [self.le_output_folder_path, self.update_option_display_line_edit],
            'workpath_option': [self.pb_workpath_option, self.update_option_display_push_buttons],
            'noconfirm_option': [self.cb_noconfirm_option, self.update_option_display_check_box],
            'upx_dir': [self.pb_upx_dir, self.update_option_display_push_buttons],
            'clean_cache': [self.cb_clean_cache, self.update_option_display_check_box],
            'log_level': [self.pb_log_level, self.update_option_display_push_buttons]
        }

    def init_ui(self):
        self.init_ui_frame()
        self.update_ui_style()
        self.set_widgets_language()
        # self.update_installer_display_info()

    def init_ui_frame(self):
        # 命令行显示控件初始化
        self.tb_command_display = ControlTextBrowser(
            flag_button_in_textbrowser=True, font_size=self.setting['tb_command_line_font_size'], default_font_size=DEFAULT_SETTING['tb_command_line_font_size'][1], flag_traceback_display=True)
        layout_command_display = QVBoxLayout(self.wdg_tb_command_display)
        layout_command_display.setContentsMargins(0, 0, 0, 0)
        layout_command_display.addWidget(self.tb_command_display)

        # 控制台显示控件初始化
        self.tb_console = ControlTextBrowser(
            flag_button_in_textbrowser=True, font_size=self.setting['tb_command_line_font_size'], default_font_size=DEFAULT_SETTING['tb_console_font_size'][1], flag_traceback_display=True)
        layout_console = QVBoxLayout(self.wdg_tb_console)
        layout_console.setContentsMargins(0, 0, 0, 0)
        layout_console.addWidget(self.tb_console)

        # 菜单按钮初始化
        list_menu_buttons = [
            self.pb_page_basic, self.pb_page_advance, self.pb_page_ios_win, self.pb_page_info, self.pb_page_console,
            self.pb_page_command, self.pb_page_setting, self.pb_show_tutorial,  self.pb_open_output_folder,
            self.pb_output_command
        ]

        self.widget_menu.setMaximumWidth(pb_size + 24)
        # self.lb_exe_icon.setPixmap(self.pixmap_from_svg(ICON_WIN).scaled(pb_size, pb_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        # self.lb_exe_icon.setFixedSize(pb_size, pb_size)
        for button in list_menu_buttons:
            button.setMinimumSize(pb_size, pb_size)
            button.setMaximumSize(pb_size, pb_size)
            button.setIconSize(QSize(pb_size-icon_padding, pb_size-icon_padding))
        self.lb_reset_all_params.setMinimumSize(pb_size, pb_size)
        self.lb_reset_all_params.setMaximumSize(pb_size, pb_size)
        filter_reset_all_parameters = LabelLeftDoubleOrLangPressFilter(self, self.lb_reset_all_params)
        filter_reset_all_parameters.signal_doublePress_longPress.connect(self.reset_parameters)
        self.lb_reset_all_params.installEventFilter(filter_reset_all_parameters)

        # 主页图标初始化
        list_icon = [self.lb_output_exe_icon_icon, self.lb_input_py_file_icon,
                     self.lb_output_file_name_icon, self.lb_output_exe_version_icon, self.lb_output_folder_path_icon]

        for icon in list_icon:
            icon.setMinimumSize(lb_icon_size, lb_icon_size)
            icon.setMaximumSize(lb_icon_size, lb_icon_size)
            icon.setScaledContents(True)
            icon.setPixmap(self.pixmap_from_svg(ICON_MENU_BTN_HOMEPAGE))

        self.le_env_specified_path_page_setting_env.setClearButtonEnabled(True)
        self.le_input_py_file_path.setClearButtonEnabled(True)
        self.le_output_exe_icon.setClearButtonEnabled(True)
        self.le_output_file_name.setClearButtonEnabled(True)
        self.le_output_folder_path.setClearButtonEnabled(True)
        self.le_output_exe_version.setClearButtonEnabled(True)

        # 命令参数表格初始化
        self.tbwdg_info.setColumnWidth(0, 150)
        self.tbwdg_info.setColumnWidth(1, 150)
        self.tbwdg_info.horizontalHeader().setMinimumSectionSize(_TABLE_WIDGET_COLUMN_MIN_WIDTH)
        self.tbwdg_info.setColumnCount(3)
        header = self.tbwdg_info.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        header.setStretchLastSection(True)
        self.tbwdg_env_conda.resizeColumnsToContents()
        self.tbwdg_env_conda.setColumnCount(5)
        self.tbwdg_env_conda.setColumnWidth(0, 100)
        self.tbwdg_env_conda.setColumnWidth(1, 100)
        self.tbwdg_env_conda.setColumnWidth(2, 500)
        self.tbwdg_env_conda.setColumnWidth(3, 100)
        self.tbwdg_env_conda.setColumnWidth(4, 500)
        self.tbwdg_env_conda.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tbwdg_env_conda.horizontalHeader().setMinimumSectionSize(_TABLE_WIDGET_COLUMN_MIN_WIDTH)
        self.tbwdg_env_conda.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.tbwdg_env_conda.horizontalHeader().setStretchLastSection(True)
        self.tbwdg_env_conda.setSelectionBehavior(QTableWidget.SelectRows)
        self.tbwdg_env_conda.setSelectionMode(QTableWidget.SingleSelection)
        self.tbwdg_env_conda.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tbwdg_env_conda.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.env_btn_group = QButtonGroup()
        self.env_btn_group.addButton(self.rb_env_sys)
        self.env_btn_group.addButton(self.rb_env_specified)
        self.env_btn_group.addButton(self.rb_env_conda)
        self.env_btn_group.addButton(self.rb_env_builtin)

        filter_env_current_install_page_base = LabelLeftDoubleToInstallFilter(self, self.lb_env_current_check_install_page_base, self.data_manager.env_current)
        filter_env_current_install_page_setting_env = LabelLeftDoubleToInstallFilter(self, self.lb_env_current_check_install_page_setting_env, self.data_manager.env_current)
        filter_env_specified_install_page_setting_env = LabelLeftDoubleToInstallFilter(self, self.lb_env_specified_check_install_page_setting_env, self.data_manager.env_specified)
        filter_env_sys_install_page_setting_env = LabelLeftDoubleToInstallFilter(self, self.lb_env_sys_check_install_page_setting_env, self.data_manager.env_sys)
        filter_env_conda_install_page_setting_env = LabelLeftDoubleToInstallFilter(self, self.lb_env_conda_check_install_page_setting_env, self.data_manager.env_conda)
        filter_env_current_install_page_base.signal_textbrowser_LDFilter.connect(self.tb_console.append_text)
        filter_env_current_install_page_setting_env.signal_textbrowser_LDFilter.connect(self.tb_console.append_text)
        filter_env_specified_install_page_setting_env.signal_textbrowser_LDFilter.connect(self.tb_console.append_text)
        filter_env_sys_install_page_setting_env.signal_textbrowser_LDFilter.connect(self.tb_console.append_text)
        filter_env_conda_install_page_setting_env.signal_textbrowser_LDFilter.connect(self.tb_console.append_text)

        self.lb_env_current_check_install_page_base.installEventFilter(filter_env_current_install_page_base)
        self.lb_env_current_check_install_page_setting_env.installEventFilter(filter_env_current_install_page_setting_env)
        self.lb_env_specified_check_install_page_setting_env.installEventFilter(filter_env_specified_install_page_setting_env)
        self.lb_env_sys_check_install_page_setting_env.installEventFilter(filter_env_sys_install_page_setting_env)
        self.lb_env_conda_check_install_page_setting_env.installEventFilter(filter_env_conda_install_page_setting_env)

        self.wdg_progressbar.hide()
        self.wdg_save_setting.hide()
        self.widget_exe_info.hide()

    def update_ui_style(self):
        # 菜单栏按钮图标
        self.pb_page_basic.setIcon(QIcon(self.pixmap_from_svg(ICON_MENU_BTN_HOMEPAGE)))
        self.pb_page_advance.setIcon(QIcon(self.pixmap_from_svg(ICON_MENU_BTN_ADVANCE)))
        self.pb_page_ios_win.setIcon(QIcon(self.pixmap_from_svg(ICON_MENU_BTN_IOS_WIN)))
        self.pb_page_info.setIcon(QIcon(self.pixmap_from_svg(ICON_MENU_BTN_INFO)))
        self.pb_page_console.setIcon(QIcon(self.pixmap_from_svg(ICON_MENU_BTN_CONSOLE)))
        self.pb_page_command.setIcon(QIcon(self.pixmap_from_svg(ICON_MENU_BTN_COMMAND)))
        self.pb_show_tutorial.setIcon(QIcon(self.pixmap_from_svg(ICON_TUTORIAL)))
        self.pb_page_setting.setIcon(QIcon(self.pixmap_from_svg(ICON_MENU_BTN_SETTING)))

        # 执行按钮图标
        self.lb_reset_all_params.setPixmap(self.pixmap_from_svg(ICON_RESET_ALL_PARAMETERS).scaled(
            self.lb_reset_all_params.width(), self.lb_reset_all_params.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.lb_reset_all_params.setContentsMargins(4, 4, 4, 4)
        self.lb_reset_all_params.setStyleSheet('QLabel{ border: 2px solid; border-radius: 5px; border-color: #000000; }')
        self.pb_open_output_folder.setIcon(QIcon(self.pixmap_from_svg(ICON_OPEN_FOLDER)))
        self.pb_output_command.setIcon(QIcon(self.pixmap_from_svg(ICON_OUTPUT_COMMAND)))
        self.pb_launch.setIcon(QIcon(self.pixmap_from_svg(ICON_LAUNCH)))

    def set_widgets_language(self):
        self.tbwdg_env_conda.setHorizontalHeaderLabels(['环境名', '版本号', 'Python解释器路径', 'Pyinstaller路径', 'Pyinstaller版本'])
        self.tbwdg_info.setHorizontalHeaderLabels(["命令名称", "命令选项", "命令值"])

    def init_signal_connections(self):
        # 换页面按钮
        self.pb_page_basic.clicked.connect(self.page_change)
        self.pb_page_advance.clicked.connect(self.page_change)
        self.pb_page_ios_win.clicked.connect(self.page_change)
        self.pb_page_info.clicked.connect(self.page_change)
        self.pb_page_console.clicked.connect(self.page_change)
        self.pb_page_command.clicked.connect(self.page_change)
        self.pb_page_setting.clicked.connect(self.page_change)
        self.pb_open_output_folder.clicked.connect(self.open_output_folder)
        self.pb_output_command.clicked.connect(self.print_command_line)
        # 命令行字体大小
        self.tb_command_display.signal_font_size.connect(self.record_font_change_in_tb_command_line)
        self.tb_console.signal_font_size.connect(self.record_font_change_in_tb_console)
        # setting页面
        self.pb_env_sys_edit_page_setting_env.clicked.connect(self.open_env_variant)
        self.pb_env_specified_browser_page_setting_env.clicked.connect(self.set_env_specified_path)
        self.tbwdg_env_conda.customContextMenuRequested.connect(self.show_conda_tabelwidget_context_menu)
        # self.tbwdg_env_conda.itemSelectionChanged.connect(lambda: self.update_env_conda_specified(isWithSelectUpdate=True))
        # self.rb_env_sys.clicked.connect(lambda: self.update_env_sys(isWithSelectUpdate=True))
        # self.rb_env_specified.clicked.connect(lambda: self.update_env_specified(isWithSelectUpdate=True))
        # self.rb_env_conda.clicked.connect(lambda: self.update_env_conda_specified(isWithSelectUpdate=True))
        # self.rb_env_builtin.clicked.connect(self.select_python_env)
        # self.le_env_specified_path_page_setting_env.textChanged.connect(lambda: self.update_env_specified(isWithSelectUpdate=True))
        self.executor_info_manager.signal_data_changed_EIM.connect(self.piii)

    def piii(self):
        # for i, v in self.executor_info_manager.executor_struct_dict.items():
        #     print(i, v)
        self.set_value_in_table_widget_env_conda(self.executor_info_manager.conda_struct_dict)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonDblClick and obj is not None:
            if event.button() == Qt.LeftButton:
                self.callback()  # 调用回调函数
        return super().eventFilter(obj, event)

    def resizeEvent(self, event):
        tbwdg_env_conda_row_width_4 = self.tbwdg_env_conda.columnWidth(4)
        if tbwdg_env_conda_row_width_4 > 600:
            self.tbwdg_env_conda.setColumnWidth(4, 600)
        super().resizeEvent(event)

    def page_change(self):
        """ 页面切换 """
        sender = self.sender()
        dict_sender = {
            self.pb_page_basic: lambda: self.stackedWidget.setCurrentWidget(self.page_base),
            self.pb_page_advance: lambda: self.stackedWidget.setCurrentWidget(self.page_advance),
            self.pb_page_ios_win: lambda: self.stackedWidget.setCurrentWidget(self.page_ios_win),
            self.pb_page_info: lambda: self.stackedWidget.setCurrentWidget(self.page_info),
            self.pb_page_console: lambda: self.stackedWidget.setCurrentWidget(self.page_console),
            self.pb_page_command: lambda: self.stackedWidget.setCurrentWidget(self.page_command_display),
            self.pb_page_setting: lambda: self.stackedWidget.setCurrentWidget(self.page_setting)
        }
        dict_sender[sender]()
        self.widget_menu.setStyleSheet(f""" #{sender.objectName()} {{background-color: {_MENU_FOCUS_BG_COLOR};}} """)

    def pixmap_from_svg(self, svg_str: str):
        """
        将svg字符串转换为QPixmap

        参数:
        - svg_str(str):svg字符串

        返回:
        - QPixmap:QPixmap对象
        """
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(svg_str.encode()))
        return pixmap

    def change_svg_fill_color(self, input_svg_str: str, new_fill_color: str) -> str:
        """
        更改 SVG 中的样式颜色.

        参数:
        - input_svg_str(str):输入的 SVG 字符串.
        - new_fill_color(str):新的颜色, RGB 格式, 注意写 '#'.

        返回值:
        - svg_string(str):修改颜色后的 SVG 字符串.
        """

        string_list = input_svg_str.split("style=\"fill:")
        if (len(string_list) > 1):
            for i in range(1, len(string_list)):
                fill_end_index = string_list[i].find("\"")
                if (fill_end_index != -1):
                    string_list[i] = new_fill_color + string_list[i][fill_end_index:]
        return 'style="fill:'.join(string_list)

    def update_installer_display_info(self):
        """ 显示安装器信息 """
        self.update_table_widget_installer_info()
        # self.update_command_display()
        # self.update_options_display() # 不是每次都需要, 只是在读文件的时候需要

    def update_table_widget_installer_info(self):
        """ 更新安装器信息 """
        tooltip = '00000126456132'
        self.installer.add_icon.set_args('E:')
        self.installer.imports_paths.append_args('F:')
        self.installer.imports_paths.append_args('F:\\test')
        self.installer_dict = self.installer.get_flattened_struct_command_args()
        length = self.installer_dict['length']
        data: dict = self.installer_dict['data']
        self.tbwdg_info.clear()
        self.tbwdg_info.setRowCount(length)

        index = 0
        for key, item in data.items():
            key: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct
            # name = getattr(self.language, f'{key.name}.display_text')
            # tooltip = getattr(self.language, f'{key.name}.tool_tip')
            name = key.name
            if isinstance(key, StateStruct) and not key.isWithOption:
                option = key.current_state
            elif isinstance(key.command_option, list):
                option = key.command_option[0]
            else:
                option = key.command_option
            item_name = QTableWidgetItem(name)
            item_option = QTableWidgetItem(option)
            self.tbwdg_info.setItem(index, 0, item_name)
            self.tbwdg_info.setItem(index, 1, item_option)
            item_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item_option.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item_name.setToolTip(tooltip)
            item_option.setToolTip(tooltip)
            if isinstance(item, list):
                sub_index = 0
                for sub_item in item:
                    item_command = QTableWidgetItem(sub_item)
                    item_command.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    if sub_index > 0:
                        item_blank_0 = QTableWidgetItem('')
                        item_blank_1 = QTableWidgetItem('')
                        item_blank_0.setFlags(Qt.NoItemFlags)
                        item_blank_1.setFlags(Qt.NoItemFlags)
                        self.tbwdg_info.setItem(index, 0, item_blank_0)
                        self.tbwdg_info.setItem(index, 1, item_blank_1)
                    self.tbwdg_info.setItem(index, 2, item_command)
                    index += 1
                    sub_index += 1
            else:
                item_command = QTableWidgetItem(item)
                if item:
                    item_command.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                else:
                    item_command.setFlags(Qt.NoItemFlags)
                self.tbwdg_info.setItem(index, 2, item_command)
                index += 1

    def update_command_display(self):
        """ 更新命令显示 """
        self.tb_command_display.clear()
        # command_line = self.installer.get_command_line(self.env_struct_current.path_pyinstaller)
        # if command_line:
        #     self.tb_command_display.set_text(command_line)

    def update_options_display(self):
        """ 
        通过 self.installer 更新界面中选项显示
        """
        self.installer = self.data_manager.pyinstaller_struct
        dict_installer: dict = self.installer.get_command_dict()
        for key, item in self.dict_mapping.items():
            target_item = dict_installer.pop(key, None)
            item[1](item[0], target_item)

    def update_option_display_push_buttons(self, widget: QPushButton, command: str):
        """ 更新选项显示按钮 """
        if not command:
            widget.setStyleSheet('')
            return
        widget.setStyleSheet('QPushButton{background-color: red}')

    def update_option_display_radio_button(self, widget: QRadioButton, command: str):
        """ 更新选项显示单选按钮 """
        if widget in (self.rb_output_form_file, self.rb_output_form_folder):
            if command in ('--onedir', '-D'):
                self.rb_output_form_folder.setChecked(True)
                if widget == self.rb_output_form_folder:
                    pass  # 此处添加样式, 区分已输入指定输出打包文件夹
            else:
                self.rb_output_form_file.setChecked(True)  # 默认样式
        elif widget in (self.rb_exe_console_display_show, self.rb_exe_console_display_hide):
            if command in ('--windowed', '--noconsole', '-w'):
                self.rb_exe_console_display_hide.setChecked(True)
            else:
                self.rb_exe_console_display_show.setChecked(True)  # 默认样式
        else:
            print('[控件错误] 请检查控件')

    def update_option_display_check_box(self, widget: QCheckBox, command: str):
        """ 更新选项显示复选框 """
        if command:
            widget.setChecked(True)
        else:
            widget.setChecked(False)  # 默认样式

    def update_option_display_line_edit(self, widget: QLineEdit, command: str):
        """ 更新选项显示单行文本框 """
        if command:
            if '"' in command:
                temp_list = command.split('"')
                if len(temp_list) > 1:
                    command = temp_list[1].strip('"')
            widget.setText(command)
        else:
            widget.clear()

    def open_output_folder(self):
        """ 打开输出文件夹 """
        try:
            exe_path = os.path.join(self.installer.output_folder_path.command_args, self.installer.output_file_name.command_args+'.exe')
            if os.path.exists(exe_path):
                Popen(['explorer', '/select,', os.path.normpath(exe_path)], creationflags=CREATE_NO_WINDOW)  # 注意这里如果不norm一下, 会找不到路径
            elif os.path.exists(self.installer.output_folder_path.command_args):
                Popen(['explorer', os.path.normpath(self.installer.output_folder_path.command_args)], creationflags=CREATE_NO_WINDOW)
            else:
                self.message.notification(f'输出文件夹不存在: {self.installer.output_folder_path.command_args}')
                self.tb_console.append_text(f'输出文件夹不存在: {self.installer.output_folder_path.command_args}')
        except Exception as e:
            # self.tb_console.append_text(format_exc())
            # print(format_exc())
            pass

    def print_command_line(self):
        """ 打印命令行 """
        output_file_name = f'[command_line]-{self.installer.output_file_name.command_args}' + '.txt'
        output_file_path = os.path.normpath(os.path.join(self.installer.output_folder_path.command_args, output_file_name))
        # if command_line := self.installer.get_command_line(self.env_struct_current.path_pyinstaller):
        #     with open(output_file_path, 'w', encoding='utf-8') as f:
        #         f.write(command_line)
        #     if self.setting['auto_open_printed_command_line_folder']:
        #         Popen(['explorer', '/select,', output_file_path], creationflags=CREATE_NO_WINDOW)
        #     if self.setting['auto_open_printed_command_line_file']:
        #         Popen(['explorer', output_file_path], creationflags=CREATE_NO_WINDOW)
        #     self.tb_console.append_text(f'[{time.localtime()}]\n命令行已打印到: {output_file_path}')
        #     self.message.notification(f'命令行已打印到', open_file_path=output_file_path)

    def record_font_change_in_tb_console(self, font_size):
        """
        记录控制台显示字体大小

        参数:
        - font_size (int): 字体大小

        应用:
        与 self.tb_console(ControlTextBrowser).signal_font_size 信号连接
        """
        self.setting['tb_console_font_size'] = font_size
        self.setting_manager.save_settings()

    def record_font_change_in_tb_command_line(self, font_size):
        """
        记录命令行显示字体大小

        参数:
        - font_size (int): 字体大小

        应用:
        与 self.tb_command_display(ControlTextBrowser).signal_font_size 信号连接
        """
        self.setting['tb_command_line_font_size'] = font_size
        self.setting_manager.save_settings()

    def open_env_variant(self):
        """
        打开环境变量
        """
        sprun('rundll32 sysdm.cpl,EditEnvironmentVariables')

    # def start_python_conda_detection(self):
    #     """
    #     开始检测 系统Python环境 与 conda环境
    #     """
    #     self.thread_python_conda_detection = PythonCondaEnvDetection(self)
    #     self.thread_python_conda_detection.signal_python_path.connect(self.get_sys_python_env_from_detection_thread)
    #     self.thread_python_conda_detection.signal_env_conda_list.connect(self.get_env_conda_from_detection_thread)
    #     self.thread_python_conda_detection.signal_finished.connect(self.finished_thread_python_conda_detection)
    #     self.thread_python_conda_detection.start()
    #     self.thread_python_conda_detection.signal_env_conda_list.connect(self.get_env_conda_from_detection_thread)
    #     self.timer_check_conda_env.timeout.connect(self.thread_python_conda_detection.start)
    #     self.timer_check_conda_env.start(2000)  # 开始循环检测 Conda环境,  Python环境将有 self.update_env_sys() 检测

    def get_sys_python_env_from_detection_thread(self, env_list: list):
        """
        更新Python环境, 由线程传入
        """
        version = env_list[0]
        py_path = env_list[1]
        # self.env_struct_sys.env_name = f'<系统环境> {version}'
        # self.env_struct_sys.version = version
        # self.env_struct_sys.path_python = py_path
        self.lb_env_sys_name_page_setting_env.setText(version)
        self.lb_env_sys_path_page_setting_env.setText(py_path)

    # def set_local_python

    def set_value_in_table_widget_env_conda(self, env_dict: dict):
        """
        conda环境列表 写入到 tableWidget

        列表格式: {base: ['base', 'C:/Users/.../miniconda3/python.exe', '3.11.5', 'C:/Users/.../miniconda3/Scripts/pyinstaller.exe', '6.3.0']}
        """
        # 获取起始的位置和选项
        last_scrollbar_value = self.tbwdg_env_conda.verticalScrollBar().value()
        if item := self.tbwdg_env_conda.item(self.tbwdg_env_conda.currentRow(), 0):
            last_env_name = item.text()
        else:
            last_env_name = ''
        target_row = -1
        self.tbwdg_env_conda.clear()
        self.tbwdg_env_conda.setRowCount(len(env_dict))
        self.tbwdg_env_conda.setHorizontalHeaderLabels(['环境名', '版本号', 'Python解释器路径', 'Pyinstaller路径', 'Pyinstaller版本'])
        # 遍历字典, 添加项目
        for index, (key, struct) in enumerate(env_dict.items()):
            struct: ExecutorInfoStruct
            if key == last_env_name:
                target_row = index
            item_name = QTableWidgetItem(struct.name)
            item_name.setToolTip(struct.name)
            item_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_python_version = QTableWidgetItem(struct.python_version)
            item_python_version.setToolTip(struct.python_version)
            item_python_version.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_python_path = QTableWidgetItem(struct.python_path.replace('\\', '\\ '))
            item_python_path.setToolTip(struct.python_path)
            item_python_path.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_pyinstaller_path = QTableWidgetItem(struct.pyinstaller_path)
            item_pyinstaller_path.setToolTip(struct.pyinstaller_path)
            item_pyinstaller_path.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_pyinstaller_version = QTableWidgetItem(struct.pyinstaller_version)
            item_pyinstaller_version.setToolTip(struct.pyinstaller_version)
            item_pyinstaller_version.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            self.tbwdg_env_conda.setItem(index, 0, item_name)
            self.tbwdg_env_conda.setItem(index, 1, item_python_version)
            self.tbwdg_env_conda.setItem(index, 2, item_python_path)
            self.tbwdg_env_conda.setItem(index, 3, item_pyinstaller_version)
            self.tbwdg_env_conda.setItem(index, 4, item_pyinstaller_path)
        # 复原滚动条位置和选项
        if target_row >= 0:
            self.tbwdg_env_conda.selectRow(target_row)
            self.tbwdg_env_conda.verticalScrollBar().setValue(last_scrollbar_value)
        else:
            self.tbwdg_env_conda.selectRow(0)

    # def finished_thread_python_conda_detection(self):
    #     self.update_env_sys()
    #     self.update_env_conda_specified(isWithSelectUpdate=True)

    def show_conda_tabelwidget_context_menu(self, pos: QPoint) -> None:
        """
        显示 Conda环境 右键菜单
        """
        mouse_item = self.tbwdg_env_conda.itemAt(pos)
        if not mouse_item:
            return
        row = mouse_item.row()
        col = mouse_item.column()

        menu = QMenu(self)
        action_copy = QAction(f'复制Python解释器路径', self)
        action_copy.triggered.connect(lambda: self.copy_python_interpreter_path(self.tbwdg_env_conda.item(row, 2).text()))
        action_open_python_folder = QAction(f'打开python所在文件夹', self)
        action_open_python_folder.triggered.connect(lambda: Popen(f'explorer /select,"{self.tbwdg_env_conda.item(row, 2).text()}"', creationflags=CREATE_NO_WINDOW))
        action_open_pyinstaller_folder = QAction(f'打开PyInstaller所在文件夹', self)
        action_open_pyinstaller_folder.triggered.connect(lambda: Popen(f'explorer /select,"{self.tbwdg_env_conda.item(row, 3).text()}"', creationflags=CREATE_NO_WINDOW))
        menu.addAction(action_copy)
        menu.addAction(action_open_python_folder)
        menu.addAction(action_open_pyinstaller_folder)
        menu.exec_(self.tbwdg_env_conda.mapToGlobal(pos))

    def copy_python_interpreter_path(self, text: str) -> None:
        """
        复制python解释器路径
        """
        self.clipboard.setText(text)
        self.message.notification(f'已复制: {text}')

    # def update_env_sys(self, isWithSelectUpdate: bool = False) -> None:
    #     """
    #     更新 系统Python 是否安装pyinstaller

    #     参数:
    #     - isWithSelectUpdate (bool): 是否更新选中项, 含函数初调用 self.reset_style_specified() 来重置 specified 样式重置, 函数尾调用 self.select_python_env() 来更新界面当前选中项
    #     """
    #     def update_installed_display(flag: bool):
    #         if flag:
    #             self.lb_env_sys_check_install_page_setting_env.setStyleSheet('background-color: rgb(0, 200, 0); color: rgb(0, 0, 0);')
    #             self.lb_env_sys_check_install_page_setting_env.setText('pyinstaller\n已安装')
    #             self.lb_env_sys_check_install_page_setting_env.setCursor(Qt.CursorShape.ArrowCursor)
    #             if not self.env_struct_sys.path_pyinstaller or not os.path.exists(self.env_struct_sys.path_pyinstaller):
    #                 self.env_struct_sys.path_pyinstaller = find_pyinstaller_path(self.env_struct_sys.path_python)
    #         else:
    #             self.lb_env_sys_check_install_page_setting_env.setStyleSheet('background-color: rgb(200, 0, 0); color: rgb(200, 200, 200);')
    #             self.lb_env_sys_check_install_page_setting_env.setText('pyinstaller\n未安装')
    #             self.lb_env_sys_check_install_page_setting_env.setCursor(Qt.CursorShape.PointingHandCursor)
    #             self.env_struct_sys.path_pyinstaller = ''
    #         if isWithSelectUpdate:
    #             self.select_python_env()
    #     if isWithSelectUpdate:
    #         self.reset_style_specified()
    #     py_path = self.lb_env_sys_path_page_setting_env.text()
    #     self.thread_sys_python_pyinstaller_check = PyinstallerCheck(self, py_path)
    #     self.thread_sys_python_pyinstaller_check.signal_pyinstaller_installed.connect(update_installed_display)
    #     self.thread_sys_python_pyinstaller_check.start()
    #     # wait_for_thread_result(self.thread_sys_python_pyinstaller_check.signal_pyinstaller_installed)

    # def update_env_conda_specified(self, isWithSelectUpdate: bool = False) -> None:
    #     """
    #     更新 指定conda环境 是否安装pyinstaller

    #     参数:
    #     - isWithSelectUpdate (bool): 是否更新选中项, 含函数初调用 self.reset_style_specified() 来重置 specified 样式重置, 函数尾调用 self.select_python_env() 来更新界面当前选中项
    #     """
    #     current_row = self.tbwdg_env_conda.currentRow()
    #     if current_row == -1:
    #         return
    #     column_env_name = 0
    #     column_env_version = 1
    #     column_python_path = 2
    #     column_pyinstaller_path = 3
    #     item_env_name = self.tbwdg_env_conda.item(current_row, column_env_name)
    #     item_env_version = self.tbwdg_env_conda.item(current_row, column_env_version)
    #     item_python_path = self.tbwdg_env_conda.item(current_row, column_python_path)
    #     item_pyinstaller_path = self.tbwdg_env_conda.item(current_row, column_pyinstaller_path)
    #     if item_python_path:
    #         if isWithSelectUpdate:
    #             self.reset_style_specified()
    #         python_path = item_python_path.text()
    #         self.lb_env_conda_path_page_setting_env.setText(python_path)
    #         self.env_struct_conda.env_name = item_env_name.text()
    #         self.env_struct_conda.version = item_env_version.text()
    #         self.env_struct_conda.path_python = python_path
    #         self.env_struct_conda.path_pyinstaller = item_pyinstaller_path.text()
    #         if self.env_struct_conda.path_pyinstaller:
    #             self.env_struct_conda.path_pyinstaller = item_pyinstaller_path.text()
    #             self.lb_env_conda_check_install_page_setting_env.setStyleSheet('background-color: rgb(0, 200, 0); color: rgb(0, 0, 0);')
    #             self.lb_env_conda_check_install_page_setting_env.setText('pyinstaller\n已安装')
    #             self.lb_env_conda_check_install_page_setting_env.setCursor(Qt.CursorShape.ArrowCursor)
    #         else:
    #             self.env_struct_conda.path_pyinstaller = ''
    #             self.lb_env_conda_check_install_page_setting_env.setStyleSheet('background-color: rgb(200, 0, 0); color: rgb(200, 200, 200);')
    #             self.lb_env_conda_check_install_page_setting_env.setText('pyinstaller\n未安装')
    #             self.lb_env_conda_check_install_page_setting_env.setCursor(Qt.CursorShape.PointingHandCursor)
    #         if isWithSelectUpdate:
    #             self.select_python_env()

    # def update_env_specified(self, isWithSelectUpdate: bool = False):
    #     """
    #     更新 指定路径 是否安装pyinstaller

    #     参数:
    #     - isWithSelectUpdate (bool): 是否更新选中项, 函数尾调用 self.select_python_env() 来更新界面当前选中项
    #     """
    #     self.le_env_specified_path_page_setting_env.setStyleSheet('')
    #     self.lb_env_specified_hint_info_page_setting_env.clear()
    #     python_path = self.le_env_specified_path_page_setting_env.text()
    #     # 去掉前后引号
    #     if (python_path.startswith(('"', '"')) and python_path.endswith(('"', '"'))):
    #         python_path = python_path[1:-1]
    #         self.le_env_specified_path_page_setting_env.setText(python_path)
    #     # 判断是否存在python解释器, 路径是否正确
    #     if os.path.exists(python_path) and python_path.endswith('python.exe'):
    #         self.env_struct_specified.path_python = python_path
    #         self.env_struct_specified.path_pyinstaller = find_pyinstaller_path(python_path)
    #         self.env_struct_specified.path_error = False
    #         if self.rb_env_specified.isChecked():
    #             self.thread_get_python_version_specified = GetPythonVersion(python_path)
    #             self.thread_get_python_version_specified.start()
    #             self.env_struct_specified.version = wait_for_thread_result(self.thread_get_python_version_specified.signal_python_version, '')
    #             self.env_struct_specified.env_name = f'<指定环境> {self.env_struct_specified.version}'
    #         if self.env_struct_specified.path_pyinstaller:
    #             self.lb_env_specified_check_install_page_setting_env.setStyleSheet('background-color: rgb(0, 200, 0); color: rgb(0, 0, 0);')
    #             self.lb_env_specified_check_install_page_setting_env.setText('pyinstaller\n已安装')
    #             self.lb_env_specified_check_install_page_setting_env.setCursor(Qt.CursorShape.ArrowCursor)
    #         else:
    #             self.lb_env_specified_check_install_page_setting_env.setStyleSheet('background-color: rgb(200, 0, 0); color: rgb(200, 200, 200);')
    #             self.lb_env_specified_check_install_page_setting_env.setText('pyinstaller\n未安装')
    #             self.lb_env_specified_check_install_page_setting_env.setCursor(Qt.CursorShape.PointingHandCursor)
    #     else:
    #         self.lb_env_specified_check_install_page_setting_env.setText('')
    #         self.lb_env_specified_check_install_page_setting_env.setStyleSheet('')

    #         self.env_struct_specified.env_name = self.env_struct_sys.env_name
    #         self.env_struct_specified.path_python = self.env_struct_sys.path_python
    #         self.env_struct_specified.path_pyinstaller = self.env_struct_sys.path_pyinstaller
    #         self.env_struct_specified.version = self.env_struct_sys.version
    #         self.env_struct_specified.path_error = True

    #         if self.rb_env_specified.isChecked():
    #             self.le_env_specified_path_page_setting_env.setStyleSheet('QLineEdit{background-color: rgb(255, 100, 0);}')
    #             self.lb_env_specified_hint_info_page_setting_env.setText('<路径不存在, 已使用系统默认路径>')
    #         # else:
    #         #     self.le_env_specified_path_page_setting_env.setStyleSheet('')
    #         #     self.lb_env_specified_hint_info_page_setting_env.clear()
    #     if isWithSelectUpdate:
    #         self.select_python_env()

    # def check_all_env_installed(self):
    #     """
    #     更新所有显示, 并更新当前环境显示
    #     """
    #     self.update_env_specified()
    #     self.update_env_conda_specified()
    #     self.update_env_sys(isWithSelectUpdate=True)

    def reset_style_specified(self):
        if not self.rb_env_specified.isChecked():
            self.le_env_specified_path_page_setting_env.setStyleSheet('')
            self.lb_env_specified_hint_info_page_setting_env.clear()

    def select_python_env(self):
        """
        更新当前选定的python环境显示
        """
        self.update_installer_display_info()

        # if self.rb_env_specified.isChecked():
        #     self.env_struct_current.env_name = self.env_struct_specified.env_name
        #     self.env_struct_current.path_python = self.env_struct_specified.path_python
        #     self.env_struct_current.path_pyinstaller = self.env_struct_specified.path_pyinstaller
        #     self.env_struct_current.version = self.env_struct_specified.version
        #     self.env_struct_current.path_error = self.env_struct_specified.path_error  # 给过滤器用的, 判断是否执行安装, 当指定路径错误时, Label仍存在且可点击, 所以要区分

        # elif self.rb_env_sys.isChecked():
        #     self.env_struct_current.env_name = self.env_struct_sys.env_name
        #     self.env_struct_current.path_python = self.env_struct_sys.path_python
        #     self.env_struct_current.path_pyinstaller = self.env_struct_sys.path_pyinstaller
        #     self.env_struct_current.version = self.env_struct_sys.version
        #     self.env_struct_current.path_error = self.env_struct_specified.path_error

        # elif self.rb_env_conda.isChecked():
        #     self.env_struct_current.env_name = self.env_struct_conda.env_name
        #     self.env_struct_current.path_python = self.env_struct_conda.path_python
        #     self.env_struct_current.path_pyinstaller = self.env_struct_conda.path_pyinstaller
        #     self.env_struct_current.version = self.env_struct_conda.version
        #     self.env_struct_current.path_error = self.env_struct_specified.path_error

        # elif self.rb_env_builtin.isChecked():
        #     self.reset_style_specified()
        #     self.env_struct_current.env_name = '<内置环境>'
        #     self.env_struct_current.path_python = '<buildin> pyinstaller'
        #     self.env_struct_current.path_pyinstaller = None
        #     self.env_struct_current.version = ''
        #     self.env_struct_current.path_error = False

        self.update_env_current_display_and_para()

    def set_env_specified_path(self):
        file_path = QFileDialog.getOpenFileName(self, '选择Python解释器', os.path.expanduser("~"), 'Python解释器 (python.exe)')[0]
        if file_path:
            self.le_env_specified_path_page_setting_env.setText(file_path)

    def update_env_current_display_and_para(self):
        """
        更新Python环境显示, 根据控件选择改变

        更改主页和设置页中的 当前环境 的显示,  包括名称, 路径, 是否安装状态
        """
        self.lb_env_current_name_page_setting_env.clear()
        self.lb_env_current_path_page_setting_env.clear()
        self.lb_env_current_name_page_base.clear()
        self.lb_env_current_path_page_base.clear()
        # self.lb_env_current_name_page_setting_env.setText(self.env_struct_current.env_name)
        # self.lb_env_current_path_page_setting_env.setText(self.env_struct_current.path_python)

        # self.lb_env_current_name_page_base.setText(self.env_struct_current.env_name)
        # self.lb_env_current_path_page_base.setText(self.env_struct_current.path_python)
        # if self.env_struct_current.path_pyinstaller:
        #     self.lb_env_current_check_install_page_setting_env.setText('pyinstaller\n已安装')
        #     self.lb_env_current_check_install_page_setting_env.setStyleSheet('background-color: rgb(0, 200, 0); color: rgb(0, 0, 0);')
        #     self.lb_env_current_check_install_page_setting_env.setCursor(Qt.CursorShape.ArrowCursor)
        #     self.lb_env_current_check_install_page_base.setText('pyinstaller\n已安装')
        #     self.lb_env_current_check_install_page_base.setStyleSheet('background-color: rgb(0, 200, 0); color: rgb(0, 0, 0);')
        #     self.lb_env_current_check_install_page_base.setCursor(Qt.CursorShape.ArrowCursor)
        # elif self.env_struct_current.path_pyinstaller is None:
        #     self.lb_env_current_check_install_page_setting_env.clear()
        #     self.lb_env_current_check_install_page_setting_env.setStyleSheet('')
        #     self.lb_env_current_check_install_page_base.clear()
        #     self.lb_env_current_check_install_page_base.setStyleSheet('')
        # else:
        #     self.lb_env_current_check_install_page_setting_env.setText('pyinstaller\n未安装')
        #     self.lb_env_current_check_install_page_setting_env.setStyleSheet('background-color: rgb(200, 0, 0); color: rgb(200, 200, 200);')
        #     self.lb_env_current_check_install_page_setting_env.setCursor(Qt.CursorShape.PointingHandCursor)
        #     self.lb_env_current_check_install_page_base.setText('pyinstaller\n未安装')
        #     self.lb_env_current_check_install_page_base.setStyleSheet('background-color: rgb(200, 0, 0); color: rgb(200, 200, 200);')
        #     self.lb_env_current_check_install_page_base.setCursor(Qt.CursorShape.PointingHandCursor)

    def reset_parameters_double_click(self):
        # 双击进行重置参数, 参数为 setting 中的
        print('双击')
        # self.installer_manager.read_data(self.setting['last_command'])
        self.update_options_display()

    def reset_parameters_long_pressed(self):
        print('长按')
        # self.installer_manager.read_data(EnumConst.DEFAULT_INSTALLER_COMMANDLINE)
        self.update_options_display()

    def reset_parameters(self, flag: str):
        if flag == 'doublePressed':
            self.reset_parameters_double_click()
        elif flag == 'longPressed':
            self.reset_parameters_long_pressed()
        else:
            pass
