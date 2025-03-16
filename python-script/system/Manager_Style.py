
from DToolslib import SingletonMeta, EventSignal
from const.Const_Parameter import *
from system.Manager_Setting import *
import threading
import typing
from PyQt5.QtWidgets import QWidget


_BORDER_STYLE_LIST = ['dashed', 'dot-dash', 'dot-dot-dash', 'dotted', 'double', 'groove', 'inset', 'outset', 'ridge', 'solid', 'none']

_log = Log.StyleManager


class _StyleItem:
    def __init__(self, name: str, target_property, value) -> None:
        self.__value = value
        self.__name: str = name
        self.__target_property: typing.Callable = target_property

    @property
    def name(self) -> str:
        return self.__name

    @property
    def value(self) -> str:
        return self.__value

    @property
    def style(self) -> str:
        if not self.__target_property:
            return ''
        return self.__target_property()

    def set_value(self, value) -> None:
        self.__value = value

    def clear(self) -> None:
        self.__value: str = ''

    def __str__(self) -> str:
        return f'"{self.__name}" : "{self.__value}" -> "{self.__target_property}"'


class WidgetsStyle:
    """
    控件样式单元

    WidgetStyle 对控件进行绑定更新样式, 不更新样式块, 涵盖的样式仅为单个样式

    属性(保护):
        name: 控件名称
        style: 控件样式
    """
    signal_style_update = EventSignal()

    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__style_attr_dict: dict = {}
        self.__register_list: list = []
        self.__update_wait_time: float = App.STYLE_UPDATE_INTERVAL
        self.__timer = threading.Timer(self.__update_wait_time, self.__update)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def style(self) -> str:
        text_list = []
        for key, item in self.__style_attr_dict.items():
            item: _StyleItem
            value = item.style
            if value != '':
                text_list.append(value)
        text: str = ' '.join(text_list) if text_list else ''
        if not text:
            full_text = ''
        elif self.name.startswith('@'):
            full_text = text
        else:
            full_text = f'{self.name} {{ {text} }}' if text else ''
        return full_text

    @property
    def style_info(self) -> str:
        text_list = []
        for key, item in self.__style_attr_dict.items():
            item: _StyleItem
            value = item.style
            if value != '':
                text_list.append(value)
        text: str = ' '.join(text_list) if text_list else ''
        if not text:
            full_text = ''
        elif self.name.startswith('@'):
            full_text = f'{self.name}:\t{{ {text} }}' if text else ''
        else:
            full_text = f'{self.name}:\t{self.name} {{ {text} }}' if text else ''
        return full_text

    def get_dict(self) -> dict:
        temp_dict = {}
        for key, item in self.__style_attr_dict.items():
            item: _StyleItem
            temp_dict[key] = item.value
        return temp_dict

    def register(self, items, doClear: bool = False):
        if doClear:
            self.__register_list.clear()
        if not isinstance(items, list) and not hasattr(items, 'setStyleSheet'):
            _log.warning(f'items {items} is not list or QWidget')
        if not isinstance(items, list):
            items = [items]
        for item in items:
            if item not in self.__register_list:
                self.__register_list.append(item)
        self.__update()

    def __update(self) -> None:
        for item in self.__register_list:
            item: QWidget
            item.setStyleSheet(self.style)
        self.__timer = threading.Timer(self.__update_wait_time, self.__update)  # 防止定时器被销毁

    def __wait_for_update(self) -> None:
        self.signal_style_update.emit()
        if self.__timer.is_alive():
            self.__timer.cancel()
        self.__timer = threading.Timer(self.__update_wait_time, self.__update)
        self.__timer.start()

    def width(self) -> str:
        return self.__prepare_value_num('width', 'width')

    def height(self) -> str:
        return self.__prepare_value_num('height', 'height')

    def max_width(self) -> None:
        return self.__prepare_value_num('max_width', 'max-width')

    def min_width(self) -> None:
        return self.__prepare_value_num('min_width', 'min-width')

    def max_height(self) -> None:
        return self.__prepare_value_num('max_height', 'max-height')

    def min_height(self) -> None:
        return self.__prepare_value_num('min_height', 'min-height')

    def margin(self) -> str:
        return self.__prepare_value_list('margin', 'margin')

    def margin_top(self) -> str:
        return self.__prepare_value_num('margin_top', 'margin-top')

    def margin_bottom(self) -> str:
        return self.__prepare_value_num('margin_bottom', 'margin-bottom')

    def margin_left(self) -> str:
        return self.__prepare_value_num('margin_left', 'margin-left')

    def margin_right(self) -> str:
        return self.__prepare_value_num('margin_right', 'margin-right')

    def padding(self) -> str:
        return self.__prepare_value_list('padding', 'padding')

    def padding_top(self) -> str:
        return self.__prepare_value_num('padding_top', 'padding-top')

    def padding_bottom(self) -> str:
        return self.__prepare_value_num('padding_bottom', 'padding-bottom')

    def padding_left(self) -> str:
        return self.__prepare_value_num('padding_left', 'padding-left')

    def padding_right(self) -> str:
        return self.__prepare_value_num('padding_right', 'padding-right')

    def color(self) -> str:
        return self.__prepare_value_color('color', 'color')

    def font(self) -> str:
        value: str | _StyleItem = self.__style_attr_dict.get('font', '')
        value: str = value.value if isinstance(value, _StyleItem) else value
        if not value or not isinstance(value, (str, list, tuple)):
            return ''
        elif isinstance(value, str):
            return f'font: {value};'
        elif isinstance(value, (list, tuple)):
            temp = []
            for i in value:
                if isinstance(i, int):
                    temp.append(f'{i}px')
                elif isinstance(i, str):
                    if i[0].isdigit():
                        temp.append(i)
                    else:
                        temp.append(f'"{i}"')
            text = ' '.join(temp)
            return f'font: {text};'
        else:
            return ''

    def font_size(self) -> str:
        return self.__prepare_value_num('font_size', 'font-size')

    def font_weight(self) -> str:
        return self.__prepare_value_str('font_weight', 'font-weight')

    def font_family(self) -> str:
        return self.__prepare_value_str('font_family', 'font-family', with_symbol=True)

    def background(self) -> str:
        return self.__prepare_value_str('background', 'background')

    def background_color(self) -> str:
        return self.__prepare_value_color('background_color', 'background-color')

    def background_origin(self) -> str:
        return self.__prepare_value_str('background_origin', 'background-origin')

    def border(self) -> str:
        value = self.__style_attr_dict.get('border', '')
        value: str = value.value if isinstance(value, _StyleItem) else value
        if not value or not isinstance(value, (str, list, tuple)):
            return ''
        elif isinstance(value, str):
            return f'border: {value};'
        elif isinstance(value, (list, tuple)):
            temp = []
            for i in value:
                if isinstance(i, int) and i < 10**2:
                    temp.append(f'{i}px')
                elif isinstance(i, str):
                    if i in _BORDER_STYLE_LIST:
                        temp.append(i)
                    else:
                        temp.append(self.__convert_color(i))
            text = ' '.join(temp)
            return f'border: {text};'
        else:
            return ''

    def border_top_color(self) -> str:
        return self.__prepare_value_color('border_top_color', 'border-top-color')

    def border_bottom_color(self) -> str:
        return self.__prepare_value_color('border_bottom_color', 'border-bottom-color')

    def border_left_color(self) -> str:
        return self.__prepare_value_color('border_left_color', 'border-left-color')

    def border_right_color(self) -> str:
        return self.__prepare_value_color('border_right_color', 'border-right-color')

    def border_color(self) -> str:
        return self.__prepare_value_color('border_color', 'border-color')

    def border_width(self) -> str:
        return self.__prepare_value_num('border_width', 'border-width')

    def border_top_width(self) -> str:
        return self.__prepare_value_num('border_top_width', 'border-top-width')

    def border_bottom_width(self) -> str:
        return self.__prepare_value_num('border_bottom_width', 'border-bottom-width')

    def border_left_width(self) -> str:
        return self.__prepare_value_num('border_left_width', 'border-left-width')

    def border_right_width(self) -> str:
        return self.__prepare_value_num('border_right_width', 'border-right-width')

    def border_style(self) -> str:
        return self.__prepare_value_str('border_style', 'border-style')

    def border_top_style(self) -> str:
        return self.__prepare_value_str('border_top_style', 'border-top-style')

    def border_bottom_style(self) -> str:
        return self.__prepare_value_str('border_bottom_style', 'border-bottom-style')

    def border_left_style(self) -> str:
        return self.__prepare_value_str('border_left_style', 'border-left-style')

    def border_right_style(self) -> str:
        return self.__prepare_value_str('border_right_style', 'border-right-style')

    def border_radius(self) -> str:
        return self.__prepare_value_num('border_radius', 'border-radius')

    def border_radius_top_left(self) -> str:
        return self.__prepare_value_num('border_radius_top_left', 'border-radius-top-left')

    def border_radius_top_right(self) -> str:
        return self.__prepare_value_num('border_radius_top_right', 'border-radius-top-right')

    def border_radius_bottom_left(self) -> str:
        return self.__prepare_value_num('border_radius_bottom_left', 'border-radius-bottom-left')

    def border_radius_bottom_right(self) -> str:
        return self.__prepare_value_num('border_radius_bottom_right', 'border-radius-bottom-right')

    def button_layout(self) -> str:
        return self.__prepare_value_int('button_layout', 'button-layout')

    def gridline_color(self) -> str:
        return self.__prepare_value_color('gridline_color', 'gridline-color')

    def lineedit_password_character(self) -> str:
        return self.__prepare_value_int('lineedit_password_character', 'lineedit-password-character')

    def lineedit_password_mask_delay(self) -> str:
        return self.__prepare_value_int('lineedit_password_mask_delay', 'lineedit-password-mask-delay')

    def message_text_interaction_flags(self) -> str:
        return self.__prepare_value_int('message_text_interaction_flags', 'message-text-interaction-flags')

    def opacity(self) -> str:
        return self.__prepare_value_int('opacity', 'opacity')

    def position(self) -> str:
        return self.__prepare_value_str('position', 'position')

    def selection_background_color(self) -> str:
        return self.__prepare_value_color('selection_background_color', 'selection-background-color')

    def selection_color(self) -> str:
        return self.__prepare_value_color('selection_color', 'selection-color')

    def spacing(self) -> str:
        return self.__prepare_value_int('spacing', 'spacing')

    def subcontrol_origin(self) -> str:
        return self.__prepare_value_str('subcontrol_origin', 'subcontrol-origin')

    def subcontrol_position(self) -> str:
        return self.__prepare_value_str('subcontrol_position', 'subcontrol-position')

    def widget_animation_duration(self) -> str:
        return self.__prepare_value_int('widget_animation_duration', 'widget-animation-duration')

    def text_align(self) -> str:
        return self.__prepare_value_str('text_align', 'text-align')

    def text_decoration(self) -> str:
        return self.__prepare_value_str('text_decoration', 'text-decoration')

    def top(self) -> str:
        return self.__prepare_value_num('top', 'top')

    def bottom(self) -> str:
        return self.__prepare_value_num('bottom', 'bottom')

    def left(self) -> str:
        return self.__prepare_value_num('left', 'left')

    def right(self) -> str:
        return self.__prepare_value_num('right', 'right')

    def set_margin(self, margin: int | str | list | tuple) -> None:
        self.__set_value_list(margin, 'margin', self.margin)

    def set_margin_left(self, margin_left: int | str) -> None:
        self.__set_value_num(margin_left, 'margin_left', self.margin_left)

    def set_margin_right(self, margin_right: int | str) -> None:
        self.__set_value_num(margin_right, 'margin_right', self.margin_right)

    def set_margin_top(self, margin_top: int | str) -> None:
        self.__set_value_num(margin_top, 'margin_top', self.margin_top)

    def set_margin_bottom(self, margin_bottom: int | str) -> None:
        self.__set_value_num(margin_bottom, 'margin_bottom', self.margin_bottom)

    def set_padding(self, padding: int | str | list | tuple) -> None:
        self.__set_value_list(padding, 'padding', self.padding)

    def set_padding_left(self, padding_left: int | str) -> None:
        self.__set_value_num(padding_left, 'padding_left', self.padding_left)

    def set_padding_right(self, padding_right: int | str) -> None:
        self.__set_value_num(padding_right, 'padding_right', self.padding_right)

    def set_padding_top(self, padding_top: int | str) -> None:
        self.__set_value_num(padding_top, 'padding_top', self.padding_top)

    def set_padding_bottom(self, padding_bottom: int | str) -> None:
        self.__set_value_num(padding_bottom, 'padding_bottom', self.padding_bottom)

    def set_width(self, width: int | str) -> None:
        self.__set_value_num(width, 'width', self.width)

    def set_height(self, height: int | str) -> None:
        self.__set_value_num(height, 'height', self.height)

    def set_max_width(self, max_width: int | str) -> None:
        self.__set_value_num(max_width, 'max_width', self.max_width)

    def set_min_width(self, min_width: int | str) -> None:
        self.__set_value_num(min_width, 'min_width', self.min_width)

    def set_max_height(self, max_height: int | str) -> None:
        self.__set_value_num(max_height, 'max_height', self.max_height)

    def set_min_height(self, min_height: int | str) -> None:
        self.__set_value_num(min_height, 'min_height', self.min_height)

    def set_color(self, color: str) -> None:
        self.__set_value_color(color, 'color', self.color)

    def set_font(self, font: str) -> None:
        self.__set_value_str(font, 'font', self.font)

    def set_font_size(self, font_size: int | str) -> None:
        self.__set_value_num(font_size, 'font_size', self.font_size)

    def set_font_weight(self, font_weight: str) -> None:
        self.__set_value_str(font_weight, 'font_weight', self.font_weight)

    def set_font_family(self, font_family: str) -> None:
        self.__set_value_str(font_family, 'font_family', self.font_family)

    def set_background(self, background: str) -> None:
        self.__set_value_str(background, 'background', self.background)

    def set_background_color(self, background_color: str) -> None:
        self.__set_value_color(background_color, 'background_color', self.background_color)

    def set_background_origin(self, background_origin: str) -> None:
        self.__set_value_str(background_origin, 'background_origin', self.background_origin)

    def set_border_top_color(self, border_top_color: str) -> None:
        self.__set_value_color(border_top_color, 'border_top_color', self.border_top_color)

    def set_border_bottom_color(self, border_bottom_color: str) -> None:
        self.__set_value_color(border_bottom_color, 'border_bottom_color', self.border_bottom_color)

    def set_border_left_color(self, border_left_color: str) -> None:
        self.__set_value_color(border_left_color, 'border_left_color', self.border_left_color)

    def set_border_right_color(self, border_right_color: str) -> None:
        self.__set_value_color(border_right_color, 'border_right_color', self.border_right_color)

    def set_border(self, border: str) -> None:
        self.__set_value_str(border, 'border', self.border)

    def set_border_color(self, border_color: str) -> None:
        self.__set_value_color(border_color, 'border_color', self.border_color)

    def set_border_width(self, border_width: int | str) -> None:
        self.__set_value_num(border_width, 'border_width', self.border_width)

    def set_border_top_width(self, border_top_width: int | str) -> None:
        self.__set_value_num(border_top_width, 'border_top_width', self.border_top_width)

    def set_border_bottom_width(self, border_bottom_width: int | str) -> None:
        self.__set_value_num(border_bottom_width, 'border_bottom_width', self.border_bottom_width)

    def set_border_left_width(self, border_left_width: int | str) -> None:
        self.__set_value_num(border_left_width, 'border_left_width', self.border_left_width)

    def set_border_right_width(self, border_right_width: int | str) -> None:
        self.__set_value_num(border_right_width, 'border_right_width', self.border_right_width)

    def set_border_style(self, border_style: str) -> None:
        self.__set_value_str(border_style, 'border_style', self.border_style)

    def set_border_top_style(self, border_top_style: str) -> None:
        self.__set_value_str(border_top_style, 'border_top_style', self.border_top_style)

    def set_border_bottom_style(self, border_bottom_style: str) -> None:
        self.__set_value_str(border_bottom_style, 'border_bottom_style', self.border_bottom_style)

    def set_border_left_style(self, border_left_style: str) -> None:
        self.__set_value_str(border_left_style, 'border_left_style', self.border_left_style)

    def set_border_right_style(self, border_right_style: str) -> None:
        self.__set_value_str(border_right_style, 'border_right_style', self.border_right_style)

    def set_border_radius(self, border_radius: int | str) -> None:
        self.__set_value_num(border_radius, 'border_radius', self.border_radius)

    def set_border_radius_top_left(self, border_radius_top_left: int | str) -> None:
        self.__set_value_num(border_radius_top_left, 'border_radius_top_left', self.border_radius_top_left)

    def set_border_radius_top_right(self, border_radius_top_right: int | str) -> None:
        self.__set_value_num(border_radius_top_right, 'border_radius_top_right', self.border_radius_top_right)

    def set_border_radius_bottom_left(self, border_radius_bottom_left: str) -> None:
        self.__set_value_num(border_radius_bottom_left, 'border_radius_bottom_left', self.border_radius_bottom_left)

    def set_border_radius_bottom_right(self, border_radius_bottom_right: str) -> None:
        self.__set_value_num(border_radius_bottom_right, 'border_radius_bottom_right', self.border_radius_bottom_right)

    def set_button_layout(self, button_layout: int) -> None:
        self.__set_value_int(button_layout, 'button_layout', self.button_layout)

    def set_gridline_color(self, gridline_color: str) -> None:
        self.__set_value_num(gridline_color, 'gridline_color', self.gridline_color)

    def set_lineedit_password_character(self, lineedit_password_character: int) -> None:
        self.__set_value_int(lineedit_password_character, 'lineedit_password_character', self.lineedit_password_character)

    def set_lineedit_password_mask_delay(self, lineedit_password_mask_delay: int) -> None:
        self.__set_value_int(lineedit_password_mask_delay, 'lineedit_password_mask_delay', self.lineedit_password_mask_delay)

    def set_message_text_interaction_flags(self, message_text_interaction_flags: int) -> None:
        self.__set_value_int(message_text_interaction_flags, 'message_text_interaction_flags', self.message_text_interaction_flags)

    def set_opacity(self, opacity: int) -> None:
        self.__set_value_int(opacity, 'opacity', self.opacity)

    # def set_paint_alternating_row_colors_for_empty_area(self, paint_alternating_row_colors_for_empty_area: str) -> None:
    #     self.__set_value_bool(paint_alternating_row_colors_for_empty_area, 'paint_alternating_row_colors_for_empty_area', self.paint_alternating_row_colors_for_empty_area)

    def set_position(self, position: str) -> None:
        self.__set_value_str(position, 'position', self.position)

    def set_selection_background_color(self, selection_background_color: str) -> None:
        self.__set_value_color(selection_background_color, 'selection_background_color', self.selection_background_color)

    def set_selection_color(self, selection_color: str) -> None:
        self.__set_value_color(selection_color, 'selection_color', self.selection_color)

    def set_spacing(self, spacing: str) -> None:
        self.__set_value_int(spacing, 'spacing', self.spacing)

    def set_subcontrol_origin(self, subcontrol_origin: str) -> None:
        self.__set_value_str(subcontrol_origin, 'subcontrol_origin', self.subcontrol_origin)

    def set_subcontrol_position(self, subcontrol_position: str) -> None:
        self.__set_value_str(subcontrol_position, 'subcontrol_position', self.subcontrol_position)

    # def set_titlebar_show_tooltips_on_buttons(self, titlebar_show_tooltips_on_buttons: str) -> None:
    #     self.__set_value_bool(titlebar_show_tooltips_on_buttons, 'titlebar_show_tooltips_on_buttons', self.titlebar_show_tooltips_on_buttons)

    def set_widget_animation_duration(self, widget_animation_duration: str) -> None:
        self.__set_value_int(widget_animation_duration, 'widget_animation_duration', self.widget_animation_duration)

    def set_text_align(self, text_align: str) -> None:
        self.__set_value_str(text_align, 'text_align', self.text_align)

    def set_text_decoration(self, text_decoration: str) -> None:
        self.__set_value_num(text_decoration, 'text_decoration', self.text_decoration)

    def set_top(self, top: str) -> None:
        self.__set_value_num(top, 'top', self.top)

    def set_bottom(self, bottom: str) -> None:
        self.__set_value_num(bottom, 'bottom', self.bottom)

    def set_left(self, left: str) -> None:
        self.__set_value_num(left, 'left', self.left)

    def set_right(self, right: str) -> None:
        self.__set_value_num(right, 'right', self.right)

    def get_value_without_unit(self, value: str) -> int:
        return int(value.replace('px', ''))

    def set_value_from_dict(self, style_dict: dict) -> None:
        if not isinstance(style_dict, dict):
            return
        for key, value in style_dict.items():
            if '-' in key:
                key: str = key.replace('-', '_')
            target_property = ''
            if hasattr(self, key):
                target_property = getattr(self, key)
            self.__style_attr_dict[key] = _StyleItem(name=key, target_property=target_property, value=value)
        self.__wait_for_update()

    def clear(self):
        # for item in self.__style_attr_dict.values():
        #     item: _StyleItem
        #     item.clear()
        self.__style_attr_dict.clear()
        self.__wait_for_update()

    def __check_HEX_color(self, color: str) -> bool:
        try:
            R = color[0:2]
            G = color[2:4]
            B = color[4:6]
            if 0 > int(R, 16) > 255 or 0 > int(G, 16) > 255 or 0 > int(B, 16) > 255:
                # 不是 HEX 格式
                return False
        except:
            # 不是 HEX 格式
            return False
        return True

    def __convert_color(self, color: str) -> str:
        if not color or not isinstance(color, (int, str)):
            return ''
        if isinstance(color, int):
            color = str(color)
        if (len(color) == 6 or len(color) == 8) and color.isalnum():
            result = self.__check_HEX_color(color)
            if not result:
                return color
            color = '#' + color[0:6]
        elif len(color) == 3 and color.isalnum():
            temp_color_str = f"{color[0]*2}{color[1]*2}{color[2]*2}"
            result = self.__check_HEX_color(temp_color_str)
            if not result:
                return color
            color = f'#{temp_color_str}'
        return color

    def __prepare_value_color(self, key, catalog) -> str:
        item: _StyleItem = self.__style_attr_dict.get(key, None)
        if not item:
            return ''
        value = self.__convert_color(item.value)
        return f'{catalog}: {value};'

    def __prepare_value_num(self, key, catalog) -> str:
        item: _StyleItem = self.__style_attr_dict.get(key, None)
        if not item:
            return ''
        value = item.value
        if not value or not isinstance(value, (int, str)):
            return ''
        elif isinstance(value, str):
            return f'{catalog}: {value};'
        elif isinstance(value, int):
            return f'{catalog}: {value}px;'
        else:
            return ''

    def __prepare_value_list(self, key, catalog) -> str:
        item: _StyleItem = self.__style_attr_dict.get(key, None)
        if not item:
            return ''
        value = item.value
        if not value or not isinstance(value, (int, str, list, tuple)):
            return ''
        elif isinstance(value, str):
            return f'{catalog}: {value};'
        elif isinstance(value, int):
            return f'{catalog}: {value}px;'
        elif isinstance(value, (list, tuple)):
            temp = []
            for i in value:
                if isinstance(i, str):
                    temp.append(i)
                elif isinstance(i, int):
                    temp.append(f'{i}px')
            text = ' '.join(temp)
            return f'{catalog}: {text};'
        else:
            return ''

    def __prepare_value_int(self, key, catalog) -> str:
        item: _StyleItem = self.__style_attr_dict.get(key, None)
        if not item:
            return ''
        value = item.value
        if not isinstance(value, int):
            return ''
        else:
            return f'{catalog}: {value};'

    def __prepare_value_bool(self, key, catalog) -> str:
        item: _StyleItem = self.__style_attr_dict.get(key, None)
        if not item:
            return ''
        value = item.value
        if not isinstance(value, bool):
            return ''
        elif value:
            return f'{catalog}: true;'
        else:
            return f'{catalog}: false;'

    def __prepare_value_str(self, key, catalog, with_symbol=False) -> str:
        item: _StyleItem = self.__style_attr_dict.get(key, None)
        if not item:
            return ''
        value = item.value
        if not value:
            return ''
        else:
            if with_symbol:
                return f'{catalog}: "{value}";'
            else:
                return f'{catalog}: {value};'

    def __set_value_num(self, value, name, target_property):
        if not value or not isinstance(value, (int, str)):
            if name in self.__style_attr_dict:
                self.__style_attr_dict[name] = ''
            return
        self.__style_attr_dict[name] = _StyleItem(name=name, target_property=target_property, value=value)
        self.__wait_for_update()

    def __set_value_int(self, value, name,  target_property):
        if not value or not isinstance(value, int):
            if name in self.__style_attr_dict:
                self.__style_attr_dict[name] = ''
            return
        self.__style_attr_dict[name] = _StyleItem(name=name, target_property=target_property, value=value)
        self.__wait_for_update()

    def __set_value_str(self, value, name,  target_property):
        if not isinstance(value, str) or not value:
            if name in self.__style_attr_dict:
                self.__style_attr_dict[name] = ''
            return
        self.__style_attr_dict[name] = _StyleItem(name=name, target_property=target_property, value=value)
        self.__wait_for_update()

    def __set_value_list(self, value, name, target_property):
        if not value or not isinstance(value, (int, str, list, tuple)):
            if name in self.__style_attr_dict:
                self.__style_attr_dict[name] = ''
            return
        self.__style_attr_dict[name] = _StyleItem(name=name, target_property=target_property, value=value)
        self.__wait_for_update()

    def __set_value_color(self, value, name, target_property):
        if not isinstance(value, str) or not value:
            if name in self.__style_attr_dict:
                self.__style_attr_dict[name] = ''
            return
        self.__style_attr_dict[name] = _StyleItem(name=name, target_property=target_property, value=self.__convert_color(value))
        self.__wait_for_update()

    def __set_value_bool(self, value, name,  target_property):
        if not isinstance(value, bool):
            if name in self.__style_attr_dict:
                self.__style_attr_dict[name] = ''
            return
        self.__style_attr_dict[name] = _StyleItem(name=name, target_property=target_property, value=value)
        self.__wait_for_update()

    def __del__(self) -> None:
        if self.__timer.is_alive():
            self.__timer.cancel()
            self.__timer.join()


