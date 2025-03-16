
import functools
import subprocess
from PyQt5.QtWidgets import QDialog, QAbstractItemView, QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy, QTextEdit, QMenu, QFileDialog, QFileIconProvider, QTableWidgetSelectionRange, QApplication
from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QEvent, QObject, QSize, QFileInfo, QRect
from PyQt5.QtGui import QIcon, QDragMoveEvent, QTextCursor


from const.Const_Icon import *
from const.Const_Parameter import *
from const.Const_Version_File import *
from system.Struct_Pyinstaller import MultiInfoStruct
from system.UI.Dialog_MessageBox import DialogMessageBox
from system.Struct_Pyinstaller import *
from system.Manager_Language import *
from system.Manager_Style import *
from tools.image_convert import *

_log = Log.UI


class _FilterTextEdit(QObject):
    """
    TextEdit 换行过滤器

    `shift` + `enter`: 换行

    `ctrl` + `enter`: 提交
    """

    def __init__(self, parent, watched: QTextEdit, callback_func) -> None:
        super().__init__(parent)
        self.__watched: QTextEdit = watched
        self.__callback_func = callback_func

    def eventFilter(self, source, event) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Return and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
                self.__callback_func()
            elif event.key() == Qt.Key.Key_Return and event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
                cursor: QTextCursor = self.__watched.textCursor()
                cursor.movePosition(QTextCursor.MoveOperation.EndOfLine)
                cursor.insertText("\n")
                self.__watched.setTextCursor(cursor)
                return True
        return super().eventFilter(source, event)


class _TableWidget(QTableWidget):
    """ 
    可拖拽排序的 TableWidget, 数据行不会对调, 而是插入, 支持顶端/低端自动移动滚动条

    参数: 
    - parent: 父窗口
    - scroll_threshold: 滚动阈值, 当鼠标拖拽超过这个值时, 自动滚动滚动条. 当数值超过表格高度或小于等于0时, 则阈值默认为表格一半高度, 初始默认为:0

    信号: 
    - rowDragged: 行拖拽信号, 参数为 (拖拽起始行, 结束目标行)
    - cellEditingFinished: 单元格编辑完成信号, 参数为 (行, 列)
    """
    rowDragged = pyqtSignal(int, int)
    cellEditingFinished = pyqtSignal(int, int)

    def __init__(self, parent=None, scroll_threshold: int = 0) -> None:
        super().__init__(parent)
        self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.scroll_timer = QTimer()
        self.scroll_timer.setInterval(50)  # 每100ms检查一次滚动
        self.scroll_timer.timeout.connect(self.__on_scroll)
        self.cellChanged.connect(self.__on_cell_changed)
        self.__isDragging: bool = False
        self.__drag_start_row: int = -1
        self.__drag_end_row: int = -1
        self.__scroll_direction: None | str = None
        self.__scroll_threshold: int = scroll_threshold

    def startDrag(self, dropActions) -> None:
        self.__drag_start_row = self.currentRow()
        self.__isDragging = True
        super().startDrag(dropActions)

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        mouse_pos = event.pos()
        top_row_height: int = self.rowHeight(0)
        bottom_row_height: int = self.rowHeight(self.rowCount() - 1)
        default_threshold = top_row_height / 2 if mouse_pos.y() < self.height() / 2 else bottom_row_height / 2
        scroll_threshold = default_threshold if self.__scroll_threshold <= 0 or default_threshold <= self.__scroll_threshold else self.__scroll_threshold
        rect = self.viewport().rect()
        if mouse_pos.y() < scroll_threshold:
            self.__scroll_direction = 'up'
            self.scroll_timer.start()
        elif mouse_pos.y() > rect.height() - scroll_threshold:
            self.__scroll_direction = 'down'
            self.scroll_timer.start()
        else:
            self.__scroll_direction = None
            self.scroll_timer.stop()

    def dropEvent(self, event) -> None:
        self.__drag_end_row = self.indexAt(event.pos()).row()
        if self.__drag_start_row == -1 or self.__drag_end_row == -1 or self.__drag_start_row == self.__drag_end_row:
            return

        row_rect: QRect = self.visualRect(self.indexAt(event.pos()))
        row_top: int = row_rect.top()
        relative_y: int = event.pos().y() - row_top
        row_half: float = self.rowHeight(self.__drag_end_row) / 2

        # 判断插入位置
        insert_row: int = self.__drag_end_row
        if relative_y >= row_half:
            insert_row += 1

        dropped_row = [self.takeItem(self.__drag_start_row, col) for col in range(self.columnCount())]
        self.removeRow(self.__drag_start_row)

        if self.__drag_start_row < insert_row:
            insert_row -= 1

        self.insertRow(insert_row)
        for col, item in enumerate(dropped_row):
            self.setItem(insert_row, col, item)

        self.clearSelection()
        self.setRangeSelected(QTableWidgetSelectionRange(insert_row, 0, insert_row, self.columnCount() - 1), True)
        self.rowDragged.emit(self.__drag_start_row, insert_row)
        self.__isDragging = False

    def __on_cell_changed(self, row: int, column: int):
        if self.__isDragging:
            return
        self.cellEditingFinished.emit(row, column)

    def __on_scroll(self):
        if self.__scroll_direction == 'up':
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - 10)
        elif self.__scroll_direction == 'down':
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + 10)


