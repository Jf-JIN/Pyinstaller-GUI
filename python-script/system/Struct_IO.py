

from system.Struc_Pyinstaller import *
from traceback import format_exc


class Struct_IO(object):
    """ 
    StrucPyinstaller 读写器

    参数：
    无

    属性：
    - struct_data: StrucPyinstaller 实例，用于存储读取的数据

    方法：
    - read_file(file_path): 从指定路径读取文件，并解析为 StrucPyinstaller 实例
    - [弃用] write_file(file_path, data): 将 StrucPyinstaller 实例写入指定路径的文件
    """

    def __init__(self):
        super().__init__()
        self.__struct_data = StrucPyinstaller()

    @property
    def struct_data(self):
        return self.__struct_data

    def read_file(self, file_path):
        data = self.__read_file(file_path)
        cmd_data = self.__get_cmd_data(data)
        hasError = self.__sort_cmd_data(cmd_data)
        if hasError == 'hasError':  # 发生错误
            return 'hasError'
        elif hasError is None:  # 无数据, 空值
            return None
        result = self.__struct_data.get_command_line(self.__implement_path_from_file)
        if result == '' or result == None:
            return None
        return self.__struct_data

    # # 弃用方法，不必使用路径转换
    # def write_file(self, file_path, data: list | str):
    #     if isinstance(data, list):  # 涵盖路径转换信息
    #         data = '\n'.join(data)
    #     elif not isinstance(data, str):  # 单纯cmd命令
    #         print('data 数据错误,  应为 list 或 str')
    #         return
    #     self.__write_file(file_path, data)

    def __read_file(self, file_path):
        with open(file_path,  'r', encoding='utf-8') as f:
            data = f.read()
        data = data.split('\n')
        return data

    # # 弃用方法
    # def __write_file(self, file_path, data):
    #     with open(file_path, 'w', encoding='utf-8') as f:
    #         f.write(data)

    def __get_cmd_data(self, data):
        cmd_data = None
        for i in data:
            i: str
            if i.strip().startswith('pyinstaller ') or i.strip().startswith('PyInstaller ') or 'pyinstaller ' in i or 'PyInstaller ' in i or 'pyinstaller.exe' in i:  # 这里有一个特性, 只会存在一个pyinstaller命令, 且只读取第一个命令
                cmd_data = i
                break
        return cmd_data

    def __sort_cmd_data(self, cmd_data: str):
        try:
            self.__struct_data.clear()
            if not cmd_data:
                print(f'没有找到pyinstaller命令, 数据为空\n{cmd_data}')
                return None
            if 'pyinstaller.exe"' in cmd_data:
                self.__implement_path_from_file = (cmd_data.split('pyinstaller.exe"')[0] + 'pyinstaller.exe"').strip('"')
                cmd_data: list = cmd_data.split('pyinstaller.exe"')[-1].split(' ')
            elif 'pyinstaller.exe ' in cmd_data:
                self.__implement_path_from_file = cmd_data.split('pyinstaller.exe ')[0] + 'pyinstaller.exe'
                cmd_data: list = cmd_data.split('pyinstaller.exe ')[-1].split(' ')
            elif "pyinstaller.exe' " in cmd_data:
                self.__implement_path_from_file = cmd_data.split("pyinstaller.exe' ")[0] + "pyinstaller.exe'".strip("'")
                cmd_data: list = cmd_data.split('pyinstaller.exe ')[-1].split(' ')
            elif 'pyinstaller ' in cmd_data:
                self.__implement_path_from_file = self.__take_next_parameter(cmd_data.split('pyinstaller ')[0].split(' ')).strip('"')
                cmd_data: list = cmd_data.split('pyinstaller ')[-1].split(' ')
            elif 'PyInstaller ' in cmd_data:
                self.__implement_path_from_file = self.__take_next_parameter(cmd_data.split('PyInstaller ')[0].split(' ')).strip('"')
                cmd_data: list = cmd_data.split('PyInstaller ')[-1].split(' ')
            else:
                print(f'没有找到pyinstaller命令\n{cmd_data}')
                return None
            # 此处的 self.__implement_path_from_file 是无引号的纯路径
            list_switch_struct = ['--strip', '-s', '--noupx', '--disable-windowed-traceback', '--uac-admin',
                                  '--uac-uiaccess', '--argv-emulation', '--bootloader-ignore-signals', '--noconfirm', '-y',
                                  '--clean']
            dict_state_struct_with_param = {
                '--debug': ['all', 'imports', 'bootloader', 'noarchive'],
                '-d': [],
                '--python-option': [],
                '--hide-console': [],
                '--target-architecture': [],
                '--target-arch': [],
                '--log-level': []
            }
            dict_state_struct_without_param = {
                '--onefile': ['--onefile', '--onedir'],
                '--console': ['--console', '--nowindowed', '--windowed', '--noconsole', '-c', '-w']
            }
            list_single_struct = ['--specpath', '--contents-directory', '--version-file', '--manifest', '-m', '--osx-bundle-identifier',
                                  '--codesign-identity', '--osx-entitlements-file', '--runtime-tmpdir', '--workpath', '--upx-dir', '--splash', '--name', '--distpath']
            list_multi_struct = ['--paths', '-p', '--hidden-import', '--hiddenimport', '--collect-submodules', '--collect-data', '--collect-datas', '--collect-binaries', '--collect-all', '--copy-metadata', '--recursive-copy-metadata',
                                 '--additional-hooks-dir', '--runtime-hook', '--exclude-module', '--upx-exclude', '--icon', '-i', '--resource', '-r', '--add-data', '--add-binary']  # 包含两类 MultiInfoStruct, RelPathStruct 都是属于可以重复调用的

            while len(cmd_data) > 0:
                cmd_word: str = cmd_data.pop(0)

                # RelPathStruct | MultiInfoStruct | SingleInfoStruct
                if '=' in cmd_word:
                    if '"' in cmd_word and not cmd_word.endswith('"'):
                        while True:
                            cmd_word += cmd_data.pop(0)
                            if cmd_word.endswith('"'):
                                break
                    option, data = cmd_word.split('=')
                    struct: SingleInfoStruct | RelPathStruct | MultiInfoStruct | None = self.__struct_data.find_struct_from_option(option)
                    if struct is None or not isinstance(struct, (SingleInfoStruct, RelPathStruct, MultiInfoStruct)):
                        print(f'[SingleInfoStruct | RelPathStruct | MultiInfoStruct] 未找到关键字 {repr(cmd_word)}')
                        continue
                    if option in list_multi_struct:
                        # RelPathStruct | MultiInfoStruct
                        struct: RelPathStruct | MultiInfoStruct
                        struct.append_args(data)
                    else:
                        # SingleInfoStruct
                        struct: SingleInfoStruct
                        struct.set_args(data)
                # StateStruct 带参数
                elif cmd_word in dict_state_struct_with_param:
                    struct: StateStruct | None = self.__struct_data.find_struct_from_option(cmd_word)
                    if struct is None or not isinstance(struct, StateStruct):
                        print(f'[StateStruct-带参数] 未找到关键字 {repr(cmd_word)}')
                        continue
                    else:
                        data = self.__take_next_parameter(cmd_data)
                        struct.set_state(data)
                # StateStruct 不带参数
                elif cmd_word in dict_state_struct_without_param['--onefile'] or cmd_word in dict_state_struct_without_param['--console']:
                    if cmd_word in dict_state_struct_without_param['--onefile']:
                        key = '--onefile'
                    else:
                        key = '--console'
                    struct: StateStruct | None = self.__struct_data.find_struct_from_option(key)
                    if struct is None or not isinstance(struct, StateStruct):
                        print(f'[StateStruct-不带参数] 未找到关键字 {repr(cmd_word)}')
                        continue
                    else:
                        struct: StateStruct
                        struct.set_state(cmd_word)
                # SwitchStruct
                elif cmd_word in list_switch_struct:
                    struct: SwitchStruct | None = self.__struct_data.find_struct_from_option(cmd_word)
                    if struct is None or not isinstance(struct, SwitchStruct):
                        print(f'[SwitchStruct] 未找到关键字 {repr(cmd_word)}')
                        continue
                    else:
                        struct.set_on()
                else:
                    # 针对 执行文件
                    if cmd_word.replace('"', '').endswith(('.py', 'pyw', 'pyd', '.spec')):
                        struct: SingleInfoStruct | None = self.__struct_data.find_struct_from_option('')
                        if struct is None or not isinstance(struct, SingleInfoStruct):
                            print(f'未找到 打包执行文件')
                            continue
                        else:
                            struct.set_args(cmd_word)
                    # 以下针对非标准写法, 比如需要写 "=", 但是没有写的情况
                    elif cmd_word in dict_state_struct_with_param:
                        struct: StateStruct | None = self.__struct_data.find_struct_from_option(cmd_word)
                        if struct is None or not isinstance(struct, StateStruct):
                            print(f'[StateStruct][无=] 未找到关键字 {repr(cmd_word)}')
                            continue
                        data = self.__take_next_parameter(cmd_data)
                        struct.set_state(data)
                    elif cmd_word in list_single_struct:
                        struct: SingleInfoStruct | None = self.__struct_data.find_struct_from_option(cmd_word)
                        if struct is None or not isinstance(struct, SingleInfoStruct):
                            print(f'[SingleInfoStruct][无=] 未找到关键字 {repr(cmd_word)}')
                            continue
                        data = self.__take_next_parameter(cmd_data)
                        struct.set_args(data)
                    elif cmd_word in list_multi_struct:
                        struct: RelPathStruct | MultiInfoStruct | None = self.__struct_data.find_struct_from_option(cmd_word)
                        if struct is None or not isinstance(struct, (RelPathStruct, MultiInfoStruct)):
                            print(f'[RelPathStruct | MultiInfoStruct][无=] 未找到关键字 {repr(cmd_word)}')
                            continue
                        data = self.__take_next_parameter(cmd_data)
                        struct.append_args(data)
                    else:
                        print(f'未找到关键字 {repr(cmd_word)}')
                        continue
            return 'ok'
        except Exception as e:
            print(f'发生错误: {format_exc()}')
            return 'hasError'

    def __take_next_parameter(self, cmd_data: list):
        if len(cmd_data) == 0:
            return None
        param: str = cmd_data.pop(0)
        if param.startswith('"') or '"' in param:
            param_list = [param]
            while cmd_data and not param_list[-1].endswith('"'):
                temp_param = cmd_data.pop(0)
                param_list.append(temp_param)
            param = ' '.join(param_list)
        return param
