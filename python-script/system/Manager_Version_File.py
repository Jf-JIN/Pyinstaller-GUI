
from const.Const_Version_File import *
from const.Const_Parameter import *
from tools.type_convert import *
import os

_log = Log.UI


class _FixedFileInfoStruct:
    def __init__(self):
        self.__filevers: list = [0, 0, 0, 0]
        self.__prodvers: list = [0, 0, 0, 0]
        self.__mask: int = 0x3f
        self.__flags: int = VersionEnum.FileFlags.VS_FF_UNKNOWN
        self.__os: int = 0x4
        self.__file_type: int = 0x1
        self.__sub_type: int = 0x0

    def set_filevers(self, filevers: list | str) -> None:
        res = self.__handle_version_data(filevers)
        if res is not None:
            self.__filevers = res

    def set_prodvers(self, prodvers: list) -> None:
        res = self.__handle_version_data(prodvers)
        if res is not None:
            self.__prodvers = res

    def __handle_version_data(self, version_data: list | str):
        if isinstance(version_data, str):
            temp = []
            for num in version_data.lstrip('(').lstrip('[').rstrip(')').rstrip(']').split(','):
                num = num.strip()
                if not num.isdigit():
                    continue
                temp.append(int(num))
            version_data = temp
        elif not isinstance(version_data, (list, tuple)):
            return None
        lengeth = len(version_data)
        temp_res = [0, 0, 0, 0]
        for idx, v in enumerate(version_data):
            if idx >= lengeth:
                break
            temp_res[idx] = v
        return temp_res

    def set_flags(self, flags: int) -> None:
        # if flags not in VersionEnum.FileFlags:
        #     return
        if not isinstance(flags, int):
            try:
                flags = int(flags, 16)
            except:
                return
        self.__flags = flags

    def set_os(self, os_list: list):
        if not isinstance(os_list, list):
            os_list = [os_list]
        value = 0
        for os_item in os_list:
            if not isinstance(os_item, int):
                try:
                    os_item = int(os_item, 16)
                except ValueError:
                    continue
            value = value | os_item
        self.__os = value

    def set_file_type(self, file_type) -> None:
        if file_type not in VersionEnum.FileType:
            return
        self.__file_type = file_type

    def set_subtype(self, subtype) -> None:
        if subtype not in VersionEnum.FileSubtype:
            return
        self.__sub_type = subtype

    @property
    def filevers(self) -> tuple:
        return tuple(self.__filevers)

    @property
    def filevers_str(self) -> str:
        major_version = self.__filevers[0]
        minor_version = self.__filevers[1]
        revision_version = self.__filevers[2]
        build_version = self.__filevers[3]
        return f"{major_version}.{minor_version}.{revision_version}.{build_version}"

    @property
    def filevers_format_txt(self) -> str:
        return f"StringStruct(u'FileVersion', u'{self.filevers_str}')"

    @property
    def prodvers(self) -> tuple:
        return tuple(self.__prodvers)

    @property
    def prodvers_str(self) -> str:
        major_version: int = self.__prodvers[0]
        minor_version: int = self.__prodvers[1]
        revision_version: int = self.__prodvers[2]
        build_version: int = self.__prodvers[3]
        return f"{major_version}.{minor_version}.{revision_version}.{build_version}"

    @property
    def prodvers_format_txt(self) -> str:
        return f"StringStruct(u'ProductVersion', u'{self.prodvers_str}')"

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def os(self) -> int:
        return self.__os

    @property
    def file_type(self) -> int:
        return self.__file_type

    @property
    def mask(self) -> int:
        return self.__mask

    @property
    def sub_type(self) -> int:
        return self.__sub_type


class _StringStructStruct:
    def __init__(self, indent: int = 4, start_level: int = 4):
        self.__key = ''
        self.__value = ''
        self.__indent = indent
        self.__start_level = start_level
        self.__start_blank = ' ' * self.__indent * self.__start_level

    def set_value(self, key: str, value: str):
        self.__key = key
        self.__value = value

    @property
    def key(self):
        return self.__key

    @property
    def value(self):
        return self.__value

    @property
    def output_text(self):
        return f"{self.__start_blank}StringStruct(u'{self.__key}', u'{self.__value}')"


