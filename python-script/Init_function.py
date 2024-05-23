import os
import sys
import json

# ****************************************初始化全局参数****************************************
workspace_path = os.getcwd()
exe_folder_path = os.path.dirname(sys.argv[0])

# ****************************************自寻py文件路径****************************************
py_file_name_auto = ''
if len(sys.argv) > 1 and sys.argv[1].endswith('.py'):
    py_file_path_auto = sys.argv[1]
    py_file_name_auto = os.path.basename(py_file_path_auto)
else:
    for name in os.listdir(workspace_path):
        if name == 'main.py':
            py_file_name_auto  = name
        elif not py_file_name_auto and '.py' in name:
            py_file_name_auto = name

# ****************************************读取setting文件****************************************
default_setting = {"Language":"简体中文(内置)", "Multiple_Windows":True, "textBrowser_font_size_px": 13, "textBrowser_cmd_font_size_px": 13,}
setting_path = os.path.join(exe_folder_path, 'setting')
# 检查是否为json格式，并检查是否存在该文件，若不存在则创建默认设置的setting文件
try:
    with open (setting_path, 'r', encoding='utf-8') as file:
        setting_file = json.load(file)
# 不为json格式，则重写setting文件
except:
    setting_file = default_setting
    with open (setting_path, 'w', encoding='utf-8') as file:
        json.dump(setting_file, file, ensure_ascii=False, indent=None)
new_setting_file_flag = False
# 检查缺失项
for i in default_setting:
    if not i in setting_file:
        new_setting_file_flag = True
        setting_file[i] = default_setting[i]
# 检查多余项
for key in setting_file.copy():
    if key not in default_setting:
        new_setting_file_flag = True
        del setting_file[key]
# 检查数据类型及内容
if not isinstance(setting_file["Language"], str) \
    or not os.path.exists(os.path.join(os.path.dirname(exe_folder_path), 'Languages',setting_file["Language"],'.json')) \
    or setting_file["Language"] != "简体中文(内置)" or setting_file["Language"] != "English(build-in)":
        setting_file["Language"] = "简体中文(内置)"
        new_setting_file_flag = True
if not isinstance(setting_file["Multiple_Windows"], bool):
    setting_file["Multiple_Windows"] = True
    new_setting_file_flag = True

# 如果存在缺失或者多余项等，则更新setting文件
if new_setting_file_flag == True:
    with open (setting_path, 'w', encoding='utf-8') as file:
        json.dump(setting_file, file, ensure_ascii=False, indent=None)
