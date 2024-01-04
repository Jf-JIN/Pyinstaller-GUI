# Pyinstaller_exe



## -----------------------**English version below**-----------------------



### 软件简介：

这是一个通过使用Pyinstaller6.0来打包python脚本的程序，用户通过界面中的各按钮来进行输入而无需使用命令行，程序可打印执行命令或直接执行打包操作。

该软件起初是因为本人想把py脚本打包成exe，但是因为参数路径等命令太长，每一次写都比较麻烦，所以开发了这个小工具。

<div style="display:inline-block;">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/main_interface_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/english_version.png" alt="image1" height = "150">   <img src="https://github.com/JIN-Junfan/test/blob/main/image/germen_version.png" alt="image2" height = "150"> </div>

### 使用方法：

##### 1. 软件安装与适用：

在.app下有直接打包好的可执行程序，供直接使用。或者在.setup下使用安装包进行安装。请注意，使用安装包的话，会自动添加鼠标右键菜单项。

如果是win 7 系统，请下载Win7版本。

##### 2. 软件使用：

软件使用前提是已安装Pyinstaller。如未安装，可点击“安装Pyinstaller”进行安装。未安装Pyinstaller而进行操作，控制台将提示“ '*pyinstaller' 不是内部或外部命令，也不是可运行的程序或批处理文件。*”。

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/Pyinstaller_noset_error.png" alt="image1" height = "150" align=center > </div>

打开软件后，软件将默认寻找工作路径下的main.py文件，如需更改，请手动选择需要打包的.py文件。当勾选“锁定”时，对应的输出文件夹或输出名称将保持当前输入；取消勾选时，将默认与原python文件同名，并输出到当前python文件所在的目录下。

当输入了.py文件后，可使用下面的按钮来进行参数的输入。当“工具提示”被勾选时，鼠标悬停时会有功能提示和说明。

当使用“清空输入”或“全部清空”时，为防止误操作，可以进行一次恢复，数据将恢复至最后一次清空前的状态。当清空后，又进行输入时，部分恢复数据不会恢复至最后一次输入的状态，而是恢复至最后一次清空前的状态。

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/clear_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/recover_example.png" alt="image1" height = "150"> </div>

当所有所需参数全部输入完成后，可点击“显示参数”进行检查，或者点击“打印cmd命令”，查看默认输出名为“output_command_of_pyinstaller.txt”文本文件。

<u>**检查无误后，可点击   “ 开始执行转换 ”   进行打包。**</u>

当“结束后仅保留exe”被勾选时，将在打包完成后删除.spec文件以及 .dict 和 .build 文件夹。

点击“打开输出文件夹”，即可查看打包完成的exe文件

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/add_file_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/dialog_example.png" alt="image1" height = "150"><img src="https://github.com/JIN-Junfan/test/blob/main/image/dialog_example_2.png" alt="image2" height = "150"> </div>

##### 3. 语言切换

在标题旁边有一个下拉菜单栏，有多种语言可供选择。语言包也可自行添加，路径为该软件的目录下.Languages\中，当自定义的语言包放到该目录后，重新启动软件，新的语言包即可在下拉菜单栏中找到并使用。请注意语言包的完整性，否则将会出现显示错误，甚至软件崩溃。

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/language_select.png" height = "150" alt="select_language" align=center /> </div>

### 开发说明：

##### 开发进度：

* 当前已完成：基本的所有**Pyinstaller*6.0***的功能项41项、运行报错提示、控制台同步输出、信息台信息更新、当前有效参数显示、命令提示符打印功能

* 正在进行：语言包的编写与扩展，当前为中文的语言包。语言切换功能

* 未完成：菜单栏的编写，英语语言包，德语语言包，版本说明，软件说明，文件拖拽输入

##### 开发所用资源及参考：

* Pyinstaller：https://pyinstaller.org/en/stable/

* icon图标：https://www.iconfont.cn/

* 所用语言及主要库：Python，PyQt5，os，subprocess，sys，threading，json

##### 版本说明：

* v3.0：窗口界面版。在v2.0基础上，重新设计窗口界面
  * 增加了控制台显示，信息台显示。
  * 补全了pyinstaller基本所有的功能41项
  * 增加了自寻找默认py文件(main.py)
  * 增加了打印命令功能，显示参数功能
  * 增加了打开环境变量，更新pip功能
  * 增加了语言切换功能
  
* v2.0：窗口界面版。将v1.0的界面改为窗口界面，增加了添加应用图标和添加文件的选项，可自动检测并安装pyinstaller，集成了pyuic5和pyrcc5，可进行ui文件转py，qrc文件转py

* v1.0：命令提示符版。可列出当前目录下所有python文件，可通过数字选择要打包的Python文件，可选择是否隐藏控制台

