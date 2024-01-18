import os
import sys
import json
from copy import deepcopy
import traceback

from PyToExe_ui import *

from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton, QDialog, QListWidget, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QFrame, QSpacerItem, QInputDialog, QLabel, QCheckBox, QRadioButton
from PyQt5.QtGui import QTextCursor, QDesktopServices, QIcon, QPixmap
from PyQt5.QtCore import Qt, QUrl, QByteArray


# workspace_path = os.path.dirname(__file__)
workspace_path = os.getcwd()
exe_folder_path = os.path.dirname(sys.argv[0])
icon_data = '''<svg version="1.1" id="svg1" width="400" height="400" viewBox="0 0 400 400" sodipodi:docname="PyToExe.svg" inkscape:version="1.3.2 (091e20e, 2023-11-25, custom)" inkscape:export-filename="PyToExe.png" inkscape:export-xdpi="96" inkscape:export-ydpi="96" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs1"> <linearGradient id="swatch6" inkscape:swatch="solid"> <stop style="stop-color:#000000;stop-opacity:1;" offset="0" id="stop6" /> </linearGradient><linearGradient id="swatch35" inkscape:swatch="solid"> <stop style="stop-color:#f54d00;stop-opacity:1;" offset="0" id="stop35" /> </linearGradient> <linearGradient inkscape:collect="always" xlink:href="#swatch35" id="linearGradient35" x1="263.0344" y1="195.86606" x2="400.23287" y2="195.86606" gradientUnits="userSpaceOnUse" /> </defs> <sodipodi:namedview id="namedview1" pagecolor="#ffffff" bordercolor="#000000" borderopacity="0.25" inkscape:showpageshadow="2" inkscape:pageopacity="0.0" inkscape:pagecheckerboard="0" inkscape:deskcolor="#d1d1d1" inkscape:zoom="1.5832414" inkscape:cx="154.11421" inkscape:cy="222.01289" inkscape:window-width="1920" inkscape:window-height="1009" inkscape:window-x="2552" inkscape:window-y="-8" inkscape:window-maximized="1" inkscape:current-layer="g1" /> <g inkscape:groupmode="layer" inkscape:label="Image" id="g1"> <path id="path1" style="fill:#ef9e01;fill-opacity:1;stroke:#000000;stroke-opacity:1;stroke-width:2;stroke-dasharray:none" d="M 190.73633,27.681641 A 172.93973,172.93973 0 0 0 121.74609,37.525391 172.93973,172.93973 0 0 0 18.384766,259.18359 172.93973,172.93973 0 0 0 240.04492,362.54492 172.93973,172.93973 0 0 0 351.23047,172.44141 l -38.29688,13.9375 A 129.19458,133.82138 70 0 1 224.75391,322.14844 129.19458,133.82138 70 0 1 54.816406,246.51562 129.19458,133.82138 70 0 1 136.37891,79.34375 129.19458,133.82138 70 0 1 281.98633,115.30078 l 0.002,0.002 c 0.0203,0.0114 0.0405,0.0243 0.0606,0.0352 0.0403,0.0238 0.0798,0.046 0.11719,0.0742 0.007,0.005 0.009,0.0125 0.0156,0.0176 0.005,0.002 0.0105,0.004 0.0156,0.006 0.0358,0.009 0.0663,0.0309 0.0976,0.0488 0.004,0.003 0.009,0.005 0.0117,0.006 0.002,0.002 0.008,0.004 0.0176,0.0117 0.006,0.004 0.009,0.0113 0.0137,0.0156 l 0.002,0.002 c 0.002,0.002 0.005,8.5e-4 0.008,0.002 0.0241,0.008 0.0442,0.024 0.0644,0.0391 h 0.002 c 0.0101,10e-4 0.0202,0.003 0.0312,0.006 0.0324,0.0107 0.0592,0.0325 0.0859,0.0527 0.009,0.007 0.0185,0.0141 0.0254,0.0215 0.0153,0.005 0.0291,0.0103 0.0449,0.0137 0.0248,0.008 0.0512,0.0139 0.0762,0.0215 0.0267,0.009 0.0513,0.0202 0.0781,0.0293 0.0301,0.0117 0.0593,0.0269 0.084,0.0469 a 129.19458,133.82138 70 0 0 -0.0293,-0.0332 20.874001,20.874001 0 0 0 18.125,1.92187 20.874001,20.874001 0 0 0 12.47851,-26.755854 20.874001,20.874001 0 0 0 -0.76953,-1.753907 172.93973,172.93973 0 0 0 -121.9082,-61.449218 z" /> <path id="rect23-1" style="fill:#2525ff;fill-opacity:1;stroke-width:2;stroke:url(#linearGradient35);stroke-opacity:1;stroke-dasharray:none" d="m 268.06954,198.3686 0.0123,-0.009 -3.98989,22.17486 0.12876,0.18526 20.18849,3.63248 47.31514,-32.88487 c 3.34059,-2.32178 7.89731,-1.49973 10.21918,1.8404 l 32.8852,47.31337 20.19025,3.6328 0.14362,-0.0998 4.01273,-22.30189 -49.54068,-71.27972 c -2.32181,-3.34063 -6.88069,-4.16091 -10.22126,-1.8391 l -71.33385,49.57833 z" /> <text xml:space="preserve" style="font-size:202.244px;line-height:0px;letter-spacing:0px;fill:#e6e6e6;fill-opacity:1;stroke:#000000;stroke-width:5.41662;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1;paint-order:stroke fill markers" x="-6.7089086" y="363.74023" id="text29-2"><tspan id="tspan29-2" x="-6.7089086" y="363.74023" sodipodi:role="line" style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:202.244px;line-height:0px;font-family:Arial;-inkscape-font-specification:'Arial Bold';letter-spacing:0px;fill:#e6e6e6;fill-opacity:1;stroke:#000000;stroke-width:5.41662;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1;paint-order:stroke fill markers">EXE</tspan></text> <text xml:space="preserve" style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:231.553px;line-height:0px;font-family:Arial;-inkscape-font-specification:'Arial Bold';letter-spacing:3.4733px;fill:#e6e6e6;fill-opacity:1;stroke:#000000;stroke-width:5.78883;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1;paint-order:stroke fill markers" x="32.131664" y="185.16193" id="text6"><tspan sodipodi:role="line" id="tspan6" x="32.131664" y="185.16193" style="font-size:231.553px;letter-spacing:3.4733px;stroke-width:5.78883">PY</tspan></text> </g> </svg>'''
# default_icon_path = os.path.join(exe_folder_path, 'PyToExe.ico') 
# default_icon_path = os.path.join(exe_folder_path, 'resource', 'PyToExe.ico')