class DialogMultiArgs(QDialog):
    """ 
    此类用于显示多参数(文字/路径)对话框

    此类不能直接实例化, 必须通过 DialogMultiArgs.edit() 方法来使用

    参数: 
    - parent: 父窗口
    - data_struct: 数据结构
    - data_type: 数据类型, 可选值为 'file', 'folder', 'both', 默认为 '', 不显示文件/文件夹选择按钮
    """
    @staticmethod
    def edit(parent, data_struct: MultiInfoStruct, data_type: str = '') -> MultiInfoStruct:
        """ 
        编辑多参数(文字/路径)对话框, 数据将在内部修改, 无需外部处理, 但仍返回修改的数据类

        参数: 
        - parent: 父窗口
        - data_struct: 数据结构
        - data_type: 数据类型, 可选值为 'file', 'folder', 'both', 默认为 '', 不显示文件/文件夹选择按钮

        返回: 
        - data_struct: 数据结构
        """
        dialog = QDialog.__new__(DialogMultiArgs)
        dialog.__init__(parent, data_struct, data_type)
        dialog.exec_()
        return dialog.__data_struct

    def __new__(cls, *args, **kwargs):
        raise TypeError("Cannot instantiate directly. Use DialogMultiArgs.edit(...) instead.")

    def __init__(self, parent, data_struct: MultiInfoStruct, data_type: str = '') -> None:
        super().__init__(parent)
        self.__parent = parent
        self.__data_struct: MultiInfoStruct = data_struct
        self.__path_mode = data_type
        self.__init_parameters()
        self.__init_ui()
        self.__init_signal_connections()
        filter_textEdit = _FilterTextEdit(self, self.__textEdit, self.__on_add)
        self.__textEdit.installEventFilter(filter_textEdit)
        self.__load_data_to_table()

    def __init_parameters(self):
        self.__isEditing = False
        self.__data: list | str = self.__data_struct.command_args
        self.__origin_data: list | str = copy.deepcopy(self.__data)
        self.__command_option: str = self.__data_struct.command_option if isinstance(self.__data_struct.command_option, str) else self.__data_struct.command_option[0]
        self.__command_name = self.__data_struct.name

    def __init_ui(self) -> None:
        title_editing = LM.getWord('title_editing')
        win_title = f'{title_editing}: {self.__command_option}'
        self.setModal(True)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowTitleHint | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
        self.setWindowTitle(win_title)
        self.setWindowIcon(QIcon(convert_svg_to_pixmap(ICON.APP_ICON)))
        self.resize(600, 600)
        layout_main = QVBoxLayout(self)
        layout_title = QVBoxLayout()
        layout_textEdit = QHBoxLayout()
        layout_textEdit_button = QVBoxLayout()
        layout_putton = QHBoxLayout()
        self.__label_title = QLabel(self)
        self.__label_title.setText(LanguageManager.getWord('description_' + self.__command_name))  # 此处应写入说明
        self.__label_command_option = QLabel(self)
        self.__label_command_option.setText(f' {self.__command_option} =')
        self.__tableWidget = _TableWidget(self)
        self.__tableWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__textEdit = QTextEdit(self)
        self.__textEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__textEdit.setPlaceholderText(LanguageManager.getWord('dialog_multi_arguments_textEdit_placeholder_text'))
        widget_holder_textEdit = QWidget(self)
        widget_holder_textEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_holder_pushbutton = QWidget(self)
        widget_holder_pushbutton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_save = QPushButton(LM.getWord('save'), self)
        self.__btn_cancel = QPushButton(LM.getWord('cancel'), self)
        self.__btn_add = QPushButton(self)
        self.__btn_delete = QPushButton(self)
        self.__btn_add_file = QPushButton(self)
        self.__btn_add_folder = QPushButton(self)
        self.__btn_save.setProperty('widgetType', 'Dialog')
        self.__btn_cancel.setProperty('widgetType', 'Dialog')
        self.__btn_add.setIcon(QIcon(convert_svg_to_pixmap(ICON.PLUS)))
        self.__btn_delete.setIcon(QIcon(convert_svg_to_pixmap(ICON.DELETE)))
        self.__btn_add_file.setIcon(QIcon(convert_svg_to_pixmap(ICON.ADD_FILE)))
        self.__btn_add_folder.setIcon(QIcon(convert_svg_to_pixmap(ICON.ADD_FOLDER)))

        for btn in [self.__btn_save, self.__btn_cancel, self.__btn_add, self.__btn_delete, self.__btn_add_file, self.__btn_add_folder]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            if btn in [self.__btn_add, self.__btn_delete, self.__btn_add_file, self.__btn_add_folder]:
                btn.setIconSize(QSize(btn.height()-10, btn.height()-10))
                btn.setFixedSize(self.__btn_add.height(), self.__btn_add.height())

        layout_main.addLayout(layout_title)
        layout_main.addWidget(self.__tableWidget)
        layout_main.addLayout(layout_textEdit)
        layout_main.addLayout(layout_putton)
        layout_title.addWidget(self.__label_title)
        layout_title.addWidget(self.__label_command_option)
        layout_textEdit.addWidget(self.__textEdit)
        layout_textEdit.addLayout(layout_textEdit_button)
        layout_textEdit_button.addWidget(self.__btn_add)
        layout_textEdit_button.addWidget(self.__btn_add_file)
        layout_textEdit_button.addWidget(self.__btn_add_folder)
        layout_textEdit_button.addWidget(self.__btn_delete)
        layout_textEdit_button.addWidget(widget_holder_textEdit)
        layout_putton.addWidget(widget_holder_pushbutton)
        layout_putton.addWidget(self.__btn_save)
        layout_putton.addWidget(self.__btn_cancel)
        layout_main.setStretch(0, 10)
        layout_main.setStretch(1, 100)
        layout_main.setStretch(2, 50)
        layout_main.setStretch(3, 10)
        layout_textEdit.setStretch(0, 100)
        layout_textEdit.setStretch(1, 0)
        layout_textEdit_button.setStretch(0, 10)
        layout_textEdit_button.setStretch(1, 10)
        layout_textEdit_button.setStretch(2, 100)
        layout_putton.setStretch(0, 100)
        layout_putton.setStretch(1, 10)
        layout_putton.setStretch(2, 10)
        self.__tableWidget.setColumnCount(1)
        self.__tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.__tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.__tableWidget.horizontalHeader().setStretchLastSection(True)
        self.__tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.__tableWidget.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.__tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.__tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.__tableWidget.setHorizontalHeaderLabels([LanguageManager.getWord('argument_value')])
        self.__tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.__tableWidget.verticalHeader().setVisible(False)
        if self.__path_mode == 'file':
            self.__btn_add_folder.hide()
        elif self.__path_mode == 'folder':
            self.__btn_add_file.hide()
        elif self.__path_mode == 'both':
            pass
        else:
            self.__btn_add_file.hide()
            self.__btn_add_folder.hide()
        self.setStyleSheet(STYLE.getBlock().style)
        self.__tableWidget.verticalScrollBar().setStyleSheet(STYLE.getBlock('~scrollbar').style)
        self.show()

    def __init_signal_connections(self) -> None:
        self.__tableWidget.cellEditingFinished.connect(self.__on_cell_changed)
        self.__tableWidget.rowDragged.connect(self.__on_dragged)
        self.__tableWidget.customContextMenuRequested.connect(self.__on_context_menu)
        self.__btn_add.clicked.connect(self.__on_add)
        self.__btn_delete.clicked.connect(self.__on_delete)
        self.__btn_add_file.clicked.connect(self.__on_add_file)
        self.__btn_add_folder.clicked.connect(self.__on_add_folder)
        self.__btn_save.clicked.connect(self.__accept)
        self.__btn_cancel.clicked.connect(self.__cancel)

    def __load_data_to_table(self) -> None:
        """ 
        加载数据到表格
        """
        self.__isEditing = True
        length = len(self.__data)
        self.__tableWidget.clearContents()
        self.__tableWidget.setRowCount(length)
        for index, item in enumerate(self.__data):
            table_item = QTableWidgetItem(item)
            self.__tableWidget.setItem(index, 0, table_item)
        self.__isEditing = False

    def __on_add(self) -> None:
        text = self.__textEdit.toPlainText()
        self.__textEdit.clear()
        if not text:
            return
        if ';' in text:
            text_splited = text.split(';')
        else:
            text_splited = text.split('\n')
        for item in text_splited:
            item = item.strip()
            if not item:
                continue
            if item not in self.__data:
                self.__data.append(item)
        self.__load_data_to_table()

    def __on_delete(self):
        selected_indexes = self.__tableWidget.selectionModel().selectedRows()
        for index in selected_indexes:
            if self.__tableWidget.item(index.row(), 0) is None:
                continue
            # self.__tableWidget.removeRow(index.row())
            del self.__data[index.row()]
            self.__load_data_to_table()

    def __on_add_file(self):
        file_path_list = QFileDialog.getOpenFileNames(self, LanguageManager.getWord('open_file'), '', 'Text Files (*.txt)')[0]
        if not file_path_list:
            return
        for file_path in file_path_list:
            self.__data.append(file_path.replace('\\', '/'))
        self.__load_data_to_table()

    def __on_add_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, LanguageManager.getWord('open_folder'), '')
        if not folder_path:
            return
        self.__data.append(folder_path.replace('\\', '/'))
        self.__load_data_to_table()

    def __on_context_menu(self, position):
        menu = QMenu()
        action_delete = menu.addAction(LanguageManager.getWord('delete'))
        action_delete.setIcon(QIcon(convert_svg_to_pixmap(ICON.DELETE)))
        action_delete.triggered.connect(self.__on_delete)
        menu.exec_(self.__tableWidget.mapToGlobal(position))

    def __on_cell_changed(self, row: int, column: int) -> None:
        if self.__isEditing:
            return
        item: QTableWidgetItem = self.__tableWidget.item(row, column)
        if item.text() in self.__data:
            del self.__data[row]
            self.__tableWidget.removeRow(row)
            return
        self.__data[row] = item.text()

    def __on_dragged(self, startRow: int,  endRow: int) -> None:
        start_text: str = self.__data[startRow]
        end_text: str = self.__data[endRow]
        self.__data[startRow] = end_text
        self.__data[endRow] = start_text

    def __accept(self) -> None:
        if self.__textEdit.toPlainText():
            result = DialogMessageBox.question(
                self,
                LanguageManager.getWord('exist_not_add'),
                LanguageManager.getWord('if_add_not_add'),
                [LanguageManager.getWord('add'), LanguageManager.getWord('not_add')]
            )
            if result == DialogMessageBox.StandardButton.CANCEL:
                return
            elif result == 0:
                self.__on_add()
                self.__accept()
        if self.__data != self.__origin_data:
            self.__data_struct.set_args(self.__data)
        self.accept()

    def __cancel(self) -> None:
        self.reject()


