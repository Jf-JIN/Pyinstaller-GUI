

from system.Struc_Pyinstaller import *
from traceback import format_exc


class Struct_IO(object):
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
        if hasError == 'hasError':
            return 'hasError'
        if self.__struct_data.get_command_line(self.exe_path) == '' or self.__struct_data.get_command_line(self.exe_path) == None:
            return None
        return self.__struct_data

    def write_file(self, file_path, data: list | str):
        if isinstance(data, list):  # 涵盖路径转换信息
            data = '\n'.join(data)
        elif not isinstance(data, str):  # 单纯cmd命令
            print('data 数据错误,  应为 list 或 str')
            return
        self.__write_file(file_path, data)

    def __read_file(self, file_path):
        with open(file_path,  'r', encoding='utf-8') as f:
            data = f.read()
        data = data.split('\n')
        return data

    def __write_file(self, file_path, data):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(data)

    def __get_cmd_data(self, data):
        cmd_data = None
        for i in data:
            i: str
            if i.strip().startswith('pyinstaller ') or 'pyinstaller ' in i or 'pyinstaller.exe' in i:  # 这里有一个特性, 只会存在一个pyinstaller命令, 且只读取第一个命令
                cmd_data = i
                break
        return cmd_data

    def __sort_cmd_data(self, cmd_data):
        try:
            if 'pyinstaller.exe"' in cmd_data:
                self.exe_path = cmd_data.split('pyinstaller.exe"')[0] + 'pyinstaller.exe'
                cmd_data: list = cmd_data.split('pyinstaller.exe"')[-1].split(' ')
            elif 'pyinstaller.exe ' in cmd_data:
                self.exe_path = cmd_data.split('pyinstaller.exe ')[0] + 'pyinstaller.exe'
                cmd_data: list = cmd_data.split('pyinstaller.exe ')[-1].split(' ')
            elif "pyinstaller.exe' " in cmd_data:
                self.exe_path = cmd_data.split("pyinstaller.exe' ")[0] + 'pyinstaller.exe'
                cmd_data: list = cmd_data.split('pyinstaller.exe ')[-1].split(' ')
            elif 'pyinstaller ' in cmd_data:
                self.exe_path = cmd_data.split('pyinstaller ')[0].split()[0]
                cmd_data: list = cmd_data.split('pyinstaller ')[-1].split(' ')
            else:
                print(f'没有找到pyinstaller命令\n{cmd_data}')
                return
            list_switch_struct = ['--strip', '--noupx', '--disable-windowed-traceback', '--uac-admin', '--uac-uiaccess', '--argv-emulation', '--bootloader-ignore-signals', '--noconfirm', '--clean']
            list_state_struct_with_param = ['--debug', '--python_option', '--hide-console', '--target-architecture', '--log-level']
            dict_state_struct_without_param = {
                '--onefile': ['--onefile', '--onedir'],
                '--console': ['--console', '--nowindowed', '--windowed', '--noconsole']
            }
            list_single_struct = ['--specpath', '--contents-directory', '--version-file', '-m', '--osx-bundle-identifier',
                                  '--codesign-identity', '--osx-entitlements-file', '--runtime-tmpdir', '--workpath', '--upx-dir', '--splash', '--name', '--distpath']
            list_multi_struct = ['--paths', '--hidden-import', '--collect-submodules', '--collect-data', '--collect-binaries', '--collect-all', '--copy-metadata', '--recursive-copy-metadata',
                                 '--additional-hooks-dir', '--runtime-hook', '--exclude-module', '--upx-exclude', '--icon', '-r', '--add-data', '--add-binary']  # 包含两类 MultiInfoStruct, RelPathStruct 都是属于可以重复调用的
            self.__struct_data.clear()
            while len(cmd_data) > 0:
                cmd_word: str = cmd_data.pop(0)
                if '=' in cmd_word:
                    # RelPathStruct | MultiInfoStruct | SingleInfoStruct
                    option, data = cmd_word.split('=')
                    struct: SingleInfoStruct | RelPathStruct | MultiInfoStruct | None = self.__struct_data.find_struct_from_option(option)
                    if struct is None:
                        print(f'未找到关键字 {cmd_word}')
                        continue
                    if option in list_multi_struct:
                        # RelPathStruct | MultiInfoStruct
                        struct: RelPathStruct | MultiInfoStruct
                        struct.append_args(data)
                    else:
                        # SingleInfoStruct
                        struct: SingleInfoStruct
                        struct.set_args(data)
                elif cmd_word in list_state_struct_with_param:
                    # StateStruct 带参数
                    struct: StateStruct | None = self.__struct_data.find_struct_from_option(cmd_word)
                    if struct is None:
                        print(f'未找到关键字 {cmd_word}')
                        continue
                    else:
                        data = cmd_data.pop(0)
                        struct.set_state(data)
                elif cmd_word in dict_state_struct_without_param['--onefile'] or cmd_word in dict_state_struct_without_param['--console']:
                    # StateStruct 不带参数
                    if cmd_word in dict_state_struct_without_param['--onefile']:
                        key = '--onefile'
                    else:
                        key = '--console'
                    struct: StateStruct | None = self.__struct_data.find_struct_from_option(key)
                    if struct is None:
                        print(f'未找到关键字 {cmd_word}')
                        continue
                    else:
                        struct: StateStruct
                        struct.set_state(cmd_word)
                elif cmd_word in list_switch_struct:
                    # SwitchStruct
                    struct: SwitchStruct | None = self.__struct_data.find_struct_from_option(cmd_word)
                    if struct is None:
                        print(f'未找到关键字 {cmd_word}')
                        continue
                    else:
                        struct.set_on()
                else:
                    if cmd_word.replace('"', '').endswith(('.py', 'pyw', 'pyd', '.spec')):
                        struct: SingleInfoStruct | None = self.__struct_data.find_struct_from_option('')
                        if struct is None:
                            print(f'未找到 打包执行文件')
                            continue
                        else:
                            struct.set_args(cmd_word)
                    elif cmd_word in list_state_struct_with_param:
                        struct: StateStruct | None = self.__struct_data.find_struct_from_option(cmd_word)
                        if struct is None:
                            print(f'未找到关键字 {cmd_word}')
                            continue
                        data = cmd_data.pop(0)
                        struct.set_state(data)
                    elif cmd_word in list_single_struct:
                        struct: SingleInfoStruct | None = self.__struct_data.find_struct_from_option(cmd_word)
                        if struct is None:
                            print(f'未找到关键字 {cmd_word}')
                            continue
                        data = cmd_data.pop(0)
                        struct.set_args(data)
                    elif cmd_word in list_multi_struct:
                        struct: RelPathStruct | MultiInfoStruct | None = self.__struct_data.find_struct_from_option(cmd_word)
                        if struct is None:
                            print(f'未找到关键字 {cmd_word}')
                            continue
                        data = cmd_data.pop(0)
                        struct.append_args(data)
                    else:
                        print(f'未找到关键字 {cmd_word}')
                        continue
        except Exception as e:
            print(f'发生错误: {format_exc()}')
            return 'hasError'
