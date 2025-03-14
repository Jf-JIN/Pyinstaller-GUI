# Pyinstaller_exe

中文请查看README_中文.md



### 软件简介  |  Software Introduction: 

This program is designed to package Python scripts using Pyinstaller 6.0. Users can input parameters through various buttons on the interface without the need for command-line usage. The program can either print the execution commands or directly perform the packaging operation.

The initial motivation for developing this software was the author's desire to package Python scripts into executable files (exe). However, dealing with lengthy command-line parameters and paths proved to be cumbersome, prompting the development of this convenient tool.

The software may still be in the process of refinement, and there might be bugs. Your feedback and suggestions are welcome!


----

### 使用方法  |  Usage **Instructions**: 

1. **Basic Usage**: 

   * *Opening and Packaging Files*: 
        - Open the file to be packaged. If the file is *.spec, all parameters will be automatically cleared.
        - Click "Run" to verify the parameters.
        - Click "Run" again to start packaging.
        - Once packaging is complete, click the button below to open the folder location.
   * *Optional*: 
     * Load an `*.ico` file.
        * Load a `Version.txt` file.
        * Edit the `Version.txt` file.
<div style="display:inline-block;"><img src="https://github.com/Jf-JIN/Pyinstaller-GUI/blob/main/image/Home_Page_en.png" alt="Home_Page_en" height = "200"><img src="https://github.com/Jf-JIN/Pyinstaller-GUI/blob/main/image/Light_en.png" alt="Light_en" height = "200"><img src="https://github.com/Jf-JIN/Pyinstaller-GUI/blob/main/image/Version_Editor_en.png" alt="Version_Editor_en." height = "200"></div>

<div style="display:inline-block;"><img src="https://github.com/Jf-JIN/Pyinstaller-GUI/blob/main/image/Operation_Page_en.png" alt="Operation_Page_en" height = "200"><img src="https://github.com/Jf-JIN/Pyinstaller-GUI/blob/main/image/Setting_Page_en.png" alt="Setting_Page_en" height = "200"></div>

2. **Parameter Settings**: 

   * In the feature page, you can configure PyInstaller parameters in detail

3. **Information Check**: 

   * In the information table, right-click to delete or jump to project editing.
   * Environment configuration helps manage console settings during packaging, ensuring the inclusion of necessary Python binary files. If libraries are still missing, try using the "Add file/folder resources" option.

4. **Command Line Check**: 

   * Use the buttons at the bottom of the window to adjust font size or clear the screen.

5. **Terminal Information View**: 

   * Similar to the command line, you can adjust font size and clear the screen.
   * If packaging fails, check here for error details.

6. **Settings**: 

   * *Language Settings*: 

     * Custom language packs are supported. Built-in packs include Simplified Chinese and English, formatted in JSON. Sample files can be found in `.Languages_PyInstallerGUI`.
     * Do not modify the sample file directly; create a copy instead. The sample file is rewritten every time the program starts to ensure its integrity.
     * Future updates will include manual sample generation to reduce redundant file writes.

   * *Execution Method Settings*: 

     Choose between `pyinstaller.exe` or `python.exe` to run commands.

   * *Environment Settings*:
     * Configure the environment under `Settings -> Environment`. By default, the built-in PyInstaller is used. The program detects Conda and system-installed Python versions.
     * You can also use `Env. setting` to turn to the setting page
     * If PyInstaller is not installed, the built-in version will be used by default. Other environments can be specified manually via path selection.
     * The currently used environment is displayed on both the Home and Settings pages
     * Double-clicking the **"PyInstaller not installed"** will install PyInstaller. If it is already installed, this action will update it.
   * *Style Settings*:
     - Choose between dark and light themes.
     - Custom style settings will be added in future updates.






----

### 开发说明   |   Development Notes: 

GUI design using PyQt5

##### 开发进度   |   Development Progress: 

* Completed: See version notes

  In Progress: Support for Linux

  Not Started: Menu bar, version notes, software description, error reporting, terminal display for packaging failure


##### 开发所用资源及参考   |   Resources and References: 

* PyQt5: https://doc.qt.io/qt-5/

* Pyinstaller: https://pyinstaller.org/en/stable/
* Icon Images: https://www.iconfont.cn/

##### 版本说明   |   Version Descriptions: 

* v4.0:
  * Added support for *.spec, *.pyw, *.pyd, *.spec, and *.txt (command-line files)
  * Added functionality for reading/loading command-line files
  * Added information display
  * Added command-line display
  * Added PyInstaller installation feature
  * Integrated PyInstaller support
  * Added version editor
  * Added multiple styles
  * Planned addition of custom style editing
  * Separated functional areas
  * Redesigned UI interface
  
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

