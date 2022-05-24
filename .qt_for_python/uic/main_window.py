# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStackedWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1328, 841)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: rgb(255,255,255);\n"
"	background-color:white;\n"
"	border: Transparent;\n"
"	text-align: center;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(212,212,212);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////"
                        "//////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: Transparent;\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"	padding-left: 0px;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left ;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left:15px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 0px;\n"
"\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	bor"
                        "der-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: center;\n"
"\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 15px solid transparent;\n"
"\n"
"	text-align: left;\n"
"	padding-left:44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox "
                        "{	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(230,230,230)\n"
"}\n"
"#extraLeftBox:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(20,20,20); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
""
                        "	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
""
                        "#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	padding:"
                        " 1px;\n"
"	border-radius:1px;\n"
"	gridline-color: rgb(40,70,160);\n"
"	border-bottom: 1px solid rgb(180,180,180);\n"
"\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(180,180,108);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(180,180,108);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(0,0,0);\n"
"	padding: 3px;\n"
"    background-color: rgb(30,30,30);\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0,0,0);\n"
"background-color: rgb(30,30,30);\n"
"color:rgb(255,255,255);\n"
"\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(70,135,230);\n"
"	color : White;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(210,210,150);\n"
"	border-radius: 5px;\n"
""
                        "	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #0078D7;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////"
                        "\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(30,30,30);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(40,70,160);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(30,30,30);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:hori"
                        "zontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(40,70,160);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(30,30,30);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(30,30,30);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, Q"
                        "ScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #78AD40;\n"
"	border: 3px solid rgb(58, 41, 11);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px s"
                        "olid #78AD40;\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    mar"
                        "gin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(119, 117, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* //////"
                        "///////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color:rgb(0,0,0);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.frame)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(0, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(60, 46))
        self.topLogoInfo.setMaximumSize(QSize(60, 50))
        self.topLogoInfo.setStyleSheet(u"background-color:#144475;\n"
"")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.topLogoInfo)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.toogle_btn_1 = QPushButton(self.topLogoInfo)
        self.toogle_btn_1.setObjectName(u"toogle_btn_1")
        self.toogle_btn_1.setMinimumSize(QSize(30, 30))
        self.toogle_btn_1.setMaximumSize(QSize(30, 16777215))
        self.toogle_btn_1.setStyleSheet(u"border:None;")
        icon = QIcon()
        icon.addFile(u"images/icons/dots.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toogle_btn_1.setIcon(icon)
        self.toogle_btn_1.setIconSize(QSize(30, 30))

        self.horizontalLayout_27.addWidget(self.toogle_btn_1)


        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setStyleSheet(u"background-color:#144475;")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 500))
        self.topMenu.setMaximumSize(QSize(16777215, 497))
        self.topMenu.setCursor(QCursor(Qt.ArrowCursor))
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.side_dashboard_btn = QPushButton(self.topMenu)
        self.side_dashboard_btn.setObjectName(u"side_dashboard_btn")
        self.side_dashboard_btn.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_dashboard_btn.sizePolicy().hasHeightForWidth())
        self.side_dashboard_btn.setSizePolicy(sizePolicy)
        self.side_dashboard_btn.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.side_dashboard_btn.setFont(font)
        self.side_dashboard_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_dashboard_btn.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u"images/setting_main_window/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_dashboard_btn.setIcon(icon1)
        self.side_dashboard_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_8.addWidget(self.side_dashboard_btn)

        self.side_tool_setting_btn = QPushButton(self.topMenu)
        self.side_tool_setting_btn.setObjectName(u"side_tool_setting_btn")
        self.side_tool_setting_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.side_tool_setting_btn.sizePolicy().hasHeightForWidth())
        self.side_tool_setting_btn.setSizePolicy(sizePolicy)
        self.side_tool_setting_btn.setMinimumSize(QSize(0, 45))
        self.side_tool_setting_btn.setFont(font)
        self.side_tool_setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_tool_setting_btn.setLayoutDirection(Qt.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u"images/setting_main_window/plc_setting_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_tool_setting_btn.setIcon(icon2)
        self.side_tool_setting_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_8.addWidget(self.side_tool_setting_btn)

        self.side_camera_setting_btn = QPushButton(self.topMenu)
        self.side_camera_setting_btn.setObjectName(u"side_camera_setting_btn")
        self.side_camera_setting_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.side_camera_setting_btn.sizePolicy().hasHeightForWidth())
        self.side_camera_setting_btn.setSizePolicy(sizePolicy)
        self.side_camera_setting_btn.setMinimumSize(QSize(0, 45))
        self.side_camera_setting_btn.setFont(font)
        self.side_camera_setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_camera_setting_btn.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u"images/setting_main_window/camera_setting_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_camera_setting_btn.setIcon(icon3)
        self.side_camera_setting_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_8.addWidget(self.side_camera_setting_btn)

        self.side_users_setting_btn = QPushButton(self.topMenu)
        self.side_users_setting_btn.setObjectName(u"side_users_setting_btn")
        self.side_users_setting_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.side_users_setting_btn.sizePolicy().hasHeightForWidth())
        self.side_users_setting_btn.setSizePolicy(sizePolicy)
        self.side_users_setting_btn.setMinimumSize(QSize(0, 45))
        self.side_users_setting_btn.setFont(font)
        self.side_users_setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_users_setting_btn.setLayoutDirection(Qt.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u"images/setting_main_window/users_setting_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_users_setting_btn.setIcon(icon4)
        self.side_users_setting_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_8.addWidget(self.side_users_setting_btn)

        self.side_general_setting_btn = QPushButton(self.topMenu)
        self.side_general_setting_btn.setObjectName(u"side_general_setting_btn")
        self.side_general_setting_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.side_general_setting_btn.sizePolicy().hasHeightForWidth())
        self.side_general_setting_btn.setSizePolicy(sizePolicy)
        self.side_general_setting_btn.setMinimumSize(QSize(0, 45))
        self.side_general_setting_btn.setFont(font)
        self.side_general_setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_general_setting_btn.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u"images/setting_main_window/general_setting_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_general_setting_btn.setIcon(icon5)
        self.side_general_setting_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_8.addWidget(self.side_general_setting_btn)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalMenuLayout.addItem(self.verticalSpacer_3)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 0, 0, 0)
        self.main_login_btn = QPushButton(self.bottomMenu)
        self.main_login_btn.setObjectName(u"main_login_btn")
        sizePolicy.setHeightForWidth(self.main_login_btn.sizePolicy().hasHeightForWidth())
        self.main_login_btn.setSizePolicy(sizePolicy)
        self.main_login_btn.setMinimumSize(QSize(0, 45))
        self.main_login_btn.setFont(font)
        self.main_login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.main_login_btn.setLayoutDirection(Qt.RightToLeft)
        icon6 = QIcon()
        icon6.addFile(u"images/login_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.main_login_btn.setIcon(icon6)
        self.main_login_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.main_login_btn)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)

        self.leftMenuFrame.raise_()
        self.topLogoInfo.raise_()

        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 1, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        self.extraLabel.setTextFormat(Qt.PlainText)

        self.extraTopLayout.addWidget(self.extraLabel, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignLeft|Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Binary_btn = QPushButton(self.extraCenter)
        self.Binary_btn.setObjectName(u"Binary_btn")
        self.Binary_btn.setMinimumSize(QSize(0, 45))
        self.Binary_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Binary_btn.setStyleSheet(u"background: transparent;\n"
"text-align:left;")

        self.verticalLayout_10.addWidget(self.Binary_btn)

        self.Localization_btn = QPushButton(self.extraCenter)
        self.Localization_btn.setObjectName(u"Localization_btn")
        self.Localization_btn.setMinimumSize(QSize(0, 45))
        self.Localization_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Localization_btn.setStyleSheet(u"background: transparent;\n"
"text-align:left;")

        self.verticalLayout_10.addWidget(self.Localization_btn, 0, Qt.AlignLeft)

        self.Classification_btn = QPushButton(self.extraCenter)
        self.Classification_btn.setObjectName(u"Classification_btn")
        self.Classification_btn.setMinimumSize(QSize(0, 45))
        self.Classification_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Classification_btn.setStyleSheet(u"background: transparent;\n"
"text-align:left;")

        self.verticalLayout_10.addWidget(self.Classification_btn, 0, Qt.AlignLeft)

        self.extraBottom = QFrame(self.extraCenter)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.extraBottom)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)


        self.verticalLayout_12.addWidget(self.extraCenter)


        self.extraColumLayout.addWidget(self.extraContent, 0, Qt.AlignLeft)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"background-color:#144475;\n"
