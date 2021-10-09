#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
番茄钟计时部件
"""

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget
from tomato_time_ui import Ui_TomatoTime


class TomatoTime(QWidget):
    """番茄钟对话框"""

    def __init__(self):
        """构造函数"""

        super().__init__(None)

        # 加载窗体文件
        self.ui = Ui_TomatoTime()
        self.ui.setupUi(self)
