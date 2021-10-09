# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_tomato.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_StartTomato(object):
    def setupUi(self, StartTomato):
        if not StartTomato.objectName():
            StartTomato.setObjectName(u"StartTomato")
        StartTomato.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(StartTomato)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(StartTomato)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(150, 150))
        self.label.setMaximumSize(QSize(150, 150))
        self.label.setPixmap(QPixmap(u":/res/tomato.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(StartTomato)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.work_time = QSpinBox(self.widget_2)
        self.work_time.setObjectName(u"work_time")
        self.work_time.setMinimum(1)
        self.work_time.setMaximum(99)
        self.work_time.setValue(25)

        self.gridLayout_2.addWidget(self.work_time, 1, 1, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.start_btn = QPushButton(self.widget_2)
        self.start_btn.setObjectName(u"start_btn")

        self.horizontalLayout_2.addWidget(self.start_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 7, 0, 1, 3)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)

        self.rest_time = QSpinBox(self.widget_2)
        self.rest_time.setObjectName(u"rest_time")
        self.rest_time.setMinimum(1)
        self.rest_time.setValue(5)

        self.gridLayout_2.addWidget(self.rest_time, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(StartTomato)

        QMetaObject.connectSlotsByName(StartTomato)
    # setupUi

    def retranslateUi(self, StartTomato):
        StartTomato.setWindowTitle(QCoreApplication.translate("StartTomato", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("StartTomato", u"\u5de5\u4f5c\u65f6\u957f\uff1a", None))
        self.start_btn.setText(QCoreApplication.translate("StartTomato", u"\u5f00\u59cb\u8ba1\u65f6", None))
        self.label_5.setText(QCoreApplication.translate("StartTomato", u"\u5206\u949f", None))
        self.label_3.setText(QCoreApplication.translate("StartTomato", u"\u5206\u949f", None))
        self.label_4.setText(QCoreApplication.translate("StartTomato", u"\u4f11\u606f\u65f6\u957f\uff1a", None))
    # retranslateUi

