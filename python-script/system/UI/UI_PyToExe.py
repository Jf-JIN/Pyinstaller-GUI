
import os
import functools
import subprocess

from const.Const_Parameter import *
from const.Const_Icon import *
from const.Const_Style import *

from system.Manager_Style import *
from system.Struct_Pyinstaller import PyinstallerStruct
from system.Manager_Executor_Info import *
from system.Manager_Language import *
from system.Manager_Setting import *
from system.Manager_Data import *

from system.Loader_Pyinstaller_Struct import *
from system.UI.UI_PyToExe_ui import *
from system.UI.Widget_Control_TextBrowser import *
from system.UI.Message_Notification import *
from system.UI.Filter_Mouse import *
from system.UI.Dialog_Version_Editor import *

from tools.image_convert import *


from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton, QPushButton, QVBoxLayout, QCheckBox, QRadioButton, QMainWindow, QTableWidgetItem, QHeaderView, QTableWidget, QMenu, QAction, QLineEdit,  QApplication, QButtonGroup, QAbstractItemView
from PyQt5.QtGui import QClipboard, QIcon
from PyQt5.QtCore import Qt, QSize

_TABLE_WIDGET_COLUMN_MIN_WIDTH = 80

pb_size = 35
lb_icon_size = 40
icon_padding = 8

_log = Log.UI


