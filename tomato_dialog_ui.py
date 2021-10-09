# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tomato_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from start_tomato import StartTomato
from tomato_time import TomatoTime

import resources_rc

class Ui_TomatoDialog(object):
    def setupUi(self, TomatoDialog):
        if not TomatoDialog.objectName():
            TomatoDialog.setObjectName(u"TomatoDialog")
        TomatoDialog.resize(402, 300)
        icon = QIcon()
        icon.addFile(u":/res/tomato.png", QSize(), QIcon.Normal, QIcon.Off)
        TomatoDialog.setWindowIcon(icon)
        TomatoDialog.setModal(False)
        self.horizontalLayout = QHBoxLayout(TomatoDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(TomatoDialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(210, 0))
        self.start_page = StartTomato()
        self.start_page.setObjectName(u"start_page")
        self.stackedWidget.addWidget(self.start_page)
        self.time_page = TomatoTime()
        self.time_page.setObjectName(u"time_page")
        self.stackedWidget.addWidget(self.time_page)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(TomatoDialog)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TomatoDialog)
    # setupUi

    def retranslateUi(self, TomatoDialog):
        TomatoDialog.setWindowTitle(QCoreApplication.translate("TomatoDialog", u"\u756a\u8304\u949f-\u672a\u5f00\u59cb", None))
    # retranslateUi