### 注意事项：

暂无

----
## 																						                          							**English Version**

****



### Software Introduction:

This program is designed to package Python scripts using Pyinstaller 6.0. Users can input parameters through various buttons on the interface without the need for command-line usage. The program can either print the execution commands or directly perform the packaging operation.

The initial motivation for developing this software was the author's desire to package Python scripts into executable files (exe). However, dealing with lengthy command-line parameters and paths proved to be cumbersome, prompting the development of this convenient tool.

<div style="display:inline-block;">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/main_interface_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/english_version.png" alt="image1" height = "150">   <img src="https://github.com/JIN-Junfan/test/blob/main/image/germen_version.png" alt="image2" height = "150"> </div>

### Usage Instructions:

##### 1. Installation and Application:

There is a pre-packaged executable program available directly under the .app directory for immediate use. Alternatively, you can use the installation package in the .setup directory for installation. Please note that using the installation package will automatically add a right-click menu item.

If you are using the Windows 7 operating system, please download the Win7 version.

##### 2. Software Utilization:

To use the software, ensure that Pyinstaller is already installed. If not installed, you can click "Install Pyinstaller" to proceed with the installation. Attempting to operate the software without installing Pyinstaller will prompt the console to display "*'pyinstaller' is not recognized as an internal or external command, operable program, or batch file.*".

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/Pyinstaller_noset_error.png" alt="image1" height = "150" align=center > </div>

Upon opening the software, it will automatically search for the "main.py" file in the working directory. If you need to change this, please manually select the desired .py file for packaging. When the "Lock" option is checked, the corresponding output folder or output name will retain the current input; when unchecked, it will default to the original Python file's name and output to the directory where the Python file is located.

Once a .py file is input, use the buttons below to enter parameters. When the "Tooltip" is checked, hovering the mouse will provide functional tips and explanations.

To prevent accidental data loss, the "Clear Input" or "Clear All" buttons trigger a one-time recovery, restoring data to the state before the last clearing operation. After clearing, if you input again, some recovered data may not return to the last input state but instead revert to the state before the last clearing operation.

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/clear_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/recover_example.png" alt="image1" height = "150"> </div>

Once all necessary parameters are entered, you can click "Show Parameters" to review them or click "Print cmd command" to view the default output named "output_command_of_pyinstaller.txt" text file.

<u>**After verifying everything is correct, click "Start Conversion" to initiate the packaging process.**</u>

If "Keep only the exe after completion" is checked, the .spec file and .dict and .build folders will be deleted after packaging is completed.

Clicking "Open Output Folder" allows you to view the packaged exe file once the process is finished.

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/add_file_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/dialog_example.png" alt="image1" height = "150"><img src="https://github.com/JIN-Junfan/test/blob/main/image/dialog_example_2.png" alt="image2" height = "150"> </div>

Next to the title, there is a dropdown menu offering multiple language options. Language packs can also be added manually, with the path being the .Languages\ directory under the software's main directory. After placing a custom language pack in this directory, restart the software, and the new language pack should be available in the dropdown menu for selection. Please ensure the integrity of the language pack to avoid display errors or potential software crashes.

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/language_select.png" height = "150" alt="select_language" align=center /> </div>

### Development Notes:

##### Development Progress:

- Completed Features: 41 basic functionalities of **Pyinstaller 6.0**, error message prompts, synchronized console output, information panel updates, current effective parameter display, and command prompt printing functionality.
- In Progress: Writing and expanding language packs; currently, a Chinese language pack is available. Language switch functionality is also being developed.
- Not Completed: Writing the menu bar, English language pack, German language pack, version description, software description, and file drag-and-drop input.

##### Resources and References:

- Pyinstaller: https://pyinstaller.org/en/stable/
- Icon Images: https://www.iconfont.cn/
- Programming Languages and Main Libraries Used: Python, PyQt5, os, subprocess, sys, threading, json

##### Version Descriptions:

- v3.0: Window Interface Version. Redesigned the window interface based on v2.0.
  - Added console display, information panel display.
  - Completed all 41 basic functionalities of Pyinstaller.
  - Added automatic detection of the default py file (main.py).
  - Added command printing and parameter display functionalities.
  - Added open environment variables, update pip functionalities.
  - Added language switch functionality.
- v2.0: Window Interface Version. Transformed the interface of v1.0 into a window interface, added options to add application icons and files. Can automatically detect and install Pyinstaller, integrated pyuic5 and pyrcc5 for UI file to py and QRC file to py conversion.
- v1.0: Command Prompt Version. Able to list all Python files in the current directory, select the Python file to package by number, and choose whether to hide the console.

### Notes:

None
