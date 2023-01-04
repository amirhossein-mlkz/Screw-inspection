# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eror_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(458, 232)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 145))
        font = QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(225, 5,5);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(21, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setStyleSheet(u"border:None;")
        self.label_2.setPixmap(QPixmap(u"images/alert.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(19)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border:None;")

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(210, 210, 210);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(25, 25, 25);\n"
"}\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(25, 25, 25);\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.close_btn = QPushButton(self.frame_3)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy1)
        self.close_btn.setMinimumSize(QSize(66, 45))
        self.close_btn.setMaximumSize(QSize(0, 45))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.close_btn.setFont(font2)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setLayoutDirection(Qt.LeftToRight)
        self.close_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(200, 200, 200);\n"
"\n"
"\n"
"\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"	background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"images/check-mark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.close_btn)

        self.suggest_btn_2 = QPushButton(self.frame_3)
        self.suggest_btn_2.setObjectName(u"suggest_btn_2")
        sizePolicy1.setHeightForWidth(self.suggest_btn_2.sizePolicy().hasHeightForWidth())
        self.suggest_btn_2.setSizePolicy(sizePolicy1)
        self.suggest_btn_2.setMinimumSize(QSize(66, 45))
        self.suggest_btn_2.setMaximumSize(QSize(0, 45))
        self.suggest_btn_2.setFont(font2)
        self.suggest_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.suggest_btn_2.setLayoutDirection(Qt.LeftToRight)
        self.suggest_btn_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(200, 200, 200);\n"
"\n"
"\n"
"\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"	background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"images/information.png", QSize(), QIcon.Normal, QIcon.Off)
        self.suggest_btn_2.setIcon(icon1)
        self.suggest_btn_2.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.suggest_btn_2)

        self.close_btn_2 = QPushButton(self.frame_3)
        self.close_btn_2.setObjectName(u"close_btn_2")
        sizePolicy1.setHeightForWidth(self.close_btn_2.sizePolicy().hasHeightForWidth())
        self.close_btn_2.setSizePolicy(sizePolicy1)
        self.close_btn_2.setMinimumSize(QSize(66, 45))
        self.close_btn_2.setMaximumSize(QSize(0, 45))
        self.close_btn_2.setFont(font2)
        self.close_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn_2.setLayoutDirection(Qt.LeftToRight)
        self.close_btn_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(200, 200, 200);\n"
"\n"
"\n"
"\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"	background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"images/error.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn_2.setIcon(icon2)
        self.close_btn_2.setIconSize(QSize(33, 30))

        self.horizontalLayout.addWidget(self.close_btn_2)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"ERROR", None))
        self.close_btn.setText("")
        self.suggest_btn_2.setText("")
        self.close_btn_2.setText("")
    # retranslateUi

