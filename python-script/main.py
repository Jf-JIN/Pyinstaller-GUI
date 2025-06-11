

import sys
import traceback
import socket
import pygetwindow as gw

from PyQt5.QtWidgets import QApplication

from const.Const_Parameter import *
from const.Const_Style import *
from const.Const_language_chinese import LANGUAGE_CHINESE
from const.Const_language_english import LANGUAGE_ENGLISH
from system.Manager_Setting import SettingManager
from system.Manager_Language import LanguageManager
from system.Manager_Style import *
from service.Function import *

isIntialized = False


def write_to_log(error_message: str):
    """ 在完成初始化前, 程序出现错误时的输出 """
    log_file_path = os.path.join(App.APP_FOLDER_PATH, 'Logs', 'critical.log')
    with open(log_file_path, 'w', encoding='utf-8') as f:
        f.write(error_message)


def exception_handler(exc_type, exc_value, exc_traceback) -> None:
    global isIntialized
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    error_message = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    if isIntialized:
        try:
            DialogMessageBox.critical(None, LM.getWord('critical_close_app')+f'\n{Log.CRITICAL.folder_path}')
            Log.CRITICAL.critical(error_message)
        except Exception as e:
            write_to_log()
    else:
        write_to_log()
    sys.exit(1)


socket_ref_list = [None]


def bring_existing_window_to_front():
    windows = gw.getWindowsWithTitle(LM.getWord('app_title'))
    if windows:
        win: gw._pygetwindow_win.Win32Window = windows[0]
        win.restore()
        win.activate()


def isAllreadyRunning():
    socket_ref_list[0] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_instance: socket.socket = socket_ref_list[0]
    try:
        socket_instance.bind(('127.0.0.1', 18686))
        return False
    except socket.error:
        return True
    except:
        Log.CRITICAL.exception()
        return True


def ensure_single_instance():
    try:
        if isAllreadyRunning():
            print("当前脚本已经在运行.")
            if not SM.getConfig('multi_win'):
                bring_existing_window_to_front()
                sys.exit()
        else:
            print("当前脚本未在运行, 继续执行其他操作. ")
    except Exception as e:
        Log.CRITICAL.exception()


def main():
    global isIntialized
    sys.excepthook = exception_handler
    SettingManager(App.APP_FOLDER_PATH, App.SettingEnum.DEFAULT_SETTING, 'PyInstallerGUI', isEncrypted=True)
    LanguageManager(LANGUAGE_CHINESE, LANGUAGE_ENGLISH, App.APP_FOLDER_PATH, SettingManager.getConfig('language'), 'PyInstallerGUI', display_tooltip=SM.getConfig('display_tooltip'))
    app = QApplication(sys.argv)
    isIntialized = True
    ensure_single_instance()
    sytle_mode = SettingManager.getConfig('style_mode')
    if sytle_mode == 'dark':
        StyleManager(SheetStyle.DARK, SheetStyle.DARK)
    elif sytle_mode == 'light':
        StyleManager(SheetStyle.LIGHT, SheetStyle.LIGHT)
    else:
        StyleManager(SheetStyle.LIGHT, SettingManager.getConfig('style_sheet'))
    window = FunctionUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