class StyleBlock:
    """
    先通过 register 注册样式, 随后当样式发生改变时, 将自动更新样式, 无需手动调用 setStyleSheet 方法

    和 WidgetStyle 的区别在于, 这个是对样式块进行处理的, 涵盖的样式更多, 范围更大

    样式块: 
    '~__main__'{
        'QScrollBar::handle:vertical': {background-color: '#5c5c5c', border-radius: '4px', width: '8px'}
        'QPushButton': {background-color: '#5c5c5c', border-radius: '4px', width: '8px'}
        '@Checkbox_in_TB': {background-color: '#5c5c5c', border-radius: '4px', width: '8px'}
    }
    单个样式:
    'QPushButton': {background-color: '#5c5c5c', border-radius: '4px', width: '8px'}
    """
    __memory__ = False
    signal_style_update = EventSignal()

    def __init__(self, name: str):
        self.__dict_objects = {}
        self.__name = name
        self.__register_list = []

    def register(self, items, doClear=False):
        if doClear:
            self.__register_list.clear()
        if not isinstance(items, list) and not hasattr(items, 'setStyleSheet'):
            return
        if not isinstance(items, list):
            items = [items]
        for item in items:
            item: QWidget
            if not hasattr(item, 'setStyleSheet'):
                _log.warning(f'item "{item}" is not QWidget, it does not have setStyleSheet method')
                continue
            if item not in self.__register_list:
                self.__register_list.append(item)
            item.setStyleSheet(self.style)

    def __update(self):
        for item in self.__register_list:
            item: QWidget
            item.setStyleSheet(self.style)
        self.signal_style_update.emit()

    def remove(self, items):
        if not isinstance(items, list) and not callable(items):
            return
        if not isinstance(items, list):
            items = [items]
        for item in items:
            if item in self.__register_list:
                self.__register_list.remove(item)

    def clear_register(self):
        self.__register_list.clear()

    def clear(self):
        for item in self.__dict_objects.values():
            item: WidgetsStyle
            item.clear()

    def load_dict(self, data: dict):
        if not self.__memory__:
            self.clear()
        for key, value in data.items():
            if key not in self.__dict_objects:
                item = WidgetsStyle(key)
                item.set_value_from_dict(value)
                self.__dict_objects[key] = item
            else:
                item: WidgetsStyle = self.__dict_objects[key]
                item.set_value_from_dict(value)
            item.signal_style_update.connect(self.__update)

    def get_dict(self):
        temp = {}
        for item in self.__dict_objects.values():
            item: WidgetsStyle
            temp[item.name] = item.get_dict()
        return temp

    def add(self, item: WidgetsStyle):
        self.__dict_objects[item.name] = item

    def remove(self, item: WidgetsStyle):
        del self.__dict_objects[item.name]

    @property
    def style(self):
        temp = []
        for item in self.__dict_objects.values():
            item: WidgetsStyle
            if item.style and not item.name.startswith('@'):
                temp.append(item.style)
        return '\n'.join(temp)

    @property
    def style_info(self):
        temp = []
        for item in self.__dict_objects.values():
            item: WidgetsStyle
            if item.style:
                temp.append(item.style_info)
        return '\n'.join(temp)

    @property
    def name(self):
        return self.__name

    @property
    def objects_dict(self):
        return self.__dict_objects

    def get_item(self, name) -> WidgetsStyle:
        if name in self.__dict_objects:
            return self.__dict_objects[name]
        else:
            _log.warning(f'"{name}" not found, Please check the style name')
            return WidgetsStyle('@NULL')


