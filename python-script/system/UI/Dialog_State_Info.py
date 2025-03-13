
from PyQt5.QtWidgets import QDialog, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy,  QWidget, QLineEdit, QRadioButton, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


from const.Const_Icon import *
from const.Const_Parameter import *
from system.Struct_Pyinstaller import *
from system.Manager_Language import *
from system.Manager_Style import *
from system.Struct_Pyinstaller import StateStruct
from system.UI.Dialog_MessageBox import DialogMessageBox
from tools.data_handle import wrapped_text
from tools.image_convert import *


class DialogStateInfo(QDialog):
    """ 
    此类用于编辑状态信息

    此类不能直接实例化, 请使用 DialogStateInfo.edit() 方法

    参数: 
    - parent: 父窗口
    - struct: 状态信息结构体
    - withHash: 是否显示哈希值, 用于 --python-option 参数
    """
    @staticmethod
    def edit(parent, struct, withHash=False) -> None:
        """ 
        编辑状态信息

        参数: 
        - parent: 父窗口
        - struct: 状态信息结构体
        - withHash: 是否显示哈希值, 用于 --python-option 参数
        """
        dialog = QDialog.__new__(DialogStateInfo)
        dialog.__init__(parent, struct, withHash)
        dialog.exec_()
        return

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("This class is not intended to be instantiated. Please use the static method `edit` to open the dialog.")

    def __init__(self, parent, struct: StateStruct, withHash=False) -> None:
        super().__init__(parent)
        self.__struct: StateStruct = struct
        self.__withHash: bool = withHash
        self.__init_paramerters()
        self.__init_ui()
        self.__init_signal_connections()

    def __init_paramerters(self) -> None:
        self.__option: str = self.__struct.command_option if isinstance(self.__struct.command_option, str) else self.__struct.command_option[0]
        self.__option_value_list: list = App.Pyinstaller.DICT_STATE_WITH_PARAMS[self.__option]
        self.__widget_list: list = []

    def __init_ui(self) -> None:
        title = self.__struct.command_option if isinstance(self.__struct.command_option, str) else self.__struct.command_option[0]
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(convert_svg_to_pixmap(ICON.APP_ICON)))
        self.setModal(True)
        widget_edit = QWidget()
        widget_btn = QWidget()
        widget_btn.setMinimumHeight(50)
        widget_hash = QWidget()
        layout_hash = QHBoxLayout(widget_hash)
        widget_btn_holder = QWidget()
        layout = QVBoxLayout(self)
        self.__layout_edit = QVBoxLayout(widget_edit)
        layout_btn = QHBoxLayout(widget_btn)
        self.__btn_save = QPushButton(LM.getWord('save'))
        self.__btn_cancel = QPushButton(LM.getWord('cancel'))
        self.__btn_reset = QPushButton(LM.getWord('reset'))
        self.__btn_save.setProperty('widgetType', 'Dialog')
        self.__btn_cancel.setProperty('widgetType', 'Dialog')
        self.__btn_reset.setProperty('widgetType', 'Dialog')
        lb = QLabel()
        lb_text: str = LM.getWord('description_'+self.__struct.name)
        if lb_text:
            lb_text = wrapped_text(lb_text, App.SENTENCE_LIMIT)
        lb.setText(lb_text)
        for widget in [widget_edit, widget_btn, widget_btn_holder, self.__btn_save, self.__btn_cancel, self.__btn_reset, lb, widget_hash]:
            widget: QWidget
            widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            if isinstance(widget, QPushButton):
                widget.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__cb_hash = QCheckBox(self)
        self.__cb_hash.setText('hash_seed=')
        self.__cb_hash.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__cb_hash.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__le_hash = QLineEdit(self)
        self.__le_hash.setCursor(Qt.CursorShape.IBeamCursor)
        self.__le_hash.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(lb)
        layout.addWidget(widget_edit)
        layout.addWidget(widget_btn)
        layout_btn.addWidget(self.__btn_reset)
        layout_btn.addWidget(widget_btn_holder)
        layout_btn.addWidget(self.__btn_save)
        layout_btn.addWidget(self.__btn_cancel)
        layout_hash.addWidget(self.__cb_hash)
        layout_hash.addWidget(self.__le_hash)

        for ly in [self.__layout_edit, layout_btn, layout_hash]:
            ly: QVBoxLayout
            ly.setContentsMargins(0, 0, 0, 0)
            ly.setSpacing(10)
        layout.setStretch(0, 50)
        layout.setStretch(1, 100)
        layout.setStretch(2, 10)
        layout_btn.setStretch(0, 10)
        layout_btn.setStretch(1, 100)
        layout_btn.setStretch(2, 10)
        layout_btn.setStretch(3, 10)
        layout_hash.setStretch(0, 10)
        layout_hash.setStretch(1, 100)
        self.__init_checkbox()
        self.__layout_edit.addWidget(widget_hash)
        if not self.__withHash:
            widget_hash.hide()
        else:
            self.__widget_list.append(self.__cb_hash)
            self.__cb_hash.stateChanged.connect(self.__exclusive_checkbox)
            self.__le_hash.editingFinished.connect(self.__on_le_changed)
        self.setStyleSheet(STYLE.getBlock().style)

    def __init_checkbox(self) -> None:
        for value in self.__option_value_list:
            if value == 'hash_seed=':
                if 'hash_seed=' in self.__struct.current_state:
                    h_v: str = self.__struct.current_state.split('hash_seed=')[1].strip()
                    self.__le_hash.setText(h_v)
                    self.__cb_hash.setChecked(True)
                continue
            widget = QCheckBox(self)
            widget.setText(value)
            widget.setCursor(Qt.CursorShape.PointingHandCursor)
            widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            widget.stateChanged.connect(self.__exclusive_checkbox)
            self.__layout_edit.addWidget(widget)
            self.__widget_list.append(widget)
            if self.__struct.current_state == value:
                widget.setChecked(True)

    def __init_signal_connections(self) -> None:
        self.__btn_reset.clicked.connect(self.__reset)
        self.__btn_save.clicked.connect(self.__save)
        self.__btn_cancel.clicked.connect(self.__cancel)

    def __exclusive_checkbox(self) -> None:
        sender: QCheckBox = self.sender()
        if sender.isChecked():
            for widget in self.__widget_list:
                widget: QCheckBox
                if widget != sender:
                    widget.setChecked(False)

    def __on_le_changed(self) -> None:
        text: str = self.__le_hash.text()
        if not text.isdigit():
            text = ''.join(c for c in text if c.isdigit())
            self.__le_hash.setText(text)

    def __reset(self) -> None:
        res: int | str = DialogMessageBox.question(self, LM.getWord('reset'), LM.getWord('reset_confirm'), [LM.getWord('reset')])
        if res == DialogMessageBox.StandardButton.CANCEL:
            return
        elif res == 0:
            for widget in self.__widget_list:
                widget: QRadioButton
                widget.setChecked(False)
            self.__struct.clear_args()
        self.accept()

    def __save(self) -> None:
        existedChecking = False
        for widget in self.__widget_list:
            widget: QRadioButton
            if widget.isChecked():
                existedChecking = True
                text: str = widget.text()
                if widget == self.__cb_hash and self.__cb_hash.isChecked():
                    if self.__le_hash.text():
                        text = 'hash_seed='+self.__le_hash.text()
                    else:
                        existedChecking = False
                self.__struct.set_state(text)
        if not existedChecking:
            self.__struct.clear_args()
        self.accept()

    def __cancel(self) -> None:
        self.reject()
