
from PyQt5.QtCore import QThread, pyqtSignal
import subprocess
import threading

from const.Const_Parameter import *
from system.Manager_Language import *
from system.UI.Message_Notification import *

_log = Log.Threads


class ThreadPipInstall(QThread):
    signal_output_text = pyqtSignal(str)
    signal_finished = pyqtSignal()

    def __init__(self, python_interpreter_path):
        super().__init__()
        self.__python_interpreter_path = python_interpreter_path
        self.__isReading = True

    def __read_output(self):
        while self.__isReading:
            output_line = self.__result.stdout.readline()
            if output_line == '' and self.__result.poll() is not None:
                break
            if output_line:
                self.signal_output_text.emit(output_line)
        _log.info(LM.getWord('finish_pyinstaller_install'))
        self.signal_finished.emit()

    def run(self):
        _log.info(LM.getWord('start_pyinstaller_install'))
        self.__result = subprocess.Popen(
            f'"{self.__python_interpreter_path}" -m pip install pyinstaller --upgrade',
            creationflags=subprocess.CREATE_NO_WINDOW,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        self.thread_read = threading.Thread(target=self.__read_output)
        self.thread_read.start()

    def __del__(self) -> None:
        self.__isReading = False
        self.thread_read.join()
