# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_note.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_AddNoteDialog(object):
    def setupUi(self, AddNoteDialog):
        if not AddNoteDialog.objectName():
            AddNoteDialog.setObjectName(u"AddNoteDialog")
        AddNoteDialog.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/res/note.png", QSize(), QIcon.Normal, QIcon.Off)
        AddNoteDialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(AddNoteDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(AddNoteDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_2 = QLabel(AddNoteDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_3 = QLabel(AddNoteDialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.title = QLineEdit(AddNoteDialog)
        self.title.setObjectName(u"title")

        self.gridLayout.addWidget(self.title, 3, 1, 1, 3)

        self.content = QTextEdit(AddNoteDialog)
        self.content.setObjectName(u"content")

        self.gridLayout.addWidget(self.content, 4, 1, 1, 3)

        self.del_btn = QPushButton(AddNoteDialog)
        self.del_btn.setObjectName(u"del_btn")

        self.gridLayout.addWidget(self.del_btn, 6, 1, 1, 1)

        self.remind = QCheckBox(AddNoteDialog)
        self.remind.setObjectName(u"remind")

        self.gridLayout.addWidget(self.remind, 0, 3, 1, 1)

        self.ok_btn = QPushButton(AddNoteDialog)
        self.ok_btn.setObjectName(u"ok_btn")

        self.gridLayout.addWidget(self.ok_btn, 6, 2, 1, 1)

        self.canle_btn = QPushButton(AddNoteDialog)
        self.canle_btn.setObjectName(u"canle_btn")

        self.gridLayout.addWidget(self.canle_btn, 6, 3, 1, 1)

        self.note_time = QDateTimeEdit(AddNoteDialog)
        self.note_time.setObjectName(u"note_time")

        self.gridLayout.addWidget(self.note_time, 0, 1, 1, 2)


        self.retranslateUi(AddNoteDialog)
        self.canle_btn.clicked.connect(AddNoteDialog.close)

        QMetaObject.connectSlotsByName(AddNoteDialog)
    # setupUi

    def retranslateUi(self, AddNoteDialog):
        AddNoteDialog.setWindowTitle(QCoreApplication.translate("AddNoteDialog", u"\u6dfb\u52a0\u8bb0\u4e8b", None))
        self.label.setText(QCoreApplication.translate("AddNoteDialog", u"\u6807\u9898\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("AddNoteDialog", u"\u5185\u5bb9\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("AddNoteDialog", u"\u65f6\u95f4\uff1a", None))
        self.del_btn.setText(QCoreApplication.translate("AddNoteDialog", u"\u5220\u9664", None))
        self.remind.setText(QCoreApplication.translate("AddNoteDialog", u"\u63d0\u9192", None))
        self.ok_btn.setText(QCoreApplication.translate("AddNoteDialog", u"\u786e\u5b9a", None))
        self.canle_btn.setText(QCoreApplication.translate("AddNoteDialog", u"\u53d6\u6d88", None))
        self.note_time.setDisplayFormat(QCoreApplication.translate("AddNoteDialog", u"yyyy-MM-dd HH:mm", None))
    # retranslateUi

