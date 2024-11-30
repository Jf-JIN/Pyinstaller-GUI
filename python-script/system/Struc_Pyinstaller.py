""" 
pyinstaller数据结构类

类: 
- BasicStruct(name:str, cmd_option:str): 基础类, 用于存储命令行参数
- SwitchStruct(name:str, cmd_option:str): 开关类, 用于存储开关参数
- StateStruct(name:str, cmd_option:str): 状态类, 用于存储状态参数, 例如:  --onefile --console --debug 等
- SingleInfoStruct(name:str, cmd_option:str): 单信息类, 用于存储单信息参数, 例如:  --distpath=E:\Programm 等
- MultiInfoStruct(name:str, cmd_option:str): 多信息类, 用于存储多信息参数, 例如:  --add-data=1.txt;E:\Programm 等
- RelPathStruct(name:str, cmd_option:str): 相对地址类, 用于存储相对地址参数, 例如:  --add-data="Programm;." 等
- StrucPyinstaller(name:str, cmd_option:str): pyinstaller数据结构类

函数: 
- 无

变量: 
- 无

"""
import os
import json
import copy


class BasicStruct(object):
    """ 
    基础类, 用于存储命令行参数

    参数: 
    - name: 结构名称
    - cmd_option: 命令行选项

    属性: 
    - name: 结构名称
    - command_option: 命令行选项
    - command_args: 命令行参数
    - command: 命令行

    方法: 
    - _set_command_option(command_option:str):  设置命令行选项
    - _set_args(para:str):  设置命令行参数, 直接覆盖添加
    - _add_args(para:str):  添加命令行参数, 在原有基础添加
    - _clear_args():  清空命令行参数
    """

    def __init__(self, name: str, cmd_option: str | list, isRepeatable: bool = False):
        super().__init__()
        self.__name = name
        self.__command_option = cmd_option  # 例如:  '--distpath' 或  ['-D', '--distpath']
        if isRepeatable:
            self.__command_args: list = []  # 例如:  ["E:\\10_Programm"] (可重复)
        else:
            self.__command_args: str = ''  # 例如:  "E:\\10_Programm" (不可重复)
        self._command = ''

    @property
    def name(self) -> str:
        return self.__name

    @property
    def command_option(self) -> str:
        return self.__command_option

    @property
    def command_args(self) -> list | str:
        return self.__command_args

    @property
    def command(self) -> str:
        return self._command

    def _set_args(self, para: str | list) -> None:
        self.__command_args = para

    def _add_args(self, para: str) -> None:
        if isinstance(self.__command_args, list):
            self.__command_args.append(para)

    def _clear_args(self) -> None:
        if isinstance(self.__command_args, list):
            self.__command_args.clear()
        else:
            self.__command_args = ''
        self._command = ''

    def _set_command_option(self, command_option: str) -> None:
        self.__command_option = command_option


class SwitchStruct(BasicStruct):
    """ 
    开关结构类
        用于存储开关命令行参数, 开则是存在命令, 关则是不存在命令, 例如: --clean --strip -noupx 等

    参数: 
    - name: 结构名称
    - cmd_option: 命令行选项

    属性: 
    - name: 结构名称
    - command_option: 命令行选项
    - command_args: 命令行参数
    - command: 命令行
    - isOn: 开关状态

    方法: 
    - set_on():  设置开关为开启状态
    - set_off():  设置开关为关闭状态

    """

    def __init__(self, name: str, cmd_option: str | list) -> None:
        super().__init__(name, cmd_option)
        self.__isOn = False

    @property
    def isOn(self) -> bool:
        return self.__isOn

    def set_on(self) -> None:
        self.__isOn = True
        self._command = self.command_option

    def set_off(self) -> None:
        self.__isOn = False
        self._clear_args()

    def _clear_args(self):
        super()._clear_args()
        self.__isOn = False


