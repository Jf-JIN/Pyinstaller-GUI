import os
from copy import deepcopy

from PyToExe_ui import *

from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton, QDialog, QListWidget, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QFrame, QSpacerItem, QInputDialog, QLabel, QCheckBox, QRadioButton
from PyQt5.QtGui import QTextCursor, QDesktopServices, QIcon, QPixmap
from PyQt5.QtCore import Qt, QUrl

# workspace_path = os.path.dirname(__file__)
workspace_path = os.getcwd()
default_icon_path = ''
if os.path.exists(default_icon_path):
    WINDOW_ICON_PATH = default_icon_path
else:
    WINDOW_ICON_PATH = None

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
        self.parameter_init()
        self.py_to_exe_ui_signal_connection()
        self.ui_init()

    # ****************************************初始化****************************************
    # UI界面的初始化
    def ui_init(self):
        self.Win.pb_Recover.hide()
        self.Win.pte_FilePath.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.pte_FileName.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.pte_OutputPath.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.textBrowser_cmd.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win.pte_OutputPath.setPlainText(os.path.join(workspace_path, 'dist'))
        self.cmd_dict['output_folder_path'][0] = '--distpath="' + os.path.join(workspace_path, 'dist') + '"'
        if py_file_auto_path:
            self.Win.pte_FilePath.setPlainText(
                os.path.join(workspace_path, py_file_auto_path))
            self.cmd_dict['python_file_path'][0] = '"' + os.path.join(workspace_path, py_file_auto_path) + '"'
            self.Win.pte_FileName.setPlainText(py_file_auto_path.split('.')[0])
            self.cmd_dict['output_file_name'][0] = '--name="' + py_file_auto_path.split('.')[0] + '"'
            self.launch_flag = True

    # 参数初始化
    def parameter_init(self):
        self.launch_flag = False
        self.clear_file_flag = True
        # 用于显示参数，Label是项目名，explain是参数含义
        self.cmd_dict = {
            'output_methode': [None, '输出方式：\t', None],  'specpath': [None, '\n.spec的文件夹：\t', None], 'output_file_name': [None, '\n输出名称：\t', None], 'contents_directory': [None, '\n除exe外，输出的其他数据的存入路径：\n', None], 'add_file_folder_data': [None, '\n添加文件资源：\t', None], 
            'add_binary_data': [None, '\n添加二进制资源：\t', None], 'imports_folder': [None, '\n搜索import模块路径：\t', None], 'import_module_name': [None, '\n引用外部指定import模块名：\t', None], 'collect_submodules': [None, '\n打包及本身及其所有子模块的模块：\t', None], 'collect_data': [None, '\n打包所有数据的模块：\t', None],
            'collect_binaries': [None, '\n打包模块的所有二进制文件：\t', None], 'collect_all': [None, '\n打包所有数据的模块：\t', None], 'copy_metadata': [None, '\n打包元数据的模块：\t', None], 'recursive_copy_metadata': [None, '\n打包本身及其所有依赖项元数据的模块：\t', None], 'additional_hooks_dir': [None, '\n添加指定的钩子文件夹路径：\t', None],
            'runtime_hook': [None, '\n添加运行时钩子文件的路径：\t', None], 'exclude_module': [None, '\n要忽略的可选模块或包：\t', None], 'add_splash_screen': [None, '\n应用程序的启动画面：\t', None], 'debug_mode': [None, '\n调试模式：\t', None], 'python_option': [None, '指定Python解释器的命令行：\t', None],
            'strip_option': [None, '\n对可执行文件和共享库应用符号表剥离：\t', None], 'noupx_option': [None, '\n使用upx压缩：\t', None], 'upx_exclude': [None, '\nupx压缩排除文件：\t', None], 'console_window_control': [None, '\n控制台窗口：\t', None], 'hide_console': [None, '控制台窗口的显示方式：\t', None],
            'add_icon': [None, '\n应用图标路径：\t', None], 'disable_windowed': [None, '\n禁用窗口化：\t', None], 'version_file': [None, '\n添加版本资源：\t', None], 'add_xml_file': [None, '\n添加文件或XML资源：\t', None], 'no_embed_manifest': [None, '\n将应用程序清单嵌入到可执行文件中：\t', None],
            'add_resource': [None, '\n添加嵌入exe中的文件或目录：\t', None], 'uac_admin_apply': [None, '\n申请管理员权限：\t', None], 'uac_uiaccess': [None, '\n允许远程桌面使用：\t', None], 'win_private_assemblies': [None, '\n共享程序集改私有：\t', None], 'win_no_prefer_redirects': [None, '\ndll优先级重定向：\t', None],
            'argv_emulation': [None, '\nmacOS启用argv仿真：\t', None], 'osx_bundle_identifier': [None, '\nBundle Identifier：\t', None], 'target_architecture': [None, '\n目标架构：\t', None], 'codesign_identity': [None, '\n代码签名：\t', None], 'osx_entitlements_file': [None, '\n二进制授权文件(entitlements文件)：\t', None],
            'runtime_tmpdir': [None, '\nPyinstaller临时目录：\t', None], 'ignore_signals': [None, '\n引导加载程序忽略信号：\t', None], 'output_folder_path': [None, '\n输出目录：\t', None], 'workpath_option': [None, '\n临时工作文件位置：\t', None], 'noconfirm_option': [None, '\n替换输出目录询问：\t', None],
            'upx_dir': [None, '\nupx工具路径：\t', None], 'ascii': [None, '\n编码支持：\t', None], 'clear_cache': [None, '\n清理缓存：\t', None], 'log_level': [None, '\n控制台消息详细程度：\t', None], 'python_file_path': [None, '\nPython脚本：\t', None]
        }
        self.cmd = [None]*3
        self.cmd[0] = os.path.splitdrive(workspace_path)[0]
        self.cmd[1] = 'cd '+ workspace_path
        self.cmd_dict['output_methode'][0] = 'pyinstaller -F'
        self.cmd_dict['output_methode'][2] = '生成单个文件'
        self.cmd_dict['clear_cache'][0] = '--clean'
        self.cmd_dict['clear_cache'][2] = '清理'
        self.cmd_dict['console_window_control'][0] = '--console'
        self.cmd_dict['console_window_control'][2] = '为标准 I/O 打开控制台窗口'
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

    # ****************************************PLE有输入变化时，数据更新****************************************
    def file_path_changed(self):
        
        file_path = self.Win.pte_FilePath.toPlainText()
        if file_path:
            self.launch_flag = True
        else:
            self.launch_flag = False
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
        # print(temp_command)
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
        action_reply = self.set_custom_message_box('警告', '您当前正在执行清空输入的操作，确认清空吗？<br><br>恢复功能只能恢复最后一次清空输入前的数据输入<br>连续两次清空输入将无法恢复此前的数据输入', ['确认清空'], messagebox_content_icon=QMessageBox.Warning)
        if action_reply == 1:
            pass
        else: return
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
        self.Win.rb_OutputMethod_F.setChecked(True)
        self.Win.rb_ConsoleWindowControl_C.setChecked(True)
        # 重置参数
        reset_py_file_path = self.recover_cmd_dict['python_file_path'][0].split('"')[1]
        self.Win.pte_FilePath.setPlainText(reset_py_file_path)
        self.Win.pte_OutputPath.setPlainText(os.path.dirname(reset_py_file_path))
        self.Win.pte_FileName.setPlainText(os.path.splitext(os.path.basename(reset_py_file_path))[0])
        self.cmd_dict['output_methode'][0] = 'pyinstaller -F'
        self.cmd_dict['output_methode'][2] = '生成单个文件'
        self.cmd_dict['clear_cache'][0] = '--clean'
        self.cmd_dict['clear_cache'][2] = '清理'
        self.cmd_dict['console_window_control'][0] = '--console'
        self.cmd_dict['console_window_control'][2] = '为标准 I/O 打开控制台窗口'
    
    # 清空所有
    def clear_all(self):
        self.clear_all_display()
        self.clear_input()
    
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
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************显示参数****************************************
    def parameter_display(self):
        try:
            self.append_TB_text(f'__________ 显 示 命 令 参 数  __________\n')
            # print(self.cmd_dict.values())
            for value in self.cmd_dict.values():
                if value[0]:
                    command_display = str(value[1] + value[2])
                    self.append_TB_text(command_display, self.Win.textBrowser)
            self.append_TB_text(f'__________ 全 部 有 效 参 数  __________\n\n')
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************打印参数到txt****************************************
    def print_cmd(self):
        print_command_path = os.path.join(workspace_path, 'output_command_of_pyinstaller.txt')
        self.cmd[2] = self.get_command_from_dict()
        try:
            with open(print_command_path, 'w', encoding='utf-8') as file:
                file.write(self.cmd[0] + '\n')
                file.write(self.cmd[1] + '\n')
                file.write(self.cmd[2] + '\n')
            QMessageBox.information(None, '提示', f'pyinstaller执行命令已完成打印<br>输出命令文件位于：<br>{print_command_path}')
            QDesktopServices.openUrl(
                            QUrl.fromLocalFile(workspace_path))
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************打开输出文件夹****************************************
    def open_output_folder(self):
        try:
            if self.cmd_dict['python_file_path'][0] and os.path.exists(self.cmd_dict['output_folder_path'][0].split('"')[1]):
                folder_path = self.cmd_dict['output_folder_path'][0].split('"')[1]
            elif workspace_path:
                folder_path = workspace_path
            else:
                QMessageBox.information(None, '提示', '无处理文件，请先选择处理文件')
                return
            QDesktopServices.openUrl(
                        QUrl.fromLocalFile(folder_path))
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************向Textbrowser添加内容****************************************
    def append_TB_text(self, text_content: str, textBrowser_object: object = None):
        if not textBrowser_object:
            textBrowser_object = self.Win.textBrowser
        textBrowser_object.moveCursor(QTextCursor.End)
        textBrowser_object.insertPlainText(text_content + "\n")
        textBrowser_object.moveCursor(QTextCursor.End)
    
    def clear_file_after_launch_flag_change(self):
        if self.Win.cb_ClearFileAfterLaunchFlagChange.isChecked():
            self.clear_file_flag = True
        else:
            self.clear_file_flag = False
    
    # ****************************************文件浏览选择****************************************
    def select_py_file(self):
        temp = self.select_file('Python文件路径', '请选择Python文件', 'Python文件 (*.py)')
        self.Win.pte_FilePath.setPlainText(temp)
        self.cmd_dict['python_file_path'][0].split('"')[1] = temp
        self.cmd_dict['python_file_path'][0] = ''.join(self.cmd_dict['python_file_path'][0])          
    
    def select_ourput_folder(self):
        temp = self.select_folder('输出.exe文件路径', '请选择输出文件夹')
        self.Win.pte_OutputPath.setPlainText(temp)
        self.cmd_dict['output_folder_path'][0].split('"')[1] = temp
        self.cmd_dict['output_folder_path'][0] = ''.join(self.cmd_dict['output_folder_path'][0])  
        self.temp = self.cmd_dict['output_folder_path'][0].split('"')    
    
    # ****************************************通用文件浏览选择****************************************
    def select_file(self, item_display:str = '', window_title:str = '', file_discription:str = '') -> str :
        options = QFileDialog.Options()
        try:
            receiver_temp, _ = QFileDialog.getOpenFileName(self, f'{window_title}', '', f'{file_discription}', options=options)
            if receiver_temp:
                self.append_TB_text(f'__________ 更新设置：{item_display} __________\n{receiver_temp}\n')
                return receiver_temp
            return
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
            
    
    def select_folder(self, item_display:str = '', window_title:str = '') -> str :
        options = QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        try:
            receiver_temp = QFileDialog.getExistingDirectory(self, f'{window_title}', '', options=options)
            if receiver_temp:
                self.append_TB_text(f'__________ 更新设置：{item_display} __________\n{receiver_temp}\n')
                return receiver_temp
            return None
        except Exception as e:
            self.append_TB_text(f'__________ 错 误 __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************自定义对话窗口****************************************
    def set_custom_message_box(self, window_title:str, description:str, button_list:list, reset_flag:bool = False, default_button:int = -1, window_icon_path = WINDOW_ICON_PATH, messagebox_content_icon = QMessageBox.Question) :
        msg_box = QMessageBox()
        msg_box.setIcon(messagebox_content_icon)
        msg_box.setWindowIcon(QIcon(window_icon_path))
        msg_box.setWindowTitle(window_title)
        msg_box.setText(description)
        buttons = []
        
        if reset_flag:
            button_reset = QPushButton('重置')
        else:
            button_reset = QPushButton('')
        msg_box.addButton(button_reset, QMessageBox.ResetRole)
        buttons.append(button_reset)
        
        for i in range(len(button_list)):
            button = QPushButton(button_list[i])
            msg_box.addButton(button, QMessageBox.YesRole)
            buttons.append(button)
        
        button_cancel = QPushButton('取消')
        msg_box.addButton(button_cancel, QMessageBox.NoRole)
        buttons.append(button_cancel)
        
        msg_box.setDefaultButton(buttons[default_button])
        
        return msg_box.exec_()
    
    # ****************************************询问文件还是文件夹对话窗口****************************************
    def type_select_dialog(self, file_type = '所有文件(*.*)'):
        action_reply = self.set_custom_message_box('选择添加数据类型', '添加文件还是文件夹？', ['文件夹', '文件'])
        if action_reply == 1:
            temp = self.select_folder('添加文件夹资料', '请选择文件夹')
        elif action_reply == 2:
            temp = self.select_file('添加文件资料', '请选择文件', file_type)
        else: return
        return temp
    
    # ****************************************自定义项目显示窗口****************************************
    def set_custom_list_widget(self, window_title, item_list, type_select_flag = 'file_folder', file_type = '所有文件(*.*)', text_discription = '请输入指定信息', extra_func = None, window_icon_path = WINDOW_ICON_PATH):
        dialog = QDialog()
        dialog.setWindowTitle(window_title)
        dialog.resize(600,500)
        if window_icon_path:
            dialog.setWindowIcon(QIcon(window_icon_path))
        dialog.setStyleSheet(
            "QDialog{min-width:600px; min-height:500px;}"
            "QFrame[objectName = 'frame_add_remove']{margin:0; padding:0; max-height:50px;}"
            "QFrame[objectName = 'frame_finish_cancel']{margin:0; padding:0; max-height:35px;}"
            "QPushButton{min-height: 30px; max-height: 30px;}"
        )
        
        list_widget = QListWidget()
        
        if item_list:
            list_widget.addItems(item_list)
        
        
            
        
        pb_add = QPushButton('添加')
        pb_remove = QPushButton('移除')
        pb_finish = QPushButton('确定')
        pb_cancel = QPushButton('取消')
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
            pb_edit_info = QPushButton('指定信息')
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
            if current_row >= 0 and current_row < list_widget.count():
                selected_item_text = list_widget.item(current_row).text()
                # 根据你的需求加载并显示图片，这里假设 selected_item_text 是图片路径
                pixmap = QPixmap(selected_item_text)
                lb_preview.setPixmap(pixmap.scaled(lb_preview.size(), Qt.KeepAspectRatio))
        def edit_info():
            current_items = [list_widget.item(i).text() for i in range(list_widget.count())]
            current_row = list_widget.currentRow()
            if current_row >= 0 and current_row < list_widget.count():
                original = list_widget.item(current_row).text()
                temp_input, _ = QInputDialog.getText(None, '请输入指定信息', '请选择需要嵌入可执行文件的数据的指定信息，格式如下：<br>"格式,名称,语言"(其中逗号","必须为英文逗号)<br><br>格式：资源的类型，通常是一个 MIME 类型，例如 "text/plain"<br> 名称：在可执行文件中嵌入的资源的名称<br>语言：资源的语言,通常是一个整数或字符串，表示资源所属的语言。在 Windows 系统上，语言代码通常是一个四位的十进制数，例如 1033 表示英语（美国）。<br>在其他系统上，可能使用标准的 IETF BCP 47 语言标签<br><br>示例：<br>image/png,app_data,1033<br>,,1033<br>,app_data<br><br>若无此需要，则按回车或点击“OK”即可<br>')
                if temp_input:
                    temp_content = original.split(',')[0] + ',' + temp_input
                if temp_content in current_items:
                    QMessageBox.information(None, '提示', f'请勿重复添加数据<br>{temp_input}<br>')
                else:
                    list_widget.item(current_row).setText(temp_content)
                
        def line_edit_input():
            temp = QInputDialog.getText(None, '请输入指定信息', text_discription)[0]
            if temp:
                return temp
            else: return None
        
        def add_item():
            current_items = [list_widget.item(i).text() for i in range(list_widget.count())]
            if type_select_flag == 'file' or type_select_flag == 'image':
                temp = self.select_file('添加文件资料', '请选择文件', file_type)
            elif type_select_flag == 'folder':
                temp = self.select_folder('添加文件夹资料', '请选择文件夹')
            elif type_select_flag == 'file_folder':
                temp = self.type_select_dialog(file_type)
            elif type_select_flag == 'text':
                temp = line_edit_input()
            elif type_select_flag == 'image':
                temp = preview_image()
            if temp in current_items:
                QMessageBox.information(None, '提示', f'请勿重复添加数据<br>{temp}<br>')
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

        result = dialog.exec_()

        if result == QDialog.Accepted:
            selected_items = [list_widget.item(i).text() for i in range(list_widget.count())]
            # print(selected_items)
            return selected_items