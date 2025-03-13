from DToolslib import *


class _DS(StaticEnum):  # Default Style
    class Dark(StaticEnum):
        BLACK = '#191919'
        BLUE = '#2D4263'
        ORANGE = '#C84B31'
        WHITE = '#ECDBBA'
        GREEN = '8FD14F'
        RED = 'FF4C4C'
        HOVER_TEXT = '#000000'
        HOVER_BACKGROUND = '#2C74B3'
        TEXT = WHITE
        BACKGROUND = BLACK
        WIDGET_BG = BLUE
        SELECTED = ORANGE
        SELECTED_ATTENTION = WHITE
        MENU = ORANGE
        HEADER_TEXT = BLACK
        HEADER_BG = WHITE
        INSTALLED_TEXT = BLUE
        INSTALLED_BG = GREEN
        UNINSTALLED_TEXT = TEXT
        UNINSTALLED_BG = RED

    class Light(StaticEnum):
        BLACK = '#191919'
        BLUE = '#78B3CE'
        LIGHT_BLUE = '#C9E6F0'
        ORANGE = '#F96E2A'
        WHITE = '#FBF8EF'
        GREEN = '8FD14F'
        RED = 'FF4C4C'
        HOVER_TEXT = '#000000'
        HOVER_BACKGROUND = '#2C74B3'
        TEXT = BLACK
        BACKGROUND = WHITE
        WIDGET_BG = LIGHT_BLUE
        SELECTED = BLUE
        SELECTED_ATTENTION = ORANGE
        MENU = LIGHT_BLUE
        HEADER_TEXT = BLACK
        HEADER_BG = LIGHT_BLUE
        INSTALLED_TEXT = BLACK
        INSTALLED_BG = GREEN
        UNINSTALLED_TEXT = WHITE
        UNINSTALLED_BG = RED

    FONT_SIZE = 14
    FONT_FAMILY = 'Arial'
    BTN_SQUARE_SIZE = 36
    BTN_ICON_PADDING = 5
    BTN_SQUARE_ICON_SIZE = BTN_SQUARE_SIZE - BTN_ICON_PADDING * 2