class StateStruct(BasicStruct):
    """ 
    状态结构类
        用于存储状态命令行参数, 其会有不同的状态参数, 例如:  --onefile --console --debug

    参数:
    - name: 结构名称
    - cmd_option: 命令行选项
    - isWithOption: 是否带选项, 默认为 True

    属性:
    - name: 结构名称
    - command_option: 命令行选项
    - command_args: 命令行参数
    - command: 命令行
    - current_state: 当前状态
    - isWithOption: 是否带选项

    方法: 
    - set_state(state:str): 设置状态
    """

    def __init__(self, name: str, cmd_option: str | list, isWithOption: bool = True) -> None:
        super().__init__(name, cmd_option)
        self.__current_state = ''
        self.__command = ''
        self.__isWithOption = isWithOption

    @property
    def current_state(self) -> str:
        return self.__current_state

    @property
    def command(self) -> str:
        return self.__command

    @property
    def isWithOption(self) -> bool:
        return self.__isWithOption

    def set_state(self, state: str) -> None:
        if state is None:
            self._clear_args()
            self._command = ''
            return None
        self.__current_state = state
        if self.__isWithOption:
            option = self.command_option[0] if isinstance(self.command_option, list) else self.command_option
            self.__command = f'{option} {self.__current_state}'
            self._set_args(self.__current_state)
        else:
            self.__command = state

    def _clear_args(self):
        super()._clear_args()
        self.__command = ''
        self.__current_state = ''


class SingleInfoStruct(BasicStruct):
    """ 
    单信息结构类
        用于存储单信息命令行参数, 例如:  --distpath=E:\Programm 等

    参数:
    - name: 结构名称
    - cmd_option: 命令行选项

    属性:
    - name: 结构名称
    - command_option: 命令行选项
    - command_args: 命令行参数
    - command: 命令行

    方法: 
    - set_args(para:str): 设置命令行参数
    """

    def __init__(self, name: str, cmd_option: str | list) -> None:
        super().__init__(name, cmd_option)

    def set_args(self, para: str) -> None:
        if para is None or para == '':
            self._clear_args()
            return None
        if '"' in para:
            para = para.replace('"', '')
        self._set_args(para)
        if self.command_option == '':  # 针对 python 执行文件路径
            self._command = f'"{para}"'
            return None
        option = self.command_option[0] if isinstance(self.command_option, list) else self.command_option
        self._command = f'{option}="{self.command_args}"'


class MultiInfoStruct(BasicStruct):
    """ 
    多信息结构类
        用于存储多信息命令行参数, 允许重复使用, 例如:  --paths="E:\Programm" --paths="C:\Python_includes" 等

    参数:
    - name: 结构名称
    - cmd_option: 命令行选项

    属性:
    - name: 结构名称
    - command_option: 命令行选项
    - command_args: 命令行参数
    - command: 命令行

    方法: 
    - set_args(para:list): 设置命令行参数
    - append_args(para:str): 追加命令行参数
    """

    def __init__(self, name, cmd_option: str) -> None:
        super().__init__(name, cmd_option, isRepeatable=True)

    def set_args(self, para: list | str) -> None:
        if para is None or para == []:
            self._clear_args()
            return None
        if isinstance(para, str):
            if '"' in para:
                para = para.replace('"', '')
            para = [para]
        elif isinstance(para, list):
            pass
        else:
            print(f'[类型错误][MultiInfoStruct][set_args]: 应为 <list> 或 <str>\t实际为{type(para)}')
        self._set_args(para)
        option = self.command_option[0] if isinstance(self.command_option, list) else self.command_option
        self._command = f'{option}="' + f'" {option}="'.join(self.command_args) + '"'

    def append_args(self, para: str):
        if para is None or para == '':
            return None
        if '"' in para:
            para = para.replace('"', '')
        self._add_args(para)
        option = self.command_option[0] if isinstance(self.command_option, list) else self.command_option
        self._command = f'"{option}"="' + f'" {option}"='.join(self.command_args) + '"'


