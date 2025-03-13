
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSpinBox, QSizePolicy, QLabel
from PyQt5.QtCore import pyqtSignal, Qt
from const.Const_Parameter import *
from system.Manager_Style import *
_log: Logger = Log.UI


class VersionWidget(QWidget):
    """ 
    此类是编辑版本号的控件, 用于 DialogVersionEditor, 主要是用在FFI中的文件版本和产品版本的编辑和显示

    该控件包含4个SpinBox, 用于编辑和显示版本号, 分别是主版本号、次版本号、修订号和构建号

    参数:
    - parent (QWidget): 父控件
    - data (list): 版本号数据, 默认为None, 表示使用默认值[0, 0, 0, 0]

    信号:
    - valueChanged (pyqtSignal(list)): 当版本号发生变化时发出信号, 参数为新的版本号列表

    方法: 
    - setValue(value: list) -> None: 设置版本号数据, 参数为新的版本号列表
    """
    valueChanged = pyqtSignal(list)

    def __init__(self, parent=None, data=None) -> None:
        super().__init__(parent)
        self.__data = data if data else [0, 0, 0, 0]
        self.__init_ui()

    def __init_ui(self) -> None:
        layout: QHBoxLayout = QHBoxLayout(self)
        self.__spinbox_list: list = []
        len_data: int = len(self.__data)
        for idx in range(4):
            spinbox: QSpinBox = QSpinBox(self)
            spinbox.setRange(0, 65536)
            # spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
            spinbox.wheelEvent = lambda event: None
            spinbox.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            if idx < len_data:
                spinbox.setValue(self.__data[idx])
            spinbox.valueChanged.connect(self.__value_changed)
            if idx != 0:
                label: QLabel = QLabel('.', self)
                label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setStyleSheet(STYLE.getBlock().get_item('@version_seperator').style)
                layout.addWidget(label)
            layout.addWidget(spinbox)
            self.__spinbox_list.append(spinbox)
        layout.setContentsMargins(5, 2, 5, 2)
        layout.setSpacing(0)
        self.setStyleSheet(STYLE.getBlock().style)

    def __value_changed(self) -> None:
        self.__data: list = [spinbox.value() for spinbox in self.__spinbox_list]
        self.valueChanged.emit(self.__data)

    def setValue(self, value: list) -> None:
        """ 
        设置版本号数据, 参数设置将从主版本号开始, 如果列表长度小于4时, 将不会填写, 如果列表长度大于4时, 将不会读取后续数据

        参数: 
        - value (list): 新的版本号列表, 列表内应为4个整数, 分别为主版本号、次版本号、修订号和构建号
        """
        len_list: int = len(value)
        for idx, spinbox in enumerate(self.__spinbox_list):
            spinbox: QSpinBox
            if idx >= len_list:
                break
            spinbox.setValue(value[idx])
