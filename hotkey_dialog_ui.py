# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hotkey_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_HotKeyDialog(object):
    def setupUi(self, HotKeyDialog):
        if not HotKeyDialog.objectName():
            HotKeyDialog.setObjectName(u"HotKeyDialog")
        HotKeyDialog.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/res/hotkey.png", QSize(), QIcon.Normal, QIcon.Off)
        HotKeyDialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(HotKeyDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.add_btn = QToolButton(HotKeyDialog)
        self.add_btn.setObjectName(u"add_btn")

        self.gridLayout.addWidget(self.add_btn, 0, 1, 1, 1)

        self.del_btn = QToolButton(HotKeyDialog)
        self.del_btn.setObjectName(u"del_btn")

        self.gridLayout.addWidget(self.del_btn, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.table = QTableWidget(HotKeyDialog)
        self.table.setObjectName(u"table")

        self.gridLayout.addWidget(self.table, 0, 0, 3, 1)


        self.retranslateUi(HotKeyDialog)

        QMetaObject.connectSlotsByName(HotKeyDialog)
    # setupUi

    def retranslateUi(self, HotKeyDialog):
        HotKeyDialog.setWindowTitle(QCoreApplication.translate("HotKeyDialog", u"\u60ec\u610f\u70ed\u952e", None))
        self.add_btn.setText(QCoreApplication.translate("HotKeyDialog", u"+", None))
        self.del_btn.setText(QCoreApplication.translate("HotKeyDialog", u"-", None))
    # retranslateUi

