# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_confirm_window(object):
    def setupUi(self, confirm_window):
        if not confirm_window.objectName():
            confirm_window.setObjectName(u"confirm_window")
        confirm_window.resize(401, 140)
        self.background_frame = QFrame(confirm_window)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setGeometry(QRect(-30, -10, 441, 161))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_frame.sizePolicy().hasHeightForWidth())
        self.background_frame.setSizePolicy(sizePolicy)
        self.background_frame.setAutoFillBackground(False)
        self.background_frame.setStyleSheet(u"QFrame {\n"
"	background-color: #144475;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.background_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 20, 380, 85))
        self.frame_2.setLayoutDirection(Qt.RightToLeft)
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color:#F3F6FE;\n"
"	border-radius: 10px;\n"
"border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(110, 50, 104, 71))
        self.msg_label = QTextEdit(self.frame_2)
        self.msg_label.setObjectName(u"msg_label")
        self.msg_label.setGeometry(QRect(9, 8, 361, 71))
        font = QFont()
        font.setPointSize(10)
        self.msg_label.setFont(font)
        self.yes_btn = QPushButton(self.background_frame)
        self.yes_btn.setObjectName(u"yes_btn")
        self.yes_btn.setGeometry(QRect(120, 115, 93, 31))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 173, 64, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.yes_btn.setPalette(palette)
        self.yes_btn.setLayoutDirection(Qt.LeftToRight)
        self.yes_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #78AD40;\n"
"	color:white;\n"
"	border: none;\n"
"	text-align: center;\n"
"	border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.no_btn = QPushButton(self.background_frame)
        self.no_btn.setObjectName(u"no_btn")
        self.no_btn.setGeometry(QRect(250, 115, 93, 31))
        self.no_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #FF1111;\n"
"	color: white;\n"
"	border: none;\n"
"	text-align:center;\n"
"	border-radius: 15px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.retranslateUi(confirm_window)

        QMetaObject.connectSlotsByName(confirm_window)
    # setupUi

    def retranslateUi(self, confirm_window):
        confirm_window.setWindowTitle(QCoreApplication.translate("confirm_window", u"Form", None))
        self.msg_label.setHtml(QCoreApplication.translate("confirm_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">text</p></body></html>", None))
        self.yes_btn.setText(QCoreApplication.translate("confirm_window", u" YES", None))
        self.no_btn.setText(QCoreApplication.translate("confirm_window", u" NO", None))
    # retranslateUi

