

import os
import sys
import platform
from DToolslib.Enum_Static import StaticEnum
from DToolslib.Logger import *


class OsType(StaticEnum):
    WINDOWS = 'Windows'
    LINUX = 'Linux'
    MACOS = 'Darwin'


def detemine_workspace_path():
    # os.chdir(os.path.dirname(os.path.dirname(__file__)))
    if len(sys.argv) > 1:
        pth = sys.argv[1]
        if os.path.isfile(pth):
            pth = os.path.dirname(pth)
        return pth
    else:
        return os.getcwd()


def detemine_app_folder_path():
    if len(sys.argv) > 1:
        pth = sys.argv[0]
        if os.path.isfile(pth):
            pth = os.path.dirname(pth)
        return pth
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


WORKSPACE_PATH = detemine_workspace_path()


class App(StaticEnum):

    class SettingEnum(StaticEnum):
        # 默认设置 值的格式为列表 [类型/元组, 默认值]
        DEFAULT_SETTING = {
            'pyinstaller_command': [str, ''],
            'language': [str, 'default'],
            'multi_win': [bool, True],
            'display_tooltip': [bool, True],
            'last_command': [str, ''],
            'tb_console_font_size': [int, 18],
            'tb_command_line_font_size': [int, 18],
            'auto_open_printed_command_line_folder': [bool, False],
            'auto_open_printed_command_line_file': [bool, True],
            'synchron_vers': [bool, True],
            'auto_add_version_index': [int, 0],
            'lock_output_folder': [bool, False],
            'lock_output_file_name': [bool, False],
            'synchron_env_from_file': [bool, True],
            'load_env_config': [bool, True],
            'use_method': [str, 'pyinstaller'],
            'delete_build_files': [bool, True],
            'delete_spec_file': [bool, True],
            'auto_handle_splash_import': [bool, True],
            'style_mode': [str, 'dark'],
            'style_sheet': [dict, {}]
        }

    class Pyinstaller(StaticEnum):
        LIST_SWITCH = [
            '--strip', '-s', '--noupx', '--disable-windowed-traceback', '--uac-admin', '--uac-uiaccess',
            '--argv-emulation', '--bootloader-ignore-signals', '--noconfirm', '-y', '--clean'
        ]
        DICT_STATE_WITH_PARAMS = {
            '--hide-console': ['hide-early', 'minimize-late', 'hide-late', 'minimize-early'],
            '--debug': ['all', 'imports', 'bootloader', 'noarchive'],
            '-d': ['all', 'imports', 'bootloader', 'noarchive'],
            '--python-option': ['v', 'u', 'W', 'X', 'hash_seed='],
            '--target-architecture': ['x86_64', 'arm64', 'universal2'],
            '--target-arch': ['x86_64', 'arm64', 'universal2'],
            '--log-level': ['TRACE', 'DEBUG', 'INFO', 'WARN',
                            'DEPRECATION', 'ERROR', 'FATAL'],
            '--optimize': ['0', '1', '2']
        }
        DICT_STATE_WITHOUT_PARAMS = {
            '--onefile': ['--onefile', '--onedir', '-F', '-D'],
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

    APP_FOLDER_PATH: str = detemine_app_folder_path()
    OS: str = detect_system()
    DEFAULT_INSTALLER_COMMANDLINE: str = '--onefile --console --clean'
    SENTENCE_LIMIT = 60
    STYLE_UPDATE_INTERVAL = 0.01


class Log(StaticEnum):
    Log_level = LogLevel.INFO
    logging_output = Logger('logging_output', App.APP_FOLDER_PATH, log_level=Log_level)
    CRITICAL = Logger('CRITICAL', App.APP_FOLDER_PATH, log_level=Log_level)
    DataManager = Logger('DataManager', App.APP_FOLDER_PATH, log_level=Log_level)
    StyleManager = Logger('StyleManager', App.APP_FOLDER_PATH, log_level=Log_level)
    LanguageManager = Logger('LanguageManager', App.APP_FOLDER_PATH, log_level=Log_level)
    SettingManager = Logger('SettingManager', App.APP_FOLDER_PATH, log_level=Log_level)
    ExecutorInfoManager = Logger('ExecutorInfoManager', App.APP_FOLDER_PATH, log_level=Log_level)
    UI = Logger('UI', App.APP_FOLDER_PATH, log_level=Log_level,  highlight_type=LogHighlightType.HTML)
    Threads = Logger('Threads', App.APP_FOLDER_PATH, log_level=Log_level)
    Tools = Logger('Tools', App.APP_FOLDER_PATH, log_level=Log_level)
    LogGroup = LoggerGroup(App.APP_FOLDER_PATH, exclude_logs=[CRITICAL], limit_files_count=5, enableFileOutput=False)


for logger in [Log.logging_output, Log.CRITICAL, Log.DataManager, Log.StyleManager, Log.LanguageManager, Log.SettingManager, Log.ExecutorInfoManager, Log.UI, Log.Threads]:
    logger.set_file_count_limit(5)
    logger.set_exclude_funcs(['get_item', 'set_config', 'setConfig',])
    logger.set_exclude_classes([])
    logger.set_highlight_type(LogHighlightType.HTML)
    logger.setEnableFileOutput(False)
    logger.setEnableConsoleOutput(False)

Log.CRITICAL.setEnableFileOutput(True)
Log.logging_output.set_listen_logging('', Log.Log_level)
