
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QObject, QTimer, QEvent, Qt


class WaveAnimationFilter(QObject):
    def __init__(self, label: QLabel, long_press_duration=1000, wave_interval=50):
        super().__init__(label)
        self._label = label
        self._progress = 0.0  # 当前进度 0~1
        self._is_long_press_activated = False  # 是否激活
        self._pressing = False  # 是否处于按压状态
        self._elapsed_time = 0  # 按压累计时间
        self._long_press_duration = long_press_duration  # 长按所需时间(ms)

        self._timer = QTimer(self)
        self._timer.setInterval(wave_interval)  # 每50ms更新一次
        self._timer.timeout.connect(self._update_animation)

    def _update_animation(self):
        """更新动画进度"""
        if self._pressing:
            # 更新进度
            self._elapsed_time += self._timer.interval()
            self._progress = min(self._elapsed_time / self._long_press_duration, 1.0)

            # 激活长按
            if self._progress >= 1.0 and not self._is_long_press_activated:
                self._is_long_press_activated = True
                self._label.setStyleSheet("background-color: green;")  # 激活状态变为绿色
        else:
            # 松开后进度下降
            self._elapsed_time = max(self._elapsed_time - self._timer.interval(), 0)
            self._progress = max(self._progress - 0.05, 0.0)

        # 停止动画计时器(当松开后进度回到 0)
        if not self._pressing and self._progress <= 0:
            self._timer.stop()

        # 触发重绘
        self._label.update()

    def eventFilter(self, obj, event):
        if obj is self._label:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self._pressing = True
                self._elapsed_time = 0
                self._is_long_press_activated = False
                self._timer.start()
                self._label.setStyleSheet("")  # 清除激活颜色
            elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self._pressing = False
                # self._label.setStyleSheet(
                #     "background-color: red;" if self._is_long_press_activated else ""
                # )  # 设置释放后的状态
                self._label.setStyleSheet("")
            elif event.type() == QEvent.Paint:
                self._paint_wave_effect()
        return super().eventFilter(obj, event)

    def _paint_wave_effect(self):
        """绘制波浪动画"""
        if self._progress > 0:
            painter = QPainter(self._label)
            painter.setRenderHint(QPainter.Antialiasing)

            rect = self._label.rect()
            height = int(rect.height() * self._progress)  # 动态高度
            wave_rect = rect.adjusted(0, rect.height() - height, 0, 0)

            # 动态绘制波浪颜色
            color = QColor(0, 0, 255, 150) if not self._is_long_press_activated else QColor(0, 255, 0, 200)

            painter.fillRect(wave_rect, color)
