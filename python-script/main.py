from pyinstaller_function import *

from PyQt5.QtWidgets import QApplication, QMainWindow

class Exe_main_window(QMainWindow, Pyinstaller_function):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(self.WINDOW_ICON)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Exe_main_window()
    mainWindow.show()
    sys.exit(app.exec_())