class RelPathStruct(BasicStruct):
    """ 
    相对地址结构类
        用于存储相对地址命令行参数, 例如:  --add-data="Programm;." 等

    参数:
    - name: 结构名称
    - cmd_option: 命令行选项

    属性:
    - name: 结构名称
    - command_option: 命令行选项
    - command_args: 命令行参数
    - command: 命令行
    - command_args_display: 命令行参数显示, 用于UI端显示输入信息

    方法: 
    - set_args(list_para:list): 设置命令行参数
    - append_args(str_para:str): 追加命令行参数
    """

    def __init__(self, name: str, cmd_option: str) -> None:
        super().__init__(name, cmd_option, isRepeatable=True)
        self.__command_args_display = []

    @property
    def command_args_display(self) -> list:
        return self.__command_args_display

    def set_args(self, list_para: list | str) -> None:
        if isinstance(list_para, str):
            if '"' in list_para:
                list_para = para.replace('"', '')
            list_para = [list_para]
        if list_para is None or list_para == []:
            self._clear_args()
            return None
        self.__command_args_display = list_para
        temp_list = []
        for para in list_para:
            format_dir = f'{os.path.basename(para)}:{os.path.relpath(para, os.getcwd())}'
            temp_list.append(format_dir)
        self._set_args(temp_list)
        option: str = self.command_option[0] if isinstance(self.command_option, list) else self.command_option
        self._command = f'"{option}"="' + f'" {option}"='.join(self.command_args) + '"'

    def append_args(self, para: str):
        if para is None or para == '':
            return None
        if '"' in para:
            para = para.replace('"', '')
        if ':' not in para:
            format_dir = f'{os.path.basename(para)}:{os.path.relpath(para, os.getcwd())}'
        else:
            format_dir = para
        self._add_args(format_dir)
        self.__command_args_display.append(para)
        option: str = self.command_option[0] if isinstance(self.command_option, list) else self.command_option
        self._command = f'{option}="' + f'" {option}="'.join(self.command_args) + '"'

    def _clear_args(self):
        super()._clear_args()
        self.__command_args_display = []


