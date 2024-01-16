# Pyinstaller_exe

中文请查看README_中文.md



### 软件简介  |  Software Introduction：

This program is designed to package Python scripts using Pyinstaller 6.0. Users can input parameters through various buttons on the interface without the need for command-line usage. The program can either print the execution commands or directly perform the packaging operation.

The initial motivation for developing this software was the author's desire to package Python scripts into executable files (exe). However, dealing with lengthy command-line parameters and paths proved to be cumbersome, prompting the development of this convenient tool.

<div style="display:inline-block;">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/main_interface_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/english_version.png" alt="image1" height = "150">   <img src="https://github.com/JIN-Junfan/test/blob/main/image/germen_version.png" alt="image2" height = "150"> </div>

----

### 使用方法  |  Usage **Instructions**：

##### 1. 软件安装与适用   |   Installation and Application：

There is a pre-packaged executable program available directly under the .app directory for immediate use. Alternatively, you can use the installation package in the .setup directory for installation. Please note that using the installation package will automatically add a right-click menu item.

If you are using the Windows 7 operating system, please download the Win7 version.

##### 2. 软件使用   |   Software Utilization：

To use the software, please ensure that Pyinstaller is already installed. If not installed, you can click "Install Pyinstaller" to proceed with the installation. Attempting to operate the software without installing Pyinstaller will prompt the console to display "*'pyinstaller' is not recognized as an internal or external command, operable program, or batch file.*".

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/Pyinstaller_noset_error.png" alt="image1" height = "150" align=center > </div>

Upon opening the software, it will automatically search for the "main.py" file in the working directory. If you need to change this, please manually select the desired .py file for packaging. When the "Lock" option is checked, the corresponding output folder or output name will retain the current input; when unchecked, it will default to the original Python file's name and output to the directory where the Python file is located.

Once a .py file is input, use the buttons below to enter parameters. When the "Tooltip" is checked, hovering the mouse will provide functional tips and explanations.

To prevent accidental data loss, the "Clear Input" or "Clear All" buttons trigger a one-time recovery, restoring data to the state before the last clearing operation. After clearing, if you input again, some recovered data may not return to the last input state but instead revert to the state before the last clearing operation.

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/clear_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/recover_example.png" alt="image1" height = "150"> </div>

Once all necessary parameters are entered, you can click "Show Parameters" to review them or click "Print cmd command" to view the default output named "output_command_of_pyinstaller.txt" text file.

<u>**After verifying everything is correct, click "Launch" to start the packaging process.**</u>

If "Keep only the exe after completion" is checked, the .spec file and .dict and .build folders will be deleted after packaging is completed.

Clicking "Open Output Folder" allows you to view the packaged exe file once the process is finished.

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/add_file_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/dialog_example.png" alt="image1" height = "150"><img src="https://github.com/JIN-Junfan/test/blob/main/image/dialog_example_2.png" alt="image2" height = "150"> </div>

##### 3. 语言切换   |   Change Language:

Next to the title, there is a dropdown menu offering multiple language options. Language packs can also be added manually, with the path being the .Languages\ directory under the software's main directory. After placing a custom language pack in this directory, restart the software, and the new language pack should be available in the dropdown menu for selection. Please ensure the integrity of the language pack to avoid display errors or potential software crashes.

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/language_select.png" height = "150" alt="select_language" align=center /> </div>

----

### 开发说明   |   Development Notes：

GUI design using PyQt5

##### 开发进度   |   Development Progress：

* Completed Features: 41 basic functionalities of **Pyinstaller 6.0**, error message prompts, synchronized console output, information panel updates, current effective parameter display, command prompt printing functionality, Language switch functionality.

* In Progress: Writing and expanding language packs; currently,  Chinese and English language packages are available.

* Not Completed: Writing the menu bar, German language pack, version description, software description, and file drag-and-drop input.

##### 开发所用资源及参考   |   Resources and References：

* Pyinstaller: https://pyinstaller.org/en/stable/
* Icon Images: https://www.iconfont.cn/

##### 版本说明   |   Version Descriptions：


* v3.1:
  * Added open environment variables, update pip functionalities.
  * Added language switch functionality.
  * Fixed a bug in certain functions where the output commands were incorrect.

- v3.0: Window Interface Version. Redesigned the window interface based on v2.0.
  - Added console display, information panel display.
  - Completed all 41 basic functionalities of Pyinstaller.
  - Added automatic detection of the default py file (main.py).
  - Added command printing and parameter display functionalities.
- v2.0: Window Interface Version. Transformed the interface of v1.0 into a window interface, added options to add application icons and files. Can automatically detect and install Pyinstaller, integrated pyuic5 and pyrcc5 for UI file to py and QRC file to py conversion.
- v1.0: Command Prompt Version. Able to list all Python files in the current directory, select the Python file to package by number, and choose whether to hide the console.

----

### 注意事项   |   Notes：

None
