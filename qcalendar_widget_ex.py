#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

import json
import datetime
import urllib.request

from PySide2.QtCore import Qt, QEvent, QPersistentModelIndex, Signal, QDate, QPoint
from PySide2.QtGui import QColor, QBrush
from PySide2.QtWidgets import QCalendarWidget, QTableView


class QCalendarWidgetEx(QCalendarWidget):
    """番茄钟对话框"""

    double_click = Signal(QDate)
    right_click = Signal(QDate, QPoint)

    def __init__(self, parent):
        """构造函数"""

        super().__init__(parent)

        now = datetime.datetime.now()
        self.cur_year = now.year
        self.cur_month = now.month
        self.days = self.get_month_info()

        self.setGridVisible(True)
        self.setMouseTracking(True)
        self.currentPageChanged.connect(self.save_current_page)

        table = self.findChild(QTableView)
        table.installEventFilter(self)
        table.setMouseTracking(True)

    def save_current_page(self, year, month):
        """当前年月改变事件"""

        self.cur_year = year
        self.cur_month = month

        self.days = self.get_month_info()

    def get_month_info(self):
        """调用接口取得上月、当月、下月的信息"""

        url = "https://api.apihubs.cn/holiday/get?size=365&cn=1&month="

        # 上个月
        year = self.cur_year
        month = self.cur_month - 1
        if self.cur_month == 0:
            month = 1
            year = self.cur_year - 1

        url += "%04d%02d," % (year, month)

        # 当月
        url += "%04d%02d," % (self.cur_year, self.cur_month)

        # 下个月
        year = self.cur_year
        month = self.cur_month + 1
        if self.cur_month == 13:
            month = 12
            year = self.cur_year + 1

        url += "%04d%02d" % (year, month)

        res = urllib.request.urlopen(url)
        day_info = json.loads(res.read())

        days = {}
        for day in day_info["data"]["list"]:
            days[str(day["date"])] = day

        return days

    def paintCell(self, painter, rect, date):
        """格子重绘事件"""

        day = date.toString("yyyyMMdd")

        # 格子颜色
        if qApp.has_note(day):
            painter.setBrush(QBrush(QColor(128, 255, 128)))
            painter.drawRect(rect)

        # 格子文字
        if day in self.days:
            c = rect.center()
            day_info = self.days[day]

            if date.year() != self.cur_year or date.month() != self.cur_month:
                # 不是本月的日期
                painter.setPen(Qt.gray)

                # 日期
                text = str(date.day())
                frect = painter.boundingRect(rect, Qt.AlignCenter, text)
                painter.drawText(c.x() - frect.width() / 2, c.y() - frect.height() / 2, text)

                # 农历
                if day_info["holiday"] != 10 and day_info["holiday_today"] == 1:
                    text = day_info["holiday_cn"]
                else:
                    if day_info["lunar_date_cn"].endswith("初一"):
                        text = day_info["lunar_date_cn"][-4:-2]
                    else:
                        text = day_info["lunar_date_cn"][-2:]
                frect = painter.boundingRect(rect, Qt.AlignCenter, text)
                painter.drawText(c.x() - frect.width() / 2, c.y() + frect.height() / 2, text)
            else:
                painter.setPen(Qt.black)
                if day_info["weekend"] == 1:
                    painter.setPen(Qt.red)

                # 日期
                text = str(date.day())
                frect = painter.boundingRect(rect, Qt.AlignCenter, text)
                painter.drawText(c.x() - frect.width() / 2, c.y() - frect.height() / 2, text)

                # 农历
                if day_info["holiday"] != 10 and day_info["holiday_today"] == 1:
                    text = day_info["holiday_cn"]
                    painter.setPen(Qt.blue)
                else:
                    if day_info["lunar_date_cn"].endswith("初一"):
                        text = day_info["lunar_date_cn"][-4:-2]
                    else:
                        text = day_info["lunar_date_cn"][-2:]

                if day_info["weekend"] == 1:
                    painter.setPen(Qt.red)
                frect = painter.boundingRect(rect, Qt.AlignCenter, text)
                painter.drawText(c.x() - frect.width() / 2, c.y() + frect.height() / 2, text)

            # 休息日
            if day_info["holiday_recess"] == 1:
                painter.drawImage(rect.x(), rect.y(), ":/res/xiu.png")

            # 调休工作日
            if day_info["holiday_overtime"] != 10:
                painter.drawImage(rect.x(), rect.y(), ":/res/ban.png")

        else:
            super().paintCell(painter, rect, date)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.ContextMenu:
            index = QPersistentModelIndex(source.indexAt(event.pos()))
            date = QDate(self.cur_year, self.cur_month, index.data())
            self.right_click.emit(date, event.pos())
        elif event.type() == QEvent.Type.MouseButtonRelease:
            index = QPersistentModelIndex(source.indexAt(event.pos()))
            date = QDate(self.cur_year, self.cur_month, index.data())
            self.double_click.emit(date)

        return False
