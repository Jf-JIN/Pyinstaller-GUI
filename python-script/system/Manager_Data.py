
from PyQt5.QtCore import QObject, pyqtSignal, QTimer

from const.Const_Parameter import *
from system.Struct_Pyinstaller import PyinstallerStruct
from system.Manager_Executor_Info import *
from tools.data_handle import normalize_path, split_path_from_env_config_line

from .Struct_Pyinstaller import *
from .Struct_Env_Info import *
from DToolslib import *

_log = Log.DataManager


class DataManager(QObject):
    """
    数据管理器(单例)
    """
    __instance = None
    signal_pyinstaller_data_changed_DM = pyqtSignal()
    signal_current_env_changed_DM = pyqtSignal()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            super(DataManager, cls.__instance).__init__()
            cls.__instance.__isInitialized = False
        return cls.__instance

    def __setattr__(self, name, value) -> None:
        if hasattr(self, f'_{self.__class__.__name__}__timer_setattr') and hasattr(self, f'_{self.__class__.__name__}__interval'):
            self.__timer_setattr.stop()
            self.__timer_setattr.start(self.__interval)
        return super().__setattr__(name, value)

    def __init__(self) -> None:
        if self.__isInitialized:
            return
        super().__init__()
        self.__isInitialized = True
        self.__interval = 100
        self.__timer_setattr = QTimer()
        self.__timer_setattr.setSingleShot(True)
        self.__timer_setattr.timeout.connect(self.__emit_signal)
        self.__init_parameter()
        self.__init_signal_connections()

    def __init_parameter(self) -> None:
        self.__pyinstaller_struct = PyinstallerStruct()
        self.__current_env: ExecutorInfoStruct = ExecutorInfoStruct('')
        self.__builtin_env: ExecutorInfoStruct = ExecutorInfoStruct('\\ <builtin>')
        self.__config_set = set()
        self.__config_input_set = set()

    def __init_signal_connections(self) -> None:
        self.__pyinstaller_struct.signal_data_changed.connect(self.__wait_to_emit)

    def __emit_signal(self) -> None:
        self.signal_pyinstaller_data_changed_DM.emit()

    def __wait_to_emit(self) -> None:
        if self.__timer_setattr.isActive():
            self.__timer_setattr.stop()
        self.__timer_setattr.start(self.__interval)

    def set_current_env(self, struct: ExecutorInfoStruct) -> None:
        self.__current_env = struct
        self.signal_current_env_changed_DM.emit()

    def set_implement_path(self, path_str: str) -> None:
        if path_str.endswith('pyinstaller.exe'):
            self.__current_env.set_pyinstaller_path(path_str)
        elif path_str.endswith('python.exe'):
            self.__current_env.set_python_path(path_str)

    def set_input_config(self, config_data: list | tuple | set) -> None:
        if not isinstance(config_data, set):
            config_data = set(config_data)
        temp = set()
        for config in config_data:
            temp.add(normalize_path(config))
        self.__config_input_set: set = temp

    def remove_config_item(self, config_item: str) -> None:
        config_path = split_path_from_env_config_line(config_item)
        if config_path:
            self.__config_input_set.discard(config_path)
            self.__update_config_set()

    def add_config_item(self, config_path: str) -> None:
        if not config_path or config_path in self.__config_input_set:
            return
        self.__config_input_set.add(config_path)
        self.__update_config_set()

    def set_config(self, config_data: list | tuple | set) -> None:
        """ 还没有考虑 input和set config的冲突, 此时 input还没有更新 """
        if not isinstance(config_data, set):
            config_data = set(config_data)
        self.__config_set: set = config_data

    def set_pyinstaller_struct(self, pyinstaller_struct: PyinstallerStruct) -> None:
        self.__pyinstaller_struct: PyinstallerStruct = pyinstaller_struct
        self.__pyinstaller_struct.signal_data_changed.connect(self.__wait_to_emit)

    def __format_env_config(self, env_path):
        if App.OS == OsType.WINDOWS:
            env_path = f'set PATH="{env_path};%PATH%"'.replace('\\', '/')
        elif App.OS == OsType.LINUX or App.OS == OsType.MACOS:
            env_path = f'export PATH="{env_path}:$PATH"'.replace('\\', '/')
        else:
            env_path = ''
        return env_path

    def command_use_pyinstaller(self, isIncludeContentsDir: bool = True) -> str:
        if not self.__current_env.pyinstaller_path:
            env_path = 'PyInstaller '
        else:
            env_path = f'"{self.__current_env.pyinstaller_path}" '
        pyinstaller_command = self.__pyinstaller_struct.get_command_line(isIncludeContentsDir=isIncludeContentsDir)
        pyinstaller_command_with_env = f'{env_path}{pyinstaller_command}'
        command = '\n'.join(self.config_str_list+[pyinstaller_command_with_env])
        return command

    def command_use_python(self, isIncludeContentsDir: bool = True) -> str:
        if not self.__current_env.python_path:
            env_path = 'PyInstaller '
        else:
            env_path = f'"{self.__current_env.python_path}" -m PyInstaller '
        pyinstaller_command = self.__pyinstaller_struct.get_command_line(isIncludeContentsDir=isIncludeContentsDir)
        pyinstaller_command_with_env = f'{env_path}{pyinstaller_command}'
        command = '\n'.join(self.config_str_list+[pyinstaller_command_with_env])
        return command

    def __update_config_set(self) -> None:
        temp = set(list(self.__config_input_set) + self.__current_env.config_libraries)
        if not temp == self.__config_set:
            self.__config_set = temp
        # _log.critical(f'config_input_set: {self.__config_input_set} \t config_libraries: {self.__current_env.config_libraries}')

    @property
    def config_path_list(self) -> list:
        self.__update_config_set()
        return list(self.__config_set)

    @property
    def config_str_list(self) -> list:
        temp = []
        for config in self.config_path_list:
            temp.append(self.__format_env_config(config))
        return temp

    @property
    def pyinstaller_struct(self) -> PyinstallerStruct:
        return self.__pyinstaller_struct

    @property
    def current_env(self) -> ExecutorInfoStruct:
        return self.__current_env

    @property
    def builtin_env(self) -> ExecutorInfoStruct:
        return self.__builtin_env
