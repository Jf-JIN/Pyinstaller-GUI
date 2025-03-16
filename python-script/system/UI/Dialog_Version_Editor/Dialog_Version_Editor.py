

import functools
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QHBoxLayout, QTableWidget, QSizePolicy, QHeaderView, QCheckBox, QAbstractItemView, QTableWidgetItem, QLineEdit,  QFileDialog, QMenu, QAction
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize

from const.Const_Parameter import *
from system.Manager_Language import *
from system.Manager_Setting import *
from system.Manager_Style import *
from system.Manager_Version_File import *
from system.Manager_Version_File import _StringTableStruct, _VarStructStruct, _StringStructStruct, VersionStruct
from system.UI.Dialog_MessageBox import DialogMessageBox
from tools.data_handle import *

from ._Widget_Version import VersionWidget
from ._Dialog_Fixed_File_Info import DialogFFI
from ._Dialog_Language_Char import *


_log = Log.UI
_display_limit = 30  # 按钮的文字显示限制


class VersionEditor(QDialog):
    """ 
    该类为版本文件编辑器, 包含三大部分: 
    1. 固定文件信息(Fixed File Information)
    2. 字符串表(String Table)
    3. 变量表(Variable Table)

    该类不能直接实例化, 只能通过静态方法 VersionEditor.edit() 或 VersionEditor.add_version() 来使用

    目前不支持对于字符串表的自定义添加

    参数: 
    - parent: 父窗口
    - version_file_path: 版本文件路径
    - doShowUI: 是否显示UI, 默认为True, 如果为False, 则不会显示UI, 用于add_version() 方法

    方法: 
    - edit(parent, version_file_path): 编辑版本文件
    - add_version(parent, version_file_path, add_option): 版本文件向上更新版本号
    """
    @staticmethod
    def edit(parent, version_file_path='') -> None:
        """ 
        编辑版本文件

        参数:
        - parent: 父窗口
        - version_file_path: 版本文件路径
        """
        dialog: VersionEditor = QDialog.__new__(VersionEditor)
        dialog.__init__(parent, version_file_path)
        dialog.exec_()
        return dialog.version_file_path

    @staticmethod
    def add_version(parent, version_file_path='', add_option=-1) -> None:
        """ 
        增加版本号

        参数:
        - parent: 父窗口
        - version_file_path: 版本文件路径
        - add_option: 增加的版本号, 默认为-1, 表示不增加版本号
        """
        if add_option < 0 or not os.path.exists(version_file_path):
            return
        dialog: VersionEditor = QDialog.__new__(VersionEditor)
        dialog.__init__(parent, version_file_path, doShowUI=False)
        struct: VersionStruct = dialog.__load_version_file()
        filevers: tuple = struct.ffi.filevers
        prodvers: tuple = struct.ffi.prodvers
        new_filevers: tuple = filevers[:add_option] + (filevers[add_option] + 1,) + filevers[add_option + 1:]
        new_prodvers: tuple = prodvers[:add_option] + (prodvers[add_option] + 1,) + prodvers[add_option + 1:]
        struct.ffi.set_filevers(new_filevers)
        struct.ffi.set_prodvers(new_prodvers)
        new_filevers_str: str = struct.ffi.filevers_str
        new_prodvers_str: str = struct.ffi.prodvers_str
        for item in struct.StringTable_dict.values():
            item: _StringTableStruct
            item.set_StringStruct('FileVersion', new_filevers_str)
            item.set_StringStruct('ProductVersion', new_prodvers_str)
        dialog.__save_version_file(struct, version_file_path)
        return

    @property
    def version_file_path(self) -> str:
        return self.__version_file_path

    def __new__(cls, *args, **kwargs):
        raise TypeError("Cannot instantiate directly. Use VersionEditor.edit() instead.")

    def __init__(self, parent=None, version_file_path='', doShowUI=True) -> None:
        super().__init__(parent)
        self.__version_file_path = version_file_path if os.path.exists(version_file_path) else ''
        self.__init_parameters()
        if not doShowUI:
            return
        self.__init_ui()
        self.__init_signal_connections()

    def __init_parameters(self) -> None:
        self.__widget_data_dict = {}
        self.__SFI_filevers_list = []
        self.__SFI_prodvers_list = []

    def __init_ui(self) -> None:
        self.resize(800, 600)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
        self.setWindowIcon(QIcon(convert_svg_to_pixmap(ICON.APP_ICON)))
        widget_btn_edit = QWidget()
        widget_btn = QWidget()
        layout_main = QVBoxLayout()
        layout_btn_edit = QHBoxLayout(widget_btn_edit)
        layout_button = QHBoxLayout(widget_btn)
        widget_btn_edit.setFixedHeight(50)
        widget_btn.setFixedHeight(50)
        self.__tableWidget = QTableWidget(self)
        self.__tableWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__tableWidget.setColumnCount(3)
        self.__tableWidget.setHorizontalHeaderLabels([LM.getWord('name'), LM.getWord('argument'), LM.getWord('argument_value')])
        self.__tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.__tableWidget.horizontalHeader().setStretchLastSection(True)
        self.__tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.__tableWidget.setColumnWidth(0, 200)
        self.__tableWidget.setColumnWidth(1, 200)
        self.__tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        widget_holder_btn = QWidget(self)
        widget_holder_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_save = QPushButton(LM.getWord('save'), self)
        self.__btn_save.setProperty('widgetType', 'Dialog')
        self.__btn_cancel = QPushButton(LM.getWord('cancel'), self)
        self.__btn_cancel.setProperty('widgetType', 'Dialog')
        widget_holder_btn_edit = QWidget()
        self.__btn_add_sfi = QPushButton()
        self.__btn_add_sfi.setProperty('widgetType', 'square')
        self.__btn_add_sfi.setIcon(QIcon(convert_svg_to_pixmap_with_color(ICON.PLUS, STYLE.getProperty('$btn_svg_color').value)))
        self.__btn_add_sfi.setIconSize(QSize(*STYLE.getProperty('$btn_square_icon_size').value))
        self.__btn_add_sfi.setToolTip(LM.getWord('add_SFI_block'))
        self.__btn_add_sfi.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_add_sfi.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_remove_sfi = QPushButton()
        self.__btn_remove_sfi.setIcon(QIcon(convert_svg_to_pixmap_with_color(ICON.DELETE, STYLE.getProperty('$btn_svg_color').value)))
        self.__btn_remove_sfi.setProperty('widgetType', 'square')
        self.__btn_remove_sfi.setIconSize(QSize(*STYLE.getProperty('$btn_square_icon_size').value))
        self.__btn_remove_sfi.setToolTip(LM.getWord('remove_SFI_block'))
        self.__btn_remove_sfi.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_remove_sfi.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__cb_synchron_vers = QCheckBox(LM.getWord('synchron_vers'), self)
        self.__cb_synchron_vers.setChecked(SM.getConfig('synchron_vers'))
        self.__cb_synchron_vers.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__cb_synchron_vers.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__cb_synchron_vers.stateChanged.connect(lambda: SM.setConfig('synchron_vers', self.__cb_synchron_vers.isChecked()))
        for btn in [self.__btn_save, self.__btn_cancel]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setLayout(layout_main)
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.setSpacing(0)
        layout_main.addWidget(self.__tableWidget)
        layout_main.addWidget(widget_btn_edit)
        layout_main.addWidget(widget_btn)
        layout_main.setStretch(0, 100)
        layout_main.setStretch(1, 10)
        layout_main.setStretch(2, 10)
        layout_btn_edit.addWidget(self.__btn_add_sfi)
        layout_btn_edit.addWidget(self.__btn_remove_sfi)
        layout_btn_edit.addWidget(self.__cb_synchron_vers)
        layout_btn_edit.addWidget(widget_holder_btn_edit)
        layout_btn_edit.setStretch(0, 10)
        layout_btn_edit.setStretch(1, 10)
        layout_btn_edit.setStretch(2, 10)
        layout_btn_edit.setStretch(3, 100)
        layout_button.addWidget(widget_holder_btn)
        layout_button.addWidget(self.__btn_save)
        layout_button.addWidget(self.__btn_cancel)
        layout_button.setStretch(0, 100)
        layout_button.setStretch(1, 10)
        layout_button.setStretch(2, 10)
        self.__version_struct: VersionStruct = self.__load_version_file()
        self.__init_version_items()
        self.setStyleSheet(STYLE.getBlock().style)
        self.__tableWidget.verticalScrollBar().setStyleSheet(STYLE.getBlock('~scrollbar').style)
        self.__tableWidget.verticalHeader().setVisible(False)

    def __init_signal_connections(self) -> None:
        self.__btn_save.clicked.connect(self.__save_version_file_from_btn)
        self.__btn_cancel.clicked.connect(self.__cancel)
        self.__btn_add_sfi.clicked.connect(self.__add_sfi)
        self.__btn_remove_sfi.clicked.connect(self.__remove_sfi_from_btn)
        self.__tableWidget.customContextMenuRequested.connect(self.__on_table_context_menu)

    def __init_version_items(self) -> None:
        self.__tableWidget.setRowCount(7)
        self.__init_ffi_section()  # 初始化控件
        self.__init_vfi_section()  # 初始化控件
        self.__set_ffi_text()  # 添加数据
        self.__set_vfi_section()  # 添加数据
        self.__update_SFI_blocks()  # 更新SFI块, 包括初始化控件和添加数据

    def __load_version_file(self) -> VersionStruct:
        loader = VersionFileLoader()
        loader.load_version_file(self.__version_file_path)
        return loader.version_struct

    def __init_ffi_section(self) -> None:
        """ 
        初始化 FFI 区域, 仅初始化控件, 不添加数据
        """
        self.__tableWidget.setItem(0, 0, QTableWidgetItem())
        self.__tableWidget.setSpan(0, 0, 1, 3)
        ffi_header = QTableWidgetItem(LM.getWord('header_FFI'))
        ffi_header.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        ffi_header.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.__tableWidget.setItem(0, 0, ffi_header)
        filevers_name_item = QTableWidgetItem(LM.getWord('name_FFI_filevers'))
        filevers_name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        filevers_arg_item = QTableWidgetItem('filevers')
        filevers_arg_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.__filevers_value_item = VersionWidget(self.__tableWidget, self.__version_struct.ffi.filevers)
        self.__filevers_value_item.valueChanged.connect(self.__version_struct.ffi.set_filevers)
        self.__filevers_value_item.valueChanged.connect(self.__synchron_version)
        self.__tableWidget.setItem(1, 0, filevers_name_item)
        self.__tableWidget.setItem(1, 1, filevers_arg_item)
        self.__tableWidget.setCellWidget(1, 2, self.__filevers_value_item)
        prodvers_name_item = QTableWidgetItem(LM.getWord('name_FFI_prodvers'))
        prodvers_name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        prodvers_arg_item = QTableWidgetItem('prodvers')
        prodvers_arg_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.__prodvers_value_item = VersionWidget(self.__tableWidget, self.__version_struct.ffi.prodvers)
        self.__prodvers_value_item.valueChanged.connect(self.__version_struct.ffi.set_prodvers)
        self.__prodvers_value_item.valueChanged.connect(self.__synchron_version)
        self.__tableWidget.setItem(2, 0, prodvers_name_item)
        self.__tableWidget.setItem(2, 1, prodvers_arg_item)
        self.__tableWidget.setCellWidget(2, 2, self.__prodvers_value_item)
        flag_name_item = QTableWidgetItem(LM.getWord('name_FFI_flags'))
        flag_name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        flag_arg_item = QTableWidgetItem('flags')
        flag_arg_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.__flag_value_item = QPushButton()
        self.__flag_value_item.setProperty('widgetType', 'versionEditor')
        self.__flag_value_item.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__flag_value_item.clicked.connect(self.__on_ffi_flags_changed)
        self.__tableWidget.setItem(3, 0, flag_name_item)
        self.__tableWidget.setItem(3, 1, flag_arg_item)
        self.__tableWidget.setCellWidget(3, 2, self.__flag_value_item)
        os_name_item = QTableWidgetItem(LM.getWord('name_FFI_OS'))
        os_name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        os_arg_item = QTableWidgetItem('OS')
        os_arg_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.__os_value_item = QPushButton()
        self.__os_value_item.setProperty('widgetType', 'versionEditor')
        self.__os_value_item.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__os_value_item.clicked.connect(self.__on_ffi_os_changed)
        self.__tableWidget.setItem(4, 0, os_name_item)
        self.__tableWidget.setItem(4, 1, os_arg_item)
        self.__tableWidget.setCellWidget(4, 2, self.__os_value_item)
        file_type_name_item = QTableWidgetItem(LM.getWord('name_FFI_fileType'))
        file_type_name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        file_type_arg_item = QTableWidgetItem('fileType')
        file_type_arg_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.__file_type_value_item = QPushButton()
        self.__file_type_value_item.setProperty('widgetType', 'versionEditor')
        self.__file_type_value_item.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__file_type_value_item.clicked.connect(self.__on_ffi_file_type_changed)
        self.__tableWidget.setItem(5, 0, file_type_name_item)
        self.__tableWidget.setItem(5, 1, file_type_arg_item)
        self.__tableWidget.setCellWidget(5, 2, self.__file_type_value_item)
        sub_type_name_item = QTableWidgetItem(LM.getWord('name_FFI_subtype'))
        sub_type_name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        sub_type_arg_item = QTableWidgetItem('subtype')
        sub_type_arg_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.__sub_type_value_item = QPushButton()
        self.__sub_type_value_item.setProperty('widgetType', 'versionEditor')
        self.__sub_type_value_item.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__sub_type_value_item.clicked.connect(self.__on_ffi_sub_type_changed)
        self.__tableWidget.setItem(6, 0, sub_type_name_item)
        self.__tableWidget.setItem(6, 1, sub_type_arg_item)
        self.__tableWidget.setCellWidget(6, 2, self.__sub_type_value_item)

    def __set_ffi_text(self) -> None:
        """ 
        设置FFI文本, 包含5部分, 
        1. filevers, prodvers
        2. flags
        3. os
        4. fileType
        5. subtype
        """
        self.__filevers_value_item.setValue(self.__version_struct.ffi.filevers)
        self.__prodvers_value_item.setValue(self.__version_struct.ffi.prodvers)
        self.__set_flags_text()
        self.__set_os_text()
        self.__set_file_type_text()
        self.__set_sub_type_text()

    def __init_vfi_section(self) -> None:
        """ 
        初始化 VFI 区域, 仅初始化控件, 不添加数据
        """
        struct: _VarStructStruct = self.__version_struct.varStruct
        current_row_count = self.__tableWidget.rowCount()
        self.__tableWidget.setRowCount(current_row_count + 2)
        self.__tableWidget.setSpan(current_row_count, 0, 1, 3)
        header = QTableWidgetItem(LM.getWord('header_Translation'))
        header.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.__tableWidget.setItem(current_row_count, 0, header)
        name_item = QTableWidgetItem('name_Translation')
        name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        arg_item = QTableWidgetItem(LM.getWord('Translation'))
        arg_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.__varStruct_widget = QPushButton(self.__tableWidget)
        self.__varStruct_widget.setProperty('widgetType', 'versionEditor')
        self.__varStruct_widget.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__varStruct_widget.clicked.connect(self.__on_varStruct_changed)
        self.__widget_data_dict[self.__varStruct_widget] = struct
        self.__tableWidget.setItem(current_row_count+1, 0, name_item)
        self.__tableWidget.setItem(current_row_count+1, 1, arg_item)
        self.__tableWidget.setCellWidget(current_row_count+1, 2, self.__varStruct_widget)

    def __set_vfi_section(self) -> None:
        """ 
        设置 VFI 数据
        """
        struct: _VarStructStruct = self.__version_struct.varStruct
        lang_list = struct.value
        if not lang_list:
            return
        value_list = []
        lang_text = ''
        char_text = ''
        for idx, item in enumerate(lang_list):
            if idx % 2 == 0:  # 语言
                lang_item = VersionEnum.LangID.getItem(item)
                if lang_item:
                    lang_text = lang_item.name
            else:  # 编码
                if not lang_text:
                    continue
                char_item = VersionEnum.CharsetID.getItem(item)
                if char_item:
                    char_text = char_item.name
                    display_lang_text = LM.getWord('lang_'+lang_text)
                    value_list.append(f'{display_lang_text}({char_text})')
                    lang_text = ''
                    char_text = ''
        value_text = '; '.join(value_list)
        if len(value_text) > _display_limit:
            value_text = value_text[:_display_limit] + ' ...'
        self.__varStruct_widget.setText(value_text)

    def __update_SFI_blocks(self) -> None:
        """ 
        更新 SFI 块, 先清空区域内的表格, 再重新生成

        如果没有 SFI 数据, 则默认生成一个 SFI 块
        """
        self.__remove_table_SFI()
        if len(self.__version_struct.StringTable_dict) == 0:
            self.__set_string_table_block()
        else:
            for idx, (key, struct) in enumerate(self.__version_struct.StringTable_dict.items()):
                self.__set_string_table_block(struct, idx)

    def __remove_table_SFI(self) -> None:
        """ 
        移除 SFI 块, 从表格的第 9 行开始, 逐行删除
        前9行数据为固定的, 分别是 FFI(7) VFI(2) 
        """
        start_row = 9
        row_count = self.__tableWidget.rowCount()
        for row in range(row_count - 1, start_row - 1, -1):
            self.__tableWidget.removeRow(row)
        self.__SFI_filevers_list = []
        self.__SFI_prodvers_list = []

    def __set_string_table_block(self, struct: _StringTableStruct | None = None, key_index: int = 0) -> None:
        """ 
        设置单个 SFI 块, 根据传入的 struct 数据, 生成表格行

        参数: 
        - struct: _StringTableStruct | None, SFI 块的数据结构, 默认为 None
        - key_index: int, SFI 块的索引, 默认为 0
        """
        current_row_count: int = self.__tableWidget.rowCount()
        dict_len: int = len(self.__version_struct.StringTable_dict)
        widget_dict: dict = {}
        general_dict: dict = {
            'FileVersion': {
                'name': LM.getWord('name_SFI_FileVersion'),
                'arg': 'FileVersion',
            },
            'ProductVersion': {
                'name': LM.getWord('name_SFI_ProductVersion'),
                'arg': 'ProductVersion',
            },
            'ProductName': {
                'name': LM.getWord('name_SFI_ProductName'),
                'arg': 'ProductName',
            },
            'CompanyName': {
                'name': LM.getWord('name_SFI_CompanyName'),
                'arg': 'CompanyName',
            },
            'FileDescription': {
                'name': LM.getWord('name_SFI_FileDescription'),
                'arg': 'FileDescription',
            },
            'InternalName': {
                'name': LM.getWord('name_SFI_InternalName'),
                'arg': 'InternalName',
            },
            'LegalCopyright': {
                'name': LM.getWord('name_SFI_LegalCopyright'),
                'arg': 'LegalCopyright',
            },
            'LegalTrademarks': {
                'name': LM.getWord('name_SFI_LegalTrademarks'),
                'arg': 'LegalTrademarks',
            },
            'OriginalFilename': {
                'name': LM.getWord('name_SFI_OriginalFilename'),
                'arg': 'OriginalFilename',
            },
            'PrivateBuild': {
                'name': LM.getWord('name_SFI_PrivateBuild'),
                'arg': 'PrivateBuild',
            },
            'SpecialBuild': {
                'name': LM.getWord('name_SFI_SpecialBuild'),
                'arg': 'SpecialBuild',
            },
        }
        if struct is not None:
            self.__load_SFI_data(struct, general_dict)
        else:
            struct = self.__version_struct.set_string_table()

        if 'value' not in general_dict['FileVersion'] or not general_dict['FileVersion']['value']:
            general_dict['FileVersion']['value'] = self.__version_struct.ffi.filevers_str
            struct.set_StringStruct('FileVersion', general_dict['FileVersion']['value'])
        if 'value' not in general_dict['ProductVersion'] or not general_dict['ProductVersion']['value']:
            general_dict['ProductVersion']['value'] = self.__version_struct.ffi.prodvers_str
            struct.set_StringStruct('ProductVersion', general_dict['ProductVersion']['value'])
        if 'value' not in general_dict['ProductName'] or not general_dict['ProductName']['value']:
            general_dict['ProductName']['value'] = 'Python_Pyinstaller_Application'
            struct.set_StringStruct('ProductName', general_dict['ProductName']['value'])
        if 'value' not in general_dict['CompanyName'] or not general_dict['CompanyName']['value']:
            general_dict['CompanyName']['value'] = 'MyCompany'
            struct.set_StringStruct('CompanyName', general_dict['CompanyName']['value'])

        self.__tableWidget.setRowCount(current_row_count + len(general_dict)+1)
        self.__tableWidget.setSpan(current_row_count, 0, 1, 3)
        header_text = LM.getWord('header_StringFileInfo') + f' {struct.table_key}'
        header = QTableWidgetItem(header_text)
        header.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        header.setData(Qt.ItemDataRole.UserRole, {'index': key_index, 'header': header_text})
        self.__tableWidget.setItem(current_row_count, 0, header)
        for idx, (key, item) in enumerate(general_dict.items()):
            name_item = QTableWidgetItem(item['name'])
            name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            name_item.setData(Qt.ItemDataRole.UserRole, {'index': key_index, 'header': header_text})
            arg_item = QTableWidgetItem(item['arg'])
            arg_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            arg_item.setData(Qt.ItemDataRole.UserRole, {'index': key_index, 'header': header_text})
            value_item = QLineEdit(item.get('value', ''))
            value_item.setClearButtonEnabled(True)
            if struct is not None:
                value_item.textChanged.connect(functools.partial(self.__on_stringFileInfo_changed, struct, key, value_item))
            self.__tableWidget.setItem(current_row_count + 1+idx, 0, name_item)
            self.__tableWidget.setItem(current_row_count + 1+idx, 1, arg_item)
            self.__tableWidget.setCellWidget(current_row_count + 1+idx, 2, value_item)
            if key == 'FileVersion':
                self.__SFI_filevers_list.append(value_item)
            elif key == 'ProductVersion':
                self.__SFI_prodvers_list.append(value_item)
            widget_dict[key] = value_item

    def __load_SFI_data(self, struct: _StringTableStruct, general_dict: dict) -> None:
        """ 
        读取 StringFileInfo 数据到 general_dict
        """
        if struct is None:
            return
        item_dict: dict = struct.StringStruct_dict
        for key, item in item_dict.items():
            item: _StringStructStruct
            if key not in general_dict:
                general_dict[key] = {
                    'name': key,
                    'arg': key,
                }
            general_dict[key]['value'] = item.value

    def __set_flags_text(self) -> None:
        """ 
        FFI 设置 flags 文本
        """
        value: int = self.__version_struct.ffi.flags
        temp: list = []
        for item in VersionEnum.FileFlags:
            name = item.name
            if value & item:
                temp.append(name)
        if not temp:
            enum_item = VersionEnum.FileFlags.getItem(value)
            if enum_item is not None:
                text = enum_item.name
            else:
                text = ''
                _log.warning(f'Unkown flags: {value}')
        else:
            text: str = '; '.join(temp)
        if len(text) > _display_limit:
            text = text[:_display_limit] + ' ...'
        self.__flag_value_item.setText(text)
        self.__flag_value_item.setToolTip(text)

    def __set_os_text(self) -> None:
        """ 
        FFI 设置 os 文本
        """
        value = self.__version_struct.ffi.os
        temp = []
        main_os = 0xffff0000 & value
        sub_os = 0x0000ffff & value
        main_item = VersionEnum.FileOS.getItem(main_os)
        sub_item = VersionEnum.FileOS.getItem(sub_os)
        if main_item is not None and main_item != VersionEnum.FileOS.VOS_UNKNOWN:
            temp.append(main_item.name)
        if sub_item is not None and sub_item != VersionEnum.FileOS.VOS_UNKNOWN:
            temp.append(sub_item.name)
        if main_item is not None and sub_item is not None and main_item == VersionEnum.FileOS.VOS_UNKNOWN and sub_item == VersionEnum.FileOS.VOS_UNKNOWN:
            temp = [VersionEnum.FileOS.VOS_UNKNOWN.name]
        text: str = '; '.join(temp)
        if len(text) > _display_limit:
            text = text[:_display_limit] + ' ...'
        self.__os_value_item.setText(text)
        self.__os_value_item.setToolTip(text)

    def __set_file_type_text(self) -> None:
        """ 
        FFI 设置 file_type 文本
        """
        value = self.__version_struct.ffi.file_type
        text = ''
        for item in VersionEnum.FileType:
            name = item.name
            if value == item:
                text = name
        if len(text) > _display_limit:
            text = text[:_display_limit] + ' ...'
        self.__file_type_value_item.setText(text)
        self.__file_type_value_item.setToolTip(text)

    def __set_sub_type_text(self) -> None:
        """ 
        FFI 设置 sub_type 文本
        """
        value = self.__version_struct.ffi.sub_type
        text = ''
        for item in VersionEnum.FileSubtype:
            name = item.name
            if value == item:
                text = name
        if len(text) > _display_limit:
            text = text[:_display_limit] + ' ...'
        self.__sub_type_value_item.setText(text)
        self.__sub_type_value_item.setToolTip(text)

    def __on_varStruct_changed(self) -> None:
        """ 
        更新 VFI 块的数据
        """
        res = DialogLanguageChar.edit(self, self.__version_struct.varStruct.value)
        if not res:
            return
        res_couple = chunk_list_by_two(res)
        self.__version_struct.varStruct.set_value('Translation', res)
        self.__set_vfi_section()
        limit_len = len(self.__version_struct.StringTable_dict)
        for idx, item in enumerate(res_couple):
            if idx >= limit_len:
                break
            struct: _StringTableStruct = self.__version_struct.StringTable_dict[idx]
            struct.set_table_key(item[0], item[1])
        self.__update_SFI_blocks()

    def __on_stringFileInfo_changed(self, struct: _StringTableStruct, key: str, lineEdit: QLineEdit) -> None:
        """ 
        更新 StringFileInfo 块的数据

        参数: 
        - struct: SFI数据类
        - key:  SFI 数据类中的键, 如: CompanyName
        - lineEdit: 对应显示的文本框, 用于获取数据
        """
        value = lineEdit.text()
        struct.set_StringStruct(key, value)

    def __on_ffi_flags_changed(self) -> None:
        """ 
        更新 FFI flags 的数据
        """
        content_dict = {}
        value = self.__version_struct.ffi.flags
        for item in VersionEnum.FileFlags:
            name = item.name
            enum_value = item.value
            isChecked = False
            if value == VersionEnum.FileFlags.VS_FF_UNKNOWN and enum_value == VersionEnum.FileFlags.VS_FF_UNKNOWN:
                isChecked = True
            elif value & enum_value:
                isChecked = True
            content_dict[name] = {
                'hint': LM.getWord(f'hint_{name}'),
                'value': enum_value,
                'status': isChecked
            }
        result = DialogFFI.edit(self, LM.getWord('title_ffi_flags'), content_dict=content_dict, isMultiParams=True)
        if result is None:
            return
        self.__version_struct.ffi.set_flags(result)
        self.__set_ffi_text()

    def __on_ffi_os_changed(self) -> None:
        """ 
        更新 FFI os 的数据
        """
        content_dict = {}
        value = self.__version_struct.ffi.os
        main_os = value & 0xffff0000
        sub_os = value & 0x0000ffff
        main_item = VersionEnum.FileOS.getItem(main_os)
        sub_item = VersionEnum.FileOS.getItem(sub_os)
        for item in VersionEnum.FileOS:
            name = item.name
            enum_value = item.value
            content_dict[name] = {
                'hint': LM.getWord(f'hint_{name}'),
                'value': enum_value,
                'status': False
            }
        content_dict[main_item.name]['status'] = True
        content_dict[sub_item.name]['status'] = True
        result = DialogFFI.edit(self, LM.getWord('title_ffi_os'), content_dict=content_dict, isMultiParams=True, isOS=True)
        if result is None:
            return
        self.__version_struct.ffi.set_os(result)
        self.__set_ffi_text()

    def __on_ffi_file_type_changed(self) -> None:
        """ 
        更新 FFI file_type 的数据
        """
        content_dict = {}
        value = self.__version_struct.ffi.file_type
        enum_item = VersionEnum.FileType.getItem(value)
        for item in VersionEnum.FileType:
            name = item.name
            enum_value = item.value
            content_dict[name] = {
                'hint': LM.getWord(f'hint_{name}'),
                'value': enum_value,
                'status': False
            }
        content_dict[enum_item.name]['status'] = True
        result = DialogFFI.edit(self, LM.getWord('title_ffi_file_type'), content_dict=content_dict, isMultiParams=False)
        if result is None:
            return
        self.__version_struct.ffi.set_file_type(result)
        self.__set_ffi_text()

    def __on_ffi_sub_type_changed(self) -> None:
        """ 
        更新 FFI sub_type 的数据
        """
        content_dict = {}
        value = self.__version_struct.ffi.sub_type
        enum_item = VersionEnum.FileSubtype.getItem(value)
        for item in VersionEnum.FileSubtype:
            name = item.name
            enum_value = item.value
            content_dict[name] = {
                'hint': LM.getWord(f'hint_{name}'),
                'value': enum_value,
                'status': False
            }
        content_dict[enum_item.name]['status'] = True
        result = DialogFFI.edit(self, LM.getWord('title_ffi_file_subtype'), content_dict=content_dict, isMultiParams=False)
        if result is None:
            return
        self.__version_struct.ffi.set_subtype(result)
        self.__set_ffi_text()

    def __cancel(self) -> None:
        """ 取消按钮 """
        res = DialogMessageBox.info(self, LM.getWord('info_version_editor_cancel'))
        if res == DialogMessageBox.StandardButton.CANCEL:
            return
        elif res == 0:
            self.reject()

    def __save_version_file_from_btn(self) -> None:
        """ 通过按钮保存文件 """  # 之后可以添加 Ctrl + S 快捷键, 或者右键等
        self.__save_version_file()

    def __save_version_file(self, struct=None, file_path=None) -> None:
        """ 保存版本文件 """
        if struct is None:
            struct = self.__version_struct
        if file_path is None:
            file_path = self.__version_file_path
        data = struct.get_file_data()
        if os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(data)
        else:
            if not self.__version_file_path:
                version_file_name = os.path.join(os.getcwd(), 'Version.txt')
            else:
                version_file_name = self.__version_file_path
            file_path = QFileDialog.getSaveFileName(self, 'Save File', version_file_name, 'Text Files (*.txt)')[0]
            if file_path:
                self.__version_file_path = file_path
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(data)
        self.accept()

    def __add_sfi(self) -> None:
        """ 新增 SFI 块 """
        self.__version_struct.set_string_table()
        self.__update_SFI_blocks()

    def __synchron_version(self) -> None:
        """ 同步 FFI 和 所有 SFI 块的版本号 """
        if not self.__cb_synchron_vers.isChecked():
            return
        file_vers_str = self.__version_struct.ffi.filevers_str
        prod_vers_str = self.__version_struct.ffi.prodvers_str
        for item in self.__SFI_filevers_list:
            item: QLineEdit
            item.setText(file_vers_str)
        for item in self.__SFI_prodvers_list:
            item: QLineEdit
            item.setText(prod_vers_str)

    def __on_table_context_menu(self, pos) -> None:
        """ 表格右键菜单 """
        if not pos:
            return
        item = self.__tableWidget.itemAt(pos)
        if not item:
            return
        row = item.row()
        column = item.column()
        menu = QMenu(self)
        action_add = QAction(LM.getWord('add_SFI_block'))
        action_add.setIcon(QIcon(convert_svg_to_pixmap(ICON.PLUS)))
        action_remove = QAction(LM.getWord('remove_SFI_block'))
        action_remove.setIcon(QIcon(convert_svg_to_pixmap(ICON.DELETE)))
        action_add.triggered.connect(self.__add_sfi)
        action_remove.triggered.connect(lambda: self.__remove_sfi_from_context(row, column))
        menu.addAction(action_add)
        menu.addAction(action_remove)
        menu.exec_(self.__tableWidget.mapToGlobal(pos))

    def __remove_sfi_from_context(self, row, column) -> None:
        """ 右键菜单移除 SFI 块"""
        item: QTableWidgetItem = self.__tableWidget.item(row, column)
        self.__remove_sfi(item)

    def __remove_sfi_from_btn(self) -> None:
        """ 按钮移除 SFI 块"""
        item: QTableWidgetItem = self.__tableWidget.currentItem()
        self.__remove_sfi(item)

    def __remove_sfi(self, item: QTableWidgetItem) -> None:
        """ 
        移除 SFI 块

        由于单元格控件初始化的时候, 就把整个 SFI 块在 self.__version_struct.StringTable_dict 字典中的键名作为 UserRole 保存了, 
        所以可以通过 UserRole 来获取到对应的键名, 从而删除对应的 SFI 块. 通过删除数据类中的数据, 再重新生成表格, 即可完成删除操作. 

        参数: 
        - item: 需要移除的 SFI 块单元格控件
        """
        if not item:
            return
        data = item.data(Qt.UserRole)
        if data is None:
            return
        header = data['header']
        text = LM.getWord('question_remove_SFI_block_')+f'\n   - {header}'
        res = DialogMessageBox.question(self, LM.getWord('remove_SFI_block'), text, [LM.getWord('remove')])
        if res == DialogMessageBox.StandardButton.CANCEL:
            return
        elif res == 0:
            del self.__version_struct.StringTable_dict[data['index']]
            self.__version_struct.sort_string_table()
            self.__update_SFI_blocks()
