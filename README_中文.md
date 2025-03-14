# Pyinstaller_exe



### 软件简介  |  Software Introduction: 

这是一个通过使用Pyinstaller6.0来打包python脚本的程序, 用户通过界面中的各按钮来进行输入而无需使用命令行或编辑spec, 程序可打印执行命令或直接执行打包操作. 

该软件起初是因为本人想把py脚本打包成exe, 但是因为参数路径等命令太长, 每一次写都比较麻烦, 所以开发了这个小工具. 

软件可能还不够完善, 其中也还可能有bug, 欢迎大家提出意见和建议! 

----

### 使用方法  | **How to Use**: 

1. 基本使用方法: 

   * 打开文件并打包: 
     * 首先打开需打包的文件, 如果文件为*.spec则将自动清空所有参数
     * 点击 "运行", 核对参数
     * 再次点击 "运行", 开始打包
     * 打包结束可点击下方的打开文件夹位置查看
   * 可选: 
     * 加载 .ico 文件
     * 加载 Version.txt 文件
     * 编辑 Version.txt 文件

   <div style="display:inline-block;"><img src="https://github.com/Jf-JIN/Pyinstaller-GUI/blob/main/image/Home_Page_zh.png" alt="erweitung4" height = "200"><img src="https://github.com/Jf-JIN/Pyinstaller-GUI/blob/main/image/Light_zh.png" alt="erweitung4" height = "200"><img src="https://github.com/Jf-JIN/Pyinstaller-GUI/blob/main/image/Version_Editor_zh.png" alt="erweitung4" height = "200"></div>
   
<div style="display:inline-block;"><img src="https://github.com/Jf-JIN/Pyinstaller-GUI/blob/main/image/Operation_Page_zh.png" alt="erweitung4" height = "200"><img src="https://github.com/Jf-JIN/Pyinstaller-GUI/blob/main/image/Setting_Page_1_zh.png" alt="erweitung4" height = "200"></div>

2. 参数设置: 

   * 在功能页中, 可以对PyInstaller的参数进行详细设置

3. 信息查看: 

   * 在信息表中, 右键可以对项目进行删除或跳转编辑
   * 环境配置是用于打包时方便控制台环境设置, 确保可以包含Python的部分二进制文件. 如果仍存在库丢失, 请尝试使用 `添加文件资源`

4. 命令行查看: 

   * 窗口下方的按钮可以对字体进行放大缩小或清空屏幕

5. 终端信息查看: 

   * 同命令行一样, 可以对字体放大缩小, 清空屏幕

   * 如果打包失败, 可以在此处查找问题

6. 设置: 

   * 语言设置: 

     可自定义语言包, 内置有简体中文和英语的语言包, 格式为json. 可以在`.Languages_PyInstallerGUI`中查看样例. 但请不要在样例中直接修改, 请创建副本. 为了保证样例的正确性, 每次启动程序时都会重写语言包样例. 后续会增加手动生成样例, 以减少反复写文件的次数

   * 执行方式设置: 

     可以选择使用 pyinstaller.exe 还是 python.exe 运行命令

   * 环境设置:

     * 可以在`设置->运行环境`中对环境进行设置, 默认使用内置PyInstaller, 支持Conda和系统环境中的Python进行检测, 如果未安装PyInstaller, 则在打包中默认使用内置PyInstaller进行打包. 其他的环境可以通过指定路径来使用

     * 也可以通过主页中环境设置直接跳转

     * 当前使用的环境将在两个页面(主页、设置)中进行显示

     * 双击 PyInstaller未安装的标志可以安装PyInstaller, 如果已经安装则会更新

   * 样式设置
   
     当前可以选择深色样式和浅色样式, 之后会增加自定义样式设置




----

### 开发说明   |   Development Notes: 

使用PyQt5进行的GUI设计

##### 开发进度   |   Development Progress: 

* 当前已完成: 详见版本说明
* 正在进行: 对Linux的支持
* 未完成: 菜单栏, 版本说明, 软件说明, 报错反馈, 打包失败跳转终端显示

##### 开发所用资源及参考   |   Resources and References: 

* PyQt5: https://doc.qt.io/qt-5/

* Pyinstaller: https://pyinstaller.org/en/stable/
* Icon Images: https://www.iconfont.cn/

##### 版本说明   |   Version Descriptions: 
* v4.0:
  * 新增对 *.spec, *.pyw, *.pyd, *.spec, *.txt(命令行文件) 的支持
  * 新增对命令行文件读取/加载的功能
  * 新增信息显示
  * 新增命令行显示
  * 新增安装PyInstaller功能
  * 新增对PyInstaller的内置集成
  * 新增版本编辑器
  * 新增多样式
  * 计划增加自定义样式编辑
  * 分离了各功能区
  * 重新设计了UI界面
* v3.3: 
  * 新增单例模式, 用户开启后, 再次打开时, 将自动定位到已打开的窗口. 当已经多次开该软件时, 已打开的将保留, 新打开的将定位至最早打开的该软件窗口. 关闭后可继续多次多窗口打开该软件
  * 新增进度提示条, 方便用户了解打包的进展
  * 修复禁用窗口化与显示控制台的逻辑冲突bug
* v3.2: 
  * 新增了软件配置文件, 目前只记录语言选项, 启动软件后, 语言将设置为上次更改后的语言
  * 新增了右键选择定位文件
  * 新增了Conda环境的选择
  * 新增了内置语言包(内置简体中文, 英语)
  * 新增了自动生成启动画面的引用文件和引用
  * 新增pyinstaller安装、版本、帮助的Conda功能
  * 修复输出位置在其他文件夹时, 打包工程文件不能删除的问题
  * 修复了部分输出命令显示错误
  * 修复.build文件夹删除不干净的问题 修复了当py脚本为空时, 清空输入而造成的闪退问题 
  * 修复了选py脚本时, 取消选择后闪退的问题 
  * 修复了自动选取Python文件时, 无法定位到main函数, 以及顺序错误的问题
  * 修正了语言包部分内容
  * 解决了不同分辨率下的显示差异的问题 
  * 更改了命令行项目顺序, 为避免打包时系统报毒, 将py脚本放在了pyinstaller的后面, 然后是--onedir或者--onefile. (其有效性目前未知)
* v3.1:
  * 增加了打开环境变量, 更新pip功能
  * 增加了语言切换功能
  * 修复了部分功能输出命令错误的bug
* v3.0: 窗口界面版. 在v2.0基础上, 重新设计窗口界面
  * 增加了控制台显示, 信息台显示. 
  * 增加了自寻找默认py文件(main.py)
  * 增加了打印命令功能, 显示参数功能
  * 补全了pyinstaller基本所有的功能41项
* v2.0: 窗口界面版. 将v1.0的界面改为窗口界面, 增加了添加应用图标和添加文件的选项, 可自动检测并安装pyinstaller, 集成了pyuic5和pyrcc5, 可进行ui文件转py, qrc文件转py
* v1.0: 命令提示符版. 可列出当前目录下所有python文件, 可通过数字选择要打包的Python文件, 可选择是否隐藏控制台
* 由于前期并没有对项目进行管理, 故v1.0, v2.0, v3.0, v3.1的版本已缺失
