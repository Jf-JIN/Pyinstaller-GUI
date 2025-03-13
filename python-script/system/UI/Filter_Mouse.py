from __future__ import annotations
from DToolslib.Logger import Logger
from PyQt5.QtCore import pyqtSignal, QObject, QEvent, Qt, QTimer
from PyQt5.QtWidgets import QLabel

from const.Const_Parameter import *
from system.Manager_Data import *
from system.Manager_Language import *
from system.Manager_Executor_Info import ExecutorInfoStruct
from system.Struct_Env_Info import StructEnvInfo
from system.Thread_Pip_Install import ThreadPipInstall
from system.Struct_Env_Info import *

if 0:
    from UI.UI_PyToExe import PyToExeUI

_log: Logger = Log.UI


class LabelLeftDoubleToInstallFilter(QObject):
    signal_output_text_LableDoubleFilter = pyqtSignal(str)

    def __init__(self, parent, label: QLabel, env_struct: StructEnvInfo) -> None:
        super().__init__(label)
        self.__parent: PyToExeUI = parent
        self.__data_manager: DataManager = DataManager()
        self.__executor_info_manager = ExecutorInfoManager()
        self.__label: QLabel = label
        self.__env_struct: StructEnvInfo = env_struct

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.MouseButtonDblClick and obj is not None:
            if event.button() == Qt.MouseButton.LeftButton:
                current_env: ExecutorInfoStruct = self.__data_manager.current_env
                python_path = current_env.python_path
                pyinstaller_path: str = current_env.pyinstaller_path
                # 如果是 内置, 则不执行
                if current_env.name == self.__data_manager.builtin_env.name:
                    pass
                elif python_path:
                    self.__thread = ThreadPipInstall(python_path)
                    self.__thread.signal_output_text.connect(self.signal_output_text_LableDoubleFilter.emit)
                    self.__thread.signal_finished.connect(lambda: self.__parent.show_message(LM.getWord('finish_pyinstaller_install')))
                    # 如果当前环境是本地环境, 则更新本地环境. Conda 和 Specified 环境是自动定时更新, 不需要手动更新
                    if current_env.name == self.__executor_info_manager.local_struct.name:
                        self.__thread.signal_finished.connect(self.__executor_info_manager.update_local_env)
                    self.__parent.show_message(LM.getWord('start_pyinstaller_install'))
                    self.__thread.start()
        return super().eventFilter(obj, event)


class LabelLeftDoubleOrLangPressFilter(QObject):
    signal_textbrowser_LDFilter = pyqtSignal(str)
    signal_doublePress_longPress = pyqtSignal(str)

    def __init__(self, parent, label: QLabel):
        super().__init__(label)
        self.__parent: PyToExeUI = parent
        self.__label: QLabel = label
        self.__timer_press = QTimer()
        self.__timer_press.timeout.connect(self.__long_press_action)
        self.__time_interval_s = 1.5
        self.__time_interval = int(self.__time_interval_s * 1000)

    def __long_press_action(self):
        self.__timer_press.stop()
        self.signal_doublePress_longPress.emit('longPressed')

    def eventFilter(self, obj, event):
        # 双击
        if event.type() == QEvent.Type.MouseButtonDblClick and obj is not None and event.button() == Qt.MouseButton.LeftButton:
            self.__timer_press.stop()
            self.signal_doublePress_longPress.emit('doublePressed')
        # 长按
        if event.type() == QEvent.Type.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
            if not self.__timer_press.isActive():
                self.__timer_press.start(self.__time_interval)
            self.is_long_press = False
        elif event.type() == QEvent.Type.MouseButtonRelease and event.button() == Qt.MouseButton.LeftButton:
            if self.__timer_press.isActive():
                self.__timer_press.stop()
        return super().eventFilter(obj, event)
