
from typing import Any, Callable, Union
import typing
import time
import traceback
from functools import wraps


def try_except_log(logger_error: callable = None, text_browser=None, message_box=None, funcrun=None) -> Callable[..., Any | None]:
    """
    用于捕获函数的异常并返回异常对象. 

    参数:
    - logger_error (callable, 可选): 用于记录异常的日志函数. 默认为None. 
    - textbrowser (QWidget, 可选): 用于显示异常信息的文本框. 默认为None. 

    返回值:
    Callable[..., Any | None]: 包装后的函数, 捕获函数的异常并返回异常对象.
    """
    def try_decorator(func: callable) -> Callable[..., Any | None]:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                e = traceback.format_exc()
                if logger_error:
                    logger_error(e, extra={'moduleName': func.__module__, 'functionName': func.__qualname__})
                else:
                    print(e)
                if text_browser:
                    try:
                        text_browser.append_text(e)
                    except:
                        print(traceback.format_exc())
                if message_box:
                    try:
                        message_box.warning(None, 'Warning', e)
                    except:
                        print(traceback.format_exc())
                    message_box.warning(None, 'Warning', e)
                if funcrun:
                    try:
                        funcrun(e)
                    except:
                        print(traceback.format_exc())
                return None
        return wrapper

    return try_decorator


def time_counter(func) -> Callable[..., tuple[Any, float]]:
    """
    用于计算函数的执行时间. 

    参数:
    - func: 的函数

    返回值:
    包装后的函数, 返回函数的执行结果和执行时间的元组
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'[{func.__module__}] - [{func.__qualname__}]-[runTime]:\t', end - start)
        return result
    return wrapper


def boundary_check(func) -> Callable[..., Any]:
    """
    用于检查函数的参数类型是否为注解的类型. 若非, 则打印错误信息, 并直接退出函数,  返回值为None.
    
    - <!> 请注意, 该修饰器仅能检查一层变量类型, 如果是嵌套的变量类型, 该修饰器无法检查, 请单独在被修饰函数中进行检查.
    - typing 中的类型仅支持 typing.Any, typing.Union, typing.Callable, typing.List, typing.Dict, typing.Tuple 类型.


    参数:
    - func: 被修饰器修饰的函数

    返回值:
    - 包装后的函数
    - 如果参数类型非注解类型, 则返回None
    """
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        param_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        all_args = dict(zip(param_names, args))
        all_args.update(kwargs)
        flag_error = False
        error_message = ''
        # print("所有参数:", all_args)
        # print("函数的变量注解:", annotations)
        for param_name, param_value in all_args.items():
            if param_name in annotations:
                param_type = annotations[param_name]
                try:
                # 检查 typing.Any 类型
                    if hasattr(param_type, '__origin__') and param_type.__origin__ is Any:
                        continue
                    # 检查 typing.Union 类型
                    elif hasattr(param_type, '__origin__') and param_type.__origin__ is Union:
                        allowed_types = param_type.__args__
                        if not isinstance(param_value, allowed_types):
                            error_message += f"""[{func.__module__}] - [{func.__qualname__}] - [类型错误]: 参数 '{param_name}' 的类型必须是 <class '{allowed_types}'>, 当前为: {type(param_value)}\n"""
                            flag_error = True
                            continue
                    # 检查 typing.Callable 类型
                    elif hasattr(param_type, '__origin__') and param_type.__origin__ is Callable:
                        if not isinstance(param_value, param_type):
                            error_message += f"""[{func.__module__}] - [{func.__qualname__}] - [类型错误]: 参数 '{param_name}' 的类型必须是 <class '{allowed_types}'>, 当前为: {type(param_value)}\n"""
                            flag_error = True
                            continue
                    # 检查 typing.List / typing.Dict / typing.Tuple 类型
                    if hasattr(param_type, '__origin__') and (param_type.__origin__ is list or param_type.__origin__ is dict or param_type.__origin__ is tuple):
                        if '.' in str(param_type):
                            param_type = param_type.__origin__
                    # 检查 None 类型
                    # 形参是 None,  实参也是 None 的情况
                    if param_value is None and (param_type is type(None) or param_type is None):
                        continue
                    # 形参是 None , 但是 实参是 非None 的情况
                    if param_value is not None and (param_type is type(None) or param_type is None):
                        error_message += f"""[{func.__module__}] - [{func.__qualname__}] - [类型错误]: 参数 '{param_name}' 的类型必须是 <class '{param_type}'> \t当前为: {type(param_value)}\n"""
                        flag_error = True
                        continue
                    # 形参是 非None , 但是 实参是 None 的情况
                    elif param_value is None and (param_type is not type(None) or param_type is not None):
                        error_message += f"""[{func.__module__}] - [{func.__qualname__}] - [类型错误]: 参数 '{param_name}' 的类型必须是 <class '{param_type}'> \t当前为: {type(param_value)}\n"""
                        flag_error = True
                        continue
                    # 检查其他类型
                    if '[' in str(param_type):  # 对例如 List[int], dict[str,int], tuple[int] 这些类型进行处理
                        param_type = eval(str(param_type).split('[')[0])
                    if not isinstance(param_value, param_type):
                        error_message += f"""[{func.__module__}] - [{func.__qualname__}] - [类型错误]: 参数 '{param_name}' 的类型必须是 <class '{param_type}'> \t当前为: {type(param_value)}\n"""
                        flag_error = True
                except Exception as e:
                    print(traceback.format_exc())
                    print(f"[{func.__module__}] - [{func.__qualname__}] - [装饰器错误]: 参数 '{param_name}' 注解指定 <class '{param_type}'> \t实际传入为: {type(param_value)}\n")
                    return None
        if flag_error:
            print(error_message)
            return None
        return func(*args, **kwargs)
    return wrapper 

if __name__ == '__main__':
    import os
    class Test():
        @boundary_check
        def test(self, a:Callable[...,str], b:Callable = 0,*args):
            print(a, type(a))
            print(' 这个是个测试语句 ')
    def aaa(func: Callable[..., Any]) -> Callable[..., Any]:
        pass
    a = Test()
    b = Test()
    c =a.test({'a':[1.0]}, b=aaa)
    os.system("pause")