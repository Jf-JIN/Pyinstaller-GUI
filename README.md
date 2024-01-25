# Pyinstaller_exe

中文请查看README_中文.md



### 软件简介  |  Software Introduction：

This program is designed to package Python scripts using Pyinstaller 6.0. Users can input parameters through various buttons on the interface without the need for command-line usage. The program can either print the execution commands or directly perform the packaging operation.

The initial motivation for developing this software was the author's desire to package Python scripts into executable files (exe). However, dealing with lengthy command-line parameters and paths proved to be cumbersome, prompting the development of this convenient tool.

The software may still be in the process of refinement, and there might be bugs. Your feedback and suggestions are welcome!

<div style="display:inline-block;">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/main_interface_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/english_version.png" alt="image1" height = "150">   <img src="https://github.com/JIN-Junfan/test/blob/main/image/germen_version.png" alt="image2" height = "150"> </div>

----

### 使用方法  |  Usage **Instructions**：

##### 1. 软件安装与适用   |   Installation and Application：

There is a pre-packaged executable program available directly under the .app directory for immediate use. Alternatively, you can use the installation package in the .setup directory for installation. Please note that using the installation package will automatically add a right-click menu item. When using the right-click menu, you can directly navigate to the selected .py file for packaging.

If you are using the Windows 7 operating system, please download the Win7 version. The version number with **D** indicates that the program is packaged as a directory (folder), while **F** indicates that the program is packaged as a file.

##### 2. 软件使用   |   Software Utilization：

To use the software, please ensure that Pyinstaller is already installed. If not installed, you can click "Install Pyinstaller" to proceed with the installation. Attempting to operate the software without installing Pyinstaller will prompt the console to display "*'pyinstaller' is not recognized as an internal or external command, operable program, or batch file.*".

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/Pyinstaller_noset_error.png" alt="image1" height = "150" align=center > </div>

After opening the software, it will automatically search for the main.py file in the working directory. If there is no main.py file, it will select the first .py file in the current folder. If you want to change this, please manually choose the .py file you want to package. When the "Lock" option is checked, the corresponding output folder or output name will remain as the current input; when unchecked, it will default to the same name as the original Python file and output to the directory where the original Python file is located.

Once a .py file is input, you can use the buttons below to input parameters. When the "Tooltip" option is checked, there will be tooltips and explanations when hovering the mouse.

To prevent accidental data loss, the "Clear Input" or "Clear All" buttons trigger a one-time recovery, restoring data to the state before the last clearing operation. After clearing, if you input again, some recovered data may not return to the last input state but instead revert to the state before the last clearing operation.

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/clear_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/recover_example.png" alt="image1" height = "150"> </div>

Once all necessary parameters are entered, you can click "Show Parameters" to review them or click "Print cmd command" to view the default output named "output_command_of_pyinstaller.txt" text file.

<u>**After verifying everything is correct, click "Launch" to start the packaging process.**</u>

If "Keep only the exe after completion" is checked, the .spec file and .dict and .build folders will be deleted after packaging is completed.

Clicking "Open Output Folder" allows you to view the packaged exe file once the process is finished.

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/add_file_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/dialog_example.png" alt="image1" height = "150"><img src="https://github.com/JIN-Junfan/test/blob/main/image/dialog_example_2.png" alt="image2" height = "150"> </div>

##### 3. 打包环境选择 | Packaging Environment Selection：

Next to the environment variables, there is a Conda Setup button. This button is only available if Conda (Anaconda, Miniconda, etc.) is installed on the current computer and configured correctly in the environment variables. When these conditions are met, the button becomes active, and the currently selected Conda environment is displayed. If you don't want to use the Conda environment, you can uncheck the "Use Conda Environment" option, and the global Python environment will be used instead.

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/conda1.png" alt="conda1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/conda2.png" alt="conda2" height = "150"><img src="https://github.com/JIN-Junfan/test/blob/main/image/conda5.png" alt= "conda" height = "150"> </div>

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/conda3.png" alt="conda3" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/conda4.png" alt="conda4" height = "150"> </div>

After entering the Conda settings, wait a moment, and all the current Conda environments will be displayed, allowing users to make selections. You can also check the installed Python packages in the selected Conda environment by using the button in the lower right corner. If Conda is updated, it is recommended to restart the software to avoid errors in Conda environment selection.

##### 4. 语言切换   |   Change Language:

Next to the title, there is a dropdown menu offering multiple language options. Language packs can also be added manually, with the path being the .Languages\ directory under the software's main directory. After placing a custom language pack in this directory, restart the software, and the new language pack should be available in the dropdown menu for selection. Please ensure the integrity of the language pack to avoid display errors or potential software crashes.

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/language_select.png" height = "150" alt="select_language" align=center /> </div>

----

### 开发说明   |   Development Notes：

GUI design using PyQt5

##### 开发进度   |   Development Progress：

* Completed so far: 41 functionalities of **Pyinstaller 6.0**, error prompt during runtime, synchronized console output, updated information in the information panel, display of current effective parameters, command prompt printing functionality, language switch functionality, built-in language packs, right-click file selection, Conda environment selection, automatic configuration of startup screen files.

* In progress: None (as of January 24, 2024).
* Not completed: Writing the menu bar, German language pack, version description, software explanation.

##### 开发所用资源及参考   |   Resources and References：

* PyQt5：https://doc.qt.io/qt-5/

* Pyinstaller: https://pyinstaller.org/en/stable/
* Icon Images: https://www.iconfont.cn/

##### 版本说明   |   Version Descriptions：

* v3.2:
  * Added a software configuration file, currently only recording language options. After launching the software, the language will be set to the language changed last time.
  
  * Added the option to locate files through right-click.
  
  * Fixed the issue where project files could not be deleted when the output location was in another folder.
  * Added the option to choose Conda environments.
  * Added Conda functionality for installing, checking versions, and providing help for Pyinstaller.
  * Fixed some display errors in the output commands.
  
  * Added built-in language packs (Simplified Chinese and English).
  
  * Corrected some content in the language packs.
  
  * Added automatic generation of references for the startup screen.
  
  * Fixed the issue of incomplete deletion of the .build folder.
  
  * Resolved a crash issue when clearing input with an empty Python script.
  
  * Fixed a crash issue when deselecting a Python script after selection.
  
  * Addressed display differences in different resolutions.
  
  * Changed the command line project order to avoid antivirus warnings during packaging. Now, the Python script is placed after PyInstaller and followed by --onedir or --onefile (the effectiveness is currently unknown).
  

- Fixed the issue where the automatic selection of Python files couldn't locate the main function and had incorrect order.


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
- Due to the lack of project management in the early stages, versions v1.0, v2.0, and v3.0 are missing.

----

### 注意事项   |   Notes：

None
