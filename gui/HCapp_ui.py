# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HandControl.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setStyleSheet(u"background-image: url(gui/image/background.jpg)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 601, 361))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.FinishButton = QPushButton(self.gridLayoutWidget)
        self.FinishButton.setObjectName(u"FinishButton")

        self.gridLayout.addWidget(self.FinishButton, 4, 5, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 7, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 3, 3, 1, 1)

        self.StartButton = QPushButton(self.gridLayoutWidget)
        self.StartButton.setObjectName(u"StartButton")

        self.gridLayout.addWidget(self.StartButton, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 2, 1, 1)

        self.videoChecker = QCheckBox(self.gridLayoutWidget)
        self.videoChecker.setObjectName(u"videoChecker")
        self.videoChecker.setChecked(True)
        self.videoChecker.setTristate(False)

        self.gridLayout.addWidget(self.videoChecker, 2, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 3, 1, 1)

        self.WorkText = QLabel(self.gridLayoutWidget)
        self.WorkText.setObjectName(u"WorkText")

        self.gridLayout.addWidget(self.WorkText, 4, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 6, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 5, 3, 1, 1)

        self.CamerIndexText = QLabel(self.gridLayoutWidget)
        self.CamerIndexText.setObjectName(u"CamerIndexText")

        self.gridLayout.addWidget(self.CamerIndexText, 1, 4, 1, 1)

        self.CameraIndex = QSpinBox(self.gridLayoutWidget)
        self.CameraIndex.setObjectName(u"CameraIndex")

        self.gridLayout.addWidget(self.CameraIndex, 2, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.FinishButton.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.videoChecker.setText(QCoreApplication.translate("MainWindow", u"Video Output", None))
        self.WorkText.setText("")
        self.CamerIndexText.setText(QCoreApplication.translate("MainWindow", u"Input camera index. Default 0", None))
    # retranslateUi

