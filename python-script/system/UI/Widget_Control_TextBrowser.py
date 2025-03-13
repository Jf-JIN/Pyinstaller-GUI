""" 
ControlTextBrowser
当前模块含有一个基于 PySide6.QtWidgets.QTextBrowser 的控件
"""

from PyQt5.QtWidgets import QWidget, QTextBrowser, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap, QTextCursor, QFont, QCursor, QPainter
from PyQt5.QtCore import Qt, QByteArray, QTimer, QSize, pyqtSignal
import traceback
import sys
import threading


_BUTTON_MIN_HEIGHT = 30
_BUTTON_MAX_HEIGHT = 30
_TEXTBROWSER_BORDER_RADIUS = 10
_TEXTBROWSER_BORDER_COLOR = 'rgba(70, 70, 70, 200)'
_TEXTBROWSER_BORDER = 1
_WIDGET_TO_TOP_BOTTOM_BORDER_RADIUS = 10

_SVG_PB_UP = """<svg width="792.55981" height="496.38947" viewBox="0 0 198.13995 124.09737" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs1" /> <g id="layer1" transform="translate(-1.2010884,-33.514282)"> <path id="rect1" style="fill:#878787;fill-opacity:1;stroke:none;stroke-width:3.94445;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-dasharray:none;paint-order:fill markers stroke" d="M 100.27085,33.514283 1.2010884,132.58449 26.227822,157.61165 100.27085,83.568635 l 74.04302,74.043015 25.02717,-25.02716 z" /> </g> </svg>"""

_SVG_PB_DOWN = """<svg width="790.28589" height="494.96527" viewBox="0 0 197.57147 123.74132" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs1" /> <g id="layer1" transform="translate(-1.4853275,-33.692307)"> <path id="rect1" style="fill:#878787;fill-opacity:1;stroke:none;stroke-width:3.93313;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-dasharray:none;paint-order:fill markers stroke" d="M 100.27128,157.43363 199.0568,58.647662 174.10187,33.692305 100.27128,107.52288 26.440694,33.692305 1.4853275,58.647662 Z" /> </g> </svg> """

_SVG_PB_INCREASE = """<svg width="795.29071" height="795.29071" viewBox="0 0 198.82268 198.82268" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs1" /> <g id="layer1" style="stroke:none;stroke-opacity:1" transform="matrix(1.0474909,0,0,1.0474907,-5.9727523,-4.2276727)"> <rect style="fill:#878787;fill-opacity:1;stroke:none;stroke-width:3.71101;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-opacity:1;paint-order:fill markers stroke" id="rect1" width="189.8085" height="39.872971" x="5.701961" y="79.003784" ry="3.7895801" /> <rect style="fill:#878787;fill-opacity:1;stroke:none;stroke-width:3.71101;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-opacity:1;paint-order:fill markers stroke" id="rect2" width="189.80853" height="39.872963" x="4.0360003" y="-120.54269" ry="3.7895794" transform="rotate(90)" /> </g> </svg> """

_SVG_PB_DECREASE = """<svg width="791.80408" height="132.28348" viewBox="0 0 197.95102 33.070869" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs1" /> <g id="layer1" transform="translate(-1.2258914,-82.11689)"> <rect style="fill:#878787;fill-opacity:1;stroke:none;stroke-width:3.86823;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect1" width="197.95102" height="33.070866" x="1.2258914" y="82.11689" /> </g> </svg> """

_SVG_PB_RESET = """<svg width="793.13031" height="785.02356" viewBox="0 0 198.28258 196.25589" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs1" /> <g id="layer1" transform="translate(-0.84551287,-1.711683)"> <path id="path4" style="fill:#878787;fill-opacity:1;stroke:none;stroke-width:4.36124;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-dasharray:none;paint-order:fill markers stroke" d="M 101.00041,1.711683 A 98.128025,98.128025 0 0 0 8.8631788,67.123559 l 22.4725662,-7.86385 7.459867,21.318654 A 65.418684,65.418684 0 0 1 101.00041,34.421284 65.418684,65.418684 0 0 1 166.41906,99.839919 65.418684,65.418684 0 0 1 101.00041,165.25855 65.418684,65.418684 0 0 1 52.410431,142.98206 l 19.981627,-13.73427 0.424828,-2.28134 -60.69086,-11.20558 -11.28051313,60.67621 2.28134313,0.4209 22.064077,-15.16597 A 98.128025,98.128025 0 0 0 101.00041,197.96758 98.128025,98.128025 0 0 0 199.12809,99.839919 98.128025,98.128025 0 0 0 101.00041,1.711683 Z" /> </g> </svg> """

_SVG_PB_CLEAR = """<svg width="780.6073" height="700.7735" viewBox="0 0 206.53567 185.41299" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs1" /> <g id="layer1" transform="translate(-2.9624258,-13.713348)"> <path id="rect2" style="fill:#878787;fill-opacity:0.988235;stroke-width:4.75524;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" d="m 132.31915,13.713348 c -4.48221,0 -8.96428,1.717077 -12.39878,5.151576 L 8.1141774,130.67113 c -6.8690009,6.869 -6.8690019,17.92856 -3e-6,24.79755 l 43.6576666,43.65767 h 4.859157 11.096381 27.325665 13.457386 62.56644 c 2.46434,0 4.44829,-1.98395 4.44828,-4.44828 l 1e-5,-0.93035 c 0,-2.46434 -1.98395,-4.44829 -4.44829,-4.44829 l -52.73951,-1e-5 86.009,-86.00851 c 6.869,-6.868997 6.869,-17.929041 0,-24.79804 L 144.71842,18.864924 c -3.4345,-3.434499 -7.91705,-5.151576 -12.39927,-5.151576 z m -87.629375,95.472242 70.152255,70.15226 -9.96207,9.96158 H 57.900459 l -40.349101,-40.3486 c -3.330215,-3.33022 -3.482117,-8.59087 -0.470823,-12.10636 l -0.02506,-0.025 0.495889,-0.49591 0.08355,-0.0835 3.906683,-3.9062 z" /> <rect style="fill:#878787;fill-opacity:0.988235;stroke-width:4.97176;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect1" width="139.60921" height="12.681196" x="49.303291" y="186.28546" ry="4.5749798" /> </g> </svg>"""

