# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_window.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(644, 105)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.total = QLabel(self.frame)
        self.total.setObjectName(u"total")

        self.horizontalLayout.addWidget(self.total)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.perfect = QLabel(self.frame)
        self.perfect.setObjectName(u"perfect")

        self.horizontalLayout.addWidget(self.perfect)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.defect = QLabel(self.frame)
        self.defect.setObjectName(u"defect")

        self.horizontalLayout.addWidget(self.defect)

        self.reset_btn = QPushButton(self.frame)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setMinimumSize(QSize(81, 25))
        self.reset_btn.setMaximumSize(QSize(70, 16777215))
        self.reset_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.reset_btn)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total Screws :", None))
        self.total.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Perfect Screws :", None))
        self.perfect.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Defect Screws :", None))
        self.defect.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

