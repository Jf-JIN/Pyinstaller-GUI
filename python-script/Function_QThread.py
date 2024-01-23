import subprocess
import threading
from PyToExe_ui import *
from PyQt5.QtCore import pyqtSignal, QThread
from copy import deepcopy

class Launch_py_QThread(QThread):
    finished_signal = pyqtSignal()
    
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
                self.parent_class.append_TB_text(output_line.strip(), self.parent_class.Win.textBrowser_cmd)
        self.parent_class.append_TB_text(f'__________ {content} __________\n', self.parent_class.Win.textBrowser_cmd)
        self.parent_class.append_TB_text(f'__________ {content} __________\n', self.parent_class.Win.textBrowser)
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
            self.parent_class.append_TB_text(f'__________ {self.parent_class.json_general["error"]} __________\n{e}\n', self.parent_class.Win.textBrowser_cmd)


class pyinstaller_setup_Qthread(QThread):
    def __init__(self, parent):
        super().__init__()
        self.parent_class = parent
    
    def read_output(self, object:object, content:str):
        while True:
            output_line = object.stdout.readline()
            if output_line == '' and object.poll() is not None:
                break
            if output_line:
                self.parent_class.append_TB_text(output_line.strip(), self.parent_class.Win.textBrowser_cmd)
        self.parent_class.append_TB_text(f'__________ {content} __________\n', self.parent_class.Win.textBrowser_cmd)
        self.parent_class.append_TB_text(f'__________ {content} __________\n', self.parent_class.Win.textBrowser)
    
    def run(self):
        self.py_install_command = 'pip install pyinstaller'
        self.full_command = f'echo Y | {self.py_install_command}'
        try:
            process = subprocess.Popen(self.full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            thread = threading.Thread(target=self.read_output(process, self.parent_class.json_widgets['pb_SetupPyinstaller']['text_browser_display']))
            thread.start()
        except subprocess.CalledProcessError as e:
            self.parent_class.append_TB_text(f'__________ {self.parent_class.json_general["error"]} __________\n{e}\n', self.parent_class.Win.textBrowser_cmd)


class Environment_Variant_Thread(QThread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        subprocess.run('rundll32 sysdm.cpl,EditEnvironmentVariables')


class Conda_Get_Env_List_Thread(QThread):
    signal_conda_env_list = pyqtSignal(list)
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
            self.parent_class.append_TB_text(f'__________ {self.parent_class.json_general["error"]} __________\n{e}\n', self.parent_class.Win.textBrowser_cmd)
    # def __del__(self):
    #     print("Conda_Get_Env_List_Thread object is being destroyed.")


class Conda_Get_Detail_Thread(QThread):
    signal_conda_detail_list = pyqtSignal(str)
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
            self.parent_class.append_TB_text(f'__________ {self.parent_class.json_general["error"]} __________\n{e}\n', self.parent_class.Win.textBrowser_cmd)
    # def __del__(self):
    #     print("Conda_Get_Env_List_Thread object is being destroyed.")