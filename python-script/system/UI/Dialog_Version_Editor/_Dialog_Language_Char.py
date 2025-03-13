from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QSizePolicy, QPushButton, QListWidget, QListWidgetItem, QAbstractItemView, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal, QPoint

from const.Const_Parameter import *
from const.Const_Version_File import *
from const.Const_Icon import *

from system.Manager_Language import *
from system.Manager_Style import *
from system.UI.Dialog_MessageBox import DialogMessageBox
from tools import *
_log = Log.UI


class _WidgetLanguageChar(QWidget):
    """ 
    该类是用于编辑 VarFileInfo 的语言和字符集的控件, 在 DialogLanguageChar 中使用

    内部主要是4个控件, 2个QLabel, 2个QComboBox

    其中 QComboBox 的值取自与枚举类 VersionEnum.LangID 和 VersionEnum.CharsetID

    当 QComboBox 的值改变时, 会发出 valueChanged 信号

    参数: 
    - parent: 父控件
    - lang: 语言, 默认为 English_US
    - char: 字符集, 默认为 Unicode

    属性: 
    - data: [lang, char] 其中, lang 和 char 都是数值, 如 [0x0804, 0x04B0]
    - lang_str: 语言名称, 名称是语言包内的名称, 不是数值, 如: '简体中文'
    - char_str: 字符集名称, 名称是枚举类变量的名称, 不是数值, 如: 'Unicode'
    """
    valueChanged = pyqtSignal()

    def __init__(self, parent=None, lang=VersionEnum.LangID.English_US, char=VersionEnum.CharsetID.Unicode) -> None:
        super().__init__(parent)
        self.__lang = lang
        self.__char = char
        self.__init_ui()

    def __init_ui(self) -> None:
        layout = QHBoxLayout(self)
        lb_lang = QLabel(LM.getWord('language')+':')
        lb_lang.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        lb_char = QLabel(LM.getWord('charset')+':')
        lb_char.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__cbb_lang = QComboBox(self)
        self.__cbb_lang.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__cbb_char = QComboBox(self)
        self.__cbb_char.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(lb_lang)
        layout.addWidget(self.__cbb_lang)
        layout.addWidget(lb_char)
        layout.addWidget(self.__cbb_char)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        layout.setStretch(0, 10)
        layout.setStretch(1, 100)
        layout.setStretch(2, 10)
        layout.setStretch(3, 100)
        for lang in VersionEnum.LangID:
            self.__cbb_lang.addItem(LM.getWord('lang_'+lang.name), lang.value)
        for char in VersionEnum.CharsetID:
            self.__cbb_char.addItem(char.name, char.value)
        self.__cbb_lang.setCurrentText(LM.getWord('lang_'+VersionEnum.LangID.getItem(self.__lang).name))
        self.__cbb_char.setCurrentText(VersionEnum.CharsetID.getItem(self.__char).name)
        self.__cbb_lang.currentIndexChanged.connect(self.__on_lang_changed)
        self.__cbb_char.currentIndexChanged.connect(self.__on_char_changed)
        self.setStyleSheet(STYLE.getBlock().style)

    def __on_lang_changed(self) -> None:
        data = self.__cbb_lang.currentData()
        self.__lang = data
        self.valueChanged.emit()

    def __on_char_changed(self) -> None:
        data: int = self.__cbb_char.currentData()
        self.__char: int = data
        self.valueChanged.emit()

    @property
    def data(self) -> list:
        return [self.__lang, self.__char]

    @property
    def lang_str(self) -> str:
        return self.__cbb_lang.currentText()

    @property
    def char_str(self) -> str:
        return self.__cbb_char.currentText()


