

from PyQt5.QtCore import QThread, pyqtSignal

import subprocess
import traceback
import platform
import os
import atexit

from tools.find_pyinstaller import *
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=5)


@atexit.register
def cleanup_executor():
    executor.shutdown(wait=True)


class PythonCondaEnvDetection(QThread):
    signal_python_path = pyqtSignal(list)
    signal_env_conda_list = pyqtSignal(list)
    signal_finished = pyqtSignal()
    signal_textBrowser_cmd = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)

    def __python_path_detection(self):
        try:
            system_name = platform.system()
            if system_name == "Windows":
                where_python = "where python"
            elif system_name == "Linux":
                where_python = "which python"
            elif system_name == "Darwin":
                where_python = "which python"
            result = subprocess.Popen(where_python, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            output = result.stdout.read().strip()
            lines = output.split('\n')
            python_path = lines[0] if lines else None

            version_result = subprocess.Popen('python --version', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            version_output = version_result.stdout.read().strip()
            version_lines = version_output.split('\n')
            python_version = version_lines[0] if version_lines else None

            self.signal_python_path.emit([python_version, python_path])
        except Exception as e:
            e = traceback.format_exc()
            # self.signal_textBrowser_cmd.emit(f'__________ {self.parent().language.error} __________\n{e}\n')

    def __conda_env_detection(self):
        try:
            result = subprocess.Popen('conda env list', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            output = result.stdout.read().strip()
            lines = output.split('\n')
            # 获取环境列表,[0] conda环境名, [1] python版本, [2] python解释器路径 [3] pyinstaller路径
            conda_env_list = []
            futures = []

            with ThreadPoolExecutor(max_workers=5) as executor:
                for line in lines:
                    if not line.startswith('#'):
                        env_info = line.split()
                        env_name = env_info[0]
                        env_path = os.path.join(env_info[-1], 'python.exe')
                        version_result = subprocess.Popen(f'"{env_path}" --version', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                        version_output = version_result.stdout.read().strip()
                        # pyinstaller_path = find_pyinstaller_path(env_path)
                        # conda_env_list.append([env_name, version_output, env_path, pyinstaller_path])
                        future = executor.submit(find_pyinstaller_path, env_path)
                        futures.append((env_name, version_output, env_path, future))

                # 等待所有线程任务完成，并收集结果
                for env_name, version_output, env_path, future in futures:
                    pyinstaller_path = future.result()  # 获取异步任务的返回结果
                    conda_env_list.append([env_name, version_output, env_path, pyinstaller_path])
                self.signal_env_conda_list.emit(conda_env_list)
                self.signal_finished.emit()
        except Exception as e:
            e = traceback.format_exc()
            print(e)
            # self.signal_textBrowser_cmd.emit(f'__________ {self.parent().language.error} __________\n{e}\n')

    def run(self):
        self.__python_path_detection()
        self.__conda_env_detection()


class PyinstallerCheck(QThread):
    signal_textBrowser_cmd = pyqtSignal(str)
    signal_pyinstaller_installed = pyqtSignal(bool)

    def __init__(self, parent, python_interpreter_path: str):
        super().__init__(parent)
        self.python_interpreter_path = python_interpreter_path

    def run(self):
        try:
            result = subprocess.Popen(f'"{self.python_interpreter_path}" -m pip show pyinstaller', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            output = result.stdout.read().strip()
            if output == 'WARNING: Package(s) not found: pyinstaller':
                self.signal_pyinstaller_installed.emit(False)
            else:
                for line in output.split('\n'):
                    if line.startswith('Version:'):
                        version = line.split(':')[1].strip()
                        if version == '5.2':
                            self.signal_pyinstaller_installed.emit(True)
                            break
                self.signal_pyinstaller_installed.emit(True)
        except Exception as e:
            e = traceback.format_exc()
            print(e)
            # self.signal_textBrowser_cmd.emit(f'__________ {self.parent().language.error} __________\n{e}\n')


class GetPythonVersion(QThread):
    signal_python_version = pyqtSignal(str)

    def __init__(self, python_interpreter_path):
        super().__init__()
        self.__python_interpreter_path = python_interpreter_path

    def run(self):
        try:
            result = subprocess.Popen('python --version', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            output = result.stdout.read().strip()
            self.signal_python_version.emit(output)
        except Exception as e:
            e = traceback.format_exc()
            print(e)
            # self.signal_textBrowser_cmd.emit(f'__________ {self.parent().language.error} __________\n{e}\n')


class Conda_Get_Detail_QThread(QThread):
    signal_conda_detail_list = pyqtSignal(str)
    signal_textBrowser_cmd = pyqtSignal(str)

    def __init__(self, parent, conda_env):
        super().__init__(parent)
        self.conda_env = conda_env

    def run(self):
        try:
            result = subprocess.Popen(f'conda list --name="{self.conda_env}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            output = result.stdout.read().strip()
            self.signal_conda_detail_list.emit(output)
        except Exception as e:
            e = traceback.format_exc()
            print(e)
            self.signal_textBrowser_cmd.emit(f'__________ {self.parent().language.error} __________\n{e}\n')
