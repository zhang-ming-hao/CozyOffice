#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
日历对话框
"""

from functools import partial

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QMenu, QAction

from edit_note import EditNoteDialog
from calendar_dialog_ui import Ui_CalendarDialog


class CalendarDialog(QDialog):
    """日历对话框"""

    def __init__(self):
        """构造函数"""

        super().__init__(None)

        # 加载窗体控件
        self.ui = Ui_CalendarDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

        self.ui.calendar.right_click.connect(self.show_menu)
        self.ui.calendar.double_click.connect(self.show_edit_note)

    def show_menu(self, date, pos):
        """
        显示操作菜单

        :param date: 点击的日期
        :param pos: 点击的位置
        """

        menu = QMenu()

        # 添加记事
        add = QAction("添加记事", self)
        add.triggered.connect(partial(self.show_edit_note, date=date))
        menu.addAction(add)

        # 分隔
        menu.addSeparator()

        # 记事标题
        notes = qApp.get_notes(date.toString("yyyyMMdd"))
        for note in notes:
            action = QAction(note["title"], self)
            action.triggered.connect(partial(self.show_edit_note, id=note["id"]))
            menu.addAction(action)

        # 显示菜单
        menu.move(self.mapToGlobal(pos))
        menu.exec_()

    def show_edit_note(self, date=None, id=None):
        """
        显示编辑记事对话框

        :param date: 点击的日期
        """

        dlg = EditNoteDialog(date=date, id=id)
        dlg.exec_()
        self.ui.calendar.update()

