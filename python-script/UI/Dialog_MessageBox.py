
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget,  QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QByteArray, QSize, Qt
from const.Const_Parameter import *
from system.Manager_Language import LanguageManager


class DialogMessageBox(QDialog):

    @staticmethod
    def question(parent, title: str = 'Qestion', content: str = '', buttons: list = [], default_button: int = -1, isResetVisible=False):
        icon = """<svg width="800.00012" height="800.00006" viewBox="0 0 211.66669 211.66669" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer1"><circle style="fill:#00a9ff;fill-opacity:1;stroke-width:5.72023;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="path1" cx="105.83334" cy="105.83334" r="105.83334" /><path d="m -251.13591,100.87967 c -1.05227,4.06808 -1.79303,9.15199 -5.32715,11.42499 -5.78404,3.72006 -14.85706,3.91424 -20.6304,0.1776 -3.03131,-1.96194 -3.26858,-6.47546 -4.35115,-9.92018 -0.97814,-3.112401 -1.56868,-6.355381 -1.90271,-9.600716 -0.5168,-5.021076 -0.68731,-10.123896 -0.14357,-15.142127 0.31689,-2.924664 0.96377,-5.838586 1.97196,-8.602215 1.01395,-2.779426 2.40049,-5.44237 4.0534,-7.896179 4.72295,-7.011387 10.81553,-13.005918 16.55685,-19.211002 5.72561,-6.188111 13.47509,-10.283399 17.82074,-17.947122 3.74144,-6.598175 7.03648,-14.7612426 6.26417,-22.6532226 -0.65096,-6.6519173 -4.47574,-12.8794774 -8.82794,-17.1624644 -5.0876,-5.00668 -11.93818,-8.429043 -18.55627,-8.354217 -7.79094,0.08808 -15.54844,4.644115 -21.68185,10.326866 -4.04331,3.7462326 -7.22075,9.0896478 -9.01045,14.7837461 -2.04335,6.5010744 -0.71406,13.8602989 -1.5328,20.7281129 -0.98565,8.267949 1.19169,19.00499 -4.06039,24.584533 -5.10486,5.42314 -14.69667,6.397879 -20.50969,2.085697 -6.23587,-4.625853 -6.66948,-15.812251 -7.87547,-24.400623 -1.03814,-7.39311 -0.76625,-15.1709656 0.6748,-22.4689629 1.64965,-8.3543843 4.58313,-16.6060491 8.93989,-23.4653671 4.9812,-7.842444 11.67404,-14.35261 18.93955,-19.082353 10.64638,-6.93064 22.67459,-12.328473 34.82127,-12.772811 12.50046,-0.457279 25.76502,2.820715 36.45378,10.500408 10.21127,7.336625 19.58565,18.611261 23.57762,31.930173 3.06936,10.240714 1.88083,22.259331 -1.00711,32.573596 -2.71863,9.709549 -8.81382,17.794138 -14.71376,25.272165 -4.31184,5.465151 -9.8955,9.301842 -14.83579,13.963838 -3.09027,2.916194 -6.81717,5.285776 -9.26147,8.762423 -1.9975,2.841145 -3.33163,6.176677 -4.17682,9.545321 -1.11014,4.424609 -0.74263,9.093301 -1.08241,13.64238 -0.20851,2.791637 0.11421,5.667502 -0.58683,8.377713 z m -14.44913,28.76315 c 5.18954,-0.04 10.82318,2.06261 14.662,6.19302 3.97208,4.27379 6.80364,10.9077 6.82497,17.2587 0.0217,6.46094 -2.79876,13.25542 -6.82497,17.62215 -3.82492,4.14842 -9.47238,6.21293 -14.662,6.19303 -5.0972,-0.0195 -10.6428,-2.07715 -14.36726,-6.19303 -4.02516,-4.4482 -6.75741,-11.3536 -6.69858,-17.86865 0.0561,-6.217 2.83109,-12.67487 6.69858,-16.88581 3.75918,-4.09301 9.25783,-6.28003 14.36726,-6.31941 z" id="text8" style="font-weight:900;font-size:258.843px;line-height:1152.23px;font-family:Arial;-inkscape-font-specification:'Arial Heavy';text-align:center;letter-spacing:0px;text-orientation:upright;text-anchor:middle;fill:#ffffff;stroke-width:35.9505;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" aria-label="?" transform="matrix(0.9917986,0,0,0.83856406,369.19287,54.324831)" /></g></svg>"""
        dialog = DialogMessageBox(parent, title, content, buttons, icon, default_button, isResetVisible)
        dialog.exec_()
        if not hasattr(dialog, 'selected_btn'):
            return None
        return dialog.selected_btn

    @staticmethod
    def info(parent, content: str):
        icon = """<svg width="800.00012" height="800.00006" viewBox="0 0 211.66669 211.66669" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer1"><circle style="fill:#00a9ff;fill-opacity:1;stroke-width:5.72023;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="path1" cx="105.83334" cy="105.83334" r="105.83334" /><circle style="fill:#ffffff;stroke-width:26.4853;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="path2" cx="104.47603" cy="38.10218" r="24.873014" /><rect style="fill:#ffffff;stroke-width:27.8501;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect2" width="80.081444" height="33.651722" x="52.916668" y="73.310226" /><rect style="fill:#ffffff;stroke-width:22.9252;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect3" width="40.040722" height="125.12727" x="92.957466" y="73.310226" /></g></svg>"""
        dialog = DialogMessageBox(parent, LanguageManager.get('info'), content, buttons=[LanguageManager.get('certain')], icon=icon, default_button=-1, isResetVisible=False)
        dialog.exec_()
        if not hasattr(dialog, 'selected_btn'):
            return None
        return dialog.selected_btn

    @staticmethod
    def warning(parent, content: str):
        icon = """<svg width="800.00012" height="800.00006" viewBox="0 0 211.66669 211.66669" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer1"><circle style="fill:#00a9ff;fill-opacity:1;stroke-width:5.72023;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="path1" cx="105.83334" cy="105.83334" r="105.83334" /><circle style="fill:#feff86;fill-opacity:1;stroke-width:22.6114;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="path2" cx="105.68243" cy="177.20258" r="21.234932" /><path id="rect3" style="fill:#feff86;fill-opacity:1;stroke-width:22.9019;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" d="m -89.125,76.204109 h 18.25 a 14.655719,14.655719 47.28696 0 1 14.609045,15.824443 l -7.46809,93.351138 A 17.195719,17.195719 137.28696 0 1 -80.875,201.20413 16.271467,16.271467 45.795614 0 1 -96.265955,185.37969 L -103.73404,92.028552 A 14.655719,14.655719 132.71304 0 1 -89.125,76.204109 Z" transform="matrix(1.0617466,0,0,1.0617466,190.62216,-67.680287)" /></g></svg>"""
        dialog = DialogMessageBox(parent, LanguageManager.get('warning'), content, buttons=[LanguageManager.get('certain')], icon=icon, default_button=-1, isResetVisible=False)
        dialog.exec_()
        if not hasattr(dialog, 'selected_btn'):
            return None
        return dialog.selected_btn

    @staticmethod
    def error(parent, content: str):
        icon = """<svg width="786.01715" height="753.34412" viewBox="0 0 207.96703 199.3223" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer1" transform="translate(-1.5563794,-2.8005225)"><path style="fill:#e43c00;fill-opacity:1;stroke:#ffdf46;stroke-width:4.99999;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-opacity:1;paint-order:fill markers stroke" id="path4" d="m 159.97814,98.071064 c -18.27503,31.653286 -184.780878,31.653286 -203.05591,0 C -61.352801,66.41778 21.900121,-77.78051 58.450184,-77.78051 c 36.550064,0 119.802986,144.198291 101.527956,175.851574 z" transform="matrix(0.97424516,0,0,0.97424516,48.595088,81.013416)" /><circle style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:4.99999;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-opacity:1;paint-order:fill markers stroke" id="path3-1" cx="105.11908" cy="164.84239" r="11.50738" /><path id="path10" style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:3.81042;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-opacity:1;paint-order:fill markers stroke" d="m 105.57488,38.542215 a 14.42989,14.42989 0 0 0 -11.131619,5.282882 6.0841031,11.05144 0 0 0 -3.391524,11.51971 l 6.074048,75.097753 a 8.1546576,14.81249 0 0 0 8.042405,12.65916 l 0.34726,0.002 a 8.1611488,14.82428 0 0 0 8.0915,-12.56512 l 6.39961,-75.380415 a 6.003071,10.90425 0 0 0 -3.58428,-11.696443 14.42989,14.42989 0 0 0 -10.8474,-4.919597 z" /></g></svg>"""
        dialog = DialogMessageBox(parent, LanguageManager.get('certain'), content, buttons=[LanguageManager.get('certain')], icon=icon, default_button=-1, isResetVisible=False)
        dialog.exec_()
        if not hasattr(dialog, 'selected_btn'):
            return None
        return dialog.selected_btn

    @staticmethod
    def critical(parent, content: str):
        icon = """<svg width="800.00012" height="800.00006" viewBox="0 0 211.66669 211.66669" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer1"><circle style="fill:#f92727;fill-opacity:1;stroke-width:5.72023;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="path1" cx="105.83334" cy="105.83334" r="105.83334" /><rect style="fill:#faf885;fill-opacity:1;stroke-width:4.61409;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect1" width="38.29879" height="192.05716" x="130.52156" y="-96.028603" ry="19.149395" transform="rotate(45)" /><rect style="fill:#faf885;fill-opacity:1;stroke-width:4.61409;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect2" width="38.29879" height="192.05716" x="-19.149397" y="-245.69949" ry="23.373528" transform="rotate(135)" /></g></svg>"""
        dialog = DialogMessageBox(parent, LanguageManager.get('critical'), content, buttons=[LanguageManager.get('certain')], icon=icon, default_button=-1, isResetVisible=False)
        dialog.exec_()
        if not hasattr(dialog, 'selected_btn'):
            return None
        return dialog.selected_btn

    @staticmethod
    def show(parent, title: str, content: str, buttons: list, icon: str = None, default_button: int = -1, isResetVisible=False):
        dialog = DialogMessageBox(parent, title, content, buttons, icon, default_button, isResetVisible)
        dialog.exec_()
        if not hasattr(dialog, 'selected_btn'):
            return None
        return dialog.selected_btn

    def __init__(self, parent, title: str, content: str, buttons: list, icon: str = None, default_button: int = -1, isResetVisible: bool = False):
        super().__init__(parent)
        self.__language = LanguageManager()
        self.setWindowTitle(title)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.__svg_blank = """<svg width="800" height="800" viewBox="0 0 211.66666 211.66667" xmlns="http://www.w3.org/2000/svg"> </svg>"""
        pixmap_icon = self.__pixmap_from_svg(icon)
        self.setStyleSheet("""\
            QLabel, QPushButton {
            font: 16px 'Arial';
            } 
            QPushButton {
                border: 1px solid #D6E5FA;
                border-radius: 13px;
                background-color:#fefefe;
                min-height: 25px;
                max-width: 200px;
            }
            QPushButton:hover {
                background-color: #CEECF0;
            }
            """)
        main_widget = QWidget()
        pb_widget = QWidget()
        wdgt_reset = QWidget()
        main_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        pb_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        pb_reset = QPushButton(self.__language.get('reset'))
        # pb_reset = QPushButton('reset')
        pb_reset.setCursor(Qt.PointingHandCursor)
        pb_reset.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        pb_reset.clicked.connect(lambda: self.__on_button_clicked('reset'))
        pb_cancel = QPushButton(self.__language.get('cancel'))
        pb_cancel.setDefault(True)
        pb_cancel.setStyleSheet(""" border: 1px solid #1E2A78;""")
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
        layout.setStretch(1, 100)
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
            if index == default_button:
                pb_cancel.setDefault(False)
                pb_cancel.setStyleSheet("""""")
                button.setDefault(True)
                button.setStyleSheet(""" border: 1px solid #1E2A78;""")
        pb_layout.addWidget(pb_cancel)
        self.adjustSize()
        self.setFixedSize(self.size())
        if not isResetVisible:
            wdgt_reset.hide()

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
            logging.warning('fehler svg')
            pixmap.loadFromData(QByteArray(self.__svg_blank.encode()))
        return pixmap


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    main = QMainWindow()
    m = DialogMessageBox.question(None)
    # m = DialogMessageBox.question(
    #     main,
    #     'This is a title',
    #     'This is a test\na short period\nIt is a very very very very long sentence! We will try it in the __main__ function!',
    #     ['ddd'],
    #     default_button=1,
    #     isResetVisible=False
    # )