"                ")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 31))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftBox = QFrame(self.rightButtons)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setMinimumSize(QSize(0, 0))
        self.leftBox.setStyleSheet(u"background-color:#144475;")
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_dorsa = QLabel(self.leftBox)
        self.label_dorsa.setObjectName(u"label_dorsa")
        self.label_dorsa.setMaximumSize(QSize(0, 16777215))
        self.label_dorsa.setPixmap(QPixmap(u"images/images/whitew.png"))
        self.label_dorsa.setScaledContents(True)
        self.label_dorsa.setMargin(-11)

        self.horizontalLayout_3.addWidget(self.label_dorsa, 0, Qt.AlignLeft)

        self.toogle_btn_2 = QPushButton(self.leftBox)
        self.toogle_btn_2.setObjectName(u"toogle_btn_2")
        self.toogle_btn_2.setMinimumSize(QSize(0, 30))
        self.toogle_btn_2.setMaximumSize(QSize(0, 30))
        icon7 = QIcon()
        icon7.addFile(u"images/icons/dots - Copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toogle_btn_2.setIcon(icon7)
        self.toogle_btn_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.toogle_btn_2)

        self.frame_login = QFrame(self.leftBox)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setMinimumSize(QSize(0, 0))
        self.frame_login.setMaximumSize(QSize(0, 40))
        self.frame_login.setStyleSheet(u"QFrame {\n"
"background-color: rgb(50,50,70);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"	border-radius:6px;\n"
"	text-align:center;\n"
"}")
        self.frame_login.setFrameShape(QFrame.Box)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_login)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_43 = QLabel(self.frame_login)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(100, 0))
        self.label_43.setMaximumSize(QSize(100, 16777215))
        self.label_43.setStyleSheet(u"color : rgb(255,255,255);")
        self.label_43.setIndent(6)

        self.horizontalLayout_34.addWidget(self.label_43)

        self.lineEdit_6 = QLineEdit(self.frame_login)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(150, 25))
        self.lineEdit_6.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_34.addWidget(self.lineEdit_6)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_44 = QLabel(self.frame_login)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(100, 0))
        self.label_44.setMaximumSize(QSize(100, 16777215))
        self.label_44.setStyleSheet(u"color : rgb(255,255,255);")
        self.label_44.setMargin(0)
        self.label_44.setIndent(17)

        self.horizontalLayout_35.addWidget(self.label_44)

        self.lineEdit_7 = QLineEdit(self.frame_login)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(100, 25))
        self.lineEdit_7.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_35.addWidget(self.lineEdit_7)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_35)

        self.pushButton_7 = QPushButton(self.frame_login)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(23, 22))
        self.pushButton_7.setMaximumSize(QSize(21, 21))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setToolTipDuration(-1)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"background-color: Transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"images/enter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.horizontalLayout_36.addWidget(self.pushButton_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_51 = QLabel(self.frame_login)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"color : rgb(255,255,255);")

        self.horizontalLayout_36.addWidget(self.label_51)


        self.horizontalLayout_3.addWidget(self.frame_login)


        self.horizontalLayout_2.addWidget(self.leftBox)

        self.horizontalSpacer_2 = QSpacerItem(2000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.miniButton = QPushButton(self.rightButtons)
        self.miniButton.setObjectName(u"miniButton")
        self.miniButton.setMinimumSize(QSize(28, 28))
        self.miniButton.setMaximumSize(QSize(28, 28))
        self.miniButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u"images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.miniButton.setIcon(icon9)
        self.miniButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.miniButton)

        self.maxiButton = QPushButton(self.rightButtons)
        self.maxiButton.setObjectName(u"maxiButton")
        self.maxiButton.setMinimumSize(QSize(28, 28))
        self.maxiButton.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maxiButton.setFont(font1)
        self.maxiButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u"images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxiButton.setIcon(icon10)
        self.maxiButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maxiButton)

        self.closeButton = QPushButton(self.rightButtons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(28, 28))
        self.closeButton.setMaximumSize(QSize(28, 28))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u"images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon11)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_settin2 = QFrame(self.contentBottom)
        self.frame_settin2.setObjectName(u"frame_settin2")
        self.frame_settin2.setMinimumSize(QSize(0, 0))
        self.frame_settin2.setMaximumSize(QSize(16777215, 0))
        self.frame_settin2.setStyleSheet(u"background-color: rgb(33, 37, 50);")
        self.frame_settin2.setFrameShape(QFrame.StyledPanel)
        self.frame_settin2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_settin2)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_8)

        self.btn_software_setting = QPushButton(self.frame_settin2)
        self.btn_software_setting.setObjectName(u"btn_software_setting")
        self.btn_software_setting.setMinimumSize(QSize(150, 0))
        self.btn_software_setting.setMaximumSize(QSize(150, 16777215))
        self.btn_software_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_software_setting.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_37.addWidget(self.btn_software_setting)

        self.pushButton_9 = QPushButton(self.frame_settin2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(150, 0))
        self.pushButton_9.setMaximumSize(QSize(150, 16777215))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_9)

        self.pushButton_15 = QPushButton(self.frame_settin2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(150, 0))
        self.pushButton_15.setMaximumSize(QSize(150, 16777215))
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.frame_settin2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(150, 0))
        self.pushButton_16.setMaximumSize(QSize(150, 16777215))
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.frame_settin2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(150, 0))
        self.pushButton_17.setMaximumSize(QSize(150, 16777215))
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70,70,70);\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"\n"
"	text-align: center;\n"
"	border-radius:3px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(150,150,150);\n"
"    color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_17)


        self.verticalLayout_6.addWidget(self.frame_settin2)

        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setToolTipDuration(-1)
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.pagesContainer.setLineWidth(1)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color : #F3F6FE;")
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.page_dashboard.setStyleSheet(u"color : rgb(20,20,20);")
        self.verticalLayout_7 = QVBoxLayout(self.page_dashboard)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_14 = QFrame(self.page_dashboard)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 500))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_16)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.camera_1 = QLabel(self.frame_16)
        self.camera_1.setObjectName(u"camera_1")
        self.camera_1.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.camera_1)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(50, 42))
        self.frame_18.setMaximumSize(QSize(158, 42))
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.fullscreen_cam_1 = QPushButton(self.frame_18)
        self.fullscreen_cam_1.setObjectName(u"fullscreen_cam_1")
        self.fullscreen_cam_1.setMaximumSize(QSize(50, 50))
        self.fullscreen_cam_1.setStyleSheet(u"border:None;")
        icon12 = QIcon()
        icon12.addFile(u"images/full-screen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreen_cam_1.setIcon(icon12)
        self.fullscreen_cam_1.setIconSize(QSize(40, 40))

        self.horizontalLayout_14.addWidget(self.fullscreen_cam_1)

        self.save_cam1_btn = QPushButton(self.frame_18)
        self.save_cam1_btn.setObjectName(u"save_cam1_btn")
        self.save_cam1_btn.setMaximumSize(QSize(50, 50))
        self.save_cam1_btn.setStyleSheet(u"border:None;")
        icon13 = QIcon()
        icon13.addFile(u"images/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_cam1_btn.setIcon(icon13)
        self.save_cam1_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_14.addWidget(self.save_cam1_btn)

        self.load_cam1_btn = QPushButton(self.frame_18)
        self.load_cam1_btn.setObjectName(u"load_cam1_btn")
        self.load_cam1_btn.setMaximumSize(QSize(50, 50))
        self.load_cam1_btn.setStyleSheet(u"border:None;")
        icon14 = QIcon()
        icon14.addFile(u"images/upload-big-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.load_cam1_btn.setIcon(icon14)
        self.load_cam1_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_14.addWidget(self.load_cam1_btn)


        self.verticalLayout_4.addWidget(self.frame_18, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_17)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.camera_2 = QLabel(self.frame_17)
        self.camera_2.setObjectName(u"camera_2")
        self.camera_2.setPixmap(QPixmap(u"images/camera.png"))
        self.camera_2.setScaledContents(True)

        self.verticalLayout_20.addWidget(self.camera_2)

        self.frame_22 = QFrame(self.frame_17)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(50, 42))
        self.frame_22.setMaximumSize(QSize(158, 42))
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.fullscreen_cam2 = QPushButton(self.frame_22)
        self.fullscreen_cam2.setObjectName(u"fullscreen_cam2")
        self.fullscreen_cam2.setMaximumSize(QSize(50, 50))
        self.fullscreen_cam2.setStyleSheet(u"border:None;")
        self.fullscreen_cam2.setIcon(icon12)
        self.fullscreen_cam2.setIconSize(QSize(40, 40))

        self.horizontalLayout_18.addWidget(self.fullscreen_cam2)

        self.save_cam2_btn = QPushButton(self.frame_22)
        self.save_cam2_btn.setObjectName(u"save_cam2_btn")
        self.save_cam2_btn.setMaximumSize(QSize(50, 50))
        self.save_cam2_btn.setStyleSheet(u"border:None;")
        self.save_cam2_btn.setIcon(icon13)
        self.save_cam2_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_18.addWidget(self.save_cam2_btn)

        self.load_cam2_btn = QPushButton(self.frame_22)
        self.load_cam2_btn.setObjectName(u"load_cam2_btn")
        self.load_cam2_btn.setMaximumSize(QSize(50, 50))
        self.load_cam2_btn.setStyleSheet(u"border:None;")
        self.load_cam2_btn.setIcon(icon14)
        self.load_cam2_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_18.addWidget(self.load_cam2_btn)


        self.verticalLayout_20.addWidget(self.frame_22, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.frame_17)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.page_dashboard)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 200))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_users_setting = QWidget()
        self.page_users_setting.setObjectName(u"page_users_setting")
        self.horizontalLayout_6 = QHBoxLayout(self.page_users_setting)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_19 = QFrame(self.page_users_setting)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(280, 16777215))
        self.frame_19.setStyleSheet(u"")
        self.frame_19.setFrameShape(QFrame.Box)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_19)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_19)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border:Transparent")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 69, 69))
        self.horizontalLayout_29 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.tableWidget_users = QTableWidget(self.scrollAreaWidgetContents_3)
        if (self.tableWidget_users.columnCount() < 2):
            self.tableWidget_users.setColumnCount(2)
        self.tableWidget_users.setObjectName(u"tableWidget_users")
        self.tableWidget_users.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_users.setProperty("showDropIndicator", False)
        self.tableWidget_users.setDragDropOverwriteMode(False)
        self.tableWidget_users.setColumnCount(2)

        self.horizontalLayout_29.addWidget(self.tableWidget_users)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_44.addWidget(self.scrollArea)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(270, 38))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.add_user_btn = QPushButton(self.frame_21)
        self.add_user_btn.setObjectName(u"add_user_btn")
        self.add_user_btn.setMinimumSize(QSize(0, 30))
        self.add_user_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_user_btn.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_28.addWidget(self.add_user_btn)

        self.add_user_btn_2 = QPushButton(self.frame_21)
        self.add_user_btn_2.setObjectName(u"add_user_btn_2")
        self.add_user_btn_2.setMinimumSize(QSize(0, 30))
        self.add_user_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_user_btn_2.setStyleSheet(u"QPushButton{\n"
"background: #78AD40;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_28.addWidget(self.add_user_btn_2)

        self.remove_user_btn = QPushButton(self.frame_21)
        self.remove_user_btn.setObjectName(u"remove_user_btn")
        self.remove_user_btn.setMinimumSize(QSize(0, 30))
        self.remove_user_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_user_btn.setStyleSheet(u"QPushButton{\n"
"background: #FF1111;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_28.addWidget(self.remove_user_btn)


        self.verticalLayout_44.addWidget(self.frame_21, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_19)

        self.frame_add_user = QFrame(self.page_users_setting)
        self.frame_add_user.setObjectName(u"frame_add_user")
        self.frame_add_user.setMinimumSize(QSize(270, 0))
        self.frame_add_user.setMaximumSize(QSize(0, 16777215))
        self.frame_add_user.setFrameShape(QFrame.StyledPanel)
        self.frame_add_user.setFrameShadow(QFrame.Sunken)
        self.frame_add_user.setLineWidth(7)
        self.frame_add_user.setMidLineWidth(4)
        self.verticalLayout_46 = QVBoxLayout(self.frame_add_user)
        self.verticalLayout_46.setSpacing(7)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(10, 10, 10, 10)
        self.groupBox = QGroupBox(self.frame_add_user)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_47 = QVBoxLayout(self.groupBox)
        self.verticalLayout_47.setSpacing(10)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 10, 0, 0)
        self.frame_42 = QFrame(self.groupBox)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(16777215, 35))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.frame_42)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_30.addWidget(self.label_64)

        self.user_id = QLineEdit(self.frame_42)
        self.user_id.setObjectName(u"user_id")
        self.user_id.setMinimumSize(QSize(0, 30))
        self.user_id.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")

        self.horizontalLayout_30.addWidget(self.user_id, 0, Qt.AlignRight)


        self.verticalLayout_47.addWidget(self.frame_42)

        self.frame_44 = QFrame(self.groupBox)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(0, 35))
        self.frame_44.setMaximumSize(QSize(16777215, 35))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.frame_44)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_32.addWidget(self.label_66)

        self.user_pass = QLineEdit(self.frame_44)
        self.user_pass.setObjectName(u"user_pass")
        self.user_pass.setMinimumSize(QSize(0, 30))
        self.user_pass.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")
        self.user_pass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_32.addWidget(self.user_pass, 0, Qt.AlignRight)


        self.verticalLayout_47.addWidget(self.frame_44)

        self.frame_43 = QFrame(self.groupBox)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 35))
        self.frame_43.setMaximumSize(QSize(16777215, 30))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.frame_43)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_31.addWidget(self.label_65)

        self.user_re_pass = QLineEdit(self.frame_43)
        self.user_re_pass.setObjectName(u"user_re_pass")
        self.user_re_pass.setMinimumSize(QSize(0, 30))
        self.user_re_pass.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")
        self.user_re_pass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_31.addWidget(self.user_re_pass, 0, Qt.AlignRight)


        self.verticalLayout_47.addWidget(self.frame_43)

        self.frame_47 = QFrame(self.groupBox)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 35))
        self.frame_47.setMaximumSize(QSize(16777215, 30))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.frame_47)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_33.addWidget(self.label_67)

        self.user_role = QComboBox(self.frame_47)
        self.user_role.setObjectName(u"user_role")
        self.user_role.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_33.addWidget(self.user_role, 0, Qt.AlignRight)


        self.verticalLayout_47.addWidget(self.frame_47)


        self.verticalLayout_46.addWidget(self.groupBox, 0, Qt.AlignTop)

        self.frame_46 = QFrame(self.frame_add_user)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 43))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.create_user = QPushButton(self.frame_46)
        self.create_user.setObjectName(u"create_user")
        self.create_user.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        self.create_user.setFont(font2)
        self.create_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_user.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_38.addWidget(self.create_user)


        self.verticalLayout_46.addWidget(self.frame_46)

        self.frame_48 = QFrame(self.frame_add_user)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 33))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_48)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.create_user_message = QLabel(self.frame_48)
        self.create_user_message.setObjectName(u"create_user_message")

        self.verticalLayout_48.addWidget(self.create_user_message, 0, Qt.AlignHCenter)


        self.verticalLayout_46.addWidget(self.frame_48)


        self.horizontalLayout_6.addWidget(self.frame_add_user, 0, Qt.AlignTop)

        self.frame_20 = QFrame(self.page_users_setting)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(77, 0))
        self.frame_20.setFrameShape(QFrame.Panel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_20.setLineWidth(2)
        self.verticalLayout_45 = QVBoxLayout(self.frame_20)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_52 = QLabel(self.frame_20)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_45.addWidget(self.label_52)

        self.tableWidget_2 = QTableWidget(self.frame_20)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setColumnCount(7)

        self.verticalLayout_45.addWidget(self.tableWidget_2)


        self.horizontalLayout_6.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.page_users_setting)
        self.page_camera_setting = QWidget()
        self.page_camera_setting.setObjectName(u"page_camera_setting")
        self.horizontalLayout_9 = QHBoxLayout(self.page_camera_setting)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_6 = QFrame(self.page_camera_setting)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(260, 600))
        self.frame_6.setMaximumSize(QSize(260, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_24 = QVBoxLayout(self.frame_6)
        self.verticalLayout_24.setSpacing(4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 17)
        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(87, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 105))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_12)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 95))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(8)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_25 = QLabel(self.frame_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_26)


        self.verticalLayout_16.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_2)


        self.verticalLayout_16.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.camera01_btn = QPushButton(self.frame_3)
        self.camera01_btn.setObjectName(u"camera01_btn")
        self.camera01_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera01_btn.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        icon15 = QIcon()
        icon15.addFile(u"images/camtop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.camera01_btn.setIcon(icon15)
        self.camera01_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_13.addWidget(self.camera01_btn)

        self.camera02_btn = QPushButton(self.frame_3)
        self.camera02_btn.setObjectName(u"camera02_btn")
        self.camera02_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera02_btn.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        self.camera02_btn.setIcon(icon15)
        self.camera02_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_13.addWidget(self.camera02_btn)


        self.verticalLayout_16.addLayout(self.horizontalLayout_13)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.line_3 = QFrame(self.frame_12)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Raised)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_17.addWidget(self.line_3)


        self.verticalLayout_24.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(246, 33))
        self.frame_9.setMaximumSize(QSize(200, 20))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.label_53 = QLabel(self.frame_9)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(80, 0))
        self.label_53.setMaximumSize(QSize(80, 16777215))
        font3 = QFont()
        font3.setBold(True)
        self.label_53.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_53)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.cameraname_label = QLabel(self.frame_9)
        self.cameraname_label.setObjectName(u"cameraname_label")
        self.cameraname_label.setMinimumSize(QSize(120, 0))
        self.cameraname_label.setMaximumSize(QSize(100, 16777215))
        self.cameraname_label.setFont(font3)
        self.cameraname_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.cameraname_label)


        self.verticalLayout_24.addWidget(self.frame_9)

        self.line_2 = QFrame(self.frame_6)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(250, 0))
        self.line_2.setMaximumSize(QSize(250, 16777215))
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_24.addWidget(self.line_2)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(250, 400))
        self.frame_10.setMaximumSize(QSize(250, 100000))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gain_label_2 = QLabel(self.frame_10)
        self.gain_label_2.setObjectName(u"gain_label_2")
        self.gain_label_2.setMinimumSize(QSize(120, 30))
        self.gain_label_2.setMaximumSize(QSize(120, 30))
        self.gain_label_2.setFont(font)

        self.verticalLayout_19.addWidget(self.gain_label_2)

        self.gain_label = QLabel(self.frame_10)
        self.gain_label.setObjectName(u"gain_label")
        self.gain_label.setMinimumSize(QSize(120, 30))
        self.gain_label.setMaximumSize(QSize(120, 30))
        self.gain_label.setFont(font)

        self.verticalLayout_19.addWidget(self.gain_label)

        self.expo_label = QLabel(self.frame_10)
        self.expo_label.setObjectName(u"expo_label")
        self.expo_label.setMinimumSize(QSize(120, 30))
        self.expo_label.setMaximumSize(QSize(120, 30))
        self.expo_label.setFont(font)

        self.verticalLayout_19.addWidget(self.expo_label)

        self.width_label = QLabel(self.frame_10)
        self.width_label.setObjectName(u"width_label")
        self.width_label.setMinimumSize(QSize(120, 30))
        self.width_label.setMaximumSize(QSize(120, 30))
        self.width_label.setFont(font)

        self.verticalLayout_19.addWidget(self.width_label)

        self.height_label = QLabel(self.frame_10)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setMinimumSize(QSize(120, 30))
        self.height_label.setMaximumSize(QSize(120, 30))
        self.height_label.setFont(font)

        self.verticalLayout_19.addWidget(self.height_label)

        self.offsetx_label = QLabel(self.frame_10)
        self.offsetx_label.setObjectName(u"offsetx_label")
        self.offsetx_label.setMinimumSize(QSize(120, 30))
        self.offsetx_label.setMaximumSize(QSize(120, 30))
        self.offsetx_label.setFont(font)

        self.verticalLayout_19.addWidget(self.offsetx_label)

        self.offsety_label = QLabel(self.frame_10)
        self.offsety_label.setObjectName(u"offsety_label")
        self.offsety_label.setMinimumSize(QSize(120, 30))
        self.offsety_label.setMaximumSize(QSize(120, 30))
        self.offsety_label.setFont(font)

        self.verticalLayout_19.addWidget(self.offsety_label)

        self.trigger_label = QLabel(self.frame_10)
        self.trigger_label.setObjectName(u"trigger_label")
        self.trigger_label.setMinimumSize(QSize(120, 30))
        self.trigger_label.setMaximumSize(QSize(120, 30))
        self.trigger_label.setFont(font)

        self.verticalLayout_19.addWidget(self.trigger_label)

        self.maxbuffer_label = QLabel(self.frame_10)
        self.maxbuffer_label.setObjectName(u"maxbuffer_label")
        self.maxbuffer_label.setMinimumSize(QSize(120, 30))
        self.maxbuffer_label.setMaximumSize(QSize(120, 30))
        self.maxbuffer_label.setFont(font)

        self.verticalLayout_19.addWidget(self.maxbuffer_label)

        self.packetdelay_label = QLabel(self.frame_10)
        self.packetdelay_label.setObjectName(u"packetdelay_label")
        self.packetdelay_label.setMinimumSize(QSize(120, 30))
        self.packetdelay_label.setMaximumSize(QSize(120, 30))
        self.packetdelay_label.setFont(font)

        self.verticalLayout_19.addWidget(self.packetdelay_label)

        self.packetsize_label = QLabel(self.frame_10)
        self.packetsize_label.setObjectName(u"packetsize_label")
        self.packetsize_label.setMinimumSize(QSize(120, 30))
        self.packetsize_label.setMaximumSize(QSize(120, 30))
        self.packetsize_label.setFont(font)

        self.verticalLayout_19.addWidget(self.packetsize_label)

        self.transmissiondelay_label = QLabel(self.frame_10)
        self.transmissiondelay_label.setObjectName(u"transmissiondelay_label")
        self.transmissiondelay_label.setMinimumSize(QSize(120, 30))
        self.transmissiondelay_label.setMaximumSize(QSize(120, 30))
        self.transmissiondelay_label.setFont(font)

        self.verticalLayout_19.addWidget(self.transmissiondelay_label)

        self.transmissiondelay_label_2 = QLabel(self.frame_10)
        self.transmissiondelay_label_2.setObjectName(u"transmissiondelay_label_2")
        self.transmissiondelay_label_2.setMinimumSize(QSize(120, 30))
        self.transmissiondelay_label_2.setMaximumSize(QSize(120, 30))
        self.transmissiondelay_label_2.setFont(font)

        self.verticalLayout_19.addWidget(self.transmissiondelay_label_2)


        self.horizontalLayout_10.addLayout(self.verticalLayout_19)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.serial_number_combo = QComboBox(self.frame_10)
        self.serial_number_combo.setObjectName(u"serial_number_combo")
        self.serial_number_combo.setEnabled(False)
        self.serial_number_combo.setMinimumSize(QSize(100, 30))
        self.serial_number_combo.setMaximumSize(QSize(100, 30))
        self.serial_number_combo.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_21.addWidget(self.serial_number_combo)

        self.gain_spinbox = QSpinBox(self.frame_10)
        self.gain_spinbox.setObjectName(u"gain_spinbox")
        self.gain_spinbox.setEnabled(False)
        self.gain_spinbox.setMinimumSize(QSize(100, 30))
        self.gain_spinbox.setMaximumSize(QSize(100, 30))
        self.gain_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.gain_spinbox.setAlignment(Qt.AlignCenter)
        self.gain_spinbox.setMaximum(360)
        self.gain_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.gain_spinbox)

        self.expo_spinbox = QSpinBox(self.frame_10)
        self.expo_spinbox.setObjectName(u"expo_spinbox")
        self.expo_spinbox.setEnabled(False)
        self.expo_spinbox.setMinimumSize(QSize(100, 30))
        self.expo_spinbox.setMaximumSize(QSize(100, 30))
        self.expo_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.expo_spinbox.setAlignment(Qt.AlignCenter)
        self.expo_spinbox.setMinimum(35)
        self.expo_spinbox.setMaximum(10000000)
        self.expo_spinbox.setSingleStep(1)
        self.expo_spinbox.setValue(3000)

        self.verticalLayout_21.addWidget(self.expo_spinbox)

        self.width_spinbox = QSpinBox(self.frame_10)
        self.width_spinbox.setObjectName(u"width_spinbox")
        self.width_spinbox.setEnabled(False)
        self.width_spinbox.setMinimumSize(QSize(100, 30))
        self.width_spinbox.setMaximumSize(QSize(100, 30))
        self.width_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.width_spinbox.setAlignment(Qt.AlignCenter)
        self.width_spinbox.setMinimum(10)
        self.width_spinbox.setMaximum(1920)
        self.width_spinbox.setSingleStep(1)
        self.width_spinbox.setValue(1920)

        self.verticalLayout_21.addWidget(self.width_spinbox)

        self.height_spinbox = QSpinBox(self.frame_10)
        self.height_spinbox.setObjectName(u"height_spinbox")
        self.height_spinbox.setEnabled(False)
        self.height_spinbox.setMinimumSize(QSize(100, 30))
        self.height_spinbox.setMaximumSize(QSize(100, 30))
        self.height_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.height_spinbox.setAlignment(Qt.AlignCenter)
        self.height_spinbox.setMinimum(10)
        self.height_spinbox.setMaximum(1200)
        self.height_spinbox.setSingleStep(1)
        self.height_spinbox.setValue(1200)

        self.verticalLayout_21.addWidget(self.height_spinbox)

        self.offsetx_spinbox = QSpinBox(self.frame_10)
        self.offsetx_spinbox.setObjectName(u"offsetx_spinbox")
        self.offsetx_spinbox.setEnabled(False)
        self.offsetx_spinbox.setMinimumSize(QSize(100, 30))
        self.offsetx_spinbox.setMaximumSize(QSize(100, 30))
        self.offsetx_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.offsetx_spinbox.setAlignment(Qt.AlignCenter)
        self.offsetx_spinbox.setMaximum(16)
        self.offsetx_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.offsetx_spinbox)

        self.offsety_spinbox = QSpinBox(self.frame_10)
        self.offsety_spinbox.setObjectName(u"offsety_spinbox")
        self.offsety_spinbox.setEnabled(False)
        self.offsety_spinbox.setMinimumSize(QSize(100, 30))
        self.offsety_spinbox.setMaximumSize(QSize(100, 30))
        self.offsety_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.offsety_spinbox.setAlignment(Qt.AlignCenter)
        self.offsety_spinbox.setMaximum(16)
        self.offsety_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.offsety_spinbox)

        self.trigger_combo = QComboBox(self.frame_10)
        self.trigger_combo.addItem("")
        self.trigger_combo.addItem("")
        self.trigger_combo.setObjectName(u"trigger_combo")
        self.trigger_combo.setEnabled(False)
        self.trigger_combo.setMinimumSize(QSize(100, 30))
        self.trigger_combo.setMaximumSize(QSize(100, 30))
        self.trigger_combo.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_21.addWidget(self.trigger_combo)

        self.maxbuffer_spinbox = QSpinBox(self.frame_10)
        self.maxbuffer_spinbox.setObjectName(u"maxbuffer_spinbox")
        self.maxbuffer_spinbox.setEnabled(False)
        self.maxbuffer_spinbox.setMinimumSize(QSize(100, 30))
        self.maxbuffer_spinbox.setMaximumSize(QSize(100, 30))
        self.maxbuffer_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.maxbuffer_spinbox.setAlignment(Qt.AlignCenter)
        self.maxbuffer_spinbox.setMaximum(360)
        self.maxbuffer_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.maxbuffer_spinbox)

        self.packetdelay_spinbox = QSpinBox(self.frame_10)
        self.packetdelay_spinbox.setObjectName(u"packetdelay_spinbox")
        self.packetdelay_spinbox.setEnabled(False)
        self.packetdelay_spinbox.setMinimumSize(QSize(100, 30))
        self.packetdelay_spinbox.setMaximumSize(QSize(100, 30))
        self.packetdelay_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.packetdelay_spinbox.setAlignment(Qt.AlignCenter)
        self.packetdelay_spinbox.setMaximum(360)
        self.packetdelay_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.packetdelay_spinbox)

        self.packetsize_spinbox = QSpinBox(self.frame_10)
        self.packetsize_spinbox.setObjectName(u"packetsize_spinbox")
        self.packetsize_spinbox.setEnabled(False)
        self.packetsize_spinbox.setMinimumSize(QSize(100, 30))
        self.packetsize_spinbox.setMaximumSize(QSize(100, 30))
        self.packetsize_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.packetsize_spinbox.setAlignment(Qt.AlignCenter)
        self.packetsize_spinbox.setMaximum(360)
        self.packetsize_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.packetsize_spinbox)

        self.transmissiondelay_spinbox = QSpinBox(self.frame_10)
        self.transmissiondelay_spinbox.setObjectName(u"transmissiondelay_spinbox")
        self.transmissiondelay_spinbox.setEnabled(False)
        self.transmissiondelay_spinbox.setMinimumSize(QSize(100, 30))
        self.transmissiondelay_spinbox.setMaximumSize(QSize(100, 30))
        self.transmissiondelay_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.transmissiondelay_spinbox.setAlignment(Qt.AlignCenter)
        self.transmissiondelay_spinbox.setMaximum(360)
        self.transmissiondelay_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.transmissiondelay_spinbox)

        self.ip_lineedit = QLineEdit(self.frame_10)
        self.ip_lineedit.setObjectName(u"ip_lineedit")
        self.ip_lineedit.setEnabled(True)
        self.ip_lineedit.setMinimumSize(QSize(100, 30))
        self.ip_lineedit.setMaximumSize(QSize(100, 30))
        self.ip_lineedit.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")
        self.ip_lineedit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.ip_lineedit)


        self.horizontalLayout_10.addLayout(self.verticalLayout_21)


        self.verticalLayout_24.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_11)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.camera_setting_apply_btn = QPushButton(self.frame_11)
        self.camera_setting_apply_btn.setObjectName(u"camera_setting_apply_btn")
        self.camera_setting_apply_btn.setEnabled(False)
        self.camera_setting_apply_btn.setMinimumSize(QSize(0, 30))
        self.camera_setting_apply_btn.setMaximumSize(QSize(16777215, 30))
        self.camera_setting_apply_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_setting_apply_btn.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_70.addWidget(self.camera_setting_apply_btn)

        self.frame_99 = QFrame(self.frame_11)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(0, 50))
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.camera_setting_connect_btn = QPushButton(self.frame_99)
        self.camera_setting_connect_btn.setObjectName(u"camera_setting_connect_btn")
        self.camera_setting_connect_btn.setEnabled(False)
        self.camera_setting_connect_btn.setMinimumSize(QSize(0, 30))
        self.camera_setting_connect_btn.setMaximumSize(QSize(16777215, 30))
        self.camera_setting_connect_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_setting_connect_btn.setStyleSheet(u"QPushButton{\n"
"background: #78AD40;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_12.addWidget(self.camera_setting_connect_btn)

        self.camera_setting_getpic_btn = QPushButton(self.frame_99)
        self.camera_setting_getpic_btn.setObjectName(u"camera_setting_getpic_btn")
        self.camera_setting_getpic_btn.setEnabled(False)
        self.camera_setting_getpic_btn.setMinimumSize(QSize(0, 30))
        self.camera_setting_getpic_btn.setMaximumSize(QSize(16777215, 30))
        self.camera_setting_getpic_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_setting_getpic_btn.setStyleSheet(u"QPushButton{\n"
"background: #78AD40;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_12.addWidget(self.camera_setting_getpic_btn)


        self.verticalLayout_70.addWidget(self.frame_99)


        self.verticalLayout_24.addWidget(self.frame_11)

        self.camera_setting_message_label = QLabel(self.frame_6)
        self.camera_setting_message_label.setObjectName(u"camera_setting_message_label")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.camera_setting_message_label.setFont(font4)
        self.camera_setting_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.camera_setting_message_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_2)


        self.horizontalLayout_9.addWidget(self.frame_6)

        self.line_4 = QFrame(self.page_camera_setting)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.line_4)

        self.frame_7 = QFrame(self.page_camera_setting)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(500, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_8)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.camera_setting_picture_label = QLabel(self.frame_8)
        self.camera_setting_picture_label.setObjectName(u"camera_setting_picture_label")
        self.camera_setting_picture_label.setMinimumSize(QSize(600, 400))
        self.camera_setting_picture_label.setFrameShape(QFrame.Box)
        self.camera_setting_picture_label.setFrameShadow(QFrame.Sunken)
        self.camera_setting_picture_label.setLineWidth(2)
        self.camera_setting_picture_label.setPixmap(QPixmap(u"images/camera.png"))
        self.camera_setting_picture_label.setScaledContents(False)
        self.camera_setting_picture_label.setMargin(13)
        self.camera_setting_picture_label.setIndent(-1)

        self.verticalLayout_25.addWidget(self.camera_setting_picture_label)


        self.verticalLayout_18.addWidget(self.frame_8)


        self.horizontalLayout_9.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_camera_setting)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_22 = QVBoxLayout(self.page_settings)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_92 = QFrame(self.page_settings)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.frame_93 = QFrame(self.frame_92)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMaximumSize(QSize(650, 16777215))
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_108 = QFrame(self.frame_93)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMaximumSize(QSize(320, 16777215))
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_108)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.groupBox_4 = QGroupBox(self.frame_108)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(300, 16777215))
        self.groupBox_4.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_75 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(10, 10, 10, 10)
        self.frame_91 = QFrame(self.groupBox_4)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(0, 200))
        self.frame_91.setMaximumSize(QSize(500, 200))
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_91)
        self.verticalLayout_72.setSpacing(10)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.frame_89 = QFrame(self.frame_91)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(0, 30))
        self.frame_89.setMaximumSize(QSize(500, 30))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_97 = QLabel(self.frame_89)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(70, 0))
        self.label_97.setMaximumSize(QSize(70, 16777215))
        font5 = QFont()
        font5.setPointSize(10)
        self.label_97.setFont(font5)

        self.horizontalLayout_66.addWidget(self.label_97)

        self.setting_style_comboBox = QComboBox(self.frame_89)
        self.setting_style_comboBox.setObjectName(u"setting_style_comboBox")
        self.setting_style_comboBox.setMinimumSize(QSize(150, 40))
        self.setting_style_comboBox.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_66.addWidget(self.setting_style_comboBox)


        self.verticalLayout_72.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.frame_91)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(0, 30))
        self.frame_90.setMaximumSize(QSize(500, 30))
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_98 = QLabel(self.frame_90)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(70, 0))
        self.label_98.setMaximumSize(QSize(70, 16777215))
        self.label_98.setFont(font5)

        self.horizontalLayout_67.addWidget(self.label_98)

        self.setting_color_comboBox = QComboBox(self.frame_90)
        self.setting_color_comboBox.setObjectName(u"setting_color_comboBox")
        self.setting_color_comboBox.setMinimumSize(QSize(150, 30))
        self.setting_color_comboBox.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_67.addWidget(self.setting_color_comboBox)


        self.verticalLayout_72.addWidget(self.frame_90)

        self.frame_5 = QFrame(self.frame_91)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 30))
        self.frame_5.setMaximumSize(QSize(500, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_5)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(70, 0))
        self.label_57.setMaximumSize(QSize(70, 16777215))
        self.label_57.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_57)

        self.setting_fontstyle_comboBox = QComboBox(self.frame_5)
        self.setting_fontstyle_comboBox.setObjectName(u"setting_fontstyle_comboBox")
        self.setting_fontstyle_comboBox.setMinimumSize(QSize(150, 30))
        self.setting_fontstyle_comboBox.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_8.addWidget(self.setting_fontstyle_comboBox)


        self.verticalLayout_72.addWidget(self.frame_5)

        self.frame_87 = QFrame(self.frame_91)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(0, 30))
        self.frame_87.setMaximumSize(QSize(500, 30))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_95 = QLabel(self.frame_87)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(70, 0))
        self.label_95.setMaximumSize(QSize(70, 16777215))
        self.label_95.setFont(font5)

        self.horizontalLayout_64.addWidget(self.label_95)

        self.setting_fontsize_comboBox = QComboBox(self.frame_87)
        self.setting_fontsize_comboBox.setObjectName(u"setting_fontsize_comboBox")
        self.setting_fontsize_comboBox.setMinimumSize(QSize(150, 30))
        self.setting_fontsize_comboBox.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_64.addWidget(self.setting_fontsize_comboBox)


        self.verticalLayout_72.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.frame_91)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(0, 30))
        self.frame_88.setMaximumSize(QSize(500, 30))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_96 = QLabel(self.frame_88)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(70, 0))
        self.label_96.setMaximumSize(QSize(70, 16777215))
        self.label_96.setFont(font5)

        self.horizontalLayout_65.addWidget(self.label_96)

        self.setting_language_comboBox = QComboBox(self.frame_88)
        self.setting_language_comboBox.setObjectName(u"setting_language_comboBox")
        self.setting_language_comboBox.setMinimumSize(QSize(150, 30))
        self.setting_language_comboBox.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_65.addWidget(self.setting_language_comboBox)


        self.verticalLayout_72.addWidget(self.frame_88)


        self.verticalLayout_75.addWidget(self.frame_91)

        self.frame_97 = QFrame(self.groupBox_4)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMinimumSize(QSize(0, 60))
        self.frame_97.setMaximumSize(QSize(500, 60))
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_97)
        self.verticalLayout_76.setSpacing(10)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.setting_appearance_apply_btn = QPushButton(self.frame_97)
        self.setting_appearance_apply_btn.setObjectName(u"setting_appearance_apply_btn")
        self.setting_appearance_apply_btn.setMinimumSize(QSize(0, 30))
        self.setting_appearance_apply_btn.setMaximumSize(QSize(500, 30))
        self.setting_appearance_apply_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_appearance_apply_btn.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_76.addWidget(self.setting_appearance_apply_btn)

        self.general_setting_appearance_message_label = QLabel(self.frame_97)
        self.general_setting_appearance_message_label.setObjectName(u"general_setting_appearance_message_label")
        self.general_setting_appearance_message_label.setMinimumSize(QSize(0, 20))
        self.general_setting_appearance_message_label.setMaximumSize(QSize(500, 20))
        self.general_setting_appearance_message_label.setFont(font4)
        self.general_setting_appearance_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.general_setting_appearance_message_label)


        self.verticalLayout_75.addWidget(self.frame_97)


        self.verticalLayout_84.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame_108)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_78 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.frame_94 = QFrame(self.groupBox_5)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(276, 200))
        self.frame_94.setMaximumSize(QSize(230, 200))
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_94)
        self.verticalLayout_74.setSpacing(10)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.frame_95 = QFrame(self.frame_94)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(276, 30))
        self.frame_95.setMaximumSize(QSize(220, 30))
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_95)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_99 = QLabel(self.frame_95)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMinimumSize(QSize(70, 0))
        self.label_99.setMaximumSize(QSize(70, 16777215))
        self.label_99.setFont(font5)
        self.label_99.setLayoutDirection(Qt.LeftToRight)
        self.label_99.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.label_99)

        self.defect_colors_number_spin = QSpinBox(self.frame_95)
        self.defect_colors_number_spin.setObjectName(u"defect_colors_number_spin")
        self.defect_colors_number_spin.setMinimumSize(QSize(80, 30))
        self.defect_colors_number_spin.setMaximumSize(QSize(80, 16777215))
        self.defect_colors_number_spin.setMinimum(3)
        self.defect_colors_number_spin.setMaximum(99)
        self.defect_colors_number_spin.setSingleStep(3)

        self.horizontalLayout_69.addWidget(self.defect_colors_number_spin)


        self.verticalLayout_74.addWidget(self.frame_95)


        self.verticalLayout_78.addWidget(self.frame_94)

        self.frame_98 = QFrame(self.groupBox_5)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(0, 60))
        self.frame_98.setMaximumSize(QSize(500, 60))
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_98)
        self.verticalLayout_77.setSpacing(10)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.setting_defects_apply_btn = QPushButton(self.frame_98)
        self.setting_defects_apply_btn.setObjectName(u"setting_defects_apply_btn")
        self.setting_defects_apply_btn.setMinimumSize(QSize(0, 30))
        self.setting_defects_apply_btn.setMaximumSize(QSize(500, 25))
        self.setting_defects_apply_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_defects_apply_btn.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_77.addWidget(self.setting_defects_apply_btn)

        self.setting_defect_message_label = QLabel(self.frame_98)
        self.setting_defect_message_label.setObjectName(u"setting_defect_message_label")
        self.setting_defect_message_label.setMinimumSize(QSize(0, 20))
        self.setting_defect_message_label.setMaximumSize(QSize(500, 20))
        self.setting_defect_message_label.setFont(font5)
        self.setting_defect_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_77.addWidget(self.setting_defect_message_label)


        self.verticalLayout_78.addWidget(self.frame_98)


        self.verticalLayout_84.addWidget(self.groupBox_5)


        self.horizontalLayout_93.addWidget(self.frame_108)

        self.frame_109 = QFrame(self.frame_93)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMaximumSize(QSize(320, 16777215))
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_109)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.groupBox_14 = QGroupBox(self.frame_109)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMaximumSize(QSize(300, 16777215))
        self.groupBox_14.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_118 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(10, 10, 10, 10)
        self.frame_152 = QFrame(self.groupBox_14)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setMinimumSize(QSize(0, 200))
        self.frame_152.setMaximumSize(QSize(500, 200))
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_152)
        self.verticalLayout_119.setSpacing(10)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.frame_153 = QFrame(self.frame_152)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setMinimumSize(QSize(0, 30))
        self.frame_153.setMaximumSize(QSize(500, 30))
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_153)
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.label_129 = QLabel(self.frame_153)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(100, 0))
        self.label_129.setMaximumSize(QSize(100, 16777215))
        self.label_129.setFont(font5)

        self.horizontalLayout_100.addWidget(self.label_129)

        self.large_rect_area_label = QLineEdit(self.frame_153)
        self.large_rect_area_label.setObjectName(u"large_rect_area_label")
        self.large_rect_area_label.setMinimumSize(QSize(100, 25))
        self.large_rect_area_label.setMaximumSize(QSize(100, 25))
        self.large_rect_area_label.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")

        self.horizontalLayout_100.addWidget(self.large_rect_area_label)


        self.verticalLayout_119.addWidget(self.frame_153)

        self.frame_154 = QFrame(self.frame_152)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setMinimumSize(QSize(0, 30))
        self.frame_154.setMaximumSize(QSize(500, 30))
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_154)
        self.horizontalLayout_101.setSpacing(0)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.label_130 = QLabel(self.frame_154)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMinimumSize(QSize(100, 0))
        self.label_130.setMaximumSize(QSize(100, 16777215))
        self.label_130.setFont(font5)

        self.horizontalLayout_101.addWidget(self.label_130)

        self.small_rect_area_label = QLineEdit(self.frame_154)
        self.small_rect_area_label.setObjectName(u"small_rect_area_label")
        self.small_rect_area_label.setMinimumSize(QSize(100, 25))
        self.small_rect_area_label.setMaximumSize(QSize(100, 25))
        self.small_rect_area_label.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")

        self.horizontalLayout_101.addWidget(self.small_rect_area_label)


        self.verticalLayout_119.addWidget(self.frame_154)

        self.frame_155 = QFrame(self.frame_152)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setMinimumSize(QSize(0, 30))
        self.frame_155.setMaximumSize(QSize(500, 30))
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_155)
        self.horizontalLayout_102.setSpacing(0)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.label_131 = QLabel(self.frame_155)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMinimumSize(QSize(100, 0))
        self.label_131.setMaximumSize(QSize(100, 16777215))
        self.label_131.setFont(font5)

        self.horizontalLayout_102.addWidget(self.label_131)

        self.rect_accuracy_label = QLineEdit(self.frame_155)
        self.rect_accuracy_label.setObjectName(u"rect_accuracy_label")
        self.rect_accuracy_label.setMinimumSize(QSize(100, 25))
        self.rect_accuracy_label.setMaximumSize(QSize(100, 25))
        self.rect_accuracy_label.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")

        self.horizontalLayout_102.addWidget(self.rect_accuracy_label)


        self.verticalLayout_119.addWidget(self.frame_155)


        self.verticalLayout_118.addWidget(self.frame_152)

        self.frame_158 = QFrame(self.groupBox_14)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setMinimumSize(QSize(0, 60))
        self.frame_158.setMaximumSize(QSize(500, 60))
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_158)
        self.verticalLayout_120.setSpacing(10)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.setting_calibration_apply_btn = QPushButton(self.frame_158)
        self.setting_calibration_apply_btn.setObjectName(u"setting_calibration_apply_btn")
        self.setting_calibration_apply_btn.setMinimumSize(QSize(0, 30))
        self.setting_calibration_apply_btn.setMaximumSize(QSize(500, 30))
        self.setting_calibration_apply_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_calibration_apply_btn.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_120.addWidget(self.setting_calibration_apply_btn)

        self.general_setting_calibration_message_label = QLabel(self.frame_158)
        self.general_setting_calibration_message_label.setObjectName(u"general_setting_calibration_message_label")
        self.general_setting_calibration_message_label.setMinimumSize(QSize(0, 20))
        self.general_setting_calibration_message_label.setMaximumSize(QSize(500, 20))
        self.general_setting_calibration_message_label.setFont(font4)
        self.general_setting_calibration_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_120.addWidget(self.general_setting_calibration_message_label)


        self.verticalLayout_118.addWidget(self.frame_158)


        self.verticalLayout_117.addWidget(self.groupBox_14)

        self.groupBox_15 = QGroupBox(self.frame_109)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_121 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.frame_159 = QFrame(self.groupBox_15)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setMinimumSize(QSize(276, 200))
        self.frame_159.setMaximumSize(QSize(230, 200))
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.frame_159)
        self.verticalLayout_122.setSpacing(10)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.frame_160 = QFrame(self.frame_159)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setMinimumSize(QSize(276, 35))
        self.frame_160.setMaximumSize(QSize(220, 35))
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_105.setSpacing(0)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.label_134 = QLabel(self.frame_160)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(70, 0))
        self.label_134.setMaximumSize(QSize(70, 16777215))
        self.label_134.setFont(font5)
        self.label_134.setLayoutDirection(Qt.LeftToRight)
        self.label_134.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_105.addWidget(self.label_134)

        self.splitsizew_spinBox = QSpinBox(self.frame_160)
        self.splitsizew_spinBox.setObjectName(u"splitsizew_spinBox")
        self.splitsizew_spinBox.setMinimumSize(QSize(80, 30))
        self.splitsizew_spinBox.setMaximumSize(QSize(80, 16777215))
        self.splitsizew_spinBox.setMaximum(50)

        self.horizontalLayout_105.addWidget(self.splitsizew_spinBox)

        self.label_54 = QLabel(self.frame_160)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(10, 0))
        self.label_54.setMaximumSize(QSize(10, 16777215))
        self.label_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_105.addWidget(self.label_54)

        self.splitsizeh_spinBox = QSpinBox(self.frame_160)
        self.splitsizeh_spinBox.setObjectName(u"splitsizeh_spinBox")
        self.splitsizeh_spinBox.setMinimumSize(QSize(80, 30))
        self.splitsizeh_spinBox.setMaximumSize(QSize(80, 16777215))
        self.splitsizeh_spinBox.setMaximum(50)

        self.horizontalLayout_105.addWidget(self.splitsizeh_spinBox)


        self.verticalLayout_122.addWidget(self.frame_160)


        self.verticalLayout_121.addWidget(self.frame_159)

        self.frame_161 = QFrame(self.groupBox_15)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMinimumSize(QSize(0, 60))
        self.frame_161.setMaximumSize(QSize(500, 60))
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_161)
        self.verticalLayout_123.setSpacing(10)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.setting_imageprocessing_apply_btn = QPushButton(self.frame_161)
        self.setting_imageprocessing_apply_btn.setObjectName(u"setting_imageprocessing_apply_btn")
        self.setting_imageprocessing_apply_btn.setMinimumSize(QSize(0, 30))
        self.setting_imageprocessing_apply_btn.setMaximumSize(QSize(500, 25))
        self.setting_imageprocessing_apply_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_imageprocessing_apply_btn.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_123.addWidget(self.setting_imageprocessing_apply_btn)

        self.setting_imageprocessing_message_label = QLabel(self.frame_161)
        self.setting_imageprocessing_message_label.setObjectName(u"setting_imageprocessing_message_label")
        self.setting_imageprocessing_message_label.setMinimumSize(QSize(0, 20))
        self.setting_imageprocessing_message_label.setMaximumSize(QSize(500, 20))
        self.setting_imageprocessing_message_label.setFont(font5)

        self.verticalLayout_123.addWidget(self.setting_imageprocessing_message_label)


        self.verticalLayout_121.addWidget(self.frame_161)


        self.verticalLayout_117.addWidget(self.groupBox_15)


        self.horizontalLayout_93.addWidget(self.frame_109)


        self.horizontalLayout_68.addWidget(self.frame_93)

        self.frame_96 = QFrame(self.frame_92)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_68.addWidget(self.frame_96)


        self.verticalLayout_22.addWidget(self.frame_92)

        self.stackedWidget.addWidget(self.page_settings)
        self.page_defects = QWidget()
        self.page_defects.setObjectName(u"page_defects")
        self.verticalLayout_23 = QVBoxLayout(self.page_defects)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.groupBox_101 = QGroupBox(self.page_defects)
        self.groupBox_101.setObjectName(u"groupBox_101")
        self.groupBox_101.setMaximumSize(QSize(1600, 500))
        self.horizontalLayout_80 = QHBoxLayout(self.groupBox_101)
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 5, 0, 0)
        self.frame_112 = QFrame(self.groupBox_101)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMinimumSize(QSize(700, 0))
        self.frame_112.setMaximumSize(QSize(1000, 16777215))
        self.frame_112.setStyleSheet(u"")
        self.frame_112.setFrameShape(QFrame.Box)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_112)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.frame_112)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"border:Transparent")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 688, 69))
        self.horizontalLayout_77 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.tableWidget_defects = QTableWidget(self.scrollAreaWidgetContents_5)
        if (self.tableWidget_defects.columnCount() < 8):
            self.tableWidget_defects.setColumnCount(8)
        self.tableWidget_defects.setObjectName(u"tableWidget_defects")
        self.tableWidget_defects.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_defects.setProperty("showDropIndicator", False)
        self.tableWidget_defects.setDragDropOverwriteMode(False)
        self.tableWidget_defects.setColumnCount(8)

        self.horizontalLayout_77.addWidget(self.tableWidget_defects)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_87.addWidget(self.scrollArea_3)

        self.frame_113 = QFrame(self.frame_112)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMinimumSize(QSize(270, 38))
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_78.setSpacing(5)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.edit_defect_btn = QPushButton(self.frame_113)
        self.edit_defect_btn.setObjectName(u"edit_defect_btn")
        self.edit_defect_btn.setMinimumSize(QSize(0, 30))
        self.edit_defect_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_defect_btn.setStyleSheet(u"QPushButton{\n"
"background: #78AD40;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_78.addWidget(self.edit_defect_btn)

        self.remove_defect_btn = QPushButton(self.frame_113)
        self.remove_defect_btn.setObjectName(u"remove_defect_btn")
        self.remove_defect_btn.setMinimumSize(QSize(0, 30))
        self.remove_defect_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_defect_btn.setStyleSheet(u"QPushButton{\n"
"background: #FF1111;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_78.addWidget(self.remove_defect_btn)


        self.verticalLayout_87.addWidget(self.frame_113, 0, Qt.AlignHCenter)


        self.horizontalLayout_80.addWidget(self.frame_112)

        self.frame_add_defect_2 = QFrame(self.groupBox_101)
        self.frame_add_defect_2.setObjectName(u"frame_add_defect_2")
        self.frame_add_defect_2.setMinimumSize(QSize(270, 0))
        self.frame_add_defect_2.setMaximumSize(QSize(0, 16777215))
        self.frame_add_defect_2.setFrameShape(QFrame.StyledPanel)
        self.frame_add_defect_2.setFrameShadow(QFrame.Sunken)
        self.frame_add_defect_2.setLineWidth(7)
        self.frame_add_defect_2.setMidLineWidth(4)
        self.verticalLayout_88 = QVBoxLayout(self.frame_add_defect_2)
        self.verticalLayout_88.setSpacing(7)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(10, 10, 10, 10)
        self.groupBox_7 = QGroupBox(self.frame_add_defect_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_89 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_89.setSpacing(10)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 10, 0, 0)
        self.frame_107 = QFrame(self.groupBox_7)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMaximumSize(QSize(16777215, 35))
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_104 = QLabel(self.frame_107)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_75.addWidget(self.label_104)

        self.defect_search_name_lineedie = QLineEdit(self.frame_107)
        self.defect_search_name_lineedie.setObjectName(u"defect_search_name_lineedie")
        self.defect_search_name_lineedie.setMinimumSize(QSize(0, 30))
        self.defect_search_name_lineedie.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")

        self.horizontalLayout_75.addWidget(self.defect_search_name_lineedie, 0, Qt.AlignRight)


        self.verticalLayout_89.addWidget(self.frame_107)

        self.frame_134 = QFrame(self.groupBox_7)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setMinimumSize(QSize(0, 35))
        self.frame_134.setMaximumSize(QSize(16777215, 30))
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_134)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.label_118 = QLabel(self.frame_134)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_106.addWidget(self.label_118)

        self.defect_search_isdefect_combo = QComboBox(self.frame_134)
        self.defect_search_isdefect_combo.addItem("")
        self.defect_search_isdefect_combo.addItem("")
        self.defect_search_isdefect_combo.addItem("")
        self.defect_search_isdefect_combo.setObjectName(u"defect_search_isdefect_combo")
        self.defect_search_isdefect_combo.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_106.addWidget(self.defect_search_isdefect_combo)


        self.verticalLayout_89.addWidget(self.frame_134)

        self.frame_119 = QFrame(self.groupBox_7)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMinimumSize(QSize(0, 35))
        self.frame_119.setMaximumSize(QSize(16777215, 30))
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_119)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.label_110 = QLabel(self.frame_119)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_85.addWidget(self.label_110)

        self.defect_search_group_combo = QComboBox(self.frame_119)
        self.defect_search_group_combo.setObjectName(u"defect_search_group_combo")
        self.defect_search_group_combo.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_85.addWidget(self.defect_search_group_combo)


        self.verticalLayout_89.addWidget(self.frame_119)

        self.frame_120 = QFrame(self.groupBox_7)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMinimumSize(QSize(0, 35))
        self.frame_120.setMaximumSize(QSize(16777215, 30))
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_111 = QLabel(self.frame_120)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_86.addWidget(self.label_111)

        self.defect_search_level_comboBox = QComboBox(self.frame_120)
        self.defect_search_level_comboBox.addItem("")
        self.defect_search_level_comboBox.addItem("")
        self.defect_search_level_comboBox.addItem("")
        self.defect_search_level_comboBox.addItem("")
        self.defect_search_level_comboBox.addItem("")
        self.defect_search_level_comboBox.setObjectName(u"defect_search_level_comboBox")
        self.defect_search_level_comboBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_86.addWidget(self.defect_search_level_comboBox)


        self.verticalLayout_89.addWidget(self.frame_120)


        self.verticalLayout_88.addWidget(self.groupBox_7, 0, Qt.AlignTop)

        self.frame_122 = QFrame(self.frame_add_defect_2)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setMinimumSize(QSize(0, 43))
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_88.setSpacing(10)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.search_defect_btn = QPushButton(self.frame_122)
        self.search_defect_btn.setObjectName(u"search_defect_btn")
        self.search_defect_btn.setMinimumSize(QSize(0, 30))
        self.search_defect_btn.setFont(font2)
        self.search_defect_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_defect_btn.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_88.addWidget(self.search_defect_btn)

        self.search_defect_clear_btn = QPushButton(self.frame_122)
        self.search_defect_clear_btn.setObjectName(u"search_defect_clear_btn")
        self.search_defect_clear_btn.setMinimumSize(QSize(0, 30))
        self.search_defect_clear_btn.setFont(font2)
        self.search_defect_clear_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_defect_clear_btn.setStyleSheet(u"QPushButton{\n"
"background: #FF1111;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_88.addWidget(self.search_defect_clear_btn)


        self.verticalLayout_88.addWidget(self.frame_122)

        self.frame_123 = QFrame(self.frame_add_defect_2)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMinimumSize(QSize(0, 33))
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_123)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.create_defect_message_2 = QLabel(self.frame_123)
        self.create_defect_message_2.setObjectName(u"create_defect_message_2")

        self.verticalLayout_90.addWidget(self.create_defect_message_2, 0, Qt.AlignHCenter)


        self.verticalLayout_88.addWidget(self.frame_123)


        self.horizontalLayout_80.addWidget(self.frame_add_defect_2)

        self.frame_add_defect = QFrame(self.groupBox_101)
        self.frame_add_defect.setObjectName(u"frame_add_defect")
        self.frame_add_defect.setMinimumSize(QSize(270, 0))
        self.frame_add_defect.setMaximumSize(QSize(0, 16777215))
        self.frame_add_defect.setFrameShape(QFrame.StyledPanel)
        self.frame_add_defect.setFrameShadow(QFrame.Sunken)
        self.frame_add_defect.setLineWidth(7)
        self.frame_add_defect.setMidLineWidth(4)
        self.verticalLayout_82 = QVBoxLayout(self.frame_add_defect)
        self.verticalLayout_82.setSpacing(7)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(10, 10, 10, 10)
        self.groupBox_6 = QGroupBox(self.frame_add_defect)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_83 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_83.setSpacing(10)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 10, 0, 0)
        self.frame_104 = QFrame(self.groupBox_6)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMaximumSize(QSize(16777215, 35))
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.label_87 = QLabel(self.frame_104)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_72.addWidget(self.label_87)

        self.defect_name_lineedit = QLineEdit(self.frame_104)
        self.defect_name_lineedit.setObjectName(u"defect_name_lineedit")
        self.defect_name_lineedit.setMinimumSize(QSize(0, 30))
        self.defect_name_lineedit.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")

        self.horizontalLayout_72.addWidget(self.defect_name_lineedit, 0, Qt.AlignRight)


        self.verticalLayout_83.addWidget(self.frame_104)

        self.frame_105 = QFrame(self.groupBox_6)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(0, 35))
        self.frame_105.setMaximumSize(QSize(16777215, 35))
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_102 = QLabel(self.frame_105)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_73.addWidget(self.label_102)

        self.defect_shortname_lineedit = QLineEdit(self.frame_105)
        self.defect_shortname_lineedit.setObjectName(u"defect_shortname_lineedit")
        self.defect_shortname_lineedit.setMinimumSize(QSize(0, 30))
        self.defect_shortname_lineedit.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")
        self.defect_shortname_lineedit.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_73.addWidget(self.defect_shortname_lineedit, 0, Qt.AlignRight)


        self.verticalLayout_83.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.groupBox_6)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(0, 35))
        self.frame_106.setMaximumSize(QSize(16777215, 30))
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_103 = QLabel(self.frame_106)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_74.addWidget(self.label_103)

        self.defect_id_lineedit = QLineEdit(self.frame_106)
        self.defect_id_lineedit.setObjectName(u"defect_id_lineedit")
        self.defect_id_lineedit.setMinimumSize(QSize(0, 30))
        self.defect_id_lineedit.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")
        self.defect_id_lineedit.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_74.addWidget(self.defect_id_lineedit, 0, Qt.AlignRight)


        self.verticalLayout_83.addWidget(self.frame_106)

        self.frame_117 = QFrame(self.groupBox_6)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setMinimumSize(QSize(0, 35))
        self.frame_117.setMaximumSize(QSize(16777215, 30))
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_108 = QLabel(self.frame_117)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_84.addWidget(self.label_108)

        self.defect_group_combo = QComboBox(self.frame_117)
        self.defect_group_combo.setObjectName(u"defect_group_combo")
        self.defect_group_combo.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_84.addWidget(self.defect_group_combo)


        self.verticalLayout_83.addWidget(self.frame_117)

        self.frame_116 = QFrame(self.groupBox_6)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMinimumSize(QSize(0, 35))
        self.frame_116.setMaximumSize(QSize(16777215, 30))
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_116)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.label_107 = QLabel(self.frame_116)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_83.addWidget(self.label_107)

        self.defect_level_comboBox = QComboBox(self.frame_116)
        self.defect_level_comboBox.addItem("")
        self.defect_level_comboBox.addItem("")
        self.defect_level_comboBox.addItem("")
        self.defect_level_comboBox.addItem("")
        self.defect_level_comboBox.setObjectName(u"defect_level_comboBox")
        self.defect_level_comboBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_83.addWidget(self.defect_level_comboBox)


        self.verticalLayout_83.addWidget(self.frame_116)

        self.frame_115 = QFrame(self.groupBox_6)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(0, 35))
        self.frame_115.setMaximumSize(QSize(16777215, 30))
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.label_106 = QLabel(self.frame_115)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_82.addWidget(self.label_106)

        self.defect_color_comboBox = QComboBox(self.frame_115)
        self.defect_color_comboBox.setObjectName(u"defect_color_comboBox")
        self.defect_color_comboBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_82.addWidget(self.defect_color_comboBox)


        self.verticalLayout_83.addWidget(self.frame_115)


        self.verticalLayout_82.addWidget(self.groupBox_6, 0, Qt.AlignTop)

        self.frame_110 = QFrame(self.frame_add_defect)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(0, 43))
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.create_defect = QPushButton(self.frame_110)
        self.create_defect.setObjectName(u"create_defect")
        self.create_defect.setMinimumSize(QSize(0, 30))
        self.create_defect.setFont(font2)
        self.create_defect.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_defect.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_76.addWidget(self.create_defect)


        self.verticalLayout_82.addWidget(self.frame_110)

        self.frame_111 = QFrame(self.frame_add_defect)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMinimumSize(QSize(0, 33))
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_111)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.create_defect_message = QLabel(self.frame_111)
        self.create_defect_message.setObjectName(u"create_defect_message")

        self.verticalLayout_85.addWidget(self.create_defect_message, 0, Qt.AlignHCenter)


        self.verticalLayout_82.addWidget(self.frame_111)


        self.horizontalLayout_80.addWidget(self.frame_add_defect)


        self.verticalLayout_23.addWidget(self.groupBox_101)

        self.line = QFrame(self.page_defects)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line)

        self.groupBox_102 = QGroupBox(self.page_defects)
        self.groupBox_102.setObjectName(u"groupBox_102")
        self.groupBox_102.setMaximumSize(QSize(1600, 500))
        self.horizontalLayout_95 = QHBoxLayout(self.groupBox_102)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 5, 0, 0)
        self.frame_128 = QFrame(self.groupBox_102)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setMinimumSize(QSize(700, 0))
        self.frame_128.setMaximumSize(QSize(1000, 16777215))
        self.frame_128.setStyleSheet(u"")
        self.frame_128.setFrameShape(QFrame.Box)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_128)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.frame_128)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"border:Transparent")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 688, 69))
        self.horizontalLayout_96 = QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.tableWidget_defectgroups = QTableWidget(self.scrollAreaWidgetContents_7)
        if (self.tableWidget_defectgroups.columnCount() < 4):
            self.tableWidget_defectgroups.setColumnCount(4)
        self.tableWidget_defectgroups.setObjectName(u"tableWidget_defectgroups")
        self.tableWidget_defectgroups.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_defectgroups.setProperty("showDropIndicator", False)
        self.tableWidget_defectgroups.setDragDropOverwriteMode(False)
        self.tableWidget_defectgroups.setColumnCount(4)

        self.horizontalLayout_96.addWidget(self.tableWidget_defectgroups)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_92.addWidget(self.scrollArea_5)

        self.frame_129 = QFrame(self.frame_128)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setMinimumSize(QSize(270, 38))
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_129)
        self.horizontalLayout_97.setSpacing(5)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.show_realated_defect_btn = QPushButton(self.frame_129)
        self.show_realated_defect_btn.setObjectName(u"show_realated_defect_btn")
        self.show_realated_defect_btn.setMinimumSize(QSize(140, 30))
        self.show_realated_defect_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_realated_defect_btn.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_97.addWidget(self.show_realated_defect_btn)

        self.edit_defect_group_btn = QPushButton(self.frame_129)
        self.edit_defect_group_btn.setObjectName(u"edit_defect_group_btn")
        self.edit_defect_group_btn.setMinimumSize(QSize(140, 30))
        self.edit_defect_group_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_defect_group_btn.setStyleSheet(u"QPushButton{\n"
"background: #78AD40;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_97.addWidget(self.edit_defect_group_btn)

        self.remove_defect_group_btn = QPushButton(self.frame_129)
        self.remove_defect_group_btn.setObjectName(u"remove_defect_group_btn")
        self.remove_defect_group_btn.setMinimumSize(QSize(140, 30))
        self.remove_defect_group_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_defect_group_btn.setStyleSheet(u"QPushButton{\n"
"background: #FF1111;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_97.addWidget(self.remove_defect_group_btn)


        self.verticalLayout_92.addWidget(self.frame_129, 0, Qt.AlignHCenter)


        self.horizontalLayout_95.addWidget(self.frame_128)

        self.frame_add_defect_4 = QFrame(self.groupBox_102)
        self.frame_add_defect_4.setObjectName(u"frame_add_defect_4")
        self.frame_add_defect_4.setMinimumSize(QSize(270, 0))
        self.frame_add_defect_4.setMaximumSize(QSize(0, 16777215))
        self.frame_add_defect_4.setFrameShape(QFrame.StyledPanel)
        self.frame_add_defect_4.setFrameShadow(QFrame.Sunken)
        self.frame_add_defect_4.setLineWidth(7)
        self.frame_add_defect_4.setMidLineWidth(4)
        self.verticalLayout_91 = QVBoxLayout(self.frame_add_defect_4)
        self.verticalLayout_91.setSpacing(7)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(10, 10, 10, 10)
        self.groupBox_9 = QGroupBox(self.frame_add_defect_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_98 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_98.setSpacing(10)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 10, 0, 0)
        self.frame_114 = QFrame(self.groupBox_9)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMaximumSize(QSize(16777215, 35))
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_114)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.label_105 = QLabel(self.frame_114)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_79.addWidget(self.label_105)

        self.defectgroup_search_name_lineedie = QLineEdit(self.frame_114)
        self.defectgroup_search_name_lineedie.setObjectName(u"defectgroup_search_name_lineedie")
        self.defectgroup_search_name_lineedie.setMinimumSize(QSize(0, 30))
        self.defectgroup_search_name_lineedie.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")

        self.horizontalLayout_79.addWidget(self.defectgroup_search_name_lineedie, 0, Qt.AlignRight)


        self.verticalLayout_98.addWidget(self.frame_114)

        self.frame_135 = QFrame(self.groupBox_9)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setMinimumSize(QSize(0, 35))
        self.frame_135.setMaximumSize(QSize(16777215, 30))
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_135)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.label_119 = QLabel(self.frame_135)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_107.addWidget(self.label_119)

        self.defectgroup_search_isdefect_combo = QComboBox(self.frame_135)
        self.defectgroup_search_isdefect_combo.addItem("")
        self.defectgroup_search_isdefect_combo.addItem("")
        self.defectgroup_search_isdefect_combo.addItem("")
        self.defectgroup_search_isdefect_combo.setObjectName(u"defectgroup_search_isdefect_combo")
        self.defectgroup_search_isdefect_combo.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_107.addWidget(self.defectgroup_search_isdefect_combo)


        self.verticalLayout_98.addWidget(self.frame_135)


        self.verticalLayout_91.addWidget(self.groupBox_9, 0, Qt.AlignTop)

        self.frame_125 = QFrame(self.frame_add_defect_4)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setMinimumSize(QSize(0, 43))
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_125)
        self.horizontalLayout_90.setSpacing(10)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.search_defectgroup_btn = QPushButton(self.frame_125)
        self.search_defectgroup_btn.setObjectName(u"search_defectgroup_btn")
        self.search_defectgroup_btn.setMinimumSize(QSize(0, 30))
        self.search_defectgroup_btn.setFont(font2)
        self.search_defectgroup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_defectgroup_btn.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_90.addWidget(self.search_defectgroup_btn)

        self.search_defectgroup_clear_btn = QPushButton(self.frame_125)
        self.search_defectgroup_clear_btn.setObjectName(u"search_defectgroup_clear_btn")
        self.search_defectgroup_clear_btn.setMinimumSize(QSize(0, 30))
        self.search_defectgroup_clear_btn.setFont(font2)
        self.search_defectgroup_clear_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_defectgroup_clear_btn.setStyleSheet(u"QPushButton{\n"
"background: #FF1111;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_90.addWidget(self.search_defectgroup_clear_btn)


        self.verticalLayout_91.addWidget(self.frame_125)

        self.frame_126 = QFrame(self.frame_add_defect_4)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setMinimumSize(QSize(0, 33))
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_126)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.create_defect_message_3 = QLabel(self.frame_126)
        self.create_defect_message_3.setObjectName(u"create_defect_message_3")

        self.verticalLayout_99.addWidget(self.create_defect_message_3, 0, Qt.AlignHCenter)


        self.verticalLayout_91.addWidget(self.frame_126)


        self.horizontalLayout_95.addWidget(self.frame_add_defect_4)

        self.frame_add_defect_3 = QFrame(self.groupBox_102)
        self.frame_add_defect_3.setObjectName(u"frame_add_defect_3")
        self.frame_add_defect_3.setMinimumSize(QSize(270, 0))
        self.frame_add_defect_3.setMaximumSize(QSize(0, 16777215))
        self.frame_add_defect_3.setFrameShape(QFrame.StyledPanel)
        self.frame_add_defect_3.setFrameShadow(QFrame.Sunken)
        self.frame_add_defect_3.setLineWidth(7)
        self.frame_add_defect_3.setMidLineWidth(4)
        self.verticalLayout_93 = QVBoxLayout(self.frame_add_defect_3)
        self.verticalLayout_93.setSpacing(7)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(10, 10, 10, 10)
        self.groupBox_8 = QGroupBox(self.frame_add_defect_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_96 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_96.setSpacing(10)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 10, 0, 0)
        self.frame_130 = QFrame(self.groupBox_8)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setMaximumSize(QSize(16777215, 35))
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_130)
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.label_115 = QLabel(self.frame_130)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_98.addWidget(self.label_115)

        self.defect_group_name_lineedit = QLineEdit(self.frame_130)
        self.defect_group_name_lineedit.setObjectName(u"defect_group_name_lineedit")
        self.defect_group_name_lineedit.setMinimumSize(QSize(0, 30))
        self.defect_group_name_lineedit.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")

        self.horizontalLayout_98.addWidget(self.defect_group_name_lineedit, 0, Qt.AlignRight)


        self.verticalLayout_96.addWidget(self.frame_130)

        self.frame_132 = QFrame(self.groupBox_8)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setMinimumSize(QSize(0, 35))
        self.frame_132.setMaximumSize(QSize(16777215, 30))
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_132)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.label_117 = QLabel(self.frame_132)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_103.addWidget(self.label_117)

        self.defect_group_id_lineedit = QLineEdit(self.frame_132)
        self.defect_group_id_lineedit.setObjectName(u"defect_group_id_lineedit")
        self.defect_group_id_lineedit.setMinimumSize(QSize(0, 30))
        self.defect_group_id_lineedit.setStyleSheet(u"QLineEdit{\n"
"border-radius: 0px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"border: 1px solid #CDCDCE;\n"
"}")
        self.defect_group_id_lineedit.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_103.addWidget(self.defect_group_id_lineedit, 0, Qt.AlignRight)


        self.verticalLayout_96.addWidget(self.frame_132)

        self.frame_133 = QFrame(self.groupBox_8)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setMinimumSize(QSize(0, 35))
        self.frame_133.setMaximumSize(QSize(16777215, 30))
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.frame_133)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.label_116 = QLabel(self.frame_133)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(4, 0))

        self.horizontalLayout_104.addWidget(self.label_116)

        self.defect_isdefectgroup_spinbox = QRadioButton(self.frame_133)
        self.defect_isdefectgroup_spinbox.setObjectName(u"defect_isdefectgroup_spinbox")

        self.horizontalLayout_104.addWidget(self.defect_isdefectgroup_spinbox)

        self.defect_notdefectgroup_spinbox = QRadioButton(self.frame_133)
        self.defect_notdefectgroup_spinbox.setObjectName(u"defect_notdefectgroup_spinbox")

        self.horizontalLayout_104.addWidget(self.defect_notdefectgroup_spinbox)


        self.verticalLayout_96.addWidget(self.frame_133)


        self.verticalLayout_93.addWidget(self.groupBox_8, 0, Qt.AlignTop)

        self.frame_137 = QFrame(self.frame_add_defect_3)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setMinimumSize(QSize(0, 43))
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_137)
        self.horizontalLayout_109.setSpacing(0)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.create_defect_group = QPushButton(self.frame_137)
        self.create_defect_group.setObjectName(u"create_defect_group")
        self.create_defect_group.setMinimumSize(QSize(0, 30))
        self.create_defect_group.setFont(font2)
        self.create_defect_group.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_defect_group.setStyleSheet(u"QPushButton{\n"
"background: #1C95D8;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_109.addWidget(self.create_defect_group)


        self.verticalLayout_93.addWidget(self.frame_137)

        self.frame_138 = QFrame(self.frame_add_defect_3)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setMinimumSize(QSize(0, 33))
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_138)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.create_defect_group_message = QLabel(self.frame_138)
        self.create_defect_group_message.setObjectName(u"create_defect_group_message")

        self.verticalLayout_97.addWidget(self.create_defect_group_message, 0, Qt.AlignHCenter)


        self.verticalLayout_93.addWidget(self.frame_138)


        self.horizontalLayout_95.addWidget(self.frame_add_defect_3)


        self.verticalLayout_23.addWidget(self.groupBox_102)

        self.stackedWidget.addWidget(self.page_defects)
        self.page_tools = QWidget()
        self.page_tools.setObjectName(u"page_tools")
        self.verticalLayout_26 = QVBoxLayout(self.page_tools)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_2 = QFrame(self.page_tools)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(232, 0))
        self.frame_13.setMaximumSize(QSize(232, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.add_btn = QPushButton(self.frame_13)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_19.addWidget(self.add_btn)

        self.edit_remove_btn = QPushButton(self.frame_13)
        self.edit_remove_btn.setObjectName(u"edit_remove_btn")
        self.edit_remove_btn.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_19.addWidget(self.edit_remove_btn)


        self.horizontalLayout_16.addWidget(self.frame_13)

        self.frame_24 = QFrame(self.frame_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(300, 0))
        self.frame_24.setMaximumSize(QSize(0, 16777215))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(9, 0, 0, 0)
        self.comboBox_edit_remove = QComboBox(self.frame_24)
        self.comboBox_edit_remove.setObjectName(u"comboBox_edit_remove")
        self.comboBox_edit_remove.setMinimumSize(QSize(0, 27))

        self.horizontalLayout_20.addWidget(self.comboBox_edit_remove)

        self.edit_btn = QPushButton(self.frame_24)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setMinimumSize(QSize(0, 27))
        self.edit_btn.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_20.addWidget(self.edit_btn)

        self.remove_screw_btn = QPushButton(self.frame_24)
        self.remove_screw_btn.setObjectName(u"remove_screw_btn")
        self.remove_screw_btn.setMinimumSize(QSize(0, 27))
        self.remove_screw_btn.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_20.addWidget(self.remove_screw_btn)


        self.horizontalLayout_16.addWidget(self.frame_24)

        self.frame_23 = QFrame(self.frame_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(300, 0))
        self.frame_23.setMaximumSize(QSize(0, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.line_new_screw = QLineEdit(self.frame_23)
        self.line_new_screw.setObjectName(u"line_new_screw")
        self.line_new_screw.setMinimumSize(QSize(0, 27))

        self.horizontalLayout_21.addWidget(self.line_new_screw)

        self.save_new_btn = QPushButton(self.frame_23)
        self.save_new_btn.setObjectName(u"save_new_btn")
        self.save_new_btn.setMinimumSize(QSize(52, 27))

        self.horizontalLayout_21.addWidget(self.save_new_btn)


        self.horizontalLayout_16.addWidget(self.frame_23)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_16.addWidget(self.label_6)

        self.label_screw_name = QLabel(self.frame_2)
        self.label_screw_name.setObjectName(u"label_screw_name")

        self.horizontalLayout_16.addWidget(self.label_screw_name)

        self.horizontalSpacer_9 = QSpacerItem(86, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_9)

        self.label_warning_tool_page = QLabel(self.frame_2)
        self.label_warning_tool_page.setObjectName(u"label_warning_tool_page")

        self.horizontalLayout_16.addWidget(self.label_warning_tool_page)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer)


        self.verticalLayout_26.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.page_tools)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_25 = QFrame(self.frame_4)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(200, 0))
        self.frame_25.setMaximumSize(QSize(200, 16777215))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_25)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 50))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(3, 0, 3, 0)
        self.grab_load_btn = QPushButton(self.frame_27)
        self.grab_load_btn.setObjectName(u"grab_load_btn")
        self.grab_load_btn.setMinimumSize(QSize(0, 27))

        self.horizontalLayout_23.addWidget(self.grab_load_btn)


        self.verticalLayout_27.addWidget(self.frame_27)

        self.line_5 = QFrame(self.frame_25)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_5)

        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.frame_33 = QFrame(self.frame_28)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(10, 10, 151, 41))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.checkBox_3 = QCheckBox(self.frame_33)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_43.addWidget(self.checkBox_3)

        self.tool1_btn = QPushButton(self.frame_33)
        self.tool1_btn.setObjectName(u"tool1_btn")
        self.tool1_btn.setMinimumSize(QSize(0, 25))
        self.tool1_btn.setCheckable(False)
        self.tool1_btn.setChecked(False)

        self.horizontalLayout_43.addWidget(self.tool1_btn)

        self.frame_34 = QFrame(self.frame_28)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(10, 50, 151, 41))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.checkBox_4 = QCheckBox(self.frame_34)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_44.addWidget(self.checkBox_4)

        self.tool2_btn = QPushButton(self.frame_34)
        self.tool2_btn.setObjectName(u"tool2_btn")
        self.tool2_btn.setMinimumSize(QSize(0, 25))
        self.tool2_btn.setCheckable(False)
        self.tool2_btn.setChecked(False)

        self.horizontalLayout_44.addWidget(self.tool2_btn)

        self.frame_35 = QFrame(self.frame_28)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(10, 90, 151, 41))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.checkBox_5 = QCheckBox(self.frame_35)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_45.addWidget(self.checkBox_5)

        self.tool3_btn = QPushButton(self.frame_35)
        self.tool3_btn.setObjectName(u"tool3_btn")
        self.tool3_btn.setMinimumSize(QSize(0, 25))
        self.tool3_btn.setCheckable(False)
        self.tool3_btn.setChecked(False)

        self.horizontalLayout_45.addWidget(self.tool3_btn)

        self.frame_36 = QFrame(self.frame_28)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(10, 130, 151, 41))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.checkBox_6 = QCheckBox(self.frame_36)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.horizontalLayout_46.addWidget(self.checkBox_6)

        self.pushButton_13 = QPushButton(self.frame_36)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 25))
        self.pushButton_13.setCheckable(False)
        self.pushButton_13.setChecked(False)

        self.horizontalLayout_46.addWidget(self.pushButton_13)


        self.verticalLayout_27.addWidget(self.frame_28)


        self.horizontalLayout_22.addWidget(self.frame_25)

        self.frame_37 = QFrame(self.frame_4)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(408, 62))
        self.frame_37.setMaximumSize(QSize(450, 16777215))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_37)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.stackedWidget_2 = QStackedWidget(self.frame_37)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(200, 0))
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.stackedWidget_2.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_29 = QVBoxLayout(self.page_1)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_26 = QFrame(self.page_1)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_26)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(445, 120))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_29)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.frame_29)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_25 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.line_image_address = QLineEdit(self.groupBox_3)
        self.line_image_address.setObjectName(u"line_image_address")
        self.line_image_address.setMinimumSize(QSize(210, 0))
        self.line_image_address.setMaximumSize(QSize(405, 16777215))

        self.horizontalLayout_24.addWidget(self.line_image_address)

        self.load_image_btn = QToolButton(self.groupBox_3)
        self.load_image_btn.setObjectName(u"load_image_btn")

        self.horizontalLayout_24.addWidget(self.load_image_btn)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_24)

        self.set_image_btn = QPushButton(self.groupBox_3)
        self.set_image_btn.setObjectName(u"set_image_btn")
        self.set_image_btn.setMinimumSize(QSize(82, 27))
        self.set_image_btn.setMaximumSize(QSize(16777215, 27))

        self.horizontalLayout_25.addWidget(self.set_image_btn)


        self.verticalLayout_39.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.frame_29)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_26 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.camera1_select_radio = QRadioButton(self.groupBox_2)
        self.camera1_select_radio.setObjectName(u"camera1_select_radio")
        self.camera1_select_radio.setChecked(True)

        self.horizontalLayout_26.addWidget(self.camera1_select_radio)

        self.camera2_select_radio = QRadioButton(self.groupBox_2)
        self.camera2_select_radio.setObjectName(u"camera2_select_radio")

        self.horizontalLayout_26.addWidget(self.camera2_select_radio)

        self.connect_grab_btn = QPushButton(self.groupBox_2)
        self.connect_grab_btn.setObjectName(u"connect_grab_btn")
        self.connect_grab_btn.setMinimumSize(QSize(129, 27))
        self.connect_grab_btn.setMaximumSize(QSize(16777215, 27))

        self.horizontalLayout_26.addWidget(self.connect_grab_btn)


        self.verticalLayout_39.addWidget(self.groupBox_2)


        self.verticalLayout_28.addWidget(self.frame_29)

        self.line_6 = QFrame(self.frame_26)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line_6)

        self.frame_30 = QFrame(self.frame_26)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(300, 0))
        self.frame_32.setMaximumSize(QSize(372, 16777215))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_32)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_41 = QFrame(self.frame_32)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_41)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_41)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 34))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.groupBox_10 = QGroupBox(self.frame_49)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_3 = QLabel(self.groupBox_10)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_47.addWidget(self.label_3)

        self.spinBox_grab_page_x_rect1 = QSpinBox(self.groupBox_10)
        self.spinBox_grab_page_x_rect1.setObjectName(u"spinBox_grab_page_x_rect1")
        self.spinBox_grab_page_x_rect1.setMaximum(20000)
        self.spinBox_grab_page_x_rect1.setSingleStep(5)

        self.horizontalLayout_47.addWidget(self.spinBox_grab_page_x_rect1)


        self.verticalLayout_36.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_4 = QLabel(self.groupBox_10)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_48.addWidget(self.label_4)

        self.spinBox_grab_page_y_rect1 = QSpinBox(self.groupBox_10)
        self.spinBox_grab_page_y_rect1.setObjectName(u"spinBox_grab_page_y_rect1")
        self.spinBox_grab_page_y_rect1.setMaximum(20000)
        self.spinBox_grab_page_y_rect1.setSingleStep(5)

        self.horizontalLayout_48.addWidget(self.spinBox_grab_page_y_rect1)


        self.verticalLayout_36.addLayout(self.horizontalLayout_48)


        self.horizontalLayout_51.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.frame_49)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_37 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_7 = QLabel(self.groupBox_11)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_49.addWidget(self.label_7)

        self.spinBox_grab_page_x_rect2 = QSpinBox(self.groupBox_11)
        self.spinBox_grab_page_x_rect2.setObjectName(u"spinBox_grab_page_x_rect2")
        self.spinBox_grab_page_x_rect2.setMaximum(20000)
        self.spinBox_grab_page_x_rect2.setSingleStep(5)

        self.horizontalLayout_49.addWidget(self.spinBox_grab_page_x_rect2)


        self.verticalLayout_37.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_8 = QLabel(self.groupBox_11)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_50.addWidget(self.label_8)

        self.spinBox_grab_page_y_rect2 = QSpinBox(self.groupBox_11)
        self.spinBox_grab_page_y_rect2.setObjectName(u"spinBox_grab_page_y_rect2")
        self.spinBox_grab_page_y_rect2.setMaximum(20000)
        self.spinBox_grab_page_y_rect2.setSingleStep(5)

        self.horizontalLayout_50.addWidget(self.spinBox_grab_page_y_rect2)


        self.verticalLayout_37.addLayout(self.horizontalLayout_50)


        self.horizontalLayout_51.addWidget(self.groupBox_11)


        self.verticalLayout_33.addWidget(self.frame_49)


        self.verticalLayout_34.addWidget(self.frame_41)

        self.frame_40 = QFrame(self.frame_32)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_40)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_5 = QLabel(self.frame_40)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_32.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.horizontalSlider_grab = QSlider(self.frame_40)
        self.horizontalSlider_grab.setObjectName(u"horizontalSlider_grab")
        self.horizontalSlider_grab.setMinimumSize(QSize(0, 30))
        self.horizontalSlider_grab.setMaximum(255)
        self.horizontalSlider_grab.setOrientation(Qt.Horizontal)

        self.verticalLayout_32.addWidget(self.horizontalSlider_grab)

        self.spinBox = QSpinBox(self.frame_40)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(255)

        self.verticalLayout_32.addWidget(self.spinBox, 0, Qt.AlignHCenter)


        self.verticalLayout_34.addWidget(self.frame_40)

        self.frame_50 = QFrame(self.frame_32)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_50)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_9 = QLabel(self.frame_50)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_9)

        self.noiseFilterSlider_grab = QSlider(self.frame_50)
        self.noiseFilterSlider_grab.setObjectName(u"noiseFilterSlider_grab")
        self.noiseFilterSlider_grab.setMaximum(100)
        self.noiseFilterSlider_grab.setSingleStep(1)
        self.noiseFilterSlider_grab.setOrientation(Qt.Horizontal)

        self.verticalLayout_38.addWidget(self.noiseFilterSlider_grab)

        self.noiseAreaSpinBox = QSpinBox(self.frame_50)
        self.noiseAreaSpinBox.setObjectName(u"noiseAreaSpinBox")
        self.noiseAreaSpinBox.setMaximum(100)

        self.verticalLayout_38.addWidget(self.noiseAreaSpinBox, 0, Qt.AlignHCenter)


        self.verticalLayout_34.addWidget(self.frame_50)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_4)

        self.frame_45 = QFrame(self.frame_32)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_45)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, 9, -1, -1)

        self.verticalLayout_34.addWidget(self.frame_45)


        self.horizontalLayout_41.addWidget(self.frame_32)


        self.verticalLayout_28.addWidget(self.frame_30)


        self.verticalLayout_29.addWidget(self.frame_26)

        self.stackedWidget_2.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_31 = QVBoxLayout(self.page_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_31 = QFrame(self.page_2)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 61))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.add_page_tool2 = QPushButton(self.frame_31)
        self.add_page_tool2.setObjectName(u"add_page_tool2")
        self.add_page_tool2.setMaximumSize(QSize(26, 16777215))
        self.add_page_tool2.setStyleSheet(u"border:none;\n"
"")
        icon16 = QIcon()
        icon16.addFile(u"images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_page_tool2.setIcon(icon16)
        self.add_page_tool2.setIconSize(QSize(26, 26))

        self.horizontalLayout_40.addWidget(self.add_page_tool2)

        self.comboBox = QComboBox(self.frame_31)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(191, 0))
        self.comboBox.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_40.addWidget(self.comboBox)

        self.pushButton_2 = QPushButton(self.frame_31)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(26, 16777215))
        self.pushButton_2.setStyleSheet(u"border:none;")
        icon17 = QIcon()
        icon17.addFile(u"images/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon17)
        self.pushButton_2.setIconSize(QSize(26, 27))

        self.horizontalLayout_40.addWidget(self.pushButton_2)


        self.verticalLayout_31.addWidget(self.frame_31)

        self.frame_52 = QFrame(self.page_2)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_52)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(0, 0))
        self.frame_53.setMaximumSize(QSize(16777215, 0))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(-1, 1, -1, 0)
        self.label_10 = QLabel(self.frame_53)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_55.addWidget(self.label_10)

        self.tedad_ghooshe_tool2 = QComboBox(self.frame_53)
        self.tedad_ghooshe_tool2.setObjectName(u"tedad_ghooshe_tool2")

        self.horizontalLayout_55.addWidget(self.tedad_ghooshe_tool2)

        self.set_tedad_ghooshe_btn = QPushButton(self.frame_53)
        self.set_tedad_ghooshe_btn.setObjectName(u"set_tedad_ghooshe_btn")
        self.set_tedad_ghooshe_btn.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_55.addWidget(self.set_tedad_ghooshe_btn)


        self.verticalLayout_42.addWidget(self.frame_53)

        self.groupBox_12 = QGroupBox(self.frame_52)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(0, 0))
        self.groupBox_12.setMaximumSize(QSize(16777215, 0))
        self.horizontalLayout_56 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.checkBox_rect = QCheckBox(self.groupBox_12)
        self.checkBox_rect.setObjectName(u"checkBox_rect")

        self.horizontalLayout_56.addWidget(self.checkBox_rect)

        self.checkBox_circle = QCheckBox(self.groupBox_12)
        self.checkBox_circle.setObjectName(u"checkBox_circle")

        self.horizontalLayout_56.addWidget(self.checkBox_circle)

        self.checkBox_mask = QCheckBox(self.groupBox_12)
        self.checkBox_mask.setObjectName(u"checkBox_mask")

        self.horizontalLayout_56.addWidget(self.checkBox_mask)


        self.verticalLayout_42.addWidget(self.groupBox_12)

        self.frame_54 = QFrame(self.frame_52)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 0))
        self.frame_54.setMaximumSize(QSize(16777215, 0))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_11 = QLabel(self.frame_54)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_54.addWidget(self.label_11)

        self.draw_complete_btn = QPushButton(self.frame_54)
        self.draw_complete_btn.setObjectName(u"draw_complete_btn")
        self.draw_complete_btn.setMaximumSize(QSize(86, 16777215))

        self.horizontalLayout_54.addWidget(self.draw_complete_btn)


        self.verticalLayout_42.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.frame_52)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(0, 0))
        self.frame_55.setMaximumSize(QSize(16777215, 0))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_55)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.groupBox_13 = QGroupBox(self.frame_55)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.horizontalLayout_52 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalSlider = QSlider(self.groupBox_13)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_52.addWidget(self.horizontalSlider)

        self.spinBox_3 = QSpinBox(self.groupBox_13)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout_52.addWidget(self.spinBox_3)


        self.verticalLayout_41.addWidget(self.groupBox_13)

        self.groupBox_16 = QGroupBox(self.frame_55)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.horizontalLayout_53 = QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalSlider_3 = QSlider(self.groupBox_16)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_53.addWidget(self.horizontalSlider_3)

        self.spinBox_5 = QSpinBox(self.groupBox_16)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.horizontalLayout_53.addWidget(self.spinBox_5)


        self.verticalLayout_41.addWidget(self.groupBox_16)


        self.verticalLayout_42.addWidget(self.frame_55)

        self.verticalSpacer_5 = QSpacerItem(20, 111111111, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_5)

        self.frame_56 = QFrame(self.frame_52)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMaximumSize(QSize(16777215, 55))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_56)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.complete_page_tool2_btn = QPushButton(self.frame_56)
        self.complete_page_tool2_btn.setObjectName(u"complete_page_tool2_btn")
        self.complete_page_tool2_btn.setMinimumSize(QSize(113, 25))

        self.verticalLayout_43.addWidget(self.complete_page_tool2_btn)


        self.verticalLayout_42.addWidget(self.frame_56, 0, Qt.AlignHCenter)


        self.verticalLayout_31.addWidget(self.frame_52)

        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget_2.addWidget(self.page_4)

        self.verticalLayout_30.addWidget(self.stackedWidget_2)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(253, 41))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.prev_page_btn = QPushButton(self.frame_38)
        self.prev_page_btn.setObjectName(u"prev_page_btn")
        icon18 = QIcon()
        icon18.addFile(u"images/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_page_btn.setIcon(icon18)

        self.horizontalLayout_39.addWidget(self.prev_page_btn)

        self.save_btn_page_grab = QPushButton(self.frame_38)
        self.save_btn_page_grab.setObjectName(u"save_btn_page_grab")
        self.save_btn_page_grab.setMinimumSize(QSize(100, 32))
        self.save_btn_page_grab.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_39.addWidget(self.save_btn_page_grab)

        self.next_page_btn = QPushButton(self.frame_38)
        self.next_page_btn.setObjectName(u"next_page_btn")
        icon19 = QIcon()
        icon19.addFile(u"images/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_page_btn.setIcon(icon19)

        self.horizontalLayout_39.addWidget(self.next_page_btn)


        self.verticalLayout_30.addWidget(self.frame_38, 0, Qt.AlignHCenter)


        self.horizontalLayout_22.addWidget(self.frame_37)

        self.frame_51 = QFrame(self.frame_4)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(69, 24))
        self.frame_51.setMaximumSize(QSize(16777215, 16777195))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_51)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_image_grab_page = QLabel(self.frame_51)
        self.label_image_grab_page.setObjectName(u"label_image_grab_page")
        self.label_image_grab_page.setPixmap(QPixmap(u"images/test1_0_12.png"))
        self.label_image_grab_page.setScaledContents(True)

        self.verticalLayout_40.addWidget(self.label_image_grab_page)

        self.frame_39 = QFrame(self.frame_51)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 36))
        self.frame_39.setMaximumSize(QSize(200, 45))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.fullscreen_cam_grab_4 = QPushButton(self.frame_39)
        self.fullscreen_cam_grab_4.setObjectName(u"fullscreen_cam_grab_4")
        self.fullscreen_cam_grab_4.setMaximumSize(QSize(50, 50))
        self.fullscreen_cam_grab_4.setStyleSheet(u"border:None;")
        icon20 = QIcon()
        icon20.addFile(u"images/rotate-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreen_cam_grab_4.setIcon(icon20)
        self.fullscreen_cam_grab_4.setIconSize(QSize(21, 40))

        self.horizontalLayout_42.addWidget(self.fullscreen_cam_grab_4)

        self.spinBox_2 = QSpinBox(self.frame_39)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimum(-90)
        self.spinBox_2.setMaximum(90)

        self.horizontalLayout_42.addWidget(self.spinBox_2)

        self.fullscreen_cam_grab_3 = QPushButton(self.frame_39)
        self.fullscreen_cam_grab_3.setObjectName(u"fullscreen_cam_grab_3")
        self.fullscreen_cam_grab_3.setMaximumSize(QSize(50, 50))
        self.fullscreen_cam_grab_3.setStyleSheet(u"border:None;")
        icon21 = QIcon()
        icon21.addFile(u"images/rotate-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreen_cam_grab_3.setIcon(icon21)
        self.fullscreen_cam_grab_3.setIconSize(QSize(21, 40))

        self.horizontalLayout_42.addWidget(self.fullscreen_cam_grab_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_6)

        self.fullscreen_cam_grab_2 = QPushButton(self.frame_39)
        self.fullscreen_cam_grab_2.setObjectName(u"fullscreen_cam_grab_2")
        self.fullscreen_cam_grab_2.setMaximumSize(QSize(50, 50))
        self.fullscreen_cam_grab_2.setStyleSheet(u"border:None;")
        icon22 = QIcon()
        icon22.addFile(u"images/x-mark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreen_cam_grab_2.setIcon(icon22)
        self.fullscreen_cam_grab_2.setIconSize(QSize(30, 40))

        self.horizontalLayout_42.addWidget(self.fullscreen_cam_grab_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_7)

        self.fullscreen_cam_grab = QPushButton(self.frame_39)
        self.fullscreen_cam_grab.setObjectName(u"fullscreen_cam_grab")
        self.fullscreen_cam_grab.setMaximumSize(QSize(50, 50))
        self.fullscreen_cam_grab.setStyleSheet(u"border:None;")
        self.fullscreen_cam_grab.setIcon(icon12)
        self.fullscreen_cam_grab.setIconSize(QSize(30, 40))

        self.horizontalLayout_42.addWidget(self.fullscreen_cam_grab)


        self.verticalLayout_40.addWidget(self.frame_39, 0, Qt.AlignHCenter)


        self.horizontalLayout_22.addWidget(self.frame_51)


        self.verticalLayout_26.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_tools)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.topMenus)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"")

        self.verticalLayout_94.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"")

        self.verticalLayout_94.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"")

        self.verticalLayout_94.addWidget(self.btn_logout)


        self.verticalLayout_14.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_95.addWidget(self.bgApp)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tool1_btn.clicked.connect(self.checkBox_3.animateClick)
        self.horizontalSlider_grab.valueChanged.connect(self.spinBox.setValue)
        self.spinBox.valueChanged.connect(self.horizontalSlider_grab.setValue)
        self.tool2_btn.clicked.connect(self.checkBox_4.animateClick)
        self.tool3_btn.clicked.connect(self.checkBox_5.animateClick)
        self.pushButton_13.clicked.connect(self.checkBox_6.animateClick)
        self.line_new_screw.textChanged.connect(self.label_screw_name.setText)
        self.comboBox_edit_remove.currentTextChanged.connect(self.label_screw_name.setText)
        self.horizontalSlider.valueChanged.connect(self.spinBox_3.setValue)
        self.spinBox_3.valueChanged.connect(self.horizontalSlider.setValue)
        self.horizontalSlider_3.valueChanged.connect(self.spinBox_5.setValue)
        self.spinBox_5.valueChanged.connect(self.horizontalSlider_3.setValue)

        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toogle_btn_1.setText("")
