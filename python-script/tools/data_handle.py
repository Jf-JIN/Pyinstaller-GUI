
from const.Const_Parameter import *


def chunk_list_by_two(data_list):
    """
    将输入列表按每两个元素一组进行分组.

    参数:
        data_list (list): 需要分组的输入列表

    返回:
        list: 包含两个元素一组的子列表的列表
    """
    temp_couple = []
    temp_list = []
    for idx, value in enumerate(data_list):
        temp_couple.append(value)
        if idx % 2 != 0:
            temp_list.append(temp_couple)
            temp_couple = []
    return temp_list


def wrapped_text(hint_phrase: str, sentence_limit=30, indent=''):
    """
    根据句子长度限制和缩进要求将文本换行.

    参数:
        hint_phrase (str): 需要换行的输入文本.
        sentence_limit (int, 可选): 每行的最大长度. 默认为30.
        indent (str, 可选): 用于缩进的字符串. 默认为空字符串.

    返回:
        str: 经过换行和缩进处理的文本.
    """
    text_list = []
    text = ''
    index_space = 0
    flag_index = False
    for idx, char in enumerate(hint_phrase):
        if char == ' ':
            index_space = idx
            flag_index = True
        if char == '\n':
            text_list.append(text)
            text = ''
            flag_index = False
            index_space = idx
            continue
        text += char
        if len(text) > sentence_limit and sentence_limit - 20 < index_space and flag_index:
            text_list.append(text[:index_space])
            text = text[index_space:]
        elif len(text) > sentence_limit:
            text_list.append(text[:sentence_limit])
            text = text[sentence_limit:]
        elif idx == len(hint_phrase) - 1:
            text_list.append(text)
    hint_phrase = f'\n{indent}'.join(text_list)
    return hint_phrase


def normalize_path(input_path):
    input_path = input_path.replace('\\', '/')
    if App.OS == OsType.WINDOWS:
        drive, p = os.path.splitdrive(input_path)
        input_path = f"{drive.upper()}{p}"
        input_path = input_path.replace("C:/users/", "C:/Users/")
    return input_path


def split_path_from_env_config_line(line: str):
    config_path = ''
    cmd_line: str = line.strip().replace('\\', '/').split(' ')[1]
    path: str = cmd_line.split('=')[1].strip('"')
    # 处理路径开头
    user_path = os.path.expanduser('~')
    if '$HOME' in path:
        path = path.replace('$HOME', user_path)
    elif 'C:/Users/' in path:
        path_part = path.split('C:/Users/')[1].split('/', 1)[1]
        path = os.path.join(user_path, path_part)
    # 处理路径结尾
    config_path = path.replace(':$PATH', '').replace(';%PATH%', '')
    # 验证路径是否存在
    if not os.path.exists(config_path):
        config_path = ''
    return config_path.replace('\\', '/')


def get_relative_path(data_path):
    if App.OS == OsType.WINDOWS:
        symbol_split = ';'
    else:
        symbol_split = ':'
        # path = f'{os.path.basename(data_path)}{symbol_split}.{os.path.relpath(os.path.dirname(data_path), App.WORKSPACE_PATH)}'
    path = f'{data_path}:.'
    return path.replace('\\', '/')


def get_absolute_path(relpath: str) -> str:
    """ 将相对路径转换为绝对路径 """
    if ';' in relpath:
        items = relpath.split(':')
        # file_name, relpath = relpath.split(';')
    else:
        items = relpath.split(':')
    file_name = ':'.join(items[:-1])
    relpath = items[-1]
    if os.path.exists(file_name):
        abspath = file_name
    else:
        abspath = os.path.join(os.path.abspath(relpath), file_name).replace('\\', '/')
    return abspath
