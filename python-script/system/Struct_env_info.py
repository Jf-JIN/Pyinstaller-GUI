
from .Signal_Event import EventSignal

from PyQt5.QtCore import QTimer


class StructEnvInfo(object):
    signal_isChanged = EventSignal()

    def __init__(self, name):
        self.__name = name
        self.env_name: str = ''
        self.path_python: str = ''
        self.path_pyinstaller: str = None
        self.version: str = ''
        self.path_error: bool = False  # 给 指定解释器路径 用的, 记录路径是否错误
        self.command_launch: str = ''  # 给 当前环境 用的, 记录启动路径
        self.__timer_setattr = QTimer()
        self.__timer_setattr.timeout.connect(self.__emit_signal)

    @property
    def name(self) -> str:
        """获取环境名称"""
        return self.__name

    def __setattr__(self, name, value):
        if hasattr(self, f'_{self.__class__.__name__}__timer_setattr'):
            self.__timer_setattr.start(100)
        return super().__setattr__(name, value)

    def __str__(self):
        return f"环境名称: {self.env_name}\npython路径: {self.path_python}\n环境版本: {self.version}"

    def __emit_signal(self):
        self.signal_isChanged.emit()
        self.__timer_setattr.stop()
