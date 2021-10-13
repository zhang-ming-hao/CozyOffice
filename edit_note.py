#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
编辑记事对话框
"""

from PySide2.QtCore import Qt, QDateTime
from PySide2.QtWidgets import QDialog, QMessageBox

from add_note_ui import Ui_AddNoteDialog


class EditNoteDialog(QDialog):
    """编辑记事对话框"""

    def __init__(self, date=None, id=0):
        """
        构造函数

        :param date: 日期
        :param id:   数据ID
        """

        super().__init__(None)
        self.id = id

        # 加载窗体控件
        self.ui = Ui_AddNoteDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

        if date:
            self.ui.note_time.setDate(date)

        if id:
            # 显示数据内容
            self.load()

        self.ui.ok_btn.clicked.connect(self.save_note)
        self.ui.del_btn.clicked.connect(self.delete_note)

    def load(self):
        """加载数据"""

        note = qApp.get_note(self.id)
        if note:
            self.ui.note_time.setDateTime(QDateTime.fromTime_t(note["timestamp"]))
            self.ui.title.setText(note["title"])
            self.ui.content.setPlainText(note["content"])
            self.ui.remind.setChecked(note["remind"] == 1)

    def save_note(self):
        """保存记事"""

        dt = self.ui.note_time.dateTime()
        date = dt.toString("yyyyMMdd")
        timestamp = dt.toTime_t()
        remind = 1 if self.ui.remind.checkState() else 0

        title = self.ui.title.text()
        if not title:
            QMessageBox.critical(self, '错误', '请填写标题。')
            self.ui.title.setFocus()
            return

        content = self.ui.content.toPlainText()
        if not content:
            QMessageBox.critical(self, '错误', '请填写内容。')
            self.ui.content.setFocus()
            return

        if self.id:
            # 更新
            qApp.update_note(self.id, date, timestamp, title, content, remind)
        else:
            # 新建
            qApp.add_note(date, timestamp, title, content, remind)

        self.close()

    def delete_note(self):
        """删除记事"""

        if QMessageBox.question(self, '确认', '是否删除当前记事？') == QMessageBox.StandardButton.Yes:
            qApp.delete_note(self.id)

        self.close()