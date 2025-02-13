
if 1:
    import os
    import sys
    parent_folder = os.path.dirname(__file__)
    parent_folder = os.path.dirname(parent_folder)
    sys.path.append(parent_folder)

import os
import sys
import platform
from DToolslib.Enum_Static import StaticEnum
from DToolslib.Logger import *

from system.Manager_Setting import SettingManager
from system.Manager_Language import LanguageManager
from const.Const_language_chinese import LANGUAGE_CHINESE
from const.Const_language_english import LANGUAGE_ENGLISH


os.chdir(os.path.dirname(os.path.dirname(__file__)))
if len(sys.argv) > 1:
    APP_WORKSPACE_PATH = sys.argv[1]
else:
    APP_WORKSPACE_PATH = os.getcwd()


def detemine_workspace_path():
    os.chdir(os.path.dirname(os.path.dirname(__file__)))
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return os.getcwd()


def detect_system() -> str:
    system_tpye = platform.system()
    if system_tpye == OsType.WINDOWS:
        return OsType.WINDOWS
    elif system_tpye == OsType.LINUX:
        return OsType.LINUX
    elif system_tpye == OsType.MACOS:
        return OsType.MACOS
    else:
        return ''


class OsType(StaticEnum):
    WINDOWS = 'Windows'
    LINUX = 'Linux'
    MACOS = 'Darwin'


class EnumConst(StaticEnum):
    DEFAULT_INSTALLER_COMMANDLINE = '--onefile --console --clean'
    THREAD_LIST_ALL = set()


# 默认设置 值的格式为列表 [类型/元组, 默认值]
DEFAULT_SETTING = {
    'language': [str, 'default'],
    'multi_win': [bool, 'True'],
    'win_mode': [str, 'simple'],
    'last_command': [str, ''],
    'tb_console_font_size': [int, 18],
    'tb_command_line_font_size': [int, 18],
    'auto_open_printed_command_line_folder': [bool, False],
    'auto_open_printed_command_line_file': [bool, True]

}


class SettingConst(StaticEnum):
    # 默认设置 值的格式为列表 [类型/元组, 默认值]
    DEFAULT_SETTING = {
        'language': [str, 'default'],
        'multi_win': [bool, 'True'],
        'win_mode': [str, 'simple'],
        'last_command': [str, ''],
        'tb_console_font_size': [int, 18],
        'tb_command_line_font_size': [int, 18],
        'auto_open_printed_command_line_folder': [bool, False],
        'auto_open_printed_command_line_file': [bool, True]
    }


_files_num = 10
_level = 'DEBUG'


class Log(StaticEnum):
    CRITICAL = Logger('CRITICAL', APP_WORKSPACE_PATH, count_limit=_files_num, log_level=_level)
    DataManager = Logger('DataManager', APP_WORKSPACE_PATH, count_limit=_files_num, log_level=_level)
    StyleManager = Logger('StyleManager', APP_WORKSPACE_PATH, count_limit=_files_num, log_level=_level)
    LanguageManager = Logger('LanguageManager', APP_WORKSPACE_PATH, count_limit=_files_num, log_level=_level)
    SettingManager = Logger('SettingManager', APP_WORKSPACE_PATH, count_limit=_files_num, log_level=_level)


class Pyinstaller(StaticEnum):

    class CmdArgsCategory:
        LIST_SWITCH = [
            '--strip', '-s', '--noupx', '--disable-windowed-traceback', '--uac-admin', '--uac-uiaccess',
            '--argv-emulation', '--bootloader-ignore-signals', '--noconfirm', '-y', '--clean'
        ]
        DICT_STATE_WITH_PARAMS = {
            '--debug': ['all', 'imports', 'bootloader', 'noarchive'],
            '-d': [],
            '--python-option': [],
            '--hide-console': [],
            '--target-architecture': [],
            '--target-arch': [],
            '--log-level': []
        }
        DICT_STATE_WITHOUT_PARAMS = {
            '--onefile': ['--onefile', '--onedir'],
            '--console': ['--console', '--nowindowed', '--windowed', '--noconsole', '-c', '-w']
        }
        LIST_SINGLE = [
            '--specpath', '--contents-directory', '--version-file', '--manifest', '-m', '--osx-bundle-identifier', '--codesign-identity',
            '--osx-entitlements-file', '--runtime-tmpdir', '--workpath', '--upx-dir', '--splash', '--name', '--distpath'
        ]
        LIST_MULTI = [
            '--paths', '-p', '--hidden-import', '--hiddenimport', '--collect-submodules', '--collect-data', '--collect-datas',
            '--collect-binaries', '--collect-all', '--copy-metadata', '--recursive-copy-metadata', '--additional-hooks-dir', '--runtime-hook',
            '--exclude-module', '--upx-exclude', '--icon', '-i', '--resource', '-r', '--add-data', '--add-binary'
        ]  # 包含两类 MultiInfoStruct, RelPathStruct 都是属于可以重复调用的


class App(EnumConst):
    WORKSPACE_PATH: str = detemine_workspace_path()
    OS: str = detect_system()
    DEFAULT_INSTALLER_COMMANDLINE: str = '--onefile --console --clean'
    DEFAULT_SETTING = {
        'language': [str, 'default'],
        'multi_win': [bool, True],
        'win_mode': [str, 'simple'],
        'last_command': [str, ''],
        'tb_console_font_size': [int, 18],
        'tb_command_line_font_size': [int, 18],
        'auto_open_printed_command_line_folder': [bool, False],
        'auto_open_printed_command_line_file': [bool, True]
    }


SettingManager(App.WORKSPACE_PATH, App.DEFAULT_SETTING, isEncrypted=True)
LanguageManager(LANGUAGE_CHINESE, LANGUAGE_ENGLISH, App.WORKSPACE_PATH, SettingManager.get('language'))
