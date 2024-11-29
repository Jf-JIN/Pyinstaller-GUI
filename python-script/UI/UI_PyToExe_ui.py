# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_PyToExe.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QStackedWidget,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(841, 776)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_menu = QWidget(self.centralwidget)
        self.widget_menu.setObjectName(u"widget_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_menu.sizePolicy().hasHeightForWidth())
        self.widget_menu.setSizePolicy(sizePolicy)
        self.widget_menu.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.verticalLayout_2 = QVBoxLayout(self.widget_menu)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 15, 10, 15)
        self.widget_exe_info = QWidget(self.widget_menu)
        self.widget_exe_info.setObjectName(u"widget_exe_info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_exe_info.sizePolicy().hasHeightForWidth())
        self.widget_exe_info.setSizePolicy(sizePolicy1)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_exe_info)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lb_exe_icon = QLabel(self.widget_exe_info)
        self.lb_exe_icon.setObjectName(u"lb_exe_icon")
        sizePolicy1.setHeightForWidth(self.lb_exe_icon.sizePolicy().hasHeightForWidth())
        self.lb_exe_icon.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.lb_exe_icon)


        self.verticalLayout_2.addWidget(self.widget_exe_info)

        self.widget_page_basic = QWidget(self.widget_menu)
        self.widget_page_basic.setObjectName(u"widget_page_basic")
        sizePolicy1.setHeightForWidth(self.widget_page_basic.sizePolicy().hasHeightForWidth())
        self.widget_page_basic.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_page_basic)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_page_basic = QPushButton(self.widget_page_basic)
        self.pb_page_basic.setObjectName(u"pb_page_basic")
        sizePolicy1.setHeightForWidth(self.pb_page_basic.sizePolicy().hasHeightForWidth())
        self.pb_page_basic.setSizePolicy(sizePolicy1)
        self.pb_page_basic.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_page_basic.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.pb_page_basic)


        self.verticalLayout_2.addWidget(self.widget_page_basic)

        self.widget_page_advance = QWidget(self.widget_menu)
        self.widget_page_advance.setObjectName(u"widget_page_advance")
        sizePolicy1.setHeightForWidth(self.widget_page_advance.sizePolicy().hasHeightForWidth())
        self.widget_page_advance.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_page_advance)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pb_page_advance = QPushButton(self.widget_page_advance)
        self.pb_page_advance.setObjectName(u"pb_page_advance")
        sizePolicy1.setHeightForWidth(self.pb_page_advance.sizePolicy().hasHeightForWidth())
        self.pb_page_advance.setSizePolicy(sizePolicy1)
        self.pb_page_advance.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.pb_page_advance)


        self.verticalLayout_2.addWidget(self.widget_page_advance)

        self.widget_3 = QWidget(self.widget_menu)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pb_page_ios_win = QPushButton(self.widget_3)
        self.pb_page_ios_win.setObjectName(u"pb_page_ios_win")
        sizePolicy1.setHeightForWidth(self.pb_page_ios_win.sizePolicy().hasHeightForWidth())
        self.pb_page_ios_win.setSizePolicy(sizePolicy1)
        self.pb_page_ios_win.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.pb_page_ios_win)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_menu)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pb_page_info = QPushButton(self.widget_4)
        self.pb_page_info.setObjectName(u"pb_page_info")
        sizePolicy1.setHeightForWidth(self.pb_page_info.sizePolicy().hasHeightForWidth())
        self.pb_page_info.setSizePolicy(sizePolicy1)
        self.pb_page_info.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.pb_page_info)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_6 = QWidget(self.widget_menu)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pb_page_command = QPushButton(self.widget_6)
        self.pb_page_command.setObjectName(u"pb_page_command")
        sizePolicy1.setHeightForWidth(self.pb_page_command.sizePolicy().hasHeightForWidth())
        self.pb_page_command.setSizePolicy(sizePolicy1)
        self.pb_page_command.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.pb_page_command)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.widget_menu)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pb_page_console = QPushButton(self.widget_5)
        self.pb_page_console.setObjectName(u"pb_page_console")
        sizePolicy1.setHeightForWidth(self.pb_page_console.sizePolicy().hasHeightForWidth())
        self.pb_page_console.setSizePolicy(sizePolicy1)
        self.pb_page_console.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.pb_page_console)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_11 = QWidget(self.widget_menu)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy1.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy1)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pb_show_tutorial = QPushButton(self.widget_11)
        self.pb_show_tutorial.setObjectName(u"pb_show_tutorial")
        sizePolicy1.setHeightForWidth(self.pb_show_tutorial.sizePolicy().hasHeightForWidth())
        self.pb_show_tutorial.setSizePolicy(sizePolicy1)
        self.pb_show_tutorial.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.pb_show_tutorial)


        self.verticalLayout_2.addWidget(self.widget_11)

        self.widget_7 = QWidget(self.widget_menu)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(100)
        sizePolicy2.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy2)
        self.widget_7.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_page_setting = QWidget(self.widget_menu)
        self.widget_page_setting.setObjectName(u"widget_page_setting")
        sizePolicy1.setHeightForWidth(self.widget_page_setting.sizePolicy().hasHeightForWidth())
        self.widget_page_setting.setSizePolicy(sizePolicy1)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_page_setting)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pb_page_setting = QPushButton(self.widget_page_setting)
        self.pb_page_setting.setObjectName(u"pb_page_setting")
        sizePolicy1.setHeightForWidth(self.pb_page_setting.sizePolicy().hasHeightForWidth())
        self.pb_page_setting.setSizePolicy(sizePolicy1)
        self.pb_page_setting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.pb_page_setting)


        self.verticalLayout_2.addWidget(self.widget_page_setting)


        self.horizontalLayout.addWidget(self.widget_menu)

        self.widget_main = QWidget(self.centralwidget)
        self.widget_main.setObjectName(u"widget_main")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(100)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_main.sizePolicy().hasHeightForWidth())
        self.widget_main.setSizePolicy(sizePolicy3)
        self.verticalLayout = QVBoxLayout(self.widget_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.page_base = QWidget()
        self.page_base.setObjectName(u"page_base")
        sizePolicy1.setHeightForWidth(self.page_base.sizePolicy().hasHeightForWidth())
        self.page_base.setSizePolicy(sizePolicy1)
        self.verticalLayout_17 = QVBoxLayout(self.page_base)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(20, 20, 20, 20)
        self.wdg_current_env_page_base = QWidget(self.page_base)
        self.wdg_current_env_page_base.setObjectName(u"wdg_current_env_page_base")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(15)
        sizePolicy4.setHeightForWidth(self.wdg_current_env_page_base.sizePolicy().hasHeightForWidth())
        self.wdg_current_env_page_base.setSizePolicy(sizePolicy4)
        self.horizontalLayout_34 = QHBoxLayout(self.wdg_current_env_page_base)
        self.horizontalLayout_34.setSpacing(20)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(10, 10, 10, 10)
        self.lb_env_current_title_page_base = QLabel(self.wdg_current_env_page_base)
        self.lb_env_current_title_page_base.setObjectName(u"lb_env_current_title_page_base")
        sizePolicy1.setHeightForWidth(self.lb_env_current_title_page_base.sizePolicy().hasHeightForWidth())
        self.lb_env_current_title_page_base.setSizePolicy(sizePolicy1)

        self.horizontalLayout_34.addWidget(self.lb_env_current_title_page_base)

        self.lb_env_current_name_page_base = QLabel(self.wdg_current_env_page_base)
        self.lb_env_current_name_page_base.setObjectName(u"lb_env_current_name_page_base")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(10)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lb_env_current_name_page_base.sizePolicy().hasHeightForWidth())
        self.lb_env_current_name_page_base.setSizePolicy(sizePolicy5)

        self.horizontalLayout_34.addWidget(self.lb_env_current_name_page_base)

        self.lb_env_current_path_page_base = QLabel(self.wdg_current_env_page_base)
        self.lb_env_current_path_page_base.setObjectName(u"lb_env_current_path_page_base")
        sizePolicy3.setHeightForWidth(self.lb_env_current_path_page_base.sizePolicy().hasHeightForWidth())
        self.lb_env_current_path_page_base.setSizePolicy(sizePolicy3)

        self.horizontalLayout_34.addWidget(self.lb_env_current_path_page_base)

        self.lb_env_current_check_install_page_base = QLabel(self.wdg_current_env_page_base)
        self.lb_env_current_check_install_page_base.setObjectName(u"lb_env_current_check_install_page_base")
        sizePolicy1.setHeightForWidth(self.lb_env_current_check_install_page_base.sizePolicy().hasHeightForWidth())
        self.lb_env_current_check_install_page_base.setSizePolicy(sizePolicy1)

        self.horizontalLayout_34.addWidget(self.lb_env_current_check_install_page_base)


        self.verticalLayout_17.addWidget(self.wdg_current_env_page_base)

        self.wdg_input_py_file_path = QWidget(self.page_base)
        self.wdg_input_py_file_path.setObjectName(u"wdg_input_py_file_path")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(20)
        sizePolicy6.setHeightForWidth(self.wdg_input_py_file_path.sizePolicy().hasHeightForWidth())
        self.wdg_input_py_file_path.setSizePolicy(sizePolicy6)
        self.horizontalLayout_11 = QHBoxLayout(self.wdg_input_py_file_path)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.lb_input_py_file_icon = QLabel(self.wdg_input_py_file_path)
        self.lb_input_py_file_icon.setObjectName(u"lb_input_py_file_icon")
        sizePolicy5.setHeightForWidth(self.lb_input_py_file_icon.sizePolicy().hasHeightForWidth())
        self.lb_input_py_file_icon.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.lb_input_py_file_icon)

        self.widget_9 = QWidget(self.wdg_input_py_file_path)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy3.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy3)
        self.verticalLayout_4 = QVBoxLayout(self.widget_9)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_input_py_file_path = QLabel(self.widget_9)
        self.lb_input_py_file_path.setObjectName(u"lb_input_py_file_path")
        sizePolicy1.setHeightForWidth(self.lb_input_py_file_path.sizePolicy().hasHeightForWidth())
        self.lb_input_py_file_path.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.lb_input_py_file_path)

        self.le_input_py_file_path = QLineEdit(self.widget_9)
        self.le_input_py_file_path.setObjectName(u"le_input_py_file_path")
        sizePolicy1.setHeightForWidth(self.le_input_py_file_path.sizePolicy().hasHeightForWidth())
        self.le_input_py_file_path.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.le_input_py_file_path)


        self.horizontalLayout_11.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.wdg_input_py_file_path)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(4)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy7)

        self.horizontalLayout_11.addWidget(self.widget_8)

        self.pb_input_py_file_browser = QPushButton(self.wdg_input_py_file_path)
        self.pb_input_py_file_browser.setObjectName(u"pb_input_py_file_browser")
        sizePolicy5.setHeightForWidth(self.pb_input_py_file_browser.sizePolicy().hasHeightForWidth())
        self.pb_input_py_file_browser.setSizePolicy(sizePolicy5)
        self.pb_input_py_file_browser.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.pb_input_py_file_browser)


        self.verticalLayout_17.addWidget(self.wdg_input_py_file_path)

        self.wdg_output_info = QWidget(self.page_base)
        self.wdg_output_info.setObjectName(u"wdg_output_info")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(40)
        sizePolicy8.setHeightForWidth(self.wdg_output_info.sizePolicy().hasHeightForWidth())
        self.wdg_output_info.setSizePolicy(sizePolicy8)
        self.verticalLayout_16 = QVBoxLayout(self.wdg_output_info)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.wdg_output_folder_path = QWidget(self.wdg_output_info)
        self.wdg_output_folder_path.setObjectName(u"wdg_output_folder_path")
        sizePolicy1.setHeightForWidth(self.wdg_output_folder_path.sizePolicy().hasHeightForWidth())
        self.wdg_output_folder_path.setSizePolicy(sizePolicy1)
        self.horizontalLayout_13 = QHBoxLayout(self.wdg_output_folder_path)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lb_output_folder_path_icon = QLabel(self.wdg_output_folder_path)
        self.lb_output_folder_path_icon.setObjectName(u"lb_output_folder_path_icon")
        sizePolicy5.setHeightForWidth(self.lb_output_folder_path_icon.sizePolicy().hasHeightForWidth())
        self.lb_output_folder_path_icon.setSizePolicy(sizePolicy5)

        self.horizontalLayout_13.addWidget(self.lb_output_folder_path_icon)

        self.widget_12 = QWidget(self.wdg_output_folder_path)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy3.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy3)
        self.verticalLayout_6 = QVBoxLayout(self.widget_12)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_12)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy1.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy1)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.lb_output_folder_path = QLabel(self.widget_16)
        self.lb_output_folder_path.setObjectName(u"lb_output_folder_path")
        sizePolicy3.setHeightForWidth(self.lb_output_folder_path.sizePolicy().hasHeightForWidth())
        self.lb_output_folder_path.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.lb_output_folder_path)

        self.cb_lock_output_folder = QCheckBox(self.widget_16)
        self.cb_lock_output_folder.setObjectName(u"cb_lock_output_folder")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(80)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.cb_lock_output_folder.sizePolicy().hasHeightForWidth())
        self.cb_lock_output_folder.setSizePolicy(sizePolicy9)

        self.horizontalLayout_15.addWidget(self.cb_lock_output_folder)


        self.verticalLayout_6.addWidget(self.widget_16)

        self.le_output_folder_path = QLineEdit(self.widget_12)
        self.le_output_folder_path.setObjectName(u"le_output_folder_path")
        sizePolicy1.setHeightForWidth(self.le_output_folder_path.sizePolicy().hasHeightForWidth())
        self.le_output_folder_path.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.le_output_folder_path)


        self.horizontalLayout_13.addWidget(self.widget_12)

        self.widget_10 = QWidget(self.wdg_output_folder_path)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy7.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy7)

        self.horizontalLayout_13.addWidget(self.widget_10)

        self.pb_output_folder_browser = QPushButton(self.wdg_output_folder_path)
        self.pb_output_folder_browser.setObjectName(u"pb_output_folder_browser")
        sizePolicy5.setHeightForWidth(self.pb_output_folder_browser.sizePolicy().hasHeightForWidth())
        self.pb_output_folder_browser.setSizePolicy(sizePolicy5)
        self.pb_output_folder_browser.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.pb_output_folder_browser)


        self.verticalLayout_16.addWidget(self.wdg_output_folder_path)

        self.wdg_output_file_name = QWidget(self.wdg_output_info)
        self.wdg_output_file_name.setObjectName(u"wdg_output_file_name")
        sizePolicy1.setHeightForWidth(self.wdg_output_file_name.sizePolicy().hasHeightForWidth())
        self.wdg_output_file_name.setSizePolicy(sizePolicy1)
        self.horizontalLayout_14 = QHBoxLayout(self.wdg_output_file_name)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lb_output_file_name_icon = QLabel(self.wdg_output_file_name)
        self.lb_output_file_name_icon.setObjectName(u"lb_output_file_name_icon")
        sizePolicy5.setHeightForWidth(self.lb_output_file_name_icon.sizePolicy().hasHeightForWidth())
        self.lb_output_file_name_icon.setSizePolicy(sizePolicy5)

        self.horizontalLayout_14.addWidget(self.lb_output_file_name_icon)

        self.widget_14 = QWidget(self.wdg_output_file_name)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy3.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy3)
        self.verticalLayout_7 = QVBoxLayout(self.widget_14)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_14)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy1.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy1)
        self.horizontalLayout_18 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lb_output_file_name = QLabel(self.widget_20)
        self.lb_output_file_name.setObjectName(u"lb_output_file_name")
        sizePolicy3.setHeightForWidth(self.lb_output_file_name.sizePolicy().hasHeightForWidth())
        self.lb_output_file_name.setSizePolicy(sizePolicy3)

        self.horizontalLayout_18.addWidget(self.lb_output_file_name)

        self.cb_lock_output_file_name = QCheckBox(self.widget_20)
        self.cb_lock_output_file_name.setObjectName(u"cb_lock_output_file_name")
        sizePolicy9.setHeightForWidth(self.cb_lock_output_file_name.sizePolicy().hasHeightForWidth())
        self.cb_lock_output_file_name.setSizePolicy(sizePolicy9)

        self.horizontalLayout_18.addWidget(self.cb_lock_output_file_name)


        self.verticalLayout_7.addWidget(self.widget_20)

        self.le_output_file_name = QLineEdit(self.widget_14)
        self.le_output_file_name.setObjectName(u"le_output_file_name")
        sizePolicy1.setHeightForWidth(self.le_output_file_name.sizePolicy().hasHeightForWidth())
        self.le_output_file_name.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.le_output_file_name)


        self.horizontalLayout_14.addWidget(self.widget_14)

        self.widget_22 = QWidget(self.wdg_output_file_name)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy7.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy7)

        self.horizontalLayout_14.addWidget(self.widget_22)

        self.widget_21 = QWidget(self.wdg_output_file_name)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(11)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy10)

        self.horizontalLayout_14.addWidget(self.widget_21)


        self.verticalLayout_16.addWidget(self.wdg_output_file_name)


        self.verticalLayout_17.addWidget(self.wdg_output_info)

        self.wdg_option = QWidget(self.page_base)
        self.wdg_option.setObjectName(u"wdg_option")
        sizePolicy8.setHeightForWidth(self.wdg_option.sizePolicy().hasHeightForWidth())
        self.wdg_option.setSizePolicy(sizePolicy8)
        self.verticalLayout_18 = QVBoxLayout(self.wdg_option)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 10, 10, 10)
        self.wdg_output_exe_icon = QWidget(self.wdg_option)
        self.wdg_output_exe_icon.setObjectName(u"wdg_output_exe_icon")
        sizePolicy1.setHeightForWidth(self.wdg_output_exe_icon.sizePolicy().hasHeightForWidth())
        self.wdg_output_exe_icon.setSizePolicy(sizePolicy1)
        self.horizontalLayout_16 = QHBoxLayout(self.wdg_output_exe_icon)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lb_output_exe_icon_icon = QLabel(self.wdg_output_exe_icon)
        self.lb_output_exe_icon_icon.setObjectName(u"lb_output_exe_icon_icon")
        sizePolicy5.setHeightForWidth(self.lb_output_exe_icon_icon.sizePolicy().hasHeightForWidth())
        self.lb_output_exe_icon_icon.setSizePolicy(sizePolicy5)

        self.horizontalLayout_16.addWidget(self.lb_output_exe_icon_icon)

        self.widget_17 = QWidget(self.wdg_output_exe_icon)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy3.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy3)
        self.verticalLayout_9 = QVBoxLayout(self.widget_17)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lb_output_exe_icon = QLabel(self.widget_17)
        self.lb_output_exe_icon.setObjectName(u"lb_output_exe_icon")
        sizePolicy1.setHeightForWidth(self.lb_output_exe_icon.sizePolicy().hasHeightForWidth())
        self.lb_output_exe_icon.setSizePolicy(sizePolicy1)

        self.verticalLayout_9.addWidget(self.lb_output_exe_icon)

        self.le_output_exe_icon = QLineEdit(self.widget_17)
        self.le_output_exe_icon.setObjectName(u"le_output_exe_icon")
        sizePolicy1.setHeightForWidth(self.le_output_exe_icon.sizePolicy().hasHeightForWidth())
        self.le_output_exe_icon.setSizePolicy(sizePolicy1)

        self.verticalLayout_9.addWidget(self.le_output_exe_icon)


        self.horizontalLayout_16.addWidget(self.widget_17)

        self.widget_13 = QWidget(self.wdg_output_exe_icon)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy7.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy7)

        self.horizontalLayout_16.addWidget(self.widget_13)

        self.pb_output_exe_icon_browser = QPushButton(self.wdg_output_exe_icon)
        self.pb_output_exe_icon_browser.setObjectName(u"pb_output_exe_icon_browser")
        sizePolicy5.setHeightForWidth(self.pb_output_exe_icon_browser.sizePolicy().hasHeightForWidth())
        self.pb_output_exe_icon_browser.setSizePolicy(sizePolicy5)
        self.pb_output_exe_icon_browser.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.pb_output_exe_icon_browser)


        self.verticalLayout_18.addWidget(self.wdg_output_exe_icon)

        self.wdg_output_exe_version = QWidget(self.wdg_option)
        self.wdg_output_exe_version.setObjectName(u"wdg_output_exe_version")
        sizePolicy1.setHeightForWidth(self.wdg_output_exe_version.sizePolicy().hasHeightForWidth())
        self.wdg_output_exe_version.setSizePolicy(sizePolicy1)
        self.horizontalLayout_17 = QHBoxLayout(self.wdg_output_exe_version)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lb_output_exe_version_icon = QLabel(self.wdg_output_exe_version)
        self.lb_output_exe_version_icon.setObjectName(u"lb_output_exe_version_icon")
        sizePolicy5.setHeightForWidth(self.lb_output_exe_version_icon.sizePolicy().hasHeightForWidth())
        self.lb_output_exe_version_icon.setSizePolicy(sizePolicy5)

        self.horizontalLayout_17.addWidget(self.lb_output_exe_version_icon)

        self.widget_19 = QWidget(self.wdg_output_exe_version)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy3.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy3)
        self.verticalLayout_10 = QVBoxLayout(self.widget_19)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lb_output_exe_version = QLabel(self.widget_19)
        self.lb_output_exe_version.setObjectName(u"lb_output_exe_version")
        sizePolicy1.setHeightForWidth(self.lb_output_exe_version.sizePolicy().hasHeightForWidth())
        self.lb_output_exe_version.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.lb_output_exe_version)

        self.le_output_exe_version = QLineEdit(self.widget_19)
        self.le_output_exe_version.setObjectName(u"le_output_exe_version")
        sizePolicy1.setHeightForWidth(self.le_output_exe_version.sizePolicy().hasHeightForWidth())
        self.le_output_exe_version.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.le_output_exe_version)


        self.horizontalLayout_17.addWidget(self.widget_19)

        self.widget_15 = QWidget(self.wdg_output_exe_version)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy7.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy7)

        self.horizontalLayout_17.addWidget(self.widget_15)

        self.lb_output_exe_version_browser = QPushButton(self.wdg_output_exe_version)
        self.lb_output_exe_version_browser.setObjectName(u"lb_output_exe_version_browser")
        sizePolicy5.setHeightForWidth(self.lb_output_exe_version_browser.sizePolicy().hasHeightForWidth())
        self.lb_output_exe_version_browser.setSizePolicy(sizePolicy5)
        self.lb_output_exe_version_browser.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.lb_output_exe_version_browser)

        self.pb_output_exe_version_edit = QPushButton(self.wdg_output_exe_version)
        self.pb_output_exe_version_edit.setObjectName(u"pb_output_exe_version_edit")
        sizePolicy5.setHeightForWidth(self.pb_output_exe_version_edit.sizePolicy().hasHeightForWidth())
        self.pb_output_exe_version_edit.setSizePolicy(sizePolicy5)
        self.pb_output_exe_version_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.pb_output_exe_version_edit)


        self.verticalLayout_18.addWidget(self.wdg_output_exe_version)


        self.verticalLayout_17.addWidget(self.wdg_option)

        self.wdg_output_form = QWidget(self.page_base)
        self.wdg_output_form.setObjectName(u"wdg_output_form")
        sizePolicy6.setHeightForWidth(self.wdg_output_form.sizePolicy().hasHeightForWidth())
        self.wdg_output_form.setSizePolicy(sizePolicy6)
        self.horizontalLayout_23 = QHBoxLayout(self.wdg_output_form)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(10, 10, 10, 10)
        self.lb_output_form = QLabel(self.wdg_output_form)
        self.lb_output_form.setObjectName(u"lb_output_form")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy11.setHorizontalStretch(50)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.lb_output_form.sizePolicy().hasHeightForWidth())
        self.lb_output_form.setSizePolicy(sizePolicy11)

        self.horizontalLayout_23.addWidget(self.lb_output_form)

        self.rb_output_form_folder = QRadioButton(self.wdg_output_form)
        self.rb_output_form_folder.setObjectName(u"rb_output_form_folder")
        sizePolicy3.setHeightForWidth(self.rb_output_form_folder.sizePolicy().hasHeightForWidth())
        self.rb_output_form_folder.setSizePolicy(sizePolicy3)
        self.rb_output_form_folder.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_23.addWidget(self.rb_output_form_folder)

        self.rb_output_form_file = QRadioButton(self.wdg_output_form)
        self.rb_output_form_file.setObjectName(u"rb_output_form_file")
        sizePolicy3.setHeightForWidth(self.rb_output_form_file.sizePolicy().hasHeightForWidth())
        self.rb_output_form_file.setSizePolicy(sizePolicy3)
        self.rb_output_form_file.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rb_output_form_file.setChecked(True)

        self.horizontalLayout_23.addWidget(self.rb_output_form_file)


        self.verticalLayout_17.addWidget(self.wdg_output_form)

        self.wdg_exe_console_display = QWidget(self.page_base)
        self.wdg_exe_console_display.setObjectName(u"wdg_exe_console_display")
        sizePolicy6.setHeightForWidth(self.wdg_exe_console_display.sizePolicy().hasHeightForWidth())
        self.wdg_exe_console_display.setSizePolicy(sizePolicy6)
        self.horizontalLayout_24 = QHBoxLayout(self.wdg_exe_console_display)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(10, 10, 10, 10)
        self.lb_exe_console_display = QLabel(self.wdg_exe_console_display)
        self.lb_exe_console_display.setObjectName(u"lb_exe_console_display")
        sizePolicy11.setHeightForWidth(self.lb_exe_console_display.sizePolicy().hasHeightForWidth())
        self.lb_exe_console_display.setSizePolicy(sizePolicy11)

        self.horizontalLayout_24.addWidget(self.lb_exe_console_display)

        self.rb_exe_console_display_show = QRadioButton(self.wdg_exe_console_display)
        self.rb_exe_console_display_show.setObjectName(u"rb_exe_console_display_show")
        sizePolicy3.setHeightForWidth(self.rb_exe_console_display_show.sizePolicy().hasHeightForWidth())
        self.rb_exe_console_display_show.setSizePolicy(sizePolicy3)
        self.rb_exe_console_display_show.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rb_exe_console_display_show.setChecked(True)

        self.horizontalLayout_24.addWidget(self.rb_exe_console_display_show)

        self.rb_exe_console_display_hide = QRadioButton(self.wdg_exe_console_display)
        self.rb_exe_console_display_hide.setObjectName(u"rb_exe_console_display_hide")
        sizePolicy3.setHeightForWidth(self.rb_exe_console_display_hide.sizePolicy().hasHeightForWidth())
        self.rb_exe_console_display_hide.setSizePolicy(sizePolicy3)
        self.rb_exe_console_display_hide.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_24.addWidget(self.rb_exe_console_display_hide)


        self.verticalLayout_17.addWidget(self.wdg_exe_console_display)

        self.widget_32 = QWidget(self.page_base)
        self.widget_32.setObjectName(u"widget_32")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(11)
        sizePolicy12.setHeightForWidth(self.widget_32.sizePolicy().hasHeightForWidth())
        self.widget_32.setSizePolicy(sizePolicy12)

        self.verticalLayout_17.addWidget(self.widget_32)

        self.stackedWidget.addWidget(self.page_base)
        self.page_advance = QWidget()
        self.page_advance.setObjectName(u"page_advance")
        self.verticalLayout_50 = QVBoxLayout(self.page_advance)
        self.verticalLayout_50.setSpacing(10)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(10, 10, 10, 10)
        self.widget_31 = QWidget(self.page_advance)
        self.widget_31.setObjectName(u"widget_31")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(90)
        sizePolicy13.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy13)
        self.gridLayout = QGridLayout(self.widget_31)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(10, 5, 10, 5)
        self.pushButton_3 = QPushButton(self.widget_31)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_31)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton_35 = QPushButton(self.widget_31)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy1.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy1)
        self.pushButton_35.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_35, 0, 2, 1, 1)

        self.pushButton_36 = QPushButton(self.widget_31)
        self.pushButton_36.setObjectName(u"pushButton_36")
        sizePolicy1.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy1)
        self.pushButton_36.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_36, 1, 0, 1, 1)

        self.pushButton_37 = QPushButton(self.widget_31)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy1.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy1)
        self.pushButton_37.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_37, 1, 1, 1, 1)

        self.pushButton_38 = QPushButton(self.widget_31)
        self.pushButton_38.setObjectName(u"pushButton_38")
        sizePolicy1.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy1)
        self.pushButton_38.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_38, 1, 2, 1, 1)

        self.pushButton = QPushButton(self.widget_31)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)


        self.verticalLayout_50.addWidget(self.widget_31)

        self.widget_81 = QWidget(self.page_advance)
        self.widget_81.setObjectName(u"widget_81")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(35)
        sizePolicy14.setHeightForWidth(self.widget_81.sizePolicy().hasHeightForWidth())
        self.widget_81.setSizePolicy(sizePolicy14)
        self.gridLayout_2 = QGridLayout(self.widget_81)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(10, 5, 10, 5)
        self.pushButton_10 = QPushButton(self.widget_81)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy1.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy1)
        self.pushButton_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.pushButton_10, 0, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.widget_81)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)
        self.pushButton_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.pushButton_11, 0, 1, 1, 1)

        self.pushButton_43 = QPushButton(self.widget_81)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy1.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy1)
        self.pushButton_43.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.pushButton_43, 0, 2, 1, 1)


        self.verticalLayout_50.addWidget(self.widget_81)

        self.widget = QWidget(self.page_advance)
        self.widget.setObjectName(u"widget")
        sizePolicy14.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy14)
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(10, 5, 10, 5)
        self.pushButton_39 = QPushButton(self.widget)
        self.pushButton_39.setObjectName(u"pushButton_39")
        sizePolicy1.setHeightForWidth(self.pushButton_39.sizePolicy().hasHeightForWidth())
        self.pushButton_39.setSizePolicy(sizePolicy1)
        self.pushButton_39.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.pushButton_39, 0, 0, 1, 1)

        self.pushButton_40 = QPushButton(self.widget)
        self.pushButton_40.setObjectName(u"pushButton_40")
        sizePolicy1.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy1)
        self.pushButton_40.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.pushButton_40, 0, 1, 1, 1)

        self.widget_79 = QWidget(self.widget)
        self.widget_79.setObjectName(u"widget_79")
        sizePolicy1.setHeightForWidth(self.widget_79.sizePolicy().hasHeightForWidth())
        self.widget_79.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.widget_79, 0, 2, 1, 1)


        self.verticalLayout_50.addWidget(self.widget)

        self.widget_33 = QWidget(self.page_advance)
        self.widget_33.setObjectName(u"widget_33")
        sizePolicy14.setHeightForWidth(self.widget_33.sizePolicy().hasHeightForWidth())
        self.widget_33.setSizePolicy(sizePolicy14)
        self.gridLayout_4 = QGridLayout(self.widget_33)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(10, 5, 10, 5)
        self.pushButton_41 = QPushButton(self.widget_33)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy1.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy1)
        self.pushButton_41.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.pushButton_41, 0, 0, 1, 1)

        self.pushButton_42 = QPushButton(self.widget_33)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy1.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy1)
        self.pushButton_42.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.pushButton_42, 0, 1, 1, 1)

        self.widget_30 = QWidget(self.widget_33)
        self.widget_30.setObjectName(u"widget_30")
        sizePolicy1.setHeightForWidth(self.widget_30.sizePolicy().hasHeightForWidth())
        self.widget_30.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.widget_30, 0, 2, 1, 1)


        self.verticalLayout_50.addWidget(self.widget_33)

        self.widget_82 = QWidget(self.page_advance)
        self.widget_82.setObjectName(u"widget_82")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(62)
        sizePolicy15.setHeightForWidth(self.widget_82.sizePolicy().hasHeightForWidth())
        self.widget_82.setSizePolicy(sizePolicy15)
        self.gridLayout_5 = QGridLayout(self.widget_82)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(20)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setContentsMargins(10, 5, 10, 5)
        self.pushButton_44 = QPushButton(self.widget_82)
        self.pushButton_44.setObjectName(u"pushButton_44")
        sizePolicy1.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy1)
        self.pushButton_44.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.pushButton_44, 0, 0, 1, 1)

        self.pushButton_30 = QPushButton(self.widget_82)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy1.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy1)
        self.pushButton_30.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.pushButton_30, 0, 1, 1, 1)

        self.pushButton_47 = QPushButton(self.widget_82)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy1.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy1)
        self.pushButton_47.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.pushButton_47, 0, 2, 1, 1)

        self.checkBox_10 = QCheckBox(self.widget_82)
        self.checkBox_10.setObjectName(u"checkBox_10")
        sizePolicy1.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy1)
        self.checkBox_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.checkBox_10, 1, 0, 1, 1)

        self.pushButton_45 = QPushButton(self.widget_82)
        self.pushButton_45.setObjectName(u"pushButton_45")
        sizePolicy1.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy1)
        self.pushButton_45.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.pushButton_45, 1, 1, 1, 1)

        self.pushButton_31 = QPushButton(self.widget_82)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy1.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy1)
        self.pushButton_31.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.pushButton_31, 1, 2, 1, 1)


        self.verticalLayout_50.addWidget(self.widget_82)

        self.widget_80 = QWidget(self.page_advance)
        self.widget_80.setObjectName(u"widget_80")
        sizePolicy13.setHeightForWidth(self.widget_80.sizePolicy().hasHeightForWidth())
        self.widget_80.setSizePolicy(sizePolicy13)
        self.gridLayout_6 = QGridLayout(self.widget_80)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(20)
        self.gridLayout_6.setVerticalSpacing(10)
        self.gridLayout_6.setContentsMargins(10, 5, 10, 5)
        self.pushButton_46 = QPushButton(self.widget_80)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy1.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy1)
        self.pushButton_46.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.pushButton_46, 0, 0, 1, 1)

        self.pushButton_33 = QPushButton(self.widget_80)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy1.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy1)
        self.pushButton_33.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.pushButton_33, 0, 1, 1, 1)

        self.pushButton_34 = QPushButton(self.widget_80)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy1.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy1)
        self.pushButton_34.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.pushButton_34, 0, 2, 1, 1)

        self.checkBox_8 = QCheckBox(self.widget_80)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy1.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy1)
        self.checkBox_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.checkBox_8, 1, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.widget_80)
        self.checkBox_7.setObjectName(u"checkBox_7")
        sizePolicy1.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy1)
        self.checkBox_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.checkBox_7, 1, 1, 1, 1)

        self.checkBox_15 = QCheckBox(self.widget_80)
        self.checkBox_15.setObjectName(u"checkBox_15")
        sizePolicy1.setHeightForWidth(self.checkBox_15.sizePolicy().hasHeightForWidth())
        self.checkBox_15.setSizePolicy(sizePolicy1)
        self.checkBox_15.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.checkBox_15, 1, 2, 1, 1)

        self.checkBox_11 = QCheckBox(self.widget_80)
        self.checkBox_11.setObjectName(u"checkBox_11")
        sizePolicy1.setHeightForWidth(self.checkBox_11.sizePolicy().hasHeightForWidth())
        self.checkBox_11.setSizePolicy(sizePolicy1)
        self.checkBox_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.checkBox_11, 2, 0, 1, 1)


        self.verticalLayout_50.addWidget(self.widget_80)

        self.widget_83 = QWidget(self.page_advance)
        self.widget_83.setObjectName(u"widget_83")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(50)
        sizePolicy16.setHeightForWidth(self.widget_83.sizePolicy().hasHeightForWidth())
        self.widget_83.setSizePolicy(sizePolicy16)

        self.verticalLayout_50.addWidget(self.widget_83)

        self.stackedWidget.addWidget(self.page_advance)
        self.page_ios_win = QWidget()
        self.page_ios_win.setObjectName(u"page_ios_win")
        self.verticalLayout_51 = QVBoxLayout(self.page_ios_win)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.groupBox = QGroupBox(self.page_ios_win)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy17 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(30)
        sizePolicy17.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy17)
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(20)
        self.gridLayout_7.setVerticalSpacing(10)
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.pushButton_16 = QPushButton(self.groupBox)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy1.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy1)
        self.pushButton_16.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_7.addWidget(self.pushButton_16, 0, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.groupBox)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy1.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy1)
        self.pushButton_17.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_7.addWidget(self.pushButton_17, 0, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.groupBox)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy1.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy1)
        self.pushButton_15.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_7.addWidget(self.pushButton_15, 0, 2, 1, 1)

        self.pushButton_29 = QPushButton(self.groupBox)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy1.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy1)
        self.pushButton_29.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_7.addWidget(self.pushButton_29, 1, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy1.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy1)
        self.checkBox_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_7.addWidget(self.checkBox_3, 1, 1, 1, 1)


        self.verticalLayout_51.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.page_ios_win)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy17.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy17)
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(20)
        self.gridLayout_8.setVerticalSpacing(10)
        self.gridLayout_8.setContentsMargins(10, 10, 10, 10)
        self.pushButton_12 = QPushButton(self.groupBox_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy1.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy1)
        self.pushButton_12.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_8.addWidget(self.pushButton_12, 0, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.groupBox_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy1.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy1)
        self.pushButton_13.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_8.addWidget(self.pushButton_13, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy1.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy1)
        self.checkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_8.addWidget(self.checkBox, 1, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy1.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy1)
        self.checkBox_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_8.addWidget(self.checkBox_2, 1, 1, 1, 1)

        self.checkBox_9 = QCheckBox(self.groupBox_2)
        self.checkBox_9.setObjectName(u"checkBox_9")
        sizePolicy1.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy1)
        self.checkBox_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_8.addWidget(self.checkBox_9, 1, 2, 1, 1)


        self.verticalLayout_51.addWidget(self.groupBox_2)

        self.widget_84 = QWidget(self.page_ios_win)
        self.widget_84.setObjectName(u"widget_84")
        sizePolicy2.setHeightForWidth(self.widget_84.sizePolicy().hasHeightForWidth())
        self.widget_84.setSizePolicy(sizePolicy2)

        self.verticalLayout_51.addWidget(self.widget_84)

        self.stackedWidget.addWidget(self.page_ios_win)
        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.verticalLayout_30 = QVBoxLayout(self.page_info)
        self.verticalLayout_30.setSpacing(10)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(10, 10, 10, 10)
        self.scrollArea_info = QScrollArea(self.page_info)
        self.scrollArea_info.setObjectName(u"scrollArea_info")
        self.scrollArea_info.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 767, 643))
        self.verticalLayout_29 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(10, 10, 10, 10)
        self.tbwdg_info = QTableWidget(self.scrollAreaWidgetContents_2)
        self.tbwdg_info.setObjectName(u"tbwdg_info")

        self.verticalLayout_29.addWidget(self.tbwdg_info)

        self.scrollArea_info.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_30.addWidget(self.scrollArea_info)

        self.stackedWidget.addWidget(self.page_info)
        self.page_command_display = QWidget()
        self.page_command_display.setObjectName(u"page_command_display")
        self.verticalLayout_3 = QVBoxLayout(self.page_command_display)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.wdg_tb_command_display = QWidget(self.page_command_display)
        self.wdg_tb_command_display.setObjectName(u"wdg_tb_command_display")
        sizePolicy2.setHeightForWidth(self.wdg_tb_command_display.sizePolicy().hasHeightForWidth())
        self.wdg_tb_command_display.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.wdg_tb_command_display)

        self.widget_2 = QWidget(self.page_command_display)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy8.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy8)

        self.verticalLayout_3.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_command_display)
        self.page_console = QWidget()
        self.page_console.setObjectName(u"page_console")
        self.verticalLayout_13 = QVBoxLayout(self.page_console)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.wdg_tb_console = QWidget(self.page_console)
        self.wdg_tb_console.setObjectName(u"wdg_tb_console")
        sizePolicy1.setHeightForWidth(self.wdg_tb_console.sizePolicy().hasHeightForWidth())
        self.wdg_tb_console.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.wdg_tb_console)

        self.stackedWidget.addWidget(self.page_console)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.verticalLayout_20 = QVBoxLayout(self.page_setting)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(20, 20, 20, 20)
        self.tabWidget = QTabWidget(self.page_setting)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tab_common = QWidget()
        self.tab_common.setObjectName(u"tab_common")
        self.verticalLayout_21 = QVBoxLayout(self.tab_common)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(10, 10, 10, 10)
        self.wdg_language = QWidget(self.tab_common)
        self.wdg_language.setObjectName(u"wdg_language")
        sizePolicy18 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(20)
        sizePolicy18.setHeightForWidth(self.wdg_language.sizePolicy().hasHeightForWidth())
        self.wdg_language.setSizePolicy(sizePolicy18)
        self.horizontalLayout_27 = QHBoxLayout(self.wdg_language)
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.lb_language = QLabel(self.wdg_language)
        self.lb_language.setObjectName(u"lb_language")
        sizePolicy19 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy19.setHorizontalStretch(40)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.lb_language.sizePolicy().hasHeightForWidth())
        self.lb_language.setSizePolicy(sizePolicy19)

        self.horizontalLayout_27.addWidget(self.lb_language)

        self.cbb_language = QComboBox(self.wdg_language)
        self.cbb_language.setObjectName(u"cbb_language")
        sizePolicy11.setHeightForWidth(self.cbb_language.sizePolicy().hasHeightForWidth())
        self.cbb_language.setSizePolicy(sizePolicy11)

        self.horizontalLayout_27.addWidget(self.cbb_language)

        self.widget_331 = QWidget(self.wdg_language)
        self.widget_331.setObjectName(u"widget_331")
        sizePolicy3.setHeightForWidth(self.widget_331.sizePolicy().hasHeightForWidth())
        self.widget_331.setSizePolicy(sizePolicy3)

        self.horizontalLayout_27.addWidget(self.widget_331)


        self.verticalLayout_21.addWidget(self.wdg_language)

        self.wdg_build_files_clear = QWidget(self.tab_common)
        self.wdg_build_files_clear.setObjectName(u"wdg_build_files_clear")
        sizePolicy18.setHeightForWidth(self.wdg_build_files_clear.sizePolicy().hasHeightForWidth())
        self.wdg_build_files_clear.setSizePolicy(sizePolicy18)
        self.horizontalLayout_26 = QHBoxLayout(self.wdg_build_files_clear)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.lb_build_files_clear = QLabel(self.wdg_build_files_clear)
        self.lb_build_files_clear.setObjectName(u"lb_build_files_clear")
        sizePolicy19.setHeightForWidth(self.lb_build_files_clear.sizePolicy().hasHeightForWidth())
        self.lb_build_files_clear.setSizePolicy(sizePolicy19)

        self.horizontalLayout_26.addWidget(self.lb_build_files_clear)

        self.cbb_build_files_clear = QCheckBox(self.wdg_build_files_clear)
        self.cbb_build_files_clear.setObjectName(u"cbb_build_files_clear")
        sizePolicy11.setHeightForWidth(self.cbb_build_files_clear.sizePolicy().hasHeightForWidth())
        self.cbb_build_files_clear.setSizePolicy(sizePolicy11)
        self.cbb_build_files_clear.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbb_build_files_clear.setChecked(True)

        self.horizontalLayout_26.addWidget(self.cbb_build_files_clear)

        self.widget_34 = QWidget(self.wdg_build_files_clear)
        self.widget_34.setObjectName(u"widget_34")
        sizePolicy3.setHeightForWidth(self.widget_34.sizePolicy().hasHeightForWidth())
        self.widget_34.setSizePolicy(sizePolicy3)

        self.horizontalLayout_26.addWidget(self.widget_34)


        self.verticalLayout_21.addWidget(self.wdg_build_files_clear)

        self.widget_27 = QWidget(self.tab_common)
        self.widget_27.setObjectName(u"widget_27")
        sizePolicy6.setHeightForWidth(self.widget_27.sizePolicy().hasHeightForWidth())
        self.widget_27.setSizePolicy(sizePolicy6)
        self.horizontalLayout_22 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.widget_27)
        self.label.setObjectName(u"label")
        sizePolicy20 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy20.setHorizontalStretch(26)
        sizePolicy20.setVerticalStretch(0)
        sizePolicy20.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy20)

        self.horizontalLayout_22.addWidget(self.label)

        self.widget_28 = QWidget(self.widget_27)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy3.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy3)
        self.horizontalLayout_21 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.rb_use_auto_select = QRadioButton(self.widget_28)
        self.rb_use_auto_select.setObjectName(u"rb_use_auto_select")
        sizePolicy1.setHeightForWidth(self.rb_use_auto_select.sizePolicy().hasHeightForWidth())
        self.rb_use_auto_select.setSizePolicy(sizePolicy1)
        self.rb_use_auto_select.setChecked(True)

        self.horizontalLayout_21.addWidget(self.rb_use_auto_select)

        self.rb_use_pyinstaller = QRadioButton(self.widget_28)
        self.rb_use_pyinstaller.setObjectName(u"rb_use_pyinstaller")
        sizePolicy1.setHeightForWidth(self.rb_use_pyinstaller.sizePolicy().hasHeightForWidth())
        self.rb_use_pyinstaller.setSizePolicy(sizePolicy1)
        self.rb_use_pyinstaller.setChecked(False)

        self.horizontalLayout_21.addWidget(self.rb_use_pyinstaller)

        self.rb_use_python = QRadioButton(self.widget_28)
        self.rb_use_python.setObjectName(u"rb_use_python")
        sizePolicy1.setHeightForWidth(self.rb_use_python.sizePolicy().hasHeightForWidth())
        self.rb_use_python.setSizePolicy(sizePolicy1)

        self.horizontalLayout_21.addWidget(self.rb_use_python)

        self.rb_use_virtual_env = QRadioButton(self.widget_28)
        self.rb_use_virtual_env.setObjectName(u"rb_use_virtual_env")
        sizePolicy1.setHeightForWidth(self.rb_use_virtual_env.sizePolicy().hasHeightForWidth())
        self.rb_use_virtual_env.setSizePolicy(sizePolicy1)

        self.horizontalLayout_21.addWidget(self.rb_use_virtual_env)


        self.horizontalLayout_22.addWidget(self.widget_28)


        self.verticalLayout_21.addWidget(self.widget_27)

        self.wdg_win_setting = QWidget(self.tab_common)
        self.wdg_win_setting.setObjectName(u"wdg_win_setting")
        sizePolicy8.setHeightForWidth(self.wdg_win_setting.sizePolicy().hasHeightForWidth())
        self.wdg_win_setting.setSizePolicy(sizePolicy8)
        self.verticalLayout_22 = QVBoxLayout(self.wdg_win_setting)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_36 = QWidget(self.wdg_win_setting)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy18.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy18)
        self.horizontalLayout_28 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 5, 5)
        self.lb_tooltip_show = QLabel(self.widget_36)
        self.lb_tooltip_show.setObjectName(u"lb_tooltip_show")
        sizePolicy19.setHeightForWidth(self.lb_tooltip_show.sizePolicy().hasHeightForWidth())
        self.lb_tooltip_show.setSizePolicy(sizePolicy19)

        self.horizontalLayout_28.addWidget(self.lb_tooltip_show)

        self.cbb_tooltip_show = QCheckBox(self.widget_36)
        self.cbb_tooltip_show.setObjectName(u"cbb_tooltip_show")
        sizePolicy11.setHeightForWidth(self.cbb_tooltip_show.sizePolicy().hasHeightForWidth())
        self.cbb_tooltip_show.setSizePolicy(sizePolicy11)
        self.cbb_tooltip_show.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbb_tooltip_show.setChecked(True)

        self.horizontalLayout_28.addWidget(self.cbb_tooltip_show)

        self.widget_37 = QWidget(self.widget_36)
        self.widget_37.setObjectName(u"widget_37")
        sizePolicy3.setHeightForWidth(self.widget_37.sizePolicy().hasHeightForWidth())
        self.widget_37.setSizePolicy(sizePolicy3)

        self.horizontalLayout_28.addWidget(self.widget_37)


        self.verticalLayout_22.addWidget(self.widget_36)

        self.widget_38 = QWidget(self.wdg_win_setting)
        self.widget_38.setObjectName(u"widget_38")
        sizePolicy18.setHeightForWidth(self.widget_38.sizePolicy().hasHeightForWidth())
        self.widget_38.setSizePolicy(sizePolicy18)
        self.horizontalLayout_29 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(5, 5, 5, 5)
        self.lb_multi_win = QLabel(self.widget_38)
        self.lb_multi_win.setObjectName(u"lb_multi_win")
        sizePolicy19.setHeightForWidth(self.lb_multi_win.sizePolicy().hasHeightForWidth())
        self.lb_multi_win.setSizePolicy(sizePolicy19)

        self.horizontalLayout_29.addWidget(self.lb_multi_win)

        self.cbb_multi_win = QCheckBox(self.widget_38)
        self.cbb_multi_win.setObjectName(u"cbb_multi_win")
        sizePolicy11.setHeightForWidth(self.cbb_multi_win.sizePolicy().hasHeightForWidth())
        self.cbb_multi_win.setSizePolicy(sizePolicy11)
        self.cbb_multi_win.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbb_multi_win.setChecked(True)

        self.horizontalLayout_29.addWidget(self.cbb_multi_win)

        self.widget_39 = QWidget(self.widget_38)
        self.widget_39.setObjectName(u"widget_39")
        sizePolicy3.setHeightForWidth(self.widget_39.sizePolicy().hasHeightForWidth())
        self.widget_39.setSizePolicy(sizePolicy3)

        self.horizontalLayout_29.addWidget(self.widget_39)


        self.verticalLayout_22.addWidget(self.widget_38)


        self.verticalLayout_21.addWidget(self.wdg_win_setting)

        self.widget_40 = QWidget(self.tab_common)
        self.widget_40.setObjectName(u"widget_40")
        sizePolicy2.setHeightForWidth(self.widget_40.sizePolicy().hasHeightForWidth())
        self.widget_40.setSizePolicy(sizePolicy2)

        self.verticalLayout_21.addWidget(self.widget_40)

        self.tabWidget.addTab(self.tab_common, "")
        self.tab_env = QWidget()
        self.tab_env.setObjectName(u"tab_env")
        self.verticalLayout_5 = QVBoxLayout(self.tab_env)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.wdg_currnt_env = QWidget(self.tab_env)
        self.wdg_currnt_env.setObjectName(u"wdg_currnt_env")
        sizePolicy21 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy21.setHorizontalStretch(0)
        sizePolicy21.setVerticalStretch(10)
        sizePolicy21.setHeightForWidth(self.wdg_currnt_env.sizePolicy().hasHeightForWidth())
        self.wdg_currnt_env.setSizePolicy(sizePolicy21)
        self.horizontalLayout_20 = QHBoxLayout(self.wdg_currnt_env)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.widget_26 = QWidget(self.wdg_currnt_env)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy3.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy3)
        self.verticalLayout_12 = QVBoxLayout(self.widget_26)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_48 = QWidget(self.widget_26)
        self.widget_48.setObjectName(u"widget_48")
        sizePolicy1.setHeightForWidth(self.widget_48.sizePolicy().hasHeightForWidth())
        self.widget_48.setSizePolicy(sizePolicy1)
        self.horizontalLayout_33 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.lb_env_current_title_page_setting_env = QLabel(self.widget_48)
        self.lb_env_current_title_page_setting_env.setObjectName(u"lb_env_current_title_page_setting_env")
        sizePolicy19.setHeightForWidth(self.lb_env_current_title_page_setting_env.sizePolicy().hasHeightForWidth())
        self.lb_env_current_title_page_setting_env.setSizePolicy(sizePolicy19)

        self.horizontalLayout_33.addWidget(self.lb_env_current_title_page_setting_env)

        self.lb_env_current_name_page_setting_env = QLabel(self.widget_48)
        self.lb_env_current_name_page_setting_env.setObjectName(u"lb_env_current_name_page_setting_env")
        sizePolicy3.setHeightForWidth(self.lb_env_current_name_page_setting_env.sizePolicy().hasHeightForWidth())
        self.lb_env_current_name_page_setting_env.setSizePolicy(sizePolicy3)

        self.horizontalLayout_33.addWidget(self.lb_env_current_name_page_setting_env)


        self.verticalLayout_12.addWidget(self.widget_48)

        self.widget_49 = QWidget(self.widget_26)
        self.widget_49.setObjectName(u"widget_49")
        sizePolicy1.setHeightForWidth(self.widget_49.sizePolicy().hasHeightForWidth())
        self.widget_49.setSizePolicy(sizePolicy1)
        self.horizontalLayout_32 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.lb_env_current_path_title_page_setting_env = QLabel(self.widget_49)
        self.lb_env_current_path_title_page_setting_env.setObjectName(u"lb_env_current_path_title_page_setting_env")
        sizePolicy22 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy22.setHorizontalStretch(30)
        sizePolicy22.setVerticalStretch(0)
        sizePolicy22.setHeightForWidth(self.lb_env_current_path_title_page_setting_env.sizePolicy().hasHeightForWidth())
        self.lb_env_current_path_title_page_setting_env.setSizePolicy(sizePolicy22)

        self.horizontalLayout_32.addWidget(self.lb_env_current_path_title_page_setting_env)

        self.lb_env_current_path_page_setting_env = QLabel(self.widget_49)
        self.lb_env_current_path_page_setting_env.setObjectName(u"lb_env_current_path_page_setting_env")
        sizePolicy3.setHeightForWidth(self.lb_env_current_path_page_setting_env.sizePolicy().hasHeightForWidth())
        self.lb_env_current_path_page_setting_env.setSizePolicy(sizePolicy3)

        self.horizontalLayout_32.addWidget(self.lb_env_current_path_page_setting_env)


        self.verticalLayout_12.addWidget(self.widget_49)


        self.horizontalLayout_20.addWidget(self.widget_26)

        self.lb_env_current_check_install_page_setting_env = QLabel(self.wdg_currnt_env)
        self.lb_env_current_check_install_page_setting_env.setObjectName(u"lb_env_current_check_install_page_setting_env")
        sizePolicy.setHeightForWidth(self.lb_env_current_check_install_page_setting_env.sizePolicy().hasHeightForWidth())
        self.lb_env_current_check_install_page_setting_env.setSizePolicy(sizePolicy)

        self.horizontalLayout_20.addWidget(self.lb_env_current_check_install_page_setting_env)


        self.verticalLayout_5.addWidget(self.wdg_currnt_env)

        self.wdg_env_sys = QWidget(self.tab_env)
        self.wdg_env_sys.setObjectName(u"wdg_env_sys")
        sizePolicy6.setHeightForWidth(self.wdg_env_sys.sizePolicy().hasHeightForWidth())
        self.wdg_env_sys.setSizePolicy(sizePolicy6)
        self.horizontalLayout_30 = QHBoxLayout(self.wdg_env_sys)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(10, 10, 10, 10)
        self.widget_43 = QWidget(self.wdg_env_sys)
        self.widget_43.setObjectName(u"widget_43")
        sizePolicy3.setHeightForWidth(self.widget_43.sizePolicy().hasHeightForWidth())
        self.widget_43.setSizePolicy(sizePolicy3)
        self.verticalLayout_23 = QVBoxLayout(self.widget_43)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_53 = QWidget(self.widget_43)
        self.widget_53.setObjectName(u"widget_53")
        sizePolicy1.setHeightForWidth(self.widget_53.sizePolicy().hasHeightForWidth())
        self.widget_53.setSizePolicy(sizePolicy1)
        self.horizontalLayout_36 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_36.setSpacing(10)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.rb_env_sys = QRadioButton(self.widget_53)
        self.rb_env_sys.setObjectName(u"rb_env_sys")
        sizePolicy5.setHeightForWidth(self.rb_env_sys.sizePolicy().hasHeightForWidth())
        self.rb_env_sys.setSizePolicy(sizePolicy5)
        self.rb_env_sys.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rb_env_sys.setChecked(True)

        self.horizontalLayout_36.addWidget(self.rb_env_sys)

        self.lb_env_sys_name_page_setting_env = QLabel(self.widget_53)
        self.lb_env_sys_name_page_setting_env.setObjectName(u"lb_env_sys_name_page_setting_env")
        sizePolicy3.setHeightForWidth(self.lb_env_sys_name_page_setting_env.sizePolicy().hasHeightForWidth())
        self.lb_env_sys_name_page_setting_env.setSizePolicy(sizePolicy3)

        self.horizontalLayout_36.addWidget(self.lb_env_sys_name_page_setting_env)


        self.verticalLayout_23.addWidget(self.widget_53)

        self.lb_env_sys_path_page_setting_env = QLabel(self.widget_43)
        self.lb_env_sys_path_page_setting_env.setObjectName(u"lb_env_sys_path_page_setting_env")
        sizePolicy1.setHeightForWidth(self.lb_env_sys_path_page_setting_env.sizePolicy().hasHeightForWidth())
        self.lb_env_sys_path_page_setting_env.setSizePolicy(sizePolicy1)

        self.verticalLayout_23.addWidget(self.lb_env_sys_path_page_setting_env)


        self.horizontalLayout_30.addWidget(self.widget_43)

        self.pb_env_sys_edit_page_setting_env = QPushButton(self.wdg_env_sys)
        self.pb_env_sys_edit_page_setting_env.setObjectName(u"pb_env_sys_edit_page_setting_env")
        sizePolicy5.setHeightForWidth(self.pb_env_sys_edit_page_setting_env.sizePolicy().hasHeightForWidth())
        self.pb_env_sys_edit_page_setting_env.setSizePolicy(sizePolicy5)
        self.pb_env_sys_edit_page_setting_env.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_30.addWidget(self.pb_env_sys_edit_page_setting_env)

        self.widget_44 = QWidget(self.wdg_env_sys)
        self.widget_44.setObjectName(u"widget_44")
        sizePolicy23 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy23.setHorizontalStretch(14)
        sizePolicy23.setVerticalStretch(0)
        sizePolicy23.setHeightForWidth(self.widget_44.sizePolicy().hasHeightForWidth())
        self.widget_44.setSizePolicy(sizePolicy23)

        self.horizontalLayout_30.addWidget(self.widget_44)

        self.lb_env_sys_check_install_page_setting_env = QLabel(self.wdg_env_sys)
        self.lb_env_sys_check_install_page_setting_env.setObjectName(u"lb_env_sys_check_install_page_setting_env")
        sizePolicy.setHeightForWidth(self.lb_env_sys_check_install_page_setting_env.sizePolicy().hasHeightForWidth())
        self.lb_env_sys_check_install_page_setting_env.setSizePolicy(sizePolicy)

        self.horizontalLayout_30.addWidget(self.lb_env_sys_check_install_page_setting_env)


        self.verticalLayout_5.addWidget(self.wdg_env_sys)

        self.wdg_env_specified = QWidget(self.tab_env)
        self.wdg_env_specified.setObjectName(u"wdg_env_specified")
        sizePolicy21.setHeightForWidth(self.wdg_env_specified.sizePolicy().hasHeightForWidth())
        self.wdg_env_specified.setSizePolicy(sizePolicy21)
        self.horizontalLayout_37 = QHBoxLayout(self.wdg_env_specified)
        self.horizontalLayout_37.setSpacing(10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(10, 10, 10, 10)
        self.widget_24 = QWidget(self.wdg_env_specified)
        self.widget_24.setObjectName(u"widget_24")
        sizePolicy5.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy5)
        self.verticalLayout_11 = QVBoxLayout(self.widget_24)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rb_env_specified = QRadioButton(self.widget_24)
        self.rb_env_specified.setObjectName(u"rb_env_specified")
        sizePolicy1.setHeightForWidth(self.rb_env_specified.sizePolicy().hasHeightForWidth())
        self.rb_env_specified.setSizePolicy(sizePolicy1)
        self.rb_env_specified.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.rb_env_specified)

        self.widget_25 = QWidget(self.widget_24)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy1.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy1)

        self.verticalLayout_11.addWidget(self.widget_25)


        self.horizontalLayout_37.addWidget(self.widget_24)

        self.widget1 = QWidget(self.wdg_env_specified)
        self.widget1.setObjectName(u"widget1")
        sizePolicy3.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy3)
        self.verticalLayout_8 = QVBoxLayout(self.widget1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.widget1)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy1.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy1)
        self.horizontalLayout_19 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.le_env_specified_path_page_setting_env = QLineEdit(self.widget_23)
        self.le_env_specified_path_page_setting_env.setObjectName(u"le_env_specified_path_page_setting_env")
        sizePolicy3.setHeightForWidth(self.le_env_specified_path_page_setting_env.sizePolicy().hasHeightForWidth())
        self.le_env_specified_path_page_setting_env.setSizePolicy(sizePolicy3)

        self.horizontalLayout_19.addWidget(self.le_env_specified_path_page_setting_env)

        self.pb_env_specified_browser_page_setting_env = QPushButton(self.widget_23)
        self.pb_env_specified_browser_page_setting_env.setObjectName(u"pb_env_specified_browser_page_setting_env")
        sizePolicy5.setHeightForWidth(self.pb_env_specified_browser_page_setting_env.sizePolicy().hasHeightForWidth())
        self.pb_env_specified_browser_page_setting_env.setSizePolicy(sizePolicy5)
        self.pb_env_specified_browser_page_setting_env.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_19.addWidget(self.pb_env_specified_browser_page_setting_env)


        self.verticalLayout_8.addWidget(self.widget_23)

        self.lb_env_specified_hint_info_page_setting_env = QLabel(self.widget1)
        self.lb_env_specified_hint_info_page_setting_env.setObjectName(u"lb_env_specified_hint_info_page_setting_env")

        self.verticalLayout_8.addWidget(self.lb_env_specified_hint_info_page_setting_env)


        self.horizontalLayout_37.addWidget(self.widget1)

        self.widget_56 = QWidget(self.wdg_env_specified)
        self.widget_56.setObjectName(u"widget_56")
        sizePolicy24 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy24.setHorizontalStretch(20)
        sizePolicy24.setVerticalStretch(0)
        sizePolicy24.setHeightForWidth(self.widget_56.sizePolicy().hasHeightForWidth())
        self.widget_56.setSizePolicy(sizePolicy24)

        self.horizontalLayout_37.addWidget(self.widget_56)

        self.lb_env_specified_check_install_page_setting_env = QLabel(self.wdg_env_specified)
        self.lb_env_specified_check_install_page_setting_env.setObjectName(u"lb_env_specified_check_install_page_setting_env")
        sizePolicy.setHeightForWidth(self.lb_env_specified_check_install_page_setting_env.sizePolicy().hasHeightForWidth())
        self.lb_env_specified_check_install_page_setting_env.setSizePolicy(sizePolicy)

        self.horizontalLayout_37.addWidget(self.lb_env_specified_check_install_page_setting_env)


        self.verticalLayout_5.addWidget(self.wdg_env_specified)

        self.wdg_env_conda = QWidget(self.tab_env)
        self.wdg_env_conda.setObjectName(u"wdg_env_conda")
        sizePolicy2.setHeightForWidth(self.wdg_env_conda.sizePolicy().hasHeightForWidth())
        self.wdg_env_conda.setSizePolicy(sizePolicy2)
        self.verticalLayout_27 = QVBoxLayout(self.wdg_env_conda)
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(10, 10, 10, 10)
        self.widget_51 = QWidget(self.wdg_env_conda)
        self.widget_51.setObjectName(u"widget_51")
        sizePolicy6.setHeightForWidth(self.widget_51.sizePolicy().hasHeightForWidth())
        self.widget_51.setSizePolicy(sizePolicy6)
        self.horizontalLayout_35 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.rb_env_conda = QRadioButton(self.widget_51)
        self.rb_env_conda.setObjectName(u"rb_env_conda")
        sizePolicy22.setHeightForWidth(self.rb_env_conda.sizePolicy().hasHeightForWidth())
        self.rb_env_conda.setSizePolicy(sizePolicy22)
        self.rb_env_conda.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_35.addWidget(self.rb_env_conda)

        self.lb_env_conda_path_page_setting_env = QLabel(self.widget_51)
        self.lb_env_conda_path_page_setting_env.setObjectName(u"lb_env_conda_path_page_setting_env")
        sizePolicy3.setHeightForWidth(self.lb_env_conda_path_page_setting_env.sizePolicy().hasHeightForWidth())
        self.lb_env_conda_path_page_setting_env.setSizePolicy(sizePolicy3)

        self.horizontalLayout_35.addWidget(self.lb_env_conda_path_page_setting_env)

        self.lb_env_conda_check_install_page_setting_env = QLabel(self.widget_51)
        self.lb_env_conda_check_install_page_setting_env.setObjectName(u"lb_env_conda_check_install_page_setting_env")
        sizePolicy.setHeightForWidth(self.lb_env_conda_check_install_page_setting_env.sizePolicy().hasHeightForWidth())
        self.lb_env_conda_check_install_page_setting_env.setSizePolicy(sizePolicy)

        self.horizontalLayout_35.addWidget(self.lb_env_conda_check_install_page_setting_env)


        self.verticalLayout_27.addWidget(self.widget_51)

        self.tbwdg_env_conda = QTableWidget(self.wdg_env_conda)
        self.tbwdg_env_conda.setObjectName(u"tbwdg_env_conda")
        sizePolicy2.setHeightForWidth(self.tbwdg_env_conda.sizePolicy().hasHeightForWidth())
        self.tbwdg_env_conda.setSizePolicy(sizePolicy2)

        self.verticalLayout_27.addWidget(self.tbwdg_env_conda)


        self.verticalLayout_5.addWidget(self.wdg_env_conda)

        self.wdg_env_builtin = QWidget(self.tab_env)
        self.wdg_env_builtin.setObjectName(u"wdg_env_builtin")
        sizePolicy21.setHeightForWidth(self.wdg_env_builtin.sizePolicy().hasHeightForWidth())
        self.wdg_env_builtin.setSizePolicy(sizePolicy21)
        self.horizontalLayout_38 = QHBoxLayout(self.wdg_env_builtin)
        self.horizontalLayout_38.setSpacing(10)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(10, 10, 10, 10)
        self.rb_env_builtin = QRadioButton(self.wdg_env_builtin)
        self.rb_env_builtin.setObjectName(u"rb_env_builtin")
        sizePolicy5.setHeightForWidth(self.rb_env_builtin.sizePolicy().hasHeightForWidth())
        self.rb_env_builtin.setSizePolicy(sizePolicy5)
        self.rb_env_builtin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_38.addWidget(self.rb_env_builtin)


        self.verticalLayout_5.addWidget(self.wdg_env_builtin)

        self.widget_35 = QWidget(self.tab_env)
        self.widget_35.setObjectName(u"widget_35")
        sizePolicy21.setHeightForWidth(self.widget_35.sizePolicy().hasHeightForWidth())
        self.widget_35.setSizePolicy(sizePolicy21)

        self.verticalLayout_5.addWidget(self.widget_35)

        self.tabWidget.addTab(self.tab_env, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_20.addWidget(self.tabWidget)

        self.wdg_save_setting = QWidget(self.page_setting)
        self.wdg_save_setting.setObjectName(u"wdg_save_setting")
        sizePolicy21.setHeightForWidth(self.wdg_save_setting.sizePolicy().hasHeightForWidth())
        self.wdg_save_setting.setSizePolicy(sizePolicy21)
        self.horizontalLayout_25 = QHBoxLayout(self.wdg_save_setting)
        self.horizontalLayout_25.setSpacing(10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(10, 10, 10, 10)
        self.widget_18 = QWidget(self.wdg_save_setting)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy3.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy3)

        self.horizontalLayout_25.addWidget(self.widget_18)

        self.pb_save_setting = QPushButton(self.wdg_save_setting)
        self.pb_save_setting.setObjectName(u"pb_save_setting")
        sizePolicy1.setHeightForWidth(self.pb_save_setting.sizePolicy().hasHeightForWidth())
        self.pb_save_setting.setSizePolicy(sizePolicy1)
        self.pb_save_setting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_25.addWidget(self.pb_save_setting)


        self.verticalLayout_20.addWidget(self.wdg_save_setting)

        self.stackedWidget.addWidget(self.page_setting)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.widget_launch = QWidget(self.widget_main)
        self.widget_launch.setObjectName(u"widget_launch")
        sizePolicy21.setHeightForWidth(self.widget_launch.sizePolicy().hasHeightForWidth())
        self.widget_launch.setSizePolicy(sizePolicy21)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_launch)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.lb_reset_all_params = QLabel(self.widget_launch)
        self.lb_reset_all_params.setObjectName(u"lb_reset_all_params")
        sizePolicy1.setHeightForWidth(self.lb_reset_all_params.sizePolicy().hasHeightForWidth())
        self.lb_reset_all_params.setSizePolicy(sizePolicy1)
        self.lb_reset_all_params.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lb_reset_all_params.setScaledContents(True)
        self.lb_reset_all_params.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lb_reset_all_params)

        self.pb_output_command = QPushButton(self.widget_launch)
        self.pb_output_command.setObjectName(u"pb_output_command")
        sizePolicy1.setHeightForWidth(self.pb_output_command.sizePolicy().hasHeightForWidth())
        self.pb_output_command.setSizePolicy(sizePolicy1)
        self.pb_output_command.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.pb_output_command)

        self.pb_open_output_folder = QPushButton(self.widget_launch)
        self.pb_open_output_folder.setObjectName(u"pb_open_output_folder")
        sizePolicy1.setHeightForWidth(self.pb_open_output_folder.sizePolicy().hasHeightForWidth())
        self.pb_open_output_folder.setSizePolicy(sizePolicy1)
        self.pb_open_output_folder.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.pb_open_output_folder)

        self.widget2 = QWidget(self.widget_launch)
        self.widget2.setObjectName(u"widget2")
        sizePolicy3.setHeightForWidth(self.widget2.sizePolicy().hasHeightForWidth())
        self.widget2.setSizePolicy(sizePolicy3)
        self.verticalLayout_19 = QVBoxLayout(self.widget2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.pb_launch = QPushButton(self.widget2)
        self.pb_launch.setObjectName(u"pb_launch")
        sizePolicy1.setHeightForWidth(self.pb_launch.sizePolicy().hasHeightForWidth())
        self.pb_launch.setSizePolicy(sizePolicy1)
        self.pb_launch.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_launch.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.pb_launch)

        self.wdg_progressbar = QWidget(self.widget2)
        self.wdg_progressbar.setObjectName(u"wdg_progressbar")
        sizePolicy1.setHeightForWidth(self.wdg_progressbar.sizePolicy().hasHeightForWidth())
        self.wdg_progressbar.setSizePolicy(sizePolicy1)

        self.verticalLayout_19.addWidget(self.wdg_progressbar)


        self.horizontalLayout_10.addWidget(self.widget2)


        self.verticalLayout.addWidget(self.widget_launch)


        self.horizontalLayout.addWidget(self.widget_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 841, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_exe_icon.setText("")
        self.pb_page_basic.setText("")
        self.pb_page_advance.setText("")
        self.pb_page_ios_win.setText("")
        self.pb_page_info.setText("")
        self.pb_page_command.setText("")
        self.pb_page_console.setText("")
        self.pb_show_tutorial.setText("")
        self.pb_page_setting.setText("")
        self.wdg_current_env_page_base.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.lb_env_current_title_page_base.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u73af\u5883", None))
        self.lb_env_current_name_page_base.setText("")
        self.lb_env_current_path_page_base.setText("")
        self.lb_env_current_check_install_page_base.setText(QCoreApplication.translate("MainWindow", u"pyinstaller\n"
"\u5df2\u5b89\u88c5", None))
        self.wdg_input_py_file_path.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.lb_input_py_file_icon.setText("")
        self.lb_input_py_file_path.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u9700\u8981\u6253\u5305\u7684 python \u811a\u672c\u5165\u53e3\u6587\u4ef6, \u652f\u6301 *.py, *.pyw, *.pyd, *.spec\u6587\u4ef6\u6216 *.ocl, *.txt", None))
        self.pb_input_py_file_browser.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.wdg_output_info.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.lb_output_folder_path_icon.setText("")
        self.lb_output_folder_path.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u6307\u5b9a\u8f93\u51fa\u7684\u6587\u4ef6\u5939", None))
        self.cb_lock_output_folder.setText(QCoreApplication.translate("MainWindow", u"\u9501\u5b9a\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.pb_output_folder_browser.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.lb_output_file_name_icon.setText("")
        self.lb_output_file_name.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u6307\u5b9a\u8f93\u5165\u6587\u4ef6\u540d", None))
        self.cb_lock_output_file_name.setText(QCoreApplication.translate("MainWindow", u"\u9501\u5b9a\u6587\u4ef6\u540d", None))
        self.wdg_option.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.lb_output_exe_icon_icon.setText("")
        self.lb_output_exe_icon.setText(QCoreApplication.translate("MainWindow", u"(\u53ef\u9009) \u8bf7\u6dfb\u52a0\u5e94\u7528\u56fe\u6807", None))
        self.pb_output_exe_icon_browser.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.lb_output_exe_version_icon.setText("")
        self.lb_output_exe_version.setText(QCoreApplication.translate("MainWindow", u"(\u53ef\u9009) \u8bf7\u6dfb\u52a0\u7248\u672c\u4fe1\u606f", None))
        self.lb_output_exe_version_browser.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.pb_output_exe_version_edit.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa/\u7f16\u8f91", None))
        self.wdg_output_form.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.lb_output_form.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5305\u8f93\u51fa\u5f62\u5f0f", None))
        self.rb_output_form_folder.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939", None))
        self.rb_output_form_file.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6(exe)", None))
        self.wdg_exe_console_display.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.lb_exe_console_display.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u7ec8\u7aef\u7a97\u53e3", None))
        self.rb_exe_console_display_show.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a", None))
        self.rb_exe_console_display_hide.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u663e\u793a/\u9690\u85cf", None))
        self.widget_31.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6\u8d44\u6e90", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u4e8c\u8fdb\u5236\u8d44\u6e90", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"\u6536\u96c6\u5b50\u6a21\u5757", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"\u6536\u96c6\u6570\u636e\u6587\u4ef6", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"\u6536\u96c6\u4e8c\u8fdb\u5236\u6587\u4ef6", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"\u6536\u96c6\u6240\u6709\u6a21\u5757\u8d44\u6e90", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u542f\u52a8\u753b\u9762", None))
        self.widget_81.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u6a21\u5757\u5bfc\u5165\u8def\u5f84", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u6a21\u5757\u641c\u5bfb\u8def\u5f84", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"\u6392\u9664\u6a21\u5757", None))
        self.widget.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u5305\u7684\u5143\u6570\u636e", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"\u9012\u5f52\u590d\u5236\u5305\u7684\u5143\u6570\u636e", None))
        self.widget_33.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"\u989d\u5916\u7684\u94a9\u5b50\u8def\u5f84", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u65f6\u7684\u94a9\u5b50", None))
        self.widget_82.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u5de5\u4f5c\u8def\u5f84", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\u6784\u5efa\u65f6\u5de5\u4f5c\u76ee\u5f55", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"SPEC \u6587\u4ef6\u751f\u6210\u8def\u5f84", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"\u7981\u7528 UPX \u538b\u7f29", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"UPX \u538b\u7f29\u5de5\u5177\u8def\u5f84", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"UPX \u6392\u9664\u6587\u4ef6", None))
        self.widget_80.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u7ea7\u522b", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Python \u9009\u9879", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u8bd5\u9009\u9879", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"\u7981\u7528\u7a97\u53e3\u5316\u56de\u6eaf", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"\u5ffd\u7565\u4fe1\u53f7\u5904\u7406", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u786e\u8ba4", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"\u53bb\u9664\u7b26\u53f7\u8868", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"IOS\u7cfb\u7edf", None))
        self.groupBox.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u67b6\u6784", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u4ee3\u7801\u7b7e\u540d", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u552f\u4e00\u6807\u8bc6\u7b26", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a Entitlements \u6587\u4ef6", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528argv\u6a21\u62df", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Windows\u7cfb\u7edf", None))
        self.groupBox_2.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u989d\u5916\u8d44\u6e90", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6e05\u5355\u6587\u4ef6", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u7533\u8bf7\u7ba1\u7406\u5458\u6743\u9650", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u7533\u8bf7 UIAccess \u6743\u9650", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u63a7\u5236\u53f0\u7a97\u53e3", None))
        self.scrollAreaWidgetContents_2.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.wdg_language.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.lb_language.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8bed\u8a00", None))
        self.wdg_build_files_clear.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.lb_build_files_clear.setText(QCoreApplication.translate("MainWindow", u"pyinstaller\u6784\u5efa\u6587\u4ef6", None))
        self.cbb_build_files_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u884c\u6267\u884c\u65b9\u5f0f", None))
        self.rb_use_auto_select.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8", None))
        self.rb_use_pyinstaller.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528pyinstaller.exe", None))
        self.rb_use_python.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528python\u89e3\u91ca\u5668", None))
        self.rb_use_virtual_env.setText(QCoreApplication.translate("MainWindow", u"\u6fc0\u6d3b\u865a\u62df\u73af\u5883", None))
        self.wdg_win_setting.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.lb_tooltip_show.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\u63d0\u793a", None))
        self.cbb_tooltip_show.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a", None))
        self.lb_multi_win.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u6587\u4ef6\u5904\u7406", None))
        self.cbb_multi_win.setText(QCoreApplication.translate("MainWindow", u"\u5141\u8bb8\u591a\u7a97\u53e3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_common), QCoreApplication.translate("MainWindow", u"\u5e38\u89c4", None))
        self.wdg_currnt_env.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.lb_env_current_title_page_setting_env.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u4f7f\u7528\u73af\u5883", None))
        self.lb_env_current_name_page_setting_env.setText("")
        self.lb_env_current_path_title_page_setting_env.setText(QCoreApplication.translate("MainWindow", u"python\u89e3\u91ca\u5668\u8def\u5f84", None))
        self.lb_env_current_path_page_setting_env.setText("")
        self.lb_env_current_check_install_page_setting_env.setText("")
        self.wdg_env_sys.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.rb_env_sys.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u7cfb\u7edf\u9ed8\u8ba4\u73af\u5883", None))
        self.lb_env_sys_name_page_setting_env.setText("")
        self.lb_env_sys_path_page_setting_env.setText("")
        self.pb_env_sys_edit_page_setting_env.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u73af\u5883\u53d8\u91cf", None))
        self.lb_env_sys_check_install_page_setting_env.setText("")
        self.wdg_env_specified.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.rb_env_specified.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u6307\u5b9a\u89e3\u91ca\u5668\u73af\u5883", None))
        self.pb_env_specified_browser_page_setting_env.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.lb_env_specified_hint_info_page_setting_env.setText("")
        self.lb_env_specified_check_install_page_setting_env.setText("")
        self.wdg_env_conda.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.rb_env_conda.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528 Conda \u73af\u5883", None))
        self.lb_env_conda_path_page_setting_env.setText("")
        self.lb_env_conda_check_install_page_setting_env.setText("")
        self.wdg_env_builtin.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.rb_env_builtin.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u5185\u7f6e pyinstaller", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_env), QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u73af\u5883", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u4e3b\u9898", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "")
        self.wdg_save_setting.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_widget", None))
        self.pb_save_setting.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5e76\u7acb\u5373\u751f\u6548", None))
        self.widget_launch.setProperty(u"wdg_group", QCoreApplication.translate("MainWindow", u"area_launch", None))
        self.lb_reset_all_params.setText("")
        self.pb_output_command.setText("")
        self.pb_open_output_folder.setText("")
        self.pb_launch.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
    # retranslateUi

