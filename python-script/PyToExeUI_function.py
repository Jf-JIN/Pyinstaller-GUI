import os
import traceback

from PyToExeUI import *

from PyQt5.QtWidgets import  QFileDialog
from PyQt5.QtGui import QTextCursor, QDesktopServices, QPixmap
from PyQt5.QtCore import Qt, QUrl


class PyToExeUI_function(PyToExeUI):
    def __init__(self):
        super().__init__()
        self.connections_pytoexeui_function()
    
    def connections_pytoexeui_function(self):
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
        self.Win.pb_TB_increase.clicked.connect(lambda: self.font_increase_px(self.Win.textBrowser, 1))
        self.Win.pb_TB_decrease.clicked.connect(lambda: self.font_increase_px(self.Win.textBrowser, -1))
        self.Win.pb_TBcmd_increase.clicked.connect(lambda: self.font_increase_px(self.Win.textBrowser_cmd, 1))
        self.Win.pb_TBcmd_decrease.clicked.connect(lambda: self.font_increase_px(self.Win.textBrowser_cmd, -1))
        
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
        if self.recover_cmd_dict['python_file_path'][0] and os.path.exists(self.recover_cmd_dict['python_file_path'][0].split('"')[1]):
            reset_py_file_path = self.recover_cmd_dict['python_file_path'][0].split('"')[1]
            self.Win.pte_FilePath.setPlainText(reset_py_file_path)
            self.Win.pte_OutputPath.setPlainText(os.path.dirname(reset_py_file_path))
            self.Win.pte_FileName.setPlainText(os.path.splitext(os.path.basename(reset_py_file_path))[0])
        else:
            self.Win.pte_FilePath.clear()
            self.Win.pte_OutputPath.clear()
            self.Win.pte_FileName.clear()
        self.cmd_dict['output_methode'][0] = '--onefile'
        self.cmd_dict['output_methode'][1] = 'rb_OutputMethod_F'
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
            self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************从字典中获取实际command执行命令函数****************************************
    def get_command_from_dict(self):
        temp_command = []
        for value in self.cmd_dict.values():
            temp_command.append(value[0])
        temp_command.insert(0, 'pyinstaller')
        temp_command_final = ' '.join(filter(None, temp_command))
        return(temp_command_final)
    
    def command_summary(self) -> list:
        self.cmd[2] = self.get_command_from_dict()
        command = [None] * 3
        command[0] = deepcopy(self.cmd[0])
        command[1] = deepcopy(self.cmd[1])
        command[2] = deepcopy(self.cmd[2])
        if self.Win.cb_CondaUse.isChecked():
            command.insert(0, f'conda activate {self.Win.lb_CondaInfo.text()}')
        return command
    
    # ****************************************显示参数****************************************
    def parameter_display(self):
        try:
            self.append_TB_text(f'__________  {self.json_general["display_command_parameter"]}  __________')
            # 更新显示参数的参数解释
            for item in self.cmd_dict.values():
                if item[0] and 'dict_explain' in self.json_widgets[item[1]]:
                    item[2] = self.json_widgets[item[1]]['dict_explain']
            # 显示参数内容
            for value in self.cmd_dict.values():
                if value[0]:
                    command_display = str(self.json_widgets[value[1]]["dict"] + value[2])
                    self.append_TB_text(command_display, self.Win.textBrowser)
            self.append_TB_text(f'__________  {self.json_general["all_parameter"]}  __________\n\n')
        except Exception as e:
            QMessageBox.warning(None, self.json_general['msg_warning'], str(e))
            # self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************打印参数到txt****************************************
    def print_cmd(self):
        print_command_path = os.path.join(workspace_path, 'output_command_of_pyinstaller.txt')
        command_list = self.command_summary()
        try:
            with open(print_command_path, 'w', encoding='utf-8') as file:
                file.write('\n'.join(command_list))
            QMessageBox.information(None, self.json_general["msg_info"], f'{self.json_special["print_cmd"]}<br>{print_command_path}')
            QDesktopServices.openUrl(
                            QUrl.fromLocalFile(workspace_path))
        except Exception as e:
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
            if self.traceback_display_flag:
                e = traceback.format_exc()
            self.append_TB_text(f'__________ {self.json_general["error"]} __________\n{e}\n', self.Win.textBrowser_cmd)
    
    # ****************************************向Textbrowser添加内容****************************************
    def append_TB_text(self, text_content: str, textBrowser_object: object = None):
        if not textBrowser_object:
            textBrowser_object = self.Win.textBrowser
        if self.json_general["error"] in text_content or text_content.startswith('===='):
            self.launch_error_count += 1
        try:
            if self.launch_flag and self.launch_error_count > 0:
                text_content = '[' + self.json_general["error"] + ']  ' + text_content.split('\n')[0]
            textBrowser_object.moveCursor(QTextCursor.End)
            textBrowser_object.insertPlainText(text_content + "\n")
            textBrowser_object.moveCursor(QTextCursor.End)
        except Exception as e:
            if self.traceback_display_flag:
                e = traceback.format_exc()
            textBrowser_object.moveCursor(QTextCursor.End)
            textBrowser_object.insertPlainText( str(e) + "\n")
            textBrowser_object.moveCursor(QTextCursor.End)
    
    def clear_file_after_launch_flag_change(self):
        if self.Win.cb_ClearFileAfterLaunchFlagChange.isChecked():
            self.clear_file_flag = True
        else:
            self.clear_file_flag = False
    
    # ****************************************文件浏览选择****************************************
    def select_py_file(self):
        temp = self.select_file(self.json_special['select_py_file']['text_browser_display'], self.json_special['select_py_file']['dialog_title'], self.json_special['select_py_file']['type_discription'])
        if temp:
            self.Win.pte_FilePath.setPlainText(temp)
            self.cmd_dict['python_file_path'][0].split('"')[1] = temp
            self.cmd_dict['python_file_path'][0] = ''.join(self.cmd_dict['python_file_path'][0])          
    
    def select_ourput_folder(self):
        temp = self.select_folder(self.json_special['select_ourput_folder']['text_browser_display'], self.json_special['select_ourput_folder']['dialog_title'])
        if temp:
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
            return None
        except Exception as e:
            if self.traceback_display_flag:
                e = traceback.format_exc()
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
            if self.traceback_display_flag:
                e = traceback.format_exc()
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
    
    # ****************************************Conda环境选择显示窗口****************************************
    def conda_widget_ui(self):
        
        # 新建对话窗口及控件
        conda_dialog = QDialog()
        conda_dialog.setWindowTitle('Conda')
        conda_dialog.resize(600,500)
        conda_dialog.setWindowIcon(self.WINDOW_ICON)
        conda_dialog.setStyleSheet(
            "QDialog{min-width:600px; min-height:500px;}"
            "QLabel{margin:0; padding:0; max-height:30px;}"
            "QFrame[objectName = 'frame_pb_view']{margin:0; padding:0; max-height:35px;}"
            "QFrame[objectName = 'frame_pb_finish']{margin:0; padding:0; max-height:50px;}"
            "QPushButton{min-height: 30px; max-height: 30px;}"
        )
        lb_env_name = QLabel()
        lb_env_path = QLabel()
        list_widget = QListWidget()
        pb_package_view = QPushButton(self.json_special['pb_package_view']['text'])
        pb_package_view.setToolTip(self.json_special['pb_package_view']['tooltip'])
        pb_package_view.setEnabled(False)
        pb_finish = QPushButton(self.json_general['pb_certain'])
        pb_finish.setEnabled(False)
        pb_cancel = QPushButton(self.json_general['pb_cancel'])
        frame_pb_view = QFrame()
        frame_pb_view.setObjectName('frame_pb_view')
        frame_pb_finish = QFrame()
        frame_pb_finish.setObjectName('frame_pb_finish')
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        def get_env_list(data_list):
            add_flag = True
            while add_flag:
                if data_list:
                    self.conda_env_list = data_list
                    for i in data_list:
                        item = QListWidgetItem(i[0])
                        list_widget.addItem(item)
                        item.setToolTip(i[1])
                    add_flag = False
            goal_items = list_widget.findItems(self.Win.lb_CondaInfo.text(), Qt.MatchExactly)
            if goal_items:
                list_widget.setCurrentItem(goal_items[0])
        Conda_Get_Env_List = Conda_Get_Env_List_QThread(self)
        Conda_Get_Env_List.text_to_textBrowser_cmd.connect(lambda content: self.append_TB_text(content, self.Win.textBrowser_cmd))
        Conda_Get_Env_List.signal_conda_env_list.connect(get_env_list)
        Conda_Get_Env_List.start()
        
        lb_env_name.setText(self.json_special['lb_env_name']['text_init'])
        lb_env_path.setText(self.json_special['lb_env_path']['text_init'])
        
        layout_pb_view = QHBoxLayout(frame_pb_view)
        layout_pb_view.setContentsMargins(0, 0, 0, 0)
        layout_pb_view.setSpacing(10)
        layout_pb_view.addItem(spacer_item)
        layout_pb_view.addWidget(pb_package_view)
        
        layout_pb_finish = QHBoxLayout(frame_pb_finish)
        layout_pb_finish.setContentsMargins(0, 0, 0, 0)
        layout_pb_finish.setSpacing(10)
        layout_pb_finish.addWidget(pb_finish)
        layout_pb_finish.addWidget(pb_cancel)
        
        layout_dialog = QVBoxLayout(conda_dialog)
        layout_dialog.addWidget(lb_env_name)
        layout_dialog.addWidget(lb_env_path)
        layout_dialog.addWidget(list_widget)
        layout_dialog.addWidget(frame_pb_view)
        layout_dialog.addWidget(frame_pb_finish)
        
        def pb_state_update():
            current_row = list_widget.currentRow()
            if current_row != -1:
                pb_finish.setEnabled(True)
                pb_package_view.setEnabled(True)
                lb_env_name.setText(self.json_special['lb_env_path']['text'] + self.conda_env_list[current_row][0])
                lb_env_path.setText(self.json_special['lb_env_path']['text'] + self.conda_env_list[current_row][1])
        
        def show_detail(current_item_text:str):
            packages_dialog = QDialog()
            packages_dialog.resize(500,300)
            packages_dialog.setMinimumWidth(500)
            packages_dialog.setWindowTitle('Packages')
            packages_dialog.setWindowIcon(self.WINDOW_ICON)
            text_browser_conda_packages = QTextBrowser()
            text_browser_conda_packages.setStyleSheet(
                "background-color: transparent;"
            )
            layout_packages_dialog = QHBoxLayout(packages_dialog)
            layout_packages_dialog.addWidget(text_browser_conda_packages)
            text_browser_conda_packages.setFocusPolicy(Qt.NoFocus)
            
            Conda_Get_Detail = Conda_Get_Detail_QThread(self, current_item_text)
            Conda_Get_Detail.text_to_textBrowser_cmd.connect(lambda content: self.append_TB_text(content, self.Win.textBrowser_cmd))
            Conda_Get_Detail.signal_conda_detail_list.connect(lambda x: display_detail(x, text_browser_conda_packages))
            Conda_Get_Detail.start()
            packages_dialog.exec_()
        
        # 处理线程信号，显示输出结果
        def display_detail(detail_text:str, text_browser_obj:object):
            add_flag = True
            while add_flag:
                if detail_text:
                    self.append_TB_text(detail_text, text_browser_obj)
                    add_flag = False
        # 信号连接
        list_widget.itemSelectionChanged.connect(pb_state_update)
        list_widget.doubleClicked.connect(conda_dialog.accept)
        pb_package_view.clicked.connect(lambda: show_detail(list_widget.currentItem().text()))
        pb_finish.clicked.connect(conda_dialog.accept)
        pb_cancel.clicked.connect(conda_dialog.reject)
        
        result = conda_dialog.exec_()
        
        if result == QDialog.Accepted:
            selected_items = list_widget.currentItem().text()
            return selected_items
    
    def font_increase_px(self, widget, increase_value):
        ori_size = widget.font().pixelSize()
        if isinstance(widget, QTextBrowser) or isinstance(widget, QPlainTextEdit):
            text_flag = widget.toPlainText()
        else:
            text_flag = widget.text()
        if text_flag:
            new_size = ori_size + increase_value
            self.font_size_setting(widget, new_size)
            return 1, new_size
        return 0, ori_size
    
    def textbrowser_font_increase_by_pb(self, widget):
        flag, new_size = self.font_increase_px(widget, 1)
        if widget == self.Win.textBrowser and flag:
            setting_file['textBrowser_font_size_px'] = new_size
        elif widget == self.Win.textBrowser and flag:
            setting_file['textBrowser_cmd_font_size_px'] = new_size

