
from UI.UI_PyToExe import *

""" 
所有参数设置的函数方法都是
1. 进行输入检查
2. 显示参数
3. 保存参数
4. 更新数据显示
"""


class FunctionUI(PyToExeUI):
    def __init__(self):
        super().__init__()

    def init_parameters(self):
        super().init_parameters()

    def init_ui(self):
        super().init_ui()

    def init_signal_connections(self):
        super().init_signal_connections()
        self.pb_input_py_file_browser.clicked.connect(self.set_input_py_file_path)
        self.pb_output_folder_browser.clicked.connect(self.set_output_folder_path)
        self.le_output_folder_path.editingFinished.connect(self.write_output_folder_path)
        self.le_output_file_name.editingFinished.connect(self.write_output_file_name)

    def init_python_file_path(self):
        self.le_input_py_file_path.clear()
        self.le_output_folder_path.clear()
        self.le_output_file_name.clear()
        if len(sys.argv) > 1 and sys.argv[1].endswith(('.py', '.pyw', '.pyd', '.spec')):
            file_path = sys.argv[1]
            self.app_workspace_path = os.path.dirname(file_path)
        elif len(sys.argv) > 1 and sys.argv[1].endswith(('.txt', '.ocl')):
            self.installer_manager.read_file(sys.argv[1])
            file_path = self.installer.python_file_path.command
        elif self.installer.python_file_path.command and os.path.exists(self.installer.python_file_path.command):
            file_path = self.installer.python_file_path.command
        else:
            return
        self.le_input_py_file_path.setText(file_path)
        self.le_output_folder_path.setText(os.path.dirname(file_path))
        self.le_output_file_name.setText(os.path.splitext(os.path.basename(file_path))[0])
        # 写配置文件
        self.installer.python_file_path.set_args(file_path)
        self.setting['last_command'] = self.installer.get_command_line(self.env_struct_current.path_pyinstaller)
        self.setting_manager.write_file_to_json()
        # 更新安装器信息
        self.update_installer_info()

    def set_input_py_file_path(self):
        file_path = QFileDialog.getOpenFileName(
            self, '选择输入文件', self.app_workspace_path, """Accepted Files (*.py *.pyw *.pyd *.spec *.txt *.ocl);; 
            Python Files (*.py *.pyw *.pyd *.spec);; 
            Text Files (*.txt);; 
            Output Command Line Files (*.ocl)""")[0]
        folder_path = ''
        output_file_name = ''
        if not file_path:
            return
        if file_path.endswith(('.ocl', '.txt')):
            hasError = self.installer_manager.read_file(file_path)
            if hasError == 'hasError':
                self.message.notification('文件错误, 非标准格式')
                return
            file_path = self.installer.python_file_path.command_args
            if self.installer.output_folder_path.command:
                folder_path = self.installer.output_folder_path.command_args
            if self.installer.output_file_name.command:
                output_file_name = self.installer.output_file_name.command_args

        self.le_input_py_file_path.setText(file_path)
        self.app_workspace_path = os.path.dirname(file_path)
        # 写配置文件
        self.installer.python_file_path.set_args(file_path)
        self.setting['last_command'] = self.installer.get_command_line(self.env_struct_current.path_pyinstaller)
        if not self.cb_lock_output_folder.isChecked():
            if not folder_path:
                folder_path = os.path.dirname(file_path)
            self.le_output_folder_path.setText(folder_path)
            self.installer.output_folder_path.set_args(folder_path)
        if not self.cb_lock_output_file_name.isChecked():
            if not output_file_name:
                output_file_name = os.path.splitext(os.path.basename(file_path))[0]
            self.le_output_file_name.setText(output_file_name)
            self.installer.output_file_name.set_args(output_file_name)
        self.setting_manager.write_file_to_json()
        # 更新安装器信息
        self.update_installer_info()

    def set_output_folder_path(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择输出文件夹', self.app_workspace_path)
        if not folder_path:
            return
        self.le_output_folder_path.setText(folder_path)
        self.installer.output_folder_path.set_args(folder_path)
        # 更新安装器信息
        self.update_installer_info()

    def write_output_folder_path(self):
        folder_path = self.le_output_folder_path.text()
        if not folder_path:
            return
        self.installer.output_folder_path.set_args(folder_path)
        # 更新安装器信息
        self.update_installer_info()

    def set_output_file_name(self):
        file_name: str = self.le_output_file_name.text()
        if not file_name:
            return
        self.installer.output_file_name.set_args(file_name)
        # 更新安装器信息
        self.update_installer_info()

    def write_output_file_name(self):
        file_path: str = self.le_input_py_file_path.text()
        output_file_name: str = self.le_output_file_name.text()
        if not file_path:
            return
        self.installer.output_file_name.set_args(output_file_name)
        # 更新安装器信息
        self.update_installer_info()