class SingleStyleValue:
    signal_style_update = EventSignal()

    def __init__(self, name, value):
        self.__name = name
        self.__value = value
        self.__callback_list = []
        self.__update_wait_time: float = App.STYLE_UPDATE_INTERVAL
        self.__timer = threading.Timer(self.__update_wait_time, self.__update)

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @property
    def style_info(self):
        return f'{self.__name} <{type(self.__value).__name__}>:\t"{self.__value}"'

    def set_value(self, value=None):
        if value is None:
            value = self.__value
        else:
            self.__value = value
        for callback in self.__callback_list:
            callback(value)
        self.__wait_for_update()

    def register(self, callback) -> None:
        if callback not in self.__callback_list:
            self.__callback_list.append(callback)
            self.set_value()

    def unregister(self, callback) -> None:
        if callback in self.__callback_list:
            self.__callback_list.remove(callback)

    def __wait_for_update(self) -> None:
        if self.__timer.is_alive():
            self.__timer.cancel()
        self.__timer = threading.Timer(self.__update_wait_time, self.__update)
        self.__timer.start()

    def __update(self):
        self.signal_style_update.emit()


class StyleManager(metaclass=SingletonMeta):
    """
    样式管理器(单例模式)

    参数:
    - default_style_dict(dict): 默认样式字典
    - applied_style_dict(dict): 应用样式字典

    属性:
    - style: qss样式表
    - objects_dict: 样式对象字典, 键值为样式名称, 值为样式对象

    方法:
    - clear(): 清空数据, 保留结构
    - reset(): 重置为默认数据
    - load_dict(dict): 从字典中加载数据
    - add(WidgetsStyle): 添加样式
    - remove(WidgetsStyle): 移除样式

    样式字典支持 css 写法(-) 和 py 写法(_), 例如: background-color 和 background_color

    颜色支持 ff00ff #ff00ff rgb(255, 0, 255)写法

    尺寸大小支持纯数字和带单位数字, 例如: 10 和 10px, 纯数字单位为px

    多参数支持列表和元组
    - 例如: font: [ 10, 'Arial'] (10px, 'Arial') '10px "Arial"' 注意: font 只能写两个参数, 如果是字符串则字体必须用引号括起来
    - 再例如: margin: [ 10, 20, 30px, 40 ] (10px, 20px, 30, 40px) '10px 20px 30px 40px' [10, 20px] (10px, 20) 注意: 此类选项使用字符串时, 必须带单位

    符号说明: 
    - @: 表示单个样式内容, 内部不可以嵌套字典, 如需嵌套, 则使用 `~`. 获取 style 的时候, 只会有 `{background-color: '#5c5c5c', width: '8px'}` 这样的内容, 而不会带上前面的名字, 在样式块的 style 中, 不会被收集
        - 读取方式: getBlock(<name>).get_item(<style_key>).style
        - 修改方式: getBlock(<name>).get_item(<style_key>).set_xxx
    - ~: 表示样式块
        - 读取方式: getBlock(<name>).style
        - 修改方式: getBlock(<name>).get_item(<style_key>).set_xxx
    - $: 表示单个值, 例如: '#5c5c5c', '8px', True ...
        - 读取方式: getProperty(<name>).value
        - 修改方式: getProperty(<name>).set_value(<value>)
    """
    class __null:
        def __repr__(self):
            return 'StyleManager.__null'
    __null = __null()

    def __init__(self, default_style_dict: dict = {}, applied_style_dict: dict = {}) -> None:
        self.__default_style_dict = default_style_dict
        self.__applied_style_dict = applied_style_dict
        self.__dict_blocks: dict = {}
        self.__dict_properties: dict = {}
        self.__update_wait_time: float = App.STYLE_UPDATE_INTERVAL
        self.__timer = threading.Timer(self.__update_wait_time, self.__update)
        if self.__applied_style_dict:
            _log.info('load applied style dict')
            self.set_theme_dict(self.__applied_style_dict)
        else:
            _log.info('load default style dict')
            self.set_theme_dict(self.__default_style_dict)

    def clear(self):
        for item in self.__dict_blocks.values():
            item: StyleBlock
            item.clear()

    def reset(self):
        self.clear()
        self.set_theme_dict(self.__default_style_dict)

    def __load_dict(self, data: dict):
        StyleBlock.__memory__ = True
        for key, value in data.items():
            key: str
            if key.startswith('$') and not isinstance(value, dict):
                if not key in self.__dict_properties:
                    self.__dict_properties[key] = SingleStyleValue(key, value)
                else:
                    single_item: SingleStyleValue = self.__dict_properties[key]
                    single_item.set_value(value)
                continue
            elif not key.startswith('~') and isinstance(value, dict):
                value = {key: value}
                key = '~__main__'
                if key not in self.__dict_blocks:
                    item = StyleBlock(key)
                    self.__dict_blocks[key] = item
            if key not in self.__dict_blocks:
                item = StyleBlock(key)
            else:
                item: StyleBlock = self.__dict_blocks[key]
            item.load_dict(value)
            item.signal_style_update.connect(self.__wait_for_update)
            self.__dict_blocks[key] = item
        StyleBlock.__memory__ = False

    def export_dict(self) -> dict:
        temp = {}
        for key, block_value in self.__dict_blocks.items():
            block_value: StyleBlock
            temp[key] = block_value.get_dict()
        for key, single_value in self.__dict_properties.items():
            single_value: SingleStyleValue
            temp[key] = single_value.value
        return temp

    def __export_dict_in_setting(self) -> None:
        SM.setConfig('style_sheet', self.export_dict())

    def add(self, item: StyleBlock):
        self.__dict_blocks[item.name] = item

    def remove(self, item: StyleBlock):
        del self.__dict_blocks[item.name]

    @property
    def blocks_dict(self):
        return self.__dict_blocks

    @staticmethod
    def setThemeDict(data: dict):
        """ 
        静态方法

        设置主题字典
        """
        instance = StyleManager()
        instance.set_theme_dict(data)

    @staticmethod
    def getProperty(name: str) -> SingleStyleValue:
        """ 
        静态方法

        获取单个样式属性(以 $ 开头)
        """
        instance = StyleManager()
        return instance.get_property(name)

    @staticmethod
    def getBlock(name: str = __null) -> StyleBlock:
        """ 
        静态方法

        获取样式块(以 ~ 开头), 未填写参数, 则返回默认主样式块 `~__main__`
        """
        instance = StyleManager()
        return instance.get_block(name)

    def set_theme_dict(self, data: dict):
        """
        TODO 注册信息丢失的问题需要考虑
        """
        self.clear()
        self.__load_dict(data)

    def get_property(self, name: str) -> SingleStyleValue:
        return self.__dict_properties.get(name, SingleStyleValue('$NULL', ''))

    def get_block(self, name: str = __null) -> StyleBlock:
        """ 
        获取样式块(以 ~ 开头), 未填写参数, 则返回默认主样式块 `~__main__`
        """
        if name == StyleManager.__null:
            block: StyleBlock = self.__dict_blocks.get('~__main__', StyleBlock('~NULL'))
        elif name in self.__dict_blocks:
            block: StyleBlock = self.__dict_blocks[name]
        else:
            _log.warning(f'"{name}" not found, Please check the style block name')
            block: StyleBlock = StyleBlock('~NULL')
        return block

    def __wait_for_update(self):
        if self.__timer.is_alive():
            self.__timer.cancel()
        self.__timer = threading.Timer(self.__update_wait_time, self.__update)
        self.__timer.start()

    def __update(self):
        self.__export_dict_in_setting()

    @property
    def style_info(self) -> str:
        temp = []
        for key, value in self.__dict_blocks.items():
            value: StyleBlock
            if value.style_info:
                temp.append(f'{key}:\n{value.style_info}\n')
        for key, value in self.__dict_properties.items():
            value: SingleStyleValue
            if value.style_info:
                temp.append(f'{value.style_info}\n')
        return '\n'.join(temp)


