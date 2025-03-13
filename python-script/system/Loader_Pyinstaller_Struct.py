

from system.Struct_Pyinstaller import *
from const.Const_Parameter import *
from system.UI.Dialog_MessageBox import DialogMessageBox
from tools import *

_log: Logger = Log.DataManager


class PyinstallerStructLoader:

    def __init__(self) -> None:
        self.__path_configurations_set: set = set()
        self.__system_tpye: str = App.OS
        self.__pyinstaller_struct: PyinstallerStruct = PyinstallerStruct()
        self.__implement_path: str = ''
        self.__pyinstaller_command: str = ''

    @property
    def path_configurations(self) -> list:
        return list(self.__path_configurations_set)

    @property
    def pyinstaller_struct(self) -> PyinstallerStruct:
        return self.__pyinstaller_struct.copy()

    @property
    def pyinstaller_command(self) -> str:
        return self.__pyinstaller_command

    @property
    def implement_path(self) -> str:
        return self.__implement_path

    def read_file(self, file_path) -> tuple:
        """
        读取安装命令行文件

        参数:
            file_path: 安装命令行文件路径

        返回:
            path_configurations(list): 配置信息, 如: set PATH=C:/Users/.../Library/bin;%PATH%
            implement_path(str): 执行器路径
            pyinstaller_struct(PyinstallerStruct): pyinstaller 结构体
        """
        self.__read_file_in_lines(file_path)
        _log.trace(f'path_configurations: {self.path_configurations}\npyinstaller_struct: {self.pyinstaller_struct}')
        return self.path_configurations, self.implement_path, self.pyinstaller_struct

    def read_command(self, command_line_str: str) -> tuple:
        self.__pyinstaller_struct.clear()
        command_line_str = command_line_str.replace("'", '"')
        command_line_list = command_line_str.split('\n')
        for command in command_line_list:
            self.__parse_command(command)
        return self.path_configurations, self.implement_path, self.pyinstaller_struct

    def __call__(self, file_path, *args, **kwds):
        return self.read_file(file_path)

    def __parse_command(self, command: str) -> bool:
        if command.startswith(('set', 'export')):
            self.__parse_and_set_env_path(command)
        elif (
            command.startswith(('pyinstaller ', 'PyInstaller ')) or
            ('pyinstaller ' in command.lower()) or
            'pyinstaller.exe' in command
        ):
            # 这里有一个特性, 只会存在一个pyinstaller命令, 且只读取第一个命令:
            self.__load_pyinstaller_command_in_struct(command)
            return True
        return False

    def __read_file_in_lines(self, file_path) -> list:
        self.__path_configurations_set.clear()
        self.__pyinstaller_struct.clear()
        with open(file_path,  'r', encoding='utf-8') as f:
            line = f.readline().strip()
            while line:
                flag_finished: bool = self.__parse_command(line)
                if flag_finished:
                    break
                line = f.readline()

    def __parse_and_set_env_path(self, line_str: str) -> None:
        """
        解析并设置环境变量路径
        line_str 示例:
        Windows: set PATH=C:\\Users\\username\\miniconda3\\envs\\envsname\\Library\\bin;%PATH%
        Linux:   export PATH="Users/username/miniconda3/envs/envsname/Library/bin:$PATH"
        MacOs:   export PATH="$HOME/miniconda3/envs/envsname/Library/bin:$PATH" 
        """
        self.__path_configurations_set.clear()
        path = split_path_from_env_config_line(line_str)
        if path:
            self.__path_configurations_set.add(path)

    def __split_implement_and_cmd(self, line_str_list: list) -> tuple:
        implement_path = ''
        flag_start = False  # 标记是否是 pyinstaller 命令的开始, 不含执行器的部分
        while len(line_str_list) > 0:
            item = self.__get_next_param(line_str_list)
            if 'python.exe' in item or 'pyinstaller.exe' in item or 'pyinstaller' in item.lower() in ['python', 'pyinstaller']:
                # 注意: 此处可能是pyinstaller.exe 或 python.exe 或者就直接是 python 或者 pyinstaller
                flag_start = True
                temp_path = item.replace('\\', '/').replace('"', '')
                if os.path.exists(temp_path):
                    implement_path = temp_path
                continue
            elif not flag_start:
                continue
            if item in ['-m', 'PyInstaller', 'pyinstaller']:
                continue
            else:
                line_str_list.insert(0, item)
                break
        return implement_path, line_str_list

    def __get_next_param(self, cmd_data: list) -> str:
        """
        获取下个参数, 针对带有双引号的参数, 如:  "C:/test folder with space/test.py"
        """
        if len(cmd_data) == 0:
            return ''
        param: str = cmd_data.pop(0)
        flag_stop = False
        if param.startswith('"') or '="' in param:
            param_list = [param]
            if not param.endswith('"'):
                while len(cmd_data) > 0:
                    if cmd_data[0].endswith('"'):
                        flag_stop = True
                    temp_param = cmd_data.pop(0)
                    param_list.append(temp_param)
                    if flag_stop:
                        break
            param = ' '.join(param_list)
        return param

    def __load_pyinstaller_command_in_struct(self, line_str: str) -> None:
        line_str_list: list = line_str.strip().split(' ')
        self.__implement_path, self.__command_line = self.__split_implement_and_cmd(line_str_list)
        self.__parse_pyinstaller_command(self.__command_line)

    def __parse_pyinstaller_command(self, command_line_list: list):
        hasUnknownParam = False
        try:
            while len(command_line_list) > 0:
                param_phrase = self.__get_next_param(command_line_list)
                # 含有 = 的参数;  RelPathStruct | MultiInfoStruct | SingleInfoStruct
                if '=' in param_phrase:
                    param_name, param_value = param_phrase.split('=', 1)
                    struct:  RelPathStruct | MultiInfoStruct | SingleInfoStruct | None = self.__pyinstaller_struct.find_struct_from_option(param_name)
                    if struct is None:
                        _log.debug(f'未找到对应参数 {param_name}')
                        hasUnknownParam = True
                        continue
                    if param_name in App.Pyinstaller.LIST_MULTI:
                        # RelPathStruct | MultiInfoStruct
                        struct: RelPathStruct | MultiInfoStruct
                        struct.append_args(param_value)
                    else:
                        # SingleInfoStruct
                        struct: SingleInfoStruct
                        struct.set_args(param_value)
                # StateStruct 带参数
                elif param_phrase in App.Pyinstaller.DICT_STATE_WITH_PARAMS:
                    param_name = param_phrase
                    struct:   StateStruct | None = self.__pyinstaller_struct.find_struct_from_option(param_name)
                    if struct is None:
                        _log.debug(f'未找到对应参数 {param_name}')
                        hasUnknownParam = True
                        continue
                    parm_state = self.__get_next_param(command_line_list)
                    struct.set_state(parm_state)
                # StateStruct 不带参数
                elif param_phrase in App.Pyinstaller.DICT_STATE_WITHOUT_PARAMS['--onefile'] or param_phrase in App.Pyinstaller.DICT_STATE_WITHOUT_PARAMS['--console']:
                    param_name = param_phrase
                    if param_phrase in App.Pyinstaller.DICT_STATE_WITHOUT_PARAMS['--onefile']:
                        option_key = '--onefile'
                    else:
                        option_key = '--console'
                    struct:   StateStruct | None = self.__pyinstaller_struct.find_struct_from_option(option_key)
                    if struct is None:
                        _log.debug(f'未找到对应参数 {param_name}')
                        hasUnknownParam = True
                        continue
                    struct: StateStruct
                    struct.set_state(param_phrase)
                # SwitchStruct
                elif param_phrase in App.Pyinstaller.LIST_SWITCH:
                    param_name = param_phrase
                    struct:   SwitchStruct | None = self.__pyinstaller_struct.find_struct_from_option(param_name)
                    if struct is None:
                        _log.debug(f'未找到对应参数 {param_name}')
                        hasUnknownParam = True
                        continue
                    else:
                        struct.set_on()
                else:
                    param_name = param_phrase.strip('"')
                    # 针对 执行文件
                    if param_name.endswith(('.py', 'pyw', 'pyd', '.spec')):
                        struct:   SingleInfoStruct | None = self.__pyinstaller_struct.find_struct_from_option('')
                        if struct is None:
                            _log.debug(f'未找到对应参数 {param_name}')
                            hasUnknownParam = True
                            continue
                        struct.set_args(param_phrase)
                    # 以下针对非标准写法, 比如需要写 "=", 但是没有写的情况
                    # StateStruct 带参数
                    elif param_name in App.Pyinstaller.DICT_STATE_WITH_PARAMS:
                        struct:   StateStruct | None = self.__pyinstaller_struct.find_struct_from_option(option_key)
                        if struct is None:
                            _log.debug(f'未找到对应参数 {param_name}')
                            hasUnknownParam = True
                            continue
                        parm_state = self.__get_next_param(command_line_list)
                        struct.set_state(parm_state)
                    # SingleInfoStruct
                    elif param_name in App.Pyinstaller.LIST_SINGLE:
                        struct: SingleInfoStruct | None | None = self.__pyinstaller_struct.find_struct_from_option(param_phrase)
                        if struct is None:
                            _log.debug(f'未找到对应参数 {param_name}')
                            hasUnknownParam = True
                            continue
                        parm_arg = self.__get_next_param(command_line_list)
                        struct.set_args(parm_arg)
                    # RelPathStruct | MultiInfoStruct
                    elif param_name in App.Pyinstaller.LIST_MULTI:
                        struct: RelPathStruct | MultiInfoStruct | None = self.__pyinstaller_struct.find_struct_from_option(param_phrase)
                        if struct is None:
                            _log.debug(f'未找到对应参数 {param_name}')
                            hasUnknownParam = True
                            continue
                        parm_arg = self.__get_next_param(command_line_list)
                        struct.append_args(parm_arg)
                    else:
                        _log.debug(f'未找到对应参数 "{param_name}"({param_phrase})')
                        hasUnknownParam = True
                        continue
        except:
            _log.exception('命令解析异常')
        if hasUnknownParam:
            DialogMessageBox.warning(None, '存在未知参数, 请检查命令行参数')