#if QT_CONFIG(tooltip)
        self.side_dashboard_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.side_dashboard_btn.setText("")
#if QT_CONFIG(tooltip)
        self.side_tool_setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"PLC Settings", None))
#endif // QT_CONFIG(tooltip)
        self.side_tool_setting_btn.setText("")
#if QT_CONFIG(tooltip)
        self.side_camera_setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Camera Settings", None))
#endif // QT_CONFIG(tooltip)
        self.side_camera_setting_btn.setText("")
#if QT_CONFIG(tooltip)
        self.side_users_setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Users Management", None))
#endif // QT_CONFIG(tooltip)
        self.side_users_setting_btn.setText("")
#if QT_CONFIG(tooltip)
        self.side_general_setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"General Settings", None))
#endif // QT_CONFIG(tooltip)
        self.side_general_setting_btn.setText("")
#if QT_CONFIG(tooltip)
        self.main_login_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Login/Logout", None))
#endif // QT_CONFIG(tooltip)
        self.main_login_btn.setText("")
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Tuning", None))
        self.Binary_btn.setText(QCoreApplication.translate("MainWindow", u"Binary            ", None))
        self.Localization_btn.setText(QCoreApplication.translate("MainWindow", u"Localization", None))
        self.Classification_btn.setText(QCoreApplication.translate("MainWindow", u"Classification", None))
        self.label_dorsa.setText("")
        self.toogle_btn_2.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"User Name :", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Login", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Please Login", None))
