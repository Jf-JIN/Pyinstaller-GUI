# Pyinstaller_exe



### 软件简介  |  Software Introduction：

这是一个通过使用Pyinstaller6.0来打包python脚本的程序，用户通过界面中的各按钮来进行输入而无需使用命令行，程序可打印执行命令或直接执行打包操作。

该软件起初是因为本人想把py脚本打包成exe，但是因为参数路径等命令太长，每一次写都比较麻烦，所以开发了这个小工具。

软件可能还不够完善，其中也还可能有bug，欢迎大家提出意见和建议！

<div style="display:inline-block;">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/main_interface_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/english_version.png" alt="image1" height = "150">   <img src="https://github.com/JIN-Junfan/test/blob/main/image/germen_version.png" alt="image2" height = "150"> </div>

----

### 使用方法  |  Usage **Instructions**：

##### 1. 软件安装与适用   |   Installation and Application：

在.app下有直接打包好的可执行程序，供直接使用。或者在.setup下使用安装包进行安装。请注意，使用安装包的话，会自动添加鼠标右键菜单项。使用右键菜单时可以直接定位至选中的py文件从而进行打包。

如果是win 7 系统，请下载Win7版本。版本号**D**表示directory 程序打包为文件夹，**F** 表示 file 程序打包为文件

##### 2. 软件使用   |   Software Utilization：

软件使用前提是已安装Pyinstaller。如未安装，可点击“安装Pyinstaller”进行安装。未安装Pyinstaller而进行操作，控制台将提示“ '*pyinstaller' 不是内部或外部命令，也不是可运行的程序或批处理文件。*”。

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/Pyinstaller_noset_error.png" alt="image1" height = "150" align=center > </div>

打开软件后，软件将默认寻找工作路径下的main.py文件，若无main.py文件，则将选择当前文件夹中第一个py文件。如需更改，请手动选择需要打包的.py文件。当勾选“锁定”时，对应的输出文件夹或输出名称将保持当前输入；取消勾选时，将默认与原python文件同名，并输出到当前python文件所在的目录下。

当输入了.py文件后，可使用下面的按钮来进行参数的输入。当“工具提示”被勾选时，鼠标悬停时会有功能提示和说明。

当使用“清空输入”或“全部清空”时，为防止误操作，可以进行一次恢复，数据将恢复至最后一次清空前的状态。当清空后，又进行输入时，部分恢复数据不会恢复至最后一次输入的状态，而是恢复至最后一次清空前的状态。

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/clear_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/recover_example.png" alt="image1" height = "150"> </div>

当所有所需参数全部输入完成后，可点击“显示参数”进行检查，或者点击“打印cmd命令”，查看默认输出名为“output_command_of_pyinstaller.txt”文本文件。

<u>**检查无误后，可点击   “ 开始执行转换 ”   进行打包。**</u>

当“结束后仅保留exe”被勾选时，将在打包完成后删除.spec文件以及 .dict 和 .build 文件夹。

点击“打开输出文件夹”，即可查看打包完成的exe文件

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/add_file_example.png" alt="image1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/dialog_example.png" alt="image1" height = "150"><img src="https://github.com/JIN-Junfan/test/blob/main/image/dialog_example_2.png" alt="image2" height = "150"> </div>

##### 3. 打包环境选择 | ：

在环境变量旁边有一个Conda设置按钮，该按钮仅在当前电脑已安装Conda (Anaconda, Miniconda ...) 并在环境变量中正确配置时才可使用，当满足上述条件时，按钮将置为可用，同时将显示当前选择的Conda环境，若不想使用Conda环境，则可以取消勾选“使用Conda环境”，则可以使用全局Python的环境。

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/conda1.png" alt="conda1" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/conda2.png" alt="conda2" height = "150"><img src="https://github.com/JIN-Junfan/test/blob/main/image/conda5.png" alt= "conda" height = "150"> </div>

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/conda3.png" alt="conda3" height = "150">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/conda4.png" alt="conda4" height = "150"> </div>

进入Conda设置后，稍等片刻后，将显示出当前conda所有的环境，用户可进行选择。也可以通过右下角的按钮，查看选中的Conda环境中已安装了哪些python包。如果Conda更新后，建议重启改软件，避免出现Conda环境选择错误。

##### 4. 语言切换   |   Change Language:

在标题旁边有一个下拉菜单栏，有多种语言可供选择。语言包也可自行添加，路径为该软件的目录下.Languages\中，当自定义的语言包放到该目录后，重新启动软件，新的语言包即可在下拉菜单栏中找到并使用。请注意语言包的完整性，否则将会出现显示错误，甚至软件崩溃。

<div style="display:inline-block">  <img src="https://github.com/JIN-Junfan/test/blob/main/image/language_select.png" height = "150" alt="select_language" align=center /> </div>

----

### 开发说明   |   Development Notes：

使用PyQt5进行的GUI设计

##### 开发进度   |   Development Progress：

* 当前已完成：基本的所有**Pyinstaller*6.0***的功能项41项、运行报错提示、控制台同步输出、信息台信息更新、当前有效参数显示、命令提示符打印功能、语言切换功能，内置语言包，右键文件选中，Conda环境选择，自动配置启动画面文件
* 正在进行：暂无(2024.1月.24)
* 未完成：菜单栏的编写，德语语言包，版本说明，软件说明

##### 开发所用资源及参考   |   Resources and References：

* PyQt5：https://doc.qt.io/qt-5/

* Pyinstaller: https://pyinstaller.org/en/stable/
* Icon Images: https://www.iconfont.cn/

##### 版本说明   |   Version Descriptions：

* v3.2：
  * 增加了软件配置文件，目前只记录语言选项，启动软件后，语言将设置为上次更改后的语言
  * 增加了右键选择定位文件
  * 修复输出位置在其他文件夹时，打包工程文件不能删除的问题
  * 增加了Conda环境的选择
  * 添加pyinstaller安装、版本、帮助的Conda功能
  * 修复了部分输出命令显示错误
  * 增加了内置语言包(内置简体中文，英语)
  * 修正了语言包部分内容
  * 增加了自动生成启动画面的引用文件和引用
  * 修复.build文件夹删除不干净的问题 修复了当py脚本为空时，清空输入而造成的闪退问题 
  * 修复了选py脚本时，取消选择后闪退的问题 
  * 解决了不同分辨率下的显示差异的问题 
  * 更改了命令行项目顺序，为避免打包时系统报毒，将py脚本放在了pyinstaller的后面，然后是--onedir或者--onefile。(其有效性目前未知)
  * 修复了自动选取Python文件时，无法定位到main函数，以及顺序错误的问题
  
* v3.1:
  * 增加了打开环境变量，更新pip功能
  * 增加了语言切换功能
  * 修复了部分功能输出命令错误的bug

* v3.0：窗口界面版。在v2.0基础上，重新设计窗口界面
  * 增加了控制台显示，信息台显示。
  * 补全了pyinstaller基本所有的功能41项
  * 增加了自寻找默认py文件(main.py)
  * 增加了打印命令功能，显示参数功能
* v2.0：窗口界面版。将v1.0的界面改为窗口界面，增加了添加应用图标和添加文件的选项，可自动检测并安装pyinstaller，集成了pyuic5和pyrcc5，可进行ui文件转py，qrc文件转py
* v1.0：命令提示符版。可列出当前目录下所有python文件，可通过数字选择要打包的Python文件，可选择是否隐藏控制台
* 由于前期并没有对项目进行管理，故v1.0，v2.0, v3.0，v3.1的版本已缺失



----

### 注意事项   |   Notes：

暂无
