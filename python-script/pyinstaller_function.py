import os
import subprocess
import threading

from PyToExeUI import *
from Function_QThread import *

from PyQt5.QtWidgets import  QMessageBox, QInputDialog

class Pyinstaller_function(PyToExeUI):
    def __init__(self):
        super().__init__()
        self.pyinstaller_function_signal_connection()
        # self.pyinstaller_function_parameter_init()
    
    # def pyinstaller_function_parameter_init(self):
    #     self.connection_sign = None
    
    def pyinstaller_function_signal_connection(self):
        # **********************按钮类**********************
        self.Win.pb_Launch.clicked.connect(self.launch_cmd)
        self.Win.pb_SetupPyinstaller.clicked.connect(self.setup_pyinstaller)
        self.Win.pb_VersionDisplay.clicked.connect(self.version_display)
        self.Win.pb_HelpDisplay.clicked.connect(self.help_display)
        
        self.Win.pb_AddBinaryData.clicked.connect(self.add_binary_data)
        self.Win.pb_AddFileFolderData.clicked.connect(self.add_file_folder_data)
        self.Win.pb_AddIcon.clicked.connect(self.add_icon)
        self.Win.pb_AdditionalHooksDir.clicked.connect(self.additional_hooks_dir)
        self.Win.pb_AddResource.clicked.connect(self.add_resource)
        self.Win.pb_AddSplashScreen.clicked.connect(self.add_splash_screen)
        self.Win.pb_AddXmlFile.clicked.connect(self.add_xml_file)
        self.Win.pb_ImportsFolder.clicked.connect(self.imports_folder)
        self.Win.pb_ImportModuleName.clicked.connect(self.import_module_name)
        self.Win.pb_VersionFile.clicked.connect(self.version_file)
        self.Win.pb_CollectSubmodules.clicked.connect(self.collect_submodules)
        self.Win.pb_CopyMetadata.clicked.connect(self.copy_metadata)
        self.Win.pb_RecursiveCopyMetadata.clicked.connect(self.recursive_copy_metadata)
        self.Win.pb_CollectData.clicked.connect(self.collect_data)
        self.Win.pb_CollectAll.clicked.connect(self.collect_all)
        self.Win.pb_CollectBinaries.clicked.connect(self.collect_binaries)
        self.Win.pb_RuntimeHook.clicked.connect(self.runtime_hook)
        self.Win.pb_TargetArchitecture.clicked.connect(self.target_architecture)
        self.Win.pb_CodesignIdentity.clicked.connect(self.codesign_identity)
        self.Win.pb_OsxEntitlementsFile.clicked.connect(self.osx_entitlements_file)
        self.Win.pb_ExcludeModule.clicked.connect(self.exclude_module)
        self.Win.pb_UpxExclude.clicked.connect(self.upx_exclude)
        self.Win.pb_UpxDir.clicked.connect(self.upx_dir)
        self.Win.pb_LogLevel.clicked.connect(self.log_level)
        self.Win.pb_RuntimeTmpdir.clicked.connect(self.runtime_tmpdir)
        self.Win.pb_WorkpathOption.clicked.connect(self.workpath_option)
        self.Win.pb_Specpath.clicked.connect(self.specpath)
        self.Win.pb_DebugMode.clicked.connect(self.debug_mode)
        self.Win.pb_PythonOption.clicked.connect(self.python_option)
        self.Win.pb_HideConsole.clicked.connect(self.hide_console)
        self.Win.pb_OsxBundleIdentifier.clicked.connect(self.osx_bundle_identifier)
        # self.Win.pb_.clicked.connect(self.)
        
        
        # **********************勾选框按钮类**********************
        self.Win.cb_DisableWindowed.stateChanged.connect(self.disable_windowed)
        self.Win.cb_UacAdminApply.stateChanged.connect(self.uac_admin_apply)
        self.Win.cb_IgnoreSignals.stateChanged.connect(self.ignore_signals)
        
        self.Win.cb_UacUiaccess.stateChanged.connect(self.uac_uiaccess)
        self.Win.cb_ArgvEmulation.stateChanged.connect(self.argv_emulation)
        self.Win.cb_NoupxOption.stateChanged.connect(self.noupx_option)
        self.Win.cb_NoconfirmOption.stateChanged.connect(self.noconfirm_option)
        self.Win.cb_ClearCache.stateChanged.connect(self.clear_cache)
        self.Win.cb_ClearFileAfterLaunchFlagChange.stateChanged.connect(self.clear_file_after_launch_flag_change)
        self.Win.cb_StripOption.stateChanged.connect(self.strip_option)
        # self.cb_.stateChanged.connect(self.)
        
        
        # **********************选择按钮类**********************
        self.Win.rb_OutputMethod_F.clicked.connect(self.output_methode)
        self.Win.rb_OutputMethod_D.clicked.connect(self.output_methode)
        self.Win.rb_ConsoleWindowControl_C.clicked.connect(self.console_window_control)
        self.Win.rb_ConsoleWindowControl_NW.clicked.connect(self.console_window_control)
        self.Win.rb_ConsoleWindowControl_W.clicked.connect(self.console_window_control)
        self.Win.rb_ConsoleWindowControl_NC.clicked.connect(self.console_window_control)
        # self.Win.rb_.clicked.connect(self.)
    
    

    # ****************************************pyinstaller具体功能****************************************
    # 安装pyinstaller项
    def setup_pyinstaller(self):
        self.pyinstaller_Qthread = pyinstaller_setup_Qthread()
        self.pyinstaller_Qthread.output_to_textbrowser_cmd.connect(lambda content: self.append_TB_text(content, self.Win.textBrowser_cmd))
        self.pyinstaller_Qthread.output_to_textbrowser.connect(lambda content: self.append_TB_text(content, self.Win.textBrowser))
        self.pyinstaller_Qthread.start()
    
    # 版本项
    def version_display(self):
        process = subprocess.Popen('pyinstaller -v', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        display_threading = threading.Thread(target = self.read_output, args=(process, '已显示Pyinstaller版本信息','当前pyinstaller的版本信息',))
        display_threading.start()
    
    # 帮助项
    def help_display(self):
        process = subprocess.Popen('pyinstaller -h', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        display_threading = threading.Thread(target = self.read_output, args=(process, '已显示Pyinstaller帮助信息','以上为pyinstaller的帮助信息',))
        display_threading.start()
    
    # [00] 项 创建一个单文件的可执行文件 或 创建包含可执行文件的一个文件夹束
    def output_methode(self):
        if self.Win.rb_OutputMethod_F.isChecked():
            self.cmd_dict['output_methode'][0] = 'pyinstaller -F'
            self.cmd_dict['output_methode'][2] = '生成单个文件'
            self.cmd_dict['contents_directory'][0] = None
        else:
            self.cmd_dict['output_methode'][0] = 'pyinstaller -D'
            self.cmd_dict['output_methode'][2] = '生成单个文件夹'
            self.contents_directory()
    
    # [01] 项 用于指定生成的 spec 文件的保存路径。Spec 文件是 PyInstaller 构建过程中生成的中间文件，它描述了构建配置的详细信息，包括输入脚本、依赖项、输出路径等。
    def specpath(self):
        try:
            if self.cmd_dict['specpath'][0]:
                current_data = self.cmd_dict['specpath'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前为：{current_data}<br>是否替换原文件选项路径<br>', ['替换'], True)
                if action_reply == 0:
                    self.cmd_dict['specpath'][0] = None
                    self.cmd_dict['specpath'][2] = None
                    return
                elif action_reply == 1:
                    pass
                else: return
            temp = self.select_folder('添加spec文件的保存路径', '请选择spec文件的保存路径')
            if temp:
                self.cmd_dict['specpath'][0] = '--specpath="'+ temp + '"'
                self.cmd_dict['specpath'][2] = self.cmd_dict['specpath'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [02] 项 pte_FileName 分配给打包应用程序和spec文件的名称
    # 具体内容写在了函数 PyToExeUI.py 中的 plain_text_update() 中
    
    # [03] 项 仅对于 onedir 构建，指定所有支持文件所在的目录名称（即除了可执行文件本身之外的所有内容）都将被放入。
    def contents_directory(self):
        try:
            if not self.Win.rb_OutputMethod_D.isChecked():
                return
            action_reply = self.set_custom_message_box('可选操作', '是否指定输出文件夹 <br>除了可执行文件本身之外的所有内容都将被放入其中<br>', ['设置'], True)
            # 重置键
            if action_reply == 0:
                self.cmd_dict['contents_directory'][0] = None
                self.cmd_dict['contents_directory'][2] = None
                return
            # 设置键
            elif action_reply == 1:
                pass
            else: return
            temp = os.path.basename(QInputDialog.getText(None, '请输入文件夹名称', '请输入文件夹名称，用于放置除.exe外的其他数据<br>')[0])
            if temp:
                self.cmd_dict['contents_directory'][0] = '--contents-directory="' + temp + '"'
                self.cmd_dict['contents_directory'][2] = self.cmd_dict['contents_directory'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [04] 项 [可重复使用] 用于添加数据文件到可执行文件中的选项。它允许将指定的文件或目录复制到生成的可执行文件所在的目录中。这对于包含资源文件（如图像、配置文件等）在可执行文件中是很有用的。
    def add_file_folder_data(self):
        try:
            # 数据处理，将原数据中引号部分提取出来，并对其进行处理，使其变为路径
            currenr_list = self.cmd_dict['add_file_folder_data'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    base_name = content_quotation.split(':')[0]
                    relative_path = os.path.abspath(content_quotation.split(':')[1])
                    content = os.path.join(relative_path, base_name)
                    content_list.append(content)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新用于添加到可执行文件中的文件','请选择用于添加到可执行文件中的文件', content_list)
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--add-data="' + os.path.basename(i) + ':' + os.path.relpath(os.path.dirname(i), workspace_path) + '"'
                    command_list.append(command)
                self.cmd_dict['add_file_folder_data'][0] = ' '.join(command_list)
                self.cmd_dict['add_file_folder_data'][2] = self.cmd_dict['add_file_folder_data'][0]
            else:
                self.cmd_dict['add_file_folder_data'][0] = None
                self.cmd_dict['add_file_folder_data'][2] = self.cmd_dict['add_file_folder_data'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [05] 项 [可重复使用] 用于将二进制文件添加到生成的可执行文件中。该选项允许将外部二进制文件嵌入到生成的可执行文件中，以便在运行时可以访问这些文件。
    def add_binary_data(self):
        try:
            # 数据处理，将原数据中引号部分提取出来，并对其进行处理，使其变为路径
            currenr_list = self.cmd_dict['add_binary_data'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    base_name = content_quotation.split(':')[0]
                    relative_path = os.path.abspath(content_quotation.split(':')[1])
                    content = os.path.join(relative_path, base_name)
                    content_list.append(content)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新二进制文件', '请选择用于添加到可执行文件中的二进制文件', content_list, 'file_folder')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--add-binary="' + os.path.basename(i) + ':' + os.path.relpath(os.path.dirname(i), workspace_path) + '"'
                    command_list.append(command)
                self.cmd_dict['add_binary_data'][0] = ' '.join(command_list)
                self.cmd_dict['add_binary_data'][2] = self.cmd_dict['add_binary_data'][0]
            else:
                self.cmd_dict['add_binary_data'][0] = None
                self.cmd_dict['add_binary_data'][2] = self.cmd_dict['add_binary_data'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [06] 项 [可重复使用] 用于指定导入模块时的搜索路径，可多次调用。通过这个选项可以将额外的目录添加到 Python 模块搜索路径中，以确保程序在运行时能够找到需要的模块。这个选项可以帮助解决程序在运行时找不到特定模块的问题，尤其是当输出应用程序依赖于一些不在默认搜索路径中的自定义模块时
    def imports_folder(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['imports_folder'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            print('d')
            temp_command_list= self.set_custom_list_widget('更新导入模块时的搜索路径', '请选择指定 Python 模块搜索路径', content_list, 'folder')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--paths="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['imports_folder'][0] = ' '.join(command_list)
                self.cmd_dict['imports_folder'][2] = self.cmd_dict['imports_folder'][0]
            else:
                self.cmd_dict['imports_folder'][0] = None
                self.cmd_dict['imports_folder'][2] = self.cmd_dict['imports_folder'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [07] 项 [可重复使用] 用于指定需要在生成的可执行文件中包含的未在源代码中显式导入的 Python 模块。有时，一些模块可能是在运行时动态导入或被其他模块隐式地导入，而不是在源代码中显式导入。此选项可以使用多次。
    def import_module_name(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['import_module_name'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新显式导入的Python模块', '请输入外部import的模块名称', content_list, 'text', text_discription='请输入需要从外部import的模块名称:<br>用于指定需要在生成的可执行文件中包含的未在源代码中显式导入的 Python 模块<br>')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--hidden-import="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['import_module_name'][0] = ' '.join(command_list)
                self.cmd_dict['import_module_name'][2] = self.cmd_dict['import_module_name'][0]
            else:
                self.cmd_dict['import_module_name'][0] = None
                self.cmd_dict['import_module_name'][2] = self.cmd_dict['import_module_name'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [08] 项 [可重复使用] 用于在打包过程中显式地收集指定模块及其所有子模块。该选项可用于确保 PyInstaller 包含指定模块及其子模块，即使它们没有在源代码中被显式导入
    def collect_submodules(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['collect_submodules'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新打包过程中显式地收集指定模块及其所有子模块', '请输入模块名称', content_list, 'text', text_discription='请输入模块名称:<br>用于在打包过程中显式地收集指定模块及其所有子模块<br>')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--collect-submodules="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['collect_submodules'][0] = ' '.join(command_list)
                self.cmd_dict['collect_submodules'][2] = self.cmd_dict['collect_submodules'][0]
            else:
                self.cmd_dict['collect_submodules'][0] = None
                self.cmd_dict['collect_submodules'][2] = self.cmd_dict['collect_submodules'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [09] 项 [可重复使用] 用于在打包过程中收集指定模块的数据文件。这个选项用于确保 PyInstaller 包含指定模块所需的数据文件，这些数据文件可能在运行时由模块动态加载。
    def collect_data(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['collect_data'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新打包过程中收集指定模块的数据文件', '请输入模块名称', content_list, 'text', text_discription='请输入需要打包数据的模块名称:<br>用于在打包过程中收集指定模块的数据文件。<br>这个选项用于确保 PyInstaller 包含指定模块所需的数据文件，这些数据文件可能在运行时由模块动态加载。<br>')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--collect-data="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['collect_data'][0] = ' '.join(command_list)
                self.cmd_dict['collect_data'][2] = self.cmd_dict['collect_data'][0]
            else:
                self.cmd_dict['collect_data'][0] = None
                self.cmd_dict['collect_data'][2] = self.cmd_dict['collect_data'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [10] 项 [可重复使用] 用于在打包过程中收集指定模块及其依赖的所有二进制文件。这个选项的作用是将模块及其相关的二进制文件包含在生成的可执行文件中。
    def collect_binaries(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['collect_binaries'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新打包过程中收集指定模块及其依赖的所有二进制文件', '请输入模块名称', content_list, 'text', text_discription='请输入需要打包二进制文件的模块名称:<br>用于在打包过程中收集指定模块及其依赖的所有二进制文件。<br>这个选项的作用是将模块及其相关的二进制文件包含在生成的可执行文件中。<br>')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--collect-binaries="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['collecollect_binaries'][0] = ' '.join(command_list)
                self.cmd_dict['collecollect_binaries'][2] = self.cmd_dict['collecollect_binaries'][0]
            else:
                self.cmd_dict['collecollect_binaries'][0] = None
                self.cmd_dict['collecollect_binaries'][2] = self.cmd_dict['collecollect_binaries'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [11] 项 [可重复使用] 用于在打包过程中收集指定模块及其依赖的所有数据文件、元数据等。这个选项的作用是尽可能地将指定模块及其相关的所有资源都包含在生成的可执行文件中。
    def collect_all(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['copy_metadata'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新打包过程中收集指定模块及其依赖的所有数据文件、元数据等', '请输入模块名称', content_list, 'text', text_discription='请输入需要打包所有数据的模块名称:<br>用于在打包过程中收集指定模块及其依赖的所有数据文件、元数据等。<br>这个选项的作用是尽可能地将指定模块及其相关的所有资源都包含在生成的可执行文件中。<br>')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--collect-all="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['collect_all'][0] = ' '.join(command_list)
                self.cmd_dict['collect_all'][2] = self.cmd_dict['collect_all'][0]
            else:
                self.cmd_dict['collect_all'][0] = None
                self.cmd_dict['collect_all'][2] = self.cmd_dict['collect_all'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [12] 项 [可重复使用] 用于在打包过程中将指定模块的元数据一起复制到生成的可执行文件中
    def copy_metadata(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['copy_metadata'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新打包过程中将指定模块的元数据', '请输入模块名称', content_list, 'text', text_discription='请输入需要打包元数据的模块名称:<br>用于在打包过程中将指定模块的元数据一起复制到生成的可执行文件中<br>')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--copy-metadata="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['copy_metadata'][0] = ' '.join(command_list)
                self.cmd_dict['copy_metadata'][2] = self.cmd_dict['copy_metadata'][0]
            else:
                self.cmd_dict['copy_metadata'][0] = None
                self.cmd_dict['copy_metadata'][2] = self.cmd_dict['copy_metadata'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [13] 项 [可重复使用] 用于在打包过程中递归地将指定包及其依赖的所有包的元数据一起复制到生成的可执行文件中。这样不仅包本身的元数据会被复制，还会包括其依赖项的元数据。
    def recursive_copy_metadata(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['recursive_copy_metadata'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新打包过程中递归地将指定包及其依赖的所有包的元数据', '请输入模块名称', content_list, 'text', text_discription='请输入需要打包元数据及其依赖的模块名称:<br>用于在打包过程中递归地将指定包及其依赖的所有包的元数据一起复制到生成的可执行文件中。<br>这样不仅包本身的元数据会被复制，还会包括其依赖项的元数据。<br>')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--recursive-copy-metadata="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['recursive_copy_metadata'][0] = ' '.join(command_list)
                self.cmd_dict['recursive_copy_metadata'][2] = self.cmd_dict['recursive_copy_metadata'][0]
            else:
                self.cmd_dict['recursive_copy_metadata'][0] = None
                self.cmd_dict['recursive_copy_metadata'][2] = self.cmd_dict['recursive_copy_metadata'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [14] 项 [可重复使用] 用于指定一个目录，其中包含用户提供的钩子脚本。这些钩子脚本用于告诉 PyInstaller 如何处理特定的模块或库，以确保它们正确地包含在生成的可执行文件中。
    def additional_hooks_dir(self):
        try:
            # 数据处理，将原数据中引号部分提取出来，并对其进行处理，使其变为路径
            currenr_list = self.cmd_dict['additional_hooks_dir'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新钩子脚本搜索目录', '请选择钩子脚本所在目录', content_list, 'folder')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--additional-hooks-dir="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['additional_hooks_dir'][0] = ' '.join(command_list)
                self.cmd_dict['additional_hooks_dir'][2] = self.cmd_dict['additional_hooks_dir'][0]
            else:
                self.cmd_dict['additional_hooks_dir'][0] = None
                self.cmd_dict['additional_hooks_dir'][2] = self.cmd_dict['additional_hooks_dir'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [15] 项 [可重复使用] 用于指定运行时的钩子脚本。这个选项允许你提供一个脚本，其中包含在生成的可执行文件运行时应该执行的特定操作。
    def runtime_hook(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['runtime_hook'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新运行时的钩子脚本路径', '请选择钩子脚本', content_list, 'file')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--runtime-hook="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['runtime_hook'][0] = ' '.join(command_list)
                self.cmd_dict['runtime_hook'][2] = self.cmd_dict['runtime_hook'][0]
            else:
                self.cmd_dict['runtime_hook'][0] = None
                self.cmd_dict['runtime_hook'][2] = self.cmd_dict['runtime_hook'][0]
            pass
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [16] 项 [可重复使用] 用于指定要在打包过程中排除的模块。这个选项允许你明确指定哪些模块不应该被包含在生成的可执行文件中。（Python 名称，而不是路径名称）
    def exclude_module(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['exclude_module'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新需要忽略的可选模块', '请输入模块名称', content_list, 'text', text_discription='请输入需要忽略的可选模块名称:<br>用于指定要在打包过程中排除的模块。<br>这个选项允许你明确指定哪些模块不应该被包含在生成的可执行文件中。<br>')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--exclude-module="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['exclude_module'][0] = ' '.join(command_list)
                self.cmd_dict['exclude_module'][2] = self.cmd_dict['exclude_module'][0]
            else:
                self.cmd_dict['exclude_module'][0] = None
                self.cmd_dict['exclude_module'][2] = self.cmd_dict['exclude_module'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [17] 项 将 IMAGE_FILE 图像添加为应用程序的启动画面
    def add_splash_screen(self):
        try:
            if self.cmd_dict['add_splash_screen'][0]:
                current_data = self.cmd_dict['add_splash_screen'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前为：{current_data}<br>是否替换原文件选项路径<br>', ['替换'], True)
                if action_reply == 0:
                    self.cmd_dict['add_splash_screen'][0] = None
                    self.cmd_dict['add_splash_screen'][2] = None
                    return
                elif action_reply == 1:
                    pass
                else: return
            temp = self.select_file('添加应用启动画面', '请选择启动画面', '所有图片(*.jpg *.jpeg *.png *.webp *.bmp *.tif *.gif *.pcx *.tga *.exif *.fpx *.svg *.psd *.cdr *.pcd *.dxf *.ufo *.eps *.ai *.raw *.WMF *.webp *.avif *.apng')
            if temp:
                self.cmd_dict['add_splash_screen'][0] = '--splash="'+ temp + '"'
                self.cmd_dict['add_splash_screen'][2] = self.cmd_dict['add_splash_screen'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [18] 项 用于设置调试模式，以便在打包过程中生成调试信息 [--debug {all,imports,bootloader,noarchive}]	
    def debug_mode(self):
        try:
            if self.cmd_dict['debug_mode'][2]:
                current_data = self.cmd_dict['debug_mode'][2]
            else: current_data = None
            action_reply = self.set_custom_message_box('日志输出级别', f'当前日志输出级别：<br>{current_data}<br><br>请选择Pyinstaller的日志输出级别：<br>',['all(全部)','imports(导入)','bootloader(引导加载程序)','noarchive(无存档)'], True)
            if action_reply == 0:
                self.cmd_dict['debug_mode'][0] = None
                self.cmd_dict['debug_mode'][2] = None
            elif action_reply == 1:
                self.cmd_dict['debug_mode'][0] = '--debug all'
                self.cmd_dict['debug_mode'][2] = self.cmd_dict['debug_mode'][0].split()[1]
            elif action_reply == 2:
                self.cmd_dict['debug_mode'][0] = '--debug imports'
                self.cmd_dict['debug_mode'][2] = self.cmd_dict['debug_mode'][0].split()[1]
            elif action_reply == 3:
                self.cmd_dict['debug_mode'][0] = '--debug bootloader'
                self.cmd_dict['debug_mode'][2] = self.cmd_dict['debug_mode'][0].split()[1]
            elif action_reply == 4:
                self.cmd_dict['debug_mode'][0] = '--debug noarchive'
                self.cmd_dict['debug_mode'][2] = self.cmd_dict['debug_mode'][0].split()[1]
            else: return
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [19] 项 用于向底层的 Python 解释器传递额外的命令行选项。该选项允许你在 PyInstaller 执行过程中向 Python 解释器传递特定的选项，以影响解释器的行为。目前支持 "v"（相当于 "--debug imports"）、"u" 和 "W <warning control>"
    def python_option(self):
        try:
            # 目前支持 "v"（相当于 "--debug imports"）、"u" 和 "W <warning control>"
            if self.cmd_dict['python_option'][2]:
                current_data = self.cmd_dict['python_option'][2]
            else: current_data = None
            action_reply = self.set_custom_message_box('Python解释器命令行选项', f'当前命令行选项：<br>{current_data}<br><br>请选择Pyinstaller的日志输出级别：<br>v：相当于--debug imports，启用详细的导入调试信息，有助于识别导入模块时的问题<br>u：通常用于非常规的用户自定义启动方式<br>W： <warning control>允许传递警告控制参数，该参数控制Python解释器中警告的行为<br><br>',
                                                        ['参数 v','参数 u','参数 w'], True)
            if action_reply == 0:
                self.cmd_dict['python_option'][0] = None
                self.cmd_dict['python_option'][2] = None
            elif action_reply == 1:
                self.cmd_dict['python_option'][0] = '--python-option v'
                self.cmd_dict['python_option'][2] = self.cmd_dict['python_option'][0].split()[1]
            elif action_reply == 2:
                self.cmd_dict['python_option'][0] = '--python-option u'
                self.cmd_dict['python_option'][2] = self.cmd_dict['python_option'][0].split()[1]
            elif action_reply == 3:
                self.cmd_dict['python_option'][0] = '--python-option w'
                self.cmd_dict['python_option'][2] = self.cmd_dict['python_option'][0].split()[1]
            else: return
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [20] 项 对可执行文件和共享库应用符号表剥离（不建议在 Windows上使用）。用于在打包过程中去除生成的可执行文件中的调试信息。调试信息包含了与源代码的关联信息，去除它们可以减小生成的可执行文件的大小。
    def strip_option(self):
        try:
            if self.Win.cb_StripOption.isChecked():
                self.cmd_dict['strip_option'][0] = '--strip'
                self.cmd_dict['strip_option'][2] = '剥离共享应用符号表'
            else: self.cmd_dict['strip_option'][0] = None
            self.cmd_dict['strip_option'][2] = None
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [21] 项 [--noupx]	用于在打包过程中禁用 UPX 压缩。UPX是一种用于可执行文件的压缩工具，可以显著减小可执行文件的大小。 即使可用，也不要使用UPX（在 Windows 和 *nix 之间工作方式不同）
    def noupx_option(self):
        try:
            if self.Win.cb_NoupxOption.isChecked():
                QMessageBox.information(None, '提示', 'UPX是一种用于可执行文件的压缩工具，可以显著减小可执行文件的大小<br><br>但即使可用，也不要使用 UPX（在 Windows 和 *nix 之间工作方式不同）<br>')
                self.cmd_dict['noupx_option'][0] = '--noupx'
                self.cmd_dict['noupx_option'][2] = '禁用 UPX 压缩'
            else: 
                self.cmd_dict['noupx_option'][0] = None
                self.cmd_dict['noupx_option'][2] = None
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [22] 项 [可重复使用]  UPX 压缩过程中要排除的文件。UPX是一种用于可执行文件的压缩工具，而 --upx-exclude 允许你指定一些文件不要被UPX压缩。
    def upx_exclude(self):
        try:
            if self.cmd_dict['upx_exclude'][0]:
                current_data = self.cmd_dict['upx_exclude'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前为：{current_data}<br>是否替换原文件选项路径<br>', ['替换'], True)
                if action_reply == 0:
                    self.cmd_dict['upx_exclude'][0] = None
                    self.cmd_dict['upx_exclude'][2] = None
                    return
                elif action_reply == 1:
                    pass
                else: return
            temp = self.select_file('添加在UPX压缩过程中要排除的文件', '请选择文件')
            if temp:
                self.cmd_dict['upx_exclude'][0] = '--upx-exclude="'+ temp + '"'
                self.cmd_dict['upx_exclude'][2] = self.cmd_dict['upx_exclude'][0]
            pass
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [23] 项 打开控制台窗口
    def console_window_control(self):
        if self.Win.rb_ConsoleWindowControl_C.isChecked():
            self.cmd_dict['console_window_control'][0] = '--console'
            self.cmd_dict['console_window_control'][2] = '打开控制台窗口(console)'
        elif self.Win.rb_ConsoleWindowControl_NW.isChecked():
            self.cmd_dict['console_window_control'][0] = '--nowindowed'
            self.cmd_dict['console_window_control'][2] = '打开控制台窗口(nowindowed)'
        elif self.Win.rb_ConsoleWindowControl_W.isChecked():
            self.cmd_dict['console_window_control'][0] = '--windowed'
            self.cmd_dict['console_window_control'][2] = '关闭控制台窗口(windowed)'
        else:
            self.cmd_dict['console_window_control'][0] = '--noconsole'
            self.cmd_dict['console_window_control'][2] = '关闭控制台窗口(console)'
    
    # [24] 项 [--hide-console {minimize-late,hide-early,minimize-early,hide-late}] 用于设置生成的可执行文件的控制台窗口的显示方式。这个选项接受以下参数 仅限 Windows：在启用控制台的可执行文件中，让引导加载程序自动隐藏或最小化，控制台窗口，如果程序拥有控制台窗口（即不是从，现有控制台窗口）。
    def hide_console(self): 
        try:
            if self.cmd_dict['hide_console'][2]:
                current_data = self.cmd_dict['hide_console'][2]
            else: current_data = None
            action_reply = self.set_custom_message_box('控制台窗口的显示方式', f'控制台窗口的显示方式：<br>{current_data}<br><br>请选择可执行文件的控制台窗口的显示方式：<br>minimize-late: 在运行时尽可能晚地最小化控制台窗口。<br>hide-early: 在运行时尽可能早地隐藏控制台窗口。<br>minimize-early: 在运行时尽可能早地最小化控制台窗口。<br>hide-late: 在运行时尽可能晚地隐藏控制台窗口。<br>',['minimize-late(最小化延迟)','hide-early(提前隐藏)','minimize-early(最小化提前)','hide-late(延迟隐藏)'], True)
            if action_reply == 0:
                self.cmd_dict['hide_console'][0] = None
                self.cmd_dict['hide_console'][2] = None
            elif action_reply == 1:
                self.cmd_dict['hide_console'][0] = '--hide-console=v'
                self.cmd_dict['hide_console'][2] = self.cmd_dict['hide_console'][0].split()[1]
            elif action_reply == 2:
                self.cmd_dict['hide_console'][0] = '--hide-console=v'
                self.cmd_dict['hide_console'][2] = self.cmd_dict['hide_console'][0].split()[1]
            elif action_reply == 3:
                self.cmd_dict['hide_console'][0] = '--hide-console=v'
                self.cmd_dict['hide_console'][2] = self.cmd_dict['hide_console'][0].split()[1]
            elif action_reply == 4:
                self.cmd_dict['hide_console'][0] = '--hide-console=v'
                self.cmd_dict['hide_console'][2] = self.cmd_dict['hide_console'][0].split()[1]
            else: return
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [25] 项 [可重复使用] 添加应用图标
    def add_icon(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['add_icon'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新应用图标', '请选择用于作为应用图标的icon图标', content_list, 'image', '图标或应用程序(*.ico *.exe);;icon图标(*.ico);;应用程序(*.exe)')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    command = '--icon="' + i + '"'
                    command_list.append(command)
                self.cmd_dict['add_icon'][0] = ' '.join(command_list)
                self.cmd_dict['add_icon'][2] = self.cmd_dict['add_icon'][0]
            else: 
                self.cmd_dict['add_icon'][0] = None
                self.cmd_dict['add_icon'][2] = self.cmd_dict['add_icon'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [26] 项 禁用窗口化。用于在 windowed 模式下禁用异常追踪信息的显示。在默认情况下，如果程序在 windowed 模式下崩溃，PyInstaller 会显示一个包含详细异常追踪信息的窗口。使用该选项后，如果程序崩溃，用户将不再看到详细的异常信息窗口，尤其是在发布产品时，该选项可能有助于提高程序的安全性
    def disable_windowed(self):
        try:
            if self.Win.cb_DisableWindowed.isChecked():
                self.cmd_dict['disable_windowed'][0] = '--disable-windowed-traceback'
                self.cmd_dict['disable_windowed'][2] = '已禁用窗口化'
            else:
                self.cmd_dict['disable_windowed'][0] = None
                self.cmd_dict['disable_windowed'][2] = None
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [27] 项 用于指定一个包含版本信息的文件。这个版本文件通常包含应用程序的版本号、公司信息等
    def version_file(self):
        try:
            if self.cmd_dict['version_file'][0]:
                current_data = self.cmd_dict['version_file'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前为：:{current_data}<br>是否替换原文件选项路径<br>', ['替换'],True)
                if action_reply == 0:
                    self.cmd_dict['version_file'][0] = None
                    self.cmd_dict['version_file'][2] = None
                    return
                elif action_reply == 1: pass
                else: return
            temp = self.select_file('添加应用版本信息文件', '请选择应用版本信息文件', '文本文件(*.txt *.ini)')
            if temp:
                self.cmd_dict['version_file'][0] = '--version-file="'+ temp + '"'
                self.cmd_dict['version_file'][2] = self.cmd_dict['version_file'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [28] 项 将文件FILE或XML的清单添加到exe文件。
    def add_xml_file(self):
        try:
            if self.cmd_dict['add_xml_file'][0]:
                current_data = self.cmd_dict['add_xml_file'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前为：:{current_data}<br>是否替换原选项<br>', ['替换'], reset_flag=True)
                # 重置键
                if action_reply == 0:
                    self.cmd_dict['add_xml_file'][0] = None
                    self.cmd_dict['add_xml_file'][2] = None
                    return
                # 替换键
                elif action_reply == 1: pass
                # 其他按键
                else: return
            temp = self.select_file('添加FILE文件或XML文件', '请选择添加到exe的FILE或XML文件', '文本文件(*.*)')
            if temp:
                self.cmd_dict['add_xml_file'][0] = '-m="'+ temp + '"'
                self.cmd_dict['add_xml_file'][2] = self.cmd_dict['add_xml_file'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [29] 项 [弃用]禁用将应用程序清单嵌入到可执行文件中。Windows 应用程序清单是一个 XML 文件，包含了应用程序的相关信息，如 UAC 请求、DLL 加载策略等。默认情况下，PyInstaller 将应用程序清单嵌入到生成的可执行文件中。但在某些情况下，可能会希望禁用这个嵌入，而是改为使用外部清单文件
    # def no_embed_manifest(self):
    #     try:
    #         if self.Win.cb_NoEmbedManifest.isChecked():
    #             QMessageBox.information(None, '提示', '此功能在Pyinstaller 5.0.0后已经被弃用了')
    #             self.cmd_dict['no_embed_manifest'][0] = '--no-embed-manifest'
    #             self.cmd_dict['no_embed_manifest'][2] = '禁用'
    #         else:
    #             self.cmd_dict['no_embed_manifest'][0] = None
    #             self.cmd_dict['no_embed_manifest'][2] = None
    #     except Exception as e:
    #         self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [30] 项 [可重复使用] 用于将文件或目录嵌入到生成的可执行文件中，以供运行时访问。RESOURCE是一个到四个项，FILE[,TYPE[,NAME[,LANGUAGE]]]。FILE可以是数据文件或exe/dll文件。对于数据文件，必须至少指定TYPE和NAME。LANGUAGE默认为0，或可以指定为通配符以更新给定TYPE和NAME的所有资源。对于exe/dll文件，如果省略了TYPE、NAME和LANGUAGE，或将它们指定为通配符，则会将FILE中的所有资源添加/更新到最终的可执行文件中。此选项可以多次使用
    def add_resource(self):
        try:
            # 数据处理，将原数据中引号部分提取出来
            currenr_list = self.cmd_dict['add_resource'][0]
            if currenr_list:
                temp_content_list = currenr_list.split()
                content_list = []
                for i in temp_content_list:
                    content_quotation = i.split('="')[1].split('"')[0]
                    content_list.append(content_quotation)
            else: content_list = None
            # 调用对话框
            temp_command_list= self.set_custom_list_widget('更新嵌入到生成的可执行文件中的文件或目录', '请选择输入数据类型，以用于将其嵌入到生成的可执行文件中', content_list, extra_func='edit_info')
            # 数据处理，将对话框的输入内容转换为命令的格式
            if temp_command_list:
                command_list = []
                for i in temp_command_list:
                    if ',' in i:
                        command = '-r="' + i + '"'
                    else: command = '-r="' + i + ',,,[]"'
                    command_list.append(command)
                self.cmd_dict['add_resource'][0] = ' '.join(command_list)
                self.cmd_dict['add_resource'][2] = self.cmd_dict['add_resource'][0]
            else:
                self.cmd_dict['add_resource'][0] = None
                self.cmd_dict['add_resource'][2] = self.cmd_dict['add_resource'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [31] 项 用于在生成的可执行文件上启用 User Account Control（UAC）管理员权限。在使用该选项时，用户在运行程序时可能会收到 UAC 提示，需要提供管理员权限，同时强制用户在以管理员身份运行可执行文件时提供管理员凭据，否则程序将无法启动
    def uac_admin_apply(self):
        try:
            if self.Win.cb_UacAdminApply.isChecked():
                self.cmd_dict['uac_admin_apply'][0] = '--uac-admin'
                self.cmd_dict['uac_admin_apply'][2] = '申请'
            else:
                self.cmd_dict['uac_admin_apply'][0] = None
                self.cmd_dict['uac_admin_apply'][2] = None
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [32] 项 用于在生成的可执行文件中启用 UIAccess, 以便程序能够在用户交互桌面(UIAccess Desktop)上运行。但要注意：1.这个选项仅在 Windows 上生效。2.程序需要具有管理员权限（通常需要 UAC 提示）才能启用 UIAccess。3.这个选项可能会导致程序在运行时需要管理员权限。
    def uac_uiaccess(self):
        try:
            if self.Win.cb_UacUiaccess.isChecked():
                self.cmd_dict['uac_uiaccess'][0] = '--uac-uiaccess'
                self.cmd_dict['uac_uiaccess'][2] = '允许'
            else:
                self.cmd_dict['uac_uiaccess'][0] = None
                self.cmd_dict['uac_uiaccess'][2] = None
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [33] 项 [弃用]将任何打包到应用程序中的共享程序集更改为私有程序集, 使用这个选项会导致 PyInstaller 将应用程序依赖的 DLL 文件复制到生成的可执行文件所在的目录，而不是依赖系统中已经存在的 DLL。请注意，使用该选项可能会增加生成的可执行文件的大小，只有在确实存在 DLL 版本兼容性问题时，才建议使用这个选项
    # def win_private_assemblies(self):
    #     try:
    #         if self.Win.cb_WinPrivateAssemblies.isChecked():
    #             QMessageBox.information(None, '提示', '此功能在Pyinstaller 5.0.0后已经被弃用了')
    #             self.cmd_dict['win_private_assemblies'][0] = '--win-private-assemblies'
    #             self.cmd_dict['win_private_assemblies'][2] = '共享程序集更改为私有程序集'
    #         else:
    #             self.cmd_dict['win_private_assemblies'][0] = None
    #             self.cmd_dict['win_private_assemblies'][2] = None
    #     except Exception as e:
    #         self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [34] 项 [弃用]用于在生成的可执行文件中禁用 DLL 优先级重定向, 强制使用系统中已安装的 DLL 而非使用在生成的可执行文件中的私有 DLL
    # def win_no_prefer_redirects(self):
    #     try:
    #         if self.Win.cb_WinNoPreferRedirects.isChecked():
    #             QMessageBox.information(None, '提示', '此功能在Pyinstaller 5.0.0后已经被弃用了')
    #             self.cmd_dict['win_no_prefer_redirects'][0] = '--win-no-prefer-redirects'
    #             self.cmd_dict['win_no_prefer_redirects'][2] = '禁用 DLL 优先级重定向'
    #         else:
    #             self.cmd_dict['win_no_prefer_redirects'][0] = None
    #             self.cmd_dict['win_no_prefer_redirects'][2] = None
    #     except Exception as e:
    #         self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [35] 项 为macOS应用程序包启用argv仿真。如果启用，则启动加载器将处理初始的打开文档/URL事件，并将传递的文件路径或URL附加到sys.argv。
    #         用于在生成的可执行文件中启用命令行参数（sys.argv）的模拟。默认情况下，PyInstaller 生成的可执行文件在运行时可能无法正确接收命令行参数。使用该选项可以解决一些在 Windows 上的问题，确保 PyInstaller 生成的可执行文件能够正确处理命令行参数。
    #         但应注意：1. 这个选项主要针对 Windows 平台。2. 在一些情况下，特别是在 Windows 上，PyInstaller 生成的可执行文件可能无法正确接收命令行参数。这个选项旨在解决这类问题。3. 请确保了解输出应用程序是否受影响，如果不受影响，则无需使用这个选项。
    def argv_emulation(self):
        try:
            if self.Win.cb_ArgvEmulation.isChecked():
                self.cmd_dict['argv_emulation'][0] = '--argv-emulation'
                self.cmd_dict['argv_emulation'][2] = '启用'
            else:
                self.cmd_dict['argv_emulation'][0] = None
                self.cmd_dict['argv_emulation'][2] = None
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [36] 项 用于在 macOS 平台上设置生成的应用程序的 Bundle Identifier。Bundle Identifier 是用于唯一标识 macOS 应用程序的字符串，通常采用逆序域名的形式。
    def osx_bundle_identifier(self):
        try:
            if self.cmd_dict['osx_bundle_identifier'][0]:
                current_data = self.cmd_dict['osx_bundle_identifier'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前选择为{current_data}<br>是否更改<br>', ['更改'],True)
                if action_reply == 0:
                    self.cmd_dict['osx_bundle_identifier'][0] = None
                    self.cmd_dict['osx_bundle_identifier'][2] = None
                    return
                elif action_reply == 1: pass
                else: return
            temp = QInputDialog.getText(None, '请输入Bundle Identifier', '添加用于在macOS平台上设置生成的应用程序的Bundle Identifier。<br>Bundle Identifier是用于唯一标识macOS应用程序的字符串，通常采用逆序域名的形式。<br>例如：com.mycompany.department.appname（默认值：第一个脚本的basename）<br><br>')[0]
            if temp: 
                self.cmd_dict['osx_bundle_identifier'][0] = '--osx-bundle-identifier="' + temp + '"'
                self.cmd_dict['osx_bundle_identifier'][2] = self.cmd_dict['osx_bundle_identifier'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [37] 项 用于指定生成的可执行文件的目标架构。该选项允许你选择生成 32 位（x86）或 64 位（x86_64）的可执行文件。
    def target_architecture(self):
        try:
            if self.cmd_dict['target_architecture'][0]:
                current_data = self.cmd_dict['target_architecture'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前选择为{current_data}<br>是否更改<br>', ['更改'],True)
                if action_reply == 0:
                    self.cmd_dict['target_architecture'][0] = None
                    self.cmd_dict['target_architecture'][2] = None
                    return
                elif action_reply == 1: pass
                else: return
            action_reply = self.set_custom_message_box('请选择目标架构', '请选择目标架构<br>默认情况下，PyInstaller 会尝试根据系统架构选择合适的目标架构。<br>', ['x86', 'x86_64'])
            if action_reply == 1: 
                self.cmd_dict['target_architecture'][0] = '--target-architecture x86'
                self.cmd_dict['target_architecture'][2] = 'x86'
            elif action_reply == 2:
                self.cmd_dict['target_architecture'][0] = '--target-architecture x86_64'
                self.cmd_dict['target_architecture'][2] = 'x86_64'
            else: return
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [38] 项 用于在 macOS 平台上对生成的应用程序进行代码签名。代码签名是一种在应用程序上附加数字签名的方法，用于验证应用程序的来源和完整性。使用提供的身份对收集的二进制文件和生成的可执行文件进行签名。如果未提供签名身份，则执行 ad-hoc 签名。
    def codesign_identity(self):
        try:
            if self.cmd_dict['codesign_identity'][0]:
                current_data = self.cmd_dict['codesign_identity'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前选择为{current_data}<br>是否更改<br>', ['更改'],True)
                if action_reply == 0:
                    self.cmd_dict['codesign_identity'][0] = None
                    self.cmd_dict['codesign_identity'][2] = None
                    return
                elif action_reply == 1: pass
                else: return
            temp = QInputDialog.getText(None, '请输入代码签名', '用于在 macOS 平台上对生成的应用程序进行代码签名。<br>代码签名是一种在应用程序上附加数字签名的方法，用于验证应用程序的来源和完整性。<br>使用提供的身份对收集的二进制文件和生成的可执行文件进行签名。<br>如果未提供签名身份，则执行 ad-hoc 签名。<br>')[0]
            if temp: 
                self.cmd_dict['codesign_identity'][0] = '--codesign-identity="' + temp + '"'
                self.cmd_dict['codesign_identity'][2] = self.cmd_dict['codesign_identity'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [39] 项 用于指定 macOS 平台上生成的应用程序的 entitlements 文件。Entitlements 文件包含了应用程序运行所需的权限和系统服务的详细信息。
    def osx_entitlements_file(self):
        try:
            if self.cmd_dict['osx_entitlements_file'][0]:
                current_data = self.cmd_dict['osx_entitlements_file'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前为：{current_data}<br>是否替换原文件选项路径<br>', ['替换'], True)
                if action_reply == 0:
                    self.cmd_dict['osx_entitlements_file'][0] = None
                    self.cmd_dict['osx_entitlements_file'][2] = None
                    return
                elif action_reply == 1:
                    pass
                else: return
            temp = self.select_file('添加entitlements文件', '请选择entitlements文件', 'entitlements文件(*.plist')
            if temp:
                self.cmd_dict['osx_entitlements_file'][0] = '--osx-entitlements-file="'+ temp + '"'
                self.cmd_dict['osx_entitlements_file'][2] = self.cmd_dict['osx_entitlements_file'][0]
            pass
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [40] 项 用于指定运行时临时目录。在运行过程中，PyInstaller 生成的可执行文件可能需要创建临时文件或缓存一些数据。该选项允许用户指定用于存储这些临时文件的目录
    #         注意：1. 这个选项通常在需要修改临时文件存储位置的特殊情况下使用。 2. 在某些环境下，默认的临时目录可能不适用，或者希望将临时文件保存在特定的目录中时，可以考虑使用这个选项。 3. 如果没有特殊要求，通常情况下无需手动设置。 PyInstaller 会在运行时使用系统默认的临时目录
    def runtime_tmpdir(self):
        try:
            if self.cmd_dict['output_methode'][0] == 'pyinstaller -D':
                pass
            else:
                QMessageBox.information(None, '提示', '该选项只能在“输出为文件夹”模式下使用')
                return
            if self.cmd_dict['runtime_tmpdir'][0]:
                current_data = self.cmd_dict['runtime_tmpdir'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前选择为{current_data}<br>是否替换原文件选项路径<br>', ['替换'])
                if action_reply == 0:
                    self.cmd_dict['runtime_tmpdir'][0] = None
                    self.cmd_dict['runtime_tmpdir'][2] = None
                    return
                elif action_reply == 1: pass
                else: return
            temp = self.select_folder('添加Pyinstaller运行时临时目录', '请选择文件夹，用于指定Pyinstaller运行时临时目录')
            if temp:
                self.cmd_dict['runtime_tmpdir'][0] = '--runtime-tmpdir="'+ temp + '"'
                self.cmd_dict['runtime_tmpdir'][2] = self.cmd_dict['runtime_tmpdir'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [41] 项 引导加载程序忽略信号，而不是将它们转发给子进程。在诸如监督进程向引导加载程序和子进程（例如通过进程组）发送信号以避免向子进程发出两次信号的情况下很有用。
    def ignore_signals(self):
        try:
            if self.Win.cb_IgnoreSignals.isChecked():
                self.cmd_dict['ignore_signals'][0] = '--bootloader-ignore-signals'
                self.cmd_dict['ignore_signals'][2] = '忽略信号'
            else:
                self.cmd_dict['ignore_signals'][0] = None
                self.cmd_dict['ignore_signals'][2] = None
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [42] 项 pte_OutputPath 应用程序打包后的输出目录（默认为 ./dist）
    # 具体内容写在了函数 PyToExeUI.py 中的 plain_text_update() 中
    
    # [43] 项 用于指定 PyInstaller 在构建过程中使用的工作目录。工作目录是 PyInstaller 用于临时存储构建过程中的中间文件和临时文件的地方。临时工作文件的位置，包括 .log，.pyz 等文件（默认为 ./build）
    def workpath_option(self):
        try:
            if self.cmd_dict['workpath_option'][0]:
                current_data = self.cmd_dict['workpath_option'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前选择为{current_data}<br>是否替换原文件选项路径<br>', ['替换'])
                if action_reply == 0:
                    self.cmd_dict['workpath_option'][0] = None
                    self.cmd_dict['workpath_option'][2] = None
                    return
                elif action_reply == 1: pass
                else: return
            temp = self.select_folder('添加临时工作文件的位置', '请选择文件夹，用于指定 PyInstaller 在构建过程中使用的工作目录')
            if temp:
                self.cmd_dict['workpath_option'][0] = '--workpath="'+ temp + '"'
                self.cmd_dict['workpath_option'][2] = self.cmd_dict['workpath_option'][0]
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [44] 项 用于在构建可执行文件时默认选择“是”以避免询问用户任何确认问题。该选项可用于自动化构建过程，以防止在构建期间需要手动确认。
    def noconfirm_option(self):
        try:
            if self.Win.cb_NoconfirmOption.isChecked():
                self.cmd_dict['noconfirm_option'][0] = '--noconfirm'
                self.cmd_dict['noconfirm_option'][2] = '默认输出目录（默认为 SPECPATH/dist/SPECNAME），不需要确认'
            else:
                self.cmd_dict['noconfirm_option'][0] = None
                self.cmd_dict['noconfirm_option'][2] = '替换输出目录（默认为 SPECPATH/dist/SPECNAME），需要确认'
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [45] 项 用于指定 UPX 压缩工具的目录路径。UPX 是一种可执行文件压缩工具，用于减小生成的可执行文件的大小。
    def upx_dir(self):
        try:
            if self.cmd_dict['upx_dir'][0]:
                current_data = self.cmd_dict['upx_dir'][0]
                action_reply = self.set_custom_message_box('数据已存在', f'当前选择为{current_data}<br>是否替换原文件选项路径<br>', ['替换'])
                if action_reply == 0:
                    self.cmd_dict['upx_dir'][0] = None
                    self.cmd_dict['upx_dir'][2] = None
                    return
                elif action_reply == 1: pass
                else: return
            temp = self.select_folder('添加指定UPX压缩工具的目录路径', '请选择文件夹, 用于指定 UPX 压缩工具的目录路径。UPX 是一种可执行文件压缩工具，用于减小生成的可执行文件的大小。')
            if temp:
                self.cmd_dict['upx_dir'][0] = '--upx-dir="'+ temp + '"'
                self.cmd_dict['upx_dir'][2] = self.cmd_dict['upx_dir'][0]
            pass
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [46] 项 [弃用]用于设置生成的可执行文件为一个控制台应用程序（命令行应用程序）。这将导致在运行生成的可执行文件时，将打开一个命令行窗口（控制台窗口）。
    def ascii(self):
        try:
            pass
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [47] 项 在构建之前清理 PyInstaller 缓存并删除临时文件
    def clear_cache(self):
        if self.Win.cb_ClearCache.isChecked():
            self.cmd_dict['clear_cache'][0] = '--clean'
            self.cmd_dict['clear_cache'][2] = '清理'
        else:
            self.cmd_dict['clear_cache'][0] = None
            self.cmd_dict['clear_cache'][2] = '不清理'
    
    # [48] 项 用于设置 PyInstaller 的日志输出级别。PyInstaller 使用不同的日志级别来记录构建过程中的各种信息，包括警告、错误和调试信息。
    def log_level(self):
        'TRACE、DEBUG、INFO、WARN、DEPRECATION、ERROR、FATAL'
        try:
            if self.cmd_dict['log_level'][2]:
                current_data = self.cmd_dict['log_level'][2]
            else: current_data = None
            action_reply = self.set_custom_message_box('日志输出级别', f'当前日志输出级别：<br>{current_data}<br><br>请选择Pyinstaller的日志输出级别：<br>',
                                                        ['TRACE(跟踪)','DEBUGL(调试)','INFO(信息)','WARN(警告)','DEPRECATION(弃用警告)','ERROR(错误)','FATAL(严重错误)'], True)
            if action_reply == 0:
                self.cmd_dict['log_level'][0] = None
                self.cmd_dict['log_level'][2] = None
            elif action_reply == 1:
                self.cmd_dict['log_level'][0] = '--log-level TRACE'
                self.cmd_dict['log_level'][2] = self.cmd_dict['log_level'][0].split()[1]
            elif action_reply == 2:
                self.cmd_dict['log_level'][0] = '--log-level DEBUG'
                self.cmd_dict['log_level'][2] = self.cmd_dict['log_level'][0].split()[1]
            elif action_reply == 3:
                self.cmd_dict['log_level'][0] = '--log-level INFO'
                self.cmd_dict['log_level'][2] = self.cmd_dict['log_level'][0].split()[1]
            elif action_reply == 4:
                self.cmd_dict['log_level'][0] = '--log-level WARN'
                self.cmd_dict['log_level'][2] = self.cmd_dict['log_level'][0].split()[1]
            elif action_reply == 5:
                self.cmd_dict['log_level'][0] = '--log-level DEPRECATION'
                self.cmd_dict['log_level'][2] = self.cmd_dict['log_level'][0].split()[1]
            elif action_reply == 6:
                self.cmd_dict['log_level'][0] = '--log-level ERROR'
                self.cmd_dict['log_level'][2] = self.cmd_dict['log_level'][0].split()[1]
            elif action_reply == 7:
                self.cmd_dict['log_level'][0] = '--log-level FATAL'
                self.cmd_dict['log_level'][2] = self.cmd_dict['log_level'][0].split()[1]
            else: return
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # [49] 项 pte_FilePath 被执行打包的python脚本
    # 具体内容写在了函数 PyToExeUI.py 中的 plain_text_update() 中
    
    def launch_cmd(self):
        self.plain_text_update()
        if not self.launch_flag:
            QMessageBox.information(None, '提示', '不存在指定Python脚本，请选择.py文件')
            return
        self.cmd[2] = self.get_command_from_dict()
        self.Launch_QThread = Launch_py_QThread(self.cmd)
        self.Launch_QThread.output_to_textbrowser_cmd.connect(lambda content: self.append_TB_text(content, self.Win.textBrowser_cmd))
        self.Launch_QThread.output_to_textbrowser.connect(lambda content: self.append_TB_text(content, self.Win.textBrowser))
        self.Launch_QThread.finished_signal.connect(self.thread_finished_file_del)
        self.Launch_QThread.start()
    
    def read_output(self, object:object, content:str = None, content_cmd:str = None):
        while True:
            output_line = object.stdout.readline()
            if output_line == '' and object.poll() is not None:
                break
            if output_line:
                self.append_TB_text(output_line.strip(), self.Win.textBrowser_cmd)
        self.append_TB_text(f'__________ {content_cmd} __________\n', self.Win.textBrowser_cmd)
        self.append_TB_text(f'__________ {content} __________\n', self.Win.textBrowser)
    
    def thread_finished_file_del(self):
        self.Launch_QThread.wait() 
        try:
            if self.clear_file_flag:
                subprocess.run('copy .\\dist\\*.exe .\\ > nul', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                subprocess.run('rd /s /q .\\build > nul', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                subprocess.run('rd /s /q .\\dist > nul', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                subprocess.run('del *.spec > nul', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                self.append_TB_text(f'__________ 已删除其余文件 __________\n', self.Win.textBrowser)
        except subprocess.CalledProcessError as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)