#if QT_CONFIG(tooltip)
        self.miniButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.miniButton.setText("")
#if QT_CONFIG(tooltip)
        self.maxiButton.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maxiButton.setText("")
#if QT_CONFIG(tooltip)
        self.closeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeButton.setText("")
        self.btn_software_setting.setText(QCoreApplication.translate("MainWindow", u"Software setting", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Tuning Setting", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"User Settings", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Database Setting", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Storage Setting", None))
        self.camera_1.setText("")
        self.fullscreen_cam_1.setText("")
#if QT_CONFIG(tooltip)
        self.save_cam1_btn.setToolTip(QCoreApplication.translate("MainWindow", u"save image", None))
#endif // QT_CONFIG(tooltip)
        self.save_cam1_btn.setText("")
#if QT_CONFIG(tooltip)
        self.load_cam1_btn.setToolTip(QCoreApplication.translate("MainWindow", u"load image", None))
#endif // QT_CONFIG(tooltip)
        self.load_cam1_btn.setText("")
        self.camera_2.setText("")
        self.fullscreen_cam2.setText("")
#if QT_CONFIG(tooltip)
        self.save_cam2_btn.setToolTip(QCoreApplication.translate("MainWindow", u"save image", None))
#endif // QT_CONFIG(tooltip)
        self.save_cam2_btn.setText("")
#if QT_CONFIG(tooltip)
        self.load_cam2_btn.setToolTip(QCoreApplication.translate("MainWindow", u"load image", None))
#endif // QT_CONFIG(tooltip)
        self.load_cam2_btn.setText("")
        self.add_user_btn.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.add_user_btn_2.setText(QCoreApplication.translate("MainWindow", u"Deatils", None))
        self.remove_user_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"ADD New User", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Re-Enter Password", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Role :", None))
        self.create_user.setText(QCoreApplication.translate("MainWindow", u"Create User", None))
        self.create_user_message.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Details Of Selected User :", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"70 (C)", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"70 (C)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cam01", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cam02", None))
        self.camera01_btn.setText("")
        self.camera02_btn.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.cameraname_label.setText(QCoreApplication.translate("MainWindow", u"No Camera Selected", None))
        self.gain_label_2.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None))
        self.gain_label.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.expo_label.setText(QCoreApplication.translate("MainWindow", u"Exposure", None))
        self.width_label.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.height_label.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.offsetx_label.setText(QCoreApplication.translate("MainWindow", u"Offset X", None))
        self.offsety_label.setText(QCoreApplication.translate("MainWindow", u"Offset Y", None))
        self.trigger_label.setText(QCoreApplication.translate("MainWindow", u"Trigger Mode", None))
        self.maxbuffer_label.setText(QCoreApplication.translate("MainWindow", u"Max Buffer", None))
        self.packetdelay_label.setText(QCoreApplication.translate("MainWindow", u"Packet Delay", None))
        self.packetsize_label.setText(QCoreApplication.translate("MainWindow", u"Packet Size", None))
        self.transmissiondelay_label.setText(QCoreApplication.translate("MainWindow", u"Transmision Delay", None))
        self.transmissiondelay_label_2.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.trigger_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"On", None))
        self.trigger_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Off", None))

        self.camera_setting_apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Settings", None))
        self.camera_setting_connect_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.camera_setting_getpic_btn.setText(QCoreApplication.translate("MainWindow", u"Get Picture", None))
        self.camera_setting_message_label.setText("")
        self.camera_setting_picture_label.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Appearance Settings", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Style", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Font-Style", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Font-Size", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.setting_appearance_apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Settings", None))
        self.general_setting_appearance_message_label.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Defects Settings", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Color Num", None))
        self.setting_defects_apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Settings", None))
        self.setting_defect_message_label.setText("")
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Calibration Settings", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Large Rect Area", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Small Rect Area", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Rect Accuracy", None))
        self.setting_calibration_apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Settings", None))
        self.general_setting_calibration_message_label.setText("")
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Image Processing", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Split Size", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.setting_imageprocessing_apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Settings", None))
        self.setting_imageprocessing_message_label.setText("")
        self.groupBox_101.setTitle(QCoreApplication.translate("MainWindow", u"Defects", None))
        self.edit_defect_btn.setText(QCoreApplication.translate("MainWindow", u"Edit Defect", None))
        self.remove_defect_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Defect(s)", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Search/Filter Defect(s)", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Defect Name", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Is Defect", None))
        self.defect_search_isdefect_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.defect_search_isdefect_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.defect_search_isdefect_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Defect-Group", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Defect Level", None))
        self.defect_search_level_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.defect_search_level_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        self.defect_search_level_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))
        self.defect_search_level_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"2", None))
        self.defect_search_level_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"3", None))

        self.search_defect_btn.setText(QCoreApplication.translate("MainWindow", u"Search/Filter", None))
        self.search_defect_clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
        self.create_defect_message_2.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"ADD/Edit Defect", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Defect Name", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Defect Short-Name", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Defect ID", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Defect Group", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Defect Level", None))
        self.defect_level_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.defect_level_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.defect_level_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.defect_level_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))

        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Defect Color Label", None))
        self.create_defect.setText(QCoreApplication.translate("MainWindow", u"Create/Apply Defect", None))
        self.create_defect_message.setText("")
        self.groupBox_102.setTitle(QCoreApplication.translate("MainWindow", u"Defect-Groups", None))
        self.show_realated_defect_btn.setText(QCoreApplication.translate("MainWindow", u"Show Related  defects", None))
        self.edit_defect_group_btn.setText(QCoreApplication.translate("MainWindow", u"Edit Defect-Group", None))
        self.remove_defect_group_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Defect-Group", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Search/Filter Defect-Group(s)", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Defect-Group Name", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Is Defect", None))
        self.defectgroup_search_isdefect_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.defectgroup_search_isdefect_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.defectgroup_search_isdefect_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"No", None))

        self.search_defectgroup_btn.setText(QCoreApplication.translate("MainWindow", u"Search/Filter", None))
        self.search_defectgroup_clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
        self.create_defect_message_3.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"ADD/Edit  Defect-Group", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Defect-Group Name", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Defect-Group ID", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Is Defect", None))
        self.defect_isdefectgroup_spinbox.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.defect_notdefectgroup_spinbox.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.create_defect_group.setText(QCoreApplication.translate("MainWindow", u"Create/Apply Defect-Group", None))
        self.create_defect_group_message.setText("")
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.edit_remove_btn.setText(QCoreApplication.translate("MainWindow", u"Edit/Remove", None))
        self.edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.remove_screw_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.save_new_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Current :", None))
        self.label_screw_name.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_warning_tool_page.setText("")
        self.grab_load_btn.setText(QCoreApplication.translate("MainWindow", u"Grab / Load", None))
        self.checkBox_3.setText("")
        self.tool1_btn.setText(QCoreApplication.translate("MainWindow", u"TOOL 1", None))
        self.checkBox_4.setText("")
        self.tool2_btn.setText(QCoreApplication.translate("MainWindow", u"TOOL 2", None))
        self.checkBox_5.setText("")
        self.tool3_btn.setText(QCoreApplication.translate("MainWindow", u"TOOL 3", None))
        self.checkBox_6.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"TOOL 4", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.line_image_address.setText("")
        self.load_image_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.set_image_btn.setText(QCoreApplication.translate("MainWindow", u"Set Image", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Camera Select", None))
        self.camera1_select_radio.setText(QCoreApplication.translate("MainWindow", u"Camera 1", None))
        self.camera2_select_radio.setText(QCoreApplication.translate("MainWindow", u"Camera 2", None))
        self.connect_grab_btn.setText(QCoreApplication.translate("MainWindow", u"Connect and Grab", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Rect 1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Rect 2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Noise filter", None))
        self.add_page_tool2.setText("")
        self.pushButton_2.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tedad Ghooshe :", None))
        self.set_tedad_ghooshe_btn.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Select Mask Mode", None))
        self.checkBox_rect.setText(QCoreApplication.translate("MainWindow", u"Rectangle", None))
        self.checkBox_circle.setText(QCoreApplication.translate("MainWindow", u"Circle", None))
        self.checkBox_mask.setText(QCoreApplication.translate("MainWindow", u"Mask", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Drawing ..........", None))
        self.draw_complete_btn.setText(QCoreApplication.translate("MainWindow", u"Complete", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Noise filter", None))
        self.complete_page_tool2_btn.setText(QCoreApplication.translate("MainWindow", u"Complete", None))
        self.prev_page_btn.setText("")
        self.save_btn_page_grab.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.next_page_btn.setText("")
        self.label_image_grab_page.setText("")
#if QT_CONFIG(tooltip)
        self.fullscreen_cam_grab_4.setToolTip(QCoreApplication.translate("MainWindow", u"clear all", None))
#endif // QT_CONFIG(tooltip)
        self.fullscreen_cam_grab_4.setText("")
#if QT_CONFIG(tooltip)
        self.fullscreen_cam_grab_3.setToolTip(QCoreApplication.translate("MainWindow", u"clear all", None))
#endif // QT_CONFIG(tooltip)
        self.fullscreen_cam_grab_3.setText("")
#if QT_CONFIG(tooltip)
        self.fullscreen_cam_grab_2.setToolTip(QCoreApplication.translate("MainWindow", u"clear all", None))
#endif // QT_CONFIG(tooltip)
        self.fullscreen_cam_grab_2.setText("")
#if QT_CONFIG(tooltip)
        self.fullscreen_cam_grab.setToolTip(QCoreApplication.translate("MainWindow", u"Full screen", None))
#endif // QT_CONFIG(tooltip)
        self.fullscreen_cam_grab.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Dorma", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