class StrucPyinstaller(object):
    """ 
    pyinstaller结构类
        用于存储完整pyinstaller命令行结构, 参数等

    属性: 
    - install_mode(str): 安装模式 pyinstaller / python / unspecified
    - implement_path(str): 执行器路径(无引号) 如: 'E:\Python\Python38\Scripts\pyinstaller.exe' 或 'E:\Python\Python38\python.exe'
    - implement_command(str): 执行器命令(含结尾空格), 如: '"E:\Python\Python38\Scripts\pyinstaller.exe" ' 或 '"E:\Python\Python38\python.exe" -m PyInstaller '
    - ...命令行属性
        (python_file_path, output_methode, specpath, output_file_name, contents_directory, add_file_folder_data, add_binary_data, imports_paths, hidden_import, collect_submodules, collect_data, collect_binaries, collect_all, copy_metadata, recursive_copy_metadata, additional_hooks_dir, runtime_hook, exclude_module, add_splash_screen, debug_mode, python_option, strip_option, noupx_option, upx_exclude, console_window_control, hide_console, add_icon, disable_traceback, version_file, add_xml_file, add_resource, uac_admin_apply, uac_uiaccess, argv_emulation, osx_bundle_identifier, target_architecture, codesign_identity, osx_entitlements_file, runtime_tmpdir, ignore_signals, output_folder_path, workpath_option, noconfirm_option, upx_dir, clean_cache, log_level)

    方法: 
    - set_implement_path(implement_path: str): 设置执行器路径
    - get_command_list(): 获取命令行参数列表
    - get_command_line(): 获取命令行
    - get_struct_list(): 获取结构列表, 列表元素为存在命令的结构对象 StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct
    - get_flattened_struct_command_args(): 获取扁平化的结构命令行参数, 用于平面显示当前结构的命令参数, 例如使用TableWidget
    - get_flattened_dict_command_args(): 获取扁平化的结构命令行参数, 用于生成命令行
    - find_struct_from_option(option:str): 根据命令行选项查找结构
    """
    @property
    def install_mode(self):
        return self.__install_mode

    @property
    def implement_path(self):
        return self.__implement_path

    @property
    def implement_command(self):
        return self.__implement_command

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
        if 'pyinstaller.exe' in implement_path and os.path.exists(implement_path):
            self.__install_mode = 'pyinstaller'
            self.__implement_path = implement_path
            self.__implement_command = f'"{implement_path}" '
        elif 'python.exe' in implement_path and os.path.exists(implement_path):
            self.__install_mode = 'python'
            self.__implement_path = implement_path
            self.__implement_command = f'"{implement_path}" -m PyInstaller '
        else:
            self.__install_mode = 'unspecified'
            self.__implement_path = ''
            self.__implement_command = 'PyInstaller '

    def get_command_dict(self) -> dict:
        """ 
        获取当前结构中的所有命令参数, 并返回一个字典, 键名为命令的名字，值为命令行

        返回: 
        dict: 例如 {'output_methode': '-F', 'imports_paths': '-p="E:\\10_Programm" -p="E:\\10_Programm\\test"'}}
        """
        temp = {
        }
        for item in self.__sequence:
            item: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct
            if item.command != '':
                temp[item.name] = item.command
        return temp

    def get_command_list(self) -> list:
        """ 
        获取命令行列表，可用于使用 内置pyinstaller. 

        返回: 
        list[str]: 如 ['-c', '-F', 'main.py', '-p="E:\Python\Python38"']
        """
        temp_list = []
        for item in self.__sequence:
            item: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct
            if item.command != '':
                temp_list.append(item.command)
        return temp_list

    def get_command_line(self, implement_path: str) -> str:
        """ 
        获取命令行字符串

        参数: 
        implement_path: str, 实现路径, 如 'E:\Python\Python38\Scripts\pyinstaller.exe'

        返回:
        str: 如 '"E:\Python\Python38\Scripts\pyinstaller.exe" -c -F main.py -p="E:\Python\Python38"'
         """
        temp_list = self.get_command_list()
        if not temp_list:
            print(f'从 get_command_list() 返回空值, 命令行无参数, 请检查. {temp_list}')
            return None
        self.set_implement_path(implement_path)   # 此处定义了 self.__install_mode, self.__implement_path, self.__implement_command
        launch_command = self.__implement_command + ' '.join(temp_list)
        # 弃用
        # if withPathChange:
        #     driver_path = os.path.splitdrive(self.__python_file_path.command)[0]
        #     py_script_path = os.path.dirname(self.__python_file_path.command)
        #     return f'{driver_path}\ncd {py_script_path}\n{launch_command}'
        return launch_command

    def get_struct_list(self) -> list:
        """ 
        获取有效结构列表

        返回:
        list: 如 [StateStruct(...), SwitchStruct(...), RelPathStruct(...), SingleInfoStruct(...), MultiInfoStruct(...)]
        """
        temp = []
        for item in self.__sequence:
            item: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct
            if item.command != '':
                temp.append(item)
        return temp

    def get_flattened_struct_command_args(self) -> dict:
        """ 
        用于平面显示当前结构的命令参数, 例如使用TableWidget
        获取当前结构中的所有命令参数, 并返回一个字典, 字典分为两个部分, 一个是含有的命令项数目/长度, 一个是命令数据. 命令数据以对象为键, 命令参数(列表|字符串)为值
        例如: {'length': 3, 'data': {StateStruct对象: '-F', MultiInfoStruct对象: ["E:\\10_Programm","E:\\10_Programm\\test"]}}

        返回: 
        dict: 包含当前结构中所有有效命令参数的字典, 键名为对象本身
        """
        temp = {
            'length': 0,
            'data': {}
        }
        for item in self.__sequence:
            item: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct
            if item.command != '':
                temp['data'][item] = item.command_args
                if isinstance(item.command_args, list):
                    temp['length'] += len(item.command_args)
                else:
                    temp['length'] += 1
        return temp

    def find_struct_from_option(self, option: str) -> SingleInfoStruct | StateStruct | RelPathStruct | MultiInfoStruct | SwitchStruct | None:
        """ 
        通过命令选项查找结构

        参数: 
        option: str: 命令选项

        返回:
        SingleInfoStruct | StateStruct | RelPathStruct | MultiInfoStruct | SwitchStruct | None: 找到的结构, 如果没有找到则返回None
        """
        for item in self.__sequence:
            item: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct
            if isinstance(item.command_option, list):
                if option in item.command_option:
                    return item
            elif item.command_option == option:
                return item
        return None

    def clear(self):
        """ 清空结构 """
        for i in self.__sequence:
            i: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct
            i._clear_args()

    def copy(self):
        """ 深拷贝结构 """
        return copy.deepcopy(self)

    def __init__(self) -> None:
        # -------------------------------------------------------------------------------
        # 开关结构类 9
        # -------------------------------------------------------------------------------
        self.__strip_option = SwitchStruct('strip_option', ['--strip', '-s'])
        self.__noupx_option = SwitchStruct('noupx_option', '--noupx')
        self.__disable_traceback = SwitchStruct('disable_traceback', '--disable-windowed-traceback')
        self.__uac_admin_apply = SwitchStruct('uac_admin_apply', '--uac-admin')
        self.__uac_uiaccess = SwitchStruct('uac_uiaccess', '--uac-uiaccess')
        self.__argv_emulation = SwitchStruct('argv_emulation', '--argv-emulation')
        self.__ignore_signals = SwitchStruct('ignore_signals', '--bootloader-ignore-signals')
        self.__noconfirm_option = SwitchStruct('noconfirm_option', ['--noconfirm', '-y'])
        self.__clean_cache = SwitchStruct('clean_cache', '--clean')
        # -------------------------------------------------------------------------------
        # 状态结构类 7
        # -------------------------------------------------------------------------------
        self.__output_methode = StateStruct('output_methode', ['--onefile', '--onedir', '-D', '-F'], False)
        self.__console_window_control = StateStruct('console_window_control', ['--console', '--nowindowed', '--windowed', '--noconsole', '-c', '-w'], False)
        self.__debug_mode = StateStruct('debug_mode', ['--debug', '-d'])
        self.__python_option = StateStruct('python_option', '--python-option')
        self.__hide_console = StateStruct('hide_console', '--hide-console')
        self.__target_architecture = StateStruct('target_architecture', ['--target-architecture', '--target-arch'])
        self.__log_level = StateStruct('log_level', '--log-level')
        # -------------------------------------------------------------------------------
        # 单信息结构类 14
        # -------------------------------------------------------------------------------
        self.__specpath = SingleInfoStruct('specpath', '--specpath')
        self.__contents_directory = SingleInfoStruct('contents_directory', '--contents-directory')
        self.__version_file = SingleInfoStruct('version_file', '--version-file')
        self.__add_xml_file = SingleInfoStruct('add_xml_file', ['--manifest', '-m'])
        self.__osx_bundle_identifier = SingleInfoStruct('osx_bundle_identifier', '--osx-bundle-identifier')
        self.__codesign_identity = SingleInfoStruct('codesign_identity', '--codesign-identity')
        self.__osx_entitlements_file = SingleInfoStruct('osx_entitlements_file', '--osx-entitlements-file')
        self.__runtime_tmpdir = SingleInfoStruct('runtime_tmpdir', '--runtime-tmpdir')
        self.__workpath_option = SingleInfoStruct('workpath_option', '--workpath')
        self.__upx_dir = SingleInfoStruct('upx_dir', '--upx-dir')
        self.__add_splash_screen = SingleInfoStruct('add_splash_screen', '--splash')
        self.__python_file_path = SingleInfoStruct('python_file_path', '')
        self.__output_file_name = SingleInfoStruct('output_file_name', '--name')
        self.__output_folder_path = SingleInfoStruct('output_folder_path', '--distpath')
        # -------------------------------------------------------------------------------
        # 多信息结构类 14
        # -------------------------------------------------------------------------------
        self.__imports_paths = MultiInfoStruct('imports_paths', ['--paths', '-p'])
        self.__hidden_import = MultiInfoStruct('hidden_import', ['--hidden-import', '--hiddenimport'])
        self.__collect_submodules = MultiInfoStruct('collect_submodules', '--collect-submodules')
        self.__collect_data = MultiInfoStruct('collect_data', ['--collect-data', '--collect-datas'])
        self.__collect_binaries = MultiInfoStruct('collect_binaries', '--collect-binaries')
        self.__collect_all = MultiInfoStruct('collect_all', '--collect-all')
        self.__copy_metadata = MultiInfoStruct('copy_metadata', '--copy-metadata')
        self.__recursive_copy_metadata = MultiInfoStruct('recursive_copy_metadata', '--recursive-copy-metadata')
        self.__additional_hooks_dir = MultiInfoStruct('additional_hooks_dir', '--additional-hooks-dir')
        self.__runtime_hook = MultiInfoStruct('runtime_hook', '--runtime-hook')
        self.__exclude_module = MultiInfoStruct('exclude_module', '--exclude-module')
        self.__upx_exclude = MultiInfoStruct('upx_exclude', '--upx-exclude')
        self.__add_icon = MultiInfoStruct('add_icon', ['--icon', '-i'])
        self.__add_resource = MultiInfoStruct('add_resource', ['--resource', '-r'])
        # -------------------------------------------------------------------------------
        # 相对路径结构类 2
        # -------------------------------------------------------------------------------
        self.__add_file_folder_data = RelPathStruct('add_file_folder_data', '--add-data')
        self.__add_binary_data = RelPathStruct('add_binary_data', '--add-binary')
        # -------------------------------------------------------------------------------
        # 命令顺序
        # -------------------------------------------------------------------------------
        self.__sequence: tuple = (
            self.__python_file_path,
            self.__output_methode,
            self.__specpath,
            self.__output_file_name,
            self.__contents_directory,
            self.__add_file_folder_data,
            self.__add_binary_data,
            self.__imports_paths,
            self.__hidden_import,
            self.__collect_submodules,
            self.__collect_data,
            self.__collect_binaries,
            self.__collect_all,
            self.__copy_metadata,
            self.__recursive_copy_metadata,
            self.__additional_hooks_dir,
            self.__runtime_hook,
            self.__exclude_module,
            self.__add_splash_screen,
            self.__debug_mode,
            self.__python_option,
            self.__strip_option,
            self.__noupx_option,
            self.__upx_exclude,
            self.__console_window_control,
            self.__hide_console,
            self.__add_icon,
            self.__disable_traceback,
            self.__version_file,
            self.__add_xml_file,
            self.__add_resource,
            self.__uac_admin_apply,
            self.__uac_uiaccess,
            self.__argv_emulation,
            self.__osx_bundle_identifier,
            self.__target_architecture,
            self.__codesign_identity,
            self.__osx_entitlements_file,
            self.__runtime_tmpdir,
            self.__ignore_signals,
            self.__output_folder_path,
            self.__workpath_option,
            self.__noconfirm_option,
            self.__upx_dir,
            self.__clean_cache,
            self.__log_level
        )
        # -------------------------------------------------------------------------------
        # python 解释器路径
        # -------------------------------------------------------------------------------
        self.__python_interpreter_path = ''

    @property
    def python_file_path(self):
        return self.__python_file_path

    @property
    def output_methode(self):
        return self.__output_methode

    @property
    def specpath(self):
        return self.__specpath

    @property
    def output_file_name(self):
        return self.__output_file_name

    @property
    def contents_directory(self):
        return self.__contents_directory

    @property
    def add_binary_data(self):
        return self.__add_binary_data

    @property
    def imports_paths(self):
        return self.__imports_paths

    @property
    def hidden_import(self):
        return self.__hidden_import

    @property
    def collect_submodules(self):
        return self.__collect_submodules

    @property
    def collect_data(self):
        return self.__collect_data

    @property
    def collect_binaries(self):
        return self.__collect_binaries

    @property
    def collect_all(self):
        return self.__collect_all

    @property
    def copy_metadata(self):
        return self.__copy_metadata

    @property
    def recursive_copy_metadata(self):
        return self.__recursive_copy_metadata

    @property
    def additional_hooks_dir(self):
        return self.__additional_hooks_dir

    @property
    def runtime_hook(self):
        return self.__runtime_hook

    @property
    def exclude_module(self):
        return self.__exclude_module

    @property
    def add_splash_screen(self):
        return self.__add_splash_screen

    @property
    def debug_mode(self):
        return self.__debug_mode

    @property
    def python_option(self):
        return self.__python_option

    @property
    def strip_option(self):
        return self.__strip_option

    @property
    def noupx_option(self):
        return self.__noupx_option

    @property
    def upx_exclude(self):
        return self.__upx_exclude

    @property
    def console_window_control(self):
        return self.__console_window_control

    @property
    def hide_console(self):
        return self.__hide_console

    @property
    def add_icon(self):
        return self.__add_icon

    @property
    def disable_traceback(self):
        return self.__disable_traceback

    @property
    def version_file(self):
        return self.__version_file

    @property
    def add_xml_file(self):
        return self.__add_xml_file

    @property
    def add_resource(self):
        return self.__add_resource

    @property
    def uac_admin_apply(self):
        return self.__uac_admin_apply

    @property
    def uac_uiaccess(self):
        return self.__uac_uiaccess

    @property
    def argv_emulation(self):
        return self.__argv_emulation

    @property
    def osx_bundle_identifier(self):
        return self.__osx_bundle_identifier

    @property
    def target_architecture(self):
        return self.__target_architecture

    @property
    def codesign_identity(self):
        return self.__codesign_identity

    @property
    def osx_entitlements_file(self):
        return self.__osx_entitlements_file

    @property
    def runtime_tmpdir(self):
        return self.__runtime_tmpdir

    @property
    def ignore_signals(self):
        return self.__ignore_signals

    @property
    def output_folder_path(self):
        return self.__output_folder_path

    @property
    def workpath_option(self):
        return self.__workpath_option

    @property
    def noconfirm_option(self):
        return self.__noconfirm_option

    @property
    def upx_dir(self):
        return self.__upx_dir

    @property
    def clean_cache(self):
        return self.__clean_cache

    @property
    def log_level(self):
        return self.__log_level

    def __take_whole_path(self, path_str: str):
        temp_list = path_str.split(' ')
        if len(temp_list) == 0:
            return None
        path_part = temp_list.pop(0)
        if path_part.startswith('"'):
            path_list = [path_part]
            while temp_list and not path_list[-1].endswith('"'):
                temp_param = temp_list.pop(0)
                path_list.append(temp_param)
            path_part = ' '.join(path_list)
        return path_part

    def __dict_struct(self) -> dict:
        temp_dict = {}
        for item in self.__sequence:
            item: StateStruct | SwitchStruct | RelPathStruct | SingleInfoStruct | MultiInfoStruct
            if not item.command:
                continue
            temp_dict[item.command] = {
                'name': item.name,
                'command_option': item.command_option,
                'command_args': item.command_args,
                'command': item.command
            }
            if hasattr(item, 'current_state'):
                temp_dict[item.command]['current_state'] = item.current_state
        return temp_dict

    def __str__(self):
        return json.dumps(self.__dict_struct(), indent=4, ensure_ascii=False)
