
from PyQt5.QtCore import QObject, pyqtSignal, QTimer

from system.Struct_Env_Info import StructEnvInfo
from system.Struct_Pyinstaller import PyinstallerStruct

from .Struct_Pyinstaller import *
from .Struct_Env_Info import *
from .Signal_Event import *


class DataManager(QObject):
    __instance = None
    signal_isNeededUpdateDisplay = EventSignal()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            super(DataManager, cls.__instance).__init__()
            cls.__instance.__isInitialized = False
        return cls.__instance

    def __setattr__(self, name, value) -> None:
        if hasattr(self, f'_{self.__class__.__name__}__timer_setattr'):
            self.__timer_setattr.stop()
            self.__timer_setattr.start(100)
        return super().__setattr__(name, value)

    def __init__(self) -> None:
        if self.__isInitialized:
            return
        super().__init__()
        self.__isInitialized = True
        self.__timer_setattr = QTimer()
        self.__timer_setattr.timeout.connect(self.__emit_signal)
        self.__init_parameter()
        self.__init_signal_connections()

    def __init_parameter(self) -> None:
        self.__pyinstaller_struct = PyinstallerStruct()
        self.__env_specified = StructEnvInfo('specified')
        self.__env_sys = StructEnvInfo('sys')
        self.__env_conda = StructEnvInfo('conda')
        self.__env_builtin = StructEnvInfo('builtin')
        self.__env_current = None
        self.__env_current_name = ''  # 用于对比当前环境是否更改
        """ 记录当前环境名称, 如: 'specified', 'sys', 'conda', 'builtin' """
        self.__install_mode: str = ''
        """ 记录当前安装方式, 如Python, Pyinstaller """
        self.__envs = {
            'specified': self.__env_specified,
            'system': self.__env_sys,
            'conda': self.__env_conda,
            'builtin': self.__env_builtin
        }

    def __init_signal_connections(self):
        self.__pyinstaller_struct.signal_isChanged.connect(self.__emit_signal)
        self.__env_specified.signal_isChanged.connect(self.__emit_signal)
        self.__env_sys.signal_isChanged.connect(self.__emit_signal)
        self.__env_conda.signal_isChanged.connect(self.__emit_signal)
        self.__env_builtin.signal_isChanged.connect(self.__emit_signal)
        self.__install_mode

    def __emit_signal(self):
        self.__timer_setattr.stop()
        self.signal_isNeededUpdateDisplay.emit()

    def set_current_env(self, env_name: str):

        if env_name not in self.__envs:
            raise ValueError(f'env_name {env_name} is not valid')
        if env_name == self.__env_current_name:
            return
        self.__env_current_name = env_name
        self.__env_current: StructEnvInfo = self.__envs[env_name]
        self.__emit_signal()

    def set_implement_path(self, implement_path: str):
        """
        置执行器路径, 其中定义了三个属性
        - self.__install_mode: 安装模式 pyinstaller / python / unspecified
        - self.__implement_path: 执行器路径(无引号) 如: 'E:\Python\Python38\Scripts\pyinstaller.exe' 或 'E:\Python\Python38\python.exe'
        - self.__implement_command: 执行器命令(含结尾空格), 如: '"E:\Python\Python38\Scripts\pyinstaller.exe" ' 或 '"E:\Python\Python38\python.exe" -m PyInstaller '

        参数:
        - implement_path: str, 执行器路径

        返回:
        None
        """
        if implement_path and 'pyinstaller.exe' in implement_path and os.path.exists(implement_path):
            self.__install_mode = 'pyinstaller'
            self.__implement_path = implement_path
            self.__implement_command = f'"{implement_path}" '
        elif implement_path and 'python.exe' in implement_path and os.path.exists(implement_path):
            self.__install_mode = 'python'
            self.__implement_path = implement_path
            self.__implement_command = f'"{implement_path}" -m PyInstaller '
        else:
            self.__install_mode = 'unspecified'
            self.__implement_path = ''
            self.__implement_command = 'PyInstaller '

    def set_pyinstaller_struct(self, pyinstaller_struct: PyinstallerStruct) -> None:
        self.__pyinstaller_struct: PyinstallerStruct = pyinstaller_struct

    def set_env_path_configs(self, set_env_path_configs: list) -> None:
        self.__set_env_path_configs: list = set_env_path_configs

    @property
    def env_path_configs(self) -> str:
        return self.__set_env_path_configs

    @property
    def pyinstaller_struct(self) -> PyinstallerStruct:
        return self.__pyinstaller_struct

    @property
    def env_current(self) -> StructEnvInfo:
        return self.__env_current

    @property
    def env_specified(self) -> StructEnvInfo:
        return self.__env_specified

    @property
    def env_sys(self) -> StructEnvInfo:
        return self.__env_sys

    @property
    def env_conda(self) -> StructEnvInfo:
        return self.__env_conda

    @property
    def display_data(self):
        pass
