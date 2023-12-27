import sys


from pyinstaller_function import *

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class Exe_main_window(QMainWindow, Pyinstaller_function):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(WINDOW_ICON_PATH))
        self.setWindowTitle(f'Python 打包转换为可执行程序.exe 开发工具')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Exe_main_window()
    mainWindow.show()
    sys.exit(app.exec_())
