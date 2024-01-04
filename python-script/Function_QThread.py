import subprocess
import threading
from PyToExe_ui import *
from PyQt5.QtCore import pyqtSignal, QThread
from copy import deepcopy

class Launch_py_QThread(QThread):
    output_to_textbrowser_cmd = pyqtSignal(str)
    output_to_textbrowser = pyqtSignal(str)
    finished_signal = pyqtSignal()

    def __init__(self, command):
        super().__init__()
        self.command = deepcopy(command)

    def read_output(self, content: str):
        while True:
            output_line = self.process.stdout.readline()
            if output_line == '' and self.process.poll() is not None:
                break
            if output_line:
                print(output_line.strip())
                self.output_to_textbrowser_cmd.emit(output_line.strip())
        self.output_to_textbrowser_cmd.emit(f'__________ {content} __________\n')
        self.output_to_textbrowser.emit(f'__________ {content} __________\n')
        self.finished_signal.emit()

    def run(self):
        self.full_command = f'{self.command[0]} && {self.command[1]} && echo Y | {self.command[2]}'
        # print(f'Command: {self.full_command}') 
        try:
            self.process = subprocess.Popen(
                self.full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            self.thread = threading.Thread(
                target=self.read_output, args=('已完成Python脚本的打包',))
            self.thread.start()
        except subprocess.CalledProcessError as e:
            self.output_to_textbrowser_cmd.emit(
                f'__________ 错 误 __________\n{e}\n')


class pyinstaller_setup_Qthread(QThread):
    output_to_textbrowser_cmd = pyqtSignal(str)
    output_to_textbrowser = pyqtSignal(str)
    finished_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
    
    def read_output(self, object:object, content:str):
        while True:
            output_line = object.stdout.readline()
            if output_line == '' and object.poll() is not None:
                break
            if output_line:
                self.output_to_textbrowser_cmd.emit(output_line.strip())
        self.output_to_textbrowser_cmd.emit(f'________________________________________\n')
        self.output_to_textbrowser.emit(f'\n__________ {content} __________\n')
        self.finished_signal.emit()
    
    def run(self):
        self.py_install_command = 'pip install pyinstaller'
        self.full_command = f'echo Y | {self.py_install_command}'
        try:
            process = subprocess.Popen(self.full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            thread = threading.Thread(target=self.read_output(process, '已成功安装pyinstaller'))
            thread.start()
        except subprocess.CalledProcessError as e:
                self.output_to_textbrowser_cmd.emit(
                    f'\n__________ 错 误 __________\n{e}\n')