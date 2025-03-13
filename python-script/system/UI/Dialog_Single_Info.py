
from PyQt5.QtWidgets import QDialog, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy, QFileDialog, QWidget, QLineEdit
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


from const.Const_Icon import *
from const.Const_Parameter import *
from system.Struct_Pyinstaller import *
from system.Manager_Language import *
from system.Manager_Style import *
from system.UI.Dialog_MessageBox import DialogMessageBox
from system.UI.Message_Notification import MessageNotification
from tools.image_convert import *
_log = Log.UI


class DialogSingleInfo(QDialog):
    """ 
    此类为单数据编辑对话框

    此类不可直接实例化, 请使用 DialogSingleInfo.edit() 方法

    参数: 
    - parent: 父窗口
    - struct: 数据结构
    - data_type: 数据类型, 用于定义输入内容方式, 显示不同的按钮, 可选值: `file` `folder` `text` 此外, 则将显示所有按钮
    - accept_file: 接受的文件类型, 用于 QFileDialog 传参, 如: `PNG File (*.png);;`
    """
    @staticmethod
    def edit(parent=None, struct=None, data_type='', accept_file=''):
        """
        编辑单数据, 虽然有返回值, 但数据实际已经在内部进行修改赋值

        参数: 
        - parent: 父窗口
        - struct: 数据结构
        - data_type: 数据类型, 用于定义输入内容方式, 显示不同的按钮, 可选值: `file` `folder` `text` 此外, 则将显示所有按钮
        - accept_file: 接受的文件类型, 用于 QFileDialog 传参, 如: `PNG File (*.png);;`

        返回: 
        - None: 无输入, 取消
        - '': 重置
        - 其他: 有效内容
        """
        dialog = QDialog.__new__(DialogSingleInfo)
        dialog.__init__(parent, struct, data_type, accept_file)
        dialog.exec()
        return dialog.__return

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("This class is not intended to be instantiated. Please use the static method `edit` to open the dialog.")

    def __init__(self, parent, struct: SingleInfoStruct, data_type='', accept_file=''):
        super().__init__(parent)
        self.__struct: SingleInfoStruct = struct
        self.__origin_data = self.__struct.command_args
        self.__return = None
        self.__data_type = data_type
        self.__accept_file = accept_file

        self.__init_parameters()
        self.__init_ui()
        self.__init_signals_connections()

    def __init_parameters(self):
        self.__command_args = self.__struct.command_args.replace('"', '')
        self.__hint_text = LM.getWord('description_'+self.__struct.name)

    def __init_ui(self):
        title = self.__struct.command_option if isinstance(self.__struct.command_option, str) else self.__struct.command_option[0]
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(convert_svg_to_pixmap(ICON.APP_ICON)))
        self.setModal(True)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowTitleHint | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
        self.resize(500, 200)
        widget_lb = QWidget(self)
        widget_lb_data = QWidget(self)
        widget_lb_new_data = QWidget(self)
        widget_edit = QWidget(self)
        widget_btn = QWidget(self)
        widget_btn_holder = QWidget(self)
        layout = QVBoxLayout(self)
        layout_lb = QVBoxLayout(widget_lb)
        layout_lb_data = QHBoxLayout(widget_lb_data)
        layout_lb_new_data = QHBoxLayout(widget_lb_new_data)
        layout_edit = QHBoxLayout(widget_edit)
        layout_btn = QHBoxLayout(widget_btn)
        lb_description = QLabel(self.__hint_text, self)
        lb_data_title = QLabel(LM.getWord('current_data_is'+': '), self)
        lb_data = QLabel(self.__command_args, self)
        lb_data.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        lb_data.setCursor(Qt.CursorShape.IBeamCursor)
        lb_new_data_title = QLabel(LM.getWord('new_data_is'+': '), self)
        self.__lb_new_data = QLabel(self)
        self.__lb_new_data.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.__lb_new_data.setCursor(Qt.CursorShape.IBeamCursor)
        self.__lineEdit = QLineEdit(self)
        self.__btn_folder = QPushButton(self)
        self.__btn_file = QPushButton(self)
        self.__btn_reset = QPushButton(LM.getWord('reset'), self)
        self.__btn_save = QPushButton(LM.getWord('save'), self)
        self.__btn_cancel = QPushButton(LM.getWord('cancel'), self)
        self.__btn_folder.setIcon(QIcon(convert_svg_to_pixmap(ICON.ADD_FOLDER)))
        self.__btn_file.setIcon(QIcon(convert_svg_to_pixmap(ICON.ADD_FILE)))
        for btn in [self.__btn_folder, self.__btn_file]:
            btn.setIconSize(QSize(30, 30))
            btn.setMaximumWidth(40)
        widget_edit.setMinimumHeight(30)
        widget_edit.setMaximumHeight(50)
        widget_btn.setMinimumHeight(30)
        widget_btn.setMaximumHeight(50)
        widget_lb.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_btn_holder.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        lb_description.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        lb_data_title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        lb_data.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__lineEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        for btn in [self.__btn_folder, self.__btn_file, self.__btn_reset, self.__btn_save, self.__btn_cancel]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_save.setProperty('widgetType', 'Dialog')
        self.__btn_cancel.setProperty('widgetType', 'Dialog')
        self.__btn_reset.setProperty('widgetType', 'Dialog')
        layout.addWidget(widget_lb)
        layout.addWidget(widget_edit)
        layout.addWidget(widget_btn)
        layout_lb.addWidget(lb_description)
        layout_lb.addWidget(widget_lb_data)
        layout_lb.addWidget(widget_lb_new_data)
        layout_lb_data.addWidget(lb_data_title)
        layout_lb_data.addWidget(lb_data)
        layout_lb_new_data.addWidget(lb_new_data_title)
        layout_lb_new_data.addWidget(self.__lb_new_data)
        layout_edit.addWidget(self.__lineEdit)
        layout_edit.addWidget(self.__btn_folder)
        layout_edit.addWidget(self.__btn_file)
        layout_btn.addWidget(self.__btn_reset)
        layout_btn.addWidget(widget_btn_holder)
        layout_btn.addWidget(self.__btn_save)
        layout_btn.addWidget(self.__btn_cancel)
        layout_lb.setContentsMargins(0, 0, 0, 0)
        layout_lb_data.setContentsMargins(0, 0, 0, 0)
        layout_lb_new_data.setContentsMargins(0, 0, 0, 0)
        layout_edit.setContentsMargins(0, 0, 0, 0)
        layout_btn.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        layout_lb.setSpacing(10)
        layout_lb_data.setSpacing(0)
        layout_lb_new_data.setSpacing(0)
        layout_edit.setSpacing(5)
        layout_btn.setSpacing(5)
        layout.setStretch(0, 100)
        layout.setStretch(1, 50)
        layout.setStretch(2, 50)
        layout_lb.setStretch(0, 100)
        layout_lb.setStretch(1, 20)
        layout_lb.setStretch(1, 30)
        layout_lb_data.setStretch(0, 1)
        layout_lb_data.setStretch(1, 100)
        layout_lb_new_data.setStretch(0, 1)
        layout_lb_new_data.setStretch(1, 100)
        layout_edit.setStretch(0, 100)
        layout_edit.setStretch(1, 10)
        layout_edit.setStretch(2, 10)
        layout_btn.setStretch(0, 1)
        layout_btn.setStretch(1, 100)
        layout_btn.setStretch(2, 1)
        layout_btn.setStretch(3, 1)
        self.__btn_cancel.setFocus(True)
        if self.__data_type == 'folder':
            self.__btn_file.hide()
        elif self.__data_type == 'file':
            self.__btn_folder.hide()
        elif self.__data_type == 'text':
            self.__btn_file.hide()
            self.__btn_folder.hide()
        self.setStyleSheet(STYLE.getBlock().style)
        self.show()

    def __init_signals_connections(self):
        self.__btn_save.clicked.connect(self.__save)
        self.__btn_cancel.clicked.connect(self.__cancel)
        self.__btn_reset.clicked.connect(self.__reset)
        self.__btn_folder.clicked.connect(self.__open_folder)
        self.__btn_file.clicked.connect(self.__open_file)
        self.__lineEdit.editingFinished.connect(self.__text_changed)

    def __text_changed(self):
        text = self.__lineEdit.text().strip().replace('\\', '/')
        _log.warning(f"__text_changed: {text}")
        if not text:
            return False
        if self.__data_type in ['file', 'folder'] and not os.path.exists(text):
            MessageNotification.showMessage(self, LM.getWord('error_path_not_exists'), hold_duration=3000, font_size_px=14)
            return False
        if self.__data_type == "folder":
            if not os.path.isdir(text):
                MessageNotification.showMessage(self, LM.getWord('should_be_folder'), hold_duration=3000, font_size_px=14)
                return False
        elif self.__data_type == "file":
            if not os.path.isfile(text):
                MessageNotification.showMessage(self, LM.getWord('should_be_file'), hold_duration=3000, font_size_px=14)
                return False
        self.__return = text
        self.__lb_new_data.setText(text)
        return True

    def __open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, LM.getWord('select_folder'), '')
        _log.critical(folder_path)
        if folder_path:
            folder_path = folder_path.replace('\\', '/').strip()
            self.__return = folder_path
            self.__lb_new_data.setText(folder_path)

    def __open_file(self):
        file_path = QFileDialog.getOpenFileName(self, LM.getWord('select_file'), '', self.__accept_file, '')[0]
        if file_path:
            file_path = file_path.replace('\\', '/').strip()
            self.__return = file_path
            self.__lb_new_data.setText(file_path)

    def __reset(self):
        res = DialogMessageBox.question(self, LM.getWord('reset'), LM.getWord('reset_confirm'), [LM.getWord('reset')])
        if res == 0:
            self.__return = ''
            self.__struct.clear_args()
        elif res == DialogMessageBox.StandardButton.CANCEL:
            return
        self.accept()

    def __save(self) -> None:
        if self.__lineEdit.text().strip():
            res = DialogMessageBox.question(self, LM.getWord('data_not_save'), LM.getWord('question_data_not_save'), [LM.getWord('save'), LM.getWord('discard')])
            if res == 0:
                result = self.__text_changed()
                if result is False:
                    return
            elif res == 1:
                pass
            elif res == DialogMessageBox.StandardButton.CANCEL:
                return
        if self.__return == '' or self.__return is None:
            self.accept()
        if self.__return != self.__origin_data:
            self.__struct.set_args(self.__return)
        self.accept()

    def __cancel(self) -> None:
        self.reject()