STYLE: TypeAlias = StyleManager

if __name__ == '__main__':
    dct = {
        '$Test': 20,
        '~Test': {
            '@CheckBox': {
                'background_color': 'red',
                'border_radius': '5px',
                'color': 'white',
                'font': '10px "Arial"'},
            'QLineEdit': {
                'background_color': 'red',
                'border_radius': '5px',
                'color': 'white',
                'font': '10px "Arial"'
            },
            'QWidget': {'background_color': 'red',
                        'border_radius': '5px',
                        'color': 'white',
                        'font': '10px "Arial"'
                        }
        },
        '@PushButton': {
            'background_color': 'red',
            'border_radius': '5px',
            'color': 'white',
            'font': '10px "Arial"'
        },
        'QLineEdit': {
            'background_color': 'red',
            'border_radius': '5px',
            'color': 'blue',
            'font': '10px "Arial"'
        },
        'QPushButton': {
            'background_color': 9199,
            'border_radius': '50pt',
            'color': '#999',
            'font': '10px "Arial"'
        }
    }
    a = StyleManager()
    a.set_theme_dict(dct)
    # print(a.style_info)
    # print(f'sytle: \n{a.get_block().style}\n')
    # print(a.get_block().style)
    # print(a.style_info)
    # a.get_block().get_item('QLineEdit').set_color('blue')
    # print(a.get_block().style_info)
    # print(StyleManager.getBlock('~Test').style_info)
    # pprint.pprint(a.export_dict())
    # for k, v in a.blockss_dict.items():
    #     v: StyleBlock
    #     print(k, v.get_item('QPushButton').style)
    # m: WidgetsStyle = a.get_item('@PushButton').set_color('blue')
    # m.set_color('blue')
    # print(a.get_item('@PushButton').style)
