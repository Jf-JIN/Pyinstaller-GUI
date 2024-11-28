import time
import logging
import os
from typing import Callable


def log_base(file_path: str, folder_name: str, log_name: str, format: str = None) -> dict[str, Callable[..., None]]:
    """
    创建日志记录器并返回日志记录方法的字典. 

    参数: 
    - file_path(str): 日志文件夹父路径. 
        - 脚本可使用: **os.path.dirname(__file__)**
        - 二进制可执行文件使用: **os.getcwd()**
    - folder_name(str): 日志文件夹的名称. 
    - log_name(str): 日志记录器的名称. 
    - format(str, 可选): 日志记录的格式, 默认为 None. 

    返回值: 
    - logger_methods(dict[str, Callable[..., None]]): 包含不同日志级别方法的字典. 
    """
    __folder_name = folder_name
    __log_name = log_name
    __format = '[%(asctime)s] [%(module)s] [%(funcName)s] - %(levelname)s\n%(message)s\n'
    if format:
        __format = format
    __time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
    __basic_path = os.path.join(file_path, 'Log')
    __log_folder_path = os.path.join(__basic_path, __folder_name)
    if not os.path.exists(__log_folder_path):
        os.makedirs(__log_folder_path)
    __logger_path = os.path.join(__log_folder_path, f'[{__log_name}]_log_{__time}.log')
    __logger = logging.getLogger(__log_name)
    __logger.setLevel(logging.DEBUG)

    __file_handler = logging.FileHandler(__logger_path)
    __file_handler.setLevel(logging.DEBUG)
    __file_handler.setFormatter(logging.Formatter(__format, datefmt='%Y-%m-%d %H:%M:%S'))

    __console_handler = logging.StreamHandler()
    __console_handler.setLevel(logging.DEBUG)
    __console_handler.setFormatter(logging.Formatter(__format, datefmt='%Y-%m-%d %H:%M:%S'))

    __logger.handlers.clear()
    __logger.addHandler(__file_handler)
    __logger.addHandler(__console_handler)
    return {
        'debug': __logger.debug,
        'info': __logger.info,
        'warning': __logger.warning,
        'error': __logger.error,
        'critical': __logger.critical
    }


def log_for_decorator(file_path: str, folder_name: str, log_name: str):
    """
    创建用于装饰器的日志记录器. 

    参数: 
    - file_path(str): 日志文件的路径. 
    - folder_name(str): 日志文件夹的名称. 
    - log_name(str): 日志记录器的名称. 

    返回值: 
    - logger_methods(dict[str, Callable[..., None]]): 包含不同日志级别方法的字典. 
    """
    return log_base(file_path, folder_name, log_name, '[%(asctime)s] [module: %(moduleName)s] [function: %(functionName)s ] - %(levelname)s\n%(message)s\n')
