

from PyQt5.QtCore import QThread, pyqtSignal
import subprocess
import threading


class ThreadPipInstall(QThread):
    signal_textbrowser_pip_install = pyqtSignal(str)
    signal_finished = pyqtSignal(bool)

    def __init__(self, python_interpreter_path):
        super().__init__()
        self.__python_interpreter_path = python_interpreter_path

    def __read_output(self):
        while True:
            output_line = self.__result.stdout.readline()
            if output_line == '' and self.__result.poll() is not None:
                break
            if output_line:
                self.signal_textbrowser_pip_install.emit(output_line)
        self.signal_finished.emit(True)

    def run(self):
        self.__result = subprocess.Popen(f'"{self.__python_interpreter_path}" -m pip install pyinstaller', creationflags=subprocess.CREATE_NO_WINDOW,
                                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        self.thread_read = threading.Thread(target=self.__read_output)
        self.thread_read.start()
