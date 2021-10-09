#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
番茄钟对话框
"""

from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog
from win10toast import ToastNotifier

from tomato_dialog_ui import Ui_TomatoDialog


class TomatoDialog(QDialog):
    """番茄钟对话框"""

    def __init__(self):
        """构造函数"""

        super().__init__(None)

        # 计时器
        self.timer = QTimer()
        self.timer.start(1000)
        self.work_time = 0      # 工作时长（秒）
        self.rest_time = 0      # 休息时长（秒）
        self.cur_time = 0       # 当前计数（秒）
        self.is_working = False
        self.is_resting = False

        # 加载窗体控件
        self.ui = Ui_TomatoDialog()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.setWindowFlags(Qt.Dialog | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

        # 连接信号与槽
        self.timer.timeout.connect(self.on_timer)
        self.ui.start_page.ui.start_btn.clicked.connect(self.start)
        self.ui.time_page.ui.end_btn.clicked.connect(self.end)

    def start(self):
        """开始番茄钟"""

        self.work_time = self.ui.start_page.ui.work_time.value() * 60
        self.rest_time = self.ui.start_page.ui.rest_time.value() * 60

        self.ui.time_page.ui.work_time.setText(self.ui.start_page.ui.work_time.text())
        self.ui.time_page.ui.rest_time.setText(self.ui.start_page.ui.rest_time.text())

        self.ui.stackedWidget.setCurrentIndex(1)
        self.start_work()

    def end(self):
        """停止番茄钟"""

        self.ui.stackedWidget.setCurrentIndex(0)
        self.setWindowIcon(QIcon(":res/tomato.png"))
        self.setWindowTitle("番茄钟-未开始")

        self.is_working = False
        self.is_resting = False

    def start_work(self):
        """设置状态为工作中"""

        self.setWindowIcon(QIcon(":res/working.png"))
        self.ui.time_page.ui.status.setPixmap(":res/working.png")
        self.setWindowTitle("番茄钟-工作中")

        self.is_working = True
        self.is_resting = False
        self.cur_time = self.work_time

        toaster = ToastNotifier()
        toaster.show_toast("番茄钟", f"开始专注工作{self.work_time / 60}分钟！", duration=5, threaded=True)

    def start_rest(self):
        """设置状态为休息中"""

        self.setWindowIcon(QIcon(":res/resting.png"))
        self.ui.time_page.ui.status.setPixmap(":res/resting.png")
        self.setWindowTitle("番茄钟-休息中")

        self.is_working = False
        self.is_resting = True
        self.cur_time = self.rest_time

        toaster = ToastNotifier()
        toaster.show_toast("番茄钟", f"休息{self.rest_time / 60}分钟。", duration=5, threaded=True)

    def on_timer(self):
        """计时器槽"""

        if self.is_working or self.is_resting:
            self.cur_time -= 1
            self.ui.time_page.ui.lcd.display(f"{int(self.cur_time / 60)}:{self.cur_time % 60}")
            if self.cur_time < 0:
                if self.is_working:
                    self.start_rest()
                else:
                    self.start_work()

    def closeEvent(self, event):
        """窗口关闭事件"""

        if self.is_working or self.is_resting:
            self.showMinimized()
            event.ignore()
