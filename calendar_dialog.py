#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog, QSystemTrayIcon
from win10toast import ToastNotifier

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