class PyToExeUI(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.init_parameters()
        self.init_ui()
        self.init_signal_connections()
        self.to_page(App.MainPage.Home)

    def init_parameters(self) -> None:
        self.setting_manager = SettingManager()
        self.data_manager = DataManager()
        self.installer: PyinstallerStruct = self.data_manager.pyinstaller_struct
        self.data_loader = PyinstallerStructLoader()
        self.executor_info_manager = ExecutorInfoManager()
        self.language = LanguageManager()
        self.timer_specified_detection = QTimer()
        self.flag_initialized = False

# =====================================================================================================================================================
        self.clipboard: QClipboard = QApplication.clipboard()

        self.first_time_get_conda_env = True
        # self.dict_mapping 是一个所有参数/控件的字典, 循环此字典, 并pop installer 的字典, 如果installer中存在控件参数, 则置控件的值, 否则置为空/默认样式
        self.dict_mapping: dict = {
            'add_binary_data': [self.pb_add_binary_data, self.update_option_display_push_buttons],
            'add_file_folder_data': [self.pb_add_file_folder_data, self.update_option_display_push_buttons],
            'add_splash_screen': [self.pb_add_splash_screen, self.update_option_display_push_buttons],
            'add_icon': [self.le_output_exe_icon, self.update_option_display_line_edit],
            'add_resource': [self.pb_add_resource, self.update_option_display_push_buttons],
            'add_xml_file': [self.pb_add_xml_file, self.update_option_display_push_buttons],
            'additional_hooks_dir': [self.pb_additional_hooks_dir, self.update_option_display_push_buttons],
            'argv_emulation': [self.cb_argv_emulation, self.update_option_display_check_box],
            'clean_cache': [self.cb_clean_cache, self.update_option_display_check_box],
            'codesign_identity': [self.pb_codesign_identity, self.update_option_display_push_buttons],
            'collect_all': [self.pb_collect_all, self.update_option_display_push_buttons],
            'collect_binaries': [self.pb_collect_binaries, self.update_option_display_push_buttons],
            'collect_data': [self.pb_collect_data, self.update_option_display_push_buttons],
            'collect_submodules': [self.pb_collect_submodules, self.update_option_display_push_buttons],
            'console_window_control': [self.rb_exe_console_display_show, self.update_option_display_radio_button],
            'copy_metadata': [self.pb_copy_metadata, self.update_option_display_push_buttons],
            'contents_directory': [self.pb_contents_directory, self.update_option_display_contents_directory],
            'debug_mode': [self.pb_debug_mode, self.update_option_display_push_buttons],
            'disable_traceback': [self.cb_disable_traceback, self.update_option_display_check_box],
            'exclude_module': [self.pb_exclude_module, self.update_option_display_push_buttons],
            'hidden_imports': [self.pb_hidden_imports, self.update_option_display_push_buttons],
            'hide_console': [self.pb_hide_console, self.update_option_display_check_box],
            'ignore_signals': [self.cb_ignore_signals, self.update_option_display_check_box],
            'import_paths': [self.pb_import_paths, self.update_option_display_push_buttons],
            'log_level': [self.pb_log_level, self.update_option_display_push_buttons],
            'noconfirm_option': [self.cb_noconfirm_option, self.update_option_display_check_box],
            'noupx_option': [self.cb_noupx_option, self.update_option_display_check_box],
            'optimize_level': [self.pb_optimize_level, self.update_option_display_push_buttons],
            'output_file_name': [self.le_output_file_name, self.update_option_display_line_edit],
            'output_method': [self.rb_output_as_file, self.update_option_display_radio_button],
            'output_folder_path': [self.le_output_folder_path, self.update_option_display_line_edit],
            'osx_bundle_identifier': [self.pb_osx_bundle_identifier, self.update_option_display_push_buttons],
            'osx_entitlements_file': [self.pb_osx_entitlements_file, self.update_option_display_push_buttons],
            'python_file_path': [self.le_input_py_file_path, self.update_option_display_line_edit],
            'python_option': [self.pb_python_option, self.update_option_display_push_buttons],
            'recursive_copy_metadata': [self.pb_recursive_copy_metadata, self.update_option_display_push_buttons],
            'runtime_hook': [self.pb_runtime_hook, self.update_option_display_push_buttons],
            'runtime_tmpdir': [self.pb_runtime_tmpdir, self.update_option_display_push_buttons],
            'specpath': [self.pb_specpath, self.update_option_display_push_buttons],
            'strip_option': [self.cb_strip_option, self.update_option_display_check_box],
            'target_architecture': [self.pb_target_architecture, self.update_option_display_push_buttons],
            'uac_admin_apply': [self.cb_uac_admin_apply, self.update_option_display_check_box],
            'uac_uiaccess': [self.cb_uac_uiaccess, self.update_option_display_check_box],
            'upx_dir': [self.pb_upx_dir, self.update_option_display_push_buttons],
            'upx_exclude': [self.pb_upx_exclude, self.update_option_display_push_buttons],
            'version_file': [self.le_output_exe_version, self.update_option_display_line_edit],
            'workpath_option': [self.pb_workpath_option, self.update_option_display_push_buttons],
        }
        self.dict_functions: dict = {}

    def init_ui(self) -> None:
        self.resize(1200, 900)
        self.setWindowTitle(LM.getWord('app_title'))
        self.setWindowIcon(QIcon(convert_svg_to_pixmap(ICON.APP_ICON)))
        self.init_ui_frame()
        self.init_ui_style()
        self.init_widgets_language()
        self.init_display_from_setting()
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# UI初始化
#
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    def init_ui_frame(self) -> None:
        # ----------------------------------------------------- [软件基础] -----------------------------------------------------
        # ----------------------------------------------------- [页外] -----------------------------------------------------
        self.__list_left_menu_buttons: list = [
            self.pb_page_basic, self.pb_page_advance, self.pb_page_ios_win, self.pb_page_info, self.pb_page_command, self.pb_page_console, self.pb_page_setting
        ]
        list_menu_buttons: list = [
            self.pb_page_basic, self.pb_page_advance, self.pb_page_ios_win, self.pb_page_info, self.pb_page_console,
            self.pb_page_command, self.pb_page_setting, self.pb_show_tutorial,  self.pb_open_output_folder,
            self.pb_output_command
        ]

        self.widget_menu.setMaximumWidth(STYLE.getProperty('$btn_square_size').value + 20)
        self.widget_menu.setMinimumWidth(STYLE.getProperty('$btn_square_size').value + 20)
        # self.lb_exe_icon.setPixmap(convert_pixmap_from_svg(ICON_WIN).scaled(pb_size, pb_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        # self.lb_exe_icon: list.setFixedSize(pb_size, pb_size)
        for button in list_menu_buttons:
            button: QPushButton
            self.set_square_btn_icon_size(button)
        self.lb_reset_all_params.setFixedSize(QSize(STYLE.getProperty('$btn_square_size').value, STYLE.getProperty('$btn_square_size').value))
        self.set_square_btn_icon_size(self.pb_output_command)
        self.set_square_btn_icon_size(self.pb_open_output_folder)
        self.pb_launch.setMaximumHeight(STYLE.getProperty('$btn_square_size').value)
        self.pb_launch.setIconSize(QSize(*STYLE.getProperty('$btn_square_icon_size').value))
        self.pb_launch_cancel.setMaximumHeight(STYLE.getProperty('$btn_square_size').value)
        self.pb_launch_cancel.setMinimumWidth(pb_size*2)

        filter_reset_all_parameters = LabelLeftDoubleOrLangPressFilter(self, self.lb_reset_all_params)
        filter_reset_all_parameters.signal_doublePress_longPress.connect(self.reset_parameters)
        self.lb_reset_all_params.installEventFilter(filter_reset_all_parameters)
        self.lb_reset_all_params.setContentsMargins(4, 4, 4, 4)

        # 隐藏控件
        self.wdg_progressbar.hide()
        self.widget_exe_info.hide()
        self.pb_launch_cancel.hide()
        # ----------------------------------------------------- [主页] -----------------------------------------------------
        # 主页图标初始化
        list_icon: list = [
            self.lb_output_exe_icon_icon, self.lb_input_py_file_icon,
            self.lb_output_file_name_icon, self.lb_output_exe_version_icon,
            self.lb_output_folder_path_icon
        ]
        for icon in list_icon:
            icon: QLabel
            icon.setMinimumSize(lb_icon_size, lb_icon_size)
            icon.setMaximumSize(lb_icon_size, lb_icon_size)
            icon.setScaledContents(True)

            # icon.setPixmap(convert_svg_to_pixmap(ICON.BTN_HOMEPAGE))
        # self.lb_input_py_file_icon.setPixmap(convert_svg_to_pixmap(ICON.PYTHON))
        self.lb_env_current_check_install_page_base.setProperty('widgetType', 'flag_installed')

        self.cb_lock_output_file_name.setChecked(SM.getConfig('lock_output_file_name'))
        self.cb_lock_output_folder.setChecked(SM.getConfig('lock_output_folder'))
        self.cb_synchron_env_from_file.setChecked(SM.getConfig('synchron_env_from_file'))
        self.cb_load_env_config.setChecked(SM.getConfig('load_env_config'))
        self.le_input_py_file_path.setClearButtonEnabled(True)
        self.le_output_exe_icon.setClearButtonEnabled(True)
        self.le_output_file_name.setClearButtonEnabled(True)
        self.le_output_folder_path.setClearButtonEnabled(True)
        self.le_output_exe_version.setClearButtonEnabled(True)
        # 输出方式
        group = QButtonGroup(self)
        group.addButton(self.rb_output_as_file)
        group.addButton(self.rb_output_as_folder)
        self.rb_output_as_file.setChecked(True)
        self.pb_contents_directory.hide()
        # 自动增加版本号的cbb控件初始化

        self.cbb_auto_add_version.addItem('', -1)
        self.cbb_auto_add_version.addItem('', 0)
        self.cbb_auto_add_version.addItem('', 1)
        self.cbb_auto_add_version.addItem('', 2)
        self.cbb_auto_add_version.addItem('', 3)
        self.cbb_auto_add_version.setCurrentIndex(SM.getConfig('auto_add_version_index'))
        # ----------------------------------------------------- [通用] -----------------------------------------------------
        # ----------------------------------------------------- [IOS/ Win] -----------------------------------------------------
        # ----------------------------------------------------- [info 表格] -----------------------------------------------------
        self.tbwdg_info.setColumnCount(3)
        self.tbwdg_info.setColumnWidth(0, 150)
        self.tbwdg_info.setColumnWidth(1, 150)
        self.tbwdg_info.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tbwdg_info.horizontalHeader().setMinimumSectionSize(_TABLE_WIDGET_COLUMN_MIN_WIDTH)
        self.tbwdg_info.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.tbwdg_info.horizontalHeader().setStretchLastSection(True)
        self.tbwdg_info.verticalHeader().setVisible(False)

        self.tbwdg_config.setColumnCount(1)
        self.tbwdg_config.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tbwdg_config.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.tbwdg_config.horizontalHeader().setStretchLastSection(True)
        self.tbwdg_config.verticalHeader().setVisible(False)
        # ----------------------------------------------------- [Pyinstaller 命令] -----------------------------------------------------
        self.tb_command_display = ControlTextBrowser(
            flag_button_in_textbrowser=True,
            font_size=self.setting_manager.get_config('tb_command_line_font_size'),
            default_font_size=App.SettingEnum.DEFAULT_SETTING['tb_command_line_font_size'][1],
            flag_traceback_display=True
        )
        layout_command_display = QVBoxLayout(self.wdg_tb_command_display)
        layout_command_display.setContentsMargins(0, 0, 0, 0)
        layout_command_display.addWidget(self.tb_command_display)
        # ----------------------------------------------------- [命令行显示] -----------------------------------------------------
        self.tb_console = ControlTextBrowser(
            flag_button_in_textbrowser=True,
            font_size=self.setting_manager.get_config('tb_console_font_size'),
            default_font_size=App.SettingEnum.DEFAULT_SETTING['tb_console_font_size'][1],
            flag_traceback_display=True
        )
        layout_console = QVBoxLayout(self.wdg_tb_console)
        layout_console.setContentsMargins(0, 0, 0, 0)
        layout_console.addWidget(self.tb_console)
        # ----------------------------------------------------- [设置 常规] -----------------------------------------------------
        self.rb_use_pyinstaller.setChecked(SM.getConfig('use_method') == 'pyinstaller')
        self.rb_use_python.setChecked(SM.getConfig('use_method') == 'python')
        self.cb_delete_build.setChecked(SM.getConfig('delete_build_files'))
        self.cb_delete_spec.setChecked(SM.getConfig('delete_spec_file'))
        self.cb_tooltip_show.setChecked(SM.getConfig('display_tooltip'))
        self.cb_multi_win.setChecked(SM.getConfig('multi_win'))
        self.cb_splash_auto_file_handle.setChecked(SM.getConfig('auto_handle_splash_import'))

        # 隐藏控件
        self.wdg_save_setting.hide()
        # ----------------------------------------------------- [设置 环境] -----------------------------------------------------
        self.le_env_specified_path_page_setting_env.setClearButtonEnabled(True)
        self.lb_env_current_check_install_page_setting_env.setProperty('widgetType', 'flag_installed')
        # self.lb_env_current_name_page_base.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        # self.lb_env_current_name_page_setting_env.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lb_env_current_path_page_base.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lb_env_current_path_page_setting_env.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lb_env_current_pyinstaller_path_page_base.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lb_env_current_pyinstaller_path_page_setting_env.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.set_square_btn_icon_size(self.pb_refresh_sys_env)
        self.rb_env_builtin.hide()

        # 环境选择按钮组
        self.env_btn_group = QButtonGroup()
        self.env_btn_group.addButton(self.rb_env_sys)
        self.env_btn_group.addButton(self.rb_env_specified)
        self.env_btn_group.addButton(self.rb_env_conda)
        # self.env_btn_group.addButton(self.rb_env_builtin)
        # Conda 环境表格初始化
        self.tbwdg_env_conda.setColumnCount(5)
        self.tbwdg_env_conda.setColumnWidth(0, 100)
        self.tbwdg_env_conda.setColumnWidth(1, 100)
        self.tbwdg_env_conda.setColumnWidth(2, 500)
        self.tbwdg_env_conda.setColumnWidth(3, 100)
        self.tbwdg_env_conda.setColumnWidth(4, 500)
        self.tbwdg_env_conda.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tbwdg_env_conda.horizontalHeader().setMinimumSectionSize(_TABLE_WIDGET_COLUMN_MIN_WIDTH)
        self.tbwdg_env_conda.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.tbwdg_env_conda.horizontalHeader().setStretchLastSection(True)
        self.tbwdg_env_conda.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tbwdg_env_conda.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.tbwdg_env_conda.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tbwdg_env_conda.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tbwdg_env_conda.verticalHeader().setVisible(False)
        # ----------------------------------------------------- [设置 样式] -----------------------------------------------------
        self.cbb_current_style.addItem(LM.getWord('theme_light'))
        self.cbb_current_style.addItem(LM.getWord('theme_dark'))
        # self.cbb_current_style.addItem(LM.getWord('theme_dark'))
        self.cbb_current_style.setCurrentText(LM.getWord('theme_'+SM.getConfig('style_mode')))
        # ----------------------------------------------------- [控件 监听器] -----------------------------------------------------
        # 监听器初始化
        filter_env_current_install_page_base = LabelLeftDoubleToInstallFilter(self, self.lb_env_current_check_install_page_base, self.data_manager.current_env)
        filter_env_current_install_page_setting_env = LabelLeftDoubleToInstallFilter(self, self.lb_env_current_check_install_page_setting_env, self.data_manager.current_env)
        # 安装监听器
        self.lb_env_current_check_install_page_base.installEventFilter(filter_env_current_install_page_base)
        self.lb_env_current_check_install_page_setting_env.installEventFilter(filter_env_current_install_page_setting_env)
        # 连接监听器信号
        filter_env_current_install_page_base.signal_output_text_LableDoubleFilter.connect(self.tb_console.append_text)
        filter_env_current_install_page_setting_env.signal_output_text_LableDoubleFilter.connect(self.tb_console.append_text)

    def init_ui_style(self) -> None:
        """ 初始化控件样式 """
        STYLE.getBlock().register(self.centralWidget())
        STYLE.getBlock().get_item('@lb_reset_all_params').register(self.lb_reset_all_params)
        STYLE.getBlock('~scrollbar').register(self.tbwdg_info.verticalScrollBar())
        STYLE.getBlock('~scrollbar').register(self.tbwdg_config.verticalScrollBar())
        STYLE.getBlock('~scrollbar').register(self.tbwdg_env_conda.verticalScrollBar())
        STYLE.getBlock('~scrollbar').register(self.tbwdg_info.horizontalScrollBar())
        STYLE.getBlock('~scrollbar').register(self.tbwdg_config.horizontalScrollBar())
        STYLE.getBlock('~scrollbar').register(self.tbwdg_env_conda.horizontalScrollBar())
        # 菜单栏按钮图标
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_page_basic, ICON.BTN_HOMEPAGE))
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_page_advance, ICON.BTN_FUNCTIONS))
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_page_ios_win, ICON.BTN_IOS_WIN))
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_page_info, ICON.BTN_PYINSTALLER_INFO))
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_page_console, ICON.BTN_CONSOLE))
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_page_command, ICON.BTN_PYINSTALLER_COMMAND))
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_show_tutorial, ICON.BTN_TUTORIAL))
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_page_setting, ICON.BTN_SETTING))
        # 执行按钮图标
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_label_pixmap, self.lb_reset_all_params, ICON.RESET_ALL_PARAMETERS))
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_open_output_folder, ICON.OPEN_FOLDER))
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_output_command, ICON.PRINT_COMMAND))
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_launch, ICON.BTN_LAUNCH))
        # 主页图标
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_label_pixmap, self.lb_input_py_file_icon, ICON.PYTHON))
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_label_pixmap, self.lb_output_folder_path_icon, ICON.FOLDER))
        STYLE.getProperty('$btn_svg_color_in_2').register(functools.partial(self.set_label_pixmap, self.lb_output_file_name_icon, ICON.EXE_FILE))
        STYLE.getProperty('$btn_svg_color_in_2').register(functools.partial(self.set_label_pixmap, self.lb_output_exe_icon_icon, ICON.ICON_FILE))
        STYLE.getProperty('$btn_svg_color_in_2').register(functools.partial(self.set_label_pixmap, self.lb_output_exe_version_icon, ICON.VERSION_FILE))
        # 设置页图标
        STYLE.getProperty('$btn_svg_color').register(functools.partial(self.set_widget_icon, self.pb_refresh_sys_env, ICON.REFRESH))

    def init_widgets_language(self) -> None:
        """ 初始化控件语言 """
        self.language.set_UI_object(self)
        self.language.set_UI_comboBox(self.cbb_language)
        LM.bindList([[
            'env_conda_table_header_name',
            'env_conda_table_header_version',
            'env_conda_table_header_python_path',
            'env_conda_table_header_pyinstaller_version',
            'env_conda_table_header_pyinstaller_path',
        ]], self.tbwdg_env_conda.setHorizontalHeaderLabels)
        LM.bindList([[
            'pyinstaller_info_table_header_name',
            'pyinstaller_info_table_header_option',
            'pyinstaller_info_table_header_value',
        ]], self.tbwdg_info.setHorizontalHeaderLabels)
        LM.bindList([['command_env_config_table_header']], self.tbwdg_config.setHorizontalHeaderLabels)
        LM.bindLanguage('version_add_label', self.lb_auto_add_version.setText)
        LM.bindLanguage('version_no_add', lambda x: self.cbb_auto_add_version.setItemText(0, x))
        LM.bindLanguage('version_major', lambda x: self.cbb_auto_add_version.setItemText(1, x))
        LM.bindLanguage('version_minor', lambda x: self.cbb_auto_add_version.setItemText(2, x))
        LM.bindLanguage('version_revision', lambda x: self.cbb_auto_add_version.setItemText(3, x))
        LM.bindLanguage('version_build', lambda x: self.cbb_auto_add_version.setItemText(4, x))
        LM.bindLanguage('theme_light', lambda x: self.cbb_current_style.setItemText(0, x))
        LM.bindLanguage('theme_dark', lambda x: self.cbb_current_style.setItemText(1, x))
        LM.bindLanguage('pyinstaller_already_installed', self.__update_pyinstaller_installation_status)
        # LM.bindLanguage('builtin_in_use', self.__update_pyinstaller_installation_status)
        LM.bindLanguage('pyinstaller_not_installed', self.__update_pyinstaller_installation_status)

    def init_display_from_setting(self) -> None:
        """ 根据配置 初始化 显示 """
        self.cb_print_cmd_auto_open_file.setChecked(bool(self.setting_manager.get_config('auto_open_printed_command_line_file')))
        self.cb_print_cmd_auto_open_folder.setChecked(bool(self.setting_manager.get_config('auto_open_printed_command_line_folder')))
        current_language_title = self.setting_manager.get_config('language')

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# 信号连接
#
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    def init_signal_connections(self) -> None:
        # ===================================================== [软件基础] =====================================================
        Log.LogGroup.signal_colorized.connect(self.tb_console.append_html_text)
        # Log.LogGroup.signal_all_color.connect(print)
        self.executor_info_manager.signal_data_changed_EIM.connect(self.set_execute_env_path_info)
        self.executor_info_manager.signal_specified_env.connect(self.set_current_env_path)
        self.data_manager.signal_pyinstaller_data_changed_DM.connect(self.update_pyinstaller_info_display)
        self.data_manager.signal_pyinstaller_data_changed_DM.connect(self.test_func)
        self.data_manager.signal_current_env_changed_DM.connect(self.set_current_env_path)
        # ===================================================== [换页] =====================================================
        self.pb_page_basic.clicked.connect(functools.partial(self.to_page, App.MainPage.Home))
        self.pb_page_advance.clicked.connect(functools.partial(self.to_page, App.MainPage.Operation))
        self.pb_page_ios_win.clicked.connect(functools.partial(self.to_page, App.MainPage.Win_IOS))
        self.pb_page_info.clicked.connect(functools.partial(self.to_page, App.MainPage.Info))
        self.pb_page_command.clicked.connect(functools.partial(self.to_page, App.MainPage.Command))
        self.pb_page_console.clicked.connect(functools.partial(self.to_page, App.MainPage.Console))
        self.pb_page_setting.clicked.connect(functools.partial(self.to_page, App.MainPage.Setting))
        # ===================================================== [主页] =====================================================
        self.pb_open_output_folder.clicked.connect(self.open_output_folder)
        self.pb_output_command.clicked.connect(self.print_command_line)
        self.pb_to_env_setting.clicked.connect(self.to_env_setting_page)
        self.le_output_exe_version.editingFinished.connect(self.__on_le_output_exe_version_changed)
        self.le_output_file_name.editingFinished.connect(self.__on_le_output_file_name_changed)
        self.le_output_folder_path.editingFinished.connect(self.__on_le_output_folder_path_changed)
        self.le_input_py_file_path.editingFinished.connect(self.__on_le_input_py_file_path_changed)
        self.le_output_exe_icon.editingFinished.connect(self.__on_le_output_exe_icon_changed)
        self.cbb_auto_add_version.currentIndexChanged.connect(self.__on_cbb_auto_add_version_changed)
        self.cb_lock_output_file_name.stateChanged.connect(self.__on_cb_lock_output_file_name_changed)
        self.cb_lock_output_folder.stateChanged.connect(self.__on_cb_lock_output_folder_changed)
        self.cb_synchron_env_from_file.stateChanged.connect(self.__on_cb_synchron_env_from_file_changed)
        self.cb_load_env_config.stateChanged.connect(self.__on_cb_load_env_config_changed)
        # ===================================================== [通用] =====================================================
        # 见 Function.py
        # ===================================================== [IOS/ Win] =====================================================
        # 见 Function.py
        # ===================================================== [info 表格] =====================================================
        self.tbwdg_info.customContextMenuRequested.connect(self.show_pyinstaller_command_info_tabelwidget_context_menu)
        self.tbwdg_config.customContextMenuRequested.connect(self.show_env_config_in_tablewidget_context_menu)
        # ===================================================== [Pyinstaller 命令] =====================================================
        self.tb_command_display.signal_font_size.connect(lambda font_size: self.setting_manager.set_config('tb_command_line_font_size', font_size))
        # ===================================================== [命令行显示] =====================================================
        self.tb_console.signal_font_size.connect(lambda font_size: self.setting_manager.set_config('tb_console_font_size', font_size))
        # ===================================================== [设置 常规] =====================================================
        self.cb_print_cmd_auto_open_file.stateChanged.connect(self.set_after_print_command_action)
        self.cb_print_cmd_auto_open_folder.stateChanged.connect(self.set_after_print_command_action)
        self.cb_tooltip_show.stateChanged.connect(self.__on_cb_tooltip_show_changed)
        self.cb_delete_build.stateChanged.connect(self.__on_delete_build_files_changed)
        self.cb_delete_spec.stateChanged.connect(self.__on_delete_spec_file_changed)
        self.cb_multi_win.stateChanged.connect(self.__on_cb_multi_win_changed)
        self.cb_splash_auto_file_handle.stateChanged.connect(self.__on_cb_splash_auto_file_handle)
        self.cbb_language.currentIndexChanged.connect(self.change_display_language)
        self.rb_use_python.clicked.connect(self.__on_use_method_changed)
        self.rb_use_pyinstaller.clicked.connect(self.__on_use_method_changed)
        # ===================================================== [设置 环境] =====================================================
        self.timer_specified_detection.timeout.connect(self.__polling_specified_env_detection)
        self.pb_env_sys_edit_page_setting_env.clicked.connect(self.open_env_variant)
        self.pb_env_specified_browser_page_setting_env.clicked.connect(self.set_env_specified_path)
        self.pb_refresh_sys_env.clicked.connect(self.__on_refresh_sys_env)
        self.tbwdg_env_conda.customContextMenuRequested.connect(self.show_conda_tabelwidget_context_menu)
        self.rb_env_sys.clicked.connect(self.__on_select_env)
        self.rb_env_specified.clicked.connect(self.__on_select_env)
        self.rb_env_conda.clicked.connect(self.__on_select_env)
        # self.rb_env_builtin.clicked.connect(self.__on_select_env)
        self.tbwdg_env_conda.itemSelectionChanged.connect(self.__on_conda_env_selected)
        self.le_env_specified_path_page_setting_env.textChanged.connect(self.__on_select_env)
        # self.le_env_specified_path_page_setting_env.textChanged.connect(lambda: self.update_env_specified(isWithSelectUpdate=True))
        # ===================================================== [设置 样式] =====================================================
        self.cbb_current_style.currentIndexChanged.connect(self.__on_current_style_changed)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# 方法