class DialogMultiRelativePath(QDialog):
    """ 
    此类用于显示多相对路径对话框, 用于 --add-data 和 --add-binary

    此类不能直接实例化, 必须通过 DialogMultiRelativePath.edit() 方法来使用

    参数: 
    - parent: 父窗口
    - data_struct: 数据结构
    """
    @staticmethod
    def edit(parent, data_struct: MultiInfoStruct) -> MultiInfoStruct:
        """ 
        编辑多相对路径对话框, 数据将在内部修改, 无需外部处理, 但仍返回修改的数据类

        参数: 
        - parent: 父窗口
        - data_struct: 数据结构

        返回:
        - data_struct: 修改后的数据结构
        """
        dialog = QDialog.__new__(DialogMultiRelativePath)
        dialog.__init__(parent, data_struct)
        dialog.exec_()
        return dialog.__data_struct

    def __new__(cls, *args, **kwargs):
        raise TypeError("Cannot instantiate directly. Use DialogMultiRelativePath.edit(...) instead.")

    def __init__(self, parent, data_struct: MultiInfoStruct) -> None:
        super().__init__(parent)
        self.__parent = parent
        self.__data_struct: MultiInfoStruct = data_struct
        self.__init_parameters()
        self.__init_ui()
        self.__init_signal_connections()
        self.__load_data_to_table()

    def __init_parameters(self):
        self.__isEditing = False
        self.__data: list | str = self.__data_struct.command_args
        self.__origin_data: list | str = copy.deepcopy(self.__data)
        self.__command_option: str = self.__data_struct.command_option if isinstance(self.__data_struct.command_option, str) else self.__data_struct.command_option[0]
        self.__command_name = self.__data_struct.name

    def __init_ui(self) -> None:
        title_editing = LM.getWord('title_editing')
        win_title = f'{title_editing}: {self.__command_option}'
        self.setModal(True)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowTitleHint | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
        self.setWindowTitle(win_title)
        self.setWindowIcon(QIcon(convert_svg_to_pixmap(ICON.APP_ICON)))
        self.resize(800, 600)
        layout_main = QVBoxLayout(self)
        layout_title = QVBoxLayout()
        layout_edit_button = QHBoxLayout()
        layout_putton = QHBoxLayout()
        self.__label_title = QLabel(self)
        self.__label_title.setText(LanguageManager.getWord('description_' + self.__command_name))  # 此处应写入说明
        self.__label_command_option = QLabel(self)
        self.__label_command_option.setText(f' {self.__command_option} =')
        self.__tableWidget = _TableWidget(self)
        self.__tableWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        widget_holder_edit_button = QWidget(self)
        widget_holder_edit_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_holder_pushbutton = QWidget(self)
        widget_holder_pushbutton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_save = QPushButton(LM.getWord('save'), self)
        self.__btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_save.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_cancel = QPushButton(LM.getWord('cancel'), self)
        self.__btn_cancel.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_cancel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_add_files = QPushButton(self)
        self.__btn_add_folders = QPushButton(self)
        self.__btn_add_folders.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_add_folders.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_delete = QPushButton(self)
        self.__btn_delete.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_delete.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_add_files.setIcon(QIcon(convert_svg_to_pixmap(ICON.ADD_FILE)))
        self.__btn_add_folders.setIcon(QIcon(convert_svg_to_pixmap(ICON.ADD_FOLDER)))
        self.__btn_delete.setIcon(QIcon(convert_svg_to_pixmap(ICON.DELETE)))
        for btn in [self.__btn_add_files, self.__btn_add_folders, self.__btn_delete]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.setFixedSize(btn.height(), btn.height())
            btn.setIconSize(QSize(btn.height()-10, btn.height()-10))

        self.__btn_save.setProperty('widgetType', 'Dialog')
        self.__btn_cancel.setProperty('widgetType', 'Dialog')

        layout_main.addLayout(layout_title)
        layout_main.addWidget(self.__tableWidget)
        layout_main.addLayout(layout_edit_button)
        layout_main.addLayout(layout_putton)
        layout_title.addWidget(self.__label_title)
        layout_title.addWidget(self.__label_command_option)
        layout_edit_button.addWidget(self.__btn_add_files)
        layout_edit_button.addWidget(self.__btn_add_folders)
        layout_edit_button.addWidget(self.__btn_delete)
        layout_edit_button.addWidget(widget_holder_edit_button)
        layout_putton.addWidget(widget_holder_pushbutton)
        layout_putton.addWidget(self.__btn_save)
        layout_putton.addWidget(self.__btn_cancel)

        layout_main.setStretch(0, 10)
        layout_main.setStretch(1, 100)
        layout_main.setStretch(2, 10)
        layout_main.setStretch(3, 10)
        layout_edit_button.setStretch(0, 10)
        layout_edit_button.setStretch(1, 10)
        layout_edit_button.setStretch(2, 0)
        layout_edit_button.setStretch(3, 100)
        layout_putton.setStretch(0, 100)
        layout_putton.setStretch(1, 10)
        layout_putton.setStretch(2, 10)

        self.__tableWidget.setColumnCount(3)
        self.__tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.__tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.__tableWidget.horizontalHeader().setStretchLastSection(True)
        self.__tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.__tableWidget.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.__tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.__tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.__tableWidget.setHorizontalHeaderLabels([LanguageManager.getWord('argument_value'), LM.getWord('type'), LM.getWord('origin_path')])
        self.__tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.__tableWidget.setColumnWidth(0, 240)
        self.__tableWidget.setColumnWidth(1, 60)
        self.setStyleSheet(STYLE.getBlock().style)
        self.__tableWidget.verticalScrollBar().setStyleSheet(STYLE.getBlock('~scrollbar').style)
        self.__tableWidget.verticalHeader().setVisible(False)
        self.show()

    def __init_signal_connections(self) -> None:
        self.__tableWidget.cellEditingFinished.connect(self.__on_cell_changed)
        self.__tableWidget.rowDragged.connect(self.__on_dragged)
        self.__tableWidget.customContextMenuRequested.connect(self.__on_context_menu)
        self.__btn_add_files.clicked.connect(self.__on_add_files)
        self.__btn_add_folders.clicked.connect(self.__on_add_folder)
        self.__btn_delete.clicked.connect(self.__on_delete)
        self.__btn_save.clicked.connect(self.__accept)
        self.__btn_cancel.clicked.connect(self.__cancel)

    def __load_data_to_table(self) -> None:
        """ 加载数据到表格 """
        self.__isEditing = True
        length = len(self.__data)
        self.__tableWidget.clearContents()
        self.__tableWidget.setRowCount(length)
        icon_provider = QFileIconProvider()
        for index, item in enumerate(self.__data):
            param_item = QTableWidgetItem(item)
            abspath = get_absolute_path(item)
            abspath_item = QTableWidgetItem(abspath)
            data_tyle = LM.getWord('file') if os.path.isfile(abspath) else LM.getWord('folder')
            type_item = QTableWidgetItem(data_tyle)
            type_item.setFlags(type_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            file_info = QFileInfo(abspath)
            icon = icon_provider.icon(file_info)
            param_item.setIcon(icon)
            self.__tableWidget.setItem(index, 0, param_item)
            self.__tableWidget.setItem(index, 1, type_item)
            self.__tableWidget.setItem(index, 2, abspath_item)
        self.__isEditing = False

    def __on_add_files(self) -> None:
        file_name_list, _ = QFileDialog.getOpenFileNames(self, LM.getWord('select_file'), '')
        isAdded = False
        if not file_name_list:
            return
        for file_name in file_name_list:
            relpath = get_relative_path(file_name)
            if relpath in self.__data:
                continue
            self.__data.append(relpath)
            isAdded = True
        if isAdded:
            self.__load_data_to_table()

    def __on_add_folder(self) -> None:
        folder_path = QFileDialog.getExistingDirectory(self, LM.getWord('select_folder'), '')
        if not folder_path:
            return
        relpath = get_relative_path(folder_path)
        if relpath in self.__data:
            return
        self.__data.append(relpath)
        self.__load_data_to_table()

    def __on_delete(self):
        selected_indexes = self.__tableWidget.selectionModel().selectedRows()
        for index in selected_indexes:
            if self.__tableWidget.item(index.row(), 0) is None:
                continue
            # self.__tableWidget.removeRow(index.row())
            del self.__data[index.row()]
            self.__load_data_to_table()

    def __on_copy(self, item: QTableWidgetItem):
        folder_path: str = os.path.normpath(self.__tableWidget.item(item.row(), 2).text()).replace('\\', '/')
        QApplication.clipboard().setText(folder_path)

    def __on_context_menu(self, position):
        item: QTableWidgetItem = self.__tableWidget.itemAt(position)
        if item is None:
            return
        menu = QMenu()
        action_copy = menu.addAction(LanguageManager.getWord('copy_path'))
        # action_copy.setIcon(QIcon(convert_svg_to_pixmap(ICON.COPY)))
        action_open_folder = menu.addAction(LanguageManager.getWord('open_folder'))
        action_open_folder.setIcon(QIcon(convert_svg_to_pixmap(ICON.FOLDER)))
        action_delete = menu.addAction(LanguageManager.getWord('delete'))
        action_delete.setIcon(QIcon(convert_svg_to_pixmap(ICON.DELETE)))
        action_copy.triggered.connect(lambda: self.__on_copy(item))
        action_open_folder.triggered.connect(lambda: self.__open_folder(item))
        action_delete.triggered.connect(self.__on_delete)
        menu.exec_(self.__tableWidget.mapToGlobal(position))

    def __open_folder(self, item: QTableWidgetItem):
        folder_path = os.path.normpath(self.__tableWidget.item(item.row(), 2).text())
        subprocess.Popen(f'explorer /select,"{folder_path}"')

    def __on_cell_changed(self, row: int, column: int) -> None:
        if self.__isEditing:
            return
        item: QTableWidgetItem = self.__tableWidget.item(row, column)
        if column == 0:
            if not os.path.exists(get_absolute_path(item.text())):
                self.__handle_path_error()
                return
            text = item.text()
        elif column == 2:
            data_path = item.text().strip('"').strip("'").strip()
            if not os.path.exists(data_path):
                self.__handle_path_error()
                return
            text = get_relative_path(data_path)
        if text in self.__data:
            del self.__data[row]
        self.__data[row] = text
        self.__load_data_to_table()

    def __handle_path_error(self):
        DialogMessageBox.warning(self, LM.getWord('error_invalid_path'))
        self.__load_data_to_table()

    def __on_dragged(self, startRow: int,  endRow: int) -> None:
        start_text: str = self.__data[startRow]
        end_text: str = self.__data[endRow]
        self.__data[startRow] = end_text
        self.__data[endRow] = start_text

    def __accept(self) -> None:
        if self.__data != self.__origin_data:
            self.__data_struct.set_args(self.__data)
        self.accept()

    def __cancel(self) -> None:
        self.reject()


class DialogMultiResourcePath(QDialog):
    """ 
    编辑多资源对话框, 数据将在内部修改, 无需外部处理, 但仍返回修改的数据类, 针对 --resource 参数

    参数: 
    - parent: 父窗口
    - data_struct: 数据结构

    返回:
    - data_struct: 修改后的数据结构
    """
    @staticmethod
    def edit(parent, data_struct: MultiInfoStruct) -> MultiInfoStruct:
        """ 
        编辑多资源对话框, 数据将在内部修改, 无需外部处理, 但仍返回修改的数据类, 针对 --resource 参数

        参数:
        - parent: 父窗口
        - data_struct: 数据结构

        返回:
        - data_struct: 修改后的数据结构
        """
        dialog = QDialog.__new__(DialogMultiResourcePath)
        dialog.__init__(parent, data_struct)
        dialog.exec_()
        return dialog.__data_struct

    def __new__(cls, *args, **kwargs):
        raise TypeError("Cannot instantiate directly. Use DialogMultiRelativePath.edit(...) instead.")

    def __init__(self, parent, data_struct: MultiInfoStruct) -> None:
        super().__init__(parent)
        self.__parent = parent
        self.__data_struct: MultiInfoStruct = data_struct
        self.__init_parameters()
        self.__init_ui()
        self.__init_signal_connections()
        self.__load_data_to_table()

    def __init_parameters(self):
        self.__isEditing = False
        self.__data: list | str = self.__data_struct.command_args
        self.__origin_data: list | str = copy.deepcopy(self.__data)
        self.__command_option: str = self.__data_struct.command_option if isinstance(self.__data_struct.command_option, str) else self.__data_struct.command_option[0]
        self.__command_name = self.__data_struct.name

    def __init_ui(self) -> None:
        title_editing = LM.getWord('title_editing')
        win_title = f'{title_editing}: {self.__command_option}'
        self.setModal(True)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowTitleHint | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
        self.setWindowTitle(win_title)
        self.setWindowIcon(QIcon(convert_svg_to_pixmap(ICON.APP_ICON)))
        self.resize(800, 600)
        layout_main = QVBoxLayout(self)
        layout_title = QVBoxLayout()
        layout_edit_button = QHBoxLayout()
        layout_putton = QHBoxLayout()
        self.__label_title = QLabel(self)
        self.__label_title.setText(LanguageManager.getWord('description_' + self.__command_name))  # 此处应写入说明
        self.__label_command_option = QLabel(self)
        self.__label_command_option.setText(f' {self.__command_option} =')
        self.__tableWidget = _TableWidget(self)
        self.__tableWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        widget_holder_edit_button = QWidget(self)
        widget_holder_edit_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_holder_pushbutton = QWidget(self)
        widget_holder_pushbutton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_save = QPushButton(LM.getWord('save'), self)
        self.__btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_save.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_cancel = QPushButton(LM.getWord('cancel'), self)
        self.__btn_cancel.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_cancel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_add_files = QPushButton(self)
        self.__btn_add_folders = QPushButton(self)
        self.__btn_add_folders.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_add_folders.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_delete = QPushButton(self)
        self.__btn_delete.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_delete.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_add_files.setIcon(QIcon(convert_svg_to_pixmap(ICON.ADD_FILE)))
        self.__btn_add_folders.setIcon(QIcon(convert_svg_to_pixmap(ICON.ADD_FOLDER)))
        self.__btn_delete.setIcon(QIcon(convert_svg_to_pixmap(ICON.DELETE)))
        for btn in [self.__btn_add_files, self.__btn_add_folders, self.__btn_delete]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.setFixedSize(btn.height(), btn.height())
            btn.setIconSize(QSize(btn.height()-10, btn.height()-10))

        self.__btn_save.setProperty('widgetType', 'Dialog')
        self.__btn_cancel.setProperty('widgetType', 'Dialog')

        layout_main.addLayout(layout_title)
        layout_main.addWidget(self.__tableWidget)
        layout_main.addLayout(layout_edit_button)
        layout_main.addLayout(layout_putton)
        layout_title.addWidget(self.__label_title)
        layout_title.addWidget(self.__label_command_option)
        layout_edit_button.addWidget(self.__btn_add_files)
        layout_edit_button.addWidget(self.__btn_add_folders)
        layout_edit_button.addWidget(self.__btn_delete)
        layout_edit_button.addWidget(widget_holder_edit_button)
        layout_putton.addWidget(widget_holder_pushbutton)
        layout_putton.addWidget(self.__btn_save)
        layout_putton.addWidget(self.__btn_cancel)

        layout_main.setStretch(0, 10)
        layout_main.setStretch(1, 100)
        layout_main.setStretch(2, 10)
        layout_main.setStretch(3, 10)
        layout_edit_button.setStretch(0, 10)
        layout_edit_button.setStretch(1, 10)
        layout_edit_button.setStretch(2, 0)
        layout_edit_button.setStretch(3, 100)
        layout_putton.setStretch(0, 100)
        layout_putton.setStretch(1, 10)
        layout_putton.setStretch(2, 10)

        self.__tableWidget.setColumnCount(4)
        self.__tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.__tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.__tableWidget.horizontalHeader().setStretchLastSection(True)
        self.__tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.__tableWidget.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.__tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.__tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.__tableWidget.setHorizontalHeaderLabels([LM.getWord('type'), LM.getWord('name'), LM.getWord('language'), LM.getWord('path')])
        self.__tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.__tableWidget.setColumnWidth(0, 150)
        self.__tableWidget.setColumnWidth(1, 150)
        self.__tableWidget.setColumnWidth(2, 150)
        self.__tableWidget.setColumnWidth(3, 300)
        self.setStyleSheet(STYLE.getBlock().style)
        self.__tableWidget.verticalScrollBar().setStyleSheet(STYLE.getBlock('~scrollbar').style)
        self.__tableWidget.verticalHeader().setVisible(False)
        self.show()

    def __init_signal_connections(self) -> None:
        self.__tableWidget.cellEditingFinished.connect(self.__on_cell_changed)
        self.__tableWidget.rowDragged.connect(self.__on_dragged)
        self.__tableWidget.customContextMenuRequested.connect(self.__on_context_menu)
        self.__btn_add_files.clicked.connect(self.__on_add_files)
        self.__btn_add_folders.clicked.connect(self.__on_add_folder)
        self.__btn_delete.clicked.connect(self.__on_delete)
        self.__btn_save.clicked.connect(self.__accept)
        self.__btn_cancel.clicked.connect(self.__cancel)

    def __load_data_to_table(self) -> None:
        """ 加载数据到表格 """
        self.__isEditing = True
        length: int = len(self.__data)
        self.__tableWidget.clearContents()
        self.__tableWidget.setRowCount(length)
        icon_provider = QFileIconProvider()
        for index, item in enumerate(self.__data):
            item_list = item.split(',')
            file_path = item_list[0]
            type_data = item_list[1]
            name_data = item_list[2]
            lang_data = item_list[3]
            file_path_item = QTableWidgetItem(file_path)
            type_item = QComboBox(self)
            type_item.addItem(f'({LM.getWord("empty")})', '')
            for typ in VersionEnum.ResourceType:
                type_item.addItem(typ.name, typ.value)
            try:
                type_data = int(type_data)
                type_item.setCurrentText(VersionEnum.ResourceType.getItem(int(type_data)).name)
            except:
                type_item.setCurrentText(f'({LM.getWord("empty")})')
            type_item.currentTextChanged.connect(functools.partial(self.__on_cell_changed, index, 0))
            name_item = QTableWidgetItem(name_data)
            lang_item = QComboBox(self)
            lang_item.addItem(f'({LM.getWord("empty")})', '')
            for lang in VersionEnum.LangID:
                display_text = LM.getWord('lang_'+lang.name)
                value = lang.value
                lang_item.addItem(display_text, value)
            try:
                lang_data = int(lang_data)
                lang_item.setCurrentText(LM.getWord('lang_'+VersionEnum.LangID.getItem(int(lang_data)).name))
            except:
                lang_item.setCurrentText(f'({LM.getWord("empty")})')
            lang_item.currentTextChanged.connect(functools.partial(self.__on_cell_changed, index, 2))
            file_info = QFileInfo(file_path)
            icon = icon_provider.icon(file_info)
            file_path_item.setIcon(icon)
            self.__tableWidget.setCellWidget(index, 0, type_item)
            self.__tableWidget.setItem(index, 1, name_item)
            self.__tableWidget.setCellWidget(index, 2, lang_item)
            self.__tableWidget.setItem(index, 3, file_path_item)
        self.__isEditing = False

    def __on_add_files(self) -> None:
        file_name_list, _ = QFileDialog.getOpenFileNames(self, LM.getWord('select_file'), '')
        isAdded = False
        if not file_name_list:
            return
        for file_name in file_name_list:
            file_name += ',,,'
            if file_name in self.__data:
                continue
            self.__data.append(file_name)
            isAdded = True
        if isAdded:
            self.__load_data_to_table()

    def __on_add_folder(self) -> None:
        folder_path = QFileDialog.getExistingDirectory(self, LM.getWord('select_folder'), '')
        if not folder_path:
            return
        folder_path += ',,,'
        if folder_path in self.__data:
            return
        self.__data.append(folder_path)
        self.__load_data_to_table()

    def __on_delete(self):
        selected_indexes = self.__tableWidget.selectionModel().selectedRows()
        for index in selected_indexes:
            if self.__tableWidget.item(index.row(), 0) is None:
                continue
            # self.__tableWidget.removeRow(index.row())
            del self.__data[index.row()]
            self.__load_data_to_table()

    def __on_copy(self, item: QTableWidgetItem):
        folder_path = os.path.normpath(self.__tableWidget.item(item.row(), 3).text()).replace('\\', '/')
        QApplication.clipboard().setText(folder_path)

    def __on_context_menu(self, position):
        item: QTableWidgetItem = self.__tableWidget.itemAt(position)
        if item is None:
            return
        menu = QMenu()
        action_copy = menu.addAction(LanguageManager.getWord('copy_path'))
        # action_copy.setIcon(QIcon(convert_svg_to_pixmap(ICON.COPY)))
        action_edit_file_path = menu.addAction(LanguageManager.getWord('edit_file_path'))
        action_edit_folder_path = menu.addAction(LanguageManager.getWord('edit_folder_path'))
        action_open_folder = menu.addAction(LanguageManager.getWord('open_folder'))
        action_open_folder.setIcon(QIcon(convert_svg_to_pixmap(ICON.FOLDER)))
        action_delete = menu.addAction(LanguageManager.getWord('delete'))
        action_delete.setIcon(QIcon(convert_svg_to_pixmap(ICON.DELETE)))
        action_edit_file_path.triggered.connect(lambda: self.__edit_file_path(item))
        action_edit_folder_path.triggered.connect(lambda: self.__edit_folder_path(item))
        action_copy.triggered.connect(lambda: self.__on_copy(item))
        action_open_folder.triggered.connect(lambda: self.__open_folder(item))
        action_delete.triggered.connect(self.__on_delete)
        menu.exec_(self.__tableWidget.mapToGlobal(position))

    def __edit_file_path(self, item: QTableWidgetItem):
        file_path = QFileDialog.getOpenFileName(self, LanguageManager.getWord('select_file'), '', '')[0]
        if not file_path:
            return
        self.__tableWidget.item(item.row(), 3).setText(file_path)

    def __edit_folder_path(self, item: QTableWidgetItem):
        folder_path = QFileDialog.getExistingDirectory(self, LanguageManager.getWord('select_folder'))
        if not folder_path:
            return
        self.__tableWidget.item(item.row(), 3).setText(folder_path)

    def __open_folder(self, item: QTableWidgetItem):
        folder_path = os.path.normpath(self.__tableWidget.item(item.row(), 3).text())
        subprocess.Popen(f'explorer /select,"{folder_path}"')

    def __on_cell_changed(self, row: int, column: int) -> None:
        if self.__isEditing:
            return
        path_item: QTableWidgetItem = self.__tableWidget.item(row, 3)
        type_item: QComboBox = self.__tableWidget.cellWidget(row, 0)
        name_item: QTableWidgetItem = self.__tableWidget.item(row, 1)
        lang_item: QComboBox = self.__tableWidget.cellWidget(row, 2)

        if path_item is None or type_item is None or name_item is None or lang_item is None:
            return
        path_text = path_item.text()
        type_text = type_item.currentData()
        name_text = name_item.text()
        lang_text = lang_item.currentData()
        if not re.compile(r'^[a-zA-Z0-9_]+$').fullmatch(name_text) and name_text != '':
            DialogMessageBox.warning(self, LM.getWord('error_resource_name_format'))
            # cleaned_text = re.sub(r'[^a-zA-Z0-9_]', '', name_text)
            # name_item.setText(cleaned_text)
            return
        text = f'{path_text},{type_text},{name_text},{lang_text}'
        if text in self.__data:
            del self.__data[row]
        self.__data[row] = text
        self.__load_data_to_table()

    def __on_dragged(self, startRow: int,  endRow: int) -> None:
        start_text: str = self.__data[startRow]
        end_text: str = self.__data[endRow]
        self.__data[startRow] = end_text
        self.__data[endRow] = start_text

    def __accept(self) -> None:
        if self.__data != self.__origin_data:
            self.__data_struct.set_args(self.__data)
        self.accept()

    def __cancel(self) -> None:
        self.reject()


class DialogMultiAbsolutePath(QDialog):
    """ 
        编辑多相对路径对话框, 数据将在内部修改, 无需外部处理, 但仍返回修改的数据类

        参数: 
        - parent: 父窗口
        - data_struct: 数据结构
        - data_type: 数据类型, 可选值为 'file', 'folder', 默认为 '', 同时显示文件和文件夹选择按钮, 除了两个指定的参数外, 其余都视为''

        返回:
        - data_struct: 修改后的数据结构
        """
    @staticmethod
    def edit(parent, data_struct: MultiInfoStruct, data_type: str = '') -> MultiInfoStruct:
        """ 
        编辑多相对路径对话框, 数据将在内部修改, 无需外部处理, 但仍返回修改的数据类

        参数: 
        - parent: 父窗口
        - data_struct: 数据结构
        - data_type: 数据类型, 可选值为 'file', 'folder', 默认为 '', 同时显示文件和文件夹选择按钮, 除了两个指定的参数外, 其余都视为''

        返回:
        - data_struct: 修改后的数据结构
        """
        dialog = QDialog.__new__(DialogMultiAbsolutePath)
        dialog.__init__(parent, data_struct, data_type=data_type)
        dialog.exec_()
        return dialog.__data_struct

    def __new__(cls, *args, **kwargs):
        raise TypeError("Cannot instantiate directly. Use DialogMultiAbsolutePath.edit(...) instead.")

    def __init__(self, parent, data_struct: MultiInfoStruct, data_type='') -> None:
        super().__init__(parent)
        self.__parent = parent
        self.__data_struct: MultiInfoStruct = data_struct
        self.__data_type: str = data_type
        self.__init_parameters()
        self.__init_ui()
        self.__init_signal_connections()
        self.__load_data_to_table()

    def __init_parameters(self):
        self.__isEditing = False
        self.__data: list | str = self.__data_struct.command_args
        self.__origin_data: list | str = copy.deepcopy(self.__data)
        self.__command_option: str = self.__data_struct.command_option if isinstance(self.__data_struct.command_option, str) else self.__data_struct.command_option[0]
        self.__command_name = self.__data_struct.name

    def __init_ui(self) -> None:
        title_editing = LM.getWord('title_editing')
        win_title = f'{title_editing}: {self.__command_option}'
        self.setModal(True)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowTitleHint | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
        self.setWindowTitle(win_title)
        self.setWindowIcon(QIcon(convert_svg_to_pixmap(ICON.APP_ICON)))
        self.resize(800, 600)
        layout_main = QVBoxLayout(self)
        layout_title = QVBoxLayout()
        layout_edit_button = QHBoxLayout()
        layout_putton = QHBoxLayout()
        self.__label_title = QLabel(self)
        self.__label_title.setText(LanguageManager.getWord('description_' + self.__command_name))  # 此处应写入说明
        self.__label_command_option = QLabel(self)
        self.__label_command_option.setText(f' {self.__command_option} =')
        self.__tableWidget = _TableWidget(self)
        self.__tableWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        widget_holder_edit_button = QWidget(self)
        widget_holder_edit_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        widget_holder_pushbutton = QWidget(self)
        widget_holder_pushbutton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_save = QPushButton(LM.getWord('save'), self)
        self.__btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_save.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_cancel = QPushButton(LM.getWord('cancel'), self)
        self.__btn_cancel.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_cancel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_add_files = QPushButton(self)
        self.__btn_add_folders = QPushButton(self)
        self.__btn_add_folders.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_add_folders.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_delete = QPushButton(self)
        self.__btn_delete.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__btn_delete.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.__btn_add_files.setIcon(QIcon(convert_svg_to_pixmap(ICON.ADD_FILE)))
        self.__btn_add_folders.setIcon(QIcon(convert_svg_to_pixmap(ICON.ADD_FOLDER)))
        self.__btn_delete.setIcon(QIcon(convert_svg_to_pixmap(ICON.DELETE)))
        for btn in [self.__btn_add_files, self.__btn_add_folders, self.__btn_delete]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.setFixedSize(btn.height(), btn.height())
            btn.setIconSize(QSize(btn.height()-10, btn.height()-10))

        self.__btn_save.setProperty('widgetType', 'Dialog')
        self.__btn_cancel.setProperty('widgetType', 'Dialog')
        # self.__btn_reset.setProperty('widgetType', 'Dialog')

        layout_main.addLayout(layout_title)
        layout_main.addWidget(self.__tableWidget)
        layout_main.addLayout(layout_edit_button)
        layout_main.addLayout(layout_putton)
        layout_title.addWidget(self.__label_title)
        layout_title.addWidget(self.__label_command_option)
        if self.__data_type == 'file':
            layout_edit_button.addWidget(self.__btn_add_files)
            self.__btn_add_folders.hide()
        elif self.__data_type == 'folder':
            layout_edit_button.addWidget(self.__btn_add_folders)
            self.__btn_add_files.hide()
        else:
            layout_edit_button.addWidget(self.__btn_add_files)
            layout_edit_button.addWidget(self.__btn_add_folders)
        layout_edit_button.addWidget(self.__btn_delete)
        layout_edit_button.addWidget(widget_holder_edit_button)
        layout_putton.addWidget(widget_holder_pushbutton)
        layout_putton.addWidget(self.__btn_save)
        layout_putton.addWidget(self.__btn_cancel)

        layout_main.setStretch(0, 10)
        layout_main.setStretch(1, 100)
        layout_main.setStretch(2, 10)
        layout_main.setStretch(3, 10)
        layout_edit_button.setStretch(0, 10)
        layout_edit_button.setStretch(1, 10)
        layout_edit_button.setStretch(2, 0)
        layout_edit_button.setStretch(3, 100)
        layout_putton.setStretch(0, 100)
        layout_putton.setStretch(1, 10)
        layout_putton.setStretch(2, 10)

        self.__tableWidget.setColumnCount(1)
        self.__tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.__tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.__tableWidget.horizontalHeader().setStretchLastSection(True)
        self.__tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.__tableWidget.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.__tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.__tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.__tableWidget.setHorizontalHeaderLabels([LanguageManager.getWord('argument_value')])
        self.__tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.setStyleSheet(STYLE.getBlock().style)
        self.__tableWidget.verticalScrollBar().setStyleSheet(STYLE.getBlock('~scrollbar').style)
        self.__tableWidget.verticalHeader().setVisible(False)
        self.show()

    def __init_signal_connections(self) -> None:
        self.__tableWidget.cellEditingFinished.connect(self.__on_cell_changed)
        self.__tableWidget.rowDragged.connect(self.__on_dragged)
        self.__tableWidget.customContextMenuRequested.connect(self.__on_context_menu)
        self.__btn_add_files.clicked.connect(self.__on_add_files)
        self.__btn_add_folders.clicked.connect(self.__on_add_folder)
        self.__btn_delete.clicked.connect(self.__on_delete)
        self.__btn_save.clicked.connect(self.__accept)
        self.__btn_cancel.clicked.connect(self.__cancel)

    def __load_data_to_table(self) -> None:
        self.__isEditing = True
        length = len(self.__data)
        self.__tableWidget.clearContents()
        self.__tableWidget.setRowCount(length)
        icon_provider = QFileIconProvider()
        for index, item in enumerate(self.__data):
            param_item = QTableWidgetItem(item)
            icon = icon_provider.icon(QFileInfo(item))
            param_item.setIcon(icon)
            self.__tableWidget.setItem(index, 0, param_item)
        self.__isEditing = False

    def __on_add_files(self) -> None:
        file_name_list, _ = QFileDialog.getOpenFileNames(self, LM.getWord('select_file'))
        isAdded = False
        if not file_name_list:
            return
        for file_name in file_name_list:
            if file_name in self.__data:
                continue
            self.__data.append(file_name)
            isAdded = True
        if isAdded:
            self.__load_data_to_table()

    def __on_add_folder(self) -> None:
        folder_path = QFileDialog.getExistingDirectory(self, LM.getWord('select_folder'))
        if not folder_path:
            return
        if folder_path in self.__data:
            return
        self.__data.append(folder_path)
        self.__load_data_to_table()

    def __on_delete(self):
        selected_indexes = self.__tableWidget.selectionModel().selectedRows()
        for index in selected_indexes:
            if self.__tableWidget.item(index.row(), 0) is None:
                continue
            del self.__data[index.row()]
            self.__load_data_to_table()

    def __on_copy(self, item: QTableWidgetItem):
        folder_path = os.path.normpath(self.__tableWidget.item(item.row(), 0).text()).replace('\\', '/')
        QApplication.clipboard().setText(folder_path)

    def __on_context_menu(self, position) -> None:
        item: QTableWidgetItem = self.__tableWidget.itemAt(position)
        if item is None:
            return
        menu = QMenu()
        action_copy = menu.addAction(LanguageManager.getWord('copy_path'))
        # action_copy.setIcon(QIcon(convert_svg_to_pixmap(ICON.COPY)))
        action_open_folder = menu.addAction(LanguageManager.getWord('open_folder'))
        action_open_folder.setIcon(QIcon(convert_svg_to_pixmap(ICON.FOLDER)))
        action_delete = menu.addAction(LanguageManager.getWord('delete'))
        action_delete.setIcon(QIcon(convert_svg_to_pixmap(ICON.DELETE)))
        action_copy.triggered.connect(lambda: self.__on_copy(item))
        action_open_folder.triggered.connect(lambda: self.__open_folder(item))
        action_delete.triggered.connect(self.__on_delete)
        menu.exec_(self.__tableWidget.mapToGlobal(position))

    def __open_folder(self, item: QTableWidgetItem) -> None:
        folder_path = os.path.normpath(self.__tableWidget.item(item.row(), 0).text())
        subprocess.Popen(f'explorer /select,"{folder_path}"')

    def __on_cell_changed(self, row: int, column: int) -> None:
        if self.__isEditing:
            return
        item: QTableWidgetItem = self.__tableWidget.item(row, column)
        text = item.text().strip('"').strip("'").strip()
        if not os.path.exists(text):
            self.__handle_path_error()
            return
        if text in self.__data:
            del self.__data[row]
        self.__data[row] = text
        self.__load_data_to_table()

    def __handle_path_error(self) -> None:
        DialogMessageBox.warning(self, LM.getWord('error_invalid_path'))
        self.__load_data_to_table()

    def __on_dragged(self, startRow: int,  endRow: int) -> None:
        start_text: str = self.__data[startRow]
        end_text: str = self.__data[endRow]
        self.__data[startRow] = end_text
        self.__data[endRow] = start_text

    def __accept(self) -> None:
        if self.__data != self.__origin_data:
            self.__data_struct.set_args(self.__data)
        self.accept()

    def __cancel(self) -> None:
        self.reject()