class SheetStyle(StaticEnum):
    # 样式
    DARK = {
        '#centralwidget, #tabWidget::pane, QTabBar::tab ,QTabWidget > QWidget, QGroupBox, QProgressBar, QDialog': {
            'color': _DS.Dark.TEXT,
            'background_color': _DS.Dark.BACKGROUND,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
        },
        'QPushButton': {
            'color': _DS.Dark.TEXT,
            'background_color': _DS.Dark.WIDGET_BG,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'min_width': '30px',
            'max_height': '50px',
            'border': 'none',
            'border_radius': '10px',
            'padding': [2, 2],
        },
        'QPushButton:hover': {
            'padding_bottom': '2px',
            'color': _DS.Dark.HOVER_TEXT,
            'background_color': _DS.Dark.HOVER_BACKGROUND
        },
        'QPushButton[widgetType="versionEditor"]': {
            'margin': 2,
            'border_width': 1,
            'border_style': 'solid',
            'border_color': _DS.Dark.ORANGE,
            'border_radius': '0px',
        },
        'QPushButton[widgetType="Dialog"]': {
            'min_width': '80px',
            'max_height': '35px',
        },
        'QPushButton[widgetType="square"]': {
            'min_width': _DS.BTN_SQUARE_SIZE,
            'max_width': _DS.BTN_SQUARE_SIZE,
            'min_height': _DS.BTN_SQUARE_SIZE,
            'max_height': _DS.BTN_SQUARE_SIZE,
            'padding': [0, 0],
            'margin': 0,
            'border_radius': 15,
        },
        'QPushButton[widgetType="message_box"]': {
            'min_height': 30,
            'max_height': 30,
        },
        'QLabel': {
            'color': _DS.Dark.TEXT,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
        },
        'QLabel[widgetType="flag_installed"]': {
            'min_width': '100px',
            'max_width': '100px',
            'min_height': '75px',
            'max_height': '75px',
            'border_radius': 20,
        },
        'QCheckBox': {
            'color': _DS.Dark.TEXT,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
        },
        'QRadioButton': {
            'color': _DS.Dark.TEXT,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
        },
        'QLineEdit, QDialog QTextEdit': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Dark.TEXT,
            'padding_left': '5px',
            'padding_right': '5px',
            'background_color': _DS.Dark.WIDGET_BG,
            'border_color': _DS.Dark.ORANGE,
            'border_width': '1px',
            'border_style': 'solid',
            'border_radius': '5px',
        },
        'QComboBox': {
            'max_height': 30,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Dark.TEXT,
            'background_color': _DS.Dark.WIDGET_BG,
            'border_color': _DS.Dark.ORANGE,
            'border_width': '1px',
            'border_style': 'solid',
            'border_radius': '5px',
        },
        'QComboBox QAbstractItemView': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Dark.TEXT,
            'background_color': _DS.Dark.WIDGET_BG,
            'border_color': _DS.Dark.ORANGE,
            'border_width': '1px',
            'border_style': 'solid',
            'border_radius': '5px',
        },
        'QComboBox QAbstractItemView::item': {
            'background_color_color': '#444',
            'color': 'white',
        },
        'QComboBox QAbstractItemView::item:selected': {
            'background_color_color': '#666',
            'color': 'black',
        },
        'QTabBar::tab': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'background_color': _DS.Dark.WIDGET_BG,
            'color': _DS.Dark.TEXT,
            'padding': '10px',
            'margin_right': '5px',
            'border': 'none',
            'border_radius': '5px',
        },
        'QTabBar::tab:selected': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'background_color': _DS.Dark.SELECTED,
            'color': _DS.Dark.TEXT,
        },
        'QTabBar::tab:hover': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'background_color': _DS.Dark.SELECTED,
            'color': _DS.Dark.TEXT,
        },
        'QTableWidget, QListWidget': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Dark.TEXT,
            'background_color': _DS.Dark.BACKGROUND,
            'gridline_color': _DS.Dark.BLUE,
        },
        'QTableWidget QHeaderView::section': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Dark.TEXT,
            'background_color': _DS.Dark.BACKGROUND,
        },
        'QTableWidget QHeaderView::section:checked, QTableWidget QHeaderView::section:pressed, QTableWidget QHeaderView::section:focus': {
            'background_color': _DS.Dark.HEADER_BG,
            'color': _DS.Dark.HEADER_TEXT,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
        },
        'QTableWidget::item:selected': {
            'background_color': _DS.Dark.SELECTED,
        },
        'QMenu': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Dark.TEXT,
            'background_color': _DS.Dark.MENU,
        },
        'QSpinBox': {
            'font_size': _DS.FONT_SIZE,
            'color': _DS.Dark.TEXT,
            'background_color': 'transparent',
            'border': '1px solid',
            'border_radius': '5px'
        },
        '@lb_reset_all_params': {
            'border': '2px solid',
            'border_radius': '5px',
            'border_color': _DS.Dark.TEXT,
        },
        '@lb_pyinstaller_installed': {
            'color': _DS.Dark.INSTALLED_TEXT,
            'background_color': _DS.Dark.INSTALLED_BG,
        },
        '@lb_pyinstaller_uninstalled': {
            'color': _DS.Dark.UNINSTALLED_TEXT,
            'background_color': _DS.Dark.UNINSTALLED_BG,
        },
        '@params_btn_loaded': {
            'background_color': 'red'
        },
        '@page_btn_selected': {
            'background_color': _DS.Dark.SELECTED_ATTENTION,
        },
        '@version_seperator': {
            'font_size': _DS.FONT_SIZE,
            'font_weight': 'bold',
        },
        '@message_box_default_button': {
            'border_width': '1px',
            'border_style': 'solid',
            'border_color': _DS.Dark.SELECTED,
        },
        '$btn_square_size': _DS.BTN_SQUARE_SIZE,
        '$btn_square_icon_size': (_DS.BTN_SQUARE_ICON_SIZE, _DS.BTN_SQUARE_ICON_SIZE),
        '$btn_svg_color': _DS.Dark.SELECTED,
        '$btn_svg_color_in_2': (_DS.Dark.SELECTED, _DS.Dark.TEXT),
        '$message_notification_background': _DS.Dark.SELECTED,
        '$message_notification_text': _DS.Dark.TEXT,
        '$message_notification_font_size': _DS.FONT_SIZE,
        '$message_notification_font_family': _DS.FONT_FAMILY,
        '~scrollbar': {
            'QScrollBar:vertical': {
                'border': 'none',
                'background_color': 'transparent',
                'width': '10px',
                'margin': [2, 0],
                'border_radius': 4,
            },
            'QScrollBar:horizontal': {
                'border': 'none',
                'background_color': 'transparent',
                'height': '10px',
                # 'min_height': 8,
                'margin': [0, 2],
                'border_radius': 4,
            },
            'QScrollBar::handle:vertical': {
                'background_color': _DS.Dark.SELECTED,
                'min_height': 10,
                'border_radius': 4,
            },
            ' QScrollBar::handle:horizontal': {
                'background_color': _DS.Dark.SELECTED,
                'min_width': 10,
                'border_radius': 4,
            },
            'QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover': {
                'background_color': '#ff0000',
            },
            'QScrollBar::sub_line:vertical, QScrollBar::add_line:vertical, QScrollBar::sub_line:horizontal, QScrollBar::add_line:horizontal': {
                'background_color': 'transparent',
            },
            'QScrollBar::add_page:vertical, QScrollBar::sub_page:vertical, QScrollBar::add_page:horizontal, QScrollBar::sub_page:horizontal': {
                'background_color': 'transparent',
            },
        }
    }
    LIGHT = {
        '#centralwidget, #tabWidget::pane, QTabBar::tab ,QTabWidget > QWidget, QGroupBox, QProgressBar, QDialog': {
            'color': _DS.Light.TEXT,
            'background_color': _DS.Light.BACKGROUND,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
        },
        'QPushButton': {
            'color': _DS.Light.TEXT,
            'background_color': _DS.Light.WIDGET_BG,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'min_width': '30px',
            'max_height': '50px',
            'border': 'none',
            'border_radius': '10px',
            'padding': [2, 2],
        },
        'QPushButton:hover': {
            'padding_bottom': '2px',
            'color': _DS.Light.HOVER_TEXT,
            'background_color': _DS.Light.HOVER_BACKGROUND
        },
        'QPushButton[widgetType="versionEditor"]': {
            'margin': 2,
            'border_width': 1,
            'border_style': 'solid',
            'border_color': _DS.Light.ORANGE,
            'border_radius': '0px',
        },
        'QPushButton[widgetType="Dialog"]': {
            'min_width': '80px',
            'max_height': '35px',
        },
        'QPushButton[widgetType="square"]': {
            'min_width': _DS.BTN_SQUARE_SIZE,
            'max_width': _DS.BTN_SQUARE_SIZE,
            'min_height': _DS.BTN_SQUARE_SIZE,
            'max_height': _DS.BTN_SQUARE_SIZE,
            'padding': [0, 0],
            'margin': 0,
            'border_radius': 15,
        },
        'QPushButton[widgetType="message_box"]': {
            'min_height': 30,
            'max_height': 30,
        },
        'QLabel': {
            'color': _DS.Light.TEXT,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
        },
        'QLabel[widgetType="flag_installed"]': {
            'min_width': '100px',
            'max_width': '100px',
            'min_height': '75px',
            'max_height': '75px',
            'border_radius': 20,
        },
        'QCheckBox': {
            'color': _DS.Light.TEXT,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
        },
        'QRadioButton': {
            'color': _DS.Light.TEXT,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
        },
        'QLineEdit, QDialog QTextEdit': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Light.TEXT,
            'padding_left': '5px',
            'padding_right': '5px',
            'background_color': _DS.Light.WIDGET_BG,
            'border_color': _DS.Light.ORANGE,
            'border_width': '1px',
            'border_style': 'solid',
            'border_radius': '5px',
        },
        'QComboBox': {
            'max_height': 30,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Light.TEXT,
            'background_color': _DS.Light.WIDGET_BG,
            'border_color': _DS.Light.ORANGE,
            'border_width': '1px',
            'border_style': 'solid',
            'border_radius': '5px',
        },
        'QComboBox QAbstractItemView': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Light.TEXT,
            'background_color': _DS.Light.WIDGET_BG,
            'border_color': _DS.Light.ORANGE,
            'border_width': '1px',
            'border_style': 'solid',
            'border_radius': '5px',
        },
        'QComboBox QAbstractItemView::item': {
            'background_color_color': '#444',
            'color': 'white',
        },
        'QComboBox QAbstractItemView::item:selected': {
            'background_color_color': '#666',
            'color': 'black',
        },
        'QTabBar::tab': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'background_color': _DS.Light.WIDGET_BG,
            'color': _DS.Light.TEXT,
            'padding': '10px',
            'margin_right': '5px',
            'border': 'none',
            'border_radius': '5px',
        },
        'QTabBar::tab:selected': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'background_color': _DS.Light.SELECTED,
            'color': _DS.Light.TEXT,
        },
        'QTabBar::tab:hover': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'background_color': _DS.Light.SELECTED,
            'color': _DS.Light.TEXT,
        },
        'QTableWidget, QListWidget': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Light.TEXT,
            'background_color': _DS.Light.BACKGROUND,
            'gridline_color': _DS.Light.BLUE,
        },
        'QTableWidget QHeaderView::section': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Light.TEXT,
            'background_color': _DS.Light.BACKGROUND,
        },
        'QTableWidget QHeaderView::section:checked, QTableWidget QHeaderView::section:pressed, QTableWidget QHeaderView::section:focus': {
            'background_color': _DS.Light.HEADER_BG,
            'color': _DS.Light.HEADER_TEXT,
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
        },
        'QTableWidget::item:selected': {
            'background_color': _DS.Light.SELECTED,
        },
        'QMenu': {
            'font_size': _DS.FONT_SIZE,
            'font_family': _DS.FONT_FAMILY,
            'color': _DS.Light.TEXT,
            'background_color': _DS.Light.MENU,
        },
        'QSpinBox': {
            'font_size': _DS.FONT_SIZE,
            'color': _DS.Light.TEXT,
            'background_color': 'transparent',
            'border': '1px solid',
            'border_radius': '5px'
        },
        '@lb_reset_all_params': {
            'border': '2px solid',
            'border_radius': '5px',
            'border_color': _DS.Light.TEXT,
        },
        '@lb_pyinstaller_installed': {
            'color': _DS.Light.INSTALLED_TEXT,
            'background_color': _DS.Light.INSTALLED_BG,
        },
        '@lb_pyinstaller_uninstalled': {
            'color': _DS.Light.UNINSTALLED_TEXT,
            'background_color': _DS.Light.UNINSTALLED_BG,
        },
        '@params_btn_loaded': {
            'background_color': 'red'
        },
        '@page_btn_selected': {
            'background_color': _DS.Light.SELECTED_ATTENTION,
        },
        '@version_seperator': {
            'font_size': _DS.FONT_SIZE,
            'font_weight': 'bold',
        },
        '@message_box_default_button': {
            'border_width': '1px',
            'border_style': 'solid',
            'border_color': _DS.Light.SELECTED,
        },
        '$btn_square_size': _DS.BTN_SQUARE_SIZE,
        '$btn_square_icon_size': (_DS.BTN_SQUARE_ICON_SIZE, _DS.BTN_SQUARE_ICON_SIZE),
        '$btn_svg_color': _DS.Light.SELECTED,
        '$btn_svg_color_in_2': (_DS.Light.SELECTED, _DS.Light.TEXT),
        '$message_notification_background': _DS.Light.SELECTED,
        '$message_notification_text': _DS.Light.TEXT,
        '$message_notification_font_size': _DS.FONT_SIZE,
        '$message_notification_font_family': _DS.FONT_FAMILY,
        '~scrollbar': {
            'QScrollBar:vertical': {
                'border': 'none',
                'background_color': 'transparent',
                'width': '10px',
                'margin': [2, 0],
                'border_radius': 4,
            },
            'QScrollBar:horizontal': {
                'border': 'none',
                'background_color': 'transparent',
                'height': '10px',
                # 'min_height': 8,
                'margin': [0, 2],
                'border_radius': 4,
            },
            'QScrollBar::handle:vertical': {
                'background_color': _DS.Light.SELECTED,
                'min_height': 10,
                'border_radius': 4,
            },
            ' QScrollBar::handle:horizontal': {
                'background_color': _DS.Light.SELECTED,
                'min_width': 10,
                'border_radius': 4,
            },
            'QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover': {
                'background_color': '#ff0000',
            },
            'QScrollBar::sub_line:vertical, QScrollBar::add_line:vertical, QScrollBar::sub_line:horizontal, QScrollBar::add_line:horizontal': {
                'background_color': 'transparent',
            },
            'QScrollBar::add_page:vertical, QScrollBar::sub_page:vertical, QScrollBar::add_page:horizontal, QScrollBar::sub_page:horizontal': {
                'background_color': 'transparent',
            },
        }
    }