#
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# ##################################################### [QT 事件] #####################################################
    def resizeEvent(self, event) -> None:
        tbwdg_env_conda_row_width_4 = self.tbwdg_env_conda.columnWidth(4)
        if tbwdg_env_conda_row_width_4 > 600:
            self.tbwdg_env_conda.setColumnWidth(4, 600)
        super().resizeEvent(event)

# ##################################################### [通用方法] #####################################################
    def set_input_file(self, file_path: str):
        if os.path.exists(file_path) and file_path.endswith('.txt'):
            self.load_pyinstaller_command(file_path)
        # 文件输入后, 进行更新,  TODO 可以添加是否覆盖的选择
        elif os.path.exists(file_path) and file_path.endswith(('.py', '.pyd', '.pyw')):
            self.installer.python_file_path.set_args(file_path)
            if not self.cb_lock_output_folder.isChecked():
                folder_path = os.path.dirname(file_path)
                self.installer.output_folder_path.set_args(folder_path)
            if not self.cb_lock_output_file_name.isChecked():
                output_file_name = os.path.splitext(os.path.basename(file_path))[0]
                self.installer.output_file_name.set_args(output_file_name)
        elif os.path.exists(file_path) and file_path.endswith(('.spec')):
            self.installer.clear()
            self.installer.python_file_path.set_args(file_path)
        else:
            self.show_message('文件不存在或格式不正确')
            return
        os.chdir(os.path.dirname(self.installer.python_file_path.command_args))

    def load_pyinstaller_command(self, data_str: str) -> None:
        if os.path.isfile(data_str):
            result = self.data_loader.read_file(data_str)
        else:
            result = self.data_loader.read_command(data_str)
        bin_config: list = result[0]
        exe_path: str = result[1]
        struct: PyinstallerStruct = result[2]
        if not struct.get_command_line(self.rb_output_as_folder.isChecked()) and self.flag_initialized:
            QMessageBox.warning(self, LM.getWord('warning'), LM.getWord('error_input_file_format'))
            return
        self.data_manager.set_pyinstaller_struct(struct)
        self.installer = self.data_manager.pyinstaller_struct
        self.data_manager.set_implement_path(exe_path)
        if self.cb_synchron_env_from_file.isChecked():
            # if exe_path:
            #     self.set_special_env(exe_path)
            # else:
            #     self.set_builtin_env()
            self.set_special_env(exe_path)
        if self.cb_load_env_config.isChecked():
            self.set_input_env_config(bin_config)

    def set_widget_icon(self, target_widget: QPushButton, svg_str: str, color: str) -> None:
        """ 
        设置图标

        参数:
        - target_widget: 目标控件, 不一定是QPushButton, 可以是其他控件
        - svg_str: svg字符串
        - color: 颜色
        """
        target_widget.setIcon(QIcon(convert_svg_to_pixmap_with_color(svg_str, color)))

    def set_label_pixmap(self, target_label: QLabel, svg_str: str, color: str) -> None:
        """ 
        设置图标

        参数:
        - target_label: 目标控件, 不一定是QPushButton, 可以是其他控件
        - svg_str: svg字符串
        - color: 颜色
        """
        target_label.setPixmap(convert_svg_to_pixmap_with_color(svg_str, color).scaled(
            target_label.width(), target_label.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def set_builtin_env(self) -> None:
        return
        # self.data_manager.set_current_env(self.data_manager.builtin_env)
        # self.rb_env_builtin.setChecked(True)
        # self.__on_select_env()

    def set_special_env(self, env_path: str) -> None:
        env_path = env_path.replace('\\', '/').replace('"', '').replace("'", '').replace('file:///', '')
        self.executor_info_manager.set_special_env(env_path)
        self.data_manager.set_current_env(self.executor_info_manager.special_struct)
        self.le_env_specified_path_page_setting_env.setText(env_path)
        self.rb_env_specified.setChecked(True)
        self.__on_select_env()

    def set_input_env_config(self, env_config) -> None:
        if env_config:
            self.data_manager.set_input_config(env_config)

    def set_square_btn_icon_size(self, button: QPushButton) -> None:
        button.setProperty('widgetType', 'square')
        button.setIconSize(QSize(*STYLE.getProperty('$btn_square_icon_size').value))

    def show_message(self, *message, **kwargs) -> None:
        MessageNotification.showMessage(
            self, *message,
            background_color=STYLE.getProperty('$message_notification_background').value,
            font_color=STYLE.getProperty('$message_notification_text').value,
            offset=100, move_in_point=(None, '20'), hold_duration=3000,
            font_size_px=STYLE.getProperty('$message_notification_font_size').value,
            font_family=STYLE.getProperty('$message_notification_font_family').value,
            **kwargs)


# ##################################################### [页外] #####################################################

    def to_page(self, index: int) -> None:
        """ 切换页面 """
        self.stackedWidget.setCurrentIndex(index)
        for btn in self.__list_left_menu_buttons:
            btn: QPushButton
            btn.setStyleSheet('')
        selected_btn: QPushButton = self.__list_left_menu_buttons[index]
        selected_btn.setStyleSheet(STYLE.getBlock().get_item('@page_btn_selected').style)

    def open_output_folder(self) -> None:
        """ 打开输出文件夹 """
        try:
            exe_path = os.path.join(self.installer.output_folder_path.command_args, self.installer.output_file_name.command_args+'.exe')
            if os.path.exists(exe_path):
                subprocess.Popen(['explorer', '/select,', os.path.normpath(exe_path)], creationflags=subprocess.CREATE_NO_WINDOW)  # 注意这里如果不norm一下, 会找不到路径
            elif os.path.exists(self.installer.output_folder_path.command_args):
                subprocess.Popen(['explorer', os.path.normpath(self.installer.output_folder_path.command_args)], creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                text = self.language.get_word('output_folder_not_exist')
                self.show_message(f'{text}: {self.installer.output_folder_path.command_args}')
                self.tb_console.append_text(f'{text}: {self.installer.output_folder_path.command_args}')
        except Exception as e:
            _log.exception()

    def print_command_line(self) -> None:
        """ 打印命令行 """
        output_file_name: str = f'[command_line]-{self.installer.output_file_name.command_args}' + '.txt'
        output_folder_path: str = self.installer.output_folder_path.command_args
        default_output_file_path: str = os.path.normpath(os.path.join(output_folder_path, output_file_name))
        output_file_path = QFileDialog.getSaveFileName(self, self.language.get_word('save_file'), default_output_file_path, 'Command Text (*.txt)')[0]
        if not output_file_path:
            return
        output_file_path: str = os.path.normpath(output_file_path)
        command_line = ''
        if self.rb_use_pyinstaller.isChecked():
            command_line: str = self.data_manager.command_use_pyinstaller(self.rb_output_as_folder.isChecked())
        elif self.rb_use_python.isChecked():
            command_line = self.data_manager.command_use_python(self.rb_output_as_folder.isChecked())
        if command_line:
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(command_line)
            if self.setting_manager.get_config('auto_open_printed_command_line_folder'):
                subprocess.Popen(['explorer', '/select,', output_file_path], creationflags=subprocess.CREATE_NO_WINDOW)
            if self.setting_manager.get_config('auto_open_printed_command_line_file'):
                subprocess.Popen(['explorer', output_file_path], creationflags=subprocess.CREATE_NO_WINDOW)
            hint_text = self.language.get_word('command_printed')
            # time_str = time.strftime("%Y.%m.%d-%H:%M:%S", time.localtime())
            # self.tb_console.append_text(f'[{time_str}]\n{hint_text}: {output_file_path}')
            _log.info(f'{hint_text}: {output_file_path}')
            self.show_message(hint_text, open_file_path=output_file_path)
        else:
            hint_text: str = self.language.get_word('command_empty')
            self.show_message(hint_text)

    def set_after_print_command_action(self) -> None:
        """
        设置打印后执行的操作
        """
        self.setting_manager.set_config('auto_open_printed_command_line_folder', self.cb_print_cmd_auto_open_folder.isChecked())
        self.setting_manager.set_config('auto_open_printed_command_line_file', self.cb_print_cmd_auto_open_file.isChecked())

    def reset_parameters_double_click(self) -> None:
        """ 重置参数 """
        _log.info(LM.getWord('completed_reset_parameters'))
        file_path = self.data_manager.pyinstaller_struct.python_file_path.command_args
        self.data_manager.pyinstaller_struct.reset()
        self.set_input_file(file_path)
        self.update_options_display()
        self.show_message(LM.getWord('completed_reset_parameters'))

    def reset_parameters_long_pressed(self) -> None:
        """ 清空所有参数 """
        _log.info(LM.getWord('completed_clear_parameters'))
        file_path = self.data_manager.pyinstaller_struct.python_file_path.command_args
        self.data_manager.pyinstaller_struct.clear()
        self.set_input_file(file_path)
        self.update_options_display()
        self.show_message(LM.getWord('completed_reset_all_parameters'))

    def reset_parameters(self, flag: str) -> None:
        if flag == 'doublePressed':
            self.reset_parameters_double_click()
        elif flag == 'longPressed':
            self.reset_parameters_long_pressed()
        else:
            pass

    def set_processbar_value(self, value: int) -> None:
        self.progressBar.setValue(value)

# ##################################################### [主页] #####################################################
    def __on_cbb_auto_add_version_changed(self) -> None:
        index = self.cbb_auto_add_version.currentIndex()
        SM.setConfig('auto_add_version_index', index)

    def __on_cb_lock_output_file_name_changed(self) -> None:
        SM.setConfig('lock_output_file_name', self.cb_lock_output_file_name.isChecked())

    def __on_cb_lock_output_folder_changed(self) -> None:
        SM.setConfig('lock_output_folder', self.cb_lock_output_folder.isChecked())

    def auto_add_version(self) -> None:
        VersionEditor.add_version(self, self.le_output_exe_version.text(), self.cbb_auto_add_version.currentData())

    def to_env_setting_page(self) -> None:
        self.to_page(App.MainPage.Setting)
        self.tabWidget.setCurrentIndex(1)

    def __on_cb_synchron_env_from_file_changed(self) -> None:
        if self.cb_synchron_env_from_file.isChecked():
            SM.setConfig('synchron_env_from_file', True)
        else:
            SM.setConfig('synchron_env_from_file', False)

    def __on_cb_load_env_config_changed(self) -> None:
        if self.cb_load_env_config.isChecked():
            SM.setConfig('load_env_config', True)
        else:
            SM.setConfig('load_env_config', False)

    def __on_le_output_exe_version_changed(self) -> None:
        version_file_path = self.le_output_exe_version.text()
        if os.path.exists(version_file_path):
            self.data_manager.pyinstaller_struct.version_file.set_args(version_file_path)
        else:
            self.data_manager.pyinstaller_struct.version_file.clear_args()

    def __on_le_output_file_name_changed(self) -> None:
        output_file_name = self.le_output_file_name.text()
        self.data_manager.pyinstaller_struct.output_file_name.set_args(output_file_name)

    def __on_le_output_folder_path_changed(self) -> None:
        output_folder_path = self.le_output_folder_path.text()
        if os.path.exists(output_folder_path):
            self.data_manager.pyinstaller_struct.output_folder_path.set_args(output_folder_path)
        else:
            input_path = self.data_manager.pyinstaller_struct.python_file_path.command_args
            self.data_manager.pyinstaller_struct.output_folder_path.set_args(input_path)

    def __on_le_input_py_file_path_changed(self) -> None:
        input_file_path = self.le_input_py_file_path.text()
        if os.path.exists(input_file_path):
            self.data_manager.pyinstaller_struct.python_file_path.set_args(input_file_path)
        else:
            self.data_manager.pyinstaller_struct.python_file_path.clear_args()

    def __on_le_output_exe_icon_changed(self) -> None:
        output_exe_icon_path = self.le_output_exe_icon.text()
        if os.path.exists(output_exe_icon_path):
            self.data_manager.pyinstaller_struct.add_icon.set_args(output_exe_icon_path)
        else:
            self.data_manager.pyinstaller_struct.add_icon.clear_args()

    # ##################################################### [功能页] #####################################################

    def update_pyinstaller_info_display(self) -> None:
        """ 显示安装器信息 """
        self.set_pyinstaller_info_in_tableWidget()
        self.set_env_config_in_tablewidget()
        self.set_pyinstaller_commandline_in_textBrowser()
        self.update_options_display()

    def update_options_display(self) -> None:
        """ 通过 self.installer 更新界面中选项显示, self.dict_mapping 是在 init_parameters 中定义的 """
        self.installer = self.data_manager.pyinstaller_struct
        dict_installer: dict = self.installer.get_command_dict(self.rb_output_as_folder.isChecked())
        for key, item in self.dict_mapping.items():
            target_item = dict_installer.pop(key, None)
            item[1](item[0], target_item)

    def update_option_display_contents_directory(self, widget: QPushButton, command: str) -> None:
        """ 更新选项显示按钮 """
        if self.installer.output_method.current_state in ['--onedir', '-D']:
            widget.show()
        else:
            widget.hide()
        if not command:
            widget.setStyleSheet('')
            return
        widget.setStyleSheet(STYLE.getBlock().get_item('@params_btn_loaded').style)

    def update_option_display_push_buttons(self, widget: QPushButton, command: str) -> None:
        """ 更新选项显示按钮 """
        if not command:
            widget.setStyleSheet('')
            return
        widget.setStyleSheet(STYLE.getBlock().get_item('@params_btn_loaded').style)

    def update_option_display_radio_button(self, widget: QRadioButton, command: str) -> None:
        """ 更新选项显示单选按钮 """
        if widget in (self.rb_output_as_file, self.rb_output_as_folder):
            if command in ('--onedir', '-D'):
                self.rb_output_as_folder.setChecked(True)
                if widget == self.rb_output_as_folder:
                    pass  # 此处添加样式, 区分已输入指定输出打包文件夹
            else:
                self.rb_output_as_file.setChecked(True)  # 默认样式
        elif widget in (self.rb_exe_console_display_show, self.rb_exe_console_display_hide):
            if command in ('--windowed', '--noconsole', '-w'):
                self.rb_exe_console_display_hide.setChecked(True)
            else:
                self.rb_exe_console_display_show.setChecked(True)  # 默认样式
        else:
            _log.warning(LM.getWord('error_widget_unknown'))

    def update_option_display_check_box(self, widget: QCheckBox, command: str) -> None:
        """ 更新选项显示复选框 """
        if command:
            widget.setChecked(True)
        else:
            widget.setChecked(False)  # 默认样式

    def update_option_display_line_edit(self, widget: QLineEdit, command: str) -> None:
        """ 更新选项显示单行文本框 """
        if command:
            if '"' in command:
                temp_list = command.split('"')
                if len(temp_list) > 1:
                    command = temp_list[1].strip('"')
            widget.setText(command)
        else:
            widget.clear()
# ##################################################### [info 表格 / 命令行] #####################################################

    def set_pyinstaller_commandline_in_textBrowser(self) -> None:
        """ 更新 PyInstaller 命令行内容 """
        self.tb_command_display.clear()
        command_line = ''
        if self.rb_use_python.isChecked():
            command_line = self.data_manager.command_use_python(self.rb_output_as_folder.isChecked())
        elif self.rb_use_pyinstaller.isChecked():
            command_line = self.data_manager.command_use_pyinstaller(self.rb_output_as_folder.isChecked())
        if command_line:
            self.tb_command_display.set_text(command_line)

    def set_pyinstaller_info_in_tableWidget(self) -> None:
        """ 更新 PyInstaller 选项信息 """
        installer_dict = self.installer.get_flattened_struct_command_args(self.rb_output_as_folder.isChecked())
        length = installer_dict['length']
        data: dict = installer_dict['data']
        self.tbwdg_info.clearContents()
        self.tbwdg_info.setRowCount(length)
        index = 0  # 此处不可为 enumerate 替代, 因为多参数的存在, 行数和项目数不相等
        for key, item in data.items():
            key: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct
            name: str = key.name
            if isinstance(key, StateStruct) and not key.isWithOption:
                option: str = key.current_state
            elif isinstance(key.command_option, list):
                option = key.command_option[0]
            else:
                option = key.command_option
            item_name = QTableWidgetItem(name)
            item_option = QTableWidgetItem(option)
            self.tbwdg_info.setItem(index, 0, item_name)
            self.tbwdg_info.setItem(index, 1, item_option)
            item_name.setData(Qt.ItemDataRole.UserRole, key)
            item_name.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            item_option.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            # item_name.setToolTip(tooltip)
            # item_option.setToolTip(tooltip)
            if isinstance(item, list):
                for sub_index, sub_item in enumerate(item):
                    item_command = QTableWidgetItem(sub_item)
                    item_command.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tbwdg_info.setItem(index, 2, item_command)
                    if sub_index == 0:
                        index += 1
                        continue
                    item_blank_0 = QTableWidgetItem('')
                    item_blank_1 = QTableWidgetItem('')
                    item_blank_0.setFlags(Qt.ItemFlag.NoItemFlags)
                    item_blank_1.setFlags(Qt.ItemFlag.NoItemFlags)
                    item_blank_0.setData(Qt.ItemDataRole.UserRole, key)
                    self.tbwdg_info.setItem(index, 0, item_blank_0)
                    self.tbwdg_info.setItem(index, 1, item_blank_1)
                    index += 1
            else:
                item_command = QTableWidgetItem(item)
                if item:
                    item_command.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                else:
                    item_command.setFlags(Qt.ItemFlag.NoItemFlags)
                self.tbwdg_info.setItem(index, 2, item_command)
                index += 1

    def set_env_config_in_tablewidget(self) -> None:
        """ 设置环境配置信息到表格中 """
        config_list = self.data_manager.config_str_list
        self.tbwdg_config.clearContents()
        self.tbwdg_config.setRowCount(len(config_list))
        for index, config_item in enumerate(config_list):
            item = QTableWidgetItem()
            item.setText(config_item)
            item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.tbwdg_config.setItem(index, 0, item)

    def show_pyinstaller_command_info_tabelwidget_context_menu(self, pos: QPoint) -> None:
        """ 显示PyInstaller命令信息 右键菜单  """
        mouse_item: QTableWidgetItem = self.tbwdg_info.itemAt(pos)
        if not mouse_item:
            return
        row: int = mouse_item.row()
        col: int = mouse_item.column()
        struct: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct = self.tbwdg_info.item(row, 0).data(Qt.ItemDataRole.UserRole)
        param: str = self.tbwdg_info.item(row, 2).text()

        menu = QMenu(self.tbwdg_info)
        action_edit_in_tableWidget = QAction(LM.getWord('edit'), self)
        action_edit_in_tableWidget.triggered.connect(lambda: self.__edit_function(row))
        action_delete_item = QAction(LM.getWord('remove'), self)
        action_delete_item.triggered.connect(lambda: self.__delete_pyinstaller_command_info_tabelWidget_item(param, struct))

        menu.addAction(action_edit_in_tableWidget)
        menu.addAction(action_delete_item)
        menu.exec_(self.tbwdg_info.mapToGlobal(pos))

    def __edit_function(self, row: int) -> None:
        command_name: str = self.tbwdg_info.item(row, 0).text()
        while not command_name:
            row = row-1
            command_name = self.tbwdg_info.item(row, 0).text()
        if command_name not in self.dict_functions:
            return
        self.dict_functions[command_name]()

    def __delete_pyinstaller_command_info_tabelWidget_item(self, param, struct: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct) -> None:
        command_args = struct.command_args
        option = struct.command_option[0] if isinstance(struct.command_option, list) else struct.command_option
        struct = self.installer.find_struct_from_option(option)
        if isinstance(command_args, list) and param in command_args:
            command_args.remove(param)
            struct.set_args(command_args)
        elif isinstance(command_args, str):
            struct.clear_args()
        else:
            hint: str = LM.getWord('fail_in_deleting_param')
            _log.info(f'{hint}: {param} <- {struct}')

    def show_env_config_in_tablewidget_context_menu(self, pos: QPoint) -> None:
        row = self.tbwdg_config.currentRow()
        hasItem = False
        config_line = ''
        if row >= 0:
            hasItem = True
            config_line = self.tbwdg_config.item(row, 0).text()
        menu = QMenu(self.tbwdg_config)
        action_open_path = QAction(LM.getWord('open_config_path'), self)
        action_open_path.triggered.connect(lambda: self.__open_config_path(config_line))
        action_copy_path = QAction(LM.getWord('copy_config_path'), self)
        action_copy_path.triggered.connect(lambda: self.__copy_config_path(config_line))
        action_add = menu.addAction(LM.getWord('add'))
        action_add.setIcon(QIcon(convert_svg_to_pixmap(ICON.ADD_FOLDER)))
        action_add.triggered.connect(self.__add_env_config_item)
        if hasItem:
            action_remove: QAction = menu.addAction(LM.getWord('remove'))
            action_remove.setIcon(QIcon(convert_svg_to_pixmap(ICON.DELETE)))
            action_remove.triggered.connect(functools.partial(self.__remove_env_config_item, config_line))
        menu.exec_(self.tbwdg_config.mapToGlobal(pos))

    def __add_env_config_item(self) -> None:
        folder_path: str = QFileDialog.getExistingDirectory(self, LM.getWord('select_folder'), '')
        if not folder_path:
            return
        self.data_manager.add_config_item(folder_path)

    def __remove_env_config_item(self, config_line) -> None:
        if not config_line:
            return
        hint_text: str = LM.getWord('question_remove_config')+f'\n{config_line}'
        res: int | str = DialogMessageBox.question(self, LM.getWord('remove'), hint_text, [LM.getWord('remove')])
        if res == DialogMessageBox.StandardButton.CANCEL:
            return
        elif res == 0:
            self.data_manager.remove_config_item(config_line)

    def __open_config_path(self, config_path) -> None:
        folder_path: str = split_path_from_env_config_line(config_path)
        subprocess.Popen(['explorer', folder_path], creationflags=subprocess.CREATE_NO_WINDOW)

    def __copy_config_path(self, config_path) -> None:
        folder_path: str = split_path_from_env_config_line(config_path)
        self.copy_path(folder_path)

# ##################################################### [设置 常规] #####################################################

    def test_func(self) -> None:
        if self.rb_use_python.isChecked():
            SM.setConfig('pyinstaller_command', self.data_manager.command_use_python(self.rb_output_as_folder.isChecked()))
        elif self.rb_use_pyinstaller.isChecked():
            self.setting_manager.set_config('pyinstaller_command', self.data_manager.command_use_pyinstaller(self.rb_output_as_folder.isChecked()))

    def __on_use_method_changed(self) -> None:
        if self.rb_use_python.isChecked():
            SM.setConfig('use_method', 'python')
        elif self.rb_use_pyinstaller.isChecked():
            SM.setConfig('use_method', 'pyinstaller')
        self.__on_select_env()

    def __on_delete_build_files_changed(self) -> None:
        if self.cb_delete_build.isChecked():
            SM.setConfig('delete_build_files', True)
        else:
            SM.setConfig('delete_build_files', False)

    def __on_delete_spec_file_changed(self) -> None:
        if self.cb_delete_spec.isChecked():
            SM.setConfig('delete_spec_file', True)
        else:
            SM.setConfig('delete_spec_file', False)

    def change_display_language(self) -> None:
        """ 切换语言 """
        lang: str = self.cbb_language.currentText()
        self.language.open_language_package(lang)
        self.setting_manager.set_config('language', self.language.language_title)

    def __on_cb_tooltip_show_changed(self):
        if self.cb_tooltip_show.isChecked():
            SM.setConfig('display_tooltip', True)
            LM.EnableTooltip(True)
        else:
            SM.setConfig('display_tooltip', False)
            LM.EnableTooltip(False)

    def __on_cb_multi_win_changed(self) -> None:
        if self.cb_multi_win.isChecked():
            SM.setConfig('multi_win', True)
        else:
            SM.setConfig('multi_win', False)

    def __on_cb_splash_auto_file_handle(self) -> None:
        if self.cb_splash_auto_file_handle.isChecked():
            SM.setConfig('auto_handle_splash_import', True)
        else:
            SM.setConfig('auto_handle_splash_import', False)


# ##################################################### [设置 环境] #####################################################

    def set_execute_env_path_info(self) -> None:
        """ 更新执行环境信息 """
        self.lb_env_sys_path_page_setting_env.setText(self.executor_info_manager.local_struct.python_path)
        self.set_current_env_path()
        self.set_conda_env_info_in_tableWidget(self.executor_info_manager.conda_struct_dict)

    def set_current_env_path(self) -> None:
        self.lb_env_current_name_page_base.setText(self.data_manager.current_env.name)
        self.lb_env_current_name_page_setting_env.setText(self.data_manager.current_env.name)
        self.lb_env_current_path_page_base.setText(self.data_manager.current_env.python_path)
        self.lb_env_current_path_page_setting_env.setText(self.data_manager.current_env.python_path)
        self.lb_env_current_pyinstaller_path_page_base.setText(self.data_manager.current_env.pyinstaller_path)
        self.lb_env_current_pyinstaller_path_page_setting_env.setText(self.data_manager.current_env.pyinstaller_path)
        self.__update_pyinstaller_installation_status()

    def set_conda_env_info_in_tableWidget(self, env_dict: dict) -> None:
        """
        conda环境列表 写入到 tableWidget

        列表格式: {base: ['base', 'C:/Users/.../miniconda3/python.exe', '3.11.5', 'C:/Users/.../miniconda3/Scripts/pyinstaller.exe', '6.3.0']}
        """
        # 获取起始的位置和选项
        last_scrollbar_vertical_value = self.tbwdg_env_conda.verticalScrollBar().value()
        last_scrollbar_horizontal_value = self.tbwdg_env_conda.horizontalScrollBar().value()
        if item := self.tbwdg_env_conda.item(self.tbwdg_env_conda.currentRow(), 0):
            last_env_name = item.text()
        else:
            last_env_name = ''
        target_row = -1
        length = len(env_dict)
        self.tbwdg_env_conda.clearContents()
        self.tbwdg_env_conda.setRowCount(length)
        # 遍历字典, 添加项目
        for index, (key, struct) in enumerate(env_dict.items()):
            struct: ExecutorInfoStruct
            if key == last_env_name:
                target_row = index
            item_name = QTableWidgetItem(struct.name)
            item_name.setToolTip(struct.name)
            item_name.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

            item_python_version = QTableWidgetItem(struct.python_version)
            item_python_version.setToolTip(struct.python_version)
            item_python_version.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

            item_python_path = QTableWidgetItem(struct.python_path)
            item_python_path.setToolTip(struct.python_path)
            item_python_path.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

            item_pyinstaller_path = QTableWidgetItem(struct.pyinstaller_path)
            item_pyinstaller_path.setToolTip(struct.pyinstaller_path)
            item_pyinstaller_path.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

            item_pyinstaller_version = QTableWidgetItem(struct.pyinstaller_version)
            item_pyinstaller_version.setToolTip(struct.pyinstaller_version)
            item_pyinstaller_version.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

            self.tbwdg_env_conda.setItem(index, 0, item_name)
            self.tbwdg_env_conda.setItem(index, 1, item_python_version)
            self.tbwdg_env_conda.setItem(index, 2, item_python_path)
            self.tbwdg_env_conda.setItem(index, 3, item_pyinstaller_version)
            self.tbwdg_env_conda.setItem(index, 4, item_pyinstaller_path)
        # 复原滚动条位置和选项
        if target_row >= 0:
            self.tbwdg_env_conda.selectRow(target_row)
            self.tbwdg_env_conda.verticalScrollBar().setValue(last_scrollbar_vertical_value)
            self.tbwdg_env_conda.horizontalScrollBar().setValue(last_scrollbar_horizontal_value)
        else:
            self.tbwdg_env_conda.selectRow(0)

    def open_env_variant(self) -> None:
        """
        打开环境变量
        """
        subprocess.run('rundll32 sysdm.cpl,EditEnvironmentVariables')

    def show_conda_tabelwidget_context_menu(self, pos: QPoint) -> None:
        """
        显示 Conda环境 右键菜单
        """
        mouse_item: QTableWidgetItem = self.tbwdg_env_conda.itemAt(pos)
        if not mouse_item:
            return
        row: int = mouse_item.row()
        col: int = mouse_item.column()

        python_path = os.path.normpath(self.tbwdg_env_conda.item(row, 2).text())
        pyinstaller_path = os.path.normpath(self.tbwdg_env_conda.item(row, 4).text())

        menu = QMenu(self.tbwdg_env_conda)
        action_python_copy = QAction(LM.getWord('copy_python_path'), self)
        action_python_copy.triggered.connect(functools.partial(self.copy_path, python_path))
        action_pyinstaller_copy = QAction(LM.getWord('copy_pyinstaller_path'), self)
        action_pyinstaller_copy.triggered.connect(functools.partial(self.copy_path, pyinstaller_path))
        action_open_python_folder = QAction(LM.getWord('open_python_folder'), self)
        action_open_python_folder.triggered.connect(lambda: subprocess.Popen(f'explorer /select,"{python_path}"', creationflags=subprocess.CREATE_NO_WINDOW))
        action_open_pyinstaller_folder = QAction(LM.getWord('open_pyinstaller_folder'), self)
        action_open_pyinstaller_folder.triggered.connect(lambda: subprocess.Popen(f'explorer /select,"{pyinstaller_path}"', creationflags=subprocess.CREATE_NO_WINDOW))
        menu.addAction(action_python_copy)
        menu.addAction(action_pyinstaller_copy)
        menu.addAction(action_open_python_folder)
        menu.addAction(action_open_pyinstaller_folder)
        menu.exec_(self.tbwdg_env_conda.mapToGlobal(pos))

    def copy_path(self, text: str) -> None:
        """
        复制python解释器路径
        """
        self.clipboard.setText(text)
        hint_text = self.language.get_word("copied")
        self.show_message(f'{hint_text}: {text}')

    def __on_conda_env_selected(self) -> None:
        if not self.rb_env_conda.isChecked():
            return
        currnet_item: QTableWidgetItem = self.tbwdg_env_conda.currentItem()
        if currnet_item is None:
            return
        row: int = currnet_item.row()
        item: QTableWidgetItem = self.tbwdg_env_conda.item(row, 0)
        if item is None:
            return
        env_name = item.text()
        conda_struct = self.executor_info_manager.conda_struct_dict.get(env_name, None)
        if conda_struct is None:
            return
        self.data_manager.set_current_env(conda_struct)

    def set_env_specified_path(self) -> None:
        file_path = QFileDialog.getOpenFileName(self, '选择Python解释器', os.path.expanduser("~"), 'Python解释器 (python.exe)')[0]
        if file_path:
            self.le_env_specified_path_page_setting_env.setText(file_path)

    def __polling_specified_env_detection(self) -> None:
        # 由于外部输入, 必须格式处理
        input_path = self.le_env_specified_path_page_setting_env.text().replace('"', '').replace("'", '').replace('file:///', '')
        if self.data_manager.current_env.pyinstaller_path and self.timer_specified_detection.interval() < 1000:
            self.timer_specified_detection.setInterval(2000)
        elif not self.data_manager.current_env.pyinstaller_path and self.timer_specified_detection.interval() > 1000:
            self.timer_specified_detection.setInterval(500)
        self.executor_info_manager.set_special_env(input_path)

    def __on_select_env(self) -> None:
        sender = self.sender()
        if (sender == self.rb_env_specified or sender == self.le_env_specified_path_page_setting_env) and self.timer_specified_detection.isActive():
            return
        self.timer_specified_detection.stop()
        if self.rb_env_sys.isChecked():
            self.data_manager.set_current_env(self.executor_info_manager.local_struct)
        elif self.rb_env_conda.isChecked():
            self.__on_conda_env_selected()
        elif self.rb_env_builtin.isChecked():
            pass
            # self.data_manager.set_current_env(self.data_manager.builtin_env)
        else:
            self.data_manager.set_current_env(self.executor_info_manager.special_struct)
            self.timer_specified_detection.setInterval(500)
            self.timer_specified_detection.start()

    def __update_pyinstaller_installation_status(self, holder_for_LM=None) -> None:  # holder_for_LM 是给 语言管理器传参使用的, 无任何实际意义
        if self.data_manager.current_env.pyinstaller_path:
            text: str = LM.getWord('pyinstaller_already_installed')
            self.lb_env_current_check_install_page_setting_env.setText(text)
            self.lb_env_current_check_install_page_base.setText(text)
            self.lb_env_current_check_install_page_setting_env.setStyleSheet(STYLE.getBlock().get_item('@lb_pyinstaller_installed').style)
            self.lb_env_current_check_install_page_base.setStyleSheet(STYLE.getBlock().get_item('@lb_pyinstaller_installed').style)
        # elif self.data_manager.current_env.name == self.data_manager.builtin_env.name:
        #     text: str = LM.getWord('builtin_in_use')
        #     self.lb_env_current_check_install_page_setting_env.setText(text)
        #     self.lb_env_current_check_install_page_base.setText(text)
        #     self.lb_env_current_check_install_page_setting_env.setStyleSheet('')
        #     self.lb_env_current_check_install_page_base.setStyleSheet('')
        else:
            text: str = LM.getWord('pyinstaller_not_installed')
            self.lb_env_current_check_install_page_setting_env.setText(text)
            self.lb_env_current_check_install_page_base.setText(text)
            self.lb_env_current_check_install_page_setting_env.setStyleSheet(STYLE.getBlock().get_item('@lb_pyinstaller_uninstalled').style)
            self.lb_env_current_check_install_page_base.setStyleSheet(STYLE.getBlock().get_item('@lb_pyinstaller_uninstalled').style)

    def __on_refresh_sys_env(self):
        self.executor_info_manager.update_local_env()
        self.show_message(LM.getWord('refresh_sys_env_success'))

# ##################################################### [设置 样式] #####################################################
    def __on_current_style_changed(self):
        text = self.cbb_current_style.currentText()
        if text == LM.getWord('theme_light'):
            STYLE.setThemeDict(SheetStyle.LIGHT)
            SM.setConfig('style_mode', 'light')
        elif text == LM.getWord('theme_dark'):
            STYLE.setThemeDict(SheetStyle.DARK)
            SM.setConfig('style_mode', 'dark')
