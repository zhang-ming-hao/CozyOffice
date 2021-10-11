#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

from PySide2.QtWidgets import QCalendarWidget
from win10toast import ToastNotifier


class QCalendarWidgetEx(QCalendarWidget):
    """番茄钟对话框"""

    def __init__(self, parent):
        """构造函数"""

        super().__init__(parent)

        self.setGridVisible(True)

    def paintCell(self, painter, rect, date):
        """格子重绘事件"""

        print(painter, rect, date)

        painter.drawText(rect.x(), rect.y(), str(date.day()))