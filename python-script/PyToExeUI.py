
import traceback
import shutil
import psutil
import win32gui
import win32process
import win32con
import socket

from PyToExe_ui import *
from Icon_svg import * 
from Init_function import *
from Function_QThread import *
from Language_init_Chinese import *
from Language_init_English import *

from PyQt5.QtWidgets import  QMessageBox, QPushButton, QDialog, QListWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSizePolicy, QFrame, QSpacerItem, QInputDialog, QLabel, QCheckBox, QRadioButton, QListWidgetItem, QTextBrowser, QLineEdit, QPlainTextEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QByteArray
import pygetwindow as gw

# 在此脚本运行前，Init_function.py将被运行

class PyToExeUI(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.Win = Ui_MainWindow()
        self.Win.setupUi(self)
        self.combo_list_init()
        self.parameter_init()
        self.ui_init()
        self.connections_pytoexeui()
        self.check_and_deal_existed_win()
        
    # ****************************************检测是否已运行该程序****************************************
    def check_and_deal_existed_win(self):
        try:
            if self.is_current_script_running() and not bool(setting_file['Multiple_Windows']):
                self.get_process_windows(self.pid[1])
                print("当前脚本已经在运行。")
                sys.exit()
            else:
                print("当前脚本未在运行，继续执行其他操作。")
        except Exception as e:
            if self.traceback_display_flag:
                e = traceback.format_exc()
            QMessageBox.information(None, ' ', e)
    
    def client(self, pid):
        print("Client PID:", os.getpid())
        com = self.find_ports_by_pid(pid)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', com))  # 连接到服务器
        client_socket.sendall(sys.argv[1])  # 发送消息
        client_socket.close()
    
    def find_ports_by_pid(self, pid):
        ports = []
        for conn in psutil.net_connections(kind='inet'):
            if conn.pid == pid:
                ports.append(conn.laddr.port)
        return ports
    
    def get_process_windows(self, pid):
        print(pid)
        for i in gw.getAllWindows():
            hwnd = i._hWnd
            _, win_pid = win32process.GetWindowThreadProcessId(hwnd)
            if pid ==  win_pid:
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(hwnd)
    
    def is_current_script_running(self):
        try:
            current_exe_path = os.path.abspath(sys.argv[0])
            current_exe_name = os.path.basename(current_exe_path)
            self.pid = []
            # 遍历所有进程，检查是否有相同的 exe 文件在运行
            exe_count = 0
            timestamp = []
            for process in psutil.process_iter(['pid', 'name', 'exe']):
                # print(process)
                temp_process_name = process.info['name']
                temp_process_exe = process.info['exe']
                temp_process_time = process.create_time()
                temp_pid = process.pid
                if temp_process_name.lower() == current_exe_name.lower() and temp_process_exe.lower() == current_exe_path.lower():
                    exe_count += 1
                    if not self.pid: # 第一个值进来
                        self.pid.append(temp_pid)
                        timestamp.append(temp_process_time)
                    elif len(self.pid) < 2:
                        if timestamp[0] < temp_process_time: # 第二个值进来。 如果第二个值比第一个值大，时间晚
                            self.pid.append(temp_pid)
                            timestamp.append(temp_process_time)
                        else:
                            self.pid.insert(0, temp_pid)
                            timestamp.insert(0, temp_process_time)
                    elif timestamp[1] > temp_process_time:
                        if timestamp[0] > temp_process_time:
                            timestamp[1] = timestamp[0]
                            timestamp[0] = temp_process_time
                            self.pid[1] = self.pid[0]
                            self.pid[0] = temp_pid
                        else:
                            timestamp[1] = temp_process_time
                            self.pid[1] = temp_process_time
            if (exe_count // 2) > 1:
                return True
            else:
                return False
        except Exception as e:
            if self.traceback_display_flag:
                e = traceback.format_exc()
            QMessageBox.information(None, ' ', e)
    
    
    # ****************************************初始化****************************************
    # UI界面的初始化
    def ui_init(self):
        self.set_text_init()
        self.Win.pte_OutputPath.setPlainText(os.path.join(workspace_path))
        self.Win.cbb_LanguageSelect.setFocusPolicy(Qt.NoFocus)
        # 隐藏控件
        self.Win.pb_Recover.hide()
        self.Win.progressBar.hide()
        self.Win.frame_CondaDisplay.hide()
        # 取消滚动条
        self.Win.pte_FilePath.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.pte_FileName.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.pte_OutputPath.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.textBrowser_cmd.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.font_size_setting(self.Win.textBrowser_cmd, 13)
        self.font_size_setting(self.Win.textBrowser, 13)
        # 设置PlainTextedit文字
        self.Win.pte_OutputPath.setPlainText(os.path.join(workspace_path))
        # 设置语言选择Combobox的焦点
        self.Win.cbb_LanguageSelect.setFocusPolicy(Qt.NoFocus)
        # 设置TextBrowser功能条图标
        self.Win.pb_TB_up.setIcon(self.icon_setup(PB_UP_GREY))
        self.pushbutton_hover(self.Win.pb_TB_up, PB_UP_PINK)
        self.Win.pb_TB_down.setIcon(self.icon_setup(PB_DOWN_GREY))
        self.pushbutton_hover(self.Win.pb_TB_down, PB_DOWN_PINK)
        self.Win.pb_TB_increase.setIcon(self.icon_setup(PB_INCREASE_GREY))
        self.pushbutton_hover(self.Win.pb_TB_increase, PB_INCREASE_PINK)
        self.Win.pb_TB_decrease.setIcon(self.icon_setup(PB_DECREASE_GREY))
        self.pushbutton_hover(self.Win.pb_TB_decrease, PB_DECREASE_PINK)
        self.Win.pb_TBcmd_up.setIcon(self.icon_setup(PB_UP_GREY))
        self.pushbutton_hover(self.Win.pb_TBcmd_up, PB_UP_WHITE)
        self.Win.pb_TBcmd_down.setIcon(self.icon_setup(PB_DOWN_GREY))
        self.pushbutton_hover(self.Win.pb_TBcmd_down, PB_DOWN_WHITE)
        self.Win.pb_TBcmd_increase.setIcon(self.icon_setup(PB_INCREASE_GREY))
        self.pushbutton_hover(self.Win.pb_TBcmd_increase, PB_INCREASE_WHITE)
        self.Win.pb_TBcmd_decrease.setIcon(self.icon_setup(PB_DECREASE_GREY))
        self.pushbutton_hover(self.Win.pb_TBcmd_decrease, PB_DECREASE_WHITE)
        # 设置控件可否使用
        self.Win.cb_CondaUse.setEnabled(False)
        self.Win.cb_DisableWindowed.setEnabled(False)
        self.Win.cb_MultiWin.setChecked(bool(setting_file['Multiple_Windows']))
        # 检查系统是否安装Conda，如果安装了，将Conda按钮置为可用
        if shutil.which("conda"):
            self.Win.pb_CondaSetting.setEnabled(True)
            self.Win.frame_CondaDisplay.show()
        else:
            self.Win.pb_CondaSetting.setEnabled(False)
        # 填写输入文件及输出文件夹的LineEdit栏
        self.cmd_dict['output_folder_path'][0] = '--distpath="' + os.path.join(workspace_path) + '"'
        if py_file_name_auto:
            self.Win.pte_FilePath.setPlainText(
                os.path.join(workspace_path, py_file_name_auto))
            self.cmd_dict['python_file_path'][0] = '"' + os.path.join(workspace_path, py_file_name_auto) + '"'
            self.Win.pte_FileName.setPlainText(py_file_name_auto.split('.')[0])
            self.cmd_dict['output_file_name'][0] = '--name="' + py_file_name_auto.split('.')[0] + '"'
            self.launch_flag = False
        self.plain_text_update()
    
    # 参数初始化
    def parameter_init(self):
        self.WINDOW_ICON = self.icon_setup(WINDOWS_ICON)
        self.progressBar_value = 0
        self.launch_flag = False
        self.launch_error_count = 0
        self.clear_file_flag = True
        self.traceback_display_flag = False
        # 用于显示参数，Label是项目名，explain是参数含义
        self.cmd_dict = {
                            'python_file_path': [None, 'pte_FilePath', None], 'output_methode': [None, 'rb_OutputMethod_F', None], 'specpath': [None, 'pb_Specpath', None], 'output_file_name': [None, 'pte_FileName', None], 'contents_directory': [None, 'contents_directory', None], 'add_file_folder_data': [None, 'pb_AddFileFolderData', None], 
                            'add_binary_data': [None, 'pb_AddBinaryData', None], 'imports_folder': [None, 'pb_ImportsFolder', None], 'import_module_name': [None, 'pb_ImportModuleName', None], 'collect_submodules': [None, 'pb_CollectSubmodules', None], 'collect_data': [None, 'pb_CollectData', None],
                            'collect_binaries': [None, 'pb_CollectBinaries', None], 'collect_all': [None, 'pb_CollectAll', None], 'copy_metadata': [None, 'pb_CopyMetadata', None], 'recursive_copy_metadata': [None, 'pb_RecursiveCopyMetadata', None], 'additional_hooks_dir': [None, 'pb_AdditionalHooksDir', None],
                            'runtime_hook': [None, 'pb_RuntimeHook', None], 'exclude_module': [None, 'pb_ExcludeModule', None], 'add_splash_screen': [None, 'pb_AddSplashScreen', None], 'debug_mode': [None, 'pb_DebugMode', None], 'python_option': [None, 'pb_PythonOption', None],
                            'strip_option': [None, 'cb_StripOption', None], 'noupx_option': [None, 'cb_NoupxOption', None], 'upx_exclude': [None, 'pb_UpxExclude', None], 'console_window_control': [None, 'rb_ConsoleWindowControl_C', None], 'hide_console': [None, 'pb_HideConsole', None],
                            'add_icon': [None, 'pb_AddIcon', None], 'disable_windowed': [None, 'cb_DisableWindowed', None], 'version_file': [None, 'pb_VersionFile', None], 'add_xml_file': [None, 'pb_AddXmlFile', None], 
                            'add_resource': [None, 'pb_AddResource', None], 'uac_admin_apply': [None, 'cb_UacAdminApply', None], 'uac_uiaccess': [None, 'cb_UacUiaccess', None],
                            'argv_emulation': [None, 'cb_ArgvEmulation', None], 'osx_bundle_identifier': [None, 'pb_OsxBundleIdentifier', None], 'target_architecture': [None, 'pb_TargetArchitecture', None], 'codesign_identity': [None, 'pb_CodesignIdentity', None], 'osx_entitlements_file': [None, 'pb_OsxEntitlementsFile', None],
                            'runtime_tmpdir': [None, 'pb_RuntimeTmpdir', None], 'ignore_signals': [None, 'cb_IgnoreSignals', None], 'output_folder_path': [None, 'pte_OutputPath', None], 'workpath_option': [None, 'pb_WorkpathOption', None], 'noconfirm_option': [None, 'cb_NoconfirmOption', None],
                            'upx_dir': [None, 'pb_UpxDir', None], 'clear_cache': [None, 'cb_ClearCache', None], 'log_level': [None, 'pb_LogLevel', None]
                        }
        self.cmd = [None]*3
        self.cmd[0] = os.path.splitdrive(workspace_path)[0]
        self.cmd[1] = 'cd '+ workspace_path
        self.cmd_dict['output_methode'][0] = '--onefile'
        self.cmd_dict['output_methode'][1] = 'rb_OutputMethod_F'
        self.cmd_dict['output_methode'][2] = self.json_widgets['rb_OutputMethod_F']['dict_explain']
        self.cmd_dict['clear_cache'][0] = '--clean'
        self.cmd_dict['clear_cache'][2] = self.json_widgets['cb_ClearCache']['dict_explain']
        self.cmd_dict['console_window_control'][0] = '--console'
        self.cmd_dict['console_window_control'][1] = 'rb_ConsoleWindowControl_C'
        self.cmd_dict['console_window_control'][2] = self.json_widgets['rb_ConsoleWindowControl_C']['dict_explain']
        # 用作恢复控制台参数的缓存
        self.recover_cmd_dict = deepcopy(self.cmd_dict)
        # 用于控制恢复显示的缓存cb,rb
        self.recover_cb = []
        self.recover_rb = []
        self.recover_lock = []
        # 用于存储Conda环境
        self.conda_env_list = []
    
    # 信号连接初始化
    def connections_pytoexeui(self):
        self.Win.pte_FilePath.textChanged.connect(self.file_path_changed)
        self.Win.pte_OutputPath.textChanged.connect(self.plain_text_update)
        self.Win.pte_FileName.textChanged.connect(self.plain_text_update)
        self.Win.cbb_LanguageSelect.currentTextChanged.connect(self.language_changed)
        self.Win.cb_Tooltips.stateChanged.connect(self.language_update)
        self.Win.cb_MultiWin.stateChanged.connect(self.multi_windows_changed)
    
    # 界面文字初始化及更改
    def combo_list_init(self):
        try:
            if os.path.exists(os.path.join(exe_folder_path, 'Languages')):
                file_list = os.listdir(os.path.join(exe_folder_path, 'Languages'))
                self.language_list = []
                for file in file_list:
                    if file.endswith('.json'):
                        self.language_list.append(os.path.splitext(file)[0])
                        self.Win.cbb_LanguageSelect.addItem(os.path.splitext(file)[0])
            # 设置显示语言
            # 检查是否存在setting文件，若不存在，则置为默认('简体中文(内置)')
            # 检查setting文件里Language参数，并检查ini的配置是否正确(存在语言包文件)，若不正确，则置为默认('简体中文(内置)')
            self.Win.cbb_LanguageSelect.setCurrentText('简体中文(内置)')
            if setting_file and setting_file['Language']:
                if os.path.exists(os.path.join(exe_folder_path, 'Languages',setting_file['Language']+'.json')):
                    self.Win.cbb_LanguageSelect.setCurrentText(setting_file['Language'])
                elif setting_file['Language'] == 'English(build-in)':
                    self.Win.cbb_LanguageSelect.setCurrentText('English(build-in)')
            self.load_language_json_file()
        except Exception as e:
            e = traceback.format_exc()
            QMessageBox.warning(None, 'PyToExe', e)
    
    # 加载语言包
    def load_language_json_file(self):
        try:
            if self.Win.cbb_LanguageSelect.currentText() == '简体中文(内置)':
                self.language_json = LANGUAGE_INIT_CHINESE
            elif self.Win.cbb_LanguageSelect.currentText() == 'English(build-in)':
                self.language_json = LANGUAGE_INIT_ENGLISH
            else:
                json_file_name = self.Win.cbb_LanguageSelect.currentText() + '.json'
                with open(os.path.join(exe_folder_path, 'Languages', json_file_name), 'r',encoding = 'utf-8') as file:
                    self.language_json = json.load(file)
            self.json_widgets = self.language_json['widgets']
            self.json_special = self.language_json['special']
            self.json_general = self.language_json['general']
        except Exception as e:
            QMessageBox.warning(None, text=e)
            # self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # 加载界面语言和工具提示语言
    def set_text_init(self):
        try:
            for name, value in self.json_widgets.items():
                if 'text' in value:
                    getattr(self.Win, name).setText(value['text'])
                if self.Win.cb_Tooltips.isChecked() and 'tooltip' in value:
                    getattr(self.Win, name).setToolTip(value['tooltip'])
            self.setWindowTitle(self.json_special['window_title'] + '\t\t\t\t' + workspace_path)
        except Exception as e:
            self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # 当语言项更改
    def language_changed(self):
        self.language_update()
        setting_file['Language'] = self.Win.cbb_LanguageSelect.currentText()
        self.write_setting_file()
    
    # 更新语言显示
    def language_update(self):
        self.load_language_json_file()
        self.set_text_init()
    
    # 变更多窗口选项
    def multi_windows_changed(self):
        setting_file['Multiple_Windows'] = self.Win.cb_MultiWin.isChecked()
        self.write_setting_file()
    
    # 更新写入setting_file
    def write_setting_file(self):
        with open (setting_path, 'w', encoding='utf-8') as file:
            json.dump(setting_file, file, ensure_ascii=False, indent=None)
    
    # ****************************************PLE有输入变化时，数据更新****************************************
    def file_path_changed(self):
        
        file_path = self.Win.pte_FilePath.toPlainText()
        if not self.Win.cb_PathLock.isChecked():
            self.Win.pte_OutputPath.setPlainText(os.path.dirname(file_path))
        if not self.Win.cb_NameLock.isChecked():
            self.Win.pte_FileName.setPlainText(os.path.splitext(os.path.basename(file_path))[0])
        self.plain_text_update()
    
    def plain_text_update(self):
        self.cmd[0] = os.path.splitdrive(self.Win.pte_FilePath.toPlainText())[0]
        self.cmd[1] = 'cd "' + os.path.dirname(self.Win.pte_FilePath.toPlainText()) + '"'
        if self.Win.pte_FilePath.toPlainText():
            self.cmd_dict['python_file_path'][0] = '"' + self.Win.pte_FilePath.toPlainText() + '"'
            self.cmd_dict['python_file_path'][2] = self.Win.pte_FilePath.toPlainText()
        if self.Win.pte_OutputPath.toPlainText():
            self.cmd_dict['output_folder_path'][0] = '--distpath="' + self.Win.pte_OutputPath.toPlainText() + '"'
            self.cmd_dict['output_folder_path'][2] = self.Win.pte_OutputPath.toPlainText()
        if self.Win.pte_FileName.toPlainText():
            self.cmd_dict['output_file_name'][0] = '--name="' + self.Win.pte_FileName.toPlainText() + '"'
            self.cmd_dict['output_file_name'][2] = self.Win.pte_FileName.toPlainText()
    
    def icon_setup(self, icon_code):
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(icon_code.encode()))
        return QIcon(pixmap)
    
    def pushbutton_hover(self, button, hover_style):
        button_normal_style = button.icon()
        def on_enter(event):
            button.setIcon(self.icon_setup(hover_style))
            event.accept()
        def on_leave(event):
            button.setIcon(button_normal_style)
            event.accept()
        button.enterEvent = on_enter
        button.leaveEvent = on_leave
    
    def font_size_setting(self, widget, px_value):
        font = widget.font()
        font.setPixelSize(px_value)
        widget.setFont(font)