# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendar_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qcalendar_widget_ex import QCalendarWidgetEx

import resources_rc

class Ui_CalendarDialog(object):
    def setupUi(self, CalendarDialog):
        if not CalendarDialog.objectName():
            CalendarDialog.setObjectName(u"CalendarDialog")
        CalendarDialog.resize(673, 493)
        icon = QIcon()
        icon.addFile(u":/res/note.png", QSize(), QIcon.Normal, QIcon.Off)
        CalendarDialog.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(CalendarDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.calendar = QCalendarWidgetEx(CalendarDialog)
        self.calendar.setObjectName(u"calendar")

        self.horizontalLayout.addWidget(self.calendar)


        self.retranslateUi(CalendarDialog)

        QMetaObject.connectSlotsByName(CalendarDialog)
    # setupUi

    def retranslateUi(self, CalendarDialog):
        CalendarDialog.setWindowTitle(QCoreApplication.translate("CalendarDialog", u"\u60ec\u610f\u8bb0\u4e8b\u672c", None))
    # retranslateUi

