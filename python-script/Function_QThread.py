import subprocess
import threading
from datetime import datetime
from copy import deepcopy

from PyQt5.QtCore import pyqtSignal, QThread

class Launch_py_QThread(QThread):
    finished_signal = pyqtSignal()
    text_to_textBrowser_cmd = pyqtSignal(str)
    text_to_textBrowser = pyqtSignal(str)
    def __init__(self, parent, command_list):
        super().__init__()
        self.command_list = deepcopy(command_list)
        self.parent_class = parent
    
    def read_output(self, content: str):
        while True:
            output_line = self.process.stdout.readline()
            if output_line == '' and self.process.poll() is not None:
                break
            if output_line:
                self.text_to_textBrowser_cmd.emit(output_line.strip())
        
        self.text_to_textBrowser_cmd.emit(f'__________ {content} __________')
        self.text_to_textBrowser.emit(f'__________ {content} __________')
        self.finished_signal.emit()
    
    def run(self):
        # self.full_command = f'{self.command[0]} && {self.command[1]} && echo Y | {self.command[2]}'
        self.command_list[-1] = 'echo Y | ' + self.command_list[-1]
        self.full_command = ' && '.join(self.command_list)
        try:
            finish_text = self.parent_class.json_special['launch_cmd']['text_browser_display']
            self.process = subprocess.Popen(self.full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            self.thread = threading.Thread(target=self.read_output, args=(finish_text,))
            self.thread.start()
        except subprocess.CalledProcessError as e:
            self.text_to_textBrowser_cmd.emit(f'__________ {self.parent_class.json_general["error"]} __________\n{e}\n')


class pyinstaller_setup_QThread(QThread):
    text_to_textBrowser_cmd = pyqtSignal(str)
    text_to_textBrowser = pyqtSignal(str)
    def __init__(self, parent):
        super().__init__()
        self.parent_class = parent
    
    def read_output(self, object:object, content:str):
        while True:
            output_line = object.stdout.readline()
            if output_line == '' and object.poll() is not None:
                break
            if output_line:
                self.text_to_textBrowser_cmd.emit(output_line.strip())
        self.text_to_textBrowser_cmd.emit(f'__________ {content} __________\n')
        self.text_to_textBrowser.emit(f'__________ {content} __________\n')
    
    def run(self):
        self.py_install_command = 'echo Y | pip install pyinstaller'
        if self.parent_class.Win.cb_CondaUse.isEnabled() and self.parent_class.Win.cb_CondaUse.isChecked():
            conda_env = self.parent_class.Win.lb_CondaInfo.text()
            self.py_install_command = f'conda activate {conda_env} && echo Y | conda install pyinstaller'
        try:
            process = subprocess.Popen(self.py_install_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            thread = threading.Thread(target=self.read_output(process, self.parent_class.json_widgets['pb_SetupPyinstaller']['text_browser_display']))
            thread.start()
        except subprocess.CalledProcessError as e:
            self.text_to_textBrowser_cmd.emit(f'__________ {self.parent_class.json_general["error"]} __________\n{e}\n')


class Environment_Variant_QThread(QThread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        subprocess.run('rundll32 sysdm.cpl,EditEnvironmentVariables')


class Conda_Get_Env_List_QThread(QThread):
    signal_conda_env_list = pyqtSignal(list)
    text_to_textBrowser_cmd = pyqtSignal(str)
    def __init__(self, parent):
        super().__init__()
        self.parent_class = parent
    
    def run(self):
        try:
            result = subprocess.Popen('conda env list', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            output = result.stdout.read().strip()
            # print(output)
            # 分割输出成行
            lines = output.split('\n')
            # 获取环境列表,[0]是环境名，[1]是环境地址
            conda_env_list = [line.split() for line in lines if not line.startswith('#')]
            self.signal_conda_env_list.emit(conda_env_list)
        except subprocess.CalledProcessError as e:
            self.text_to_textBrowser_cmd.emit(f'__________ {self.parent_class.json_general["error"]} __________\n{e}\n')
    # def __del__(self):
    #     print("Conda_Get_Env_List_Thread object is being destroyed.")


class Conda_Get_Detail_QThread(QThread):
    signal_conda_detail_list = pyqtSignal(str)
    text_to_textBrowser_cmd = pyqtSignal(str)
    def __init__(self, parent, conda_env):
        super().__init__()
        self.conda_env = conda_env
        self.parent_class = parent
    
    def run(self):
        try:
            result = subprocess.Popen(f'conda list --name="{self.conda_env}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            output = result.stdout.read().strip()
            self.signal_conda_detail_list.emit(output)
        except subprocess.CalledProcessError as e:
            self.text_to_textBrowser_cmd.emit(f'__________ {self.parent_class.json_general["error"]} __________\n{e}\n')
    # def __del__(self):
    #     print("Conda_Get_Env_List_Thread object is being destroyed.")