_SVG_PB_TO_TOP = """<svg width="713.82867" height="767.67645" viewBox="0 0 188.86716 203.1144" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs1" /> <g id="layer1" transform="translate(-12.785978,-1.8265682)"> <rect style="fill:#333333;fill-opacity:1;stroke-width:4.11401;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect1" width="188.86716" height="36.896679" x="12.785977" y="168.04428" ry="4.201107" /> <rect style="fill:#333333;fill-opacity:1;stroke-width:4.11401;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect2" width="32.878227" height="137.35793" x="88.040588" y="51.143909" ry="4.201107" /> <path style="fill:#333333;fill-opacity:1;stroke-width:4.11401;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="path2" d="M 81.716488,14.909206 55.892988,59.636822 30.069485,14.909205 4.2459829,-29.818409 l 51.6470031,-2e-6 51.647004,-10e-7 z" transform="rotate(180,80.551656,30.731695)" /> </g> </svg> """

_SVG_PB_TO_BOTTOM = """<svg width="713.82861" height="767.67645" viewBox="0 0 188.86715 203.1144" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs1" /> <g id="layer1" transform="translate(-10.959397,-5.2050861)"> <rect style="fill:#333333;fill-opacity:1;stroke-width:4.11401;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect1" width="188.86716" height="36.896679" x="-199.82655" y="-42.101765" ry="4.201107" transform="scale(-1)" /> <rect style="fill:#333333;fill-opacity:1;stroke-width:4.11401;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect2" width="32.878227" height="137.35793" x="-124.57195" y="-159.00214" ry="4.201107" transform="scale(-1)" /> <path style="fill:#333333;fill-opacity:1;stroke-width:4.11401;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="path2" d="M 81.716488,14.909206 55.892988,59.636822 30.069485,14.909205 4.2459829,-29.818409 l 51.6470031,-2e-6 51.647004,-10e-7 z" transform="translate(51.509222,148.68265)" /> </g> </svg> """