class _VarStructStruct:
    def __init__(self, indent: int = 4, start_level: int = 3):
        self.__key = ''
        self.__value = ''
        self.__indent = indent
        self.__start_level = start_level
        self.__start_blank = ' ' * self.__indent * self.__start_level

    def set_value(self, key: str, value: str | list):
        self.__key = key
        self.__value = []
        if isinstance(value, str):
            if not value.startswith('['):
                return
            temp = []
            value = value.strip('[').strip(']')
            flag_lang = False
            for item in value.split(','):
                item = item.strip()
                if '"' in item or "'" in item:
                    continue
                try:
                    item = int(item, 16)
                except:
                    continue
                if item in VersionEnum.LangID and not flag_lang:
                    flag_lang = True
                elif item in VersionEnum.CharsetID and flag_lang:
                    flag_lang = False
                else:
                    break
                if item is not None:
                    temp.append(item)
            self.__value = temp
        elif isinstance(value, (list, tuple)):
            temp = []
            flag_lang = False
            for item in value:
                if not isinstance(item, int):
                    try:
                        item = int(item, 16)
                    except:
                        continue
                if item in VersionEnum.LangID and not flag_lang:
                    flag_lang = True
                elif item in VersionEnum.CharsetID and flag_lang:
                    flag_lang = False
                else:
                    break
                temp.append(item)
            self.__value = temp

    @property
    def key(self):
        return self.__key

    @property
    def value(self):
        return self.__value

    @property
    def output_text(self):
        params = []
        temp = []
        flag_lang = False
        for item in self.__value:
            if item in VersionEnum.LangID and not flag_lang:
                temp.append(f'0x{item:04X}')
                flag_lang = True
            if item in VersionEnum.CharsetID and flag_lang:
                temp.append(f'0x{item:04X}')
                params.append(', '.join(temp))
                temp = []
                flag_lang = False
        if not params:
            return ''
        params = f",\n{self.__start_blank+' ' * self.__indent}".join(params)
        return f"{self.__start_blank}VarStruct('{self.__key}', [\n{self.__start_blank+' ' * self.__indent}{params}\n{self.__start_blank}])"


class _StringTableStruct:
    def __init__(self, indent: int = 4, start_level: int = 3):
        self.__StringStruct_dict = {}
        self.__table_key = ''
        self.__indent = indent
        self.__start_level = start_level
        self.__start_blank = ' ' * self.__indent * self.__start_level

    def set_table_key(self, lang_id: int, charset_id: int):
        language = f'0x{lang_id:04X}'
        charset_id = f'0x{charset_id:04X}'
        self.__table_key = f'{language[2:]}{charset_id[2:]}'

    def set_StringStruct(self, key, value):
        struct = _StringStructStruct()
        struct.set_value(key, value)
        self.__StringStruct_dict[key] = struct

    @property
    def table_key(self):
        return self.__table_key

    @property
    def StringStruct_dict(self):
        return self.__StringStruct_dict

    @property
    def output_text(self):
        string_struct_list_text = ',\n'.join([struct.output_text for struct in self.__StringStruct_dict.values()])
        return f"{self.__start_blank}StringTable(u'{self.__table_key}', [\n{string_struct_list_text}\n{self.__start_blank}])"


class VersionStruct:
    def __init__(self):
        self.__ffi: _FixedFileInfoStruct = _FixedFileInfoStruct()
        self.__StringTable_dict = {}
        self.__varStruct = _VarStructStruct()

    @property
    def ffi(self) -> _FixedFileInfoStruct:
        return self.__ffi

    @property
    def varStruct(self) -> _VarStructStruct:
        return self.__varStruct

    @property
    def StringTable_dict(self) -> dict:
        return self.__StringTable_dict

    def sort_string_table(self):
        temp = {}
        for idx, (key, value) in enumerate(self.__StringTable_dict.items()):
            temp[idx] = value
        self.__StringTable_dict = temp

    def set_string_table(self, key="u'040904B0'") -> _StringTableStruct:
        index = len(self.__StringTable_dict)
        struct = _StringTableStruct()
        key = key.strip("u'").strip("'")
        lang = int(key[:4], 16)
        charset = int(key[4:], 16)
        struct.set_table_key(lang, charset)
        self.__StringTable_dict[index] = struct
        return struct

    def set_var_struct(self, key, value):
        self.__varStruct.set_value(key, value)

    def get_file_data(self):
        StringFileInfo_text = ',\n'.join([struct.output_text for struct in self.__StringTable_dict.values()])
        text = f"""\
VSVersionInfo(
    ffi=FixedFileInfo(
        filevers={self.__ffi.filevers},
        prodvers={self.__ffi.prodvers},
        mask=0x{self.__ffi.mask:08X},
        flags=0x{self.__ffi.flags:08X},
        OS=0x{self.__ffi.os:08X},
        fileType=0x{self.__ffi.file_type:08X},
        subtype=0x{self.__ffi.sub_type:08X},
    ),
    kids=[
        StringFileInfo([\n{StringFileInfo_text}
        ]),
        VarFileInfo([\n{self.__varStruct.output_text}
        ])
    ]
)"""
        return text


