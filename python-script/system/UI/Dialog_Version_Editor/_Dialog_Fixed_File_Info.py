

from PyQt5.QtWidgets import QDialog, QVBoxLayout,  QPushButton, QCheckBox, QGroupBox, QHBoxLayout,  QWidget, QSizePolicy, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from const.Const_Icon import *
from const.Const_Version_File import *
from const.Const_Parameter import *
from system.Manager_Language import *
from system.Manager_Style import *
from tools import *
_log = Log.UI


class DialogFFI(QDialog):
    """ 
    该类是处理/显示固定文件信息的对话框.

    只能通过 DialogFFI.edit() 方法来显示对话框, 不能对其实例化
    """
    @staticmethod
    def edit(parent, title: str, content_dict: dict, isMultiParams: bool = False, isOS: bool = False) -> int | None:
        """
        显示一个对话框, 用于选择单/多个参数.

        参数: 
        - content_dict
            - key: 显示文字
            - value: 
                - hint: 提示文字
                - value: 枚举值
                - state: 是否选中
        - isMultiParams: 是否多选, 文件操作系统和文件标志使用多选
        - isOS: 是否是编辑文件操作系统

        返回: 
        - 数值(int|None), 多选的话, 将会对所有数值取或运算值, None 表示没有选择任何内容
        """
        dialog: DialogFFI = QDialog.__new__(DialogFFI)
        dialog.__init__(parent, title, content_dict, isMultiParams, isOS=isOS)
        dialog.exec_()
        return dialog.__return

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("This class is not intended to be instantiated.")

    def __init__(self, parent, title: str, content_dict: dict, isMultiParams: bool = False, isOS: bool = False) -> None:
        super().__init__(parent)
        self.__content_dict: dict = content_dict
        self.__isMultiParams: bool = isMultiParams
        self.__return = None
        self.resize(600, 400)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(convert_svg_to_pixmap(ICON.APP_ICON)))
        self.__init_ui_general() if not isOS else self.__init_ui_os()

    def __init_ui(self) -> None:
        """ 
        UI 通用部分
        """
        widget_content = QWidget(self)
        widget_content.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_button = QWidget(self)
        widget_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_button.setFixedHeight(40)
        layout_main = QVBoxLayout(self)
        self.__layout_content = QVBoxLayout(widget_content)
        layout_button = QHBoxLayout(widget_button)
        widget_holder_btn = QWidget(self)
        widget_holder_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn_save = QPushButton(LM.getWord('save'), self)
        btn_save.setProperty('widgetType', 'Dialog')
        btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_save.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn_save.clicked.connect(self.__save)
        btn_cancel = QPushButton(LM.getWord('cancel'), self)
        btn_cancel.setProperty('widgetType', 'Dialog')
        btn_cancel.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_cancel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn_cancel.clicked.connect(self.__cancel)
        layout_button.setContentsMargins(0, 0, 0, 0)
        layout_button.setSpacing(10)
        layout_button.addWidget(widget_holder_btn)
        layout_button.addWidget(btn_save)
        layout_button.addWidget(btn_cancel)
        layout_button.setStretch(0, 100)
        layout_button.setStretch(1, 10)
        layout_button.setStretch(2, 10)
        layout_main.setSpacing(0)
        layout_main.addWidget(widget_content)
        layout_main.addWidget(widget_button)
        layout_main.setStretch(0, 100)
        layout_main.setStretch(1, 10)
        self.__input_widget_list = []

    def __init_ui_general(self) -> None:
        """ 
        非 OS 部分, 因为 OS 需要分组
        """
        self.__init_ui()
        if not self.__isMultiParams:
            radio_group = QButtonGroup(self)
        for key, value in self.__content_dict.items():
            key: str
            value: dict
            hint = value.get('hint', '')
            status: str = value.get('status')
            enum_value: int = value.get('value')
            if self.__isMultiParams:
                input_widget = QCheckBox(self)
            else:
                input_widget = QRadioButton(self)
                radio_group.addButton(input_widget)
            hint_phrase = f'(<0x{enum_value:08X}>{hint})' if hint else ''
            if len(hint_phrase) > App.SENTENCE_LIMIT:
                hint_phrase = wrapped_text(hint, App.SENTENCE_LIMIT, ' ' * len(key))
            input_widget.setText(f'{key} {hint_phrase}')
            input_widget.setChecked(status)
            input_widget.setCursor(Qt.CursorShape.PointingHandCursor)
            self.__input_widget_list.append(input_widget)
            self.__layout_content.addWidget(input_widget)
        self.setStyleSheet(STYLE.getBlock().style)

    def __init_ui_os(self) -> None:
        """ 
        OS 部分
        """
        def __update_unknown_os_state() -> None:
            """ 
            控制三个部分的勾选框的互斥 

            main_os 与 sub_os 不互斥, 但是各自内部块中的勾选框互斥

            当 Unknown 被勾选时, 如果 main_os 和 sub_os 都被勾选, 那么 main_os 和 sub_os 则被取消勾选. 如果 main_os 和 sub_os 都没有被勾选, 那么 Unknown 则被勾选. 

            当 Unknown 被勾选时, 如果 main_os 和 sub_os 至少有一个没有被勾选, 则不会有任何操作
            """
            nonlocal cb_unknown
            sender: QCheckBox = self.sender()
            # main_os 控制部分
            if sender in self.__group_main_os:
                if sender.isChecked():
                    for widget_item in self.__group_main_os:
                        widget_item: QCheckBox
                        widget_item.setChecked(False)
                    sender.setChecked(True)
                    self.__main_selected = True
                else:
                    self.__main_selected = False
            # sub_os 控制部分
            elif sender in self.__group_sub_os:
                if sender.isChecked():
                    for widget_item in self.__group_sub_os:
                        widget_item: QCheckBox
                        widget_item.setChecked(False)
                    sender.setChecked(True)
                    self.__sub_selected = True
                else:
                    self.__sub_selected = False
            # unknown 控制部分
            if sender == cb_unknown and cb_unknown.isChecked() and self.__main_selected and self.__sub_selected:
                for widget_item in self.__input_widget_list:
                    widget_item: QCheckBox
                    widget_item.setChecked(False)
                cb_unknown.setChecked(True)
                self.__main_selected = False
                self.__sub_selected = False
            if self.__main_selected or self.__sub_selected:
                cb_unknown.setChecked(False)
            elif not self.__main_selected and not self.__sub_selected:
                cb_unknown.setChecked(True)
        # OS UI 部分
        self.__init_ui()
        gb_main_os = QGroupBox(LM.getWord('file_os_main'), self)
        gb_sub_os = QGroupBox(LM.getWord('file_os_sub'), self)
        self.__group_main_os = []
        self.__group_sub_os = []
        self.__main_selected = False
        self.__sub_selected = False
        layout_main_os = QVBoxLayout(gb_main_os)
        layout_sub_os = QVBoxLayout(gb_sub_os)
        unknown_os_text = ''
        for key, value in self.__content_dict.items():
            key: str
            value: dict
            hint: str = value.get('hint', '')
            status: str = value.get('status')
            enum_value: int = value.get('value')
            hint = value.get('hint', '')
            hint_phrase = f'(<0x{enum_value:08X}>{hint})' if hint else ''
            if len(hint_phrase) > App.SENTENCE_LIMIT:
                hint_phrase = wrapped_text(hint, App.SENTENCE_LIMIT, ' ' * len(key))
            widget_text = f'{key} {hint_phrase}'
            if enum_value == VersionEnum.FileOS.VOS_UNKNOWN:
                unknown_os_text = widget_text
                continue
            elif enum_value >= 1 << 2**4:
                input_widget = QCheckBox(self)
                layout_main_os.addWidget(input_widget)
                self.__group_main_os.append(input_widget)
                if status:
                    self.__main_selected = True
            else:
                input_widget = QCheckBox(self)
                layout_sub_os.addWidget(input_widget)
                self.__group_sub_os.append(input_widget)
                if status:
                    self.__sub_selected = True
            input_widget.setText(widget_text)
            if status:
                input_widget.setChecked(status)
            input_widget.setCursor(Qt.CursorShape.PointingHandCursor)
            input_widget.stateChanged.connect(__update_unknown_os_state)
            self.__input_widget_list.append(input_widget)
        cb_unknown = QCheckBox(self)
        cb_unknown.setText(unknown_os_text)
        cb_unknown.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__input_widget_list.append(cb_unknown)
        cb_unknown.stateChanged.connect(__update_unknown_os_state)
        self.__layout_content.addWidget(cb_unknown)
        self.__layout_content.addWidget(gb_main_os)
        self.__layout_content.addWidget(gb_sub_os)
        self.setStyleSheet(STYLE.getBlock().style)

    def __save(self) -> None:
        value = 0
        isSelected = False
        for item in self.__input_widget_list:
            item: QCheckBox | QRadioButton
            if item.isChecked():
                isSelected = True
                key = item.text().split(' ')[0]
                dict_value = self.__content_dict[key]['value']
                value |= dict_value
        self.__return: int | None = value if isSelected else None
        self.accept()

    def __cancel(self) -> None:
        self.reject()
