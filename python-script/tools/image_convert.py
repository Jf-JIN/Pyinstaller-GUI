
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QByteArray
import xml.etree.ElementTree as ET
import re
from const.Const_Parameter import *

_log = Log.Tools


def convert_svg_to_pixmap(svg_str: str) -> QPixmap:
    """
        将svg字符串转换为QPixmap

        参数:
        - svg_str(str):svg字符串

        返回:
        - QPixmap:QPixmap对象
        """
    pixmap = QPixmap()
    pixmap.loadFromData(QByteArray(svg_str.encode()))
    return pixmap


def change_svg_color(input_svg_str: str, new_color: str = '', *args) -> str:
    """
    更改 SVG 中的颜色.

    参数:
    - input_svg_str(str):输入的 SVG 字符串.
    - new_color(str):新的颜色, RGB 格式, 注意写 '#'.

    返回值:
    - svg_string(str):修改颜色后的 SVG 字符串.
    """
    root = ET.fromstring(input_svg_str)
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    color_tuple = args
    isChanged = False

    fill_pattern = re.compile(r'fill:\s*#[0-9a-fA-F]+')
    stroke_pattern = re.compile(r'stroke:\s*#[0-9a-fA-F]+')
    for elem in root.iter():
        if 'changeable' in elem.attrib and 'style' in elem.attrib:
            change_part = elem.attrib['changeable'].lower()
            style = elem.attrib['style']
            color = new_color
            if 'cpart' in elem.attrib and len(color_tuple) > 0:
                try:
                    idx = int(elem.attrib['cpart']) - 1
                    if idx < 0 or idx >= len(color_tuple):
                        _log.error(f'cpart of <{elem.tag}> must be in range [1, {len(color_tuple)}] instead of {elem.attrib["cpart"]}')
                    color = color_tuple[idx]
                except ValueError:
                    _log.exception(f'cpart of <{elem.tag}> must be int instead of {elem.attrib["cpart"]}')
            if change_part in ['f', 'fill', 'b', 'both']:
                style = re.sub(fill_pattern, 'fill:' + color, style)
                isChanged = True
            if change_part in ['s', 'stroke', 'b', 'both']:
                style = re.sub(stroke_pattern, 'stroke:' + color, style)
                isChanged = True
            elem.set('style', style)
    if isChanged:
        new_svg_str = ET.tostring(root, encoding='unicode')
    else:
        new_svg_str = input_svg_str
    return new_svg_str


def convert_svg_to_pixmap_with_color(input_svg_str, new_color: str | tuple | None = None) -> QPixmap:
    """将svg字符串转换为QPixmap对象"""
    if isinstance(new_color, str):
        new_color = (new_color, )
    return convert_svg_to_pixmap(change_svg_color(input_svg_str, *new_color))
