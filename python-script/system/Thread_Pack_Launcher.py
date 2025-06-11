

from PyQt5.QtCore import QThread, pyqtSignal
import subprocess
import psutil
import traceback
import functools
from tools import *

from const.Const_Parameter import *
from system.Manager_Language import *
# import PyInstaller.__main__

_log = Log.Threads


class ThreadPackLauncher(QThread):
    signal_thread_finished = pyqtSignal(bool)
    signal_cmd_text = pyqtSignal(str)
    signal_processbar_value = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)
        self.__init_parameter()
        self.__process_bar_value_dict = {
            'Module search paths': [0, 5],
            'checking Analysis': [5, 10],
            'Initializing module': [10, 15],
            'Processing ': [15, 60],
            'checking PYZ': [80, 85],
            'Building PKG': [85, 90],
            'checking EXE': [90, 95],
            'Fixing EXE': [95, 99],
        }
        try:
            self.__logger = Logger('PyInstaller', App.APP_FOLDER_PATH, log_level=LogLevel.INFO)
            self.__logger.set_listen_logging('PyInstaller', LogLevel.INFO)
            Log.LogGroup.remove_log(self.__logger)
            self.__logger.set_enable_file_output(False)
            self.__logger.set_enable_console_output(False)
            self.__logger.set_file_count_limit(1)
            self.__logger.signal_colorized.connect(self.__cal_processbar_value)
            self.__logger.signal_colorized.connect(self.__send_log)
            self.signal_thread_finished.connect(self.__init_parameter)
        except Exception as e:
            _log.exception()

    def __send_log(self, loglevel, log: str):
        self.signal_cmd_text.emit(log)

    def set_cmd(self, cmd: str | list):
        self.__command_line = ''
        self.__command_list = []
        self.__env = ''
        if isinstance(cmd, str):
            cmd_list = cmd.split('&&')
            self.__command_line = cmd_list[-1]
            cmd_env = cmd_list[:-1]
            temp_env = []
            for env in cmd_env:
                temp_env.append(split_path_from_env_config_line(env))
            env = os.environ.copy()
            sys_env = env['PATH']
            temp_env_str = ';'.join(temp_env)
            env['PATH'] = temp_env_str + f';{sys_env}' if temp_env_str else sys_env
            self.__env = env
        else:
            self.__command_list = cmd
            self.__doUseBuiltin = True

    def __init_parameter(self, flag=None):  # flag 用于接收 signal_thread_finished 的参数, 没有实际作用
        self.__progressbar_value = 0
        self.__limit_value = 0
        self.__command_line = ''
        self.__command_list = []
        self.__doUseBuiltin = False
        self.__isSuccessful = True

    def __read_output(self):
        try:
            while True:
                output = self.__process.stdout.readline()
                if output == '' and self.__process.poll() is not None:
                    break
                if output:
                    text = output.strip()
                    self.__cal_processbar_value(None, text)
                    self.signal_cmd_text.emit(text)
        except Exception as e:
            self.signal_cmd_text.emit(traceback.format_exc())
        finally:
            if self.__isSuccessful:
                self.signal_thread_finished.emit(True)
            else:
                self.signal_thread_finished.emit(False)

    def __cal_processbar_value(self, loglevel, content: str):
        try:
            if not content:
                return
            if content[0].isdigit() and ': ' in content:
                content = content.split(': ', 1)[1]
            if self.__progressbar_value < 99 and self.__progressbar_value < self.__limit_value:
                self.__progressbar_value += 1
            for key, (lower_limit, upper_limit) in self.__process_bar_value_dict.items():
                if content.startswith(key) and self.__progressbar_value < lower_limit:
                    self.__limit_value = upper_limit
                    self.__progressbar_value = lower_limit
            if content.startswith('Building EXE') and content.endswith('successfully.'):
                self.__limit_value = 100
                self.__progressbar_value = 100
            self.signal_processbar_value.emit(self.__progressbar_value)
        except:
            _log.exception()

    def stop(self):
        if self.__doUseBuiltin:
            return

        if self.__process is None:
            _log.info('No process to terminate')
            return
        try:
            _log.info('Try to kill process tree')
            pid = self.__process.pid
            parent = psutil.Process(pid)
            children = parent.children(recursive=True)
            for child in children:
                try:
                    child.terminate()
                except psutil.NoSuchProcess:
                    pass
            parent.terminate()
            _, alive = psutil.wait_procs([parent] + children, timeout=5)
            if alive:
                for p in alive:
                    p.kill()
                psutil.wait_procs(alive)

            try:
                if self.__process.stdout is not None:
                    self.__process.stdout.close()
            except AttributeError:
                pass  # stdout 未初始化
            try:
                if self.__process.stderr is not None:
                    self.__process.stderr.close()
            except AttributeError:
                pass  # stderr 未初始化

            _log.info(f'Process {pid} terminated')
        except psutil.NoSuchProcess:
            _log.warning(f'Process {pid} does not exist')
        except Exception as e:
            _log.error(f'Error terminating process: {e}')
        finally:
            self.__process = None
            self.__isSuccessful = False

    def run(self):
        _log.info('--------------------'+LM.getWord("info_start_packing")+'--------------------')
        self.__limit_value = 0
        self.__progressbar_value = 0
        self.signal_processbar_value.emit(self.__progressbar_value)
        try:
            if self.__doUseBuiltin:
                # Log.logging_output.remove_listen_logging()
                # PyInstaller.__main__.run(self.__command_list)
                # Log.logging_output.set_listen_logging('', Log.Log_level)
                self.signal_thread_finished.emit(True)
            else:
                self.__process = subprocess.Popen(
                    self.__command_line,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    shell=True,
                    text=True,
                    env=self.__env,
                    encoding='utf-8',
                    errors='replace',
                    cwd=os.getcwd()
                )
                self.__read_output()  # 直接调用, 无需额外线程
        except Exception as e:
            _log.exception()
            self.signal_cmd_text.emit(f"Process failed: {traceback.format_exc()}")
            self.signal_thread_finished.emit(False)

    def __del__(self):
        print("Thread_Pack_Launcher::__del__")
        super().__del__()
