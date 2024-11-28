import enum
import os
from queue import PriorityQueue
from re import L
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

from UI.UI_PyToExe_ui import *
from UI.Widget_Control_TextBrowser import *
from UI.Message_Notification import *
from const.Const_Icon import *
from const.Const_Parameter import *
from system.Manager_Language import *
from system.Manager_Setting import *
from system.Struct_IO import *
from system.Struct_env_info import *
from system.Thread_Conda import *
from system.Thread_Pip_Install import *
from system.Filter_Left_Double import *
from tools.wait_thread import *


from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton, QDialog, QListWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSizePolicy, QFrame, QSpacerItem, QInputDialog, QLabel, QCheckBox, QRadioButton, QListWidgetItem, QTextBrowser, QMainWindow, QTableWidgetItem, QHeaderView, QTableWidget, QMenu, QAction, QTabWidget, QWidget, QScrollArea, QLineEdit, QComboBox, QGroupBox, QGridLayout, QProgressBar, QApplication, QButtonGroup
from PyQt5.QtGui import QTextCursor, QDesktopServices, QIcon, QPixmap
from PyQt5.QtCore import Qt, QUrl, QByteArray, QSize, QItemSelectionModel, QEventLoop, QEvent, QObject
# import pygetwindow as gw

_MENU_FOCUS_BG_COLOR = "#E8E8E8"
_TABLE_WIDGET_COLUMN_MIN_WIDTH = 80


class PyToExeUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_parameters()
        self.init_ui()
        self.init_signal_connections()

    def init_parameters(self):
        self.app_workspace_path = APP_WORKSPACE_PATH
        self.setting_manager = SettingManager(self.app_workspace_path)
        self.setting = self.setting_manager.setting_data
        self.installer_manager = Struct_IO()
        self.installer = self.installer_manager.struct_data
        # self.language = LanguageManager(PATH_APP_FOLDER)
        self.message = MessageNotification(self, position='bottom', offset=100, move_in_point=(None, '50'))
        self.clipboard = QApplication.clipboard()

        self.env_struct_current = StructEnvInfo('current')
        self.env_struct_specified = StructEnvInfo('specified')
        self.env_struct_sys = StructEnvInfo('sys')
        self.env_struct_conda = StructEnvInfo('conda')

        self.timer_check_install = QTimer()
        self.timer_check_install.timeout.connect(self.check_all_env)
        self.timer_check_install.start(1000)
        self.timer_check_env = QTimer()
        self.timer_check_env.timeout.connect(self.check_env)
        self.timer_check_env.start(2000)

    def init_ui(self):
        self.init_ui_frame()
        self.update_ui_style()
        self.update_installer_info()

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
            self.pb_page_command, self.pb_page_setting, self.pb_show_tutorial, self.pb_reset_all_params, self.pb_open_output_folder,
            self.pb_output_command]
        pb_size = 35
        icon_padding = 8
        self.widget_menu.setMaximumWidth(pb_size + 24)
        # self.lb_exe_icon.setPixmap(self.pixmap_from_svg(ICON_WIN).scaled(pb_size, pb_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        # self.lb_exe_icon.setFixedSize(pb_size, pb_size)
        for button in list_menu_buttons:
            button.setMinimumSize(pb_size, pb_size)
            button.setMaximumSize(pb_size, pb_size)
            button.setIconSize(QSize(pb_size-icon_padding, pb_size-icon_padding))

        # 主页图标初始化
        list_icon = [self.lb_output_exe_icon_icon, self.lb_input_py_file_icon,
                     self.lb_output_file_name_icon, self.lb_output_exe_version_icon, self.lb_output_folder_path_icon]
        lb_icon_size = 40
        for icon in list_icon:
            icon.setMinimumSize(lb_icon_size, lb_icon_size)
            icon.setMaximumSize(lb_icon_size, lb_icon_size)
            icon.setScaledContents(True)
            icon.setPixmap(self.pixmap_from_svg(ICON_MENU_BTN_HOMEPAGE))

        # 命令参数表格初始化
        self.tbwdg_info.setColumnWidth(0, 150)
        self.tbwdg_info.setColumnWidth(1, 150)
        self.tbwdg_info.horizontalHeader().setMinimumSectionSize(_TABLE_WIDGET_COLUMN_MIN_WIDTH)
        self.tbwdg_info.setColumnCount(3)
        header = self.tbwdg_info.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        header.setStretchLastSection(True)

        self.tbwdg_env_conda.setColumnCount(4)
        self.tbwdg_env_conda.setColumnWidth(0, 100)
        self.tbwdg_env_conda.setColumnWidth(1, 100)
        self.tbwdg_env_conda.setColumnWidth(2, 300)
        self.tbwdg_env_conda.horizontalHeader().setMinimumSectionSize(_TABLE_WIDGET_COLUMN_MIN_WIDTH)
        self.tbwdg_env_conda.setContextMenuPolicy(Qt.CustomContextMenu)
        conda_header = self.tbwdg_env_conda.horizontalHeader()
        conda_header.setSectionResizeMode(QHeaderView.Interactive)
        conda_header.setStretchLastSection(True)
        self.tbwdg_env_conda.setSelectionBehavior(QTableWidget.SelectRows)
        self.tbwdg_env_conda.setSelectionMode(QTableWidget.SingleSelection)

        self.env_btn_group = QButtonGroup()
        self.env_btn_group.addButton(self.rb_env_sys)
        self.env_btn_group.addButton(self.rb_env_specified)
        self.env_btn_group.addButton(self.rb_env_conda)
        self.env_btn_group.addButton(self.rb_env_builtin)

        env_current_install_page_base = LabelLeftDoubleToInstallFilter(self, self.lb_env_current_check_install_page_base, self.env_struct_current)
        env_current_install_page_setting_env = LabelLeftDoubleToInstallFilter(self, self.lb_env_current_check_install_page_setting_env, self.env_struct_current)
        env_specified_install_page_setting_env = LabelLeftDoubleToInstallFilter(self, self.lb_env_specified_check_install_page_setting_env, self.env_struct_specified)
        env_sys_install_page_setting_env = LabelLeftDoubleToInstallFilter(self, self.lb_env_sys_check_install_page_setting_env, self.env_struct_sys)
        env_conda_install_page_setting_env = LabelLeftDoubleToInstallFilter(self, self.lb_env_conda_check_install_page_setting_env, self.env_struct_conda)
        env_current_install_page_base.signal_textbrowser_LDFilter.connect(self.tb_console.append_text)
        env_current_install_page_setting_env.signal_textbrowser_LDFilter.connect(self.tb_console.append_text)
        env_specified_install_page_setting_env.signal_textbrowser_LDFilter.connect(self.tb_console.append_text)
        env_sys_install_page_setting_env.signal_textbrowser_LDFilter.connect(self.tb_console.append_text)
        env_conda_install_page_setting_env.signal_textbrowser_LDFilter.connect(self.tb_console.append_text)

        self.lb_env_current_check_install_page_base.installEventFilter(env_current_install_page_base)
        self.lb_env_current_check_install_page_setting_env.installEventFilter(env_current_install_page_setting_env)
        self.lb_env_specified_check_install_page_setting_env.installEventFilter(env_specified_install_page_setting_env)
        self.lb_env_sys_check_install_page_setting_env.installEventFilter(env_sys_install_page_setting_env)
        self.lb_env_conda_check_install_page_setting_env.installEventFilter(env_conda_install_page_setting_env)

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
        self.pb_reset_all_params.setIcon(QIcon(self.pixmap_from_svg(ICON_RESET_ALL_PARAMETERS)))
        self.pb_open_output_folder.setIcon(QIcon(self.pixmap_from_svg(ICON_OPEN_FOLDER)))
        self.pb_output_command.setIcon(QIcon(self.pixmap_from_svg(ICON_OUTPUT_COMMAND)))
        self.pb_launch.setIcon(QIcon(self.pixmap_from_svg(ICON_LAUNCH)))

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
        self.tbwdg_env_conda.itemSelectionChanged.connect(self.update_env_conda_specified)
        self.rb_env_sys.clicked.connect(self.update_env_sys)
        self.rb_env_specified.clicked.connect(self.update_env_specified)
        self.rb_env_conda.clicked.connect(self.update_env_conda_specified)
        self.rb_env_builtin.clicked.connect(self.select_python_env)
        self.le_env_specified_path_page_setting_env.textChanged.connect(self.update_env_specified)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonDblClick and obj is not None:
            if event.button() == Qt.LeftButton:
                self.callback()  # 调用回调函数
        return super().eventFilter(obj, event)

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

    def update_installer_info(self):
        """ 显示安装器信息 """
        self.update_table_widget_installer_info()
        self.update_command_display()

    def update_table_widget_installer_info(self):
        """ 更新安装器信息 """
        tooltip = '00000126456132'
        # self.installer.add_icon.set_args('E:')
        # self.installer.imports_paths.append_args('F:')
        # self.installer.imports_paths.append_args('F:\\test')
        installer_dict = self.installer.get_flattened_struct_command_args()
        length = installer_dict['length']
        data: dict = installer_dict['data']
        self.tbwdg_info.clear()
        self.tbwdg_info.setRowCount(length)
        self.tbwdg_info.setHorizontalHeaderLabels(["命令名称", "命令选项", "命令值"])
        index = 0
        for key, item in data.items():
            key: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct
            # name = getattr(self.language, f'{key.name}.display_text')
            # tooltip = getattr(self.language, f'{key.name}.tool_tip')
            item_name = QTableWidgetItem(key.name)
            item_option = QTableWidgetItem(key.command_option)
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
        self.current_interpreter_path = self.lb_env_current_path_page_setting_env.text()
        # if not self.current_interpreter_path:
        #     return
        command_line = self.installer.get_command_line(self.current_interpreter_path)
        if command_line:
            self.tb_command_display.set_text(command_line)

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
            self.tb_console.append_text(format_exc())
            print(format_exc())

    def print_command_line(self):
        """ 打印命令行 """
        output_file_name = f'[command_line]-{self.installer.output_file_name.command_args}' + '.txt'
        output_file_path = os.path.normpath(os.path.join(self.installer.output_folder_path.command_args, output_file_name))
        if command_line := self.installer.get_command_line(self.lb_env_current_path_page_setting_env.text()):
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(command_line)
            Popen(['explorer', '/select,', output_file_path], creationflags=CREATE_NO_WINDOW)
            Popen(['explorer', output_file_path], creationflags=CREATE_NO_WINDOW)

    def record_font_change_in_tb_console(self, font_size):
        """
        记录控制台显示字体大小

        参数:
        - font_size (int): 字体大小

        应用:
        与 self.tb_console(ControlTextBrowser).signal_font_size 信号连接
        """
        self.setting['tb_console_font_size'] = font_size
        self.setting_manager.write_file_to_json()

    def record_font_change_in_tb_command_line(self, font_size):
        """
        记录命令行显示字体大小

        参数:
        - font_size (int): 字体大小

        应用:
        与 self.tb_command_display(ControlTextBrowser).signal_font_size 信号连接
        """
        self.setting['tb_command_line_font_size'] = font_size
        self.setting_manager.write_file_to_json()

    def open_env_variant(self):
        """
        打开环境变量
        """
        sprun('rundll32 sysdm.cpl,EditEnvironmentVariables')

    def start_python_conda_detection(self):
        """
        开始检测 系统Python环境 与 conda环境
        """
        self.thread_python_conda_detection = PythonCondaEnvDetection(self)
        self.thread_python_conda_detection.signal_python_path.connect(self.get_sys_python_env_from_detection_thread)
        self.thread_python_conda_detection.signal_env_conda_list.connect(lambda x: self.get_env_conda_from_detection_thread(x, True))
        self.thread_python_conda_detection.signal_finished.connect(self.finished_thread_python_conda_detection)
        self.thread_python_conda_detection.start()

    def get_sys_python_env_from_detection_thread(self, env_list: list):
        """
        更新Python环境, 由线程传入
        """
        version = env_list[0]
        py_path = env_list[1]
        self.env_struct_sys.env_name = f'<系统环境> {version}'
        self.env_struct_sys.version = version
        self.env_struct_sys.path_python = py_path
        self.lb_env_sys_name_page_setting_env.setText(version)
        self.lb_env_sys_path_page_setting_env.setText(py_path)

    def get_env_conda_from_detection_thread(self, env_list: list, isFirstRun: bool = False):
        """
        更新conda环境, 由线程传入
        """
        if not isFirstRun:
            last_env_name = self.tbwdg_env_conda.item(self.tbwdg_env_conda.currentRow(), 0).text()
            existing_data = []
            for row in range(self.tbwdg_env_conda.rowCount()):
                existing_data.append([
                    self.tbwdg_env_conda.item(row, col).text() for col in range(4)
                ])
            if existing_data == env_list:
                return
        self.tbwdg_env_conda.clear()
        self.tbwdg_env_conda.setRowCount(len(env_list))
        self.tbwdg_env_conda.setHorizontalHeaderLabels(['环境名', '版本号', 'Python解释器路径', 'Pyinstaller路径'])
        for index, item in enumerate(env_list):
            item_name = QTableWidgetItem(item[0])
            item_name.setToolTip(item[0])
            item_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_version = QTableWidgetItem(item[1])
            item_version.setToolTip(item[1])
            item_version.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_python_path = QTableWidgetItem(item[2])
            item_python_path.setToolTip(item[2])
            item_python_path.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            item_pyinstaller_path = QTableWidgetItem(item[3])
            item_pyinstaller_path.setToolTip(item[3])
            item_pyinstaller_path.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            self.tbwdg_env_conda.setItem(index, 0, item_name)
            self.tbwdg_env_conda.setItem(index, 1, item_version)
            self.tbwdg_env_conda.setItem(index, 2, item_python_path)
            self.tbwdg_env_conda.setItem(index, 3, item_pyinstaller_path)
        if not isFirstRun:
            target_row = None
            for idx in range(self.tbwdg_env_conda.rowCount()):
                if self.tbwdg_env_conda.item(idx, 0).text() == last_env_name:
                    target_row = idx
                    break
            if target_row is not None:
                self.tbwdg_env_conda.selectRow(target_row)
            else:
                self.tbwdg_env_conda.selectRow(0)
        else:
            self.tbwdg_env_conda.selectRow(0)

    def finished_thread_python_conda_detection(self):
        self.update_env_sys()
        self.update_env_conda_specified()

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
        self.message.notification(f'已复制：{text}')

    def update_env_sys_without_select_python_env(self):
        """
        更新 系统Python 是否安装pyinstaller
        """
        def update_installed_display(flag: bool):
            if flag:
                self.lb_env_sys_check_install_page_setting_env.setStyleSheet('background-color: rgb(0, 200, 0); color: rgb(0, 0, 0);')
                self.lb_env_sys_check_install_page_setting_env.setText('pyinstaller\n已安装')
                self.env_struct_sys.path_pyinstaller = find_pyinstaller_path(self.env_struct_sys.path_python)
            else:
                self.lb_env_sys_check_install_page_setting_env.setStyleSheet('background-color: rgb(200, 0, 0); color: rgb(200, 200, 200);')
                self.lb_env_sys_check_install_page_setting_env.setText('pyinstaller\n未安装')
                self.env_struct_sys.path_pyinstaller = ''
        py_path = self.lb_env_sys_path_page_setting_env.text()
        self.thread_sys_python_pyinstaller_check = PyinstallerCheck(self, py_path)
        self.thread_sys_python_pyinstaller_check.signal_pyinstaller_installed.connect(update_installed_display)
        self.thread_sys_python_pyinstaller_check.start()
        wait_for_thread_result(self.thread_sys_python_pyinstaller_check.signal_pyinstaller_installed)

    def update_env_conda_specified_without_select_python_env(self) -> None:
        """ 更新 指定conda环境 是否安装pyinstaller """
        current_row = self.tbwdg_env_conda.currentRow()
        if current_row == -1:
            return
        column_env_name = 0
        column_env_version = 1
        column_python_path = 2
        column_pyinstaller_path = 3
        item_env_name = self.tbwdg_env_conda.item(current_row, column_env_name)
        item_env_version = self.tbwdg_env_conda.item(current_row, column_env_version)
        item_python_path = self.tbwdg_env_conda.item(current_row, column_python_path)
        item_pyinstaller_path = self.tbwdg_env_conda.item(current_row, column_pyinstaller_path)
        if item_python_path:
            python_path = item_python_path.text()
            self.lb_env_conda_path_page_setting_env.setText(python_path)
            self.env_struct_conda.env_name = item_env_name.text()
            self.env_struct_conda.version = item_env_version.text()
            self.env_struct_conda.path_python = python_path
            self.env_struct_conda.path_pyinstaller = item_pyinstaller_path.text()
            if self.env_struct_conda.path_pyinstaller:
                self.env_struct_conda.path_pyinstaller = item_pyinstaller_path.text()
                self.lb_env_conda_check_install_page_setting_env.setStyleSheet('background-color: rgb(0, 200, 0); color: rgb(0, 0, 0);')
                self.lb_env_conda_check_install_page_setting_env.setText('pyinstaller\n已安装')
            else:
                self.env_struct_conda.path_pyinstaller = ''
                self.lb_env_conda_check_install_page_setting_env.setStyleSheet('background-color: rgb(200, 0, 0); color: rgb(200, 200, 200);')
                self.lb_env_conda_check_install_page_setting_env.setText('pyinstaller\n未安装')

    def update_env_specified_without_select_python_env(self):
        """
        更新 指定路径 是否安装pyinstaller
        """
        self.le_env_specified_path_page_setting_env.setStyleSheet('')
        self.lb_env_specified_hint_info_page_setting_env.clear()
        python_path = self.le_env_specified_path_page_setting_env.text()
        if (python_path.startswith('"') and python_path.endswith('"')) or (python_path.startswith("'") and python_path.endswith("'")):
            python_path = python_path[1:-1]
            self.le_env_specified_path_page_setting_env.setText(python_path)
        if os.path.exists(python_path) and python_path.endswith('python.exe'):
            self.env_struct_specified.env_name = '<指定环境>'
            self.env_struct_specified.path_python = python_path
            self.env_struct_specified.path_pyinstaller = find_pyinstaller_path(python_path)
            self.env_struct_specified.path_error = False
            if self.rb_env_specified.isChecked():
                self.thread_get_python_version_specified = GetPythonVersion(python_path)
                self.thread_get_python_version_specified.start()
                self.env_struct_specified.version = wait_for_thread_result(self.thread_get_python_version_specified.signal_python_version, '')
                self.env_struct_specified.env_name = f'<指定环境> {self.env_struct_specified.version}'
                if self.env_struct_specified.path_pyinstaller:
                    self.lb_env_specified_check_install_page_setting_env.setStyleSheet('background-color: rgb(0, 200, 0); color: rgb(0, 0, 0);')
                    self.lb_env_specified_check_install_page_setting_env.setText('pyinstaller\n已安装')
                else:
                    self.lb_env_specified_check_install_page_setting_env.setStyleSheet('background-color: rgb(200, 0, 0); color: rgb(200, 200, 200);')
                    self.lb_env_specified_check_install_page_setting_env.setText('pyinstaller\n未安装')
        else:
            self.lb_env_specified_check_install_page_setting_env.setText('')
            self.lb_env_specified_check_install_page_setting_env.setStyleSheet('')

            self.env_struct_specified.env_name = self.env_struct_sys.env_name
            self.env_struct_specified.path_python = self.env_struct_sys.path_python
            self.env_struct_specified.path_pyinstaller = self.env_struct_sys.path_pyinstaller
            self.env_struct_specified.version = self.env_struct_sys.version
            self.env_struct_specified.path_error = True

            if self.rb_env_specified.isChecked():
                self.le_env_specified_path_page_setting_env.setStyleSheet('QLineEdit{background-color: rgb(255, 100, 0);}')
                self.lb_env_specified_hint_info_page_setting_env.setText('<路径不存在, 已使用系统默认路径>')
            # else:
            #     self.le_env_specified_path_page_setting_env.setStyleSheet('')
            #     self.lb_env_specified_hint_info_page_setting_env.clear()

    def update_env_sys(self) -> None:
        """
        更新系统python环境显示，并更新当前环境显示
        """
        self.reset_style_specified()
        self.update_env_sys_without_select_python_env()
        self.select_python_env()

    def update_env_conda_specified(self) -> None:
        """
        更新指定conda环境显示，并更新当前环境显示
        """
        self.reset_style_specified()
        self.update_env_conda_specified_without_select_python_env()
        self.select_python_env()

    def update_env_specified(self):
        """
        更新指定路径环境显示，并更新当前环境显示
        """
        self.update_env_specified_without_select_python_env()
        self.select_python_env()

    def check_all_env(self):
        """
        更新所有显示，并更新当前环境显示
        """
        self.update_env_specified_without_select_python_env()
        self.update_env_sys_without_select_python_env()
        self.update_env_conda_specified_without_select_python_env()
        self.select_python_env()

    def check_env(self):
        self.thread_python_conda_detection = PythonCondaEnvDetection(self)
        self.thread_python_conda_detection.signal_python_path.connect(self.get_sys_python_env_from_detection_thread)
        self.thread_python_conda_detection.signal_env_conda_list.connect(self.get_env_conda_from_detection_thread)
        self.thread_python_conda_detection.start()

    def reset_style_specified(self):
        if not self.rb_env_specified.isChecked():
            self.le_env_specified_path_page_setting_env.setStyleSheet('')
            self.lb_env_specified_hint_info_page_setting_env.clear()

    def select_python_env(self):  # 重写
        """ 
        更新当前选定的python环境显示
        """
        self.update_installer_info()

        if self.rb_env_specified.isChecked():
            self.env_struct_current.env_name = self.env_struct_specified.env_name
            self.env_struct_current.path_python = self.env_struct_specified.path_python
            self.env_struct_current.path_pyinstaller = self.env_struct_specified.path_pyinstaller
            self.env_struct_current.version = self.env_struct_specified.version
            self.env_struct_current.path_error = self.env_struct_specified.path_error  # 给过滤器用的，判断是否执行安装，当指定路径错误时，Label仍存在且可点击，所以要区分

        elif self.rb_env_sys.isChecked():
            self.env_struct_current.env_name = self.env_struct_sys.env_name
            self.env_struct_current.path_python = self.env_struct_sys.path_python
            self.env_struct_current.path_pyinstaller = self.env_struct_sys.path_pyinstaller
            self.env_struct_current.version = self.env_struct_sys.version
            self.env_struct_current.path_error = self.env_struct_specified.path_error

        elif self.rb_env_conda.isChecked():  # (sender == self.rb_env_conda or sender == self.tbwdg_env_conda) and
            self.env_struct_current.env_name = self.env_struct_conda.env_name
            self.env_struct_current.path_python = self.env_struct_conda.path_python
            self.env_struct_current.path_pyinstaller = self.env_struct_conda.path_pyinstaller
            self.env_struct_current.version = self.env_struct_conda.version
            self.env_struct_current.path_error = self.env_struct_specified.path_error

        elif self.rb_env_builtin.isChecked():
            self.reset_style_specified()
            self.env_struct_current.env_name = '<内置环境>'
            self.env_struct_current.path_python = '<buildin> pyinstaller'
            self.env_struct_current.path_pyinstaller = None
            self.env_struct_current.version = ''
            self.env_struct_current.path_error = False

        self.update_env_current_display_and_para()
        self.update_installer_info()

    def set_env_specified_path(self):
        file_path = QFileDialog.getOpenFileName(self, '选择Python解释器', os.path.expanduser("~"), 'Python解释器 (python.exe)')[0]
        if file_path:
            self.le_env_specified_path_page_setting_env.setText(file_path)

    def update_env_current_display_and_para(self):
        """
        更新Python环境显示，根据控件选择改变

        更改主页和设置页中的 当前环境 的显示， 包括名称，路径，是否安装状态
        """
        self.lb_env_current_name_page_setting_env.clear()
        self.lb_env_current_path_page_setting_env.clear()
        self.lb_env_current_name_page_base.clear()
        self.lb_env_current_path_page_base.clear()
        self.lb_env_current_name_page_setting_env.setText(self.env_struct_current.env_name)
        self.lb_env_current_path_page_setting_env.setText(self.env_struct_current.path_python)

        self.lb_env_current_name_page_base.setText(self.env_struct_current.env_name)
        self.lb_env_current_path_page_base.setText(self.env_struct_current.path_python)
        if self.env_struct_current.path_pyinstaller:
            self.lb_env_current_check_install_page_setting_env.setText('pyinstaller\n已安装')
            self.lb_env_current_check_install_page_setting_env.setStyleSheet('background-color: rgb(0, 200, 0); color: rgb(0, 0, 0);')
            self.lb_env_current_check_install_page_base.setText('pyinstaller\n已安装')
            self.lb_env_current_check_install_page_base.setStyleSheet('background-color: rgb(0, 200, 0); color: rgb(0, 0, 0);')
        elif self.env_struct_current.path_pyinstaller is None:
            self.lb_env_current_check_install_page_setting_env.clear()
            self.lb_env_current_check_install_page_setting_env.setStyleSheet('')
            self.lb_env_current_check_install_page_base.clear()
            self.lb_env_current_check_install_page_base.setStyleSheet('')
        else:
            self.lb_env_current_check_install_page_setting_env.setText('pyinstaller\n未安装')
            self.lb_env_current_check_install_page_setting_env.setStyleSheet('background-color: rgb(200, 0, 0); color: rgb(200, 200, 200);')
            self.lb_env_current_check_install_page_base.setText('pyinstaller\n未安装')
            self.lb_env_current_check_install_page_base.setStyleSheet('background-color: rgb(200, 0, 0); color: rgb(200, 200, 200);')
