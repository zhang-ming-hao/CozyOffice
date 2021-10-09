#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
启动番茄钟小部件
"""

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget
from start_tomato_ui import Ui_StartTomato


class StartTomato(QWidget):
    """番茄钟对话框"""

    def __init__(self):
        """构造函数"""

        super().__init__(None)

        # 加载窗体文件
        self.ui = Ui_StartTomato()
        self.ui.setupUi(self)
