import os
from PyQt5.QtCore import QThread, pyqtSignal
from tools.wait_thread import wait_for_thread_result

__thread_pool_find_pyinstaller_path = []


def find_pyinstaller_path(start_path: str):
    def thread_finished():
        __thread_pool_find_pyinstaller_path.remove(thread_find)
    thread_find = Finder(start_path)
    __thread_pool_find_pyinstaller_path.append(thread_find)
    thread_find.finished.connect(thread_finished)
    thread_find.start()
    return wait_for_thread_result(thread_find.signal_pyinstaller_path, '')


class Finder(QThread):
    signal_pyinstaller_path = pyqtSignal(str)
    signal_finished = pyqtSignal()

    def __init__(self, start_path: str):
        super().__init__()
        self.__start_path = start_path

    def __find_pyinstaller_path(self, start_path: str):
        if not start_path:
            return ''
        elif start_path.endswith('python.exe'):
            start_path = os.path.dirname(start_path)
        target_file = 'pyinstaller.exe'
        for entry in os.scandir(start_path):
            # if entry.name.startswith('.') or start_path.endswith('miniconda3') and entry.name != 'Scripts':
            #     continue
            if entry.is_file() and entry.name == target_file:
                return entry.path
            elif entry.is_dir():
                result = self.__find_pyinstaller_path(entry.path)
                if result:
                    return result
        return ''

    def run(self):
        pyinstaller_path = self.__find_pyinstaller_path(self.__start_path)
        self.signal_pyinstaller_path.emit(pyinstaller_path)
        self.signal_finished.emit()


# def find_pyinstaller_path(start_path: str):
#     if not start_path:
#         return ''
#     elif start_path.endswith('python.exe'):
#         start_path = os.path.dirname(start_path)
#     target_file = 'pyinstaller.exe'
#     for entry in os.scandir(start_path):
#         if entry.name.startswith('.') or start_path.endswith('miniconda3') and entry.name != 'Scripts':
#             continue
#         if entry.is_file() and entry.name == target_file:
#             return entry.path
#         elif entry.is_dir():
#             result = find_pyinstaller_path(entry.path)
#             if result:
#                 return result
#     return ''