class ControlTextBrowser(QWidget):
    """
    自定义的 QTextBrowser, 其中包含1个 TextBrowser, 8个可以调节 TextBrowser 显示的按钮
    6个固定按钮分别为: 向上, 向下, 增加字号, 减小字号, 重置字号, 清空
    2个非固定按钮: 返回顶端、返回底端, 根据 TextBrowser 的滚动位置自动切换
    滚动到最底端时自动更新显示最新内容, 停留在其他位置时将保持当前视图内容
    同时可以选择按钮栏显示位置, 默认在下方

    参数:
    - font_family(str, 可选): 默认字体, 默认 <'Arial'>.
    - font_size(int, 可选): 默认字号, 默认 <13>.
    - default_font_size(int, 可选): 重置字号, 默认 <13>.
    - font_color(str, 可选): 默认字体颜色, 默认 <'rgb(255, 255, 255)'>.
    - background_color(str, 可选): 背景颜色, 默认 <'rgb(60, 60, 60)'>.
    - button_color(str, 可选): 按钮颜色, 默认 <'#878787'>.
    - button_hover_color(str, 可选): 按钮悬停颜色, 默认 <'#ffffff'>.
    - button_to_top_bottom_background_color(str, 可选): 按钮向上向下按钮的背景颜色, 默认 <'rgba(60, 60, 60, 160)'>.
    - button_to_top_bottom_opacity(int | float, 可选): 按钮向上向下按钮的透明度, 默认 <140>.
    - buttons_position(str, 可选): 按钮位置, 默认<'bottom'>, 可选'bottom', 'top', 'left', 'right'.
    - flag_button_in_textbrowser(bool, 可选): 是否将按钮放在TextBrowser中, 默认 < False > 不放在TextBrowser中.
    - flag_scrollbar_display(bool, 可选): 是否显示滚动条, 默认 < False > 不显示.
    - flag_traceback_display(bool, 可选): 是否显示 traceback, 默认 < False > 不显示.
    - svg_button_up(str, 可选): 向上按钮svg代码.
    - svg_button_down(str, 可选): 向下按钮svg代码.
    - svg_button_increase(str, 可选): 增加字号按钮svg代码.
    - svg_button_decrease(str, 可选): 减小字号按钮svg代码.
    - svg_button_reset(str, 可选): 重置字号按钮svg代码.
    - svg_button_clear(str, 可选): 清空按钮svg代码.
    - svg_button_to_top(str, 可选): 返回顶端按钮svg代码.
    - svg_button_to_bottom(str, 可选): 返回底端按钮svg代码.
    - tooltip_button_up(str, 可选): 按钮向上提示, 默认 <'向上滚动'>.
    - tooltip_button_down(str, 可选): 按钮向下提示, 默认 <'向下滚动'>.
    - tooltip_button_increase(str, 可选): 按钮增加字号提示, 默认 <'增加字号'>.
    - tooltip_button_decrease(str, 可选): 按钮减小字号提示, 默认 <'减小字号'>.
    - tooltip_button_reset(str, 可选): 按钮重置字号提示, 默认 <'重置字号'>.
    - tooltip_button_clear(str, 可选): 按钮清空提示, 默认 <'清空显示'>.
    - tooltip_button_to_top(str, 可选): 按钮返回顶端提示, 默认 <'返回顶部'>.
    - tooltip_button_to_bottom(str, 可选): 按钮返回底端提示, 默认 <'返回底部'>.


    方法:
    - text()-> str: 获取TextBrowser中的文字.
    - set_text(text_on_textbrowser: str)-> None: 设置TextBrowser中的文字.
    - append_text(text_on_textbrowser: str)-> None: 向TextBrowser中添加文字.
    - set_font_size(font_size: int)-> None: 设置TextBrowser中的文字大小.
    - clear() -> None: 清空TextBrowser显示.


    """
    signal_font_size = pyqtSignal(int)

    def text(self) -> str:
        """
        获取文本内容的方法

        Returns:
            str: 返回文本内容
        """
        return self.__text_browser.toPlainText()

    def set_text(self, text_on_textbrowser: str) -> None:
        """
        设置 TextBrowser 中的文字.

        参数:
        - text_on_textbrowser(str):要添加的内容.
        """
        if not isinstance(text_on_textbrowser, str):
            sys.stdout.write(f'\n[Error-ConsoleTextBrowser]-[set_text]\ttext_on_textbrowser 必须为 <str> 类型\t当前为{type(text_on_textbrowser)}\n')
            return None
        self.__text_browser.setPlainText(text_on_textbrowser + "\n")

    def append_text(self, text_on_textbrowser: str) -> None:
        """
        向 TextBrowser 中的末行添加文字.

        参数:
        - text_on_textbrowser(str):要添加的内容.
        """
        try:
            if not isinstance(text_on_textbrowser, str):
                sys.stdout.write('\n[Error-ConsoleTextBrowser]-[append_text]\ttext_on_textbrowser 必须为 <str> 类型\t当前为{type(text_on_textbrowser)}\n')
                return None
            self.__text_list.append(text_on_textbrowser)
            if not self.__timer_text_append.is_alive():
                self.__timer_text_append = threading.Timer(1, self.__append_text_in_textBrowser)
                self.__timer_text_append.start()
        except Exception as e:
            sys.stdout.write(f'\n[Error-ConsoleTextBrowser]-[append_text]\t{traceback.format_exc()}\n')
            raise ValueError(traceback.format_exc())

    def append_html_text(self, text_on_textbrowser: str) -> None:
        """ 添加 HTML 文本 """
        if not isinstance(text_on_textbrowser, str):
            sys.stdout.write('\n[Error-ConsoleTextBrowser]-[append_text]\ttext_on_textbrowser 必须为 <str> 类型\t当前为{type(text_on_textbrowser)}\n')
            return None
        self.__html_list.append(text_on_textbrowser)
        if not self.__timer_html_append.is_alive():
            # self.__timer_html_append.start()
            self.__timer_html_append = threading.Timer(1, self.__append_html_in_textBrowser)
            self.__timer_html_append.start()

    def clear(self) -> None:
        """ 清空 TextBrowser 显示 """
        self.__text_browser.clear()

    def set_font_size(self, font_size: int) -> None:
        """ 设置字体大小 """
        if not isinstance(font_size, int) or font_size <= 0:
            sys.stdout.write('\n[Error-ConsoleTextBrowser]-[set_font_size]\tfont_size 必须为大于0的整数\n')
            return None
        try:
            font = self.__text_browser.font()
            font.setPixelSize(font_size)
            self.__text_browser.setFont(font)
            self.signal_font_size.emit(font_size)
        except Exception as e:
            if self.__flag_traceback_display:
                e = traceback.format_exc()
            self.append_text(e)

    def __init__(self,
                 font_family: str = 'Arial',
                 font_size: int = 13,
                 default_font_size: int = 13,
                 font_color: str = 'rgb(255, 255, 255)',
                 background_color: str = 'rgb(60, 60, 60)',
                 button_color: str = '#878787',
                 button_hover_color: str = '#ffffff',
                 button_to_top_bottom_color: str = None,
                 button_to_top_bottom_background_color: str = 'rgba(60, 60, 60, 160)',
                 button_to_top_bottom_opacity: int | float = 140,
                 buttons_position: str = 'bottom',
                 flag_button_in_textbrowser: bool = False,
                 flag_scrollbar_display: bool = True,
                 flag_traceback_display: bool = False,
                 svg_button_up: str = _SVG_PB_UP,
                 svg_button_down: str = _SVG_PB_DOWN,
                 svg_button_increase: str = _SVG_PB_INCREASE,
                 svg_button_decrease: str = _SVG_PB_DECREASE,
                 svg_button_reset: str = _SVG_PB_RESET,
                 svg_button_clear: str = _SVG_PB_CLEAR,
                 svg_button_to_top: str = _SVG_PB_TO_TOP,
                 svg_button_to_bottom: str = _SVG_PB_TO_BOTTOM,
                 tooltip_button_up: str = "向上滚动",
                 tooltip_button_down: str = "向下滚动",
                 tooltip_button_increase: str = "增加字号",
                 tooltip_button_decrease: str = "减小字号",
                 tooltip_button_reset: str = "重置字号",
                 tooltip_button_clear: str = "清空显示",
                 tooltip_button_to_top: str = "返回顶部",
                 tooltip_button_to_bottom: str = "返回底部") -> None:
        super().__init__()
        list_raise = []
        for i in [(font_family, 'font_family', str),
                  (font_size, 'font_size', int),
                  (default_font_size, 'default_font_size', int),
                  (font_color, 'font_color', str),
                  (background_color, 'background_color', str),
                  (button_color, 'button_color', str),
                  (button_hover_color, 'button_hover_color', str),
                  (button_to_top_bottom_color, 'button_to_top_bottom_color', (str, type(None))),
                  (button_to_top_bottom_background_color, 'button_to_top_bottom_background_color', str),
                  (button_to_top_bottom_opacity, 'button_to_top_bottom_opacity', (int, float)),
                  (buttons_position, 'buttons_position', str),
                  (flag_button_in_textbrowser, 'flag_button_in_textbrowser', bool),
                  (flag_scrollbar_display, 'flag_scrollbar_display', bool),
                  (flag_traceback_display, 'flag_traceback_display', bool),
                  (svg_button_up, 'svg_button_up', str),
                  (svg_button_down, 'svg_button_down', str),
                  (svg_button_increase, 'svg_button_increase', str),
                  (svg_button_decrease, 'svg_button_decrease', str),
                  (svg_button_reset, 'svg_button_reset', str),
                  (svg_button_clear, 'svg_button_clear', str),
                  (svg_button_to_top, 'svg_button_to_top', str),
                  (svg_button_to_bottom, 'svg_button_to_bottom', str),
                  (tooltip_button_up, 'tooltip_button_up', str),
                  (tooltip_button_down, 'tooltip_button_down', str),
                  (tooltip_button_increase, 'tooltip_button_increase', str),
                  (tooltip_button_decrease, 'tooltip_button_decrease', str),
                  (tooltip_button_reset, 'tooltip_button_reset', str),
                  (tooltip_button_clear, 'tooltip_button_clear', str),
                  (tooltip_button_to_top, 'tooltip_button_to_top', str),
                  (tooltip_button_to_bottom, 'tooltip_button_to_bottom', str)]:
            if not isinstance(i[0], i[2]):
                list_raise.append(f'[ConsoleTextBrowser]-[__init__]:\t<{i[1]}>\t必须为: {i[2]}\t当前为: {type(i[0])}\n')
        if list_raise or len(list_raise) > 0:
            raise TypeError('\n'+''.join(list_raise))

        self.__flag_button_in_textbrowser: bool = flag_button_in_textbrowser
        self.__flag_traceback_display: bool = flag_traceback_display
        self.__flag_scrollbar_display: bool = flag_scrollbar_display
        self.__font_size: int = font_size
        self.__default_font_size: int = default_font_size
        self.__font_family: str = font_family
        self.__font_color: str = font_color
        if button_to_top_bottom_color is None:
            self.__button_top_bottom_color: str = button_color
        else:
            self.__button_top_bottom_color: str = button_to_top_bottom_color
        self.__DEFAULT_BACKGROUND_COLOR: str = background_color
        self.__button_color: str = button_color
        self.__button_hover_color: str = button_hover_color
        self.__button_to_top_bottom_background_color: str = button_to_top_bottom_background_color
        self.__button_to_top_bottom_opacity: int | float = button_to_top_bottom_opacity
        self.__buttons_position: str = buttons_position
        self.__svg_pb_up: str = svg_button_up
        self.__svg_pb_down: str = svg_button_down
        self.__svg_pb_increase: str = svg_button_increase
        self.__svg_pb_decrease: str = svg_button_decrease
        self.__svg_pb_reset: str = svg_button_reset
        self.__svg_pb_clear: str = svg_button_clear
        self.__svg_pb_to_top: str = svg_button_to_top
        self.__svg_pb_to_bottom: str = svg_button_to_bottom
        self.__tooltip_pb_up: str = tooltip_button_up
        self.__tooltip_pb_down: str = tooltip_button_down
        self.__tooltip_pb_increase: str = tooltip_button_increase
        self.__tooltip_pb_decrease: str = tooltip_button_decrease
        self.__tooltip_pb_reset: str = tooltip_button_reset
        self.__tooltip_pb_clear: str = tooltip_button_clear
        self.__tooltip_pb_top: str = tooltip_button_to_top
        self.__tooltip_pb_bottom: str = tooltip_button_to_bottom

        self.__init_para()
        self.__init_ui()
        self.__init_signal_connections()
        self.__text_browser.installEventFilter(self)

    def __init_para(self):
        """ 参数初始化 """
        self.__svg_pb_up = self.__change_svg_fill_color(self.__svg_pb_up, self.__button_color)
        self.__svg_pb_down = self.__change_svg_fill_color(self.__svg_pb_down, self.__button_color)
        self.__svg_pb_increase = self.__change_svg_fill_color(self.__svg_pb_increase, self.__button_color)
        self.__svg_pb_decrease = self.__change_svg_fill_color(self.__svg_pb_decrease, self.__button_color)
        self.__svg_pb_reset = self.__change_svg_fill_color(self.__svg_pb_reset, self.__button_color)
        self.__svg_pb_clear = self.__change_svg_fill_color(self.__svg_pb_clear, self.__button_color)
        self.__svg_pb_to_top = self.__change_svg_fill_color(self.__svg_pb_to_top, self.__button_top_bottom_color)
        self.__svg_pb_to_bottom = self.__change_svg_fill_color(self.__svg_pb_to_bottom, self.__button_top_bottom_color)

        self.__timer_up = QTimer(self)
        self.__timer_down = QTimer(self)
        self.__timer_text_append = threading.Timer(1, self.__append_text_in_textBrowser)
        self.__timer_html_append = threading.Timer(1, self.__append_html_in_textBrowser)
        self.__text_list = []
        self.__html_list = []
        self.__scroll_follow_distance = 10

    def __init_ui(self):
        """ UI初始化 """
        self.__widget_init()
        self.__layout_init()

    def __init_signal_connections(self):
        """ 信号连接初始化 """
        self.__timer_up.timeout.connect(self.__scrolling_up)
        self.__timer_down.timeout.connect(self.__scrolling_down)
        self.__pb_up.pressed.connect(self.__start_scrolling_up)
        self.__pb_up.released.connect(self.__stop_scrolling_up)
        self.__pb_down.pressed.connect(self.__start_scrolling_down)
        self.__pb_down.released.connect(self.__stop_scrolling_down)
        self.__pb_reset.clicked.connect(lambda: self.__font_size_resize())
        self.__pb_font_size_increase.clicked.connect(lambda: self.__font_size_increase())  # pyd 中不用 lambda 会报参数错误
        self.__pb_font_size_decrease.clicked.connect(lambda: self.__font_size_decrease())  # pyd 中不用 lambda 会报参数错误
        self.__pb_clear.clicked.connect(self.__text_browser.clear)
        self.__text_browser.verticalScrollBar().valueChanged.connect(self.__show_to_buttons)

    def __widget_init(self):
        """ 控件初始化 """
        self.setMinimumHeight(100)
        self.__widget_main = QWidget(self)
        self.__widget_main.setObjectName('widget_main')
        self.__widget_pbs = QWidget(self.__widget_main)
        self.__text_browser = QTextBrowser(self.__widget_main)
        self.__text_browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if self.__flag_scrollbar_display:
            self.__text_browser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        else:
            self.__text_browser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__pb_up = QPushButton()
        self.__pb_up.setToolTip(self.__tooltip_pb_up)
        self.__pb_up.setIcon(self.__icon_setup(self.__svg_pb_up))
        self.__pb_up.setCursor(QCursor(Qt.PointingHandCursor))
        self.__pushbutton_hover(self.__pb_up, self.__set_pb_hover_icon(self.__svg_pb_up))
        self.__pb_down = QPushButton()
        self.__pb_down.setToolTip(self.__tooltip_pb_down)
        self.__pb_down.setIcon(self.__icon_setup(self.__svg_pb_down))
        self.__pb_down.setCursor(QCursor(Qt.PointingHandCursor))
        self.__pushbutton_hover(self.__pb_down, self.__set_pb_hover_icon(self.__svg_pb_down))
        self.__pb_font_size_increase = QPushButton()
        self.__pb_font_size_increase.setToolTip(self.__tooltip_pb_increase)
        self.__pb_font_size_increase.setIcon(self.__icon_setup(self.__svg_pb_increase))
        self.__pb_font_size_increase.setCursor(QCursor(Qt.PointingHandCursor))
        self.__pushbutton_hover(self.__pb_font_size_increase, self.__set_pb_hover_icon(self.__svg_pb_increase))
        self.__pb_font_size_decrease = QPushButton()
        self.__pb_font_size_decrease.setToolTip(self.__tooltip_pb_decrease)
        self.__pb_font_size_decrease.setIcon(self.__icon_setup(self.__svg_pb_decrease))
        self.__pb_font_size_decrease.setCursor(QCursor(Qt.PointingHandCursor))
        self.__pushbutton_hover(self.__pb_font_size_decrease, self.__set_pb_hover_icon(self.__svg_pb_decrease))
        self.__pb_reset = QPushButton()
        self.__pb_reset.setToolTip(self.__tooltip_pb_reset)
        self.__pb_reset.setIcon(self.__icon_setup(self.__svg_pb_reset))
        self.__pushbutton_hover(self.__pb_reset, self.__set_pb_hover_icon(self.__svg_pb_reset))
        self.__pb_reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.__pb_clear = QPushButton()
        self.__pb_clear.setToolTip(self.__tooltip_pb_clear)
        self.__pb_clear.setIcon(self.__icon_setup(self.__svg_pb_clear))
        self.__pb_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.__pushbutton_hover(self.__pb_clear, self.__set_pb_hover_icon(self.__svg_pb_clear))
        scroll_style = f"""
            QScrollBar:vertical {{
                border: none;
                background:transparent;
                width: 8px;
                margin: 2px 0 2px 0;
                border-radius: 4px;
            }}
            QScrollBar::handle:vertical {{
                background: rgb(255,100,100);
                min-height: 10px;
                border-radius: 4px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: #ff0000;
            }}
            QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {{
                background: transparent;
            }}
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
                background: transparent;
            }}
            """
        if self.__flag_button_in_textbrowser:
            self.__widget_main.setStyleSheet(f"""QWidget{{
                                                        background-color:{self.__DEFAULT_BACKGROUND_COLOR};
                                                        border:{_TEXTBROWSER_BORDER}px solid {_TEXTBROWSER_BORDER_COLOR};
                                                        border-radius: {_TEXTBROWSER_BORDER_RADIUS}px;}}""")
            self.__text_browser.setStyleSheet(f"""QTextBrowser{{
                    border: None;
                    color: {self.__font_color};
                    }}
                """)
        else:
            self.__widget_main.setStyleSheet(
                f"""QWidget{{border: None; background-color: transparent;}}""")
            self.__text_browser.setStyleSheet(F"""QTextBrowser
                    {{
                        background-color:{self.__DEFAULT_BACKGROUND_COLOR};
                        border:{_TEXTBROWSER_BORDER}px solid {_TEXTBROWSER_BORDER_COLOR};
                        border-radius: {_TEXTBROWSER_BORDER_RADIUS}px;
                        color: {self.__font_color};
                        }}
                    """)
        self.__text_browser.verticalScrollBar().setStyleSheet(scroll_style)
        self.__widget_pbs.setStyleSheet(""" border: None; background-color: transparent; """)
        font = QFont()
        font.setFamily(self.__font_family)
        font.setPixelSize(self.__font_size)
        self.__text_browser.setFont(font)
        self.__pb_list: list[QPushButton] = [self.__pb_up, self.__pb_down, self.__pb_font_size_increase, self.__pb_font_size_decrease, self.__pb_reset, self.__pb_clear]
        for pb in self.__pb_list:
            pb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            pb.setMinimumHeight(_BUTTON_MIN_HEIGHT)
            pb.setMaximumHeight(_BUTTON_MAX_HEIGHT)
            pb.setStyleSheet(F"""QPushButton{{
                                    border: None;
                                    background-color: transparent;
                                }}
                                QPushButton:hover{{
                                    padding-bottom: 5px;
                                }}
                            """)
        self.__widget_pb_to = QWidget(self.__text_browser)
        self.__widget_pb_to.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.__widget_pb_to.setStyleSheet(F"""QWidget{{background-color: {self.__button_to_top_bottom_background_color}; border: None; border-radius: {_WIDGET_TO_TOP_BOTTOM_BORDER_RADIUS}px;}}""")
        self.__pb_to_top = QPushButton(self.__text_browser)
        self.__pb_to_top.setIcon(self.__icon_setup_with_opacity(self.__svg_pb_to_top, self.__button_to_top_bottom_opacity))
        self.__pushbutton_hover(self.__pb_to_top, self.__set_pb_hover_icon(self.__svg_pb_to_top))
        self.__pb_to_top.setToolTip(self.__tooltip_pb_top)
        self.__pb_to_top.clicked.connect(self.__up_to_top)
        self.__pb_to_bottom = QPushButton(self.__text_browser)
        self.__pb_to_bottom.setIcon(self.__icon_setup_with_opacity(self.__svg_pb_to_bottom, self.__button_to_top_bottom_opacity))
        self.__pushbutton_hover(self.__pb_to_bottom, self.__set_pb_hover_icon(self.__svg_pb_to_bottom))
        self.__pb_to_bottom.setToolTip(self.__tooltip_pb_bottom)
        self.__pb_to_bottom.clicked.connect(self.__down_to_bottom)
        for i in [self.__pb_to_top, self.__pb_to_bottom]:
            i.setMinimumSize(QSize(_BUTTON_MIN_HEIGHT, _BUTTON_MIN_HEIGHT))
            i.setMaximumSize(QSize(_BUTTON_MAX_HEIGHT, _BUTTON_MAX_HEIGHT))
            i.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            i.setStyleSheet(f"""QPushButton{{background-color: transparent; border:None; border-radius: 0px;}}""")
            i.setCursor(Qt.PointingHandCursor)

    def __layout_init(self):
        """ 布局初始化 """
        if self.__buttons_position in ('left', 'right'):
            layout_pbs = QVBoxLayout(self.__widget_pbs)
        else:
            layout_pbs = QHBoxLayout(self.__widget_pbs)
        layout_pbs.setContentsMargins(0, 0, 0, 0)
        layout_pbs.setSpacing(0)
        layout_pbs.addWidget(self.__pb_up)
        layout_pbs.addWidget(self.__pb_down)
        layout_pbs.addWidget(self.__pb_font_size_increase)
        layout_pbs.addWidget(self.__pb_font_size_decrease)
        layout_pbs.addWidget(self.__pb_reset)
        layout_pbs.addWidget(self.__pb_clear)
        if self.__buttons_position == 'top':
            layout_main_widget = QVBoxLayout(self.__widget_main)
            layout_main_widget.addWidget(self.__widget_pbs, stretch=1)
            layout_main_widget.addWidget(self.__text_browser, stretch=100)
        elif self.__buttons_position == 'left':
            layout_main_widget = QHBoxLayout(self.__widget_main)
            layout_main_widget.addWidget(self.__widget_pbs, stretch=1)
            layout_main_widget.addWidget(self.__text_browser, stretch=100)
        elif self.__buttons_position == 'right':
            layout_main_widget = QHBoxLayout(self.__widget_main)
            layout_main_widget.addWidget(self.__text_browser, stretch=100)
            layout_main_widget.addWidget(self.__widget_pbs, stretch=1)
        else:
            layout_main_widget = QVBoxLayout(self.__widget_main)
            layout_main_widget.addWidget(self.__text_browser, stretch=100)
            layout_main_widget.addWidget(self.__widget_pbs, stretch=1)
        layout_main_widget.setContentsMargins(0, 0, 0, 0)
        layout_main_widget.setSpacing(2)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.__widget_main)
        self.setLayout(layout)
        layout_pb_to = QVBoxLayout(self.__widget_pb_to)
        layout_pb_to.setContentsMargins(0, 0, 0, 0)
        layout_pb_to.setSpacing(0)
        layout_pb_to.addWidget(self.__pb_to_top)
        layout_pb_to.addWidget(self.__pb_to_bottom)

    def resizeEvent(self, event):
        self.__show_to_buttons()
        return super().resizeEvent(event)

    def __append_text_in_textBrowser(self) -> None:
        text_on_textbrowser = '\n'.join(self.__text_list)+'\n'
        self.__text_list = []
        try:
            if self.__text_browser.verticalScrollBar().value() <= self.__text_browser.verticalScrollBar().maximum() - self.__scroll_follow_distance:
                text_cursor: QTextCursor = self.__text_browser.textCursor()
                text_cursor.movePosition(QTextCursor.MoveOperation.End)
                text_cursor.insertText(text_on_textbrowser)
            else:
                self.__text_browser.moveCursor(QTextCursor.MoveOperation.End)
                self.__text_browser.insertPlainText(text_on_textbrowser)
                self.__text_browser.moveCursor(QTextCursor.MoveOperation.End)
                self.__text_browser.verticalScrollBar().setValue(self.__text_browser.verticalScrollBar().maximum())
        except Exception as e:
            if self.__flag_traceback_display:
                e = traceback.format_exc()
            self.__text_browser.moveCursor(QTextCursor.MoveOperation.End)
            self.__text_browser.insertPlainText(str(e) + "\n")
            self.__text_browser.moveCursor(QTextCursor.MoveOperation.End)
            sys.stdout.write(traceback.format_exc())

    def __append_html_in_textBrowser(self) -> None:
        text_on_textbrowser = '\n'.join(self.__html_list)
        self.__html_list = []
        try:
            if self.__text_browser.verticalScrollBar().value() <= self.__text_browser.verticalScrollBar().maximum() - self.__scroll_follow_distance:
                text_cursor: QTextCursor = self.__text_browser.textCursor()
                text_cursor.movePosition(QTextCursor.MoveOperation.End)
                text_cursor.insertHtml(text_on_textbrowser)
            else:
                self.__text_browser.moveCursor(QTextCursor.MoveOperation.End)
                self.__text_browser.insertHtml(text_on_textbrowser)
                self.__text_browser.moveCursor(QTextCursor.MoveOperation.End)
                self.__text_browser.verticalScrollBar().setValue(self.__text_browser.verticalScrollBar().maximum())
        except Exception as e:
            if self.__flag_traceback_display:
                e = traceback.format_exc()
            self.__text_browser.moveCursor(QTextCursor.MoveOperation.End)
            self.__text_browser.insertPlainText(str(e) + "\n")
            self.__text_browser.moveCursor(QTextCursor.MoveOperation.End)
            sys.stdout.write(traceback.format_exc())


    def __set_pb_hover_icon(self, ori_icon: str):
        """
        设置按钮悬停时的颜色更改.

        参数:
        - ori_icon(str):原来的 SVG 图标字符串.

        返回值:
        - 修改颜色后的 SVG 图标字符串.
        """
        return self.__change_svg_fill_color(ori_icon, self.__button_hover_color)

    def __change_svg_fill_color(self, input_svg_str: str, new_fill_color: str) -> str:
        """
        更改 SVG 中的样式颜色.

        参数:
        - input_svg_str(str):输入的 SVG 字符串.
        - new_fill_color(str):新的颜色, RGB 格式, 注意写 '#'.

        返回值:
        - svg_string(str):修改颜色后的 SVG 字符串.
        """

        string_list = input_svg_str.split("style=\"fill:")
        if (len(string_list) > 1):
            for i in range(1, len(string_list)):
                fill_end_index = string_list[i].find("\"")
                if (fill_end_index != -1):
                    string_list[i] = new_fill_color + string_list[i][fill_end_index:]
        return 'style="fill:'.join(string_list)

    def __pushbutton_hover(self, button: QPushButton, hover_icon_svg_str: str):
        """
        按钮悬停样式改变.

        参数:
        - button(QPushButton):要改变悬停样式的按钮.
        - hover_icon_svg_str(str):悬停时的 SVG 图标字符串.
        """
        button_normal_style = button.icon()

        def on_enter(event):
            button.setIcon(self.__icon_setup(hover_icon_svg_str))
            event.accept()

        def on_leave(event):
            button.setIcon(button_normal_style)
            event.accept()
        button.enterEvent = on_enter
        button.leaveEvent = on_leave

    def __icon_setup(self, svg_string: str) -> QIcon:
        """
        设置 QIcon 对象.

        参数:
        - svg_string(str):SVG 图标字符串.

        返回值:
        - QIcon 对象.
        """
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(svg_string.encode()))
        return QIcon(pixmap)

    def __icon_setup_with_opacity(self, svg_string: str, opacity: int = 255) -> QIcon:
        """
        设置带透明背景的 QIcon 对象.

        参数:
        - svg_string(str):SVG 图标字符串.

        返回值:
        - QIcon 对象.
        """
        if opacity > 1 and opacity <= 255:
            opacity = opacity / 255
        elif opacity > 255:
            opacity = 1
        elif opacity < 0:
            opacity = 0
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(svg_string.encode()))
        transparent_pixmap = QPixmap(pixmap.size())
        transparent_pixmap.fill(Qt.transparent)
        painter = QPainter(transparent_pixmap)
        painter.setOpacity(opacity)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        return QIcon(transparent_pixmap)

    def __font_size_increase(self):
        """ 增大字号 """
        try:
            font = self.__text_browser.font()
            size = font.pixelSize() + 1
            font.setPixelSize(size)
            self.__text_browser.setFont(font)
            self.signal_font_size.emit(size)
        except Exception as e:
            if self.__flag_traceback_display:
                e = traceback.format_exc()
            self.append_text(e)

    def __font_size_decrease(self):
        """ 减小字号 """
        try:
            font = self.__text_browser.font()
            size = font.pixelSize() - 1
            font.setPixelSize(size)
            self.__text_browser.setFont(font)
            self.signal_font_size.emit(size)
        except Exception as e:
            if self.__flag_traceback_display:
                e = traceback.format_exc()
            self.append_text(e)

    def __font_size_resize(self):
        """ 重置字号 """
        try:
            font = self.__text_browser.font()
            font.setPixelSize(self.__default_font_size)
            self.__text_browser.setFont(font)
            self.signal_font_size.emit(self.__default_font_size)
        except Exception as e:
            if self.__flag_traceback_display:
                e = traceback.format_exc()
            self.append_text(e)

    def __start_scrolling_up(self):
        """ 向上滚动定时器启动 """
        self.__timer_up.start(50)

    def __stop_scrolling_up(self):
        """ 向上滚动定时器停止 """
        self.__timer_up.stop()

    def __start_scrolling_down(self):
        """ 向下滚动定时器启动 """
        self.__timer_down.start(50)

    def __stop_scrolling_down(self):
        """ 向下滚动定时器停止 """
        self.__timer_down.stop()

    def __scrolling_up(self):
        """ 向上滚动 """
        scrollbar = self.__text_browser.verticalScrollBar()
        value = scrollbar.value()
        scrollbar.setValue(value-2)

    def __scrolling_down(self):
        """ 向下滚动 """
        scrollbar = self.__text_browser.verticalScrollBar()
        value = scrollbar.value()
        scrollbar.setValue(value+2)

    def __show_to_buttons(self):
        """ 显示回到顶/底部的按钮 """
        self.__widget_pb_to.show()
        if self.__text_browser.verticalScrollBar().value() != 0:
            self.__pb_to_top.show()
        else:
            self.__pb_to_top.hide()
        if self.__text_browser.verticalScrollBar().value() != self.__text_browser.verticalScrollBar().maximum():
            self.__pb_to_bottom.show()
        else:
            self.__pb_to_bottom.hide()
        self.__widget_pb_to.adjustSize()
        parent_loc = self.__text_browser.pos()
        if self.__buttons_position == 'top':
            x = parent_loc.x() + self.__text_browser.width() - self.__widget_pb_to.width() - 5
            y = parent_loc.y() + self.__text_browser.height() - self.__widget_pbs.height() - self.__widget_pb_to.height() - 5
        elif self.__buttons_position == 'left':
            x = parent_loc.x() + self.__text_browser.width() - self.__widget_pbs.width() - self.__widget_pb_to.width() - 5
            y = parent_loc.y() + self.__text_browser.height() - self.__widget_pb_to.height() - 5
        elif self.__buttons_position == 'right':
            x = parent_loc.x() + self.__text_browser.width() - self.__widget_pb_to.width() - 5
            y = parent_loc.y() + self.__text_browser.height() - self.__widget_pb_to.height() - 5
        else:
            x = parent_loc.x() + self.__text_browser.width() - self.__widget_pb_to.width() - 5
            y = parent_loc.y() + self.__text_browser.height() - self.__widget_pb_to.height() - 5
        self.__widget_pb_to.move(x, y)

    def __up_to_top(self):
        """ 回到顶部 """
        self.__text_browser.verticalScrollBar().setValue(0)
        self.__show_to_buttons()

    def __down_to_bottom(self):
        """ 回到底部 """
        self.__text_browser.verticalScrollBar().setValue(self.__text_browser.verticalScrollBar().maximum())
        self.__show_to_buttons()