for i in os.listdir(workspace_path):
    if i == 'main.py':
        py_file_auto_path = i
        break
    elif '.py' in i and not 'ui' in i:
        py_file_auto_path = i
    else:
        py_file_auto_path = None


class PyToExeUI(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.Win = Ui_MainWindow()
        self.Win.setupUi(self)
        self.combo_list_init()
        self.parameter_init()
        self.ui_init()
        self.py_to_exe_ui_signal_connection()

    # ****************************************初始化****************************************
    # UI界面的初始化
    def ui_init(self):
        self.set_text_init()
        self.Win.pb_Recover.hide()
        self.Win.pte_FilePath.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.pte_FileName.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.pte_OutputPath.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.textBrowser_cmd.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.pte_OutputPath.setPlainText(os.path.join(workspace_path))
        self.Win.cbb_LanguageSelect.setFocusPolicy(Qt.NoFocus)
        self.cmd_dict['output_folder_path'][0] = '--distpath="' + os.path.join(workspace_path) + '"'
        if py_file_auto_path:
            self.Win.pte_FilePath.setPlainText(
                os.path.join(workspace_path, py_file_auto_path))
            self.cmd_dict['python_file_path'][0] = '"' + os.path.join(workspace_path, py_file_auto_path) + '"'
            self.Win.pte_FileName.setPlainText(py_file_auto_path.split('.')[0])
            self.cmd_dict['output_file_name'][0] = '--name="' + py_file_auto_path.split('.')[0] + '"'
            self.launch_flag = True

    # 参数初始化
    def parameter_init(self):
        pixmap_icon = QPixmap()
        pixmap_icon.loadFromData(QByteArray(icon_data.encode()))
        self.WINDOW_ICON = QIcon(pixmap_icon)
        self.launch_flag = True
        self.clear_file_flag = True
        # 用于显示参数，Label是项目名，explain是参数含义
        # self.cmd_dictsss = {
        #     'output_methode': [None, self.json_widgets['rb_OutputMethod_F']['dict'], None], 'specpath': [None, '\n.spec的文件夹：\t', None], 'output_file_name': [None, '\n输出名称：\t', None], 'contents_directory': [None, '\n除exe外，输出的其他数据的存入路径：\n', None], 'add_file_folder_data': [None, '\n添加文件资源：\t', None], 
        #     'add_binary_data': [None, '\n添加二进制资源：\t', None], 'imports_folder': [None, '\n搜索import模块路径：\t', None], 'import_module_name': [None, '\n引用外部指定import模块名：\t', None], 'collect_submodules': [None, '\n打包及本身及其所有子模块的模块：\t', None], 'collect_data': [None, '\n打包所有数据的模块：\t', None],
        #     'collect_binaries': [None, '\n打包模块的所有二进制文件：\t', None], 'collect_all': [None, '\n打包所有数据的模块：\t', None], 'copy_metadata': [None, '\n打包元数据的模块：\t', None], 'recursive_copy_metadata': [None, '\n打包本身及其所有依赖项元数据的模块：\t', None], 'additional_hooks_dir': [None, '\n添加指定的钩子文件夹路径：\t', None],
        #     'runtime_hook': [None, '\n添加运行时钩子文件的路径：\t', None], 'exclude_module': [None, '\n要忽略的可选模块或包：\t', None], 'add_splash_screen': [None, '\n应用程序的启动画面：\t', None], 'debug_mode': [None, '\n调试模式：\t', None], 'python_option': [None, '指定Python解释器的命令行：\t', None],
        #     'strip_option': [None, '\n对可执行文件和共享库应用符号表剥离：\t', None], 'noupx_option': [None, '\n使用upx压缩：\t', None], 'upx_exclude': [None, '\nupx压缩排除文件：\t', None], 'console_window_control': [None, '\n控制台窗口：\t', None], 'hide_console': [None, '控制台窗口的显示方式：\t', None],
        #     'add_icon': [None, '\n应用图标路径：\t', None], 'disable_windowed': [None, '\n禁用窗口化：\t', None], 'version_file': [None, '\n添加版本资源：\t', None], 'add_xml_file': [None, '\n添加文件或XML资源：\t', None], 'no_embed_manifest': [None, '\n将应用程序清单嵌入到可执行文件中：\t', None],
        #     'add_resource': [None, '\n添加嵌入exe中的文件或目录：\t', None], 'uac_admin_apply': [None, '\n申请管理员权限：\t', None], 'uac_uiaccess': [None, '\n允许远程桌面使用：\t', None], 'win_private_assemblies': [None, '\n共享程序集改私有：\t', None], 'win_no_prefer_redirects': [None, '\ndll优先级重定向：\t', None],
        #     'argv_emulation': [None, '\nmacOS启用argv仿真：\t', None], 'osx_bundle_identifier': [None, '\nBundle Identifier：\t', None], 'target_architecture': [None, '\n目标架构：\t', None], 'codesign_identity': [None, '\n代码签名：\t', None], 'osx_entitlements_file': [None, '\n二进制授权文件(entitlements文件)：\t', None],
        #     'runtime_tmpdir': [None, '\nPyinstaller临时目录：\t', None], 'ignore_signals': [None, '\n引导加载程序忽略信号：\t', None], 'output_folder_path': [None, '\n输出目录：\t', None], 'workpath_option': [None, '\n临时工作文件位置：\t', None], 'noconfirm_option': [None, '\n替换输出目录询问：\t', None],
        #     'upx_dir': [None, '\nupx工具路径：\t', None], 'ascii': [None, '\n编码支持：\t', None], 'clear_cache': [None, '\n清理缓存：\t', None], 'log_level': [None, '\n控制台消息详细程度：\t', None], 'python_file_path': [None, '\nPython脚本：\t', None]
        # }
        self.cmd_dict = {
                            'output_methode': [None, 'rb_OutputMethod_F', None], 'specpath': [None, 'pb_Specpath', None], 'output_file_name': [None, 'pte_FileName', None], 'contents_directory': [None, 'rb_OutputMethod_D', None], 'add_file_folder_data': [None, 'pb_AddFileFolderData', None], 
                            'add_binary_data': [None, 'pb_AddBinaryData', None], 'imports_folder': [None, 'pb_ImportsFolder', None], 'import_module_name': [None, 'pb_ImportModuleName', None], 'collect_submodules': [None, 'pb_CollectSubmodules', None], 'collect_data': [None, 'pb_CollectData', None],
                            'collect_binaries': [None, 'pb_CollectBinaries', None], 'collect_all': [None, 'pb_CollectAll', None], 'copy_metadata': [None, 'pb_CopyMetadata', None], 'recursive_copy_metadata': [None, 'pb_RecursiveCopyMetadata', None], 'additional_hooks_dir': [None, 'pb_AdditionalHooksDir', None],
                            'runtime_hook': [None, 'pb_RuntimeHook', None], 'exclude_module': [None, 'pb_ExcludeModule', None], 'add_splash_screen': [None, 'pb_AddSplashScreen', None], 'debug_mode': [None, 'pb_DebugMode', None], 'python_option': [None, 'pb_PythonOption', None],
                            'strip_option': [None, 'cb_StripOption', None], 'noupx_option': [None, 'cb_NoupxOption', None], 'upx_exclude': [None, 'pb_UpxExclude', None], 'console_window_control': [None, 'rb_ConsoleWindowControl_C', None], 'hide_console': [None, 'pb_HideConsole', None],
                            'add_icon': [None, 'pb_AddIcon', None], 'disable_windowed': [None, 'cb_DisableWindowed', None], 'version_file': [None, 'pb_VersionFile', None], 'add_xml_file': [None, 'pb_AddXmlFile', None], 
                            'add_resource': [None, 'pb_AddResource', None], 'uac_admin_apply': [None, 'cb_UacAdminApply', None], 'uac_uiaccess': [None, 'cb_UacUiaccess', None],
                            'argv_emulation': [None, 'cb_ArgvEmulation', None], 'osx_bundle_identifier': [None, 'pb_OsxBundleIdentifier', None], 'target_architecture': [None, 'pb_TargetArchitecture', None], 'codesign_identity': [None, 'pb_CodesignIdentity', None], 'osx_entitlements_file': [None, 'pb_OsxEntitlementsFile', None],
                            'runtime_tmpdir': [None, 'pb_RuntimeTmpdir', None], 'ignore_signals': [None, 'cb_IgnoreSignals', None], 'output_folder_path': [None, 'pte_OutputPath', None], 'workpath_option': [None, 'pb_WorkpathOption', None], 'noconfirm_option': [None, 'cb_NoconfirmOption', None],
                            'upx_dir': [None, 'pb_UpxDir', None], 'clear_cache': [None, 'cb_ClearCache', None], 'log_level': [None, 'pb_LogLevel', None], 'python_file_path': [None, 'pte_FilePath', None]
                        }
        self.cmd = [None]*3
        self.cmd[0] = os.path.splitdrive(workspace_path)[0]
        self.cmd[1] = 'cd '+ workspace_path
        self.cmd_dict['output_methode'][0] = 'pyinstaller -F'
        self.cmd_dict['output_methode'][2] = self.json_widgets['rb_OutputMethod_F']['dict_explain']
        self.cmd_dict['clear_cache'][0] = '--clean'
        self.cmd_dict['clear_cache'][2] = self.json_widgets['cb_ClearCache']['dict_explain']
        self.cmd_dict['console_window_control'][0] = '--console'
        self.cmd_dict['console_window_control'][2] = self.json_widgets['rb_ConsoleWindowControl_C']['dict_explain']
        # 用作恢复控制台参数的缓存
        self.recover_cmd_dict = deepcopy(self.cmd_dict)
        # 用于控制恢复显示的缓存cb,rb
        self.recover_cb = []
        self.recover_rb = []
        self.recover_lock = []

    # 信号连接初始化
    def py_to_exe_ui_signal_connection(self):
        self.Win.pte_FilePath.textChanged.connect(self.file_path_changed)
        self.Win.pte_OutputPath.textChanged.connect(self.plain_text_update)
        self.Win.pte_FileName.textChanged.connect(self.plain_text_update)
        self.Win.pb_FilePath.clicked.connect(self.select_py_file)
        self.Win.pb_OutputPath.clicked.connect(self.select_ourput_folder)
        self.Win.pb_Recover.clicked.connect(self.recover)
        self.Win.pb_ClearAll.clicked.connect(self.clear_all)
        self.Win.pb_ClearConsole.clicked.connect(self.clear_console_display)
        self.Win.pb_ClearInfo.clicked.connect(self.clear_Info_display)
        self.Win.pb_ClearAllDisplay.clicked.connect(self.clear_all_display)
        self.Win.pb_ClearInput.clicked.connect(self.clear_input)
        self.Win.pb_ShowParameter.clicked.connect(self.parameter_display)
        self.Win.pb_OpenDir.clicked.connect(self.open_output_folder)
        self.Win.pb_Print.clicked.connect(self.print_cmd)
        self.Win.cbb_LanguageSelect.currentTextChanged.connect(self.language_update)
        self.Win.cb_Tooltips.stateChanged.connect(self.language_update)

# 界面文字初始化及更改
    def load_language_json_file(self):
        try:
            json_file_name = self.Win.cbb_LanguageSelect.currentText() + '.json'
            with open(os.path.join(exe_folder_path, 'Languages', json_file_name), 'r',encoding = 'utf-8') as file:
                self.language_json = json.load(file)
            self.json_widgets = self.language_json['widgets']
            self.json_special = self.language_json['special']
            self.json_general = self.language_json['general']
        except Exception as e:
            # traceback.print_exc()
            QMessageBox.warning(None, text=e)
            # self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    def combo_list_init(self):
        try:
            file_list = os.listdir(os.path.join(exe_folder_path, 'Languages'))
            self.language_list = []
            for file in file_list:
                if file.endswith('.json'):
                    self.language_list.append(os.path.splitext(file)[0])
                    self.Win.cbb_LanguageSelect.addItem(os.path.splitext(file)[0])
            for perfer_language in ['Chinese_S','Chinese_simplified','ChineseSimplified', 'Chinese','中文简体','简体中文','中文']:
                if perfer_language in self.language_list:
                    self.Win.cbb_LanguageSelect.setCurrentText(perfer_language)
                    break
            self.load_language_json_file()
        except Exception as e:
            # traceback.print_exc()
            QMessageBox.warning(None, self.json_general["msg_info"], '语言包(./Language)缺失，可能无法进行正常显示\n\nDas Sprachpaket (./Language) fehlt, möglicherweise können die Inhalte nicht ordnungsgemäß angezeigt werden\n\nThe language pack (./Language) is missing, normal display may not be possible.\n')
            self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    def set_text_init(self):
        try:
            for name, value in self.json_widgets.items():
                if 'text' in value:
                    getattr(self.Win, name).setText(value['text'])
                if self.Win.cb_Tooltips.isChecked() and 'tooltip' in value:
                    getattr(self.Win, name).setToolTip(value['tooltip'])
            self.setWindowTitle(self.json_special['window_title'] + '\t\t\t\t' + workspace_path)
        except Exception as e:
            # traceback.print_exc()
            self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    def language_update(self):
        self.load_language_json_file()
        self.set_text_init()

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

    # ****************************************从字典中获取实际command执行命令函数****************************************
    def get_command_from_dict(self):
        temp_command = []
        for value in self.cmd_dict.values():
            temp_command.append(value[0])
        temp_command_final = ' '.join(filter(None, temp_command))
        return(temp_command_final)

    # ****************************************清空函数****************************************
    # 清空控制台显示
    def clear_console_display(self):
        self.Win.textBrowser_cmd.clear()
    # 清空信息台显示
    def clear_Info_display(self):
        self.Win.textBrowser.clear()
    # 清空显示
    def clear_all_display(self):
        self.Win.textBrowser.clear()
        self.Win.textBrowser_cmd.clear()
    # 清空输入
    def clear_input(self):
        action_reply = self.set_custom_message_box(self.json_general["msg_warning"], self.json_widgets['pb_ClearInput']['msg_content'], [self.json_widgets['pb_ClearInput']['pb_certain_clear']], messagebox_content_icon=QMessageBox.Warning)
        if action_reply == 1:
            pass
        else: return False
        self.recover_cmd_dict = deepcopy(self.cmd_dict)
        if not self.Win.pb_Recover.isVisible():
            self.Win.pb_Recover.show()
        self.Win.pte_FilePath.clear()
        self.Win.pte_FileName.clear()
        self.Win.pte_OutputPath.clear()
        for value in self.cmd_dict.values():
            value[0] = None
            value[2] = None
        self.recover_cb = [[checkbox_item, checkbox_item.isChecked()] for checkbox_item in self.Win.frame_cb.findChildren(QCheckBox)]
        self.recover_rb = [[radio_button_item, radio_button_item.isChecked()] for radio_button_item in self.Win.frame_rb.findChildren(QRadioButton)]
        self.recover_lock = [[radio_button_item, radio_button_item.isChecked()] for radio_button_item in self.Win.frame_FileInfo.findChildren(QRadioButton)]
        for i in self.recover_cb: i[0].setChecked(False)
        for i in self.recover_lock: i[0].setChecked(False)
        self.Win.cb_ClearCache.setChecked(True)
        self.Win.cb_ClearFileAfterLaunchFlagChange.setChecked(True)
        self.Win.rb_OutputMethod_F.setChecked(True)
        self.Win.rb_ConsoleWindowControl_C.setChecked(True)
        # 重置参数
        reset_py_file_path = self.recover_cmd_dict['python_file_path'][0].split('"')[1]
        self.Win.pte_FilePath.setPlainText(reset_py_file_path)
        self.Win.pte_OutputPath.setPlainText(os.path.dirname(reset_py_file_path))
        self.Win.pte_FileName.setPlainText(os.path.splitext(os.path.basename(reset_py_file_path))[0])
        self.cmd_dict['output_methode'][0] = 'pyinstaller -F'
        self.cmd_dict['output_methode'][2] = self.json_widgets['rb_OutputMethod_F']['dict_explain']
        self.cmd_dict['clear_cache'][0] = '--clean'
        self.cmd_dict['clear_cache'][2] = self.json_widgets['cb_ClearCache']['dict_explain']
        self.cmd_dict['console_window_control'][0] = '--console'
        self.cmd_dict['console_window_control'][2] = self.json_widgets['rb_ConsoleWindowControl_C']['dict_explain']
        return True
    
    # 清空所有
    def clear_all(self):
        clear_flag = self.clear_input()
        if clear_flag:
            self.clear_all_display()
    
    # 恢复清空前的数据
    def recover(self):
        try:
            self.cmd_dict = deepcopy(self.recover_cmd_dict)
            for i in self.recover_cb:
                i[0].setChecked(i[1])
            for i in self.recover_rb:
                i[0].setChecked(i[1])
            for i in self.recover_lock:
                i[0].setChecked(i[1])
            if self.recover_cmd_dict['python_file_path'][0]:
                self.Win.pte_FilePath.setPlainText(self.recover_cmd_dict['python_file_path'][0].split('"')[1])
            if self.recover_cmd_dict['output_folder_path'][0]:
                self.Win.pte_OutputPath.setPlainText(self.recover_cmd_dict['output_folder_path'][0].split('"')[1])
            if self.recover_cmd_dict['output_file_name'][0]:
                self.Win.pte_FileName.setPlainText(self.recover_cmd_dict['output_file_name'][0].split('"')[1])
            self.Win.pb_Recover.hide()
        except Exception as e:
            # traceback.print_exc()
            self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************显示参数****************************************
    def parameter_display(self):
        try:
            self.append_TB_text(f'__________  {self.json_general["display_command_parameter"]}  __________\n')
            for value in self.cmd_dict.values():
                if value[0]:
                    command_display = str(self.json_widgets[value[1]]["dict"] + value[2])
                    self.append_TB_text(command_display, self.Win.textBrowser)
            self.append_TB_text(f'__________  {self.json_general["all_parameter"]}  __________\n\n')
        except Exception as e:
            # traceback.print_exc()
            QMessageBox.warning(None, '警告Warning', str(e))
            # self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************打印参数到txt****************************************
    def print_cmd(self):
        print_command_path = os.path.join(workspace_path, 'output_command_of_pyinstaller.txt')
        self.cmd[2] = self.get_command_from_dict()
        try:
            with open(print_command_path, 'w', encoding='utf-8') as file:
                file.write(self.cmd[0] + '\n')
                file.write(self.cmd[1] + '\n')
                file.write(self.cmd[2] + '\n')
            QMessageBox.information(None, self.json_general["msg_info"], f'{self.json_special["print_cmd"]}<br>{print_command_path}')
            QDesktopServices.openUrl(
                            QUrl.fromLocalFile(workspace_path))
        except Exception as e:
            # traceback.print_exc()
            self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************打开输出文件夹****************************************
    def open_output_folder(self):
        try:
            if self.cmd_dict['python_file_path'][0] and os.path.exists(self.cmd_dict['output_folder_path'][0].split('"')[1]):
                folder_path = self.cmd_dict['output_folder_path'][0].split('"')[1]
            elif workspace_path:
                QMessageBox.information(None, self.json_general["msg_info"], self.json_special['open_output_folder']['no_folder'])
                folder_path = workspace_path
            else:
                QMessageBox.information(None, self.json_general["msg_info"], self.json_special['open_output_folder']['no_file'])
                return
            QDesktopServices.openUrl(
                        QUrl.fromLocalFile(folder_path))
        except Exception as e:
            # traceback.print_exc()
            self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************向Textbrowser添加内容****************************************
    def append_TB_text(self, text_content: str, textBrowser_object: object = None):
        if not textBrowser_object:
            textBrowser_object = self.Win.textBrowser
        try:
            textBrowser_object.moveCursor(QTextCursor.End)
            textBrowser_object.insertPlainText(text_content + "\n")
            textBrowser_object.moveCursor(QTextCursor.End)
        except Exception as e:
            textBrowser_object.moveCursor(QTextCursor.End)
            textBrowser_object.insertPlainText(e + "\n")
            textBrowser_object.moveCursor(QTextCursor.End)
    
    def clear_file_after_launch_flag_change(self):
        if self.Win.cb_ClearFileAfterLaunchFlagChange.isChecked():
            self.clear_file_flag = True
        else:
            self.clear_file_flag = False
    
    # ****************************************文件浏览选择****************************************
    def select_py_file(self):
        temp = self.select_file(self.json_special['select_py_file']['text_browser_display'], self.json_special['select_py_file']['dialog_title'], self.json_special['select_py_file']['type_discription'])
        self.Win.pte_FilePath.setPlainText(temp)
        self.cmd_dict['python_file_path'][0].split('"')[1] = temp
        self.cmd_dict['python_file_path'][0] = ''.join(self.cmd_dict['python_file_path'][0])          
    
    def select_ourput_folder(self):
        temp = self.select_folder(self.json_special['select_ourput_folder']['text_browser_display'], self.json_special['select_ourput_folder']['dialog_title'])
        self.Win.pte_OutputPath.setPlainText(temp)
        self.cmd_dict['output_folder_path'][0].split('"')[1] = temp
        self.cmd_dict['output_folder_path'][0] = ''.join(self.cmd_dict['output_folder_path'][0])  
        self.temp = self.cmd_dict['output_folder_path'][0].split('"')    
    
    # ****************************************通用文件浏览选择****************************************
    def select_file(self, display_text:str = '', window_title:str = '', file_discription:str = '') -> str :
        options = QFileDialog.Options()
        try:
            receiver_temp, _ = QFileDialog.getOpenFileName(self, f'{window_title}', '', f'{file_discription}', options=options)
            if receiver_temp:
                self.append_TB_text(f'__________ {self.json_general["setting_update"]}{display_text} __________\n{receiver_temp}\n')
                return receiver_temp
            return
        except Exception as e:
            # traceback.print_exc()
            self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    def select_folder(self, display_text:str = '', window_title:str = '') -> str :
        options = QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        try:
            receiver_temp = QFileDialog.getExistingDirectory(self, f'{window_title}', '', options=options)
            if receiver_temp:
                self.append_TB_text(f'__________ {self.json_general["setting_update"]}{display_text} __________\n{receiver_temp}\n')
                return receiver_temp
            return None
        except Exception as e:
            # traceback.print_exc()
            self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************自定义对话窗口****************************************
    def set_custom_message_box(self, window_title:str, description:str, button_list:list, reset_flag:bool = False, default_button:int = -1, window_icon = None, messagebox_content_icon = QMessageBox.Question) :
        if not window_icon:
            window_icon = self.WINDOW_ICON
        msg_box = QMessageBox()
        msg_box.setIcon(messagebox_content_icon)
        msg_box.setWindowIcon(window_icon)
        msg_box.setWindowTitle(window_title)
        msg_box.setText(description)
        buttons = []
        
        if reset_flag:
            button_reset = QPushButton(self.json_general['pb_reset'])
        else:
            button_reset = QPushButton('')
        msg_box.addButton(button_reset, QMessageBox.ResetRole)
        buttons.append(button_reset)
        
        for i in range(len(button_list)):
            button = QPushButton(button_list[i])
            msg_box.addButton(button, QMessageBox.YesRole)
            buttons.append(button)
        
        button_cancel = QPushButton(self.json_general['pb_cancel'])
        msg_box.addButton(button_cancel, QMessageBox.NoRole)
        buttons.append(button_cancel)
        msg_box.setDefaultButton(buttons[default_button])
        
        return msg_box.exec_()
    
    # ****************************************询问文件还是文件夹对话窗口****************************************
    def type_select_dialog(self, display_text, file_type = None):
        if not file_type:
            file_type = f'{self.json_general["type_all_files"]}(*.*)'
        action_reply = self.set_custom_message_box(self.json_special['type_select_dialog']['msg_title'], self.json_special['type_select_dialog']['msg_content'], [self.json_general['folder'], self.json_general['file']])
        if action_reply == 1:
            temp = self.select_folder(display_text, )
        elif action_reply == 2:
            temp = self.select_file(display_text, self.json_general['select_file'], file_type)
        else: return
        return temp
    
    # ****************************************自定义项目显示窗口****************************************
    def set_custom_list_widget(self, display_text, window_title, item_list, type_select_flag = 'file_folder', file_type = None, text_discription = None, extra_func = None, window_icon = None):
        if not window_icon:
            window_icon = self.WINDOW_ICON
        if not file_type:
            file_type = f'{self.json_general["type_all_files"]}(*.*)'
        if not text_discription:
            text_discription = self.json_general['input_specified_data']
        dialog = QDialog()
        dialog.setWindowTitle(window_title)
        dialog.resize(600,500)
        dialog.setWindowIcon(window_icon)
        dialog.setStyleSheet(
            "QDialog{min-width:600px; min-height:500px;}"
            "QFrame[objectName = 'frame_add_remove']{margin:0; padding:0; max-height:50px;}"
            "QFrame[objectName = 'frame_finish_cancel']{margin:0; padding:0; max-height:35px;}"
            "QPushButton{min-height: 30px; max-height: 30px;}"
        )
        list_widget = QListWidget()
        
        if item_list:
            list_widget.addItems(item_list)
        pb_add = QPushButton(self.json_general['pb_add'])
        pb_remove = QPushButton(self.json_general['pb_remove'])
        pb_finish = QPushButton(self.json_general['pb_certain'])
        pb_cancel = QPushButton(self.json_general['pb_cancel'])
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        frame_add_remove = QFrame()
        frame_add_remove.setObjectName('frame_add_remove')
        add_remove_layout = QHBoxLayout(frame_add_remove)
        add_remove_layout.setContentsMargins(0, 0, 0, 0)
        add_remove_layout.setSpacing(10)
        
        if type_select_flag == 'image':
            lb_preview = QLabel()
            lb_preview.setFixedSize(50, 50)
            lb_preview.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            add_remove_layout.addWidget(lb_preview)
        add_remove_layout.addItem(spacer_item)
        if extra_func == 'edit_info':
            pb_edit_info = QPushButton(self.json_general['specified_info'])
            add_remove_layout.addWidget(pb_edit_info)
        add_remove_layout.addWidget(pb_add)
        add_remove_layout.addWidget(pb_remove)
        
        frame_finish_cancel = QFrame()
        frame_finish_cancel.setObjectName('frame_finish_cancel')
        finish_cancel_layout = QHBoxLayout(frame_finish_cancel)
        finish_cancel_layout.setContentsMargins(0, 0, 0, 0)
        finish_cancel_layout.setSpacing(10)
        finish_cancel_layout.addWidget(pb_finish)
        finish_cancel_layout.addWidget(pb_cancel)

        main_layout = QVBoxLayout(dialog)
        main_layout.addWidget(list_widget)
        main_layout.addWidget(frame_add_remove)
        main_layout.addWidget(frame_finish_cancel)
        
        def preview_image():
            current_row = list_widget.currentRow()
            if current_row >= 0 and current_row <= list_widget.count():
                selected_item_text = list_widget.item(current_row).text()
                pixmap = QPixmap(selected_item_text)
                lb_preview.setPixmap(pixmap.scaled(lb_preview.size(), Qt.KeepAspectRatio))
        def edit_info():
            current_items = [list_widget.item(i).text() for i in range(list_widget.count())]
            current_row = list_widget.currentRow()
            if current_row >= 0 and current_row < list_widget.count():
                original = list_widget.item(current_row).text()
                temp_input, _ = QInputDialog.getText(None, self.json_general['input_specified_data'], self.json_widgets['pb_AddResource']['msg_content'])
                if temp_input:
                    temp_content = original.split(',')[0] + ',' + temp_input
                if temp_content in current_items:
                    QMessageBox.information(None, self.json_general["msg_info"], f'{self.json_general["redundant_info"]}<br>{temp_input}<br>')
                else:
                    list_widget.item(current_row).setText(temp_content)
                
        def line_edit_input():
            temp = QInputDialog.getText(None, self.json_general['input_specified_data'], text_discription)[0]
            if temp:
                return temp
            else: return None
        
        def add_item():
            current_items = [list_widget.item(i).text() for i in range(list_widget.count())]
            if type_select_flag == 'file' or type_select_flag == 'image':
                temp = self.select_file(display_text, self.json_general['select_file'], file_type)
            elif type_select_flag == 'folder':
                temp = self.select_folder(display_text, self.json_general['select_folder'])
            elif type_select_flag == 'file_folder':
                temp = self.type_select_dialog(display_text, file_type)
            elif type_select_flag == 'text':
                temp = line_edit_input()
                self.append_TB_text(f'__________ {self.json_general["setting_update"]}{display_text} __________\n{temp}\n')
            if temp in current_items:
                QMessageBox.information(None, self.json_general["msg_info"], f'{self.json_general["redundant_info"]}<br>{temp}<br>')
            else:
                list_widget.addItem(temp)
            
        if extra_func == 'edit_info':
                pb_edit_info.clicked.connect(edit_info)
        
        def remove_item():
            current_row = list_widget.currentRow()
            if current_row >= 0 and current_row < list_widget.count():
                list_widget.takeItem(current_row)
            elif list_widget.count == 0:
                list_widget.clear()
        
        pb_add.clicked.connect(add_item)
        pb_remove.clicked.connect(remove_item)
        pb_finish.clicked.connect(dialog.accept)
        pb_cancel.clicked.connect(dialog.reject)
        
        if type_select_flag == 'image':
            list_widget.currentRowChanged.connect(preview_image)
        result = dialog.exec_()
        
        if result == QDialog.Accepted:
            selected_items = [list_widget.item(i).text() for i in range(list_widget.count())]
            return selected_items