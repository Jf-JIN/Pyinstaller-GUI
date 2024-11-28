
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget,  QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QByteArray, QSize, Qt


class DialogMessageBox(QDialog):

    @staticmethod
    def show(parent, title: str, content: str, buttons: list, icon: str = None, default_button: int = -1, isResetVisible=True):
        dialog = DialogMessageBox(parent, title, content, buttons, icon, default_button, isResetVisible)
        dialog.exec_()
        if not hasattr(dialog, 'selected_btn'):
            return None
        return dialog.selected_btn

    def __init__(self, parent, title: str, content: str, buttons: list, icon: str = None, default_button: int = -1, isResetVisible: bool = True):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.__svg_blank = """<svg width="800" height="800" viewBox="0 0 211.66666 211.66667" xmlns="http://www.w3.org/2000/svg"> </svg>"""
        pixmap_icon = self.__pixmap_from_svg(icon)
        main_widget = QWidget()
        pb_widget = QWidget()
        wdgt_reset = QWidget()
        pb_reset = QPushButton(self.parent().languange.reset)
        # pb_reset = QPushButton('reset')
        pb_reset.setCursor(Qt.PointingHandCursor)
        pb_reset.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        pb_reset.clicked.connect(lambda: self.__on_button_clicked('reset'))
        pb_cancel = QPushButton(self.parent().languange.cancel)
        # pb_cancel = QPushButton('cancel')
        pb_cancel.setDefault(True)
        pb_cancel.setCursor(Qt.PointingHandCursor)
        pb_cancel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        pb_cancel.clicked.connect(lambda: self.__on_button_clicked('cancel'))
        content_label = QLabel(content)
        icon_label = QLabel(self)
        icon_label.setPixmap(pixmap_icon)
        icon_label.setScaledContents(True)
        icon_label.setFixedSize(QSize(50, 50))
        layout = QVBoxLayout(self)
        layout.addWidget(main_widget)
        layout.addWidget(pb_widget)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(20)
        layout.setStretch(0, 100)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(20)
        main_layout.setStretch(0, 100)
        pb_layout = QHBoxLayout(pb_widget)
        pb_layout.setContentsMargins(0, 0, 0, 0)
        pb_layout.setSpacing(10)
        reset_layout = QHBoxLayout(wdgt_reset)
        reset_layout.setContentsMargins(0, 0, 0, 0)
        reset_layout.setSpacing(10)
        main_layout.addWidget(icon_label)
        main_layout.addWidget(content_label)
        reset_layout.addWidget(pb_reset)
        pb_layout.addWidget(wdgt_reset)
        for index, label in enumerate(buttons):
            button = QPushButton(label)
            button.setCursor(Qt.PointingHandCursor)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.clicked.connect(lambda _, btn_index=index: self.__on_button_clicked(btn_index))
            pb_layout.addWidget(button)
            if index+1 == default_button:
                pb_cancel.setDefault(False)
                button.setDefault(True)
        pb_layout.addWidget(pb_cancel)
        self.adjustSize()
        self.setFixedSize(self.size())
        if not isResetVisible:
            pb_reset.hide()

    def __on_button_clicked(self, button_index: int | str):
        self.selected_btn = button_index
        self.accept()

    def __pixmap_from_svg(self, icon_code: str) -> QIcon:
        '''
        设置图标

        参数:
            Icon_code: SVG 的源码(str)
        '''
        if icon_code == "" or icon_code == None:
            icon_code = self.__svg_blank
        pixmap = QPixmap()
        try:
            pixmap.loadFromData(QByteArray(icon_code.encode()))
        except:
            print('fehler svg')
            pixmap.loadFromData(QByteArray(self.__svg_blank.encode()))
        return pixmap


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    main = QMainWindow()
    m = DialogMessageBox.show(main, 'This is a title', 'This is a test\na short period\nIt is a very very very very long sentence! We will try it in the __main__ function!',
                              ['ddd'], default_button=0, isResetVisible=True)