if __name__ == "__main__":

    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import QTimer
    import sys
    app = QApplication(sys.argv)
    # main_window = ControlTextBrowser(background_color='#000088', flag_button_in_textbrowser=False, buttons_position='bottom')
    main_window = ControlTextBrowser(flag_button_in_textbrowser=False)
    main_window.append_text(main_window._ControlTextBrowser__svg_pb_increase)
    main_window.show()
    QTimer.singleShot(1000, lambda: main_window.append_text('123'))
    QTimer.singleShot(5000, lambda: main_window.append_text(main_window._ControlTextBrowser__svg_pb_increase))
    QTimer.singleShot(10000, lambda: main_window.append_text("456"))
    QTimer.singleShot(15000, lambda: main_window.append_text(main_window._ControlTextBrowser__svg_pb_increase))
    QTimer.singleShot(20000, lambda: main_window.append_text("-------------------------------------------------"))
    QTimer.singleShot(25000, lambda: main_window.append_text(main_window._ControlTextBrowser__svg_pb_increase))
    QTimer.singleShot(30000, lambda: main_window.append_text("789"))
    QTimer.singleShot(35000, lambda: main_window.append_text(main_window._ControlTextBrowser__svg_pb_increase))
    QTimer.singleShot(40000, lambda: main_window.append_text("0"))
    sys.exit(app.exec())
