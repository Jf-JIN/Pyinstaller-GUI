
from PyQt5.QtCore import Qt, QPropertyAnimation, QTimer, QParallelAnimationGroup, QPoint, QEvent, QObject
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
from subprocess import Popen, CREATE_NO_WINDOW
from os.path import exists


class MessageNotification(QWidget):
    """ 
    无交互消息提示框类

    参数:
    - parent (QWidget): 父窗口, None时为屏幕
    - position (str or tuple): 提示框的位置, 默认为 'center'. 参数可以为:  
        - 'center', 'top', 'left', 'right', 'bottom', 
        - 'top-left', 'top-right', 'bottom-left', 'bottom-right', 
        - (x, y) 的元组表示坐标, 此时为相对父窗口或屏幕的位置. 
    - offset (int): 提示框与父窗口边界的偏移量, 单位为像素(px)
    - flag_move_in (bool): 是否启用提示框进入动画, 默认为 **True**
    - flag_move_out (bool): 是否启用提示框退出动画, 默认为 True
    - hold_duration (int): 提示框显示停留的时间, 单位为毫秒(ms)
    - fade_in_duration (int): 提示框淡入动画持续时间, 单位为毫秒(ms)
    - fade_out_duration (int): 提示框淡出动画持续时间, 单位为毫秒(ms)
    - move_duration (int): 提示框移动动画持续时间, 单位为毫秒(ms)
    - move_in_point (tuple[None|int|str, None|int|str]): 提示框进入动画的起始点, 默认为None, 格式为 (x, y), x和y的值可以为: 
        - None, 表示其值与终点相同, 
        - int, 表示相对父窗口的位置, 
        - str, 表示相对于终点的值, 可以是正数或负数, 正数表示向下或向右, 负数表示向上或向左. 正数时可以省略'+'
    - background_color (str): 提示框背景颜色, 默认为 'rgba(0, 0, 0, 200)', 具体参数与QSS相同
    - padding (int): 提示框内边距, 单位为像素(px), 具体参数与QSS相同
    - border_width (int): 提示框边框宽度, 单位为像素(px), 具体参数与QSS相同
    - border_color (str): 提示框边框颜色, 默认为 'white', 具体参数与QSS相同
    - border_style (str): 提示框边框样式, 默认为 'solid', 具体参数与QSS相同
    - border_radius (int): 提示框边框圆角半径, 单位为像素(px), 具体参数与QSS相同
    - font_color (str): 提示框字体颜色, 默认为 'white', 具体参数与QSS相同
    - font_family (str): 提示框字体族, 默认为 'Arial', 具体参数与QSS相同
    - font_size_px (int): 提示框字体大小, 单位为像素(px), 具体参数与QSS相同
    - font_weight (str): 提示框字体粗细, 默认为 'normal', 具体参数与QSS相同
    - font_italic (bool): 提示框字体是否斜体, 默认为 False

    属性(保护):
    - style: 获取样式表

    方法:
    - notification(message): 显示提示框并开始淡入动画
    - set_style(background_color=None, padding=None,
                border_width=None, border_style=None, border_color=None, border_radius=None, font_color=None, font_family=None, font_size_px=None, font_weight=None, font_italic=None): 设置样式属性并更新样式表
    """

    def notification(self, *message: str | tuple, open_file_path: str = None) -> None:
        """
        显示提示框并开始淡入动画

        参数:
            - *message (str): 要显示的提示信息
            - open_file_path (str): 点击提示框时打开的文件路径, 默认为 None
        """
        if not message:
            return
        text_list = []
        for i in message:
            try:
                text_list.append(str(i))
            except:
                print('参数 message 必须为字符串')
                return
        text_str = ' '.join(text_list)
        if open_file_path:
            self.__label.setCursor(Qt.PointingHandCursor)
            self.__label.mousePressEvent = lambda event: self.__open_excel_folder(open_file_path) if event.button() == Qt.LeftButton else None
            path_format = open_file_path.replace('\\', '  /  ')
            self.__label.setText(f"{text_str}: <b><u>{path_format}</u></b>")
        else:
            self.__label.setCursor(Qt.ArrowCursor)
            self.__label.mousePressEvent = None
            self.__label.setText(text_str)
        self.__set_position()  # 设置提示框位置
        self.show()
        self.__animation_group_in.start()
        self.__timer.start()  # 启动计时器

    def set_style(self, background_color: str = None, padding: int = None,
                  border_width: int = None, border_style: str = None, border_color: str = None, border_radius: int = None,
                  font_color: str = None, font_family: str = None, font_size_px: int = None, font_weight: str | int = None, font_italic: bool = None):
        """
        设置样式属性并更新样式表

        参数:
        - background_color (str, optional): 背景颜色, 默认为None, 维持原样式
        - padding (int, optional): 内边距, 默认为None, 维持原样式
        - border_width (int, optional): 边框宽度, 默认为None, 维持原样式
        - border_style (str, optional): 边框样式, 默认为None, 维持原样式
        - border_color (str, optional): 边框颜色, 默认为None, 维持原样式
        - border_radius (int, optional): 边框圆角半径, 默认为None, 维持原样式
        - font_color (str, optional): 字体颜色, 默认为None, 维持原样式
        - font_family (str, optional): 字体族, 默认为None, 维持原样式
        - font_size_px (int, optional): 字体大小(像素(px)), 默认为None, 维持原样式
        - font_weight (str | int, optional): 字体粗细, 默认为None, 维持原样式
        - font_italic (bool, optional): 是否斜体, 默认为None, 维持原样式
        """
        def check_type(param, param_type, param_name):
            if param is not None and not isinstance(param, param_type):
                print(f'{param_name} 必须为 {param_type.__name__} 或 None')
                return False
            return True

        if not (check_type(background_color, str, 'background_color') and
                check_type(padding, int, 'padding') and
                check_type(border_width, int, 'border_width') and
                check_type(border_style, str, 'border_style') and
                check_type(border_color, str, 'border_color') and
                check_type(border_radius, int, 'border_radius') and
                check_type(font_color, str, 'font_color') and
                check_type(font_family, str, 'font_family') and
                check_type(font_size_px, int, 'font_size_px') and
                check_type(font_weight, (str, int), 'font_weight') and
                check_type(font_italic, bool, 'font_italic')):
            return
        self.__set_style_sheet(background_color=background_color, padding=padding,
                               border_width=border_width, border_style=border_style, border_color=border_color, border_radius=border_radius,
                               font_color=font_color, font_family=font_family, font_size_px=font_size_px, font_weight=font_weight, font_italic=font_italic)
        self.__label.setStyleSheet(self.__style_sheet)

    @property
    def style(self):
        """ 获取样式表 """
        return self.__style_sheet

    def __init__(self, parent, position: str = 'center', offset: int = 20, flag_move_in: bool = True, flag_move_out: bool = True,
                 hold_duration: int = 2000, fade_in_duration: int = 1000, fade_out_duration: int = 500,
                 move_duration: int = 500, move_in_point: tuple[str | int | None, str | int | None] = None,
                 background_color: str = 'rgba(0, 0, 0, 200)', padding: int = 10,
                 border_width: int = 1, border_style: str = 'solid', border_color: str = '#000000', border_radius: int = 5,
                 font_color: str = 'white', font_family: str = 'Arial', font_size_px: int = 12, font_weight: str | int = 'normal', font_italic: bool = False) -> None:
        super().__init__(parent)
        # 设置样式
        self.__set_style_sheet(background_color=background_color, padding=padding,
                               border_width=border_width, border_style=border_style, border_color=border_color, border_radius=border_radius,
                               font_color=font_color, font_family=font_family, font_size_px=font_size_px, font_weight=font_weight, font_italic=font_italic)

        # 位置参数
        self.__position: str | tuple = position
        self.__flag_move_in: bool = flag_move_in
        self.__flag_move_out: bool = flag_move_out
        # 显示停留持续时间
        self.__hold_duration: int = hold_duration
        # 淡入持续时间
        self.__fade_in_duration: int = fade_in_duration
        # 淡出持续时间
        self.__fade_out_duration: int = fade_out_duration
        # 边界偏移量
        self.__offset: int = offset
        # 移动持续时间
        self.__move_duration: int = move_duration
        # 进入起始点
        self.__move_in_point: tuple[str | int | None, str | int | None] = move_in_point
        self.__parameter_init()
        self.__ui_init()

    def __parameter_init(self) -> None:
        self.__timer_init(self.__hold_duration)
        self.__display_pos = None
        self.__background_color: str
        self.__padding: int
        self.__font_color: str
        self.__font_family: str
        self.__font_size_px: int
        self.__font_weight: str | int
        self.__font_italic: bool
        self.__border_width: int
        self.__border_style: str
        self.__border_color: str
        self.__border_radius: int
        self.__animation_group_in = QParallelAnimationGroup(self)
        self.__animation_group_out = QParallelAnimationGroup(self)
        self.__animation_move_in = QPropertyAnimation(self, b"pos")
        self.__animation_move_out = QPropertyAnimation(self, b"pos")
        self.__fade_out = QPropertyAnimation(self, b"windowOpacity")
        self.__fade_in = QPropertyAnimation(self, b"windowOpacity")
        self.__fade_in_action(self.__fade_in_duration)
        self.__fade_out_action(self.__fade_out_duration)
        self.parent().installEventFilter(self)

    def __ui_init(self) -> None:
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0)  # 透明度
        self.__label = QLabel('', self)
        self.__label.setStyleSheet(self.__style_sheet)
        self.__label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(self)
        layout.addWidget(self.__label)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        if source == self.parent():
            if event.type() == QEvent.WindowStateChange:
                if self.parent().windowState() & Qt.WindowMinimized:
                    self.hide()
                else:
                    if self.__label.text() != "":
                        self.show()
            elif event.type() == QEvent.Move or event.type() == QEvent.Resize:
                self.__set_position()
                self.__adjust_animation_targets()
        return super().eventFilter(source, event)

    def __set_style_sheet(self, background_color=None, padding=None,
                          border_width=None, border_style=None, border_color=None, border_radius=None,
                          font_color=None, font_family=None, font_size_px=None, font_weight=None, font_italic=None) -> None:
        """
        设置样式表. 

        参数: 
        - background_color(str, 可选): 背景颜色. 
        - padding(int, 可选): 内边距. 
        - border_width(int, 可选): 边框宽度. 
        - border_style(str, 可选): 边框样式. 
        - border_color(str, 可选): 边框颜色. 
        - border_radius(int, 可选): 边框圆角半径. 
        - font_color(str, 可选): 字体颜色. 
        - font_family(str, 可选): 字体族. 
        - font_size_px(int, 可选): 字体大小(像素(px)). 
        - font_weight(str, 可选): 字体粗细. 
        - font_italic(bool, 可选): 是否使用斜体字体. 
        """
        style_properties = {
            '__background_color': background_color,
            '__padding': padding,
            '__border_width': border_width,
            '__border_style': border_style,
            '__border_color': border_color,
            '__border_radius': border_radius,
            '__font_color': font_color,
            '__font_family': font_family,
            '__font_size_px': font_size_px,
            '__font_weight': font_weight,
            '__font_italic': font_italic}
        # 只有非空值, 才进行赋值操作, 其他保留原值
        for key, value in style_properties.items():
            if value is not None:
                setattr(self, f'_{self.__class__.__name__}{key}', value)

        self.__style_sheet = f"""QLabel {{
            background-color: {self.__background_color};
            padding: {self.__padding}px;
            border: {self.__border_width}px {self.__border_style} {self.__border_color};
            border-radius: {self.__border_radius}px;
            color: {self.__font_color};
            font-family: {self.__font_family};
            font-size: {self.__font_size_px}px;
            font-weight: {self.__font_weight};
            font-style: {'italic' if self.__font_italic else 'normal'};
        }}
        """

    def __fade_in_action(self, fade_in_duration_ms: int) -> None:
        """
        创建淡入动画

        参数:
        - fade_in_duration_ms(int): 淡入动画的持续时间, 单位为毫秒(ms)
        """
        self.__fade_in.setDuration(fade_in_duration_ms)  # 淡入时间 1 秒
        self.__fade_in.setStartValue(0.0)
        self.__fade_in.setEndValue(1.0)
        self.__animation_group_in.addAnimation(self.__fade_in)

    def __fade_out_action(self, fade_out_duration_ms) -> None:
        """
        创建淡出动画

        参数:
        - fade_out_duration_ms(int): 淡出动画的持续时间, 单位为毫秒(ms)
        """
        self.__fade_out.setDuration(fade_out_duration_ms)  # 淡出时间 1 秒
        self.__fade_out.setStartValue(1.0)
        self.__fade_out.setEndValue(0.0)
        self.__animation_group_out.addAnimation(self.__fade_out)

    def __move_action(self, animation: QPropertyAnimation, start_pos: tuple | QPoint, end_pos: tuple | QPoint, duration_ms: int) -> None:
        """
        创建移动动画

        参数:
        - animation(QPropertyAnimation): QPropertyAnimation 对象, 用于执行移动动画
        - start_pos(tuple or QPoint): 移动动画的起始位置, 可以是一个包含 x 和 y 坐标的元组或 QPoint 对象
        - end_pos(tuple or QPoint): 移动动画的结束位置, 可以是一个包含 x 和 y 坐标的元组或 QPoint 对象
        - duration_ms(int): 动画的持续时间, 单位为毫秒(ms)
        """
        if not all(start_pos) or not all(end_pos):
            return
        if not isinstance(start_pos, (tuple, QPoint)):
            print(f'start_pos 类型应为 tuple 或 QPoint, 当前为: {type(start_pos)}')
            return
        if not isinstance(end_pos, (tuple, QPoint)):
            print(f'end_pos 类型应为 tuple 或 QPoint, 当前为: {type(end_pos)}')
            return
        start_pos = QPoint(*start_pos) if isinstance(start_pos, tuple) else start_pos
        end_pos = QPoint(*end_pos) if isinstance(end_pos, tuple) else end_pos
        animation.setDuration(duration_ms)
        animation.setStartValue(start_pos)
        animation.setEndValue(end_pos)

    def __move_in_action(self) -> None:
        """创建移入动画"""
        if not self.__display_pos or not self.__move_in_point:
            return
        x, y = self.__move_in_point
        start_x = self.__derive_start_value(x, self.__display_pos[0])
        start_y = self.__derive_start_value(y, self.__display_pos[1])
        start_pos = (start_x, start_y)
        self.__move_action(self.__animation_move_in, start_pos, self.__display_pos, self.__move_duration)
        self.__animation_group_in.addAnimation(self.__animation_move_in)

    def __move_out_action(self) -> None:
        """创建移出动画"""
        if not self.__display_pos or not self.__move_in_point:
            return
        x, y = self.__move_in_point
        start_x = self.__derive_start_value(x, self.__display_pos[0])
        start_y = self.__derive_start_value(y, self.__display_pos[1])
        start_pos = (start_x, start_y)
        self.__move_action(self.__animation_move_out, self.__display_pos, start_pos, self.__move_duration)
        self.__animation_group_out.addAnimation(self.__animation_move_out)

    def __timer_init(self, duration: int) -> None:
        """
        计时器初始化

        参数:
        - duration(int): 计时器的间隔时间, 单位为毫秒(ms)
        """
        self.__timer = QTimer(self)
        self.__timer.setInterval(duration)  # 显示的持续时间
        self.__timer.timeout.connect(self.__start_fade_out)

    def __start_fade_out(self) -> None:
        """开始淡出动画"""
        self.__animation_group_out.start()
        self.__animation_group_out.finished.connect(self.close)

    def __set_position(self):
        """ 设置窗口位置 """
        if self.__position == 'left' or self.__position == 'right':
            self.__label.setText(self.__convert_text_to_vertical(self.__label.text()))
        self.adjustSize()
        if self.parent():  # 确保有父窗口
            parent_geometry = self.parent().geometry()
            parent_x = parent_geometry.x()
            parent_y = parent_geometry.y()
            parent_width = parent_geometry.width()
            parent_height = parent_geometry.height()
            middle_horizontal = parent_x + (parent_width - self.width()) // 2
            middle_vertical = parent_y + (parent_height - self.height()) // 2
            side_left = parent_x + self.__offset
            side_right = parent_x + parent_width - self.width() - self.__offset
            side_top = parent_y + self.__offset
            side_bottom = parent_y + parent_height - self.height() - self.__offset
            dict_position_options = {
                'center': (middle_horizontal, middle_vertical),
                'top': (middle_horizontal, side_top),
                'left': (side_left, middle_vertical),
                'right': (side_right, middle_vertical),
                'bottom': (middle_horizontal, side_bottom),
                'top-left': (side_left, side_top),
                'top-right': (side_right, side_top),
                'bottom-left': (side_left, side_bottom),
                'bottom-right': (side_right, side_bottom),
            }
            if isinstance(self.__position, str):
                x, y = dict_position_options[self.__position]
            elif isinstance(self.__position, tuple):
                x = self.__position[0] + parent_x
                y = self.__position[1] + parent_y
            else:
                return
            self.move(x, y)
            self.__display_pos = (x, y)
            if self.__flag_move_in:
                self.__move_in_action()
            if self.__flag_move_out:
                self.__move_out_action()

    def __adjust_animation_targets(self):
        """动态调整动画目标位置"""
        if self.__flag_move_in and self.__animation_move_in.state() == QPropertyAnimation.Running:
            self.__animation_move_in.setEndValue(QPoint(*self.__display_pos))
        if self.__flag_move_out and self.__animation_move_out.state() == QPropertyAnimation.Running:
            self.__animation_move_out.setStartValue(QPoint(*self.__display_pos))

    def __convert_text_to_vertical(self, text: str) -> str:
        """
        将字符串中的每个字符拆分为竖向显示

        参数:
        - text(str): 需要转换的字符串

        返回值:
        - 转换后的字符串, 每个字符之间用换行符分隔
        """
        return "\n".join(text)  # 在每个字符之间添加换行符

    def __derive_int_from_str(self, string: str) -> None | int:
        """
        从字符串中提取整数值

        参数:
        - string(str): 需要提取整数的字符串

        返回值:
        - 提取到的整数值, 如果无法提取则返回None
        """
        sign = '+'
        if string.startswith('-'):
            string = string[1:]
            sign = '-'
        elif string.startswith('+'):
            string = string[1:]
        temp = ''
        for i in string:
            if not i.isdigit():
                break
            temp += i
        if temp == '':
            return None
        return int(sign+temp)

    def __derive_start_value(self, value: str | int | None, base: int) -> int:
        """
        根据给定的起始值和基准值, 计算起始值

        参数:
        - value(str | int | None): 起始值, 可以是字符串、整数或None
        - base(int): 基准值, 用于计算起始值的参考值

        返回值:
        - 计算得到的起始值, 如果无法计算则返回基准值
        """
        if isinstance(value, str):
            value = self.__derive_int_from_str(value)
            if value is not None and value < 0:
                start_value = base - value
            elif value is not None and value >= 0:
                start_value = base + value
        elif isinstance(value, int):
            start_value = value
        else:
            start_value = base
        return start_value

    def __open_excel_folder(self, file_path: str):
        if not file_path or not exists(file_path):
            return
        Popen(['explorer', '/select,', file_path], creationflags=CREATE_NO_WINDOW)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import sys

    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setGeometry(100, 100, 600, 400)
    window.show()

    notification = MessageNotification(window, position='bottom', move_in_point=(None, '+20'))

    messages = ['测试测试测试测试测试测试', 'testtesttesttesttesttest', 'テストテストテストテスト', 'PrüfenPrüfenPrüfenPrüfen']
    print(notification.style)
    for i, message in enumerate(messages):
        QTimer.singleShot(i * 5000, lambda msg=message: notification .notification(msg))  # 每隔3秒显示一个消息00
    sys.exit(app.exec_())
