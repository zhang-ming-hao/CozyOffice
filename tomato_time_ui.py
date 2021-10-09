# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tomato_time.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_TomatoTime(object):
    def setupUi(self, TomatoTime):
        if not TomatoTime.objectName():
            TomatoTime.setObjectName(u"TomatoTime")
        TomatoTime.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(TomatoTime)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(TomatoTime)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.status = QLabel(self.widget)
        self.status.setObjectName(u"status")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setMinimumSize(QSize(150, 150))
        self.status.setMaximumSize(QSize(150, 150))
        self.status.setPixmap(QPixmap(u":/res/working.png"))
        self.status.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.status)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(TomatoTime)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.end_btn = QPushButton(self.widget_2)
        self.end_btn.setObjectName(u"end_btn")

        self.horizontalLayout_3.addWidget(self.end_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.lcd = QLCDNumber(self.widget_2)
        self.lcd.setObjectName(u"lcd")
        self.lcd.setStyleSheet(u"border: 1px solid green; color: green;")
        self.lcd.setSmallDecimalPoint(False)
        self.lcd.setDigitCount(5)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcd, 3, 0, 1, 3)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.rest_time = QLabel(self.widget_2)
        self.rest_time.setObjectName(u"rest_time")
        self.rest_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.rest_time, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.work_time = QLabel(self.widget_2)
        self.work_time.setObjectName(u"work_time")
        self.work_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.work_time, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(TomatoTime)

        QMetaObject.connectSlotsByName(TomatoTime)
    # setupUi

    def retranslateUi(self, TomatoTime):
        TomatoTime.setWindowTitle(QCoreApplication.translate("TomatoTime", u"Form", None))
        self.status.setText("")
        self.label_4.setText(QCoreApplication.translate("TomatoTime", u"\u4f11\u606f\u65f6\u957f\uff1a", None))
        self.end_btn.setText(QCoreApplication.translate("TomatoTime", u"\u7ed3\u675f\u8ba1\u65f6", None))
        self.label.setText(QCoreApplication.translate("TomatoTime", u"\u5de5\u4f5c\u65f6\u957f\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("TomatoTime", u"\u5206\u949f", None))
        self.label_3.setText(QCoreApplication.translate("TomatoTime", u"\u5206\u949f", None))
        self.rest_time.setText(QCoreApplication.translate("TomatoTime", u"5", None))
        self.work_time.setText(QCoreApplication.translate("TomatoTime", u"25", None))
    # retranslateUi

