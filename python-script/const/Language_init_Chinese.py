LANGUAGE_INIT_CHINESE = {
  "widgets": {
    "pb_Enviroment": {
      "tooltip": "该选项可直接打开环境变量, \n用于确定进行打包操作的python解释器版本",
      "text": "环境变量"
    },
    "pb_CondaSetting": {
      "tooltip": "可通过该控件设置打包使用Conda环境\n, 注意: 如果未安装Conda或未将Conda添加进环境变量, \n则无法使用该按钮, 请检查Conda的安装",
      "text": "Conda设置"
    },
    "pb_FilePath": {
      "tooltip": "浏览Python脚本路径, 默认为当前目录下的main.py文件路径",
      "text": "浏览"
    },
    "pb_OutputPath": {
      "tooltip": "浏览输出路径, 该路径可能包含.spec, /build, /dict或.exe",
      "text": "浏览"
    },
    "pb_Recover": {
      "tooltip": "该功能仅能恢复最后一次清除输入或清除全部前的选项内容\n请谨慎操作! ",
      "text": "恢复"
    },
    "pb_ClearAll": {
      "tooltip": "清空全部内容, 包含控制台信息、信息台信息、当前输入的选项内容\n为防止误操作, 可通过恢复按钮来恢复数据\n请谨慎操作! ",
      "text": "全部清空"
    },
    "pb_ClearConsole": {
      "tooltip": "将清空控制台显示的信息",
      "text": "清空控制台显示"
    },
    "pb_ClearInfo": {
      "tooltip": "将清空信息台显示的信息",
      "text": "清空信息台显示"
    },
    "pb_ClearAllDisplay": {
      "tooltip": "将清空全部显示信息, 包含控制台及信息台",
      "text": "清空全部显示"
    },
    "pb_ClearInput": {
      "tooltip": "将清空当前输入选项内容\n为防止误操作, 可通过恢复按钮来恢复数据\n请谨慎操作! ",
      "text": "清空输入",
      "msg_content": "您当前正在执行清空输入的操作, 确认清空吗？<br><br>恢复功能只能恢复最后一次清空输入前的数据输入<br>连续两次清空输入将无法恢复此前的数据输入",
      "pb_certain_clear": "确认清空"
    },
    "pb_ShowParameter": {
      "tooltip": "将显示已输入的所有有效参数",
      "text": "显示参数"
    },
    "pb_OpenDir": { "tooltip": "将打开输出文件夹", "text": "打开输出文件夹" },
    "pb_Print": {
      "tooltip": "将打印command命令行命令到output_command_of_pyinstaller.txt",
      "text": "打印cmd执行命令"
    },
    "pb_Launch": { "tooltip": "开始进行打包操作", "text": "开始执行转换" },
    "pb_SetupPyinstaller": {
      "tooltip": "安装Pyinstaller",
      "text": "安装Pyinstaller",
      "text_browser_display":"已成功安装pyinstaller"
    },
    "pb_VersionDisplay": {
      "tooltip": "在控制台中显示Pyinstaller版本信息",
      "text": "pyinstaller版本",
      "text_browser_display": "已显示Pyinstaller版本信息",
      "text_browser_cmd_display": "当前pyinstaller的版本信息"
    },
    "pb_HelpDisplay": {
      "tooltip": "在控制台中显示Pyinstaller的帮助信息",
      "text": "pyinstaller帮助",
      "text_browser_display": "已显示Pyinstaller帮助信息",
      "text_browser_cmd_display": "以上为pyinstaller的帮助信息"
    },
    "pb_AddBinaryData": {
      "tooltip": "[可重复使用]\n用于将二进制文件添加到生成的可执行文件中. \n该选项允许将外部二进制文件嵌入到生成的可执行文件中, 以便在运行时可以访问这些文件. \n请注意, 当前被打包的py文件须在根文件夹中, 添加的文件资源须在根文件夹下",
      "text": "添加二进制资源",
      "dict": "\n添加二进制资源: \t",
      "text_browser_display": "更新二进制文件",
      "dialog_title": "请选择用于添加到可执行文件中的二进制文件"
    },
    "pb_AddFileFolderData": {
      "tooltip": "[可重复使用]\n用于添加数据文件到可执行文件中的选项. \n它允许将指定的文件或目录复制到生成的可执行文件所在的目录中. \n这对于包含资源文件(如图像、配置文件等)在可执行文件中是很有用的. ",
      "text": "添加文件资源",
      "dict": "\n添加文件资源: \t",
      "text_browser_display": "更新用于添加到可执行文件中的文件",
      "dialog_title": "请选择用于添加到可执行文件中的文件"
    },
    "pb_AddIcon": {
      "tooltip": "[可重复使用]\n添加应用图标,但任务栏的图标请在py文件中自行添加. ",
      "text": "添加应用图标",
      "dict": "\n应用图标路径: \t",
      "text_browser_display": "更新应用图标",
      "dialog_title": "请选择用于作为应用图标的icon图标"
    },
    "pb_AdditionalHooksDir": {
      "tooltip": "[可重复使用]\n用于指定一个目录, 其中包含用户提供的钩子脚本. \n这些钩子脚本用于告诉 PyInstaller 如何处理特定的模块或库, \n以确保它们正确地包含在生成的可执行文件中. ",
      "text": "钩子文件夹路径",
      "dict": "\n添加指定的钩子文件夹路径: \t",
      "text_browser_display": "更新钩子脚本搜索目录",
      "dialog_title": "请选择钩子脚本所在目录"
    },
    "pb_AddResource": {
      "tooltip": "[可重复使用] 用于将文件或目录嵌入到生成的可执行文件中, 以供运行时访问. \nRESOURCE是一个到四个项, FILE[,TYPE[,NAME[,LANGUAGE]]]. FILE可以是数据文件或exe/dll文件. \n对于数据文件, 必须至少指定TYPE和NAME. LANGUAGE默认为0, 或可以指定为通配符以更新给定TYPE和NAME的所有资源. \n对于exe/dll文件, 如果省略了TYPE、NAME和LANGUAGE, 或将它们指定为通配符, 则会将FILE中的所有资源添加/更新到最终的可执行文件中. ",
      "text": "添加资源(可指定)",
      "dict": "\n添加嵌入exe中的文件或目录: \t",
      "msg_content": "请选择需要嵌入可执行文件的数据的指定信息, 格式如下: <br>'格式,名称,语言'(其中逗号','必须为英文逗号)<br><br>格式: 资源的类型, 通常是一个 MIME 类型, 例如 'text/plain'<br> 名称: 在可执行文件中嵌入的资源的名称<br>语言: 资源的语言,通常是一个整数或字符串, 表示资源所属的语言. 在 Windows 系统上, 语言代码通常是一个四位的十进制数, 例如 1033 表示英语(美国). <br>在其他系统上, 可能使用标准的 IETF BCP 47 语言标签<br><br>示例: <br>image/png,app_data,1033<br>,,1033<br>,app_data<br><br>若无此需要, 则按回车或点击“OK”即可<br>",
      "text_browser_display": "更新嵌入到生成的可执行文件中的文件或目录",
      "dialog_title": "请选择输入数据类型, 以用于将其嵌入到生成的可执行文件中"
    },
    "pb_AddSplashScreen": {
      "tooltip": "将 IMAGE_FILE 图像添加为应用程序的启动画面",
      "text": "添加启动画面",
      "dict": "\n应用程序的启动画面: \t",
      "text_browser_display": "添加应用启动画面",
      "dialog_title": "请选择启动画面"
    },
    "pb_AddXmlFile": {
      "tooltip": "将文件FILE或XML的清单添加到exe文件. ",
      "text": "添加FILE或XML",
      "dict": "\n添加文件或XML资源: \t",
      "text_browser_display": "添加FILE文件或XML文件",
      "dialog_title": "请选择添加到exe的FILE或XML文件"
    },
    "pb_ImportsFolder": {
      "tooltip": "[可重复使用] 用于指定导入模块时的搜索路径, 可多次调用. \n通过这个选项可以将额外的目录添加到 Python 模块搜索路径中, \n以确保程序在运行时能够找到需要的模块. \n这个选项可以帮助解决程序在运行时找不到特定模块的问题, \n尤其是当输出应用程序依赖于一些不在默认搜索路径中的自定义模块时",
      "text": "搜索import路径",
      "dict": "\n搜索import模块路径: \t",
      "text_browser_display": "更新导入模块时的搜索路径",
      "dialog_title": "请选择指定 Python 模块搜索路径"
    },
    "pb_ImportModuleName": {
      "tooltip": "[可重复使用] 用于指定需要在生成的可执行文件中包含的未在源代码中显式导入的 Python 模块. \n有时一些模块可能是在运行时动态导入或被其他模块隐式地导入, \n而不是在源代码中显式导入. 此选项可以使用多次. ",
      "text": "引用外部指定import",
      "dict": "\n引用外部指定import模块名: \t",
      "text_browser_display": "更新显式导入的Python模块",
      "dialog_title": "请输入外部import的模块名称",
      "sub_dialog_title": "请输入需要从外部import的模块名称:",
      "sub_dialog_content": "用于指定需要在生成的可执行文件中包含的未在源代码中显式导入的 Python 模块"
    },
    "pb_VersionFile": {
      "tooltip": "用于指定一个包含版本信息的文件. \n这个版本文件通常包含应用程序的版本号、公司信息等",
      "text": "添加版本资源",
      "dict": "\n添加版本资源: \t",
      "text_browser_display": "添加应用版本信息文件",
      "dialog_title": "请选择应用版本信息文件"
    },
    "pb_CollectSubmodules": {
      "tooltip": "[可重复使用] 用于在打包过程中显式地收集指定模块及其所有子模块. \n该选项可用于确保 PyInstaller 包含指定模块及其子模块, \n即使它们没有在源代码中被显式导入",
      "text": "打包模块及子模块",
      "dict": "\n打包及本身及其所有子模块的模块: \t",
      "text_browser_display": "更新打包过程中显式地收集指定模块及其所有子模块",
      "dialog_title": "请输入模块名称",
      "sub_dialog_title": "请输入模块名称:",
      "sub_dialog_content": "用于在打包过程中显式地收集指定模块及其所有子模块"
    },
    "pb_CopyMetadata": {
      "tooltip": "[可重复使用] 用于在打包过程中将指定模块的元数据一起复制到生成的可执行文件中",
      "text": "复制模块元数据",
      "dict": "\n打包元数据的模块: \t",
      "text_browser_display": "更新打包过程中将指定模块的元数据",
      "dialog_title": "请输入模块名称",
      "sub_dialog_title": "请输入需要打包元数据的模块名称",
      "sub_dialog_content": "用于在打包过程中将指定模块的元数据一起复制到生成的可执行文件中"
    },
    "pb_RecursiveCopyMetadata": {
      "tooltip": "[可重复使用] 用于在打包过程中递归地将指定包及其依赖的所有包的元数据一起复制到生成的可执行文件中. \n这样不仅包本身的元数据会被复制, 还会包括其依赖项的元数据. ",
      "text": "复制模块元数据\n并包含依赖项",
      "dict": "\n打包本身及其所有依赖项元数据的模块: \t",
      "text_browser_display": "更新打包过程中递归地将指定包及其依赖的所有包的元数据",
      "dialog_title": "请输入模块名称",
      "sub_dialog_title": "请输入需要打包元数据及其依赖的模块名称:",
      "sub_dialog_content": "用于在打包过程中递归地将指定包及其依赖的所有包的元数据一起复制到生成的可执行文件中. <br>这样不仅包本身的元数据会被复制, 还会包括其依赖项的元数据. "
    },
    "pb_CollectData": {
      "tooltip": "[可重复使用] 用于在打包过程中收集指定模块的数据文件. \n这个选项用于确保 PyInstaller 包含指定模块所需的数据文件, \n这些数据文件可能在运行时由模块动态加载. ",
      "text": "打包模块数据文件",
      "dict": "\n打包所有数据的模块: \t",
      "text_browser_display": "更新打包过程中收集指定模块的数据文件",
      "dialog_title": "请输入模块名称",
      "sub_dialog_title": "请输入需要打包数据的模块名称:",
      "sub_dialog_content": "用于在打包过程中收集指定模块的数据文件. <br>这个选项用于确保 PyInstaller 包含指定模块所需的数据文件, 这些数据文件可能在运行时由模块动态加载. "
    },
    "pb_CollectAll": {
      "tooltip": "[可重复使用] 用于在打包过程中收集指定模块及其依赖的所有数据文件、元数据等. \n这个选项的作用是尽可能地将指定模块及其相关的所有资源都包含在生成的可执行文件中. ",
      "text": "打包模块所有数据",
      "dict": "\n打包所有数据的模块: \t",
      "text_browser_display": "更新打包过程中收集指定模块及其依赖的所有数据文件、元数据等",
      "dialog_title": "请输入模块名称",
      "sub_dialog_title": "请输入需要打包所有数据的模块名称:",
      "sub_dialog_content": "用于在打包过程中收集指定模块及其依赖的所有数据文件、元数据等. <br>这个选项的作用是尽可能地将指定模块及其相关的所有资源都包含在生成的可执行文件中. "
    },
    "pb_CollectBinaries": {
      "tooltip": "[可重复使用] 用于在打包过程中收集指定模块及其依赖的所有二进制文件. \n这个选项的作用是将模块及其相关的二进制文件包含在生成的可执行文件中. ",
      "text": "打包模块二进制文件",
      "dict": "\n打包模块的所有二进制文件: \t",
      "text_browser_display": "更新打包过程中收集指定模块及其依赖的所有二进制文件",
      "dialog_title": "请输入模块名称",
      "sub_dialog_title": "请输入需要打包二进制文件的模块名称:",
      "sub_dialog_content": "用于在打包过程中收集指定模块及其依赖的所有二进制文件. <br>这个选项的作用是将模块及其相关的二进制文件包含在生成的可执行文件中. "
    },
    "pb_RuntimeHook": {
      "tooltip": "[可重复使用] 用于指定运行时的钩子脚本. \n这个选项允许你提供一个脚本, 其中包含在生成的可执行文件运行时应该执行的特定操作. ",
      "text": "钩子文件路径",
      "dict": "\n添加运行时钩子文件的路径: \t",
      "text_browser_display": "更新运行时的钩子脚本路径",
      "dialog_title": "请选择钩子脚本"
    },
    "pb_TargetArchitecture": {
      "tooltip": "用于指定生成的可执行文件的目标架构. \n该选项允许你选择生成 32 位(x86)或 64 位(x86_64)的可执行文件. 仅MacOs",
      "text": "指定架构",
      "dict": "\n目标架构: \t",
      "text_browser_display": "请选择目标架构",
      "dialog_title": "请选择目标架构<br>默认情况下, PyInstaller 会尝试根据系统架构选择合适的目标架构. "
    },
    "pb_CodesignIdentity": {
      "tooltip": "用于在 macOS 平台上对生成的应用程序进行代码签名. \n代码签名是一种在应用程序上附加数字签名的方法, 用于验证应用程序的来源和完整性. \n使用提供的身份对收集的二进制文件和生成的可执行文件进行签名. \n如果未提供签名身份, 则执行 ad-hoc 签名. ",
      "text": "代码签名",
      "dict": "\n代码签名: \t",
      "text_browser_display": "请输入代码签名",
      "dialog_title": "用于在 macOS 平台上对生成的应用程序进行代码签名. <br>代码签名是一种在应用程序上附加数字签名的方法, 用于验证应用程序的来源和完整性. <br>使用提供的身份对收集的二进制文件和生成的可执行文件进行签名. <br>如果未提供签名身份, 则执行 ad-hoc 签名. "
    },
    "pb_OsxEntitlementsFile": {
      "tooltip": "用于指定 macOS 平台上生成的应用程序的 entitlements 文件. \nEntitlements 文件包含了应用程序运行所需的权限和系统服务的详细信息. ",
      "text": "添加签名文件",
      "dict": "\n二进制授权文件(entitlements文件): \t",
      "text_browser_display": "添加entitlements文件",
      "dialog_title": "请选择entitlements文件"
    },
    "pb_ExcludeModule": {
      "tooltip": "[可重复使用] 用于指定要在打包过程中排除的模块. \n这个选项允许你明确指定哪些模块不应该被包含在生成的可执行文件中. \n注意是Python 名称, 而不是路径名称",
      "text": "需忽略的可选模块",
      "dict": "\n要忽略的可选模块或包: \t",
      "text_browser_display": "更新需要忽略的可选模块",
      "dialog_title": "请输入模块名称",
      "sub_dialog_title": "请输入需要忽略的可选模块名称:",
      "sub_dialog_content": "用于指定要在打包过程中排除的模块. <br>这个选项允许你明确指定哪些模块不应该被包含在生成的可执行文件中. "
    },
    "pb_UpxExclude": {
      "tooltip": "[可重复使用]  UPX 压缩过程中要排除的文件. \nUPX是一种用于可执行文件的压缩工具, 而 --upx-exclude 允许你指定一些文件不要被UPX压缩. ",
      "text": "upx压缩",
      "dict": "\nupx压缩排除文件: \t",
      "text_browser_display": "添加在UPX压缩过程中要排除的文件",
      "dialog_title": "请选择在UPX压缩过程中要排除的文件"
    },
    "pb_UpxDir": {
      "tooltip": "用于指定 UPX 压缩工具的目录路径. \nUPX 是一种可执行文件压缩工具, 用于减小生成的可执行文件的大小. ",
      "text": "UPX_DIR路径",
      "dict": "\nupx工具路径: \t",
      "text_browser_display": "添加指定UPX压缩工具的目录路径",
      "dialog_title": "请选择文件夹, 用于指定 UPX 压缩工具的目录路径"
    },
    "pb_LogLevel": {
      "tooltip": "用于设置 PyInstaller 的日志输出级别. \nPyInstaller 使用不同的日志级别来记录构建过程中的各种信息, 包括警告、错误和调试信息. ",
      "text": "控制台详细程度",
      "dict": "\n控制台消息详细程度: \t",
      "text_browser_display": "日志输出级别",
      "current_level": "当前日志输出级别: ",
      "dialog_title": "请选择Pyinstaller的日志输出级别: ",
      "trace_translate": "(跟踪)",
      "debug_translate": "(调试)",
      "info_translate": "(信息)",
      "warn_translate": "(警告)",
      "deprecation_translate": "(弃用警告)",
      "error_translate": "(错误)",
      "fatal_translate": "(严重错误)"
    },
    "pb_RuntimeTmpdir": {
      "tooltip": "用于提取库和支持文件的目录. \n在运行过程中, PyInstaller 生成的可执行文件可能需要创建临时文件或缓存一些数据. \n该选项允许用户指定用于存储这些临时文件的目录\n注意: 1. 这个选项通常在需要修改临时文件存储位置的特殊情况下使用.  \n2. 在某些环境下, 默认的临时目录可能不适用, 或者希望将临时文件保存在特定的目录中时, 可以考虑使用这个选项.  \n3. 如果没有特殊要求, 通常情况下无需手动设置. PyInstaller 会在运行时使用系统默认的临时目录",
      "text": "提取库和支持文件的目录",
      "dict": "\n提取库和支持文件的目录: \t",
      "msg_info": "该选项只能在“输出为文件夹”模式下使用",
      "text_browser_display": "添加提取库和支持文件的目录",
      "dialog_title": "请选择文件夹, 用于指定提取库和支持文件的目录"
    },
    "pb_WorkpathOption": {
      "tooltip": "用于指定 PyInstaller 在构建过程中使用的工作目录. \n工作目录是 PyInstaller 用于临时存储构建过程中的中间文件和临时文件的地方. \n临时工作文件的位置, 包括 .log, .pyz 等文件(默认为 ./build)",
      "text": "临时工作文件位置",
      "dict": "\n临时工作文件位置: \t",
      "text_browser_display": "添加临时工作文件的位置",
      "dialog_title": "请选择文件夹, 用于指定 PyInstaller 在构建过程中使用的工作目录"
    },
    "pb_DebugMode": {
      "tooltip": "用于设置调试模式, 以便在打包过程中生成调试信息\nall, imports, bootloader, noarchive",
      "text": "设置调试模式",
      "dict": "\n调试模式: \t",
      "text_browser_display": "调试模式",
      "current_level": "当前调试模式: ",
      "dialog_title": "请选择调试模式: ",
      "all_translate": "(全部)",
      "imports_translate": "(导入)",
      "bootloader_translate": "(引导加载程序)",
      "noarchive_translate": "(警无存档告)"
    },
    "pb_PythonOption": {
      "tooltip": "python解释器命令行选项\n 用于向底层的 Python 解释器传递额外的命令行选项. \n该选项允许你在 PyInstaller 执行过程中向 Python 解释器传递特定的选项, 以影响解释器的行为. \n目前支持 'v'(相当于 '--debug imports')、'u' 和 'W <warning control>'",
      "text": "解释器命令行选项",
      "dict": "指定Python解释器的命令行: \t",
      "text_browser_display": "Python解释器命令行选项",
      "current_level": "当前命令行选项: ",
      "dialog_title": "请选择命令行选项: ",
      "dialog_content": "v: 相当于--debug imports, 启用详细的导入调试信息, 有助于识别导入模块时的问题<br>u: 通常用于非常规的用户自定义启动方式<br>W:  <warning control>允许传递警告控制参数, 该参数控制Python解释器中警告的行为",
      "parameter": "参数"
    },
    "pb_HideConsole": {
      "tooltip": "设置可执行程序运行时, 控制台的显示方式\nminimize-late: 在运行时尽可能晚地最小化控制台窗口\nhide-early: 在运行时尽可能早地隐藏控制台窗口\nminimize-early: 在运行时尽可能早地最小化控制台窗口\nhide-late: 在运行时尽可能晚地隐藏控制台窗口",
      "text": "控制台显示方式",
      "dict": "\n控制台窗口的显示方式: \t",
      "text_browser_display": "控制台窗口的显示方式",
      "current_level": "控制台窗口的显示方式: ",
      "dialog_title": "请选择可执行文件的控制台窗口的显示方式: ",
      "dialog_content": "minimize-late: 在运行时尽可能晚地最小化控制台窗口. <br>hide-early: 在运行时尽可能早地隐藏控制台窗口. <br>minimize-early: 在运行时尽可能早地最小化控制台窗口. <br>hide-late: 在运行时尽可能晚地隐藏控制台窗口. ",
      "minimize_late_translate": "(最小化延迟)",
      "hide_early_translate": "(提前隐藏)",
      "minimize_early_translate": "(最小化提前)",
      "hide_late_translate": "(延迟隐藏)"
    },
    "pb_OsxBundleIdentifier": {
      "tooltip": "用于在 macOS 平台上设置生成的应用程序的 Bundle Identifier. \nBundle Identifier 是用于唯一标识 macOS 应用程序的字符串, 通常采用逆序域名的形式. ",
      "text": "Bundle Identifier",
      "dict": "\nBundle Identifier: \t",
      "dialog_title": "请输入Bundle Identifier",
      "dialog_content": "添加用于在macOS平台上设置生成的应用程序的Bundle Identifier. <br>Bundle Identifier是用于唯一标识macOS应用程序的字符串, 通常采用逆序域名的形式. <br>例如: com.mycompany.department.appname(默认值: 第一个脚本的basename)"
    },
    "pb_Specpath": {
      "tooltip": "用于指定生成的 spec 文件的保存路径. \nSpec 文件是 PyInstaller 构建过程中生成的中间文件, \n它描述了构建配置的详细信息, 包括输入脚本、依赖项、输出路径等. ",
      "text": "spec文件路径",
      "dict": "\n.spec的文件夹: \t",
      "msg_replace": "是否替换原文件选项路径",
      "select_folder_text_browser": "添加spec文件的保存路径",
      "select_folder_win_title": "请选择spec文件的保存路径"
    },
    "cb_CondaUse": {
      "tooltip": "当已经设置了Conda设置后, 该项会自动勾选, \n取消勾选即可使用系统中python解释器环境",
      "text": "使用Conda环境"
    },
    "cb_Tooltips": {
      "tooltip": "该选项勾选后, 当鼠标悬停时, 会出现工具提示",
      "text": "显示工具提示"
    },
    "cb_PathLock": {
      "tooltip": "该项被勾选时, 输出路径将不再随py脚本路径自动更改",
      "text": "锁定"
    },
    "cb_NameLock": {
      "tooltip": "该项被勾选时, 输出文件名称将不再随py脚本名称自动更改",
      "text": "锁定"
    },
    "cb_DisableWindowed": {
      "tooltip": "禁用窗口化. \n用于在 windowed 模式下禁用异常追踪信息的显示. \n在默认情况下, 如果程序在 windowed 模式下崩溃, PyInstaller 会显示一个包含详细异常追踪信息的窗口. \n使用该选项后, 如果程序崩溃, 用户将不再看到详细的异常信息窗口, \n尤其是在发布产品时, 该选项可能有助于提高程序的安全性",
      "text": "禁用窗口化",
      "dict": "\n禁用窗口化: \t",
      "dict_explain": "已禁用窗口化"
    },
    "cb_UacAdminApply": {
      "tooltip": "用于在生成的可执行文件上启用 User Account Control(UAC)管理员权限. \n在使用该选项时, 用户在运行程序时可能会收到 UAC 提示, 需要提供管理员权限, \n同时强制用户在以管理员身份运行可执行文件时提供管理员凭据, \n否则程序将无法启动",
      "text": "申请管理员权限",
      "dict": "\n申请管理员权限: \t",
      "dict_explain": "申请"
    },
    "cb_IgnoreSignals": {
      "tooltip": "引导加载程序忽略信号, 而不是将它们转发给子进程. \n在诸如监督进程向引导加载程序和子进程(例如通过进程组)发送信号以避免向子进程发出两次信号的情况下很有用. ",
      "text": "忽略特定信号",
      "dict": "\n引导加载程序忽略信号: \t",
      "dict_explain": "忽略信号"
    },
    "cb_UacUiaccess": {
      "tooltip": "用于在生成的可执行文件中启用 UIAccess, 以便程序能够在用户交互桌面(UIAccess Desktop)上运行. 但要注意: \n1.这个选项仅在 Windows 上生效. \n2.程序需要具有管理员权限(通常需要 UAC 提示)才能启用 UIAccess. \n3.这个选项可能会导致程序在运行时需要管理员权限. ",
      "text": "允许远程桌面使用",
      "dict": "\n允许远程桌面使用: \t",
      "dict_explain": "允许"
    },
    "cb_ArgvEmulation": {
      "tooltip": "为macOS应用程序包启用argv仿真. \n如果启用, 则启动加载器将处理初始的打开文档/URL事件, 并将传递的文件路径或URL附加到sys.argv. \n用于在生成的可执行文件中启用命令行参数(sys.argv)的模拟. \n默认情况下, PyInstaller 生成的可执行文件在运行时可能无法正确接收命令行参数. \n使用该选项可以解决一些在 Windows 上的问题, 确保 PyInstaller 生成的可执行文件能够正确处理命令行参数. 但应注意: \n1. 这个选项主要针对 Windows 平台. \n2. 在一些情况下, 特别是在 Windows 上, PyInstaller 生成的可执行文件可能无法正确接收命令行参数. 这个选项旨在解决这类问题. \n3. 请确保了解输出应用程序是否受影响, 如果不受影响, 则无需使用这个选项. ",
      "text": "启用argv仿真",
      "dict": "\nmacOS启用argv仿真: \t",
      "dict_explain": "启用"
    },
    "cb_NoupxOption": {
      "tooltip": "用于在打包过程中禁用 UPX 压缩. \nUPX是一种用于可执行文件的压缩工具, 可以显著减小可执行文件的大小.  \n即使可用, 也不要使用UPX(在 Windows 和 *nix 之间工作方式不同)",
      "text": "禁用UPX",
      "dict": "\n使用upx压缩: \t",
      "dict_explain": "禁用 UPX 压缩",
      "msg_content": "UPX是一种用于可执行文件的压缩工具, 可以显著减小可执行文件的大小<br><br>但即使可用, 也不要使用 UPX(在 Windows 和 *nix 之间工作方式不同)"
    },
    "cb_NoconfirmOption": {
      "tooltip": "用于在构建可执行文件时默认选择“是”以避免询问用户任何确认问题. \n该选项可用于自动化构建过程, 以防止在构建期间需要手动确认. ",
      "text": "输出目录确认",
      "dict": "\n替换输出目录询问: \t",
      "dict_explain": "默认输出目录(默认为 SPECPATH/dist/SPECNAME), 不需要确认"
    },
    "cb_ClearCache": {
      "tooltip": "在构建之前清理 PyInstaller 缓存并删除临时文件",
      "text": "清理临时文件",
      "dict": "\n清理缓存: \t",
      "dict_explain": "清理"
    },
    "cb_ClearFileAfterLaunchFlagChange": {
      "tooltip": "当打包操作结束后, 其他用于打包的临时文件将被删除, 包括.spec、/build、/dict, 仅留.exe文件",
      "text": "结束后仅保留exe"
    },
    "cb_StripOption": {
      "tooltip": "对可执行文件和共享库应用符号表剥离(不建议在 Windows上使用). \n用于在打包过程中去除生成的可执行文件中的调试信息. \n调试信息包含了与源代码的关联信息, 去除它们可以减小生成的可执行文件的大小. ",
      "text": "共享库应用符号表剥离",
      "dict": "\n对可执行文件和共享库应用符号表剥离: \t",
      "dict_explain": "剥离共享应用符号表"
    },
    "cb_SplashAutoFile":{
        "tooltip":"勾选后将自动生成SplashModule.py文件, \n并在在主函数中加入导入, 避免启动画面在启动后不自动关闭",
        "text": "自动配置启动画面配置"
    },
    "cb_MultiWin":{
        "tooltip":"勾选后, 当处理多个py文件转换时, 使用多个窗口. 未勾选则是每次只可处理一个py文件, 可通过右键打开文件自动定位",
        "text": "多窗口"
    },
    "rb_OutputMethod_F": {
      "tooltip": "创建一个单文件的可执行文件",
      "text": "输 出 文 件",
      "dict": "\n输出方式: \t",
      "dict_explain": "生成单个文件"
    },
    "rb_OutputMethod_D": {
      "tooltip": "创建包含可执行文件的一个文件夹束",
      "text": "输 出 文 件 夹",
      "dict": "\n输出方式: \t",
      "dict_explain": "生成文件夹"
    },
    "contents_directory": {
      "dict": "\n除exe外, 输出的其他数据的存入路径: \t",
      "msg_content": "是否指定输出文件夹<br>除了可执行文件本身之外的所有内容都将被放入其中",
      "dialog_title": "请输入文件夹名称",
      "dialog_content": "请输入文件夹名称, 用于放置除.exe外的其他数据"
    },
    "rb_ConsoleWindowControl_C": {
      "tooltip": "打开控制台窗口",
      "text": "打开控制台(标准)",
      "dict": "\n控制台窗口: \t",
      "dict_explain": "打开控制台窗口(console)"
    },
    "rb_ConsoleWindowControl_NW": {
      "tooltip": "打开控制台窗口",
      "text": "打开控制台",
      "dict": "\n控制台窗口: \t",
      "dict_explain": "打开控制台窗口(nowindowed)"
    },
    "rb_ConsoleWindowControl_W": {
      "tooltip": "隐藏控制台窗口",
      "text": "隐藏控制台(标准)",
      "dict": "\n控制台窗口: \t",
      "dict_explain": "关闭控制台窗口(windowed)"
    },
    "rb_ConsoleWindowControl_NC": {
      "tooltip": "隐藏控制台窗口",
      "text": "隐藏控制台",
      "dict": "\n控制台窗口: \t",
      "dict_explain": "关闭控制台窗口(console)"
    },
    "lb_Title": { "text": "Python 转 exe" },
    "lb_FilePath": { "text": "文件路径:" },
    "lb_OutputPath": { "text": "输出路径:" },
    "lb_FileName": { "text": "输出文件名: " },
    "lb_CondaTitle": { "text": "当前为: "},
    "pte_FilePath": { "dict": "\nPython脚本: \t" },
    "pte_OutputPath": { "dict": "\n输出目录: \t" },
    "pte_FileName": { "dict": "\n输出名称: \t" }
  },
  "special": {
    "window_title": "Python 打包转换为可执行程序.exe 开发工具",
    "print_cmd": "pyinstaller执行命令已完成打印<br>输出命令文件位于: ",
    "open_output_folder": {
      "no_file": "无处理文件, 请先选择处理文件",
      "no_folder": "不存在指定输出文件夹, 请重新选择"
    },
    "select_py_file": {
      "text_browser_display": "Python文件路径:",
      "dialog_title": "请选择Python文件",
      "type_discription": "Python文件 (*.py)"
    },
    "select_ourput_folder": {
      "text_browser_display": "输出.exe文件路径",
      "dialog_title": "请选择输出文件夹"
    },
    "type_select_dialog": {
      "msg_title": "选择添加数据类型",
      "msg_content": "添加文件还是文件夹？"
    },
    "launch_cmd": {
      "msg_content_no_file": "不存在指定Python脚本, 请重新选择.py文件",
      "msg_content_no_folder": "不存在输出文件夹, 请重新指定输出文件夹",
      "msg_content_nolaunch":"不可进行转换\n\n当前已有文件正在被执行转换\n\n请稍后",
      "text_browser_display":"已完成Python脚本的打包"
    },
    "pb_package_view":{
        "text":"查看环境中已安装包列表",
        "tooltip":"可查看当前选中的Conda环境中\n已经安装的python库的列表"
        },
    "lb_env_name": { 
        "text_init": "请选择Conda环境",
        "text":"Conda环境: \t"
        },
    "lb_env_path": { 
        "text_init": "当前Conda环境的路径",
        "text":"环境路径: \t"
        }
  },
  "general": {
    "error": "错 误",
    "setting_update": "更新设置: ",
    "display_command_parameter": "显 示 命 令 参 数",
    "all_parameter": "全 部 有 效 参 数",
    "msg_info": "提示",
    "msg_warning": "警告",
    "pb_add": "添加",
    "pb_remove": "移除",
    "pb_certain": "确定",
    "pb_cancel": "取消",
    "pb_replace": "替换",
    "pb_reset": "重置",
    "pb_set": "设置",
    "pb_change": "更改",
    "folder": "文件夹",
    "file": "文件",
    "select_folder": "请选择文件夹",
    "select_file": "请选择文件",
    "type_all_files": "所有文件",
    "input_specified_data": "请输入指定信息",
    "specified_info": "指定信息",
    "redundant_info": "请勿重复添加数据",
    "data_exist": "数据已存在",
    "optional_option": "可选操作",
    "current_data": "当前为: ",
    "all_image_file": "所有图片",
    "image_file": "图片",
    "icon": "icon 图标",
    "application": "应用程序",
    "text_file": "文本文件",
    "or": " 或 ",
    "msg_file_replace": "是否替换原文件选项路径",
    "msg_item_replace": "是否替换原选项",
    "msg_if_replace": "是否更改",
    "deleted_file": "已删除其余文件"
  }
}