class VersionFileLoader:
    def __init__(self):
        self.__version_struct = VersionStruct()
        self.__ffi_name_func_dict = {
            'filevers': self.__version_struct.ffi.set_filevers,
            'prodvers': self.__version_struct.ffi.set_prodvers,
            'flags': self.__version_struct.ffi.set_flags,
            'OS': self.__version_struct.ffi.set_os,
            'fileType': self.__version_struct.ffi.set_file_type,
            'subtype': self.__version_struct.ffi.set_subtype,
        }
        self.__ffi_func_list = list(self.__ffi_name_func_dict.values())

    @property
    def version_struct(self) -> VersionStruct:
        return self.__version_struct

    def __set_fixed_file_info(self, data_list: list):
        for index, value in enumerate(data_list):
            value: str
            if '=' in value:
                res = value.split('=')
                if len(res) != 2:
                    continue
                key, value = res
                if key in self.__ffi_name_func_dict:
                    self.__ffi_name_func_dict[key](value)
                else:
                    continue
            else:
                self.__ffi_func_list[index](value)

    def __set_string_table(self, data_list: list):
        key = data_list[0]
        value = data_list[1]
        struct: _StringTableStruct = self.__version_struct.set_string_table(key)
        params_list = split_parameters(value.lstrip('[').rstrip(']'))
        for param in params_list:
            param: str
            param = param.lstrip('StringStruct(').rstrip(')')
            args_list = param.split(',')
            string_struct_key = args_list[0].strip().strip("u'").strip("'")
            string_struct_value = args_list[1].strip().strip("u'").strip("'")
            struct.set_StringStruct(string_struct_key, string_struct_value)

    def __set_var_struct(self, data_list: list):
        key = data_list[0].strip('"').strip("'")
        value = data_list[1].strip('"').strip("'")
        self.__version_struct.set_var_struct(key, value)

    def load_version_file(self, version_file_path):
        if not os.path.exists(version_file_path):
            return
        try:
            with open(version_file_path, 'r', encoding='utf-8') as f:
                line = f.readline()
                temp = []
                while line:
                    temp.append(line.split('#')[0].strip())
                    line = f.readline()
            text = ''.join(temp)
            if 'VSVersionInfo(' not in text:
                return
            main_struct = text.split('VSVersionInfo(')[1].strip(')')
            if not main_struct.startswith('FixedFileInfo(') and not main_struct.startswith('ffi'):
                return
            if 'kids=' not in main_struct:
                fixed_file_info, kids = split_parameters(main_struct)
                fixed_file_info = fixed_file_info.rstrip(')')
                kids = kids.lstrip('[')
            else:
                fixed_file_info, kids = main_struct.split('),kids=[')
            fixed_file_info = fixed_file_info.split('FixedFileInfo(')[-1].rstrip(',')
            kids = kids.rstrip(']')
            params_fixed_file_info = split_parameters(fixed_file_info)
            self.__set_fixed_file_info(params_fixed_file_info)
            params_kids = split_parameters(kids)
            string_file_info = None
            for param in params_kids:
                param: str
                if param.startswith('StringFileInfo'):
                    string_file_info = param.split('StringFileInfo([')[1].rstrip('])')  # 目前仅支持一个StringTable
                    string_file_info_list = split_parameters(string_file_info)
                    for item in string_file_info_list:
                        item: str
                        string_table = item.split('StringTable(')[1].rstrip(')')
                        params_string_table = split_parameters(string_table)
                        self.__set_string_table(params_string_table)
                elif param.startswith('VarFileInfo'):
                    var_file_info = param.split('VarFileInfo([')[1].rstrip(')').rstrip(']')
                    var_file_info_list = split_parameters(var_file_info)
                    for item in var_file_info_list:
                        item: str
                        if not item.startswith('VarStruct'):
                            continue
                        var_struct = item.split('VarStruct(')[1].rstrip(')')
                        params_var_table = split_parameters(var_struct)
                        self.__set_var_struct(params_var_table)
        except:
            _log.exception(f'Failed to parse version info from file {version_file_path}')
