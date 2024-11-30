from PyQt5.QtCore import QEventLoop, pyqtSignal, QObject, QEvent, Qt, QTimer
from PyQt5.QtWidgets import QLabel

from system.Thread_Pip_Install import ThreadPipInstall
from system.Struct_env_info import *
# from UI.UI_PyToExe import PyToExeUI # 可以用于检查 PyToExeUI 中的属性、方法名是否正确. 注意! 运行时必须注释掉, 否则将循环引入


class LabelLeftDoubleToInstallFilter(QObject):
    signal_textbrowser_LDFilter = pyqtSignal(str)

    def __init__(self, parent, label: QLabel, env_struct: StructEnvInfo):
        super().__init__(label)
        # self.__parent: PyToExeUI = parent # 用于检查, 记得运行时注释掉! 
        self.__parent = parent
        self.__label = label
        self.__env_struct = env_struct

    def __wait_for_thread_result(self, outputsignal: pyqtSignal) -> bool:
        """
        等待线程完成并返回结果
        """
        loop = QEventLoop()
        outputsignal.connect(lambda: loop.quit())
        loop.exec_()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonDblClick and obj is not None:
            if event.button() == Qt.LeftButton:
                pyinstaller_path = self.__env_struct.path_pyinstaller
                python_interpreter_path = self.__env_struct.path_python
                if python_interpreter_path != '' and not pyinstaller_path:
                    # 如果是 指定, 但是路径错误, 则不执行
                    if self.__label == self.__parent.lb_env_specified_check_install_page_setting_env and self.__parent.env_struct_current.path_error:
                        return super().eventFilter(obj, event)
                    self.__thread = ThreadPipInstall(python_interpreter_path)
                    self.__thread.signal_textbrowser_pip_install.connect(self.signal_textbrowser_LDFilter.emit)
                    self.__thread.start()
                    self.__wait_for_thread_result(self.__thread.signal_finished)

                    # 全局
                    if self.__label == self.__parent.lb_env_current_check_install_page_base or self.__label == self.__parent.lb_env_current_check_install_page_setting_env:
                        # 选中 Conda
                        if self.__parent.rb_env_conda.isChecked():
                            self.__parent.update_env_conda_specified()
                        # 选中 指定
                        elif self.__parent.rb_env_specified.isChecked():
                            self.__parent.update_env_specified()
                        else:
                            self.__parent.update_env_sys()  # 系统 或者 指定但是路径错误
                    # conda
                    elif self.__label == self.__parent.lb_env_conda_check_install_page_setting_env:
                        self.__parent.update_env_conda_specified()  # 函数内已经使用了更新全局
                    # 指定
                    elif self.__label == self.__parent.lb_env_specified_check_install_page_setting_env:
                        self.__parent.update_env_specified()
                    # 系统
                    elif self.__label == self.__parent.lb_env_sys_check_install_page_setting_env:
                        self.__parent.update_env_sys()
        return super().eventFilter(obj, event)


class LabelLeftDoubleOrLangPressFilter(QObject):
    signal_textbrowser_LDFilter = pyqtSignal(str)
    signal_doublePress_longPress = pyqtSignal(str)

    def __init__(self, parent, label: QLabel):
        super().__init__(label)
        # self.__parent: PyToExeUI = parent # 用于检查, 记得运行时注释掉! 
        self.__parent = parent
        self.__label = label
        self.__timer_press = QTimer()
        self.__timer_press.timeout.connect(self.__long_press_action)
        self.__time_interval_s = 1.5
        self.__time_interval = int(self.__time_interval_s * 1000)

    def __long_press_action(self):
        self.__timer_press.stop()
        self.signal_doublePress_longPress.emit('longPressed')

    def eventFilter(self, obj, event):
        # 双击
        if event.type() == QEvent.MouseButtonDblClick and obj is not None and event.button() == Qt.LeftButton:
            self.__timer_press.stop()
            self.signal_doublePress_longPress.emit('doublePressed')
        # 长按
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            if not self.__timer_press.isActive():
                self.__timer_press.start(self.__time_interval)
            self.is_long_press = False
        elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            if self.__timer_press.isActive():
                self.__timer_press.stop()
        return super().eventFilter(obj, event)
