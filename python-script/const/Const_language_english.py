LANGUAGE_ENGLISH = {
    "Widgets": {
        "pb_Enviroment": {
            "tooltip": "This option directly opens the environment variables and \nis used to determine the Python interpreter version for the packaging operation",
            "text": "Environment Variables"
        },
        "pb_CondaSetting": {
            "tooltip": "This control can be used to set up the use of the Conda environment for packaging.\nNote: If Conda is not installed or not added to the environment variable, this button cannot be used.\nPlease check the installation of Conda",
            "text": "Conda settings"
        },
        "pb_FilePath": {
            "tooltip": "Browse the Python script path, \nwhich defaults to the main.py file path in the current directory",
            "text": "Open"
        },
        "pb_OutputPath": {
            "tooltip": "Browse the output path, \nwhich may include .spec, /build, /dict or .exe",
            "text": "Open"
        },
        "pb_Recover": {
            "tooltip": "This function can only restore the last option content before clearing input or clearing all\nPlease operate with caution!",
            "text": "Recover"
        },
        "pb_ClearAll": {
            "tooltip": "Clear all contents, including console display, info display, and currently entered option contents\nTo prevent misoperation, you can restore data through the restore button\nPlease operate with caution!",
            "text": "Clear All"
        },
        "pb_ClearConsole": {
            "tooltip": "Clear the information displayed on the console",
            "text": "Clear Console"
        },
        "pb_ClearInfo": {
            "tooltip": "Clear the information displayed on the info display",
            "text": "Clear Info Display"
        },
        "pb_ClearAllDisplay": {
            "tooltip": "Clear all display information, including console and info display",
            "text": "Clear All Displays"
        },
        "pb_ClearInput": {
            "tooltip": "The current input options will be cleared\nTo prevent misoperation, you can restore data through the restore button\nPlease operate with caution!",
            "text": "Clear Input",
            "msg_content": "You are currently executing the operation to clear the input. Do you want to confirm this?<br><br>The restore function can only restore data entered before the last clearing of the input.<br>Consecutive clearing of input twice will make it impossible to restore the previous data entered",
            "pb_certain_clear": "Confirm clearing"
        },
        "pb_ShowParameter": {
            "tooltip": "Display all entered valid parameters",
            "text": "Show Parameters"
        },
        "pb_OpenDir": {
            "tooltip": "Open the output folder",
            "text": "Open Output Folder"
        },
        "pb_Print": {
            "tooltip": "Print the command line command to output_command_of_pyinstaller.txt",
            "text": "Print Execution Commands"
        },
        "pb_Launch": {
            "tooltip": "Start the packaging operation",
            "text": "Launch"
        },
        "pb_SetupPyinstaller": {
            "tooltip": "Install PyInstaller",
            "text": "Install PyInstaller",
            "text_browser_display": "已成功安装pyinstaller"
        },
        "pb_VersionDisplay": {
            "tooltip": "Display PyInstaller version information in the console",
            "text": "Pyinstaller Version",
            "text_browser_display": "PyInstaller version information has been displayed",
            "text_browser_cmd_display": "Current PyInstaller version information"
        },
        "pb_HelpDisplay": {
            "tooltip": "Display the help information for PyInstaller in the console",
            "text": "Pyinstaller Help",
            "text_browser_display": "PyInstaller help information has been displayed",
            "text_browser_cmd_display": "The above information is the help information for PyInstaller"
        },
        "pb_AddBinaryData": {
            "tooltip": "Additional binary files to be added to the executable.\nThis option can be used multiple times",
            "text": "Add Binary Resource",
            "dict": "\nAdding binary resources: \t",
            "text_browser_display": "Update binary file",
            "dialog_title": "Please select the binary file to be added to the executable file"
        },
        "pb_AddFileFolderData": {
            "tooltip": "Additional data files or directories containing data files to be added to the application. \nThe argument value should be in form of 'source:dest_dir', where source is the path to file (or directory) to be collected, \ndest_dir is the destination directory relative to the top-level application directory, \nand both paths are separated by a colon (:). To put a file in the top-level application directory, use . as a dest_dir. \nThis option can be used multiple times",
            "text": "Add Data",
            "dict": "\nAdd file resources: \t",
            "text_browser_display": "Update the file to be added to the executable file",
            "dialog_title": "Please select the file to be added to the executable file"
        },
        "pb_AddIcon": {
            "tooltip": "apply the icon to a Windows executable. FILE.exe,ID: extract the icon with ID from an exe. FILE.icns: apply the icon to the .app bundle on Mac OS. \nIf an image file is entered that isn't in the platform format (ico on Windows, icns on Mac), \nPyInstaller tries to use Pillow to translate the icon into the correct format (if Pillow is installed). \nUse 'NONE' to not apply any icon, thereby making the OS show some default (default: apply PyInstaller'sicon). \nThis option can be used multiple times",
            "text": "Add Application Icon",
            "dict": "\nApplication icon path: \t",
            "text_browser_display": "Update the application icon",
            "dialog_title": "Please select the icon to be used as the application icon"
        },
        "pb_AdditionalHooksDir": {
            "tooltip": "An additional path to search for hooks. \nThis option can be used multiple times",
            "text": "Additional Hook Path",
            "dict": "\nAdd the specified hook folder path: \t",
            "text_browser_display": "Update the hook script search directory",
            "dialog_title": "Please select the directory where the hook scripts are located"
        },
        "pb_AddResource": {
            "tooltip": "Add or update a resource to a Windows executable. \nThe RESOURCE is one to four items, FILE[,TYPE[,NAME[,LANGUAGE]]]. \nFILE can be a data file or an exe/dll. For data files, at least TYPE and NAME must be specified. \nLANGUAGE defaults to 0 or may be specified as wildcard * to update all resources of the given TYPE and NAME. \nFor exe/dll files, all resources from FILE will be added/updated to the final executable if TYPE, NAME and LANGUAGE are omitted or specified as wildcard *. \nThis option can be used multiple times",
            "text": "Add Resource (Specify)",
            "dict": "\nAdd files or directories embedded in the EXE: \t",
            "msg_content": "Please select the specific information for the data to be embedded in the executable file, in the following format:<br>'Format, Name, Language' (where the comma ',' must be an English comma)<br><br>Format: The type of resource, typically a MIME type, such as 'text/plain'<br>Name: The name of the resource embedded in the executable file<br>Language: The language of the resource, typically a number or string indicating the language of the resource. On Windows systems, the language code is usually a four-digit decimal number, for example, 1033 for English (USA). On other systems, the standard IETF BCP 47 language tag may be used.<br><br>Example:<br>image/png,app_data,1033<br>,,1033<br>,app_data<br><br>If this is not needed, simply press Enter or click 'OK'",
            "text_browser_display": "Update the files or directories embedded in the generated executable file",
            "dialog_title": "Please select the input data type to be embedded in the generated executable file"
        },
        "pb_AddSplashScreen": {
            "tooltip": "(EXPERIMENTAL) Add an splash screen with the image IMAGE_FILE to the application.\nThe splash screen can display progress updates while unpacking",
            "text": "Add Splash Screen",
            "dict": "\nApplication startup screen: \t",
            "text_browser_display": "Add the application startup screen",
            "dialog_title": "Please select the startup screen"
        },
        "pb_AddXmlFile": {
            "tooltip": "Add manifest FILE or XML to the exe",
            "text": "Add FILE or XML",
            "dict": "\nAdd file or XML resources: \t",
            "text_browser_display": "Add FILE or XML files",
            "dialog_title": "Please select the FILE or XML files to be added to the EXE"
        },
        "pb_ImportsFolder": {
            "tooltip": "A path to search for imports (like using PYTHONPATH). \nMultiple paths are allowed, separated by ``';'``, \nor use this option multiple times. \nEquivalent to supplying the ``pathex`` argument in the spec file",
            "text": "Search Import Paths",
            "dict": "\nSearch for the import module path: \t",
            "text_browser_display": "Update the search path when importing modules",
            "dialog_title": "Please select the specified Python module search path"
        },
        "pb_ImportModuleName": {
            "tooltip": "",
            "text": "Hidden Import",
            "dict": "\nReference to an external, specified import module name: \t",
            "text_browser_display": "Update the explicitly imported Python modules",
            "dialog_title": "Please enter the name of the externally imported module",
            "sub_dialog_title": "Please enter the name of the module to be imported from external sources.:",
            "sub_dialog_content": "Use this to specify Python modules not explicitly imported in the source code that should be included in the generated executable"
        },
        "pb_VersionFile": {
            "tooltip": "Add a version resource from FILE to the exe",
            "text": "Add Version File",
            "dict": "\nAdd version resources: \t",
            "text_browser_display": "Add the application version information file",
            "dialog_title": "Please select the application version information file"
        },
        "pb_CollectSubmodules": {
            "tooltip": "Collect all submodules from the specified package or module. \nThis option can be used multiple times",
            "text": "Collect Submodules",
            "dict": "\nPackage itself and all its submodules: \t",
            "text_browser_display": "Update the packaging process to explicitly collect specified modules and all their submodules",
            "dialog_title": "Please enter the module name",
            "sub_dialog_title": "Please enter the module name:",
            "sub_dialog_content": "Use this to explicitly collect specified modules and all their submodules during the packaging process"
        },
        "pb_CopyMetadata": {
            "tooltip": "Copy metadata for the specified package. This option can be used multiple times.",
            "text": "Copy Metadata",
            "dict": "\nModule for packaging metadata: \t",
            "text_browser_display": "Update the packaging process to include the metadata of the specified module.",
            "dialog_title": "Please enter the module name.",
            "sub_dialog_title": "Please enter the module name for which metadata should be packaged.",
            "sub_dialog_content": "Use this to copy the metadata of the specified module into the generated executable file during the packaging process."
        },
        "pb_RecursiveCopyMetadata": {
            "tooltip": "Copy metadata for the specified package and all its dependencies. This option can be used multiple times.",
            "text": "Recursive Copy Metadata",
            "dict": "\nModule for packaging metadata for itself and all dependencies: \t",
            "text_browser_display": "Update the packaging process to recursively include the metadata of the specified package and all packages it depends on.",
            "dialog_title": "Please enter the module name.",
            "sub_dialog_title": "Please enter the module name for which metadata and dependencies should be packaged:",
            "sub_dialog_content": "Use this to recursively copy the metadata of the specified package and all packages it depends on into the generated executable file during the packaging process. This way, not only the metadata of the package itself will be copied, but also the metadata of its dependencies."
        },
        "pb_CollectData": {
            "tooltip": "Collect all data from the specified package or module. This option can be used multiple times.",
            "text": "Collect Module Data",
            "dict": "\nModule for packaging all data: \t",
            "text_browser_display": "Update the packaging process to collect data files of the specified module",
            "dialog_title": "Please enter the module name.",
            "sub_dialog_title": "Please enter the module name for which data should be packaged:",
            "sub_dialog_content": "Use this to collect data files of the specified module during the packaging process. <br> This option ensures that PyInstaller includes the necessary data files for the specified module, which may be dynamically loaded by the module at runtime."
        },
        "pb_CollectAll": {
            "tooltip": "Collect all submodules, data files, and binaries from the specified package or module. This option can be used multiple times.",
            "text": "Collect all Module Data",
            "dict": "\nModule for packaging all data: \t",
            "text_browser_display": "Update the packaging process to collect all data files, metadata, etc. of the specified module and its dependencies.",
            "dialog_title": "Please enter the module name",
            "sub_dialog_title": "Please enter the module name for which all data should be packaged: ",
            "sub_dialog_content": "Use this to collect all data files, metadata, etc. of the specified module and its dependencies during the packaging process. <br> The purpose of this option is to include as many resources as possible from the specified module and its related elements in the generated executable file."
        },
        "pb_CollectBinaries": {
            "tooltip": "Collect all binaries from the specified package or module. This option can be used multiple times.",
            "text": "Collect Binaries",
            "dict": "\nModule for packaging all binary files of the module: \t",
            "text_browser_display": "Update the packaging process to collect all binary files of the specified module and its dependencies.",
            "dialog_title": "Please enter the module name",
            "sub_dialog_title": "Please enter the module name for which binary files should be packaged: ",
            "sub_dialog_content": "Use this to collect all binary files of the specified module and its dependencies during the packaging process. <br> The purpose of this option is to include the binary files of the module and its relevant elements in the generated executable file."
        },
        "pb_RuntimeHook": {
            "tooltip": "Path to a custom runtime hook file. A runtime hook is code that is bundled with the executable and is executed before any other code or module to set up special features of the runtime environment. This option can be used multiple times.",
            "text": "Runtime Hook",
            "dict": "\nAdd the path for runtime hook files: \t",
            "text_browser_display": "Update the path for runtime hook scripts",
            "dialog_title": "Please select the hook script"
        },
        "pb_TargetArchitecture": {
            "tooltip": "Target architecture (macOS only; valid values: x86_64, arm64, universal2). Enables switching between universal2 and single-arch version of frozen application (provided python installation supports the target architecture). If not target architecture is not specified, the current running architecture is targeted. Only MacOs",
            "text": "Target Architecture",
            "dict": "\nTarget architecture: \t",
            "text_browser_display": "Please select the target architecture.",
            "dialog_title": "Please select the target architecture.<br>By default, PyInstaller will attempt to choose the appropriate target architecture based on the system architecture."
        },
        "pb_CodesignIdentity": {
            "tooltip": "Code signing identity (macOS only). Use the provided identity to sign collected binaries and generated executable. If signing identity is not provided, ad-hoc signing is performed instead.",
            "text": "Codesign Identity",
            "dict": "\nCode-Signatur:\t",
            "text_browser_display": "Please enter the code signing.",
            "dialog_title": "Used on the macOS platform to sign the generated application.<br>Code signing is a method of adding a digital signature to the application to verify its origin and integrity.<br>Use the provided identity to sign the collected binary files and the generated executable.<br>If no signing identity is provided, it will perform an ad-hoc signing."
        },
        "pb_OsxEntitlementsFile": {
            "tooltip": "Entitlements file to use when code-signing the collected binaries (macOS only).",
            "text": "Osx Entitlements File",
            "dict": "\nBinary entitlements file:\t",
            "text_browser_display": "Add entitlements file",
            "dialog_title": "Please select entitlements file"
        },
        "pb_ExcludeModule": {
            "tooltip": "Optional module or package (the Python name, not the path name) that will be ignored (as though it was not found). This option can be used multiple times.",
            "text": "Exclude Module",
            "dict": "\nOptional modules or packages to be ignored:\t",
            "text_browser_display": "Update the optional modules to be ignored.",
            "dialog_title": "Please input the module name",
            "sub_dialog_title": "Please input the module name to be ignored:",
            "sub_dialog_content": "Used to specify modules to be excluded during the packaging process.<br>This option allows you to explicitly specify which modules should not be included in the generated executable file."
        },
        "pb_UpxExclude": {
            "tooltip": "Prevent a binary from being compressed when using upx. This is typically used if upx corrupts certain binaries during compression. FILE is the filename of the binary without path. This option can be used multiple times.",
            "text": "Upx Exclude",
            "dict": "\nExclude files from UPX compression:\t",
            "text_browser_display": "Add files to be excluded during the UPX compression process",
            "dialog_title": "Select files to be excluded during the UPX compression process:"
        },
        "pb_UpxDir": {
            "tooltip": "Path to UPX utility (default: search the execution path)",
            "text": "Upx Directory",
            "dict": "\nPath of UPX-Tool: \t",
            "text_browser_display": "Add the directory path for the specified UPX compression tool",
            "dialog_title": "Please select the folder to specify the directory path for the specific UPX compression tool"
        },
        "pb_LogLevel": {
            "tooltip": "Amount of detail in build-time console messages. LEVEL may be one of TRACE, DEBUG, INFO, WARN, DEPRECATION, ERROR, FATAL (default: INFO). Also settable via and overrides the PYI_LOG_LEVEL environment variable.",
            "text": "Log Level",
            "dict": "\nLog Level: \t",
            "text_browser_display": "Log Level",
            "current_level": "Current Log Level: ",
            "dialog_title": "Please select Log Level",
            "trace_translate": "",
            "debug_translate": "",
            "info_translate": "",
            "warn_translate": "",
            "deprecation_translate": "",
            "error_translate": "",
            "fatal_translate": ""
        },
        "pb_RuntimeTmpdir": {
            "tooltip": "Where to extract libraries and support files in `onefile`-mode. If this option is given, the bootloader will ignore any temp-folder location defined by the run-time OS. The ``_MEIxxxxxx``-folder will be created here. Please use this option only if you know what you are doing.",
            "text": "Runtime Tempdirectory",
            "dict": "\nDirectory for extracting libraries and support files: \t",
            "msg_info": "This option can only be used in \"Output as Folder\" mode",
            "text_browser_display": "Add the directory for extracting libraries and support files",
            "dialog_title": "Please select the folder to specify the directory for extracting libraries and support files"
        },
        "pb_WorkpathOption": {
            "tooltip": "Where to put all the temporary work files, .log, .pyz and etc. (default: ./build)",
            "text": "Workpath",
            "dict": "\nWorkpath: \t",
            "text_browser_display": "Add workpath",
            "dialog_title": "Please select the folder to specify the working directory"
        },
        "pb_DebugMode": {
            "tooltip": "Provide assistance with debugging a frozen application. This argument may be provided multiple times to select several of the following options. <br><br>- all: All three of the following options. <br><br>- imports: specify the -v option to the underlying Python interpreter, causing it to print a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded. <br><br>- bootloader: tell the bootloader to issue progress messages while initializing and starting the bundled app. Used to diagnose problems with missing imports. <br><br>- noarchive: instead of storing all frozen Python source files as an archive inside the resulting executable, store them as files in the resulting output directory.",
            "text": "Debug Mode",
            "dict": "\nDebug Mode: \t",
            "text_browser_display": "Debug Mode",
            "current_level": "Current Debug Mode: ",
            "dialog_title": "Please select Debug Mode: ",
            "all_translate": "",
            "imports_translate": "",
            "bootloader_translate": "",
            "noarchive_translate": ""
        },
        "pb_PythonOption": {
            "tooltip": "Specify a command-line option to pass to the Python interpreter at runtime. Currently supports 'v' (equivalent to '--debug imports'), 'u', and 'W <warning control>'",
            "text": "Python Option",
            "dict": "\nCommand line for the specified Python interpreter:\t",
            "text_browser_display": "Options of Command line for the specified Python interpreter",
            "current_level": "Current option: ",
            "dialog_title": "Please select option: ",
            "dialog_content": "Currently supports 'v' (equivalent to '--debug imports'), 'u', and 'W <warning control>'",
            "parameter": "parameter"
        },
        "pb_HideConsole": {
            "tooltip": "Windows only: in console-enabled executable, have bootloader automatically hide or minimize the console window if the program owns the console window (i.e., was not launched from an existing console window).",
            "text": "Console Display",
            "dict": "\nDisplay mode of the console window:\t",
            "text_browser_display": "Display mode of the console window:",
            "current_level": "Display mode of the console window:",
            "dialog_title": "Please select the display mode of the console window",
            "dialog_content": "",
            "minimize_late_translate": "",
            "hide_early_translate": "",
            "minimize_early_translate": "",
            "hide_late_translate": ""
        },
        "pb_OsxBundleIdentifier": {
            "tooltip": "Mac OS .app bundle identifier is used as the default unique program name for code signing purposes. The usual form is a hierarchical name in reverse DNS notation. For example: com.mycompany.department.appname (default: first script's basename)",
            "text": "Bundle Identifier",
            "dict": "\nBundle Identifier: \t",
            "dialog_title": "Please input Bundle Identifier",
            "dialog_content": "Mac OS .app bundle identifier is used as the default unique program name for code signing purposes.<br> The usual form is a hierarchical name in reverse DNS notation. <br>For example: com.mycompany.department.appname (default: first script's basename)"
        },
        "pb_Specpath": {
            "tooltip": "Folder to store the generated spec file (default: current directory)",
            "text": "Specpath",
            "dict": "\n.spec folder: \t",
            "msg_replace": "Do you want to replace the path for the \"Replace original file\" option?",
            "select_folder_text_browser": "Add the save path for the .spec file",
            "select_folder_win_title": "Please select the save path for the .spec file"
        },
        "cb_CondaUse": {
            "tooltip": "After Conda settings have been configured, this option will be automatically selected.\nDeselect to use the system's Python interpreter environment",
            "text": "Using the Conda environment"
        },
        "cb_Tooltips": {
            "tooltip": "After selecting this option, a tooltip will appear when hovering the mouse",
            "text": "Tooltips"
        },
        "cb_PathLock": {
            "tooltip": "When this option is selected, the output path will no longer be automatically changed with the path of the Py script",
            "text": "Locked"
        },
        "cb_NameLock": {
            "tooltip": "When this option is selected, the output filename will no longer be automatically changed with the name of the Py script",
            "text": "Locked"
        },
        "cb_DisableWindowed": {
            "tooltip": "Disable traceback dump of unhandled exception in windowed (noconsole) mode (Windows and macOS only), and instead display a message that this feature is disabled.",
            "text": "Disable Windowed",
            "dict": "\nDisable Windowed: \t",
            "dict_explain": "Disable Windowed"
        },
        "cb_UacAdminApply": {
            "tooltip": "Using this option creates a Manifest that will request elevation upon application start",
            "text": "Uac Admin Apply",
            "dict": "\nUac Admin Apply:\t",
            "dict_explain": "Apply"
        },
        "cb_IgnoreSignals": {
            "tooltip": "Tell the bootloader to ignore signals rather than forwarding them to the child process. Useful in situations where for example a supervisor process signals both the bootloader and the child (e.g., via a process group) to avoid signalling the child twice.",
            "text": "Ignore Signals",
            "dict": "\nBootloader ignores signals:\t",
            "dict_explain": "Ignore Signals"
        },
        "cb_UacUiaccess": {
            "tooltip": "Using this option allows an elevated application to work with Remote Desktop.",
            "text": "Uac Uiaccess",
            "dict": "\nElevated application to work with Remote Desktop:\t",
            "dict_explain": "Allow"
        },
        "cb_ArgvEmulation": {
            "tooltip": "Enable argv emulation for macOS app bundles. If enabled, the initial open document/URL event is processed by the bootloader and the passed file paths or URLs are appended to sys.argv.",
            "text": "Argv Emulation",
            "dict": "\nEnable macOS argv emulation:\t",
            "dict_explain": "Enable"
        },
        "cb_NoupxOption": {
            "tooltip": "Do not use UPX even if it is available (works differently between Windows and *nix)",
            "text": "No upx Option",
            "dict": "\nUse UPX:\t",
            "dict_explain": "No UPX",
            "msg_content": "UPX is a compression tool for executable files and can significantly reduce the size of executable files.<br><br>But even if available, do not use UPX (it works differently between Windows and *nix)."
        },
        "cb_NoconfirmOption": {
            "tooltip": "Replace output directory (default: SPECPATH/dist/SPECNAME) without asking for confirmation",
            "text": "No confirm Option",
            "dict": "\nReplace output directory:\t",
            "dict_explain": "default: SPECPATH/dist/SPECNAME, without asking for confirmation"
        },
        "cb_ClearCache": {
            "tooltip": "Clean PyInstaller cache and remove temporary files before building.",
            "text": "Clear Cache",
            "dict": "\nClear Cache: \t",
            "dict_explain": "Clear"
        },
        "cb_ClearFileAfterLaunchFlagChange": {
            "tooltip": "After the packaging operation is complete, other temporary files used for packaging will be deleted, including .spec, /build, /dict. Only the .exe file will be retained",
            "text": "Only Exe"
        },
        "cb_StripOption": {
            "tooltip": "Apply a symbol-table strip to the executable and shared libs (not recommended for Windows)",
            "text": "Strip Option",
            "dict": "\nStrip application symbol table from executable file and shared libraries:\t",
            "dict_explain": "Strip shared application symbol table"
        },
        "cb_SplashAutoFile": {
            "tooltip": "After selecting, the file SplashModule.py will be automatically generated, \nand the import will be added in the main function \nto avoid the splash screen not closing automatically after launch",
            "text": "Auto-splash-screen\nconfiguration"
        },
        "cb_MultiWin": {
            "tooltip": "After selecting this option, when processing multiple .py files, multiple windows will be used. \nIf not selected, only one .py file can be processed at a time, but you can open files automatically through right-click.",
            "text": "Multi-Wins"
        },
        "rb_OutputMethod_F": {
            "tooltip": "Create a one-file bundled executable.",
            "text": "Output as File",
            "dict": "\nOutput methode: \t",
            "dict_explain": "Create a one-file bundled executable"
        },
        "rb_OutputMethod_D": {
            "tooltip": "Create a one-folder bundle containing an executable",
            "text": "Output as Folder",
            "dict": "\nOutput methode: \t",
            "dict_explain": "Create a one-folder bundle containing an executable"
        },
        "contents_directory": {
            "dict": "\nThe path for storing other data, apart from the .exe file:\t",
            "msg_content": "Is an output folder specified?<br>All content, except for the executable file itself, will be placed there.",
            "dialog_title": "Please input the name of the folder",
            "dialog_content": "Please enter the folder name to place other data besides the .exe file."
        },
        "rb_ConsoleWindowControl_C": {
            "tooltip": "Display Console",
            "text": "Console On(standard)",
            "dict": "\nConsole display: \t",
            "dict_explain": "Display Console (console)"
        },
        "rb_ConsoleWindowControl_NW": {
            "tooltip": "Display Console",
            "text": "Console On",
            "dict": "\nConsole display: \t",
            "dict_explain": "Display Console (nowindowed)"
        },
        "rb_ConsoleWindowControl_W": {
            "tooltip": "Hide Console",
            "text": "Console Off(standard)",
            "dict": "\nConsole display: \t",
            "dict_explain": "Hide Console (windowed)"
        },
        "rb_ConsoleWindowControl_NC": {
            "tooltip": "Hide Console",
            "text": "Console Off",
            "dict": "\nConsole display: \t",
            "dict_explain": "Hide Console (console)"
        },
        "lb_Title": {"text": "Python To exe"},
        "lb_FilePath": {"text": "File path:"},
        "lb_OutputPath": {"text": "Output path:"},
        "lb_FileName": {"text": "Output file name: "},
        "lb_CondaTitle": {"text": "Conda Current: "},
        "pte_FilePath": {"dict": "\nPython script: \t"},
        "pte_OutputPath": {"dict": "\nOutput directory\t"},
        "pte_FileName": {"dict": "\nOutput file name: \t"},
        # ############################################# [PushButton] #############################################
        "pb_input_py_file_browser": {
            "display_text": "Browse ____",
            "tooltip": "______________________"
        },
        "pb_output_folder_browser": {
            "display_text": "Browse ____",
            "tooltip": "______________________"
        },
        "pb_output_exe_icon_browser": {
            "display_text": "Browse ____",
            "tooltip": "______________________"
        },
        "pb_output_exe_version_browser": {
            "display_text": "Browse ____",
            "tooltip": "______________________"
        },
        "pb_output_exe_version_edit": {
            "display_text": "Create/Edit/Preview ____",
            "tooltip": "______________________"
        },
        "pb_add_file_folder_data": {
            "display_text": "Add file resources ____",
            "tooltip": "______________________"
        },
        "pb_add_binary_data": {
            "display_text": "Add binary resources ____",
            "tooltip": "______________________"
        },
        "pb_collect_submodules": {
            "display_text": "Collect submodules ____",
            "tooltip": "______________________ ____"
        },
        "pb_collect_data": {
            "display_text": "Collect data files ____",
            "tooltip": "______________________"
        },
        "pb_collect_binaries": {
            "display_text": "Collect binary files ____",
            "tooltip": "______________________"
        },
        "pb_collect_all": {
            "display_text": "收集所有模块资源 ____",
            "tooltip": "______________________"
        },
        "pb_add_splash_screen": {
            "display_text": "添加启动画面 ____",
            "tooltip": "______________________"
        },
        "pb_hidden_import": {
            "display_text": "指定模块导入路径 ____",
            "tooltip": "______________________"
        },
        "pb_imports_paths": {
            "display_text": "指定模块搜寻路径 ____",
            "tooltip": "______________________"
        },
        "pb_exclude_module": {
            "display_text": "排除模块 ____",
            "tooltip": "______________________"
        },
        "pb_copy_metadata": {
            "display_text": "复制包的元数据 ____",
            "tooltip": "______________________"
        },
        "pb_recursive_copy_metadata": {
            "display_text": "递归复制包的元数据 ____",
            "tooltip": "______________________"
        },
        "pb_additional_hooks_dir": {
            "display_text": "额外的钩子路径 ____",
            "tooltip": "______________________"
        },
        "pb_runtime_hook": {
            "display_text": "运行时的钩子 ____",
            "tooltip": "______________________"
        },
        "pb_runtime_tmpdir": {
            "display_text": "运行工作路径 ____",
            "tooltip": "______________________"
        },
        "pb_workpath_option": {
            "display_text": "构建时工作目录 ____",
            "tooltip": "______________________"
        },
        "pb_specpath": {
            "display_text": "SPEC 文件生成路径 ____",
            "tooltip": "______________________"
        },
        "pb_upx_dir": {
            "display_text": "UPX 压缩工具路径 ____",
            "tooltip": "______________________"
        },
        "pb_upx_exclude": {
            "display_text": "UPX 排除文件 ____",
            "tooltip": "______________________"
        },
        "pb_log_level": {
            "display_text": "日志级别 ____",
            "tooltip": "______________________"
        },
        "pb_python_option": {
            "display_text": "Python 选项 ____",
            "tooltip": "______________________"
        },
        "pb_debug_mode": {
            "display_text": "调试选项 ____",
            "tooltip": "______________________"
        },
        "pb_target_architecture": {
            "display_text": "指定架构 ____",
            "tooltip": "______________________"
        },
        "pb_codesign_identity": {
            "display_text": "指定代码签名 ____",
            "tooltip": "______________________"
        },
        "pb_osx_bundle_identifier": {
            "display_text": "设置唯一标识符 ____",
            "tooltip": "______________________"
        },
        "pb_osx_entitlements_file": {
            "display_text": "指定 Entitlements 文件 ____",
            "tooltip": "______________________"
        },
        "pb_add_resource": {
            "display_text": "添加额外资源 ____",
            "tooltip": "______________________"
        },
        "pb_add_xml_file": {
            "display_text": "添加清单文件 ____",
            "tooltip": "______________________"
        },
        "pb_save_setting": {
            "display_text": "保存并立即生效 ____",
            "tooltip": "______________________"
        },
        "pb_env_sys_edit_page_setting_env": {
            "display_text": "打开环境变量 ____",
            "tooltip": "______________________"
        },
        "pb_env_specified_browser_page_setting_env": {
            "display_text": "浏览 ____",
            "tooltip": "______________________"
        },
        "pb_env_specified_save_page_setting_env": {
            "display_text": "保存 ____",
            "tooltip": "______________________"
        },
        "pb_launch": {
            "display_text": "运行 ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        # ############################################# [ComboBox] #############################################
        "cb_lock_output_folder": {
            "display_text": "锁定文件夹路径 ____",
            "tooltip": "______________________"
        },
        "cb_lock_output_file_name": {
            "display_text": "锁定文件名 ____",
            "tooltip": "______________________"
        },
        "cb_noupx_option": {
            "display_text": "禁用 UPX 压缩 ____",
            "tooltip": "______________________"
        },
        "cb_disable_traceback": {
            "display_text": "禁用窗口化回溯 ____",
            "tooltip": "______________________"
        },
        "cb_ignore_signals": {
            "display_text": "忽略信号处理 ____",
            "tooltip": "______________________"
        },
        "cb_noconfirm_option": {
            "display_text": "自动确认 ____",
            "tooltip": "______________________"
        },
        "cb_strip_option": {
            "display_text": "去除符号表 ____",
            "tooltip": "______________________"
        },
        "cb_clean_cache": {
            "display_text": "清理缓存 ____",
            "tooltip": "______________________"
        },
        "cb_argv_emulation": {
            "display_text": "启用argv模拟 ____",
            "tooltip": "______________________"
        },
        "cb_uac_admin_apply": {
            "display_text": "申请管理员权限 ____",
            "tooltip": "______________________"
        },
        "cb_uac_uiaccess": {
            "display_text": "申请 UIAccess 权限 ____",
            "tooltip": "______________________"
        },
        "cb_hide_console": {
            "display_text": "隐藏控制台窗口 ____",
            "tooltip": "______________________"
        },
        "cb_delete_build": {
            "display_text": "清除 /build 文件夹 ____",
            "tooltip": "______________________"
        },
        "cb_delete_spec": {
            "display_text": "删除 *.spec 文件 ____",
            "tooltip": "______________________"
        },
        "rb_use_pyinstaller": {
            "display_text": "使用pyinstaller.exe ____",
            "tooltip": "______________________"
        },
        "rb_use_python": {
            "display_text": "使用python解释器 ____",
            "tooltip": "______________________"
        },
        "cbb_tooltip_show": {
            "display_text": "显示 ____",
            "tooltip": "______________________"
        },
        "cbb_multi_win": {
            "display_text": "允许多窗口 ____",
            "tooltip": "______________________"
        },
        "cb_print_cmd_auto_open_folder": {
            "display_text": "Automatically open folders ____",
            "tooltip": "______________________"
        },
        "cb_print_cmd_auto_open_file": {
            "display_text": "Automatically open files ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        # ############################################# [RadioButton] #############################################
        "rb_output_form_folder": {
            "display_text": "文件夹 ____",
            "tooltip": "______________________"
        },
        "rb_output_form_file": {
            "display_text": "文件(exe) ____",
            "tooltip": "______________________"
        },
        "rb_exe_console_display_show": {
            "display_text": "显示 ____",
            "tooltip": "______________________"
        },
        "rb_exe_console_display_hide": {
            "display_text": "不显示/隐藏 ____",
            "tooltip": "______________________"
        },
        "rb_env_sys": {
            "display_text": "使用系统默认环境 ____",
            "tooltip": "______________________"
        },
        "rb_env_specified": {
            "display_text": "使用指定解释器环境 ____",
            "tooltip": "______________________"
        },
        "rb_env_conda": {
            "display_text": "使用 Conda 环境 ____",
            "tooltip": "______________________"
        },
        "rb_env_builtin": {
            "display_text": "使用内置 pyinstaller ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        # ############################################# [Label] #############################################
        "lb_env_current_title_page_base": {
            "display_text": "当前环境 ____",
            "tooltip": "______________________"
        },
        "lb_input_py_file_path": {
            "display_text": "请选择需要打包的 python 脚本入口文件, 支持 *.py, *.pyw, *.pyd, *.spec文件或 *.ocl, *.txt ____",
            "tooltip": "______________________"
        },
        "lb_output_folder_path": {
            "display_text": "请指定输出的文件夹 ____",
            "tooltip": "______________________"
        },
        "lb_output_file_name": {
            "display_text": "请指定输入文件名 ____",
            "tooltip": "______________________"
        },
        "lb_output_exe_icon": {
            "display_text": "(可选) 请添加应用图标 ____",
            "tooltip": "______________________"
        },
        "lb_output_exe_version": {
            "display_text": "(可选) 请添加版本信息 ____",
            "tooltip": "______________________"
        },
        "lb_output_form": {
            "display_text": "打包输出形式 ____",
            "tooltip": "______________________"
        },
        "lb_exe_console_display": {
            "display_text": "显示终端窗口 ____",
            "tooltip": "______________________"
        },
        "lb_language": {
            "display_text": "显示语言 ____",
            "tooltip": "______________________"
        },
        "lb_build_files_clear": {
            "display_text": "执行完打包后 ____",
            "tooltip": "______________________"
        },
        "lb_use_py_pyinstaller_auto_conda": {
            "display_text": "命令行执行方式 ____",
            "tooltip": "______________________"
        },
        "lb_tooltip_show": {
            "display_text": "工具提示 ____",
            "tooltip": "______________________"
        },
        "lb_multi_win": {
            "display_text": "新文件处理 ____",
            "tooltip": "______________________"
        },
        "lb_print_cmd_option": {
            "display_text": "打印完命令行后 ____",
            "tooltip": "______________________"
        },
        "lb_env_current_title_page_setting_env": {
            "display_text": "当前使用环境 ____",
            "tooltip": "______________________"
        },
        "lb_env_current_path_title_page_setting_env": {
            "display_text": "python解释器路径 ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        # ############################################# [GroupBox] #############################################
        "groupBox_ios": {
            "display_text": "IOS系统 ____",
            "tooltip": "______________________"
        },
        "groupBox_windows": {
            "display_text": "Windows系统 ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        # ############################################# [TabWidget] #############################################
        "tabWidget": {
            "tab_common": {
                "display_text": "常规 ____",
                "tooltip": "______________________"
            },
            "tab_env": {
                "display_text": "运行环境 ____",
                "tooltip": "______________________"
            },
            "tab_theme": {
                "display_text": "主题 ____",
                "tooltip": "______________________"
            },
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
        "_________________________": {
            "display_text": "______________________ ____",
            "tooltip": "______________________"
        },
    },
    "special": {
        "window_title": "Python packaging to executable (.exe) development tools",
        "print_cmd": "The execution of the PyInstaller command has been completed.<br>The output command file is located at:",
        "open_output_folder": {
            "no_file": "No processing files found. Please select processing files first",
            "no_folder": "The specified output folder does not exist. Please make a new selection."
        },
        "select_py_file": {
            "text_browser_display": "Python script path:",
            "dialog_title": "Please select Python script",
            "type_discription": "Python script (*.py)"
        },
        "select_ourput_folder": {
            "text_browser_display": "Output path of the .exe file",
            "dialog_title": "Please select output folder"
        },
        "type_select_dialog": {
            "msg_title": "Choose the data type to add",
            "msg_content": "Add file or folder? "
        },
        "launch_cmd": {
            "msg_content_no_file": "Specified Python script not found. Please select a .py file again.",
            "msg_content_no_folder": "Output folder does not exist. Please specify a valid output folder.",
            "msg_content_nolaunch": "Conversion not possible\n\nCurrently a file is already being converted.\n\nPlease wait a moment",
            "text_browser_display": "Successfully packaged Python script"
        },
        "pb_package_view": {
            "text": "view the installed packages",
            "tooltip": "Viewing the list of Python libraries installed in the currently selected Conda environment."
        },
        "lb_env_name": {
            "text_init": "Please select the Conda environment",
            "text": "Conda environment: \t"
        },
        "lb_env_path": {
            "text_init": "Path to the current Conda environment",
            "text": "Environment path: \t"
        }
    },
    "UIString": {
        "error": "Error",
        "setting_update": "Update setting: ",
        "display_command_parameter": "display parameter",
        "all_parameter": "All valid parameters",
        "msg_info": "Hint",
        "msg_warning": "Warning",
        "pb_add": "Add",
        "pb_remove": "Remove",
        "pb_certain": "Confirm",
        "pb_cancel": "Cancel",
        "pb_replace": "Replace",
        "pb_reset": "Reset",
        "pb_set": "setting",
        "pb_change": "Change",
        "folder": "folder",
        "file": "file",
        "select_folder": "Please select folder",
        "select_file": "Please select file",
        "type_all_files": "All files",
        "input_specified_data": "Please enter specified information",
        "specified_info": "Specify information",
        "redundant_info": "Do not add data repeatedly",
        "data_exist": "data existed",
        "optional_option": "Optional actions",
        "current_data": "current: ",
        "all_image_file": "All pictures",
        "image_file": "pic",
        "icon": "icon",
        "application": "Application",
        "text_file": "text file",
        "or": " or ",
        "msg_file_replace": "Would you want to replace the original file option path",
        "msg_item_replace": "Would you want to replace the original option",
        "msg_if_replace": "Would you want to replace",
        "deleted_file": "Remaining files deleted",
        # ############################################# [Others] #############################################
        "reset": "重置 ____",
        "cancel": "取消 ____",
        "certain": "确定 ____",
        "error": "错误 ____",
        "warning": "警告 ____",
        "info": "信息 ____",
        "critical": "严重错误 ____",
        "copied": "已复制 ____",
        "command_printed": "命令行已打印到",
        "command_empty": "Pyinstaller 命令为空",
        "env_conda_table_header": ["环境名 ____", "版本号 ____", "Python解释器路径 ____", "Pyinstaller路径 ____", "Pyinstaller版本 ____"],
        "pyinstaller_info_table_header": ["命令名称 ____", "命令选项 ____", "命令值 ____"],
        "output_folder_not_exist": "输出文件夹不存在 ____",

    }
}
