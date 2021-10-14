#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
快捷键对话框
"""

from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QDialog, QHeaderView, QLineEdit

from hotkey_dialog_ui import Ui_HotKeyDialog


class HotKeyDialog(QDialog):
    """快捷键对话框"""

    def __init__(self):
        """构造函数"""

        super().__init__(None)

        # 加载窗体控件
        self.ui = Ui_HotKeyDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

        # 表格标题
        self.ui.table.setColumnCount(2)
        self.ui.table.setHorizontalHeaderLabels(["快捷键", "命令"])
        self.ui.table.setColumnWidth(0, 200)
        self.ui.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        # 表格内容
        self.hotkeys = qApp.get_hotkeys()
        self.ui.table.setRowCount(len(self.hotkeys))
        for row, hk in enumerate(self.hotkeys):
            hotkey = HotKeyEdit(self, row)
            hotkey.setText(hk[0])
            hotkey.editingFinished.connect(self.change_hotkey)
            self.ui.table.setCellWidget(row, 0, hotkey)

            cmd = RowEdit(self, row)
            cmd.setText(hk[1])
            cmd.editingFinished.connect(self.change_cmd)
            self.ui.table.setCellWidget(row, 1, cmd)

        # 信号与槽
        self.ui.add_btn.clicked.connect(self.add_row)
        self.ui.del_btn.clicked.connect(self.del_row)

    def add_row(self):
        """在表格内添加行"""

        row = self.ui.table.rowCount()
        self.ui.table.setRowCount(row + 1)
        hotkey = HotKeyEdit(self, row)
        hotkey.editingFinished.connect(self.change_hotkey)
        self.ui.table.setCellWidget(row, 0, hotkey)

        cmd = RowEdit(self, row)
        cmd.editingFinished.connect(self.change_cmd)
        self.ui.table.setCellWidget(row, 1, cmd)

        self.hotkeys.append(["", ""])

    def del_row(self):
        """删除表格中的行"""

        index = self.ui.table.currentIndex()
        if index.isValid():
            row = index.row()
            qApp.unregister_hotkey(self.hotkeys[row][0])
            self.ui.table.removeRow(row)
            self.hotkeys.pop(row)

    def change_hotkey(self, row, hotkey):
        """更新热键"""

        old_key = self.hotkeys[row][0]
        qApp.unregister_hotkey(old_key)
        self.hotkeys[row][0] = hotkey

        cmd = self.hotkeys[row][1]
        qApp.register_hotkey(hotkey, cmd)

    def change_cmd(self, row, cmd):
        """更新命令"""

        hotkey = self.hotkeys[row][0]
        qApp.register_hotkey(hotkey, cmd)
        self.hotkeys[row][1] = cmd


class RowEdit(QLineEdit):
    """重写Qt的文本框"""

    editingFinished = Signal(int, str)

    def __init__(self, parent, row):
        super().__init__(parent)

        self.row = row

        self.setStyleSheet("border: 0")
        self.setAlignment(Qt.AlignCenter)

    def focusOutEvent(self, event):
        """失去焦点事件"""

        self.editingFinished.emit(self.row, self.text())
        super().focusOutEvent(event)


class HotKeyEdit(RowEdit):
    """快捷键输入控件"""

    def __init__(self, parent, row):
        super().__init__(parent, row)

        self.row = row

        self.setStyleSheet("border: 0")
        self.setAlignment(Qt.AlignCenter)

    def keyPressEvent(self, event):
        """键盘按下事件"""

        key_name = ""
        if (event.key() >= Qt.Key_A and event.key() <= Qt.Key_Z) or event.key() >= Qt.Key_0 and event.key() <= Qt.Key_9:
            key_name = chr(event.key())
        elif event.key() >= Qt.Key_F1 and event.key() <= Qt.Key_F12:
            key_name = "F%d" % (event.key() - Qt.Key_F1 + 1)

        comb = ""
        mod = qApp.keyboardModifiers()
        if mod & Qt.ControlModifier == Qt.ControlModifier:
            comb += "Control + "

        if mod & Qt.AltModifier == Qt.AltModifier:
            comb += "Alt + "

        if mod & Qt.ShiftModifier == Qt.ShiftModifier:
            comb += "Shift + "

        self.setText(comb + key_name)