class DialogLanguageChar(QDialog):
    """ 
    该类是用于编辑 VarFileInfo 的语言和字符集的对话框

    该类不可以实例化, 只能通过静态方法 DialogLanguageChar.edit() 来调用

    参数: 
    - parent: 父窗口
    - data_list: 语言和字符集的列表, 格式为 [语言, 字符集, 语言, 字符集, ...], 并非是分类好的

    返回: 
    list: 格式同 data_list
    """
    @staticmethod
    def edit(parent, data_list: list) -> list:
        dialog: DialogLanguageChar = QDialog.__new__(DialogLanguageChar)
        dialog.__init__(parent, data_list)
        dialog.exec_()
        return dialog.__return

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError('Use select() method instead')

    def __init__(self, parent=None, data_list: list = []) -> None:
        super().__init__(parent)
        self.__data_list = data_list
        self.__return = []
        self.__init_ui()
        self.__init_signal_connections()

    def __init_ui(self) -> None:
        self.setModal(True)
        self.setMinimumWidth(400)
        self.setMinimumHeight(300)
        self.resize(400, 300)
        self.setWindowTitle(LM.getWord('title_Dialog_Language_Char'))
        self.setWindowIcon(QIcon(convert_svg_to_pixmap(ICON.APP_ICON)))
        widget_btn = QWidget(self)
        widget_btn.setMinimumHeight(40)
        widget_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_btn_holder = QWidget(self)
        widget_btn_holder.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_edit_btn = QWidget(self)
        widget_edit_btn.setFixedHeight(40)
        widget_edit_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_edit_btn_holder = QWidget(self)
        widget_edit_btn_holder.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout = QVBoxLayout(self)
        layout_btn = QHBoxLayout(widget_btn)
        layout_edit_btn = QHBoxLayout(widget_edit_btn)
        self.__btn_add = QPushButton(LM.getWord('add'))
        self.__btn_remove = QPushButton(LM.getWord('remove'))
        self.__btn_save = QPushButton(LM.getWord('save'))
        self.__btn_cancel = QPushButton(LM.getWord('cancel'))
        for btn in [self.__btn_add, self.__btn_remove, self.__btn_save, self.__btn_cancel]:
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.setProperty('widgetType', 'Dialog')
        self.__listWidget = QListWidget(self)
        self.__listWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__listWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.__listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        layout.addWidget(self.__listWidget)
        layout.addWidget(widget_edit_btn)
        layout.addWidget(widget_btn)
        layout.setSpacing(2)
        layout_btn.setContentsMargins(0, 0, 0, 0)
        layout_btn.setSpacing(10)
        layout_edit_btn.setContentsMargins(0, 0, 0, 0)
        layout_edit_btn.setSpacing(10)
        layout.setStretch(0, 100)
        layout.setStretch(1, 10)
        layout.setStretch(2, 10)
        layout_btn.addWidget(widget_btn_holder)
        layout_btn.addWidget(self.__btn_save)
        layout_btn.addWidget(self.__btn_cancel)
        layout_btn.setStretch(0, 100)
        layout_btn.setStretch(1, 10)
        layout_btn.setStretch(2, 10)
        layout_edit_btn.addWidget(self.__btn_add)
        layout_edit_btn.addWidget(self.__btn_remove)
        layout_edit_btn.addWidget(widget_edit_btn_holder)
        layout_edit_btn.setStretch(0, 10)
        layout_edit_btn.setStretch(1, 10)
        layout_edit_btn.setStretch(2, 100)
        self.__init_listWidget()
        self.setStyleSheet(STYLE.getBlock().style)
        self.show()

    def __init_listWidget(self) -> None:
        self.__data_list = chunk_list_by_two(self.__data_list)
        for value in self.__data_list:
            lang, char = value
            listWidget_item = QListWidgetItem(self.__listWidget)
            widget = _WidgetLanguageChar(self, lang, char)
            # widget.valueChanged.connect(self.__update_data)
            self.__listWidget.addItem(listWidget_item)
            self.__listWidget.setItemWidget(listWidget_item, widget)

    def __init_signal_connections(self) -> None:
        self.__btn_add.clicked.connect(self.__add_item)
        self.__btn_remove.clicked.connect(self.__remove_item_from_button)
        self.__btn_save.clicked.connect(self.__save_data)
        self.__btn_cancel.clicked.connect(self.__cancel_data)
        self.__listWidget.customContextMenuRequested.connect(self.__on_context_menu_show)

    def __update_data(self) -> None:
        """ 
        更新数据 获取 _WidgetLanguageChar 中的数据, 
        数据格式为: [lang, char] 其中, lang 和 char 都是数值, 如 [0x0804, 0x04B0]
        """
        self.__return = []
        for idx in range(self.__listWidget.count()):
            list_item: QListWidgetItem = self.__listWidget.item(idx)
            widget: _WidgetLanguageChar = self.__listWidget.itemWidget(list_item)
            data_list: list = widget.data
            self.__return += data_list

    def __save_data(self) -> None:
        self.__update_data()
        self.accept()

    def __cancel_data(self) -> None:
        self.__return: list = []
        self.reject()

    def __add_item(self) -> None:
        item: QListWidgetItem = QListWidgetItem()
        widget: _WidgetLanguageChar = _WidgetLanguageChar()
        self.__listWidget.addItem(item)
        self.__listWidget.setItemWidget(item, widget)

    def __remove_item_from_button(self) -> None:
        idx: int = self.__listWidget.currentRow()
        self.__remove_item(idx)

    def __remove_item_from_context_menu(self, pos: QPoint) -> None:
        item: QListWidgetItem = self.__listWidget.itemAt(pos)
        idx: int = self.__listWidget.row(item)
        self.__remove_item(idx)

    def __remove_item(self, idx: int) -> None:
        """ 
        移除项目
        """
        if idx < 0:
            return
        list_item: QListWidgetItem = self.__listWidget.item(idx)
        widget: _WidgetLanguageChar = self.__listWidget.itemWidget(list_item)
        text: str = LM.getWord('lb_new_data_tiquestion_remove_lang_char_itemle')+f'\n   - {widget.lang_str} {widget.char_str}'
        res: int = DialogMessageBox.question(self, LM.getWord('remove_lang_char_item'), text, [LM.getWord('remove')])
        if res == 0:
            self.__listWidget.takeItem(idx)
        elif res == DialogMessageBox.StandardButton.CANCEL:
            return

    def __on_context_menu_show(self, pos: QPoint) -> None:
        menu = QMenu()
        action_remove = QAction(LM.getWord('remove'))
        action_remove.setIcon(QIcon(convert_svg_to_pixmap(ICON.DELETE)))
        menu.addAction(action_remove)
        action_remove.triggered.connect(lambda: self.__remove_item_from_context_menu(pos))
        menu.exec_(self.__listWidget.mapToGlobal(pos))
