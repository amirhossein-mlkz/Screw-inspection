# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(1168, 783)
        MainWindow.setMinimumSize(QSize(0, 28))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(17)
        self.centralwidget.setFont(font)
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
"	background-color: rgb(40, 44, 52);\n"
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
"	border-left:12px solid transparent;\n"
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
"	background-color: rgb(40, 44, 52);\n"
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
"\n"
"/* /////////////////////"
                        "////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(210,210,150);\n"
"	border-radius: 2px;\n"
"	border: 1px solid rgb(33, 37, 43);\n"
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
"Q"
                        "PlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
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
"    subcontrol-origin: margin;"
                        "\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
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
"     s"
                        "ubcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
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
"    back"
                        "ground: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #78AD40;\n"
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
"QSlide"
                        "r::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
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
"	color: rgb(255, 170, 255"
                        ");\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 1px solid rgb(52, 59, 72);\n"
"	border-radius: 3px;	\n"
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
"#frame_28 QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}")
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
        self.topLogoInfo.setStyleSheet(u"")
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
        icon.addFile(u"images/setting_main_window/toogle_down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toogle_btn_1.setIcon(icon)
        self.toogle_btn_1.setIconSize(QSize(16, 16))

        self.horizontalLayout_27.addWidget(self.toogle_btn_1)


        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setStyleSheet(u"")
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
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.side_dashboard_btn.setFont(font1)
        self.side_dashboard_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_dashboard_btn.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u"images/setting_main_window/dashboard_orange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_dashboard_btn.setIcon(icon1)
        self.side_dashboard_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_8.addWidget(self.side_dashboard_btn)

        self.side_tool_setting_btn = QPushButton(self.topMenu)
        self.side_tool_setting_btn.setObjectName(u"side_tool_setting_btn")
        self.side_tool_setting_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.side_tool_setting_btn.sizePolicy().hasHeightForWidth())
        self.side_tool_setting_btn.setSizePolicy(sizePolicy)
        self.side_tool_setting_btn.setMinimumSize(QSize(0, 45))
        self.side_tool_setting_btn.setFont(font1)
        self.side_tool_setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_tool_setting_btn.setLayoutDirection(Qt.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u"images/setting_main_window/tools_setting_orange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_tool_setting_btn.setIcon(icon2)
        self.side_tool_setting_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_8.addWidget(self.side_tool_setting_btn)

        self.side_camera_setting_btn = QPushButton(self.topMenu)
        self.side_camera_setting_btn.setObjectName(u"side_camera_setting_btn")
        self.side_camera_setting_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.side_camera_setting_btn.sizePolicy().hasHeightForWidth())
        self.side_camera_setting_btn.setSizePolicy(sizePolicy)
        self.side_camera_setting_btn.setMinimumSize(QSize(0, 45))
        self.side_camera_setting_btn.setFont(font1)
        self.side_camera_setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_camera_setting_btn.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u"images/setting_main_window/camera_setting_orange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_camera_setting_btn.setIcon(icon3)
        self.side_camera_setting_btn.setIconSize(QSize(38, 38))

        self.verticalLayout_8.addWidget(self.side_camera_setting_btn)

        self.side_calibration_setting_btn = QPushButton(self.topMenu)
        self.side_calibration_setting_btn.setObjectName(u"side_calibration_setting_btn")
        self.side_calibration_setting_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.side_calibration_setting_btn.sizePolicy().hasHeightForWidth())
        self.side_calibration_setting_btn.setSizePolicy(sizePolicy)
        self.side_calibration_setting_btn.setMinimumSize(QSize(0, 45))
        self.side_calibration_setting_btn.setFont(font1)
        self.side_calibration_setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_calibration_setting_btn.setLayoutDirection(Qt.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u"images/setting_main_window/calibration_setting_orange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_calibration_setting_btn.setIcon(icon4)
        self.side_calibration_setting_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_8.addWidget(self.side_calibration_setting_btn)

        self.side_users_setting_btn = QPushButton(self.topMenu)
        self.side_users_setting_btn.setObjectName(u"side_users_setting_btn")
        self.side_users_setting_btn.setEnabled(False)
        sizePolicy.setHeightForWidth(self.side_users_setting_btn.sizePolicy().hasHeightForWidth())
        self.side_users_setting_btn.setSizePolicy(sizePolicy)
        self.side_users_setting_btn.setMinimumSize(QSize(0, 45))
        self.side_users_setting_btn.setFont(font1)
        self.side_users_setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_users_setting_btn.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u"images/setting_main_window/users_setting_orange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_users_setting_btn.setIcon(icon5)
        self.side_users_setting_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_8.addWidget(self.side_users_setting_btn)

        self.side_general_setting_btn = QPushButton(self.topMenu)
        self.side_general_setting_btn.setObjectName(u"side_general_setting_btn")
        self.side_general_setting_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.side_general_setting_btn.sizePolicy().hasHeightForWidth())
        self.side_general_setting_btn.setSizePolicy(sizePolicy)
        self.side_general_setting_btn.setMinimumSize(QSize(0, 45))
        self.side_general_setting_btn.setFont(font1)
        self.side_general_setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_general_setting_btn.setLayoutDirection(Qt.LeftToRight)
        icon6 = QIcon()
        icon6.addFile(u"images/setting_main_window/general_setting_orange.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_general_setting_btn.setIcon(icon6)
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
        self.main_login_btn.setFont(font1)
        self.main_login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.main_login_btn.setLayoutDirection(Qt.RightToLeft)
        icon7 = QIcon()
        icon7.addFile(u"../../../../../home/milad/.designer/backup/images/login_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.main_login_btn.setIcon(icon7)
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
        self.contentTopBg.setStyleSheet(u"")
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
        self.label_dorsa.setPixmap(QPixmap(u"../../../../../home/milad/.designer/backup/images/images/whitew.png"))
        self.label_dorsa.setScaledContents(True)
        self.label_dorsa.setMargin(-11)

        self.horizontalLayout_3.addWidget(self.label_dorsa, 0, Qt.AlignLeft)

        self.toogle_btn_2 = QPushButton(self.leftBox)
        self.toogle_btn_2.setObjectName(u"toogle_btn_2")
        self.toogle_btn_2.setMinimumSize(QSize(0, 30))
        self.toogle_btn_2.setMaximumSize(QSize(0, 30))
        icon8 = QIcon()
        icon8.addFile(u"images/setting_main_window/toogle_left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toogle_btn_2.setIcon(icon8)
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
        icon9 = QIcon()
        icon9.addFile(u"../../../../../home/milad/.designer/backup/images/enter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon9)
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
        icon10 = QIcon()
        icon10.addFile(u"images/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.miniButton.setIcon(icon10)
        self.miniButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.miniButton)

        self.maxiButton = QPushButton(self.rightButtons)
        self.maxiButton.setObjectName(u"maxiButton")
        self.maxiButton.setMinimumSize(QSize(28, 28))
        self.maxiButton.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maxiButton.setFont(font2)
        self.maxiButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u"images/icons/cil-rectangle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxiButton.setIcon(icon11)
        self.maxiButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maxiButton)

        self.closeButton = QPushButton(self.rightButtons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(28, 28))
        self.closeButton.setMaximumSize(QSize(28, 28))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u"images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon12)
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
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(8, 0, 9, 0)
        self.frame_66 = QFrame(self.page_dashboard)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(0, 73))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_14 = QFrame(self.frame_66)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(590, 500))
        self.frame_14.setMaximumSize(QSize(9000, 16777215))
        self.frame_14.setFrameShape(QFrame.Box)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_14.setLineWidth(2)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 3, 0, 2)
        self.frame_147 = QFrame(self.frame_14)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_147)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_20 = QLabel(self.frame_147)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_20, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_21)

        self.label_img_top_live = QLabel(self.frame_147)
        self.label_img_top_live.setObjectName(u"label_img_top_live")
        self.label_img_top_live.setFrameShape(QFrame.Box)
        self.label_img_top_live.setFrameShadow(QFrame.Raised)
        self.label_img_top_live.setScaledContents(True)
        self.label_img_top_live.setMargin(1)

        self.verticalLayout_4.addWidget(self.label_img_top_live, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_22)

        self.line_37 = QFrame(self.frame_147)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.HLine)
        self.line_37.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_37)

        self.frame_45 = QFrame(self.frame_147)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(266, 47))
        self.frame_45.setMaximumSize(QSize(500, 47))
        self.frame_45.setFrameShape(QFrame.Panel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.frame_45.setLineWidth(1)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.btn_enabel_mask_draw_live_side = QCheckBox(self.frame_45)
        self.btn_enabel_mask_draw_live_side.setObjectName(u"btn_enabel_mask_draw_live_side")

        self.horizontalLayout_18.addWidget(self.btn_enabel_mask_draw_live_side)

        self.btn_save_top_cam_live_page = QPushButton(self.frame_45)
        self.btn_save_top_cam_live_page.setObjectName(u"btn_save_top_cam_live_page")
        self.btn_save_top_cam_live_page.setMaximumSize(QSize(50, 50))
        self.btn_save_top_cam_live_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_top_cam_live_page.setStyleSheet(u"border:None;")
        icon13 = QIcon()
        icon13.addFile(u"images/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_top_cam_live_page.setIcon(icon13)
        self.btn_save_top_cam_live_page.setIconSize(QSize(26, 40))

        self.horizontalLayout_18.addWidget(self.btn_save_top_cam_live_page)


        self.verticalLayout_4.addWidget(self.frame_45)


        self.horizontalLayout_89.addWidget(self.frame_147)

        self.frame_139 = QFrame(self.frame_14)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setMinimumSize(QSize(0, 0))
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_139)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_21 = QLabel(self.frame_139)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_20.addWidget(self.label_21, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_23)

        self.label_img_side_live = QLabel(self.frame_139)
        self.label_img_side_live.setObjectName(u"label_img_side_live")
        self.label_img_side_live.setFrameShape(QFrame.Box)
        self.label_img_side_live.setFrameShadow(QFrame.Raised)
        self.label_img_side_live.setScaledContents(True)
        self.label_img_side_live.setMargin(1)

        self.verticalLayout_20.addWidget(self.label_img_side_live, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_24)

        self.line_38 = QFrame(self.frame_139)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.HLine)
        self.line_38.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_20.addWidget(self.line_38)

        self.frame_22 = QFrame(self.frame_139)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(266, 47))
        self.frame_22.setMaximumSize(QSize(500, 47))
        self.frame_22.setFrameShape(QFrame.Panel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_22.setLineWidth(1)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.btn_enabel_mask_draw_live_top = QCheckBox(self.frame_22)
        self.btn_enabel_mask_draw_live_top.setObjectName(u"btn_enabel_mask_draw_live_top")
        self.btn_enabel_mask_draw_live_top.setChecked(False)

        self.horizontalLayout_78.addWidget(self.btn_enabel_mask_draw_live_top)

        self.btn_save_side_cam_live_page = QPushButton(self.frame_22)
        self.btn_save_side_cam_live_page.setObjectName(u"btn_save_side_cam_live_page")
        self.btn_save_side_cam_live_page.setMaximumSize(QSize(50, 50))
        self.btn_save_side_cam_live_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_side_cam_live_page.setStyleSheet(u"border:None;")
        self.btn_save_side_cam_live_page.setIcon(icon13)
        self.btn_save_side_cam_live_page.setIconSize(QSize(26, 40))

        self.horizontalLayout_78.addWidget(self.btn_save_side_cam_live_page)


        self.verticalLayout_20.addWidget(self.frame_22, 0, Qt.AlignHCenter)


        self.horizontalLayout_89.addWidget(self.frame_139)


        self.horizontalLayout_7.addWidget(self.frame_14)

        self.line_13 = QFrame(self.frame_66)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_13)

        self.frame_67 = QFrame(self.frame_66)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(456, 0))
        self.frame_67.setFrameShape(QFrame.Box)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.frame_67.setLineWidth(2)
        self.verticalLayout_23 = QVBoxLayout(self.frame_67)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_18 = QFrame(self.frame_67)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(54, 0))
        self.frame_18.setMaximumSize(QSize(550, 205))
        self.frame_18.setFrameShape(QFrame.Box)
        self.frame_18.setFrameShadow(QFrame.Plain)
        self.frame_18.setLineWidth(1)
        self.verticalLayout_58 = QVBoxLayout(self.frame_18)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.frame_220 = QFrame(self.frame_18)
        self.frame_220.setObjectName(u"frame_220")
        self.frame_220.setFrameShape(QFrame.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_196 = QHBoxLayout(self.frame_220)
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.horizontalLayout_196.setContentsMargins(0, 0, 0, 0)
        self.groupBox_29 = QGroupBox(self.frame_220)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.horizontalLayout_195 = QHBoxLayout(self.groupBox_29)
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.horizontalLayout_195.setContentsMargins(0, 0, 0, 0)
        self.frame_64 = QFrame(self.groupBox_29)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMaximumSize(QSize(340, 42))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.connect_cameras_live_page = QPushButton(self.frame_64)
        self.connect_cameras_live_page.setObjectName(u"connect_cameras_live_page")
        self.connect_cameras_live_page.setMinimumSize(QSize(50, 32))
        self.connect_cameras_live_page.setMaximumSize(QSize(50, 32))
        self.connect_cameras_live_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.connect_cameras_live_page.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(200,200,200);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"images/connect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_cameras_live_page.setIcon(icon14)
        self.connect_cameras_live_page.setIconSize(QSize(41, 26))

        self.horizontalLayout_70.addWidget(self.connect_cameras_live_page)

        self.line_camera_status = QLineEdit(self.frame_64)
        self.line_camera_status.setObjectName(u"line_camera_status")
        self.line_camera_status.setMinimumSize(QSize(0, 26))
        self.line_camera_status.setReadOnly(True)

        self.horizontalLayout_70.addWidget(self.line_camera_status)

        self.disconnect_cameras_live_page = QPushButton(self.frame_64)
        self.disconnect_cameras_live_page.setObjectName(u"disconnect_cameras_live_page")
        self.disconnect_cameras_live_page.setEnabled(False)
        self.disconnect_cameras_live_page.setMinimumSize(QSize(50, 32))
        self.disconnect_cameras_live_page.setMaximumSize(QSize(50, 32))
        self.disconnect_cameras_live_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.disconnect_cameras_live_page.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(200,200,200);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"images/disconnected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.disconnect_cameras_live_page.setIcon(icon15)
        self.disconnect_cameras_live_page.setIconSize(QSize(41, 26))

        self.horizontalLayout_70.addWidget(self.disconnect_cameras_live_page)


        self.horizontalLayout_195.addWidget(self.frame_64)


        self.horizontalLayout_196.addWidget(self.groupBox_29)

        self.groupBox_14 = QGroupBox(self.frame_220)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(0, 43))
        self.horizontalLayout_182 = QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_182.setSpacing(2)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(0, 0, 0, 0)
        self.label_176 = QLabel(self.groupBox_14)
        self.label_176.setObjectName(u"label_176")

        self.horizontalLayout_182.addWidget(self.label_176)

        self.plc_status_live_page = QLabel(self.groupBox_14)
        self.plc_status_live_page.setObjectName(u"plc_status_live_page")

        self.horizontalLayout_182.addWidget(self.plc_status_live_page)

        self.label_179 = QLabel(self.groupBox_14)
        self.label_179.setObjectName(u"label_179")

        self.horizontalLayout_182.addWidget(self.label_179)

        self.plc_mode_live_page = QLabel(self.groupBox_14)
        self.plc_mode_live_page.setObjectName(u"plc_mode_live_page")

        self.horizontalLayout_182.addWidget(self.plc_mode_live_page)

        self.label_183 = QLabel(self.groupBox_14)
        self.label_183.setObjectName(u"label_183")

        self.horizontalLayout_182.addWidget(self.label_183)

        self.plc_reject_live_page = QLabel(self.groupBox_14)
        self.plc_reject_live_page.setObjectName(u"plc_reject_live_page")

        self.horizontalLayout_182.addWidget(self.plc_reject_live_page)


        self.horizontalLayout_196.addWidget(self.groupBox_14)


        self.verticalLayout_58.addWidget(self.frame_220)

        self.line_17 = QFrame(self.frame_18)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_58.addWidget(self.line_17)

        self.frame_62 = QFrame(self.frame_18)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMaximumSize(QSize(16777215, 40))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_62)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(100, 0))
        self.label_29.setMaximumSize(QSize(104, 16777215))

        self.horizontalLayout_63.addWidget(self.label_29)

        self.combobox_select_screw_live = QComboBox(self.frame_62)
        self.combobox_select_screw_live.setObjectName(u"combobox_select_screw_live")

        self.horizontalLayout_63.addWidget(self.combobox_select_screw_live)

        self.pushButton_5 = QPushButton(self.frame_62)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(81, 25))
        self.pushButton_5.setMaximumSize(QSize(70, 16777215))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_63.addWidget(self.pushButton_5)

        self.history_btn = QPushButton(self.frame_62)
        self.history_btn.setObjectName(u"history_btn")
        self.history_btn.setMinimumSize(QSize(81, 25))
        self.history_btn.setMaximumSize(QSize(70, 16777215))
        self.history_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_63.addWidget(self.history_btn)


        self.verticalLayout_58.addWidget(self.frame_62)

        self.frame_75 = QFrame(self.frame_18)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(-1, 0, -1, 0)
        self.label_selected_screw_top_live = QLabel(self.frame_75)
        self.label_selected_screw_top_live.setObjectName(u"label_selected_screw_top_live")
        self.label_selected_screw_top_live.setMinimumSize(QSize(66, 66))
        self.label_selected_screw_top_live.setMaximumSize(QSize(66, 66))
        self.label_selected_screw_top_live.setFrameShape(QFrame.WinPanel)
        self.label_selected_screw_top_live.setFrameShadow(QFrame.Plain)
        self.label_selected_screw_top_live.setLineWidth(3)
        self.label_selected_screw_top_live.setPixmap(QPixmap(u"../../../../../home/milad/.designer/backup/sample images/New folder/31x_1_2.png"))
        self.label_selected_screw_top_live.setScaledContents(True)
        self.label_selected_screw_top_live.setMargin(0)

        self.horizontalLayout_112.addWidget(self.label_selected_screw_top_live)

        self.label_selected_screw_side_live = QLabel(self.frame_75)
        self.label_selected_screw_side_live.setObjectName(u"label_selected_screw_side_live")
        self.label_selected_screw_side_live.setMinimumSize(QSize(41, 66))
        self.label_selected_screw_side_live.setMaximumSize(QSize(41, 66))
        self.label_selected_screw_side_live.setFrameShape(QFrame.WinPanel)
        self.label_selected_screw_side_live.setLineWidth(3)
        self.label_selected_screw_side_live.setPixmap(QPixmap(u"../../../../../home/milad/.designer/backup/sample images/New folder/42x_0_20.png"))
        self.label_selected_screw_side_live.setScaledContents(True)

        self.horizontalLayout_112.addWidget(self.label_selected_screw_side_live)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_112.addItem(self.horizontalSpacer_35)

        self.frame_219 = QFrame(self.frame_75)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setMinimumSize(QSize(0, 34))
        self.frame_219.setFrameShape(QFrame.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.frame_219)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(-1, 0, -1, 0)
        self.start_capture_live_page = QPushButton(self.frame_219)
        self.start_capture_live_page.setObjectName(u"start_capture_live_page")
        self.start_capture_live_page.setMinimumSize(QSize(130, 32))
        self.start_capture_live_page.setMaximumSize(QSize(50, 32))
        self.start_capture_live_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_capture_live_page.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(200,200,200);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.start_capture_live_page.setIconSize(QSize(41, 26))

        self.verticalLayout_138.addWidget(self.start_capture_live_page)

        self.stop_capture_live_page = QPushButton(self.frame_219)
        self.stop_capture_live_page.setObjectName(u"stop_capture_live_page")
        self.stop_capture_live_page.setMinimumSize(QSize(130, 32))
        self.stop_capture_live_page.setMaximumSize(QSize(50, 32))
        self.stop_capture_live_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_capture_live_page.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(200,200,200);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.stop_capture_live_page.setIconSize(QSize(41, 26))

        self.verticalLayout_138.addWidget(self.stop_capture_live_page)


        self.horizontalLayout_112.addWidget(self.frame_219)


        self.verticalLayout_58.addWidget(self.frame_75, 0, Qt.AlignHCenter)


        self.verticalLayout_23.addWidget(self.frame_18, 0, Qt.AlignHCenter)

        self.line_19 = QFrame(self.frame_67)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line_19)

        self.verticalSpacer_14 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_23.addItem(self.verticalSpacer_14)

        self.groupBox_19 = QGroupBox(self.frame_67)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.verticalLayout_136 = QVBoxLayout(self.groupBox_19)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(2, 2, 2, 2)
        self.table_live_top_live_page = QTableWidget(self.groupBox_19)
        if (self.table_live_top_live_page.columnCount() < 6):
            self.table_live_top_live_page.setColumnCount(6)
        if (self.table_live_top_live_page.rowCount() < 9):
            self.table_live_top_live_page.setRowCount(9)
        self.table_live_top_live_page.setObjectName(u"table_live_top_live_page")
        self.table_live_top_live_page.setStyleSheet(u"QTableWidget {	\n"
"	padding: 1px;\n"
"	border-radius:1px;\n"
"	gridline-color: rgb(190,170,160);\n"
"	border-bottom: 1px solid rgb(180,180,180);\n"
"	color:rgb(255,255,255);\n"
"\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(0,0,0);\n"
"	padding: 3px;\n"
"    background-color: rgb(30,30,30);\n"
"\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0,0,0);\n"
"background-color: rgb(30,30,30);\n"
"color:rgb(255,255,255);\n"
"\n"
"}\n"
"")
        self.table_live_top_live_page.setInputMethodHints(Qt.ImhNone)
        self.table_live_top_live_page.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_live_top_live_page.setTextElideMode(Qt.ElideMiddle)
        self.table_live_top_live_page.setSortingEnabled(True)
        self.table_live_top_live_page.setRowCount(9)
        self.table_live_top_live_page.setColumnCount(6)
        self.table_live_top_live_page.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_live_top_live_page.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_136.addWidget(self.table_live_top_live_page)


        self.verticalLayout_23.addWidget(self.groupBox_19)

        self.line_39 = QFrame(self.frame_67)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.HLine)
        self.line_39.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line_39)

        self.groupBox_21 = QGroupBox(self.frame_67)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.verticalLayout_137 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(2, 2, 2, 2)
        self.table_live_side_live_page = QTableWidget(self.groupBox_21)
        if (self.table_live_side_live_page.columnCount() < 6):
            self.table_live_side_live_page.setColumnCount(6)
        if (self.table_live_side_live_page.rowCount() < 9):
            self.table_live_side_live_page.setRowCount(9)
        self.table_live_side_live_page.setObjectName(u"table_live_side_live_page")
        self.table_live_side_live_page.setStyleSheet(u"QTableWidget {	\n"
"	padding: 1px;\n"
"	border-radius:1px;\n"
"	gridline-color: rgb(190,170,160);\n"
"	border-bottom: 1px solid rgb(180,180,180);\n"
"	color:rgb(255,255,255);\n"
"\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(0,0,0);\n"
"	padding: 3px;\n"
"    background-color: rgb(30,30,30);\n"
"\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0,0,0);\n"
"background-color: rgb(30,30,30);\n"
"color:rgb(255,255,255);\n"
"\n"
"}\n"
"")
        self.table_live_side_live_page.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_live_side_live_page.setRowCount(9)
        self.table_live_side_live_page.setColumnCount(6)

        self.verticalLayout_137.addWidget(self.table_live_side_live_page)


        self.verticalLayout_23.addWidget(self.groupBox_21)


        self.horizontalLayout_7.addWidget(self.frame_67)


        self.verticalLayout_7.addWidget(self.frame_66)

        self.frame_15 = QFrame(self.page_dashboard)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 200))
        self.frame_15.setFrameShape(QFrame.Panel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_15.setLineWidth(1)
        self.frame_15.setMidLineWidth(0)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 9)
        self.bottomBar = QFrame(self.frame_15)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"background-color:white;")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(False)
        font3.setItalic(False)
        self.creditsLabel.setFont(font3)
        self.creditsLabel.setStyleSheet(u"color:black;")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setStyleSheet(u"color:black;")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.horizontalLayout_14.addWidget(self.bottomBar)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.page_dashboard)
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
        self.add_btn.setEnabled(True)
        self.add_btn.setMinimumSize(QSize(0, 35))
        self.add_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_btn.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")

        self.horizontalLayout_19.addWidget(self.add_btn)

        self.edit_remove_btn = QPushButton(self.frame_13)
        self.edit_remove_btn.setObjectName(u"edit_remove_btn")
        self.edit_remove_btn.setMinimumSize(QSize(0, 35))
        self.edit_remove_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_remove_btn.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")

        self.horizontalLayout_19.addWidget(self.edit_remove_btn)


        self.horizontalLayout_16.addWidget(self.frame_13)

        self.line_10 = QFrame(self.frame_2)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_10)

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
        self.edit_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_btn.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")

        self.horizontalLayout_20.addWidget(self.edit_btn)

        self.remove_screw_btn = QPushButton(self.frame_24)
        self.remove_screw_btn.setObjectName(u"remove_screw_btn")
        self.remove_screw_btn.setMinimumSize(QSize(69, 27))
        self.remove_screw_btn.setMaximumSize(QSize(60, 16777215))
        self.remove_screw_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_screw_btn.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")

        self.horizontalLayout_20.addWidget(self.remove_screw_btn)


        self.horizontalLayout_16.addWidget(self.frame_24)

        self.frame_23 = QFrame(self.frame_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 0))
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
        self.save_new_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_21.addWidget(self.save_new_btn)


        self.horizontalLayout_16.addWidget(self.frame_23)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_16.addWidget(self.label_6)

        self.label_screw_name = QLabel(self.frame_2)
        self.label_screw_name.setObjectName(u"label_screw_name")

        self.horizontalLayout_16.addWidget(self.label_screw_name)

        self.horizontalSpacer_15 = QSpacerItem(17, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)

        self.label_status_mode = QLabel(self.frame_2)
        self.label_status_mode.setObjectName(u"label_status_mode")
        palette = QPalette()
        brush = QBrush(QColor(194, 194, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(243, 246, 254, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 0, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        brush4 = QBrush(QColor(190, 190, 190, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.label_status_mode.setPalette(palette)
        font4 = QFont()
        font4.setPointSize(12)
        self.label_status_mode.setFont(font4)

        self.horizontalLayout_16.addWidget(self.label_status_mode)

        self.horizontalSpacer_9 = QSpacerItem(86, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_9)

        self.label_warning_tool_page = QLabel(self.frame_2)
        self.label_warning_tool_page.setObjectName(u"label_warning_tool_page")
        self.label_warning_tool_page.setMaximumSize(QSize(16777215, 37))

        self.horizontalLayout_16.addWidget(self.label_warning_tool_page)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer)


        self.verticalLayout_26.addWidget(self.frame_2)

        self.line_9 = QFrame(self.page_tools)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line_9)

        self.frame_4 = QFrame(self.page_tools)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_25 = QFrame(self.frame_4)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(222, 0))
        self.frame_25.setMaximumSize(QSize(200, 16777215))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_25)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(209, 0))
        self.frame_28.setFrameShape(QFrame.Box)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.frame_28.setLineWidth(2)
        self.verticalLayout_49 = QVBoxLayout(self.frame_28)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.groupBox_23 = QGroupBox(self.frame_28)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.verticalLayout_62 = QVBoxLayout(self.groupBox_23)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.frame_33 = QFrame(self.groupBox_23)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.checkbox_page0_1_top = QCheckBox(self.frame_33)
        self.checkbox_page0_1_top.setObjectName(u"checkbox_page0_1_top")
        self.checkbox_page0_1_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkbox_page0_1_top.setChecked(True)

        self.horizontalLayout_43.addWidget(self.checkbox_page0_1_top)

        self.btn_page0_1_top = QPushButton(self.frame_33)
        self.btn_page0_1_top.setObjectName(u"btn_page0_1_top")
        self.btn_page0_1_top.setEnabled(False)
        self.btn_page0_1_top.setMinimumSize(QSize(100, 25))
        self.btn_page0_1_top.setMaximumSize(QSize(100, 16777215))
        self.btn_page0_1_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page0_1_top.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.btn_page0_1_top.setCheckable(False)
        self.btn_page0_1_top.setChecked(False)

        self.horizontalLayout_43.addWidget(self.btn_page0_1_top)


        self.verticalLayout_62.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.groupBox_23)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setEnabled(False)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.checkbox_page0_2_top = QCheckBox(self.frame_34)
        self.checkbox_page0_2_top.setObjectName(u"checkbox_page0_2_top")
        self.checkbox_page0_2_top.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_44.addWidget(self.checkbox_page0_2_top)

        self.btn_page0_2_top = QPushButton(self.frame_34)
        self.btn_page0_2_top.setObjectName(u"btn_page0_2_top")
        self.btn_page0_2_top.setEnabled(False)
        self.btn_page0_2_top.setMinimumSize(QSize(100, 25))
        self.btn_page0_2_top.setMaximumSize(QSize(100, 16777215))
        palette1 = QPalette()
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush7 = QBrush(QColor(255, 255, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        brush8 = QBrush(QColor(50, 50, 50, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.btn_page0_2_top.setPalette(palette1)
        self.btn_page0_2_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page0_2_top.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.btn_page0_2_top.setCheckable(False)
        self.btn_page0_2_top.setChecked(False)
        self.btn_page0_2_top.setAutoDefault(False)

        self.horizontalLayout_44.addWidget(self.btn_page0_2_top)


        self.verticalLayout_62.addWidget(self.frame_34)

        self.frame_53 = QFrame(self.groupBox_23)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setEnabled(False)
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.checkbox_page0_3_top = QCheckBox(self.frame_53)
        self.checkbox_page0_3_top.setObjectName(u"checkbox_page0_3_top")
        self.checkbox_page0_3_top.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_55.addWidget(self.checkbox_page0_3_top)

        self.btn_page0_3_top = QPushButton(self.frame_53)
        self.btn_page0_3_top.setObjectName(u"btn_page0_3_top")
        self.btn_page0_3_top.setEnabled(False)
        self.btn_page0_3_top.setMinimumSize(QSize(100, 25))
        self.btn_page0_3_top.setMaximumSize(QSize(100, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.btn_page0_3_top.setPalette(palette2)
        self.btn_page0_3_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page0_3_top.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.btn_page0_3_top.setCheckable(False)
        self.btn_page0_3_top.setChecked(False)

        self.horizontalLayout_55.addWidget(self.btn_page0_3_top)


        self.verticalLayout_62.addWidget(self.frame_53)

        self.frame_190 = QFrame(self.groupBox_23)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setEnabled(False)
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_190)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.checkbox_page0_4_top = QCheckBox(self.frame_190)
        self.checkbox_page0_4_top.setObjectName(u"checkbox_page0_4_top")
        self.checkbox_page0_4_top.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_69.addWidget(self.checkbox_page0_4_top)

        self.btn_page0_4_top = QPushButton(self.frame_190)
        self.btn_page0_4_top.setObjectName(u"btn_page0_4_top")
        self.btn_page0_4_top.setEnabled(False)
        self.btn_page0_4_top.setMinimumSize(QSize(100, 25))
        self.btn_page0_4_top.setMaximumSize(QSize(100, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.btn_page0_4_top.setPalette(palette3)
        self.btn_page0_4_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page0_4_top.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.btn_page0_4_top.setCheckable(False)
        self.btn_page0_4_top.setChecked(False)

        self.horizontalLayout_69.addWidget(self.btn_page0_4_top)


        self.verticalLayout_62.addWidget(self.frame_190)

        self.frame_212 = QFrame(self.groupBox_23)
        self.frame_212.setObjectName(u"frame_212")
        self.frame_212.setEnabled(False)
        self.frame_212.setFrameShape(QFrame.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_189 = QHBoxLayout(self.frame_212)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.checkbox_page0_5_top = QCheckBox(self.frame_212)
        self.checkbox_page0_5_top.setObjectName(u"checkbox_page0_5_top")
        self.checkbox_page0_5_top.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_189.addWidget(self.checkbox_page0_5_top)

        self.btn_page0_5_top = QPushButton(self.frame_212)
        self.btn_page0_5_top.setObjectName(u"btn_page0_5_top")
        self.btn_page0_5_top.setEnabled(False)
        self.btn_page0_5_top.setMinimumSize(QSize(100, 25))
        self.btn_page0_5_top.setMaximumSize(QSize(100, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.btn_page0_5_top.setPalette(palette4)
        self.btn_page0_5_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page0_5_top.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.btn_page0_5_top.setCheckable(False)
        self.btn_page0_5_top.setChecked(False)

        self.horizontalLayout_189.addWidget(self.btn_page0_5_top)


        self.verticalLayout_62.addWidget(self.frame_212)


        self.verticalLayout_49.addWidget(self.groupBox_23)

        self.groupBox_22 = QGroupBox(self.frame_28)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.verticalLayout_61 = QVBoxLayout(self.groupBox_22)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.frame_35 = QFrame(self.groupBox_22)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.checkbox_page0_1_side = QCheckBox(self.frame_35)
        self.checkbox_page0_1_side.setObjectName(u"checkbox_page0_1_side")
        self.checkbox_page0_1_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkbox_page0_1_side.setChecked(True)

        self.horizontalLayout_45.addWidget(self.checkbox_page0_1_side)

        self.btn_page0_1_side = QPushButton(self.frame_35)
        self.btn_page0_1_side.setObjectName(u"btn_page0_1_side")
        self.btn_page0_1_side.setEnabled(False)
        self.btn_page0_1_side.setMinimumSize(QSize(100, 25))
        self.btn_page0_1_side.setMaximumSize(QSize(100, 16777215))
        self.btn_page0_1_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page0_1_side.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.btn_page0_1_side.setCheckable(False)
        self.btn_page0_1_side.setChecked(False)

        self.horizontalLayout_45.addWidget(self.btn_page0_1_side)


        self.verticalLayout_61.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.groupBox_22)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setEnabled(True)
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.checkbox_page0_2_side = QCheckBox(self.frame_36)
        self.checkbox_page0_2_side.setObjectName(u"checkbox_page0_2_side")
        self.checkbox_page0_2_side.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_46.addWidget(self.checkbox_page0_2_side)

        self.btn_page0_2_side = QPushButton(self.frame_36)
        self.btn_page0_2_side.setObjectName(u"btn_page0_2_side")
        self.btn_page0_2_side.setEnabled(False)
        self.btn_page0_2_side.setMinimumSize(QSize(100, 25))
        self.btn_page0_2_side.setMaximumSize(QSize(100, 16777215))
        self.btn_page0_2_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page0_2_side.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.btn_page0_2_side.setCheckable(False)
        self.btn_page0_2_side.setChecked(False)

        self.horizontalLayout_46.addWidget(self.btn_page0_2_side)


        self.verticalLayout_61.addWidget(self.frame_36)

        self.frame_78 = QFrame(self.groupBox_22)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setEnabled(True)
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.checkbox_page0_3_side = QCheckBox(self.frame_78)
        self.checkbox_page0_3_side.setObjectName(u"checkbox_page0_3_side")
        self.checkbox_page0_3_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkbox_page0_3_side.setChecked(True)

        self.horizontalLayout_117.addWidget(self.checkbox_page0_3_side)

        self.btn_page0_3_side = QPushButton(self.frame_78)
        self.btn_page0_3_side.setObjectName(u"btn_page0_3_side")
        self.btn_page0_3_side.setEnabled(False)
        self.btn_page0_3_side.setMinimumSize(QSize(100, 25))
        self.btn_page0_3_side.setMaximumSize(QSize(100, 16777215))
        self.btn_page0_3_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page0_3_side.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.btn_page0_3_side.setCheckable(False)
        self.btn_page0_3_side.setChecked(False)

        self.horizontalLayout_117.addWidget(self.btn_page0_3_side)


        self.verticalLayout_61.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.groupBox_22)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setEnabled(False)
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.checkbox_page0_4_side = QCheckBox(self.frame_79)
        self.checkbox_page0_4_side.setObjectName(u"checkbox_page0_4_side")
        self.checkbox_page0_4_side.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_118.addWidget(self.checkbox_page0_4_side)

        self.btn_page0_4_side = QPushButton(self.frame_79)
        self.btn_page0_4_side.setObjectName(u"btn_page0_4_side")
        self.btn_page0_4_side.setMinimumSize(QSize(100, 25))
        self.btn_page0_4_side.setMaximumSize(QSize(100, 16777215))
        self.btn_page0_4_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page0_4_side.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.btn_page0_4_side.setCheckable(False)
        self.btn_page0_4_side.setChecked(False)

        self.horizontalLayout_118.addWidget(self.btn_page0_4_side)


        self.verticalLayout_61.addWidget(self.frame_79)

        self.frame_2284 = QFrame(self.groupBox_22)
        self.frame_2284.setObjectName(u"frame_2284")
        self.frame_2284.setEnabled(False)
        self.frame_2284.setFrameShape(QFrame.StyledPanel)
        self.frame_2284.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.frame_2284)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.checkbox_page0_5_side = QCheckBox(self.frame_2284)
        self.checkbox_page0_5_side.setObjectName(u"checkbox_page0_5_side")
        self.checkbox_page0_5_side.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_144.addWidget(self.checkbox_page0_5_side)

        self.btn_page0_5_side = QPushButton(self.frame_2284)
        self.btn_page0_5_side.setObjectName(u"btn_page0_5_side")
        self.btn_page0_5_side.setMinimumSize(QSize(100, 25))
        self.btn_page0_5_side.setMaximumSize(QSize(100, 16777215))
        self.btn_page0_5_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page0_5_side.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.btn_page0_5_side.setCheckable(False)
        self.btn_page0_5_side.setChecked(False)

        self.horizontalLayout_144.addWidget(self.btn_page0_5_side)


        self.verticalLayout_61.addWidget(self.frame_2284)

        self.frame_112 = QFrame(self.groupBox_22)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setEnabled(False)
        self.frame_112.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_162 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.checkbox_page0_6_side = QCheckBox(self.frame_112)
        self.checkbox_page0_6_side.setObjectName(u"checkbox_page0_6_side")

        self.horizontalLayout_162.addWidget(self.checkbox_page0_6_side)

        self.btn_page0_6_side = QPushButton(self.frame_112)
        self.btn_page0_6_side.setObjectName(u"btn_page0_6_side")
        self.btn_page0_6_side.setEnabled(False)
        self.btn_page0_6_side.setMinimumSize(QSize(100, 25))
        self.btn_page0_6_side.setMaximumSize(QSize(100, 16777215))
        self.btn_page0_6_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page0_6_side.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")
        self.btn_page0_6_side.setCheckable(False)
        self.btn_page0_6_side.setChecked(False)

        self.horizontalLayout_162.addWidget(self.btn_page0_6_side)


        self.verticalLayout_61.addWidget(self.frame_112)


        self.verticalLayout_49.addWidget(self.groupBox_22)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_7)


        self.verticalLayout_27.addWidget(self.frame_28)


        self.horizontalLayout_22.addWidget(self.frame_25)

        self.line_5 = QFrame(self.frame_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_22.addWidget(self.line_5)

        self.frame_37 = QFrame(self.frame_4)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(408, 62))
        self.frame_37.setMaximumSize(QSize(450, 16777215))
        self.frame_37.setFrameShape(QFrame.Box)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.frame_37.setLineWidth(2)
        self.verticalLayout_30 = QVBoxLayout(self.frame_37)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.stackedWidget_2 = QStackedWidget(self.frame_37)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(200, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget_2.addWidget(self.page)
        self.page_1_top = QWidget()
        self.page_1_top.setObjectName(u"page_1_top")
        self.verticalLayout_29 = QVBoxLayout(self.page_1_top)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_26 = QFrame(self.page_1_top)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_26)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 139))
        self.frame_29.setMaximumSize(QSize(445, 139))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_29)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_29)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_39.addWidget(self.label_19)

        self.groupBox_3 = QGroupBox(self.frame_29)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 54))
        self.horizontalLayout_25 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.line_img_path0_1_top = QLineEdit(self.groupBox_3)
        self.line_img_path0_1_top.setObjectName(u"line_img_path0_1_top")
        self.line_img_path0_1_top.setMinimumSize(QSize(210, 0))
        self.line_img_path0_1_top.setMaximumSize(QSize(405, 16777215))

        self.horizontalLayout_24.addWidget(self.line_img_path0_1_top)

        self.btn_load_image0_1_top = QToolButton(self.groupBox_3)
        self.btn_load_image0_1_top.setObjectName(u"btn_load_image0_1_top")

        self.horizontalLayout_24.addWidget(self.btn_load_image0_1_top)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_24)

        self.btn_set_img0_1_top = QPushButton(self.groupBox_3)
        self.btn_set_img0_1_top.setObjectName(u"btn_set_img0_1_top")
        self.btn_set_img0_1_top.setMinimumSize(QSize(82, 27))
        self.btn_set_img0_1_top.setMaximumSize(QSize(16777215, 27))

        self.horizontalLayout_25.addWidget(self.btn_set_img0_1_top)


        self.verticalLayout_39.addWidget(self.groupBox_3)

        self.frame_211 = QFrame(self.frame_29)
        self.frame_211.setObjectName(u"frame_211")
        self.frame_211.setFrameShape(QFrame.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_188 = QHBoxLayout(self.frame_211)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.label_124 = QLabel(self.frame_211)
        self.label_124.setObjectName(u"label_124")

        self.horizontalLayout_188.addWidget(self.label_124)

        self.btn_connect_camera0_1_top = QPushButton(self.frame_211)
        self.btn_connect_camera0_1_top.setObjectName(u"btn_connect_camera0_1_top")
        self.btn_connect_camera0_1_top.setMinimumSize(QSize(129, 27))
        self.btn_connect_camera0_1_top.setMaximumSize(QSize(16777215, 27))

        self.horizontalLayout_188.addWidget(self.btn_connect_camera0_1_top)


        self.verticalLayout_39.addWidget(self.frame_211)


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

        self.spin_roi_x1_1_top = QSpinBox(self.groupBox_10)
        self.spin_roi_x1_1_top.setObjectName(u"spin_roi_x1_1_top")
        self.spin_roi_x1_1_top.setMaximum(20000)
        self.spin_roi_x1_1_top.setSingleStep(5)

        self.horizontalLayout_47.addWidget(self.spin_roi_x1_1_top)


        self.verticalLayout_36.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_4 = QLabel(self.groupBox_10)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_48.addWidget(self.label_4)

        self.spin_roi_y1_1_top = QSpinBox(self.groupBox_10)
        self.spin_roi_y1_1_top.setObjectName(u"spin_roi_y1_1_top")
        self.spin_roi_y1_1_top.setMaximum(20000)
        self.spin_roi_y1_1_top.setSingleStep(5)

        self.horizontalLayout_48.addWidget(self.spin_roi_y1_1_top)


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

        self.spin_roi_x2_1_top = QSpinBox(self.groupBox_11)
        self.spin_roi_x2_1_top.setObjectName(u"spin_roi_x2_1_top")
        self.spin_roi_x2_1_top.setMaximum(20000)
        self.spin_roi_x2_1_top.setSingleStep(5)

        self.horizontalLayout_49.addWidget(self.spin_roi_x2_1_top)


        self.verticalLayout_37.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_8 = QLabel(self.groupBox_11)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_50.addWidget(self.label_8)

        self.spin_roi_y2_1_top = QSpinBox(self.groupBox_11)
        self.spin_roi_y2_1_top.setObjectName(u"spin_roi_y2_1_top")
        self.spin_roi_y2_1_top.setMaximum(20000)
        self.spin_roi_y2_1_top.setSingleStep(5)

        self.horizontalLayout_50.addWidget(self.spin_roi_y2_1_top)


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

        self.bar_thresh0_1_top = QSlider(self.frame_40)
        self.bar_thresh0_1_top.setObjectName(u"bar_thresh0_1_top")
        self.bar_thresh0_1_top.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_1_top.setMaximum(255)
        self.bar_thresh0_1_top.setOrientation(Qt.Horizontal)

        self.verticalLayout_32.addWidget(self.bar_thresh0_1_top)

        self.spinBox = QSpinBox(self.frame_40)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(255)

        self.verticalLayout_32.addWidget(self.spinBox, 0, Qt.AlignHCenter)

        self.checkbox_thresh_inv0_1_top = QCheckBox(self.frame_40)
        self.checkbox_thresh_inv0_1_top.setObjectName(u"checkbox_thresh_inv0_1_top")

        self.verticalLayout_32.addWidget(self.checkbox_thresh_inv0_1_top)


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

        self.bar_noise_filter0_1_top = QSlider(self.frame_50)
        self.bar_noise_filter0_1_top.setObjectName(u"bar_noise_filter0_1_top")
        self.bar_noise_filter0_1_top.setMaximum(100)
        self.bar_noise_filter0_1_top.setSingleStep(1)
        self.bar_noise_filter0_1_top.setOrientation(Qt.Horizontal)

        self.verticalLayout_38.addWidget(self.bar_noise_filter0_1_top)

        self.noiseAreaSpinBox = QSpinBox(self.frame_50)
        self.noiseAreaSpinBox.setObjectName(u"noiseAreaSpinBox")
        self.noiseAreaSpinBox.setMaximum(100)

        self.verticalLayout_38.addWidget(self.noiseAreaSpinBox, 0, Qt.AlignHCenter)


        self.verticalLayout_34.addWidget(self.frame_50)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_4)


        self.horizontalLayout_41.addWidget(self.frame_32)


        self.verticalLayout_28.addWidget(self.frame_30)


        self.verticalLayout_29.addWidget(self.frame_26)

        self.stackedWidget_2.addWidget(self.page_1_top)
        self.page_2_top = QWidget()
        self.page_2_top.setObjectName(u"page_2_top")
        self.verticalLayout_31 = QVBoxLayout(self.page_2_top)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_57 = QFrame(self.page_2_top)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(16777215, 46))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_12 = QLabel(self.frame_57)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_57.addWidget(self.label_12)

        self.line_name_region0_2_top = QLineEdit(self.frame_57)
        self.line_name_region0_2_top.setObjectName(u"line_name_region0_2_top")

        self.horizontalLayout_57.addWidget(self.line_name_region0_2_top)


        self.verticalLayout_31.addWidget(self.frame_57, 0, Qt.AlignTop)

        self.frame_31 = QFrame(self.page_2_top)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 61))
        self.frame_31.setFrameShape(QFrame.Box)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.btn_add_region0_2_top = QPushButton(self.frame_31)
        self.btn_add_region0_2_top.setObjectName(u"btn_add_region0_2_top")
        self.btn_add_region0_2_top.setMaximumSize(QSize(26, 16777215))
        self.btn_add_region0_2_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_region0_2_top.setStyleSheet(u"border:none;\n"
"")
        icon16 = QIcon()
        icon16.addFile(u"images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_region0_2_top.setIcon(icon16)
        self.btn_add_region0_2_top.setIconSize(QSize(26, 26))

        self.horizontalLayout_40.addWidget(self.btn_add_region0_2_top)

        self.combo_regions_name0_2_top = QComboBox(self.frame_31)
        self.combo_regions_name0_2_top.setObjectName(u"combo_regions_name0_2_top")
        self.combo_regions_name0_2_top.setMinimumSize(QSize(191, 0))
        self.combo_regions_name0_2_top.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_40.addWidget(self.combo_regions_name0_2_top)

        self.btn_remove_region0_2_top = QPushButton(self.frame_31)
        self.btn_remove_region0_2_top.setObjectName(u"btn_remove_region0_2_top")
        self.btn_remove_region0_2_top.setMaximumSize(QSize(26, 16777215))
        self.btn_remove_region0_2_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove_region0_2_top.setStyleSheet(u"border:none;")
        icon17 = QIcon()
        icon17.addFile(u"images/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_region0_2_top.setIcon(icon17)
        self.btn_remove_region0_2_top.setIconSize(QSize(26, 27))

        self.horizontalLayout_40.addWidget(self.btn_remove_region0_2_top)


        self.verticalLayout_31.addWidget(self.frame_31, 0, Qt.AlignTop)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_19)

        self.line_11 = QFrame(self.page_2_top)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_11)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_18)

        self.frame_52 = QFrame(self.page_2_top)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(16777215, 0))
        self.frame_52.setFrameShape(QFrame.Box)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_52)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_54 = QFrame(self.frame_52)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 0))
        self.frame_54.setMaximumSize(QSize(16777215, 300))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_11 = QLabel(self.frame_54)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_54.addWidget(self.label_11)


        self.verticalLayout_42.addWidget(self.frame_54)

        self.frame_150 = QFrame(self.frame_52)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setEnabled(True)
        self.frame_150.setMinimumSize(QSize(0, 66))
        self.frame_150.setMaximumSize(QSize(16777215, 67))
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_150)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.label_126 = QLabel(self.frame_150)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_106.addWidget(self.label_126, 0, Qt.AlignHCenter)

        self.frame_151 = QFrame(self.frame_150)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setMinimumSize(QSize(0, 43))
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_167 = QHBoxLayout(self.frame_151)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.horizontalLayout_167.setContentsMargins(0, 0, -1, 0)
        self.checkbox_thresh_inv0_2_top = QCheckBox(self.frame_151)
        self.checkbox_thresh_inv0_2_top.setObjectName(u"checkbox_thresh_inv0_2_top")
        self.checkbox_thresh_inv0_2_top.setMinimumSize(QSize(100, 0))
        self.checkbox_thresh_inv0_2_top.setMaximumSize(QSize(87, 16777215))

        self.horizontalLayout_167.addWidget(self.checkbox_thresh_inv0_2_top)

        self.bar_thresh0_2_top = QSlider(self.frame_151)
        self.bar_thresh0_2_top.setObjectName(u"bar_thresh0_2_top")
        self.bar_thresh0_2_top.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_2_top.setMaximum(255)
        self.bar_thresh0_2_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_167.addWidget(self.bar_thresh0_2_top)

        self.spinBox_12 = QSpinBox(self.frame_151)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setEnabled(True)
        self.spinBox_12.setMaximum(255)

        self.horizontalLayout_167.addWidget(self.spinBox_12)


        self.verticalLayout_106.addWidget(self.frame_151)


        self.verticalLayout_42.addWidget(self.frame_150)

        self.frame_156 = QFrame(self.frame_52)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setEnabled(True)
        self.frame_156.setMinimumSize(QSize(0, 70))
        self.frame_156.setMaximumSize(QSize(16777215, 67))
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_156)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.label_127 = QLabel(self.frame_156)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_107.addWidget(self.label_127, 0, Qt.AlignHCenter)

        self.frame_157 = QFrame(self.frame_156)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setMinimumSize(QSize(0, 43))
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_168 = QHBoxLayout(self.frame_157)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(0, 0, -1, 0)
        self.bar_noise_filter0_2_top = QSlider(self.frame_157)
        self.bar_noise_filter0_2_top.setObjectName(u"bar_noise_filter0_2_top")
        self.bar_noise_filter0_2_top.setMinimumSize(QSize(0, 30))
        self.bar_noise_filter0_2_top.setMaximum(255)
        self.bar_noise_filter0_2_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_168.addWidget(self.bar_noise_filter0_2_top)

        self.spinBox_13 = QSpinBox(self.frame_157)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setEnabled(True)
        self.spinBox_13.setMaximum(255)

        self.horizontalLayout_168.addWidget(self.spinBox_13)


        self.verticalLayout_107.addWidget(self.frame_157)


        self.verticalLayout_42.addWidget(self.frame_156)

        self.groupBox_12 = QGroupBox(self.frame_52)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(0, 0))
        self.groupBox_12.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_52 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.check_circle_2_top = QRadioButton(self.groupBox_12)
        self.check_circle_2_top.setObjectName(u"check_circle_2_top")

        self.horizontalLayout_52.addWidget(self.check_circle_2_top)

        self.check_rect_2_top = QRadioButton(self.groupBox_12)
        self.check_rect_2_top.setObjectName(u"check_rect_2_top")

        self.horizontalLayout_52.addWidget(self.check_rect_2_top)

        self.check_hexagonal_2_top = QRadioButton(self.groupBox_12)
        self.check_hexagonal_2_top.setObjectName(u"check_hexagonal_2_top")

        self.horizontalLayout_52.addWidget(self.check_hexagonal_2_top)


        self.verticalLayout_42.addWidget(self.groupBox_12)

        self.stackedWidget_3 = QStackedWidget(self.frame_52)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(0, 200))
        self.page_circle = QWidget()
        self.page_circle.setObjectName(u"page_circle")
        self.verticalLayout_41 = QVBoxLayout(self.page_circle)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_162 = QFrame(self.page_circle)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setMinimumSize(QSize(0, 44))
        self.frame_162.setFrameShape(QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_169 = QHBoxLayout(self.frame_162)
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.label_128 = QLabel(self.frame_162)
        self.label_128.setObjectName(u"label_128")

        self.horizontalLayout_169.addWidget(self.label_128)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_25)

        self.label_132 = QLabel(self.frame_162)
        self.label_132.setObjectName(u"label_132")

        self.horizontalLayout_169.addWidget(self.label_132)

        self.label_min_diameter_2_top = QLabel(self.frame_162)
        self.label_min_diameter_2_top.setObjectName(u"label_min_diameter_2_top")

        self.horizontalLayout_169.addWidget(self.label_min_diameter_2_top)

        self.label_133 = QLabel(self.frame_162)
        self.label_133.setObjectName(u"label_133")

        self.horizontalLayout_169.addWidget(self.label_133)

        self.label_max_diameter_2_top = QLabel(self.frame_162)
        self.label_max_diameter_2_top.setObjectName(u"label_max_diameter_2_top")

        self.horizontalLayout_169.addWidget(self.label_max_diameter_2_top)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_26)


        self.verticalLayout_41.addWidget(self.frame_162)

        self.frame_164 = QFrame(self.page_circle)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setFrameShape(QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_171 = QHBoxLayout(self.frame_164)
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.label_135 = QLabel(self.frame_164)
        self.label_135.setObjectName(u"label_135")

        self.horizontalLayout_171.addWidget(self.label_135)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_171.addItem(self.horizontalSpacer_29)

        self.label_140 = QLabel(self.frame_164)
        self.label_140.setObjectName(u"label_140")

        self.horizontalLayout_171.addWidget(self.label_140)

        self.spin_min_diameter_2_top = QSpinBox(self.frame_164)
        self.spin_min_diameter_2_top.setObjectName(u"spin_min_diameter_2_top")
        self.spin_min_diameter_2_top.setMaximum(20000)
        self.spin_min_diameter_2_top.setSingleStep(5)

        self.horizontalLayout_171.addWidget(self.spin_min_diameter_2_top)

        self.label_141 = QLabel(self.frame_164)
        self.label_141.setObjectName(u"label_141")

        self.horizontalLayout_171.addWidget(self.label_141)

        self.spin_max_diameter_2_top = QSpinBox(self.frame_164)
        self.spin_max_diameter_2_top.setObjectName(u"spin_max_diameter_2_top")
        self.spin_max_diameter_2_top.setMaximum(20000)
        self.spin_max_diameter_2_top.setSingleStep(5)

        self.horizontalLayout_171.addWidget(self.spin_max_diameter_2_top)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_171.addItem(self.horizontalSpacer_30)


        self.verticalLayout_41.addWidget(self.frame_164)

        self.stackedWidget_3.addWidget(self.page_circle)
        self.page_rect_mask = QWidget()
        self.page_rect_mask.setObjectName(u"page_rect_mask")
        self.verticalLayout_43 = QVBoxLayout(self.page_rect_mask)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_163 = QFrame(self.page_rect_mask)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setMinimumSize(QSize(0, 50))
        self.frame_163.setMaximumSize(QSize(16777215, 50))
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_172 = QHBoxLayout(self.frame_163)
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.label_142 = QLabel(self.frame_163)
        self.label_142.setObjectName(u"label_142")

        self.horizontalLayout_172.addWidget(self.label_142)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_172.addItem(self.horizontalSpacer_31)

        self.label_143 = QLabel(self.frame_163)
        self.label_143.setObjectName(u"label_143")

        self.horizontalLayout_172.addWidget(self.label_143)

        self.label_min_district_2_top = QLabel(self.frame_163)
        self.label_min_district_2_top.setObjectName(u"label_min_district_2_top")

        self.horizontalLayout_172.addWidget(self.label_min_district_2_top)

        self.label_144 = QLabel(self.frame_163)
        self.label_144.setObjectName(u"label_144")

        self.horizontalLayout_172.addWidget(self.label_144)

        self.label_max_district_2_top = QLabel(self.frame_163)
        self.label_max_district_2_top.setObjectName(u"label_max_district_2_top")

        self.horizontalLayout_172.addWidget(self.label_max_district_2_top)


        self.verticalLayout_43.addWidget(self.frame_163)

        self.frame_152 = QFrame(self.page_rect_mask)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setMinimumSize(QSize(0, 44))
        self.frame_152.setMaximumSize(QSize(16777215, 44))
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_152)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_153 = QFrame(self.frame_152)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setMinimumSize(QSize(0, 50))
        self.frame_153.setMaximumSize(QSize(16777215, 50))
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_175 = QHBoxLayout(self.frame_153)
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.label_129 = QLabel(self.frame_153)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(122, 0))

        self.horizontalLayout_175.addWidget(self.label_129)

        self.label_130 = QLabel(self.frame_153)
        self.label_130.setObjectName(u"label_130")

        self.horizontalLayout_175.addWidget(self.label_130)

        self.spin_min_district_2_top = QSpinBox(self.frame_153)
        self.spin_min_district_2_top.setObjectName(u"spin_min_district_2_top")
        self.spin_min_district_2_top.setMaximumSize(QSize(48, 16777215))
        self.spin_min_district_2_top.setMaximum(20000)
        self.spin_min_district_2_top.setSingleStep(5)

        self.horizontalLayout_175.addWidget(self.spin_min_district_2_top)

        self.label_131 = QLabel(self.frame_153)
        self.label_131.setObjectName(u"label_131")

        self.horizontalLayout_175.addWidget(self.label_131)

        self.spin_max_district_2_top = QSpinBox(self.frame_153)
        self.spin_max_district_2_top.setObjectName(u"spin_max_district_2_top")
        self.spin_max_district_2_top.setMaximumSize(QSize(44, 16777215))
        self.spin_max_district_2_top.setMaximum(20000)
        self.spin_max_district_2_top.setSingleStep(5)

        self.horizontalLayout_175.addWidget(self.spin_max_district_2_top)


        self.verticalLayout_25.addWidget(self.frame_153)


        self.verticalLayout_43.addWidget(self.frame_152)

        self.frame_165 = QFrame(self.page_rect_mask)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setMinimumSize(QSize(0, 50))
        self.frame_165.setMaximumSize(QSize(16777215, 50))
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_173 = QHBoxLayout(self.frame_165)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.label_145 = QLabel(self.frame_165)
        self.label_145.setObjectName(u"label_145")

        self.horizontalLayout_173.addWidget(self.label_145)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_173.addItem(self.horizontalSpacer_33)

        self.label_146 = QLabel(self.frame_165)
        self.label_146.setObjectName(u"label_146")

        self.horizontalLayout_173.addWidget(self.label_146)

        self.label_min_corner_2_top = QLabel(self.frame_165)
        self.label_min_corner_2_top.setObjectName(u"label_min_corner_2_top")

        self.horizontalLayout_173.addWidget(self.label_min_corner_2_top)

        self.label_147 = QLabel(self.frame_165)
        self.label_147.setObjectName(u"label_147")

        self.horizontalLayout_173.addWidget(self.label_147)

        self.label_max_corner_2_top = QLabel(self.frame_165)
        self.label_max_corner_2_top.setObjectName(u"label_max_corner_2_top")

        self.horizontalLayout_173.addWidget(self.label_max_corner_2_top)


        self.verticalLayout_43.addWidget(self.frame_165)

        self.frame_154 = QFrame(self.page_rect_mask)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setMinimumSize(QSize(0, 50))
        self.frame_154.setMaximumSize(QSize(16777215, 50))
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_178 = QHBoxLayout(self.frame_154)
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.label_134 = QLabel(self.frame_154)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(122, 0))

        self.horizontalLayout_178.addWidget(self.label_134)

        self.label_161 = QLabel(self.frame_154)
        self.label_161.setObjectName(u"label_161")

        self.horizontalLayout_178.addWidget(self.label_161)

        self.spin_min_corner_2_top = QSpinBox(self.frame_154)
        self.spin_min_corner_2_top.setObjectName(u"spin_min_corner_2_top")
        self.spin_min_corner_2_top.setMaximumSize(QSize(48, 16777215))
        self.spin_min_corner_2_top.setMaximum(20000)
        self.spin_min_corner_2_top.setSingleStep(5)

        self.horizontalLayout_178.addWidget(self.spin_min_corner_2_top)

        self.label_162 = QLabel(self.frame_154)
        self.label_162.setObjectName(u"label_162")

        self.horizontalLayout_178.addWidget(self.label_162)

        self.spin_max_corner_2_top = QSpinBox(self.frame_154)
        self.spin_max_corner_2_top.setObjectName(u"spin_max_corner_2_top")
        self.spin_max_corner_2_top.setMaximumSize(QSize(44, 16777215))
        self.spin_max_corner_2_top.setMaximum(20000)
        self.spin_max_corner_2_top.setSingleStep(5)

        self.horizontalLayout_178.addWidget(self.spin_max_corner_2_top)


        self.verticalLayout_43.addWidget(self.frame_154)

        self.stackedWidget_3.addWidget(self.page_rect_mask)

        self.verticalLayout_42.addWidget(self.stackedWidget_3)

        self.btn_draw_complete0_2_top = QPushButton(self.frame_52)
        self.btn_draw_complete0_2_top.setObjectName(u"btn_draw_complete0_2_top")
        self.btn_draw_complete0_2_top.setEnabled(False)
        self.btn_draw_complete0_2_top.setMinimumSize(QSize(79, 22))
        self.btn_draw_complete0_2_top.setStyleSheet(u"QPushButton:enabled { \n"
"	background-color: rgb(255,255,255);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(50,50,50);\n"
"	color: white;\n"
"}")

        self.verticalLayout_42.addWidget(self.btn_draw_complete0_2_top, 0, Qt.AlignHCenter)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_16)


        self.verticalLayout_31.addWidget(self.frame_52)

        self.stackedWidget_2.addWidget(self.page_2_top)
        self.page_3_top = QWidget()
        self.page_3_top.setObjectName(u"page_3_top")
        self.verticalLayout_111 = QVBoxLayout(self.page_3_top)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.frame_166 = QFrame(self.page_3_top)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setMaximumSize(QSize(16777215, 46))
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_166)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_136 = QLabel(self.frame_166)
        self.label_136.setObjectName(u"label_136")

        self.horizontalLayout_80.addWidget(self.label_136)

        self.line_name_region0_3_top = QLineEdit(self.frame_166)
        self.line_name_region0_3_top.setObjectName(u"line_name_region0_3_top")

        self.horizontalLayout_80.addWidget(self.line_name_region0_3_top)


        self.verticalLayout_111.addWidget(self.frame_166)

        self.frame_55 = QFrame(self.page_3_top)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMaximumSize(QSize(16777215, 61))
        self.frame_55.setFrameShape(QFrame.Box)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.btn_add_region0_3_top = QPushButton(self.frame_55)
        self.btn_add_region0_3_top.setObjectName(u"btn_add_region0_3_top")
        self.btn_add_region0_3_top.setMaximumSize(QSize(26, 16777215))
        self.btn_add_region0_3_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_region0_3_top.setStyleSheet(u"border:none;\n"
"")
        self.btn_add_region0_3_top.setIcon(icon16)
        self.btn_add_region0_3_top.setIconSize(QSize(26, 26))

        self.horizontalLayout_56.addWidget(self.btn_add_region0_3_top)

        self.combo_regions_name0_3_top = QComboBox(self.frame_55)
        self.combo_regions_name0_3_top.setObjectName(u"combo_regions_name0_3_top")
        self.combo_regions_name0_3_top.setMinimumSize(QSize(191, 0))
        self.combo_regions_name0_3_top.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_56.addWidget(self.combo_regions_name0_3_top)

        self.btn_remove_region0_3_top = QPushButton(self.frame_55)
        self.btn_remove_region0_3_top.setObjectName(u"btn_remove_region0_3_top")
        self.btn_remove_region0_3_top.setMaximumSize(QSize(26, 16777215))
        self.btn_remove_region0_3_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove_region0_3_top.setStyleSheet(u"border:none;")
        self.btn_remove_region0_3_top.setIcon(icon17)
        self.btn_remove_region0_3_top.setIconSize(QSize(26, 27))

        self.horizontalLayout_56.addWidget(self.btn_remove_region0_3_top)


        self.verticalLayout_111.addWidget(self.frame_55)

        self.line_12 = QFrame(self.page_3_top)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_111.addWidget(self.line_12)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_111.addItem(self.verticalSpacer_15)

        self.frame_193 = QFrame(self.page_3_top)
        self.frame_193.setObjectName(u"frame_193")
        self.frame_193.setMinimumSize(QSize(0, 540))
        self.frame_193.setMaximumSize(QSize(16777215, 604))
        self.frame_193.setFrameShape(QFrame.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Raised)
        self.verticalLayout_130 = QVBoxLayout(self.frame_193)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.groupBox_8 = QGroupBox(self.frame_193)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(0, 80))
        self.groupBox_8.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_119 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.frame_56 = QFrame(self.groupBox_8)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(0, 40))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_139 = QLabel(self.frame_56)
        self.label_139.setObjectName(u"label_139")

        self.horizontalLayout_81.addWidget(self.label_139)

        self.spin_roi_x1_3_top = QSpinBox(self.frame_56)
        self.spin_roi_x1_3_top.setObjectName(u"spin_roi_x1_3_top")

        self.horizontalLayout_81.addWidget(self.spin_roi_x1_3_top)

        self.label_148 = QLabel(self.frame_56)
        self.label_148.setObjectName(u"label_148")

        self.horizontalLayout_81.addWidget(self.label_148)

        self.spin_roi_y1_3_top = QSpinBox(self.frame_56)
        self.spin_roi_y1_3_top.setObjectName(u"spin_roi_y1_3_top")

        self.horizontalLayout_81.addWidget(self.spin_roi_y1_3_top)

        self.label_149 = QLabel(self.frame_56)
        self.label_149.setObjectName(u"label_149")

        self.horizontalLayout_81.addWidget(self.label_149)

        self.spin_roi_r1_3_top = QSpinBox(self.frame_56)
        self.spin_roi_r1_3_top.setObjectName(u"spin_roi_r1_3_top")

        self.horizontalLayout_81.addWidget(self.spin_roi_r1_3_top)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_12)


        self.verticalLayout_119.addWidget(self.frame_56)


        self.verticalLayout_130.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.frame_193)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(0, 80))
        self.groupBox_9.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_120 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.frame_171 = QFrame(self.groupBox_9)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_171)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_151 = QLabel(self.frame_171)
        self.label_151.setObjectName(u"label_151")

        self.horizontalLayout_82.addWidget(self.label_151)

        self.spin_roi_x2_3_top = QSpinBox(self.frame_171)
        self.spin_roi_x2_3_top.setObjectName(u"spin_roi_x2_3_top")

        self.horizontalLayout_82.addWidget(self.spin_roi_x2_3_top)

        self.label_152 = QLabel(self.frame_171)
        self.label_152.setObjectName(u"label_152")

        self.horizontalLayout_82.addWidget(self.label_152)

        self.spin_roi_y2_3_top = QSpinBox(self.frame_171)
        self.spin_roi_y2_3_top.setObjectName(u"spin_roi_y2_3_top")

        self.horizontalLayout_82.addWidget(self.spin_roi_y2_3_top)

        self.label_153 = QLabel(self.frame_171)
        self.label_153.setObjectName(u"label_153")

        self.horizontalLayout_82.addWidget(self.label_153)

        self.spin_roi_r2_3_top = QSpinBox(self.frame_171)
        self.spin_roi_r2_3_top.setObjectName(u"spin_roi_r2_3_top")

        self.horizontalLayout_82.addWidget(self.spin_roi_r2_3_top)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_27)


        self.verticalLayout_120.addWidget(self.frame_171)


        self.verticalLayout_130.addWidget(self.groupBox_9)

        self.frame_169 = QFrame(self.frame_193)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setEnabled(True)
        self.frame_169.setMinimumSize(QSize(0, 66))
        self.frame_169.setMaximumSize(QSize(16777215, 67))
        self.frame_169.setFrameShape(QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_169)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.label_138 = QLabel(self.frame_169)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_109.addWidget(self.label_138, 0, Qt.AlignHCenter)

        self.frame_170 = QFrame(self.frame_169)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setMinimumSize(QSize(0, 43))
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_174 = QHBoxLayout(self.frame_170)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalLayout_174.setContentsMargins(0, 0, -1, 0)
        self.checkbox_thresh_inv0_3_top = QCheckBox(self.frame_170)
        self.checkbox_thresh_inv0_3_top.setObjectName(u"checkbox_thresh_inv0_3_top")
        self.checkbox_thresh_inv0_3_top.setMinimumSize(QSize(96, 4))
        self.checkbox_thresh_inv0_3_top.setMaximumSize(QSize(87, 16777215))

        self.horizontalLayout_174.addWidget(self.checkbox_thresh_inv0_3_top)

        self.bar_thresh0_3_top = QSlider(self.frame_170)
        self.bar_thresh0_3_top.setObjectName(u"bar_thresh0_3_top")
        self.bar_thresh0_3_top.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_3_top.setMaximum(255)
        self.bar_thresh0_3_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_174.addWidget(self.bar_thresh0_3_top)

        self.spinBox_5 = QSpinBox(self.frame_170)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setEnabled(True)
        self.spinBox_5.setMaximum(255)

        self.horizontalLayout_174.addWidget(self.spinBox_5)


        self.verticalLayout_109.addWidget(self.frame_170)


        self.verticalLayout_130.addWidget(self.frame_169)

        self.frame_167 = QFrame(self.frame_193)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setEnabled(True)
        self.frame_167.setMaximumSize(QSize(16777215, 65))
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_167)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.label_137 = QLabel(self.frame_167)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setEnabled(True)
        self.label_137.setAlignment(Qt.AlignCenter)

        self.verticalLayout_108.addWidget(self.label_137)

        self.frame_168 = QFrame(self.frame_167)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setMinimumSize(QSize(0, 29))
        self.frame_168.setFrameShape(QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_170 = QHBoxLayout(self.frame_168)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.bar_noise_filter0_3_top = QSlider(self.frame_168)
        self.bar_noise_filter0_3_top.setObjectName(u"bar_noise_filter0_3_top")
        self.bar_noise_filter0_3_top.setMinimumSize(QSize(0, 30))
        self.bar_noise_filter0_3_top.setMaximum(100)
        self.bar_noise_filter0_3_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_170.addWidget(self.bar_noise_filter0_3_top)

        self.spinBox_14 = QSpinBox(self.frame_168)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setMaximum(100)

        self.horizontalLayout_170.addWidget(self.spinBox_14)


        self.verticalLayout_108.addWidget(self.frame_168)


        self.verticalLayout_130.addWidget(self.frame_167)

        self.frame_192 = QFrame(self.frame_193)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setMaximumSize(QSize(16777215, 50))
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_181 = QHBoxLayout(self.frame_192)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.label_115 = QLabel(self.frame_192)
        self.label_115.setObjectName(u"label_115")

        self.horizontalLayout_181.addWidget(self.label_115)

        self.spin_min_area_3_top = QSpinBox(self.frame_192)
        self.spin_min_area_3_top.setObjectName(u"spin_min_area_3_top")
        self.spin_min_area_3_top.setMinimumSize(QSize(100, 0))
        self.spin_min_area_3_top.setMaximumSize(QSize(200, 16777215))
        self.spin_min_area_3_top.setMaximum(999999)
        self.spin_min_area_3_top.setSingleStep(10)

        self.horizontalLayout_181.addWidget(self.spin_min_area_3_top)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_181.addItem(self.horizontalSpacer_28)


        self.verticalLayout_130.addWidget(self.frame_192)

        self.groupBox_18 = QGroupBox(self.frame_193)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setMaximumSize(QSize(16777215, 82))
        self.horizontalLayout_105 = QHBoxLayout(self.groupBox_18)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.frame_17 = QFrame(self.groupBox_18)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.label_187 = QLabel(self.frame_17)
        self.label_187.setObjectName(u"label_187")

        self.horizontalLayout_90.addWidget(self.label_187)

        self.label_min_area_3_top = QLabel(self.frame_17)
        self.label_min_area_3_top.setObjectName(u"label_min_area_3_top")

        self.horizontalLayout_90.addWidget(self.label_min_area_3_top)

        self.line_36 = QFrame(self.frame_17)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.VLine)
        self.line_36.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_90.addWidget(self.line_36)

        self.label_195 = QLabel(self.frame_17)
        self.label_195.setObjectName(u"label_195")

        self.horizontalLayout_90.addWidget(self.label_195)

        self.label_max_area_3_top = QLabel(self.frame_17)
        self.label_max_area_3_top.setObjectName(u"label_max_area_3_top")

        self.horizontalLayout_90.addWidget(self.label_max_area_3_top)


        self.horizontalLayout_105.addWidget(self.frame_17)


        self.verticalLayout_130.addWidget(self.groupBox_18)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_130.addItem(self.verticalSpacer_25)


        self.verticalLayout_111.addWidget(self.frame_193)

        self.stackedWidget_2.addWidget(self.page_3_top)
        self.page_4_top = QWidget()
        self.page_4_top.setObjectName(u"page_4_top")
        self.verticalLayout_129 = QVBoxLayout(self.page_4_top)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.frame_194 = QFrame(self.page_4_top)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.frame_194)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.frame_195 = QFrame(self.frame_194)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setEnabled(True)
        self.frame_195.setMinimumSize(QSize(0, 66))
        self.frame_195.setMaximumSize(QSize(16777215, 67))
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.frame_195)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.label_170 = QLabel(self.frame_195)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_127.addWidget(self.label_170, 0, Qt.AlignHCenter)

        self.frame_197 = QFrame(self.frame_195)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setMinimumSize(QSize(0, 43))
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_186 = QHBoxLayout(self.frame_197)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_186.setContentsMargins(0, 0, -1, 0)
        self.checkbox_thresh_inv0_4_top = QCheckBox(self.frame_197)
        self.checkbox_thresh_inv0_4_top.setObjectName(u"checkbox_thresh_inv0_4_top")
        self.checkbox_thresh_inv0_4_top.setMinimumSize(QSize(96, 4))
        self.checkbox_thresh_inv0_4_top.setMaximumSize(QSize(87, 16777215))

        self.horizontalLayout_186.addWidget(self.checkbox_thresh_inv0_4_top)

        self.bar_thresh0_4_top = QSlider(self.frame_197)
        self.bar_thresh0_4_top.setObjectName(u"bar_thresh0_4_top")
        self.bar_thresh0_4_top.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_4_top.setMaximum(255)
        self.bar_thresh0_4_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_186.addWidget(self.bar_thresh0_4_top)

        self.spinBox_17 = QSpinBox(self.frame_197)
        self.spinBox_17.setObjectName(u"spinBox_17")
        self.spinBox_17.setEnabled(True)
        self.spinBox_17.setMaximum(255)

        self.horizontalLayout_186.addWidget(self.spinBox_17)


        self.verticalLayout_127.addWidget(self.frame_197)


        self.verticalLayout_121.addWidget(self.frame_195)

        self.frame_207 = QFrame(self.frame_194)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setEnabled(True)
        self.frame_207.setMaximumSize(QSize(16777215, 72))
        self.frame_207.setFrameShape(QFrame.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.frame_207)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.label_171 = QLabel(self.frame_207)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setEnabled(True)
        self.label_171.setAlignment(Qt.AlignCenter)

        self.verticalLayout_128.addWidget(self.label_171)

        self.frame_208 = QFrame(self.frame_207)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setMinimumSize(QSize(0, 29))
        self.frame_208.setFrameShape(QFrame.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_187 = QHBoxLayout(self.frame_208)
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.horizontalLayout_187.setContentsMargins(0, 0, 0, 0)
        self.bar_noise_filter0_4_top = QSlider(self.frame_208)
        self.bar_noise_filter0_4_top.setObjectName(u"bar_noise_filter0_4_top")
        self.bar_noise_filter0_4_top.setMinimumSize(QSize(0, 30))
        self.bar_noise_filter0_4_top.setMaximum(100)
        self.bar_noise_filter0_4_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_187.addWidget(self.bar_noise_filter0_4_top)

        self.spinBox_18 = QSpinBox(self.frame_208)
        self.spinBox_18.setObjectName(u"spinBox_18")
        self.spinBox_18.setMaximum(100)

        self.horizontalLayout_187.addWidget(self.spinBox_18)


        self.verticalLayout_128.addWidget(self.frame_208)


        self.verticalLayout_121.addWidget(self.frame_207)


        self.verticalLayout_129.addWidget(self.frame_194)

        self.groupBox_15 = QGroupBox(self.page_4_top)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setEnabled(False)
        self.groupBox_15.setMinimumSize(QSize(0, 0))
        self.groupBox_15.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_77 = QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.check_circle_4_top = QRadioButton(self.groupBox_15)
        self.check_circle_4_top.setObjectName(u"check_circle_4_top")

        self.horizontalLayout_77.addWidget(self.check_circle_4_top)

        self.check_rect_4_top = QRadioButton(self.groupBox_15)
        self.check_rect_4_top.setObjectName(u"check_rect_4_top")

        self.horizontalLayout_77.addWidget(self.check_rect_4_top)

        self.check_hexagonal_4_top = QRadioButton(self.groupBox_15)
        self.check_hexagonal_4_top.setObjectName(u"check_hexagonal_4_top")

        self.horizontalLayout_77.addWidget(self.check_hexagonal_4_top)


        self.verticalLayout_129.addWidget(self.groupBox_15)

        self.label_117 = QLabel(self.page_4_top)
        self.label_117.setObjectName(u"label_117")

        self.verticalLayout_129.addWidget(self.label_117)

        self.spin_min_area_4_top = QSpinBox(self.page_4_top)
        self.spin_min_area_4_top.setObjectName(u"spin_min_area_4_top")
        self.spin_min_area_4_top.setMaximum(5000)
        self.spin_min_area_4_top.setSingleStep(10)

        self.verticalLayout_129.addWidget(self.spin_min_area_4_top)

        self.label_120 = QLabel(self.page_4_top)
        self.label_120.setObjectName(u"label_120")

        self.verticalLayout_129.addWidget(self.label_120)

        self.frame_16 = QFrame(self.page_4_top)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.label_121 = QLabel(self.frame_16)
        self.label_121.setObjectName(u"label_121")

        self.horizontalLayout_97.addWidget(self.label_121)

        self.label_min_area_4_top = QLabel(self.frame_16)
        self.label_min_area_4_top.setObjectName(u"label_min_area_4_top")

        self.horizontalLayout_97.addWidget(self.label_min_area_4_top)

        self.line_33 = QFrame(self.frame_16)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.VLine)
        self.line_33.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_97.addWidget(self.line_33)

        self.label_125 = QLabel(self.frame_16)
        self.label_125.setObjectName(u"label_125")

        self.horizontalLayout_97.addWidget(self.label_125)

        self.label_max_area_4_top = QLabel(self.frame_16)
        self.label_max_area_4_top.setObjectName(u"label_max_area_4_top")

        self.horizontalLayout_97.addWidget(self.label_max_area_4_top)


        self.verticalLayout_129.addWidget(self.frame_16)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_129.addItem(self.verticalSpacer_5)

        self.stackedWidget_2.addWidget(self.page_4_top)
        self.page_5_top = QWidget()
        self.page_5_top.setObjectName(u"page_5_top")
        self.verticalLayout_132 = QVBoxLayout(self.page_5_top)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.frame_172 = QFrame(self.page_5_top)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_172)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.combo_regions_name0_5_top = QComboBox(self.frame_172)
        self.combo_regions_name0_5_top.setObjectName(u"combo_regions_name0_5_top")

        self.verticalLayout_135.addWidget(self.combo_regions_name0_5_top)

        self.frame_214 = QFrame(self.frame_172)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setEnabled(True)
        self.frame_214.setMinimumSize(QSize(0, 66))
        self.frame_214.setMaximumSize(QSize(16777215, 67))
        self.frame_214.setFrameShape(QFrame.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.frame_214)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_182 = QLabel(self.frame_214)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_133.addWidget(self.label_182, 0, Qt.AlignHCenter)

        self.frame_215 = QFrame(self.frame_214)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setMinimumSize(QSize(0, 43))
        self.frame_215.setFrameShape(QFrame.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_190 = QHBoxLayout(self.frame_215)
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_190.setContentsMargins(0, 0, -1, 0)
        self.checkbox_thresh_inv0_5_top = QCheckBox(self.frame_215)
        self.checkbox_thresh_inv0_5_top.setObjectName(u"checkbox_thresh_inv0_5_top")
        self.checkbox_thresh_inv0_5_top.setMaximumSize(QSize(87, 16777215))

        self.horizontalLayout_190.addWidget(self.checkbox_thresh_inv0_5_top)

        self.bar_thresh0_5_top = QSlider(self.frame_215)
        self.bar_thresh0_5_top.setObjectName(u"bar_thresh0_5_top")
        self.bar_thresh0_5_top.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_5_top.setMaximum(255)
        self.bar_thresh0_5_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_190.addWidget(self.bar_thresh0_5_top)

        self.spinBox_21 = QSpinBox(self.frame_215)
        self.spinBox_21.setObjectName(u"spinBox_21")
        self.spinBox_21.setEnabled(True)
        self.spinBox_21.setMaximum(255)

        self.horizontalLayout_190.addWidget(self.spinBox_21)


        self.verticalLayout_133.addWidget(self.frame_215)


        self.verticalLayout_135.addWidget(self.frame_214)

        self.frame_216 = QFrame(self.frame_172)
        self.frame_216.setObjectName(u"frame_216")
        self.frame_216.setEnabled(True)
        self.frame_216.setMaximumSize(QSize(16777215, 72))
        self.frame_216.setFrameShape(QFrame.StyledPanel)
        self.frame_216.setFrameShadow(QFrame.Raised)
        self.verticalLayout_134 = QVBoxLayout(self.frame_216)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.label_184 = QLabel(self.frame_216)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setEnabled(True)
        self.label_184.setAlignment(Qt.AlignCenter)

        self.verticalLayout_134.addWidget(self.label_184)

        self.frame_217 = QFrame(self.frame_216)
        self.frame_217.setObjectName(u"frame_217")
        self.frame_217.setMinimumSize(QSize(0, 29))
        self.frame_217.setFrameShape(QFrame.StyledPanel)
        self.frame_217.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_191 = QHBoxLayout(self.frame_217)
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.horizontalLayout_191.setContentsMargins(0, 0, 0, 0)
        self.bar_noise_filter0_5_top = QSlider(self.frame_217)
        self.bar_noise_filter0_5_top.setObjectName(u"bar_noise_filter0_5_top")
        self.bar_noise_filter0_5_top.setMinimumSize(QSize(0, 30))
        self.bar_noise_filter0_5_top.setMaximum(100)
        self.bar_noise_filter0_5_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_191.addWidget(self.bar_noise_filter0_5_top)

        self.spinBox_22 = QSpinBox(self.frame_217)
        self.spinBox_22.setObjectName(u"spinBox_22")
        self.spinBox_22.setMaximum(100)

        self.horizontalLayout_191.addWidget(self.spinBox_22)


        self.verticalLayout_134.addWidget(self.frame_217)


        self.verticalLayout_135.addWidget(self.frame_216)

        self.frame_213 = QFrame(self.frame_172)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setMaximumSize(QSize(16777215, 40))
        self.frame_213.setFrameShape(QFrame.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_193 = QHBoxLayout(self.frame_213)
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.label_185 = QLabel(self.frame_213)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_193.addWidget(self.label_185)

        self.label_distance_centers_5_top = QLabel(self.frame_213)
        self.label_distance_centers_5_top.setObjectName(u"label_distance_centers_5_top")

        self.horizontalLayout_193.addWidget(self.label_distance_centers_5_top)


        self.verticalLayout_135.addWidget(self.frame_213)

        self.frame_218 = QFrame(self.frame_172)
        self.frame_218.setObjectName(u"frame_218")
        self.frame_218.setMaximumSize(QSize(16777215, 50))
        self.frame_218.setFrameShape(QFrame.StyledPanel)
        self.frame_218.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_192 = QHBoxLayout(self.frame_218)
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.label_193 = QLabel(self.frame_218)
        self.label_193.setObjectName(u"label_193")

        self.horizontalLayout_192.addWidget(self.label_193)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_192.addItem(self.horizontalSpacer_32)

        self.label_194 = QLabel(self.frame_218)
        self.label_194.setObjectName(u"label_194")

        self.horizontalLayout_192.addWidget(self.label_194)

        self.spin_min_distance_5_top = QSpinBox(self.frame_218)
        self.spin_min_distance_5_top.setObjectName(u"spin_min_distance_5_top")
        self.spin_min_distance_5_top.setMaximum(20000)
        self.spin_min_distance_5_top.setSingleStep(5)

        self.horizontalLayout_192.addWidget(self.spin_min_distance_5_top)

        self.label_196 = QLabel(self.frame_218)
        self.label_196.setObjectName(u"label_196")

        self.horizontalLayout_192.addWidget(self.label_196)

        self.spin_max_distance_5_top = QSpinBox(self.frame_218)
        self.spin_max_distance_5_top.setObjectName(u"spin_max_distance_5_top")
        self.spin_max_distance_5_top.setMaximum(20000)
        self.spin_max_distance_5_top.setSingleStep(5)

        self.horizontalLayout_192.addWidget(self.spin_max_distance_5_top)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_192.addItem(self.horizontalSpacer_34)


        self.verticalLayout_135.addWidget(self.frame_218)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_135.addItem(self.verticalSpacer_20)


        self.verticalLayout_132.addWidget(self.frame_172)

        self.stackedWidget_2.addWidget(self.page_5_top)
        self.page_1_side = QWidget()
        self.page_1_side.setObjectName(u"page_1_side")
        self.verticalLayout_53 = QVBoxLayout(self.page_1_side)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_58 = QFrame(self.page_1_side)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setEnabled(True)
        self.frame_58.setMinimumSize(QSize(300, 0))
        self.frame_58.setMaximumSize(QSize(372, 16777215))
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_58)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_58)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_35.addWidget(self.label_13)

        self.frame_68 = QFrame(self.frame_58)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_68)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.groupBox_20 = QGroupBox(self.frame_68)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.horizontalLayout_91 = QHBoxLayout(self.groupBox_20)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.line_img_path0_1_side = QLineEdit(self.groupBox_20)
        self.line_img_path0_1_side.setObjectName(u"line_img_path0_1_side")
        self.line_img_path0_1_side.setMinimumSize(QSize(210, 0))
        self.line_img_path0_1_side.setMaximumSize(QSize(405, 16777215))

        self.horizontalLayout_92.addWidget(self.line_img_path0_1_side)

        self.btn_load_image0_1_side = QToolButton(self.groupBox_20)
        self.btn_load_image0_1_side.setObjectName(u"btn_load_image0_1_side")

        self.horizontalLayout_92.addWidget(self.btn_load_image0_1_side)


        self.horizontalLayout_91.addLayout(self.horizontalLayout_92)

        self.btn_set_img0_1_side = QPushButton(self.groupBox_20)
        self.btn_set_img0_1_side.setObjectName(u"btn_set_img0_1_side")
        self.btn_set_img0_1_side.setMinimumSize(QSize(82, 27))
        self.btn_set_img0_1_side.setMaximumSize(QSize(16777215, 27))
        self.btn_set_img0_1_side.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_91.addWidget(self.btn_set_img0_1_side)


        self.verticalLayout_57.addWidget(self.groupBox_20)


        self.verticalLayout_35.addWidget(self.frame_68)

        self.frame_27 = QFrame(self.frame_58)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.label_26 = QLabel(self.frame_27)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_94.addWidget(self.label_26)

        self.btn_connect_camera0_1_side = QPushButton(self.frame_27)
        self.btn_connect_camera0_1_side.setObjectName(u"btn_connect_camera0_1_side")
        self.btn_connect_camera0_1_side.setMinimumSize(QSize(129, 27))
        self.btn_connect_camera0_1_side.setMaximumSize(QSize(16777215, 27))
        self.btn_connect_camera0_1_side.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_94.addWidget(self.btn_connect_camera0_1_side)


        self.verticalLayout_35.addWidget(self.frame_27)

        self.line_16 = QFrame(self.frame_58)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_35.addWidget(self.line_16)

        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setEnabled(True)
        self.frame_59.setMinimumSize(QSize(0, 130))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_59)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_60 = QFrame(self.frame_59)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setEnabled(True)
        self.frame_60.setMinimumSize(QSize(0, 118))
        self.frame_60.setMaximumSize(QSize(16777215, 118))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.groupBox_17 = QGroupBox(self.frame_60)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setEnabled(True)
        self.groupBox_17.setMinimumSize(QSize(0, 103))
        self.groupBox_17.setMaximumSize(QSize(16777215, 103))
        self.horizontalLayout_61 = QHBoxLayout(self.groupBox_17)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, -1, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_10)

        self.frame_72 = QFrame(self.groupBox_17)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.frame_71 = QFrame(self.frame_72)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_71)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_15 = QLabel(self.frame_71)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_62.addWidget(self.label_15)

        self.spin_roi_x1_1_side = QSpinBox(self.frame_71)
        self.spin_roi_x1_1_side.setObjectName(u"spin_roi_x1_1_side")
        self.spin_roi_x1_1_side.setMaximum(20000)
        self.spin_roi_x1_1_side.setSingleStep(5)

        self.horizontalLayout_62.addWidget(self.spin_roi_x1_1_side)


        self.verticalLayout_56.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.label_16 = QLabel(self.frame_71)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_99.addWidget(self.label_16)

        self.spin_roi_y1_1_side = QSpinBox(self.frame_71)
        self.spin_roi_y1_1_side.setObjectName(u"spin_roi_y1_1_side")
        self.spin_roi_y1_1_side.setMaximum(20000)
        self.spin_roi_y1_1_side.setSingleStep(5)

        self.horizontalLayout_99.addWidget(self.spin_roi_y1_1_side)


        self.verticalLayout_56.addLayout(self.horizontalLayout_99)


        self.horizontalLayout_108.addWidget(self.frame_71)

        self.frame_69 = QFrame(self.frame_72)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_69)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_18 = QLabel(self.frame_69)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_60.addWidget(self.label_18)

        self.spin_roi_x2_1_side = QSpinBox(self.frame_69)
        self.spin_roi_x2_1_side.setObjectName(u"spin_roi_x2_1_side")
        self.spin_roi_x2_1_side.setMaximum(20000)
        self.spin_roi_x2_1_side.setSingleStep(5)

        self.horizontalLayout_60.addWidget(self.spin_roi_x2_1_side)


        self.verticalLayout_51.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_14 = QLabel(self.frame_69)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_59.addWidget(self.label_14)

        self.spin_roi_y2_1_side = QSpinBox(self.frame_69)
        self.spin_roi_y2_1_side.setObjectName(u"spin_roi_y2_1_side")
        self.spin_roi_y2_1_side.setMaximum(20000)
        self.spin_roi_y2_1_side.setSingleStep(5)

        self.horizontalLayout_59.addWidget(self.spin_roi_y2_1_side)


        self.verticalLayout_51.addLayout(self.horizontalLayout_59)


        self.horizontalLayout_108.addWidget(self.frame_69)


        self.horizontalLayout_61.addWidget(self.frame_72)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_58.addWidget(self.groupBox_17)


        self.verticalLayout_50.addWidget(self.frame_60)


        self.verticalLayout_35.addWidget(self.frame_59)

        self.frame_61 = QFrame(self.frame_58)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setEnabled(True)
        self.frame_61.setMinimumSize(QSize(0, 66))
        self.frame_61.setMaximumSize(QSize(16777215, 67))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_61)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_61)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_54.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.frame_73 = QFrame(self.frame_61)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(0, 43))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(0, 0, -1, 0)
        self.checkbox_thresh_inv0_1_side = QCheckBox(self.frame_73)
        self.checkbox_thresh_inv0_1_side.setObjectName(u"checkbox_thresh_inv0_1_side")
        self.checkbox_thresh_inv0_1_side.setMaximumSize(QSize(87, 16777215))

        self.horizontalLayout_110.addWidget(self.checkbox_thresh_inv0_1_side)

        self.bar_thresh0_1_side = QSlider(self.frame_73)
        self.bar_thresh0_1_side.setObjectName(u"bar_thresh0_1_side")
        self.bar_thresh0_1_side.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_1_side.setMaximum(255)
        self.bar_thresh0_1_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_110.addWidget(self.bar_thresh0_1_side)

        self.spinBox_4 = QSpinBox(self.frame_73)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setEnabled(True)
        self.spinBox_4.setMaximum(255)

        self.horizontalLayout_110.addWidget(self.spinBox_4)


        self.verticalLayout_54.addWidget(self.frame_73)


        self.verticalLayout_35.addWidget(self.frame_61)

        self.frame_63 = QFrame(self.frame_58)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setEnabled(True)
        self.frame_63.setMaximumSize(QSize(16777215, 72))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_63)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_22 = QLabel(self.frame_63)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setEnabled(True)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_55.addWidget(self.label_22)

        self.frame_74 = QFrame(self.frame_63)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(0, 29))
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.bar_noise_filter0_1_side = QSlider(self.frame_74)
        self.bar_noise_filter0_1_side.setObjectName(u"bar_noise_filter0_1_side")
        self.bar_noise_filter0_1_side.setMinimumSize(QSize(0, 30))
        self.bar_noise_filter0_1_side.setMaximum(100)
        self.bar_noise_filter0_1_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_111.addWidget(self.bar_noise_filter0_1_side)

        self.spinBox_6 = QSpinBox(self.frame_74)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(100)

        self.horizontalLayout_111.addWidget(self.spinBox_6)


        self.verticalLayout_55.addWidget(self.frame_74)


        self.verticalLayout_35.addWidget(self.frame_63)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_8)

        self.frame_61.raise_()
        self.frame_68.raise_()
        self.frame_27.raise_()
        self.line_16.raise_()
        self.frame_59.raise_()
        self.frame_63.raise_()
        self.label_13.raise_()

        self.verticalLayout_53.addWidget(self.frame_58)

        self.stackedWidget_2.addWidget(self.page_1_side)
        self.page_2_side = QWidget()
        self.page_2_side.setObjectName(u"page_2_side")
        self.verticalLayout_66 = QVBoxLayout(self.page_2_side)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_46 = QLabel(self.page_2_side)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_66.addWidget(self.label_46)

        self.groupBox_24 = QGroupBox(self.page_2_side)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setMinimumSize(QSize(0, 103))
        self.groupBox_24.setMaximumSize(QSize(16777215, 103))
        self.horizontalLayout_119 = QHBoxLayout(self.groupBox_24)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, -1, 0)
        self.frame_81 = QFrame(self.groupBox_24)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.frame_82 = QFrame(self.frame_81)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_82)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.label_40 = QLabel(self.frame_82)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_121.addWidget(self.label_40)

        self.spin_roi_x1_2_side = QSpinBox(self.frame_82)
        self.spin_roi_x1_2_side.setObjectName(u"spin_roi_x1_2_side")
        self.spin_roi_x1_2_side.setMaximum(20000)
        self.spin_roi_x1_2_side.setSingleStep(5)

        self.horizontalLayout_121.addWidget(self.spin_roi_x1_2_side)


        self.verticalLayout_64.addLayout(self.horizontalLayout_121)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.label_41 = QLabel(self.frame_82)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_122.addWidget(self.label_41)

        self.spin_roi_y1_2_side = QSpinBox(self.frame_82)
        self.spin_roi_y1_2_side.setObjectName(u"spin_roi_y1_2_side")
        self.spin_roi_y1_2_side.setMaximum(20000)
        self.spin_roi_y1_2_side.setSingleStep(5)

        self.horizontalLayout_122.addWidget(self.spin_roi_y1_2_side)


        self.verticalLayout_64.addLayout(self.horizontalLayout_122)


        self.horizontalLayout_120.addWidget(self.frame_82)

        self.frame_83 = QFrame(self.frame_81)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_83)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.label_42 = QLabel(self.frame_83)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_123.addWidget(self.label_42)

        self.spin_roi_x2_2_side = QSpinBox(self.frame_83)
        self.spin_roi_x2_2_side.setObjectName(u"spin_roi_x2_2_side")
        self.spin_roi_x2_2_side.setMaximum(20000)
        self.spin_roi_x2_2_side.setSingleStep(5)

        self.horizontalLayout_123.addWidget(self.spin_roi_x2_2_side)


        self.verticalLayout_65.addLayout(self.horizontalLayout_123)

        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.label_45 = QLabel(self.frame_83)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_124.addWidget(self.label_45)

        self.spin_roi_y2_2_side = QSpinBox(self.frame_83)
        self.spin_roi_y2_2_side.setObjectName(u"spin_roi_y2_2_side")
        self.spin_roi_y2_2_side.setMaximum(20000)
        self.spin_roi_y2_2_side.setSingleStep(5)

        self.horizontalLayout_124.addWidget(self.spin_roi_y2_2_side)


        self.verticalLayout_65.addLayout(self.horizontalLayout_124)


        self.horizontalLayout_120.addWidget(self.frame_83)


        self.horizontalLayout_119.addWidget(self.frame_81, 0, Qt.AlignHCenter)


        self.verticalLayout_66.addWidget(self.groupBox_24)

        self.frame_140 = QFrame(self.page_2_side)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setMinimumSize(QSize(0, 44))
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_145 = QHBoxLayout(self.frame_140)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.label_93 = QLabel(self.frame_140)
        self.label_93.setObjectName(u"label_93")

        self.horizontalLayout_145.addWidget(self.label_93)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_19)

        self.label_91 = QLabel(self.frame_140)
        self.label_91.setObjectName(u"label_91")

        self.horizontalLayout_145.addWidget(self.label_91)

        self.label_min_lenght_2_side = QLabel(self.frame_140)
        self.label_min_lenght_2_side.setObjectName(u"label_min_lenght_2_side")

        self.horizontalLayout_145.addWidget(self.label_min_lenght_2_side)

        self.label_92 = QLabel(self.frame_140)
        self.label_92.setObjectName(u"label_92")

        self.horizontalLayout_145.addWidget(self.label_92)

        self.label_max_lenght_2_side = QLabel(self.frame_140)
        self.label_max_lenght_2_side.setObjectName(u"label_max_lenght_2_side")

        self.horizontalLayout_145.addWidget(self.label_max_lenght_2_side)

        self.label_94 = QLabel(self.frame_140)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_145.addWidget(self.label_94)

        self.label_avg_lenght_2_side = QLabel(self.frame_140)
        self.label_avg_lenght_2_side.setObjectName(u"label_avg_lenght_2_side")

        self.horizontalLayout_145.addWidget(self.label_avg_lenght_2_side)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_20)


        self.verticalLayout_66.addWidget(self.frame_140)

        self.frame_2282 = QFrame(self.page_2_side)
        self.frame_2282.setObjectName(u"frame_2282")
        self.frame_2282.setMinimumSize(QSize(0, 50))
        self.frame_2282.setFrameShape(QFrame.StyledPanel)
        self.frame_2282.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_2282)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.frame_2283 = QFrame(self.frame_2282)
        self.frame_2283.setObjectName(u"frame_2283")
        self.frame_2283.setFrameShape(QFrame.StyledPanel)
        self.frame_2283.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.frame_2283)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.label_100 = QLabel(self.frame_2283)
        self.label_100.setObjectName(u"label_100")

        self.horizontalLayout_134.addWidget(self.label_100)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_134.addItem(self.horizontalSpacer_22)

        self.label_69 = QLabel(self.frame_2283)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_134.addWidget(self.label_69)

        self.spin_min_lenght_2_side = QSpinBox(self.frame_2283)
        self.spin_min_lenght_2_side.setObjectName(u"spin_min_lenght_2_side")
        self.spin_min_lenght_2_side.setMaximum(20000)
        self.spin_min_lenght_2_side.setSingleStep(5)

        self.horizontalLayout_134.addWidget(self.spin_min_lenght_2_side)

        self.label_70 = QLabel(self.frame_2283)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_134.addWidget(self.label_70)

        self.spin_max_lenght_2_side = QSpinBox(self.frame_2283)
        self.spin_max_lenght_2_side.setObjectName(u"spin_max_lenght_2_side")
        self.spin_max_lenght_2_side.setMaximum(20000)
        self.spin_max_lenght_2_side.setSingleStep(5)

        self.horizontalLayout_134.addWidget(self.spin_max_lenght_2_side)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_134.addItem(self.horizontalSpacer_21)


        self.verticalLayout_69.addWidget(self.frame_2283)


        self.verticalLayout_66.addWidget(self.frame_2282, 0, Qt.AlignHCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_66.addItem(self.verticalSpacer_9)

        self.frame_2286 = QFrame(self.page_2_side)
        self.frame_2286.setObjectName(u"frame_2286")
        self.frame_2286.setFrameShape(QFrame.StyledPanel)
        self.frame_2286.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_2286)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.frame_2287 = QFrame(self.frame_2286)
        self.frame_2287.setObjectName(u"frame_2287")
        self.frame_2287.setEnabled(True)
        self.frame_2287.setMinimumSize(QSize(0, 66))
        self.frame_2287.setMaximumSize(QSize(16777215, 67))
        self.frame_2287.setFrameShape(QFrame.StyledPanel)
        self.frame_2287.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_2287)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_2287)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_59.addWidget(self.label_33, 0, Qt.AlignHCenter)

        self.frame_110 = QFrame(self.frame_2287)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(0, 43))
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_113 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, -1, 0)
        self.bar_thresh0_2_side = QSlider(self.frame_110)
        self.bar_thresh0_2_side.setObjectName(u"bar_thresh0_2_side")
        self.bar_thresh0_2_side.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_2_side.setMaximum(255)
        self.bar_thresh0_2_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_113.addWidget(self.bar_thresh0_2_side)

        self.spinBox_7 = QSpinBox(self.frame_110)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setEnabled(True)
        self.spinBox_7.setMaximum(255)

        self.horizontalLayout_113.addWidget(self.spinBox_7)


        self.verticalLayout_59.addWidget(self.frame_110)


        self.verticalLayout_60.addWidget(self.frame_2287)


        self.verticalLayout_66.addWidget(self.frame_2286)

        self.stackedWidget_2.addWidget(self.page_2_side)
        self.page_3_side = QWidget()
        self.page_3_side.setObjectName(u"page_3_side")
        self.verticalLayout_63 = QVBoxLayout(self.page_3_side)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.label_49 = QLabel(self.page_3_side)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_63.addWidget(self.label_49)

        self.groupBox_25 = QGroupBox(self.page_3_side)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setMinimumSize(QSize(0, 103))
        self.groupBox_25.setMaximumSize(QSize(16777215, 103))
        self.horizontalLayout_126 = QHBoxLayout(self.groupBox_25)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, -1, 0)
        self.frame_85 = QFrame(self.groupBox_25)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.frame_86 = QFrame(self.frame_85)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_86)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.label_50 = QLabel(self.frame_86)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_128.addWidget(self.label_50)

        self.spin_roi_x1_3_side = QSpinBox(self.frame_86)
        self.spin_roi_x1_3_side.setObjectName(u"spin_roi_x1_3_side")
        self.spin_roi_x1_3_side.setMaximum(20000)
        self.spin_roi_x1_3_side.setSingleStep(5)

        self.horizontalLayout_128.addWidget(self.spin_roi_x1_3_side)


        self.verticalLayout_67.addLayout(self.horizontalLayout_128)

        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.label_55 = QLabel(self.frame_86)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_129.addWidget(self.label_55)

        self.spin_roi_y1_3_side = QSpinBox(self.frame_86)
        self.spin_roi_y1_3_side.setObjectName(u"spin_roi_y1_3_side")
        self.spin_roi_y1_3_side.setMaximum(20000)
        self.spin_roi_y1_3_side.setSingleStep(5)

        self.horizontalLayout_129.addWidget(self.spin_roi_y1_3_side)


        self.verticalLayout_67.addLayout(self.horizontalLayout_129)


        self.horizontalLayout_127.addWidget(self.frame_86)

        self.frame_2280 = QFrame(self.frame_85)
        self.frame_2280.setObjectName(u"frame_2280")
        self.frame_2280.setFrameShape(QFrame.StyledPanel)
        self.frame_2280.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_2280)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.label_56 = QLabel(self.frame_2280)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_130.addWidget(self.label_56)

        self.spin_roi_x2_3_side = QSpinBox(self.frame_2280)
        self.spin_roi_x2_3_side.setObjectName(u"spin_roi_x2_3_side")
        self.spin_roi_x2_3_side.setMaximum(20000)
        self.spin_roi_x2_3_side.setSingleStep(5)

        self.horizontalLayout_130.addWidget(self.spin_roi_x2_3_side)


        self.verticalLayout_68.addLayout(self.horizontalLayout_130)

        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.label_58 = QLabel(self.frame_2280)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_131.addWidget(self.label_58)

        self.spin_roi_y2_3_side = QSpinBox(self.frame_2280)
        self.spin_roi_y2_3_side.setObjectName(u"spin_roi_y2_3_side")
        self.spin_roi_y2_3_side.setMaximum(20000)
        self.spin_roi_y2_3_side.setSingleStep(5)

        self.horizontalLayout_131.addWidget(self.spin_roi_y2_3_side)


        self.verticalLayout_68.addLayout(self.horizontalLayout_131)


        self.horizontalLayout_127.addWidget(self.frame_2280)


        self.horizontalLayout_126.addWidget(self.frame_85, 0, Qt.AlignHCenter)


        self.verticalLayout_63.addWidget(self.groupBox_25)

        self.frame_80 = QFrame(self.page_3_side)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_132.addItem(self.horizontalSpacer_14)

        self.label_59 = QLabel(self.frame_80)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_132.addWidget(self.label_59)

        self.spin_jump_thresh_3_side = QSpinBox(self.frame_80)
        self.spin_jump_thresh_3_side.setObjectName(u"spin_jump_thresh_3_side")
        self.spin_jump_thresh_3_side.setMaximum(20000)
        self.spin_jump_thresh_3_side.setSingleStep(1)

        self.horizontalLayout_132.addWidget(self.spin_jump_thresh_3_side)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_132.addItem(self.horizontalSpacer_13)


        self.verticalLayout_63.addWidget(self.frame_80)

        self.line_15 = QFrame(self.page_3_side)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_63.addWidget(self.line_15)

        self.frame_2281 = QFrame(self.page_3_side)
        self.frame_2281.setObjectName(u"frame_2281")
        self.frame_2281.setFrameShape(QFrame.Box)
        self.frame_2281.setFrameShadow(QFrame.Raised)
        self.frame_2281.setLineWidth(2)
        self.horizontalLayout_133 = QHBoxLayout(self.frame_2281)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.label_62 = QLabel(self.frame_2281)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_133.addWidget(self.label_62)

        self.label_thread_lenght_3_side = QLabel(self.frame_2281)
        self.label_thread_lenght_3_side.setObjectName(u"label_thread_lenght_3_side")

        self.horizontalLayout_133.addWidget(self.label_thread_lenght_3_side, 0, Qt.AlignHCenter)

        self.label_60 = QLabel(self.frame_2281)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_133.addWidget(self.label_60)

        self.spin_min_thread_lenght_3_side = QSpinBox(self.frame_2281)
        self.spin_min_thread_lenght_3_side.setObjectName(u"spin_min_thread_lenght_3_side")
        self.spin_min_thread_lenght_3_side.setMaximumSize(QSize(50, 16777215))
        self.spin_min_thread_lenght_3_side.setMaximum(20000)
        self.spin_min_thread_lenght_3_side.setSingleStep(5)

        self.horizontalLayout_133.addWidget(self.spin_min_thread_lenght_3_side)

        self.label_61 = QLabel(self.frame_2281)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_133.addWidget(self.label_61)

        self.spin_max_thread_lenght_3_side = QSpinBox(self.frame_2281)
        self.spin_max_thread_lenght_3_side.setObjectName(u"spin_max_thread_lenght_3_side")
        self.spin_max_thread_lenght_3_side.setMaximumSize(QSize(50, 16777215))
        self.spin_max_thread_lenght_3_side.setMaximum(20000)
        self.spin_max_thread_lenght_3_side.setSingleStep(5)

        self.horizontalLayout_133.addWidget(self.spin_max_thread_lenght_3_side)


        self.verticalLayout_63.addWidget(self.frame_2281)

        self.frame_118 = QFrame(self.page_3_side)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setFrameShape(QFrame.Box)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.frame_118.setLineWidth(2)
        self.horizontalLayout_135 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.label_71 = QLabel(self.frame_118)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_135.addWidget(self.label_71)

        self.label_count_thread_3_side = QLabel(self.frame_118)
        self.label_count_thread_3_side.setObjectName(u"label_count_thread_3_side")

        self.horizontalLayout_135.addWidget(self.label_count_thread_3_side)

        self.label_72 = QLabel(self.frame_118)
        self.label_72.setObjectName(u"label_72")

        self.horizontalLayout_135.addWidget(self.label_72)

        self.spin_min_thread_count_3_side = QSpinBox(self.frame_118)
        self.spin_min_thread_count_3_side.setObjectName(u"spin_min_thread_count_3_side")
        self.spin_min_thread_count_3_side.setMaximumSize(QSize(50, 16777215))
        self.spin_min_thread_count_3_side.setMaximum(20000)
        self.spin_min_thread_count_3_side.setSingleStep(5)

        self.horizontalLayout_135.addWidget(self.spin_min_thread_count_3_side)

        self.label_73 = QLabel(self.frame_118)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_135.addWidget(self.label_73)

        self.spin_max_thread_count_3_side = QSpinBox(self.frame_118)
        self.spin_max_thread_count_3_side.setObjectName(u"spin_max_thread_count_3_side")
        self.spin_max_thread_count_3_side.setMaximumSize(QSize(50, 16777215))
        self.spin_max_thread_count_3_side.setMaximum(20000)
        self.spin_max_thread_count_3_side.setSingleStep(5)

        self.horizontalLayout_135.addWidget(self.spin_max_thread_count_3_side)


        self.verticalLayout_63.addWidget(self.frame_118)

        self.frame_121 = QFrame(self.page_3_side)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFrameShape(QFrame.Box)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.frame_121.setLineWidth(2)
        self.horizontalLayout_136 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.label_74 = QLabel(self.frame_121)
        self.label_74.setObjectName(u"label_74")

        self.horizontalLayout_136.addWidget(self.label_74)

        self.label_step_distance_3_side = QLabel(self.frame_121)
        self.label_step_distance_3_side.setObjectName(u"label_step_distance_3_side")

        self.horizontalLayout_136.addWidget(self.label_step_distance_3_side)

        self.label_75 = QLabel(self.frame_121)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_136.addWidget(self.label_75)

        self.spin_min_thread_distance_3_side = QSpinBox(self.frame_121)
        self.spin_min_thread_distance_3_side.setObjectName(u"spin_min_thread_distance_3_side")
        self.spin_min_thread_distance_3_side.setMaximumSize(QSize(50, 16777215))
        self.spin_min_thread_distance_3_side.setMaximum(20000)
        self.spin_min_thread_distance_3_side.setSingleStep(5)

        self.horizontalLayout_136.addWidget(self.spin_min_thread_distance_3_side)

        self.label_76 = QLabel(self.frame_121)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_136.addWidget(self.label_76)

        self.spin_max_thread_distance_3_side = QSpinBox(self.frame_121)
        self.spin_max_thread_distance_3_side.setObjectName(u"spin_max_thread_distance_3_side")
        self.spin_max_thread_distance_3_side.setMaximumSize(QSize(50, 16777215))
        self.spin_max_thread_distance_3_side.setMaximum(20000)
        self.spin_max_thread_distance_3_side.setSingleStep(5)

        self.horizontalLayout_136.addWidget(self.spin_max_thread_distance_3_side)


        self.verticalLayout_63.addWidget(self.frame_121)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_10)

        self.frame_2289 = QFrame(self.page_3_side)
        self.frame_2289.setObjectName(u"frame_2289")
        self.frame_2289.setMinimumSize(QSize(0, 42))
        self.frame_2289.setFrameShape(QFrame.StyledPanel)
        self.frame_2289.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_2289)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_25 = QLabel(self.frame_2289)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_88.addWidget(self.label_25)

        self.checkbox_navel_3_side = QCheckBox(self.frame_2289)
        self.checkbox_navel_3_side.setObjectName(u"checkbox_navel_3_side")

        self.horizontalLayout_88.addWidget(self.checkbox_navel_3_side)


        self.verticalLayout_63.addWidget(self.frame_2289)

        self.frame_111 = QFrame(self.page_3_side)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_111)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.frame_114 = QFrame(self.frame_111)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setEnabled(True)
        self.frame_114.setMinimumSize(QSize(0, 66))
        self.frame_114.setMaximumSize(QSize(16777215, 67))
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_114)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_114)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_91.addWidget(self.label_34, 0, Qt.AlignHCenter)

        self.frame_115 = QFrame(self.frame_114)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(0, 43))
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(0, 0, -1, 0)
        self.bar_thresh0_3_side = QSlider(self.frame_115)
        self.bar_thresh0_3_side.setObjectName(u"bar_thresh0_3_side")
        self.bar_thresh0_3_side.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_3_side.setMaximum(255)
        self.bar_thresh0_3_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_114.addWidget(self.bar_thresh0_3_side)

        self.spinBox_8 = QSpinBox(self.frame_115)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setEnabled(True)
        self.spinBox_8.setMaximum(255)

        self.horizontalLayout_114.addWidget(self.spinBox_8)


        self.verticalLayout_91.addWidget(self.frame_115)


        self.verticalLayout_92.addWidget(self.frame_114)


        self.verticalLayout_63.addWidget(self.frame_111)

        self.stackedWidget_2.addWidget(self.page_3_side)
        self.page_4_side = QWidget()
        self.page_4_side.setObjectName(u"page_4_side")
        self.verticalLayout_79 = QVBoxLayout(self.page_4_side)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.label_63 = QLabel(self.page_4_side)
        self.label_63.setObjectName(u"label_63")

        self.verticalLayout_79.addWidget(self.label_63)

        self.frame_142 = QFrame(self.page_4_side)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_146 = QHBoxLayout(self.frame_142)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.label_47 = QLabel(self.frame_142)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_146.addWidget(self.label_47)

        self.line_name_region0_4_side = QLineEdit(self.frame_142)
        self.line_name_region0_4_side.setObjectName(u"line_name_region0_4_side")

        self.horizontalLayout_146.addWidget(self.line_name_region0_4_side)


        self.verticalLayout_79.addWidget(self.frame_142, 0, Qt.AlignTop)

        self.frame_84 = QFrame(self.page_4_side)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMaximumSize(QSize(16777215, 61))
        self.frame_84.setFrameShape(QFrame.Box)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.btn_add_region0_4_side = QPushButton(self.frame_84)
        self.btn_add_region0_4_side.setObjectName(u"btn_add_region0_4_side")
        self.btn_add_region0_4_side.setMaximumSize(QSize(26, 16777215))
        self.btn_add_region0_4_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_region0_4_side.setStyleSheet(u"border:none;\n"
"")
        self.btn_add_region0_4_side.setIcon(icon16)
        self.btn_add_region0_4_side.setIconSize(QSize(26, 26))

        self.horizontalLayout_125.addWidget(self.btn_add_region0_4_side)

        self.combo_regions_name0_4_side = QComboBox(self.frame_84)
        self.combo_regions_name0_4_side.setObjectName(u"combo_regions_name0_4_side")
        self.combo_regions_name0_4_side.setMinimumSize(QSize(191, 0))
        self.combo_regions_name0_4_side.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_125.addWidget(self.combo_regions_name0_4_side)

        self.btn_remove_region0_4_side = QPushButton(self.frame_84)
        self.btn_remove_region0_4_side.setObjectName(u"btn_remove_region0_4_side")
        self.btn_remove_region0_4_side.setMaximumSize(QSize(26, 16777215))
        self.btn_remove_region0_4_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove_region0_4_side.setStyleSheet(u"border:none;")
        self.btn_remove_region0_4_side.setIcon(icon17)
        self.btn_remove_region0_4_side.setIconSize(QSize(26, 27))

        self.horizontalLayout_125.addWidget(self.btn_remove_region0_4_side)


        self.verticalLayout_79.addWidget(self.frame_84, 0, Qt.AlignTop)

        self.line_34 = QFrame(self.page_4_side)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.HLine)
        self.line_34.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_79.addWidget(self.line_34, 0, Qt.AlignTop)

        self.frame_141 = QFrame(self.page_4_side)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setMaximumSize(QSize(16777215, 300))
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_141)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.groupBox_26 = QGroupBox(self.frame_141)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setMinimumSize(QSize(0, 103))
        self.groupBox_26.setMaximumSize(QSize(16777215, 103))
        self.horizontalLayout_137 = QHBoxLayout(self.groupBox_26)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(0, 0, -1, 0)
        self.frame_124 = QFrame(self.groupBox_26)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.frame_124)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.frame_127 = QFrame(self.frame_124)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_127)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_139 = QHBoxLayout()
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.label_78 = QLabel(self.frame_127)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_139.addWidget(self.label_78)

        self.spin_roi_x1_4_side = QSpinBox(self.frame_127)
        self.spin_roi_x1_4_side.setObjectName(u"spin_roi_x1_4_side")
        self.spin_roi_x1_4_side.setMaximum(20000)
        self.spin_roi_x1_4_side.setSingleStep(5)

        self.horizontalLayout_139.addWidget(self.spin_roi_x1_4_side)


        self.verticalLayout_71.addLayout(self.horizontalLayout_139)

        self.horizontalLayout_140 = QHBoxLayout()
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.label_79 = QLabel(self.frame_127)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_140.addWidget(self.label_79)

        self.spin_roi_y1_4_side = QSpinBox(self.frame_127)
        self.spin_roi_y1_4_side.setObjectName(u"spin_roi_y1_4_side")
        self.spin_roi_y1_4_side.setMaximum(20000)
        self.spin_roi_y1_4_side.setSingleStep(5)

        self.horizontalLayout_140.addWidget(self.spin_roi_y1_4_side)


        self.verticalLayout_71.addLayout(self.horizontalLayout_140)


        self.horizontalLayout_138.addWidget(self.frame_127)

        self.frame_131 = QFrame(self.frame_124)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_131)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_141 = QHBoxLayout()
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.label_80 = QLabel(self.frame_131)
        self.label_80.setObjectName(u"label_80")

        self.horizontalLayout_141.addWidget(self.label_80)

        self.spin_roi_x2_4_side = QSpinBox(self.frame_131)
        self.spin_roi_x2_4_side.setObjectName(u"spin_roi_x2_4_side")
        self.spin_roi_x2_4_side.setMaximum(20000)
        self.spin_roi_x2_4_side.setSingleStep(5)

        self.horizontalLayout_141.addWidget(self.spin_roi_x2_4_side)


        self.verticalLayout_73.addLayout(self.horizontalLayout_141)

        self.horizontalLayout_142 = QHBoxLayout()
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.label_81 = QLabel(self.frame_131)
        self.label_81.setObjectName(u"label_81")

        self.horizontalLayout_142.addWidget(self.label_81)

        self.spin_roi_y2_4_side = QSpinBox(self.frame_131)
        self.spin_roi_y2_4_side.setObjectName(u"spin_roi_y2_4_side")
        self.spin_roi_y2_4_side.setMaximum(20000)
        self.spin_roi_y2_4_side.setSingleStep(5)

        self.horizontalLayout_142.addWidget(self.spin_roi_y2_4_side)


        self.verticalLayout_73.addLayout(self.horizontalLayout_142)


        self.horizontalLayout_138.addWidget(self.frame_131)


        self.horizontalLayout_137.addWidget(self.frame_124, 0, Qt.AlignHCenter)


        self.verticalLayout_80.addWidget(self.groupBox_26)

        self.frame_145 = QFrame(self.frame_141)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setMinimumSize(QSize(0, 44))
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_159 = QHBoxLayout(self.frame_145)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.label_103 = QLabel(self.frame_145)
        self.label_103.setObjectName(u"label_103")

        self.horizontalLayout_159.addWidget(self.label_103)

        self.label_106 = QLabel(self.frame_145)
        self.label_106.setObjectName(u"label_106")

        self.horizontalLayout_159.addWidget(self.label_106)

        self.label_min_diameter_4_side = QLabel(self.frame_145)
        self.label_min_diameter_4_side.setObjectName(u"label_min_diameter_4_side")

        self.horizontalLayout_159.addWidget(self.label_min_diameter_4_side)

        self.label_107 = QLabel(self.frame_145)
        self.label_107.setObjectName(u"label_107")

        self.horizontalLayout_159.addWidget(self.label_107)

        self.label_max_diameter_4_side = QLabel(self.frame_145)
        self.label_max_diameter_4_side.setObjectName(u"label_max_diameter_4_side")

        self.horizontalLayout_159.addWidget(self.label_max_diameter_4_side)

        self.label_108 = QLabel(self.frame_145)
        self.label_108.setObjectName(u"label_108")

        self.horizontalLayout_159.addWidget(self.label_108)

        self.label_avg_diameter_4_side = QLabel(self.frame_145)
        self.label_avg_diameter_4_side.setObjectName(u"label_avg_diameter_4_side")

        self.horizontalLayout_159.addWidget(self.label_avg_diameter_4_side)


        self.verticalLayout_80.addWidget(self.frame_145)

        self.frame_136 = QFrame(self.frame_141)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setMinimumSize(QSize(0, 0))
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.frame_136)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.label_82 = QLabel(self.frame_136)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_143.addWidget(self.label_82)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_18)

        self.label_84 = QLabel(self.frame_136)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_143.addWidget(self.label_84)

        self.spin_min_body_diameter_4_side = QSpinBox(self.frame_136)
        self.spin_min_body_diameter_4_side.setObjectName(u"spin_min_body_diameter_4_side")
        self.spin_min_body_diameter_4_side.setMaximumSize(QSize(50, 16777215))
        self.spin_min_body_diameter_4_side.setMaximum(20000)
        self.spin_min_body_diameter_4_side.setSingleStep(5)

        self.horizontalLayout_143.addWidget(self.spin_min_body_diameter_4_side)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_17)

        self.label_85 = QLabel(self.frame_136)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_143.addWidget(self.label_85)

        self.spin_max_body_diameter_4_side = QSpinBox(self.frame_136)
        self.spin_max_body_diameter_4_side.setObjectName(u"spin_max_body_diameter_4_side")
        self.spin_max_body_diameter_4_side.setMaximumSize(QSize(50, 16777215))
        self.spin_max_body_diameter_4_side.setMaximum(20000)
        self.spin_max_body_diameter_4_side.setSingleStep(5)

        self.horizontalLayout_143.addWidget(self.spin_max_body_diameter_4_side)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_16)


        self.verticalLayout_80.addWidget(self.frame_136)

        self.btn_complete_area_4_side = QPushButton(self.frame_141)
        self.btn_complete_area_4_side.setObjectName(u"btn_complete_area_4_side")
        self.btn_complete_area_4_side.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_80.addWidget(self.btn_complete_area_4_side, 0, Qt.AlignHCenter)


        self.verticalLayout_79.addWidget(self.frame_141)

        self.frame_116 = QFrame(self.page_4_side)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_116)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.frame_117 = QFrame(self.frame_116)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setEnabled(True)
        self.frame_117.setMinimumSize(QSize(0, 66))
        self.frame_117.setMaximumSize(QSize(16777215, 67))
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_117)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_117)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_93.addWidget(self.label_38, 0, Qt.AlignHCenter)

        self.frame_119 = QFrame(self.frame_117)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMinimumSize(QSize(0, 43))
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.frame_119)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(0, 0, -1, 0)
        self.bar_thresh0_4_side = QSlider(self.frame_119)
        self.bar_thresh0_4_side.setObjectName(u"bar_thresh0_4_side")
        self.bar_thresh0_4_side.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_4_side.setMaximum(255)
        self.bar_thresh0_4_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_115.addWidget(self.bar_thresh0_4_side)

        self.spinBox_9 = QSpinBox(self.frame_119)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setEnabled(True)
        self.spinBox_9.setMaximum(255)

        self.horizontalLayout_115.addWidget(self.spinBox_9)


        self.verticalLayout_93.addWidget(self.frame_119)


        self.verticalLayout_96.addWidget(self.frame_117)


        self.verticalLayout_79.addWidget(self.frame_116)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_79.addItem(self.verticalSpacer_11)

        self.stackedWidget_2.addWidget(self.page_4_side)
        self.page_5_side = QWidget()
        self.page_5_side.setObjectName(u"page_5_side")
        self.verticalLayout_85 = QVBoxLayout(self.page_5_side)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.frame_38 = QFrame(self.page_5_side)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_38)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.label_68 = QLabel(self.frame_38)
        self.label_68.setObjectName(u"label_68")

        self.verticalLayout_83.addWidget(self.label_68)

        self.groupBox_27 = QGroupBox(self.frame_38)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setMinimumSize(QSize(0, 103))
        self.groupBox_27.setMaximumSize(QSize(16777215, 103))
        self.horizontalLayout_147 = QHBoxLayout(self.groupBox_27)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(0, 0, -1, 0)
        self.frame_125 = QFrame(self.groupBox_27)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_148 = QHBoxLayout(self.frame_125)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.frame_128 = QFrame(self.frame_125)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_128)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_149 = QHBoxLayout()
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.label_83 = QLabel(self.frame_128)
        self.label_83.setObjectName(u"label_83")

        self.horizontalLayout_149.addWidget(self.label_83)

        self.spin_roi_x1_5_side = QSpinBox(self.frame_128)
        self.spin_roi_x1_5_side.setObjectName(u"spin_roi_x1_5_side")
        self.spin_roi_x1_5_side.setMaximum(20000)
        self.spin_roi_x1_5_side.setSingleStep(5)

        self.horizontalLayout_149.addWidget(self.spin_roi_x1_5_side)


        self.verticalLayout_81.addLayout(self.horizontalLayout_149)

        self.horizontalLayout_150 = QHBoxLayout()
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.label_86 = QLabel(self.frame_128)
        self.label_86.setObjectName(u"label_86")

        self.horizontalLayout_150.addWidget(self.label_86)

        self.spin_roi_y1_5_side = QSpinBox(self.frame_128)
        self.spin_roi_y1_5_side.setObjectName(u"spin_roi_y1_5_side")
        self.spin_roi_y1_5_side.setMaximum(20000)
        self.spin_roi_y1_5_side.setSingleStep(5)

        self.horizontalLayout_150.addWidget(self.spin_roi_y1_5_side)


        self.verticalLayout_81.addLayout(self.horizontalLayout_150)


        self.horizontalLayout_148.addWidget(self.frame_128)

        self.frame_132 = QFrame(self.frame_125)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_132)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_151 = QHBoxLayout()
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.label_87 = QLabel(self.frame_132)
        self.label_87.setObjectName(u"label_87")

        self.horizontalLayout_151.addWidget(self.label_87)

        self.spin_roi_x2_5_side = QSpinBox(self.frame_132)
        self.spin_roi_x2_5_side.setObjectName(u"spin_roi_x2_5_side")
        self.spin_roi_x2_5_side.setMaximum(20000)
        self.spin_roi_x2_5_side.setSingleStep(5)

        self.horizontalLayout_151.addWidget(self.spin_roi_x2_5_side)


        self.verticalLayout_82.addLayout(self.horizontalLayout_151)

        self.horizontalLayout_152 = QHBoxLayout()
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.label_88 = QLabel(self.frame_132)
        self.label_88.setObjectName(u"label_88")

        self.horizontalLayout_152.addWidget(self.label_88)

        self.spin_roi_y2_5_side = QSpinBox(self.frame_132)
        self.spin_roi_y2_5_side.setObjectName(u"spin_roi_y2_5_side")
        self.spin_roi_y2_5_side.setMaximum(20000)
        self.spin_roi_y2_5_side.setSingleStep(5)

        self.horizontalLayout_152.addWidget(self.spin_roi_y2_5_side)


        self.verticalLayout_82.addLayout(self.horizontalLayout_152)


        self.horizontalLayout_148.addWidget(self.frame_132)


        self.horizontalLayout_147.addWidget(self.frame_125, 0, Qt.AlignHCenter)


        self.verticalLayout_83.addWidget(self.groupBox_27)

        self.line = QFrame(self.frame_38)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_83.addWidget(self.line)

        self.frame_65 = QFrame(self.frame_38)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(0, 66))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_23 = QLabel(self.frame_65)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_71.addWidget(self.label_23)

        self.btn_top_5_side = QRadioButton(self.frame_65)
        self.btn_top_5_side.setObjectName(u"btn_top_5_side")

        self.horizontalLayout_71.addWidget(self.btn_top_5_side)

        self.btn_bottom_5_side = QRadioButton(self.frame_65)
        self.btn_bottom_5_side.setObjectName(u"btn_bottom_5_side")

        self.horizontalLayout_71.addWidget(self.btn_bottom_5_side)


        self.verticalLayout_83.addWidget(self.frame_65)

        self.frame_149 = QFrame(self.frame_38)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setMinimumSize(QSize(0, 66))
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_149)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.checkbox_belt_5_side = QRadioButton(self.frame_149)
        self.checkbox_belt_5_side.setObjectName(u"checkbox_belt_5_side")

        self.horizontalLayout_79.addWidget(self.checkbox_belt_5_side, 0, Qt.AlignHCenter)


        self.verticalLayout_83.addWidget(self.frame_149)

        self.frame_146 = QFrame(self.frame_38)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setMinimumSize(QSize(0, 44))
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_160 = QHBoxLayout(self.frame_146)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.label_111 = QLabel(self.frame_146)
        self.label_111.setObjectName(u"label_111")

        self.horizontalLayout_160.addWidget(self.label_111)

        self.label_112 = QLabel(self.frame_146)
        self.label_112.setObjectName(u"label_112")

        self.horizontalLayout_160.addWidget(self.label_112)

        self.label_min_head_height_5_side = QLabel(self.frame_146)
        self.label_min_head_height_5_side.setObjectName(u"label_min_head_height_5_side")

        self.horizontalLayout_160.addWidget(self.label_min_head_height_5_side)

        self.label_113 = QLabel(self.frame_146)
        self.label_113.setObjectName(u"label_113")

        self.horizontalLayout_160.addWidget(self.label_113)

        self.label_max_head_height_5_side = QLabel(self.frame_146)
        self.label_max_head_height_5_side.setObjectName(u"label_max_head_height_5_side")

        self.horizontalLayout_160.addWidget(self.label_max_head_height_5_side)

        self.label_114 = QLabel(self.frame_146)
        self.label_114.setObjectName(u"label_114")

        self.horizontalLayout_160.addWidget(self.label_114)

        self.label_avg_head_height_5_side = QLabel(self.frame_146)
        self.label_avg_head_height_5_side.setObjectName(u"label_avg_head_height_5_side")

        self.horizontalLayout_160.addWidget(self.label_avg_head_height_5_side)


        self.verticalLayout_83.addWidget(self.frame_146)

        self.line_14 = QFrame(self.frame_38)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_83.addWidget(self.line_14)

        self.frame_138 = QFrame(self.frame_38)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_166 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.label_30 = QLabel(self.frame_138)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_166.addWidget(self.label_30)

        self.label_109 = QLabel(self.frame_138)
        self.label_109.setObjectName(u"label_109")

        self.horizontalLayout_166.addWidget(self.label_109)

        self.spin_min_height_5_side = QSpinBox(self.frame_138)
        self.spin_min_height_5_side.setObjectName(u"spin_min_height_5_side")
        self.spin_min_height_5_side.setMaximumSize(QSize(50, 16777215))
        self.spin_min_height_5_side.setMaximum(20000)
        self.spin_min_height_5_side.setSingleStep(5)

        self.horizontalLayout_166.addWidget(self.spin_min_height_5_side)

        self.label_110 = QLabel(self.frame_138)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_166.addWidget(self.label_110)

        self.spin_max_height_5_side = QSpinBox(self.frame_138)
        self.spin_max_height_5_side.setObjectName(u"spin_max_height_5_side")
        self.spin_max_height_5_side.setMaximumSize(QSize(50, 16777215))
        self.spin_max_height_5_side.setMaximum(20000)
        self.spin_max_height_5_side.setSingleStep(5)

        self.horizontalLayout_166.addWidget(self.spin_max_height_5_side)


        self.verticalLayout_83.addWidget(self.frame_138)

        self.frame_76 = QFrame(self.frame_38)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(0, 30))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_28 = QLabel(self.frame_76)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_73.addWidget(self.label_28)

        self.spin_jump_thresh_5_side = QSpinBox(self.frame_76)
        self.spin_jump_thresh_5_side.setObjectName(u"spin_jump_thresh_5_side")

        self.horizontalLayout_73.addWidget(self.spin_jump_thresh_5_side)


        self.verticalLayout_83.addWidget(self.frame_76, 0, Qt.AlignHCenter)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_83.addItem(self.verticalSpacer_12)

        self.frame_120 = QFrame(self.frame_38)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_120)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.frame_122 = QFrame(self.frame_120)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setEnabled(True)
        self.frame_122.setMinimumSize(QSize(0, 66))
        self.frame_122.setMaximumSize(QSize(16777215, 67))
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_122)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_122)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_97.addWidget(self.label_39, 0, Qt.AlignHCenter)

        self.frame_123 = QFrame(self.frame_122)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMinimumSize(QSize(0, 43))
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(0, 0, -1, 0)
        self.bar_thresh0_5_side = QSlider(self.frame_123)
        self.bar_thresh0_5_side.setObjectName(u"bar_thresh0_5_side")
        self.bar_thresh0_5_side.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_5_side.setMaximum(255)
        self.bar_thresh0_5_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_116.addWidget(self.bar_thresh0_5_side)

        self.spinBox_10 = QSpinBox(self.frame_123)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setEnabled(True)
        self.spinBox_10.setMaximum(255)

        self.horizontalLayout_116.addWidget(self.spinBox_10)


        self.verticalLayout_97.addWidget(self.frame_123)


        self.verticalLayout_98.addWidget(self.frame_122)


        self.verticalLayout_83.addWidget(self.frame_120)


        self.verticalLayout_85.addWidget(self.frame_38)

        self.stackedWidget_2.addWidget(self.page_5_side)
        self.page_6_side = QWidget()
        self.page_6_side.setObjectName(u"page_6_side")
        self.verticalLayout_89 = QVBoxLayout(self.page_6_side)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.label_24 = QLabel(self.page_6_side)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_89.addWidget(self.label_24)

        self.frame_144 = QFrame(self.page_6_side)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_154 = QHBoxLayout(self.frame_144)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.label_48 = QLabel(self.frame_144)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_154.addWidget(self.label_48)

        self.line_name_region0_6_side = QLineEdit(self.frame_144)
        self.line_name_region0_6_side.setObjectName(u"line_name_region0_6_side")

        self.horizontalLayout_154.addWidget(self.line_name_region0_6_side)


        self.verticalLayout_89.addWidget(self.frame_144, 0, Qt.AlignTop)

        self.frame_113 = QFrame(self.page_6_side)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMaximumSize(QSize(16777215, 61))
        self.frame_113.setFrameShape(QFrame.Box)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_153 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.btn_add_region0_6_side = QPushButton(self.frame_113)
        self.btn_add_region0_6_side.setObjectName(u"btn_add_region0_6_side")
        self.btn_add_region0_6_side.setMaximumSize(QSize(26, 16777215))
        self.btn_add_region0_6_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_region0_6_side.setStyleSheet(u"border:none;\n"
"")
        self.btn_add_region0_6_side.setIcon(icon16)
        self.btn_add_region0_6_side.setIconSize(QSize(26, 26))

        self.horizontalLayout_153.addWidget(self.btn_add_region0_6_side)

        self.combo_regions_name0_6_side = QComboBox(self.frame_113)
        self.combo_regions_name0_6_side.setObjectName(u"combo_regions_name0_6_side")
        self.combo_regions_name0_6_side.setMinimumSize(QSize(191, 0))
        self.combo_regions_name0_6_side.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_153.addWidget(self.combo_regions_name0_6_side)

        self.btn_remove_region0_6_side = QPushButton(self.frame_113)
        self.btn_remove_region0_6_side.setObjectName(u"btn_remove_region0_6_side")
        self.btn_remove_region0_6_side.setMaximumSize(QSize(26, 16777215))
        self.btn_remove_region0_6_side.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove_region0_6_side.setStyleSheet(u"border:none;")
        self.btn_remove_region0_6_side.setIcon(icon17)
        self.btn_remove_region0_6_side.setIconSize(QSize(26, 27))

        self.horizontalLayout_153.addWidget(self.btn_remove_region0_6_side)


        self.verticalLayout_89.addWidget(self.frame_113, 0, Qt.AlignTop)

        self.line_35 = QFrame(self.page_6_side)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.HLine)
        self.line_35.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_89.addWidget(self.line_35, 0, Qt.AlignTop)

        self.frame_143 = QFrame(self.page_6_side)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setMinimumSize(QSize(0, 0))
        self.frame_143.setMaximumSize(QSize(16777215, 0))
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_143)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.groupBox_28 = QGroupBox(self.frame_143)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setMinimumSize(QSize(0, 103))
        self.groupBox_28.setMaximumSize(QSize(16777215, 103))
        self.horizontalLayout_155 = QHBoxLayout(self.groupBox_28)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(0, 0, -1, 0)
        self.frame_126 = QFrame(self.groupBox_28)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_156 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.frame_129 = QFrame(self.frame_126)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_129)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_157 = QHBoxLayout()
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.label_89 = QLabel(self.frame_129)
        self.label_89.setObjectName(u"label_89")

        self.horizontalLayout_157.addWidget(self.label_89)

        self.spin_roi_x1_6_side = QSpinBox(self.frame_129)
        self.spin_roi_x1_6_side.setObjectName(u"spin_roi_x1_6_side")
        self.spin_roi_x1_6_side.setMaximum(20000)
        self.spin_roi_x1_6_side.setSingleStep(5)

        self.horizontalLayout_157.addWidget(self.spin_roi_x1_6_side)


        self.verticalLayout_87.addLayout(self.horizontalLayout_157)

        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.label_90 = QLabel(self.frame_129)
        self.label_90.setObjectName(u"label_90")

        self.horizontalLayout_158.addWidget(self.label_90)

        self.spin_roi_y1_6_side = QSpinBox(self.frame_129)
        self.spin_roi_y1_6_side.setObjectName(u"spin_roi_y1_6_side")
        self.spin_roi_y1_6_side.setMaximum(20000)
        self.spin_roi_y1_6_side.setSingleStep(5)

        self.horizontalLayout_158.addWidget(self.spin_roi_y1_6_side)


        self.verticalLayout_87.addLayout(self.horizontalLayout_158)


        self.horizontalLayout_156.addWidget(self.frame_129)

        self.frame_133 = QFrame(self.frame_126)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_133)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_163 = QHBoxLayout()
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.label_101 = QLabel(self.frame_133)
        self.label_101.setObjectName(u"label_101")

        self.horizontalLayout_163.addWidget(self.label_101)

        self.spin_roi_x2_6_side = QSpinBox(self.frame_133)
        self.spin_roi_x2_6_side.setObjectName(u"spin_roi_x2_6_side")
        self.spin_roi_x2_6_side.setMaximum(20000)
        self.spin_roi_x2_6_side.setSingleStep(5)

        self.horizontalLayout_163.addWidget(self.spin_roi_x2_6_side)


        self.verticalLayout_88.addLayout(self.horizontalLayout_163)

        self.horizontalLayout_164 = QHBoxLayout()
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.label_102 = QLabel(self.frame_133)
        self.label_102.setObjectName(u"label_102")

        self.horizontalLayout_164.addWidget(self.label_102)

        self.spin_roi_y2_6_side = QSpinBox(self.frame_133)
        self.spin_roi_y2_6_side.setObjectName(u"spin_roi_y2_6_side")
        self.spin_roi_y2_6_side.setMaximum(20000)
        self.spin_roi_y2_6_side.setSingleStep(5)

        self.horizontalLayout_164.addWidget(self.spin_roi_y2_6_side)


        self.verticalLayout_88.addLayout(self.horizontalLayout_164)


        self.horizontalLayout_156.addWidget(self.frame_133)


        self.horizontalLayout_155.addWidget(self.frame_126, 0, Qt.AlignHCenter)


        self.verticalLayout_86.addWidget(self.groupBox_28)

        self.frame_137 = QFrame(self.frame_143)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_165 = QHBoxLayout(self.frame_137)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.label_27 = QLabel(self.frame_137)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_165.addWidget(self.label_27)

        self.label_area_6_side = QLabel(self.frame_137)
        self.label_area_6_side.setObjectName(u"label_area_6_side")

        self.horizontalLayout_165.addWidget(self.label_area_6_side, 0, Qt.AlignHCenter)

        self.label_104 = QLabel(self.frame_137)
        self.label_104.setObjectName(u"label_104")

        self.horizontalLayout_165.addWidget(self.label_104)

        self.spin_min_damage_6_side = QSpinBox(self.frame_137)
        self.spin_min_damage_6_side.setObjectName(u"spin_min_damage_6_side")
        self.spin_min_damage_6_side.setMaximumSize(QSize(50, 16777215))
        self.spin_min_damage_6_side.setMaximum(20000)
        self.spin_min_damage_6_side.setSingleStep(5)

        self.horizontalLayout_165.addWidget(self.spin_min_damage_6_side)

        self.label_105 = QLabel(self.frame_137)
        self.label_105.setObjectName(u"label_105")

        self.horizontalLayout_165.addWidget(self.label_105)

        self.spin_max_damage_6_side = QSpinBox(self.frame_137)
        self.spin_max_damage_6_side.setObjectName(u"spin_max_damage_6_side")
        self.spin_max_damage_6_side.setMaximumSize(QSize(50, 16777215))
        self.spin_max_damage_6_side.setMaximum(20000)
        self.spin_max_damage_6_side.setSingleStep(5)

        self.horizontalLayout_165.addWidget(self.spin_max_damage_6_side)


        self.verticalLayout_86.addWidget(self.frame_137)

        self.btn_complete_area_6_side = QPushButton(self.frame_143)
        self.btn_complete_area_6_side.setObjectName(u"btn_complete_area_6_side")
        self.btn_complete_area_6_side.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_86.addWidget(self.btn_complete_area_6_side, 0, Qt.AlignHCenter)


        self.verticalLayout_89.addWidget(self.frame_143)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_89.addItem(self.verticalSpacer_13)

        self.frame_130 = QFrame(self.page_6_side)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_130)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.frame_134 = QFrame(self.frame_130)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setEnabled(True)
        self.frame_134.setMinimumSize(QSize(0, 66))
        self.frame_134.setMaximumSize(QSize(16777215, 67))
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_134)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.frame_134)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_99.addWidget(self.label_77, 0, Qt.AlignHCenter)

        self.frame_135 = QFrame(self.frame_134)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setMinimumSize(QSize(0, 43))
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_161 = QHBoxLayout(self.frame_135)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.horizontalLayout_161.setContentsMargins(0, 0, -1, 0)
        self.bar_thresh0_6_side = QSlider(self.frame_135)
        self.bar_thresh0_6_side.setObjectName(u"bar_thresh0_6_side")
        self.bar_thresh0_6_side.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_6_side.setMaximum(255)
        self.bar_thresh0_6_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_161.addWidget(self.bar_thresh0_6_side)

        self.spinBox_11 = QSpinBox(self.frame_135)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setEnabled(True)
        self.spinBox_11.setMaximum(255)

        self.horizontalLayout_161.addWidget(self.spinBox_11)


        self.verticalLayout_99.addWidget(self.frame_135)


        self.verticalLayout_100.addWidget(self.frame_134)


        self.verticalLayout_89.addWidget(self.frame_130)

        self.stackedWidget_2.addWidget(self.page_6_side)

        self.verticalLayout_30.addWidget(self.stackedWidget_2)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_17)

        self.frame_save_btns = QFrame(self.frame_37)
        self.frame_save_btns.setObjectName(u"frame_save_btns")
        self.frame_save_btns.setMinimumSize(QSize(253, 0))
        self.frame_save_btns.setMaximumSize(QSize(16777215, 0))
        self.frame_save_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_save_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_save_btns)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.prev_page_btn = QPushButton(self.frame_save_btns)
        self.prev_page_btn.setObjectName(u"prev_page_btn")
        self.prev_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prev_page_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200,200,200);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u"images/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_page_btn.setIcon(icon18)

        self.horizontalLayout_39.addWidget(self.prev_page_btn)

        self.save_btn_page_grab = QPushButton(self.frame_save_btns)
        self.save_btn_page_grab.setObjectName(u"save_btn_page_grab")
        self.save_btn_page_grab.setEnabled(True)
        self.save_btn_page_grab.setMinimumSize(QSize(100, 32))
        self.save_btn_page_grab.setMaximumSize(QSize(100, 16777215))
        self.save_btn_page_grab.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_39.addWidget(self.save_btn_page_grab)

        self.next_page_btn = QPushButton(self.frame_save_btns)
        self.next_page_btn.setObjectName(u"next_page_btn")
        self.next_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_page_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200,200,200);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u"images/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_page_btn.setIcon(icon19)

        self.horizontalLayout_39.addWidget(self.next_page_btn)


        self.verticalLayout_30.addWidget(self.frame_save_btns, 0, Qt.AlignHCenter)


        self.horizontalLayout_22.addWidget(self.frame_37)

        self.line_7 = QFrame(self.frame_4)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_22.addWidget(self.line_7)

        self.frame_51 = QFrame(self.frame_4)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(69, 24))
        self.frame_51.setMaximumSize(QSize(16777215, 16777195))
        self.frame_51.setFrameShape(QFrame.Box)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.frame_51.setLineWidth(2)
        self.verticalLayout_40 = QVBoxLayout(self.frame_51)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_image_grab_page = QLabel(self.frame_51)
        self.label_image_grab_page.setObjectName(u"label_image_grab_page")
        self.label_image_grab_page.setPixmap(QPixmap(u"../../../../../home/milad/.designer/backup/images/test1_0_12.png"))
        self.label_image_grab_page.setScaledContents(True)

        self.verticalLayout_40.addWidget(self.label_image_grab_page)

        self.line_8 = QFrame(self.frame_51)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_40.addWidget(self.line_8)

        self.frame_2285 = QFrame(self.frame_51)
        self.frame_2285.setObjectName(u"frame_2285")
        self.frame_2285.setMinimumSize(QSize(0, 48))
        self.frame_2285.setMaximumSize(QSize(16777215, 48))
        self.frame_2285.setFrameShape(QFrame.StyledPanel)
        self.frame_2285.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_2285)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.frame_77 = QFrame(self.frame_2285)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(236, 36))
        self.frame_77.setMaximumSize(QSize(220, 16777215))
        self.frame_77.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_77)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_72.addWidget(self.label_32)

        self.label_35 = QLabel(self.frame_77)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_72.addWidget(self.label_35)

        self.label_x_pos_tool_page = QLabel(self.frame_77)
        self.label_x_pos_tool_page.setObjectName(u"label_x_pos_tool_page")

        self.horizontalLayout_72.addWidget(self.label_x_pos_tool_page)

        self.label_37 = QLabel(self.frame_77)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_72.addWidget(self.label_37)

        self.label_y_pos_tool_page = QLabel(self.frame_77)
        self.label_y_pos_tool_page.setObjectName(u"label_y_pos_tool_page")

        self.horizontalLayout_72.addWidget(self.label_y_pos_tool_page)

        self.label_36 = QLabel(self.frame_77)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_72.addWidget(self.label_36)

        self.label_31 = QLabel(self.frame_77)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_72.addWidget(self.label_31)

        self.label_color_value = QLabel(self.frame_77)
        self.label_color_value.setObjectName(u"label_color_value")

        self.horizontalLayout_72.addWidget(self.label_color_value)

        self.img_color_value = QLabel(self.frame_77)
        self.img_color_value.setObjectName(u"img_color_value")
        self.img_color_value.setMinimumSize(QSize(27, 27))
        self.img_color_value.setMaximumSize(QSize(27, 27))
        self.img_color_value.setFrameShape(QFrame.Box)
        self.img_color_value.setScaledContents(True)
        self.img_color_value.setMargin(1)

        self.horizontalLayout_72.addWidget(self.img_color_value)


        self.horizontalLayout_74.addWidget(self.frame_77)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_74.addItem(self.horizontalSpacer_24)

        self.frame_39 = QFrame(self.frame_2285)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 36))
        self.frame_39.setMaximumSize(QSize(439, 45))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_23)

        self.label_188 = QLabel(self.frame_39)
        self.label_188.setObjectName(u"label_188")

        self.horizontalLayout_42.addWidget(self.label_188)

        self.btn_enabel_mask_draw = QCheckBox(self.frame_39)
        self.btn_enabel_mask_draw.setObjectName(u"btn_enabel_mask_draw")
        self.btn_enabel_mask_draw.setChecked(True)
        self.btn_enabel_mask_draw.setTristate(False)

        self.horizontalLayout_42.addWidget(self.btn_enabel_mask_draw)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_6)

        self.fullscreen_cam_grab_2 = QPushButton(self.frame_39)
        self.fullscreen_cam_grab_2.setObjectName(u"fullscreen_cam_grab_2")
        self.fullscreen_cam_grab_2.setMaximumSize(QSize(50, 50))
        self.fullscreen_cam_grab_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.fullscreen_cam_grab_2.setStyleSheet(u"border:None;")
        icon20 = QIcon()
        icon20.addFile(u"../../../../../home/milad/.designer/backup/images/x-mark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreen_cam_grab_2.setIcon(icon20)
        self.fullscreen_cam_grab_2.setIconSize(QSize(30, 40))

        self.horizontalLayout_42.addWidget(self.fullscreen_cam_grab_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_7)

        self.fullscreen_page_tools = QPushButton(self.frame_39)
        self.fullscreen_page_tools.setObjectName(u"fullscreen_page_tools")
        self.fullscreen_page_tools.setMaximumSize(QSize(50, 50))
        self.fullscreen_page_tools.setCursor(QCursor(Qt.PointingHandCursor))
        self.fullscreen_page_tools.setStyleSheet(u"border:None;")
        icon21 = QIcon()
        icon21.addFile(u"../../../../../home/milad/.designer/backup/images/full-screen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreen_page_tools.setIcon(icon21)
        self.fullscreen_page_tools.setIconSize(QSize(30, 40))

        self.horizontalLayout_42.addWidget(self.fullscreen_page_tools)


        self.horizontalLayout_74.addWidget(self.frame_39)


        self.verticalLayout_40.addWidget(self.frame_2285)


        self.horizontalLayout_22.addWidget(self.frame_51)


        self.verticalLayout_26.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_tools)
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
        icon22 = QIcon()
        icon22.addFile(u"images/camtop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.camera01_btn.setIcon(icon22)
        self.camera01_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_13.addWidget(self.camera01_btn)

        self.camera02_btn = QPushButton(self.frame_3)
        self.camera02_btn.setObjectName(u"camera02_btn")
        self.camera02_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera02_btn.setStyleSheet(u"background-color:Transparent;\n"
"border-color:Transparent")
        icon23 = QIcon()
        icon23.addFile(u"images/camside.png", QSize(), QIcon.Normal, QIcon.Off)
        self.camera02_btn.setIcon(icon23)
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
        font5 = QFont()
        font5.setBold(True)
        self.label_53.setFont(font5)

        self.horizontalLayout_11.addWidget(self.label_53)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.cameraname_label = QLabel(self.frame_9)
        self.cameraname_label.setObjectName(u"cameraname_label")
        self.cameraname_label.setMinimumSize(QSize(120, 0))
        self.cameraname_label.setMaximumSize(QSize(100, 16777215))
        self.cameraname_label.setFont(font5)
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

        self.ultra_setting_btn = QPushButton(self.frame_6)
        self.ultra_setting_btn.setObjectName(u"ultra_setting_btn")
        self.ultra_setting_btn.setMinimumSize(QSize(105, 29))
        self.ultra_setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ultra_setting_btn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_24.addWidget(self.ultra_setting_btn, 0, Qt.AlignHCenter)

        self.frame_228 = QFrame(self.frame_6)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setEnabled(True)
        self.frame_228.setMinimumSize(QSize(250, 0))
        self.frame_228.setMaximumSize(QSize(250, 0))
        self.frame_228.setFrameShape(QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_228)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gain_label_2 = QLabel(self.frame_228)
        self.gain_label_2.setObjectName(u"gain_label_2")
        self.gain_label_2.setMinimumSize(QSize(120, 30))
        self.gain_label_2.setMaximumSize(QSize(120, 30))
        self.gain_label_2.setFont(font1)

        self.verticalLayout_19.addWidget(self.gain_label_2)

        self.gain_label = QLabel(self.frame_228)
        self.gain_label.setObjectName(u"gain_label")
        self.gain_label.setMinimumSize(QSize(120, 30))
        self.gain_label.setMaximumSize(QSize(120, 30))
        self.gain_label.setFont(font1)

        self.verticalLayout_19.addWidget(self.gain_label)

        self.expo_label = QLabel(self.frame_228)
        self.expo_label.setObjectName(u"expo_label")
        self.expo_label.setMinimumSize(QSize(120, 30))
        self.expo_label.setMaximumSize(QSize(120, 30))
        self.expo_label.setFont(font1)

        self.verticalLayout_19.addWidget(self.expo_label)

        self.width_label = QLabel(self.frame_228)
        self.width_label.setObjectName(u"width_label")
        self.width_label.setMinimumSize(QSize(120, 30))
        self.width_label.setMaximumSize(QSize(120, 30))
        self.width_label.setFont(font1)

        self.verticalLayout_19.addWidget(self.width_label)

        self.height_label = QLabel(self.frame_228)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setMinimumSize(QSize(120, 30))
        self.height_label.setMaximumSize(QSize(120, 30))
        self.height_label.setFont(font1)

        self.verticalLayout_19.addWidget(self.height_label)

        self.offsetx_label = QLabel(self.frame_228)
        self.offsetx_label.setObjectName(u"offsetx_label")
        self.offsetx_label.setMinimumSize(QSize(120, 30))
        self.offsetx_label.setMaximumSize(QSize(120, 30))
        self.offsetx_label.setFont(font1)

        self.verticalLayout_19.addWidget(self.offsetx_label)

        self.offsety_label = QLabel(self.frame_228)
        self.offsety_label.setObjectName(u"offsety_label")
        self.offsety_label.setMinimumSize(QSize(120, 30))
        self.offsety_label.setMaximumSize(QSize(120, 30))
        self.offsety_label.setFont(font1)

        self.verticalLayout_19.addWidget(self.offsety_label)

        self.trigger_label = QLabel(self.frame_228)
        self.trigger_label.setObjectName(u"trigger_label")
        self.trigger_label.setMinimumSize(QSize(120, 30))
        self.trigger_label.setMaximumSize(QSize(120, 30))
        self.trigger_label.setFont(font1)

        self.verticalLayout_19.addWidget(self.trigger_label)

        self.maxbuffer_label = QLabel(self.frame_228)
        self.maxbuffer_label.setObjectName(u"maxbuffer_label")
        self.maxbuffer_label.setMinimumSize(QSize(120, 30))
        self.maxbuffer_label.setMaximumSize(QSize(120, 30))
        self.maxbuffer_label.setFont(font1)

        self.verticalLayout_19.addWidget(self.maxbuffer_label)

        self.packetdelay_label = QLabel(self.frame_228)
        self.packetdelay_label.setObjectName(u"packetdelay_label")
        self.packetdelay_label.setMinimumSize(QSize(120, 30))
        self.packetdelay_label.setMaximumSize(QSize(120, 30))
        self.packetdelay_label.setFont(font1)

        self.verticalLayout_19.addWidget(self.packetdelay_label)

        self.packetsize_label = QLabel(self.frame_228)
        self.packetsize_label.setObjectName(u"packetsize_label")
        self.packetsize_label.setMinimumSize(QSize(120, 30))
        self.packetsize_label.setMaximumSize(QSize(120, 30))
        self.packetsize_label.setFont(font1)

        self.verticalLayout_19.addWidget(self.packetsize_label)

        self.transmissiondelay_label = QLabel(self.frame_228)
        self.transmissiondelay_label.setObjectName(u"transmissiondelay_label")
        self.transmissiondelay_label.setMinimumSize(QSize(120, 30))
        self.transmissiondelay_label.setMaximumSize(QSize(120, 30))
        self.transmissiondelay_label.setFont(font1)

        self.verticalLayout_19.addWidget(self.transmissiondelay_label)

        self.transmissiondelay_label_2 = QLabel(self.frame_228)
        self.transmissiondelay_label_2.setObjectName(u"transmissiondelay_label_2")
        self.transmissiondelay_label_2.setMinimumSize(QSize(120, 30))
        self.transmissiondelay_label_2.setMaximumSize(QSize(120, 30))
        self.transmissiondelay_label_2.setFont(font1)

        self.verticalLayout_19.addWidget(self.transmissiondelay_label_2)


        self.horizontalLayout_10.addLayout(self.verticalLayout_19)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.serial_number_combo = QComboBox(self.frame_228)
        self.serial_number_combo.setObjectName(u"serial_number_combo")
        self.serial_number_combo.setEnabled(True)
        self.serial_number_combo.setMinimumSize(QSize(100, 30))
        self.serial_number_combo.setMaximumSize(QSize(100, 30))
        self.serial_number_combo.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_21.addWidget(self.serial_number_combo)

        self.gain_spinbox = QSpinBox(self.frame_228)
        self.gain_spinbox.setObjectName(u"gain_spinbox")
        self.gain_spinbox.setEnabled(True)
        self.gain_spinbox.setMinimumSize(QSize(100, 30))
        self.gain_spinbox.setMaximumSize(QSize(100, 30))
        self.gain_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.gain_spinbox.setAlignment(Qt.AlignCenter)
        self.gain_spinbox.setMinimum(200)
        self.gain_spinbox.setMaximum(1000)
        self.gain_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.gain_spinbox)

        self.expo_spinbox = QSpinBox(self.frame_228)
        self.expo_spinbox.setObjectName(u"expo_spinbox")
        self.expo_spinbox.setEnabled(True)
        self.expo_spinbox.setMinimumSize(QSize(100, 30))
        self.expo_spinbox.setMaximumSize(QSize(100, 30))
        self.expo_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.expo_spinbox.setAlignment(Qt.AlignCenter)
        self.expo_spinbox.setMinimum(100)
        self.expo_spinbox.setMaximum(10000000)
        self.expo_spinbox.setSingleStep(1)
        self.expo_spinbox.setValue(3000)

        self.verticalLayout_21.addWidget(self.expo_spinbox)

        self.width_spinbox = QSpinBox(self.frame_228)
        self.width_spinbox.setObjectName(u"width_spinbox")
        self.width_spinbox.setEnabled(True)
        self.width_spinbox.setMinimumSize(QSize(100, 30))
        self.width_spinbox.setMaximumSize(QSize(100, 30))
        self.width_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.width_spinbox.setAlignment(Qt.AlignCenter)
        self.width_spinbox.setMinimum(500)
        self.width_spinbox.setMaximum(1920)
        self.width_spinbox.setSingleStep(1)
        self.width_spinbox.setValue(1920)

        self.verticalLayout_21.addWidget(self.width_spinbox)

        self.height_spinbox = QSpinBox(self.frame_228)
        self.height_spinbox.setObjectName(u"height_spinbox")
        self.height_spinbox.setEnabled(True)
        self.height_spinbox.setMinimumSize(QSize(100, 30))
        self.height_spinbox.setMaximumSize(QSize(100, 30))
        self.height_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.height_spinbox.setAlignment(Qt.AlignCenter)
        self.height_spinbox.setMinimum(500)
        self.height_spinbox.setMaximum(1200)
        self.height_spinbox.setSingleStep(1)
        self.height_spinbox.setValue(1200)

        self.verticalLayout_21.addWidget(self.height_spinbox)

        self.offsetx_spinbox = QSpinBox(self.frame_228)
        self.offsetx_spinbox.setObjectName(u"offsetx_spinbox")
        self.offsetx_spinbox.setEnabled(True)
        self.offsetx_spinbox.setMinimumSize(QSize(100, 30))
        self.offsetx_spinbox.setMaximumSize(QSize(100, 30))
        self.offsetx_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.offsetx_spinbox.setAlignment(Qt.AlignCenter)
        self.offsetx_spinbox.setMaximum(16)
        self.offsetx_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.offsetx_spinbox)

        self.offsety_spinbox = QSpinBox(self.frame_228)
        self.offsety_spinbox.setObjectName(u"offsety_spinbox")
        self.offsety_spinbox.setEnabled(True)
        self.offsety_spinbox.setMinimumSize(QSize(100, 30))
        self.offsety_spinbox.setMaximumSize(QSize(100, 30))
        self.offsety_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.offsety_spinbox.setAlignment(Qt.AlignCenter)
        self.offsety_spinbox.setMaximum(16)
        self.offsety_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.offsety_spinbox)

        self.trigger_combo = QComboBox(self.frame_228)
        self.trigger_combo.addItem("")
        self.trigger_combo.addItem("")
        self.trigger_combo.setObjectName(u"trigger_combo")
        self.trigger_combo.setEnabled(True)
        self.trigger_combo.setMinimumSize(QSize(100, 30))
        self.trigger_combo.setMaximumSize(QSize(100, 30))
        self.trigger_combo.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_21.addWidget(self.trigger_combo)

        self.maxbuffer_spinbox = QSpinBox(self.frame_228)
        self.maxbuffer_spinbox.setObjectName(u"maxbuffer_spinbox")
        self.maxbuffer_spinbox.setEnabled(True)
        self.maxbuffer_spinbox.setMinimumSize(QSize(100, 30))
        self.maxbuffer_spinbox.setMaximumSize(QSize(100, 30))
        self.maxbuffer_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.maxbuffer_spinbox.setAlignment(Qt.AlignCenter)
        self.maxbuffer_spinbox.setMaximum(360)
        self.maxbuffer_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.maxbuffer_spinbox)

        self.packetdelay_spinbox = QSpinBox(self.frame_228)
        self.packetdelay_spinbox.setObjectName(u"packetdelay_spinbox")
        self.packetdelay_spinbox.setEnabled(True)
        self.packetdelay_spinbox.setMinimumSize(QSize(100, 30))
        self.packetdelay_spinbox.setMaximumSize(QSize(100, 30))
        self.packetdelay_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.packetdelay_spinbox.setAlignment(Qt.AlignCenter)
        self.packetdelay_spinbox.setMaximum(360)
        self.packetdelay_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.packetdelay_spinbox)

        self.packetsize_spinbox = QSpinBox(self.frame_228)
        self.packetsize_spinbox.setObjectName(u"packetsize_spinbox")
        self.packetsize_spinbox.setEnabled(True)
        self.packetsize_spinbox.setMinimumSize(QSize(100, 30))
        self.packetsize_spinbox.setMaximumSize(QSize(100, 30))
        self.packetsize_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.packetsize_spinbox.setAlignment(Qt.AlignCenter)
        self.packetsize_spinbox.setMaximum(360)
        self.packetsize_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.packetsize_spinbox)

        self.transmissiondelay_spinbox = QSpinBox(self.frame_228)
        self.transmissiondelay_spinbox.setObjectName(u"transmissiondelay_spinbox")
        self.transmissiondelay_spinbox.setEnabled(True)
        self.transmissiondelay_spinbox.setMinimumSize(QSize(100, 30))
        self.transmissiondelay_spinbox.setMaximumSize(QSize(100, 30))
        self.transmissiondelay_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.transmissiondelay_spinbox.setAlignment(Qt.AlignCenter)
        self.transmissiondelay_spinbox.setMaximum(360)
        self.transmissiondelay_spinbox.setSingleStep(1)

        self.verticalLayout_21.addWidget(self.transmissiondelay_spinbox)

        self.ip_lineedit = QLineEdit(self.frame_228)
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


        self.verticalLayout_24.addWidget(self.frame_228)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 179))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_11)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frame_160 = QFrame(self.frame_11)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.camera_setting_apply_btn = QPushButton(self.frame_160)
        self.camera_setting_apply_btn.setObjectName(u"camera_setting_apply_btn")
        self.camera_setting_apply_btn.setEnabled(True)
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

        self.horizontalLayout_12.addWidget(self.camera_setting_apply_btn)

        self.camera_setting_reset_btn = QPushButton(self.frame_160)
        self.camera_setting_reset_btn.setObjectName(u"camera_setting_reset_btn")
        self.camera_setting_reset_btn.setMinimumSize(QSize(0, 30))
        self.camera_setting_reset_btn.setMaximumSize(QSize(16777215, 30))
        self.camera_setting_reset_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 120, 0);\n"
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

        self.horizontalLayout_12.addWidget(self.camera_setting_reset_btn)

        self.camera_setting_connect_btn = QPushButton(self.frame_160)
        self.camera_setting_connect_btn.setObjectName(u"camera_setting_connect_btn")
        self.camera_setting_connect_btn.setEnabled(True)
        self.camera_setting_connect_btn.setMinimumSize(QSize(0, 0))
        self.camera_setting_connect_btn.setMaximumSize(QSize(0, 0))
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


        self.verticalLayout_70.addWidget(self.frame_160)

        self.frame_148 = QFrame(self.frame_11)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_148)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.play_camera_setting_btn = QPushButton(self.frame_148)
        self.play_camera_setting_btn.setObjectName(u"play_camera_setting_btn")
        self.play_camera_setting_btn.setEnabled(True)
        self.play_camera_setting_btn.setMaximumSize(QSize(50, 16777215))
        self.play_camera_setting_btn.setStyleSheet(u"\n"
"background-color: rgb(0, 170, 0);")
        icon24 = QIcon()
        icon24.addFile(u"images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_camera_setting_btn.setIcon(icon24)

        self.horizontalLayout_23.addWidget(self.play_camera_setting_btn)

        self.pause_camera_setting_btn = QPushButton(self.frame_148)
        self.pause_camera_setting_btn.setObjectName(u"pause_camera_setting_btn")
        self.pause_camera_setting_btn.setEnabled(True)
        self.pause_camera_setting_btn.setMaximumSize(QSize(50, 16777215))
        self.pause_camera_setting_btn.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        icon25 = QIcon()
        icon25.addFile(u"images/icons/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_camera_setting_btn.setIcon(icon25)

        self.horizontalLayout_23.addWidget(self.pause_camera_setting_btn)


        self.verticalLayout_70.addWidget(self.frame_148)

        self.line_31 = QFrame(self.frame_11)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.HLine)
        self.line_31.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_70.addWidget(self.line_31)

        self.frame_99 = QFrame(self.frame_11)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(0, 75))
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.frame_99)
        self.verticalLayout_118.setSpacing(5)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.frame_189 = QFrame(self.frame_99)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setMinimumSize(QSize(0, 44))
        self.frame_189.setStyleSheet(u"\n"
"background-color: rgb(153, 193, 241);")
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_189)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.label_178 = QLabel(self.frame_189)
        self.label_178.setObjectName(u"label_178")

        self.verticalLayout_139.addWidget(self.label_178, 0, Qt.AlignHCenter)

        self.line_path_top_cam_live_page_2 = QLineEdit(self.frame_189)
        self.line_path_top_cam_live_page_2.setObjectName(u"line_path_top_cam_live_page_2")
        self.line_path_top_cam_live_page_2.setReadOnly(False)

        self.verticalLayout_139.addWidget(self.line_path_top_cam_live_page_2)


        self.verticalLayout_118.addWidget(self.frame_189)


        self.verticalLayout_70.addWidget(self.frame_99)


        self.verticalLayout_24.addWidget(self.frame_11)

        self.camera_setting_message_label = QLabel(self.frame_6)
        self.camera_setting_message_label.setObjectName(u"camera_setting_message_label")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.camera_setting_message_label.setFont(font6)
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
        self.horizontalLayout_53 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.frame_209 = QFrame(self.frame_8)
        self.frame_209.setObjectName(u"frame_209")
        self.frame_209.setFrameShape(QFrame.StyledPanel)
        self.frame_209.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_209)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.label_10 = QLabel(self.frame_209)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_110.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.camera_setting_picture_top = QLabel(self.frame_209)
        self.camera_setting_picture_top.setObjectName(u"camera_setting_picture_top")
        self.camera_setting_picture_top.setMinimumSize(QSize(0, 0))
        self.camera_setting_picture_top.setFrameShape(QFrame.Box)
        self.camera_setting_picture_top.setFrameShadow(QFrame.Sunken)
        self.camera_setting_picture_top.setLineWidth(2)
        self.camera_setting_picture_top.setPixmap(QPixmap(u"../../../../../home/milad/.designer/backup/images/camera.png"))
        self.camera_setting_picture_top.setScaledContents(True)
        self.camera_setting_picture_top.setWordWrap(True)
        self.camera_setting_picture_top.setMargin(13)
        self.camera_setting_picture_top.setIndent(-1)

        self.verticalLayout_110.addWidget(self.camera_setting_picture_top)

        self.camera_setting_get_top_camera = QPushButton(self.frame_209)
        self.camera_setting_get_top_camera.setObjectName(u"camera_setting_get_top_camera")
        self.camera_setting_get_top_camera.setEnabled(True)
        self.camera_setting_get_top_camera.setMinimumSize(QSize(88, 30))
        self.camera_setting_get_top_camera.setMaximumSize(QSize(16777215, 30))
        self.camera_setting_get_top_camera.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_setting_get_top_camera.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_110.addWidget(self.camera_setting_get_top_camera, 0, Qt.AlignHCenter)

        self.fullscreen_cam_top_btn = QPushButton(self.frame_209)
        self.fullscreen_cam_top_btn.setObjectName(u"fullscreen_cam_top_btn")
        self.fullscreen_cam_top_btn.setMaximumSize(QSize(50, 16777215))
        self.fullscreen_cam_top_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fullscreen_cam_top_btn.setStyleSheet(u"border:none;")
        icon26 = QIcon()
        icon26.addFile(u"images/full-screen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreen_cam_top_btn.setIcon(icon26)
        self.fullscreen_cam_top_btn.setIconSize(QSize(26, 26))

        self.verticalLayout_110.addWidget(self.fullscreen_cam_top_btn, 0, Qt.AlignHCenter)


        self.horizontalLayout_53.addWidget(self.frame_209)

        self.frame_210 = QFrame(self.frame_8)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setFrameShape(QFrame.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.frame_210)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.label_150 = QLabel(self.frame_210)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_131.addWidget(self.label_150, 0, Qt.AlignHCenter)

        self.camera_setting_picture_side = QLabel(self.frame_210)
        self.camera_setting_picture_side.setObjectName(u"camera_setting_picture_side")
        self.camera_setting_picture_side.setMinimumSize(QSize(0, 0))
        self.camera_setting_picture_side.setFrameShape(QFrame.Box)
        self.camera_setting_picture_side.setFrameShadow(QFrame.Sunken)
        self.camera_setting_picture_side.setLineWidth(2)
        self.camera_setting_picture_side.setPixmap(QPixmap(u"../../../../../home/milad/.designer/backup/images/camera.png"))
        self.camera_setting_picture_side.setScaledContents(True)
        self.camera_setting_picture_side.setMargin(13)
        self.camera_setting_picture_side.setIndent(-1)

        self.verticalLayout_131.addWidget(self.camera_setting_picture_side)

        self.camera_setting_get_side_camera = QPushButton(self.frame_210)
        self.camera_setting_get_side_camera.setObjectName(u"camera_setting_get_side_camera")
        self.camera_setting_get_side_camera.setEnabled(True)
        self.camera_setting_get_side_camera.setMinimumSize(QSize(88, 30))
        self.camera_setting_get_side_camera.setMaximumSize(QSize(16777215, 30))
        self.camera_setting_get_side_camera.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_setting_get_side_camera.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_131.addWidget(self.camera_setting_get_side_camera, 0, Qt.AlignHCenter)

        self.fullscreen_cam_side_btn = QPushButton(self.frame_210)
        self.fullscreen_cam_side_btn.setObjectName(u"fullscreen_cam_side_btn")
        self.fullscreen_cam_side_btn.setMaximumSize(QSize(50, 16777215))
        self.fullscreen_cam_side_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fullscreen_cam_side_btn.setStyleSheet(u"border:none;")
        self.fullscreen_cam_side_btn.setIcon(icon26)
        self.fullscreen_cam_side_btn.setIconSize(QSize(26, 26))

        self.verticalLayout_131.addWidget(self.fullscreen_cam_side_btn, 0, Qt.AlignHCenter)


        self.horizontalLayout_53.addWidget(self.frame_210)


        self.verticalLayout_18.addWidget(self.frame_8)

        self.camera_setting_tools_page = QPushButton(self.frame_7)
        self.camera_setting_tools_page.setObjectName(u"camera_setting_tools_page")
        self.camera_setting_tools_page.setEnabled(True)
        self.camera_setting_tools_page.setMinimumSize(QSize(88, 30))
        self.camera_setting_tools_page.setMaximumSize(QSize(16777215, 30))
        self.camera_setting_tools_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_setting_tools_page.setStyleSheet(u"QPushButton{\n"
"background: rgb(120,120,120);\n"
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

        self.verticalLayout_18.addWidget(self.camera_setting_tools_page, 0, Qt.AlignHCenter)


        self.horizontalLayout_9.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_camera_setting)
        self.page_calibration = QWidget()
        self.page_calibration.setObjectName(u"page_calibration")
        self.verticalLayout_90 = QVBoxLayout(self.page_calibration)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.frame_70 = QFrame(self.page_calibration)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.frame_181 = QFrame(self.frame_70)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setFrameShape(QFrame.WinPanel)
        self.frame_181.setFrameShadow(QFrame.Raised)
        self.frame_181.setLineWidth(0)
        self.verticalLayout_52 = QVBoxLayout(self.frame_181)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.frame_161 = QFrame(self.frame_181)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMinimumSize(QSize(300, 0))
        self.frame_161.setMaximumSize(QSize(16777215, 50))
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_161)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.label_172 = QLabel(self.frame_161)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_102.addWidget(self.label_172)

        self.btn_connect_top_cal_page = QPushButton(self.frame_161)
        self.btn_connect_top_cal_page.setObjectName(u"btn_connect_top_cal_page")
        self.btn_connect_top_cal_page.setMinimumSize(QSize(50, 32))
        self.btn_connect_top_cal_page.setMaximumSize(QSize(50, 32))
        self.btn_connect_top_cal_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_connect_top_cal_page.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(200,200,200);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}")
        self.btn_connect_top_cal_page.setIcon(icon14)
        self.btn_connect_top_cal_page.setIconSize(QSize(41, 26))

        self.horizontalLayout_102.addWidget(self.btn_connect_top_cal_page)

        self.btn_disconnect_top_cal_page = QPushButton(self.frame_161)
        self.btn_disconnect_top_cal_page.setObjectName(u"btn_disconnect_top_cal_page")
        self.btn_disconnect_top_cal_page.setMinimumSize(QSize(50, 32))
        self.btn_disconnect_top_cal_page.setMaximumSize(QSize(50, 32))
        self.btn_disconnect_top_cal_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_disconnect_top_cal_page.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(200,200,200);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}")
        self.btn_disconnect_top_cal_page.setIcon(icon15)
        self.btn_disconnect_top_cal_page.setIconSize(QSize(41, 26))

        self.horizontalLayout_102.addWidget(self.btn_disconnect_top_cal_page)

        self.line_28 = QFrame(self.frame_161)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.VLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_102.addWidget(self.line_28)

        self.label_163 = QLabel(self.frame_161)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setMinimumSize(QSize(60, 0))
        self.label_163.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_102.addWidget(self.label_163)

        self.connection_status_top_cal_page = QLabel(self.frame_161)
        self.connection_status_top_cal_page.setObjectName(u"connection_status_top_cal_page")
        self.connection_status_top_cal_page.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_102.addWidget(self.connection_status_top_cal_page)


        self.verticalLayout_52.addWidget(self.frame_161, 0, Qt.AlignHCenter)

        self.line_22 = QFrame(self.frame_181)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_22)

        self.frame_159 = QFrame(self.frame_181)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setFrameShape(QFrame.Box)
        self.frame_159.setFrameShadow(QFrame.Plain)
        self.frame_159.setLineWidth(1)
        self.verticalLayout_104 = QVBoxLayout(self.frame_159)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.camera_top_cal_page = QLabel(self.frame_159)
        self.camera_top_cal_page.setObjectName(u"camera_top_cal_page")
        self.camera_top_cal_page.setPixmap(QPixmap(u"../../../../../home/milad/.designer/backup/images/settings.png"))
        self.camera_top_cal_page.setScaledContents(True)

        self.verticalLayout_104.addWidget(self.camera_top_cal_page)


        self.verticalLayout_52.addWidget(self.frame_159)

        self.line_24 = QFrame(self.frame_181)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_52.addWidget(self.line_24)

        self.frame_155 = QFrame(self.frame_181)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setMaximumSize(QSize(16777215, 85))
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_155)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.frame_187 = QFrame(self.frame_155)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setEnabled(True)
        self.frame_187.setMinimumSize(QSize(0, 66))
        self.frame_187.setMaximumSize(QSize(16777215, 67))
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_187)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.label_174 = QLabel(self.frame_187)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_117.addWidget(self.label_174, 0, Qt.AlignHCenter)

        self.frame_188 = QFrame(self.frame_187)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setMinimumSize(QSize(0, 43))
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_180 = QHBoxLayout(self.frame_188)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(0, 0, -1, 0)
        self.checkbox_thresh_inv0_top_cal_page = QCheckBox(self.frame_188)
        self.checkbox_thresh_inv0_top_cal_page.setObjectName(u"checkbox_thresh_inv0_top_cal_page")
        self.checkbox_thresh_inv0_top_cal_page.setMinimumSize(QSize(100, 0))
        self.checkbox_thresh_inv0_top_cal_page.setMaximumSize(QSize(100, 16777215))
        self.checkbox_thresh_inv0_top_cal_page.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_180.addWidget(self.checkbox_thresh_inv0_top_cal_page)

        self.bar_thresh0_top_cal_page = QSlider(self.frame_188)
        self.bar_thresh0_top_cal_page.setObjectName(u"bar_thresh0_top_cal_page")
        self.bar_thresh0_top_cal_page.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_top_cal_page.setMaximum(255)
        self.bar_thresh0_top_cal_page.setOrientation(Qt.Horizontal)

        self.horizontalLayout_180.addWidget(self.bar_thresh0_top_cal_page)

        self.spinBox_16 = QSpinBox(self.frame_188)
        self.spinBox_16.setObjectName(u"spinBox_16")
        self.spinBox_16.setEnabled(True)
        self.spinBox_16.setMaximum(255)

        self.horizontalLayout_180.addWidget(self.spinBox_16)


        self.verticalLayout_117.addWidget(self.frame_188)


        self.horizontalLayout_101.addWidget(self.frame_187)

        self.frame_158 = QFrame(self.frame_155)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setEnabled(True)
        self.frame_158.setMaximumSize(QSize(16777215, 72))
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_158)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.label_173 = QLabel(self.frame_158)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setEnabled(True)
        self.label_173.setAlignment(Qt.AlignCenter)

        self.verticalLayout_105.addWidget(self.label_173)

        self.frame_186 = QFrame(self.frame_158)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setMinimumSize(QSize(0, 29))
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_179 = QHBoxLayout(self.frame_186)
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.horizontalLayout_179.setContentsMargins(0, 0, 0, 0)
        self.bar_noise_filter0_top_cal_page = QSlider(self.frame_186)
        self.bar_noise_filter0_top_cal_page.setObjectName(u"bar_noise_filter0_top_cal_page")
        self.bar_noise_filter0_top_cal_page.setMinimumSize(QSize(0, 30))
        self.bar_noise_filter0_top_cal_page.setMaximum(100)
        self.bar_noise_filter0_top_cal_page.setOrientation(Qt.Horizontal)

        self.horizontalLayout_179.addWidget(self.bar_noise_filter0_top_cal_page)

        self.spinBox_15 = QSpinBox(self.frame_186)
        self.spinBox_15.setObjectName(u"spinBox_15")
        self.spinBox_15.setMaximum(100)

        self.horizontalLayout_179.addWidget(self.spinBox_15)


        self.verticalLayout_105.addWidget(self.frame_186)


        self.horizontalLayout_101.addWidget(self.frame_158)


        self.verticalLayout_52.addWidget(self.frame_155)

        self.frame_196 = QFrame(self.frame_181)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setMaximumSize(QSize(16777215, 50))
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.frame_196)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.label_180 = QLabel(self.frame_196)
        self.label_180.setObjectName(u"label_180")

        self.horizontalLayout_104.addWidget(self.label_180)

        self.lineEdit_2 = QLineEdit(self.frame_196)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_104.addWidget(self.lineEdit_2)

        self.btn_calibration_top_cal_page = QPushButton(self.frame_196)
        self.btn_calibration_top_cal_page.setObjectName(u"btn_calibration_top_cal_page")
        self.btn_calibration_top_cal_page.setMinimumSize(QSize(90, 26))
        self.btn_calibration_top_cal_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calibration_top_cal_page.setStyleSheet(u"#pagesContainer QPushButton {\n"
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
"")

        self.horizontalLayout_104.addWidget(self.btn_calibration_top_cal_page)

        self.line_23 = QFrame(self.frame_196)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.VLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_104.addWidget(self.line_23)

        self.label_181 = QLabel(self.frame_196)
        self.label_181.setObjectName(u"label_181")

        self.horizontalLayout_104.addWidget(self.label_181)

        self.label_top_calibration = QLabel(self.frame_196)
        self.label_top_calibration.setObjectName(u"label_top_calibration")
        self.label_top_calibration.setMinimumSize(QSize(21, 0))

        self.horizontalLayout_104.addWidget(self.label_top_calibration)

        self.btn_save_value_top_cal_page = QPushButton(self.frame_196)
        self.btn_save_value_top_cal_page.setObjectName(u"btn_save_value_top_cal_page")
        self.btn_save_value_top_cal_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_value_top_cal_page.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        icon27 = QIcon()
        icon27.addFile(u"../../../../../home/milad/.designer/backup/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_value_top_cal_page.setIcon(icon27)

        self.horizontalLayout_104.addWidget(self.btn_save_value_top_cal_page)


        self.verticalLayout_52.addWidget(self.frame_196)


        self.horizontalLayout_98.addWidget(self.frame_181)

        self.line_30 = QFrame(self.frame_70)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShadow(QFrame.Plain)
        self.line_30.setLineWidth(2)
        self.line_30.setFrameShape(QFrame.VLine)

        self.horizontalLayout_98.addWidget(self.line_30)

        self.frame_198 = QFrame(self.frame_70)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setFrameShape(QFrame.WinPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.frame_198)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.frame_199 = QFrame(self.frame_198)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setMinimumSize(QSize(300, 0))
        self.frame_199.setMaximumSize(QSize(16777215, 50))
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_199)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.label_186 = QLabel(self.frame_199)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_106.addWidget(self.label_186)

        self.btn_connect_side_cal_page = QPushButton(self.frame_199)
        self.btn_connect_side_cal_page.setObjectName(u"btn_connect_side_cal_page")
        self.btn_connect_side_cal_page.setMinimumSize(QSize(50, 32))
        self.btn_connect_side_cal_page.setMaximumSize(QSize(50, 32))
        self.btn_connect_side_cal_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_connect_side_cal_page.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(200,200,200);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}")
        self.btn_connect_side_cal_page.setIcon(icon14)
        self.btn_connect_side_cal_page.setIconSize(QSize(41, 26))

        self.horizontalLayout_106.addWidget(self.btn_connect_side_cal_page)

        self.btn_disconnect_side_cal_page = QPushButton(self.frame_199)
        self.btn_disconnect_side_cal_page.setObjectName(u"btn_disconnect_side_cal_page")
        self.btn_disconnect_side_cal_page.setMinimumSize(QSize(50, 32))
        self.btn_disconnect_side_cal_page.setMaximumSize(QSize(50, 32))
        self.btn_disconnect_side_cal_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_disconnect_side_cal_page.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(200,200,200);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}")
        self.btn_disconnect_side_cal_page.setIcon(icon15)
        self.btn_disconnect_side_cal_page.setIconSize(QSize(41, 26))

        self.horizontalLayout_106.addWidget(self.btn_disconnect_side_cal_page)

        self.line_29 = QFrame(self.frame_199)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.VLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_106.addWidget(self.line_29)

        self.label_177 = QLabel(self.frame_199)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setMinimumSize(QSize(60, 0))
        self.label_177.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_106.addWidget(self.label_177)

        self.connection_status_side_cal_page = QLabel(self.frame_199)
        self.connection_status_side_cal_page.setObjectName(u"connection_status_side_cal_page")
        self.connection_status_side_cal_page.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_106.addWidget(self.connection_status_side_cal_page)


        self.verticalLayout_122.addWidget(self.frame_199, 0, Qt.AlignHCenter)

        self.line_25 = QFrame(self.frame_198)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_122.addWidget(self.line_25)

        self.frame_200 = QFrame(self.frame_198)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setFrameShape(QFrame.Box)
        self.frame_200.setFrameShadow(QFrame.Plain)
        self.verticalLayout_123 = QVBoxLayout(self.frame_200)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.camera_side_cal_page = QLabel(self.frame_200)
        self.camera_side_cal_page.setObjectName(u"camera_side_cal_page")
        self.camera_side_cal_page.setPixmap(QPixmap(u"../../../../../home/milad/.designer/backup/images/settings.png"))
        self.camera_side_cal_page.setScaledContents(True)

        self.verticalLayout_123.addWidget(self.camera_side_cal_page)


        self.verticalLayout_122.addWidget(self.frame_200)

        self.line_26 = QFrame(self.frame_198)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_122.addWidget(self.line_26)

        self.frame_201 = QFrame(self.frame_198)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setMaximumSize(QSize(16777215, 85))
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_201)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.frame_202 = QFrame(self.frame_201)
        self.frame_202.setObjectName(u"frame_202")
        self.frame_202.setEnabled(True)
        self.frame_202.setMinimumSize(QSize(0, 66))
        self.frame_202.setMaximumSize(QSize(16777215, 67))
        self.frame_202.setFrameShape(QFrame.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.frame_202)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.label_189 = QLabel(self.frame_202)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_125.addWidget(self.label_189, 0, Qt.AlignHCenter)

        self.frame_203 = QFrame(self.frame_202)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setMinimumSize(QSize(0, 43))
        self.frame_203.setFrameShape(QFrame.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_183 = QHBoxLayout(self.frame_203)
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.horizontalLayout_183.setContentsMargins(0, 0, -1, 0)
        self.checkbox_thresh_inv0_side_cal_page = QCheckBox(self.frame_203)
        self.checkbox_thresh_inv0_side_cal_page.setObjectName(u"checkbox_thresh_inv0_side_cal_page")
        self.checkbox_thresh_inv0_side_cal_page.setMinimumSize(QSize(100, 0))
        self.checkbox_thresh_inv0_side_cal_page.setMaximumSize(QSize(100, 16777215))
        self.checkbox_thresh_inv0_side_cal_page.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_183.addWidget(self.checkbox_thresh_inv0_side_cal_page)

        self.bar_thresh0_side_cal_page = QSlider(self.frame_203)
        self.bar_thresh0_side_cal_page.setObjectName(u"bar_thresh0_side_cal_page")
        self.bar_thresh0_side_cal_page.setMinimumSize(QSize(0, 30))
        self.bar_thresh0_side_cal_page.setMaximum(255)
        self.bar_thresh0_side_cal_page.setOrientation(Qt.Horizontal)

        self.horizontalLayout_183.addWidget(self.bar_thresh0_side_cal_page)

        self.spinBox_19 = QSpinBox(self.frame_203)
        self.spinBox_19.setObjectName(u"spinBox_19")
        self.spinBox_19.setEnabled(True)
        self.spinBox_19.setMaximum(255)

        self.horizontalLayout_183.addWidget(self.spinBox_19)


        self.verticalLayout_125.addWidget(self.frame_203)


        self.horizontalLayout_107.addWidget(self.frame_202)

        self.frame_204 = QFrame(self.frame_201)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setEnabled(True)
        self.frame_204.setMaximumSize(QSize(16777215, 72))
        self.frame_204.setFrameShape(QFrame.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.frame_204)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.label_190 = QLabel(self.frame_204)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setEnabled(True)
        self.label_190.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.label_190)

        self.frame_205 = QFrame(self.frame_204)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setMinimumSize(QSize(0, 29))
        self.frame_205.setFrameShape(QFrame.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_184 = QHBoxLayout(self.frame_205)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.horizontalLayout_184.setContentsMargins(0, 0, 0, 0)
        self.bar_noise_filter0_side_cal_page = QSlider(self.frame_205)
        self.bar_noise_filter0_side_cal_page.setObjectName(u"bar_noise_filter0_side_cal_page")
        self.bar_noise_filter0_side_cal_page.setMinimumSize(QSize(0, 30))
        self.bar_noise_filter0_side_cal_page.setMaximum(100)
        self.bar_noise_filter0_side_cal_page.setOrientation(Qt.Horizontal)

        self.horizontalLayout_184.addWidget(self.bar_noise_filter0_side_cal_page)

        self.spinBox_20 = QSpinBox(self.frame_205)
        self.spinBox_20.setObjectName(u"spinBox_20")
        self.spinBox_20.setMaximum(100)

        self.horizontalLayout_184.addWidget(self.spinBox_20)


        self.verticalLayout_126.addWidget(self.frame_205)


        self.horizontalLayout_107.addWidget(self.frame_204)


        self.verticalLayout_122.addWidget(self.frame_201)

        self.frame_206 = QFrame(self.frame_198)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setMaximumSize(QSize(16777215, 50))
        self.frame_206.setFrameShape(QFrame.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_185 = QHBoxLayout(self.frame_206)
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.label_191 = QLabel(self.frame_206)
        self.label_191.setObjectName(u"label_191")

        self.horizontalLayout_185.addWidget(self.label_191)

        self.lineEdit_4 = QLineEdit(self.frame_206)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_185.addWidget(self.lineEdit_4)

        self.btn_calibration_side_cal_page = QPushButton(self.frame_206)
        self.btn_calibration_side_cal_page.setObjectName(u"btn_calibration_side_cal_page")
        self.btn_calibration_side_cal_page.setMinimumSize(QSize(90, 26))
        self.btn_calibration_side_cal_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calibration_side_cal_page.setStyleSheet(u"#pagesContainer QPushButton {\n"
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
"")

        self.horizontalLayout_185.addWidget(self.btn_calibration_side_cal_page)

        self.line_27 = QFrame(self.frame_206)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.VLine)
        self.line_27.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_185.addWidget(self.line_27)

        self.label_192 = QLabel(self.frame_206)
        self.label_192.setObjectName(u"label_192")

        self.horizontalLayout_185.addWidget(self.label_192)

        self.label_side_calibration = QLabel(self.frame_206)
        self.label_side_calibration.setObjectName(u"label_side_calibration")
        self.label_side_calibration.setMinimumSize(QSize(21, 0))

        self.horizontalLayout_185.addWidget(self.label_side_calibration)

        self.btn_save_value_side_cal_page = QPushButton(self.frame_206)
        self.btn_save_value_side_cal_page.setObjectName(u"btn_save_value_side_cal_page")
        self.btn_save_value_side_cal_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_value_side_cal_page.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.btn_save_value_side_cal_page.setIcon(icon27)

        self.horizontalLayout_185.addWidget(self.btn_save_value_side_cal_page)


        self.verticalLayout_122.addWidget(self.frame_206)


        self.horizontalLayout_98.addWidget(self.frame_198)


        self.verticalLayout_90.addWidget(self.frame_70)

        self.stackedWidget.addWidget(self.page_calibration)
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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 276, 666))
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
        font7 = QFont()
        font7.setPointSize(8)
        font7.setBold(False)
        self.create_user.setFont(font7)
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
        self.frame_93.setMaximumSize(QSize(352, 16777215))
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_2288 = QFrame(self.frame_93)
        self.frame_2288.setObjectName(u"frame_2288")
        self.frame_2288.setMaximumSize(QSize(320, 16777215))
        self.frame_2288.setFrameShape(QFrame.StyledPanel)
        self.frame_2288.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_2288)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.groupBox_4 = QGroupBox(self.frame_2288)
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
        self.frame_91.setMinimumSize(QSize(0, 297))
        self.frame_91.setMaximumSize(QSize(500, 268))
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_91)
        self.verticalLayout_72.setSpacing(10)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.frame_91)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 42))
        self.horizontalLayout_26 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_26.setSpacing(3)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.line_main_path = QLineEdit(self.groupBox_2)
        self.line_main_path.setObjectName(u"line_main_path")
        self.line_main_path.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_26.addWidget(self.line_main_path)

        self.tool_btn_main_path = QToolButton(self.groupBox_2)
        self.tool_btn_main_path.setObjectName(u"tool_btn_main_path")

        self.horizontalLayout_26.addWidget(self.tool_btn_main_path)


        self.verticalLayout_72.addWidget(self.groupBox_2)

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
        font8 = QFont()
        font8.setPointSize(10)
        self.label_97.setFont(font8)

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
        self.label_98.setFont(font8)

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
        self.label_57.setFont(font8)

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
        self.label_95.setFont(font8)

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
        self.label_96.setFont(font8)

        self.horizontalLayout_65.addWidget(self.label_96)

        self.combo_change_language = QComboBox(self.frame_88)
        self.combo_change_language.setObjectName(u"combo_change_language")
        self.combo_change_language.setMinimumSize(QSize(150, 30))
        self.combo_change_language.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_65.addWidget(self.combo_change_language)


        self.verticalLayout_72.addWidget(self.frame_88)

        self.label_language = QLabel(self.frame_91)
        self.label_language.setObjectName(u"label_language")
        self.label_language.setMinimumSize(QSize(40, 35))
        self.label_language.setMaximumSize(QSize(40, 35))
        self.label_language.setScaledContents(True)

        self.verticalLayout_72.addWidget(self.label_language, 0, Qt.AlignHCenter)


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
        self.general_setting_appearance_message_label.setFont(font6)
        self.general_setting_appearance_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.general_setting_appearance_message_label)


        self.verticalLayout_75.addWidget(self.frame_97)


        self.verticalLayout_84.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame_2288)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(300, 319))
        self.verticalLayout_78 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_102 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.frame_95 = QFrame(self.groupBox_7)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_95)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_116 = QLabel(self.frame_95)
        self.label_116.setObjectName(u"label_116")

        self.horizontalLayout_76.addWidget(self.label_116)

        self.label_122 = QLabel(self.frame_95)
        self.label_122.setObjectName(u"label_122")

        self.horizontalLayout_76.addWidget(self.label_122)

        self.line_top_cam_x_resolution = QLineEdit(self.frame_95)
        self.line_top_cam_x_resolution.setObjectName(u"line_top_cam_x_resolution")

        self.horizontalLayout_76.addWidget(self.line_top_cam_x_resolution)

        self.label_123 = QLabel(self.frame_95)
        self.label_123.setObjectName(u"label_123")

        self.horizontalLayout_76.addWidget(self.label_123)

        self.line_top_cam_y_resolution = QLineEdit(self.frame_95)
        self.line_top_cam_y_resolution.setObjectName(u"line_top_cam_y_resolution")

        self.horizontalLayout_76.addWidget(self.line_top_cam_y_resolution)


        self.verticalLayout_103.addLayout(self.horizontalLayout_76)


        self.verticalLayout_102.addWidget(self.frame_95)


        self.verticalLayout_78.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_101 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.frame_94 = QFrame(self.groupBox_6)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_94)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_99 = QLabel(self.frame_94)
        self.label_99.setObjectName(u"label_99")

        self.horizontalLayout_75.addWidget(self.label_99)

        self.label_118 = QLabel(self.frame_94)
        self.label_118.setObjectName(u"label_118")

        self.horizontalLayout_75.addWidget(self.label_118)

        self.line_side_cam_x_resolution = QLineEdit(self.frame_94)
        self.line_side_cam_x_resolution.setObjectName(u"line_side_cam_x_resolution")

        self.horizontalLayout_75.addWidget(self.line_side_cam_x_resolution)

        self.label_119 = QLabel(self.frame_94)
        self.label_119.setObjectName(u"label_119")

        self.horizontalLayout_75.addWidget(self.label_119)

        self.line_side_cam_y_resolution = QLineEdit(self.frame_94)
        self.line_side_cam_y_resolution.setObjectName(u"line_side_cam_y_resolution")

        self.horizontalLayout_75.addWidget(self.line_side_cam_y_resolution)


        self.verticalLayout_74.addLayout(self.horizontalLayout_75)


        self.verticalLayout_101.addWidget(self.frame_94)


        self.verticalLayout_78.addWidget(self.groupBox_6)

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
        self.btn_set_szies = QPushButton(self.frame_98)
        self.btn_set_szies.setObjectName(u"btn_set_szies")
        self.btn_set_szies.setMinimumSize(QSize(0, 30))
        self.btn_set_szies.setMaximumSize(QSize(500, 25))
        self.btn_set_szies.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_set_szies.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_77.addWidget(self.btn_set_szies)

        self.setting_defect_message_label = QLabel(self.frame_98)
        self.setting_defect_message_label.setObjectName(u"setting_defect_message_label")
        self.setting_defect_message_label.setMinimumSize(QSize(0, 20))
        self.setting_defect_message_label.setMaximumSize(QSize(500, 20))
        self.setting_defect_message_label.setFont(font8)
        self.setting_defect_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_77.addWidget(self.setting_defect_message_label)


        self.verticalLayout_78.addWidget(self.frame_98)


        self.verticalLayout_84.addWidget(self.groupBox_5)


        self.horizontalLayout_93.addWidget(self.frame_2288)


        self.horizontalLayout_68.addWidget(self.frame_93)

        self.frame_96 = QFrame(self.frame_92)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_96)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.frame_174 = QFrame(self.frame_96)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setMaximumSize(QSize(16777215, 108))
        self.frame_174.setFrameShape(QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_174)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.label_154 = QLabel(self.frame_174)
        self.label_154.setObjectName(u"label_154")

        self.horizontalLayout_83.addWidget(self.label_154)

        self.plc_ip_line = QLineEdit(self.frame_174)
        self.plc_ip_line.setObjectName(u"plc_ip_line")
        self.plc_ip_line.setMinimumSize(QSize(0, 28))
        self.plc_ip_line.setMaximumSize(QSize(700, 16777215))

        self.horizontalLayout_83.addWidget(self.plc_ip_line)

        self.btn_save_ip_plc = QPushButton(self.frame_174)
        self.btn_save_ip_plc.setObjectName(u"btn_save_ip_plc")
        self.btn_save_ip_plc.setMaximumSize(QSize(50, 16777215))
        self.btn_save_ip_plc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_ip_plc.setStyleSheet(u"background-color: rgb(100,100,100);")
        self.btn_save_ip_plc.setIcon(icon13)

        self.horizontalLayout_83.addWidget(self.btn_save_ip_plc)


        self.verticalLayout_112.addLayout(self.horizontalLayout_83)

        self.frame_173 = QFrame(self.frame_174)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setFrameShape(QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_173)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.plc_warnings = QLabel(self.frame_173)
        self.plc_warnings.setObjectName(u"plc_warnings")

        self.horizontalLayout_84.addWidget(self.plc_warnings)

        self.connect_plc_btn = QPushButton(self.frame_173)
        self.connect_plc_btn.setObjectName(u"connect_plc_btn")
        self.connect_plc_btn.setMinimumSize(QSize(80, 30))
        self.connect_plc_btn.setMaximumSize(QSize(80, 30))
        self.connect_plc_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.connect_plc_btn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_84.addWidget(self.connect_plc_btn)

        self.options_plc_btn = QPushButton(self.frame_173)
        self.options_plc_btn.setObjectName(u"options_plc_btn")
        self.options_plc_btn.setEnabled(False)
        self.options_plc_btn.setMinimumSize(QSize(80, 30))
        self.options_plc_btn.setMaximumSize(QSize(80, 16777215))
        self.options_plc_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.options_plc_btn.setStyleSheet(u"QPushButton{\n"
"background: #000000;\n"
"border: Transparent;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #8D8D8D;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_84.addWidget(self.options_plc_btn)

        self.disconnect_plc_btn = QPushButton(self.frame_173)
        self.disconnect_plc_btn.setObjectName(u"disconnect_plc_btn")
        self.disconnect_plc_btn.setMinimumSize(QSize(80, 30))
        self.disconnect_plc_btn.setMaximumSize(QSize(80, 16777215))
        self.disconnect_plc_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.disconnect_plc_btn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_84.addWidget(self.disconnect_plc_btn)


        self.verticalLayout_112.addWidget(self.frame_173)


        self.verticalLayout_124.addWidget(self.frame_174)

        self.frame_175 = QFrame(self.frame_96)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setFrameShape(QFrame.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.frame_175)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.groupBox_13 = QGroupBox(self.frame_175)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_114 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.frame_176 = QFrame(self.groupBox_13)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setMinimumSize(QSize(61, 0))
        self.frame_176.setMaximumSize(QSize(16777215, 16777215))
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_176)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.frame_177 = QFrame(self.frame_176)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setMinimumSize(QSize(460, 55))
        self.frame_177.setMaximumSize(QSize(16777215, 55))
        self.frame_177.setFrameShape(QFrame.Box)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_177)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.label_155 = QLabel(self.frame_177)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_95.addWidget(self.label_155)

        self.line_run_plc = QLineEdit(self.frame_177)
        self.line_run_plc.setObjectName(u"line_run_plc")
        self.line_run_plc.setMaximumSize(QSize(300, 30))

        self.horizontalLayout_95.addWidget(self.line_run_plc)

        self.check_run_plc = QPushButton(self.frame_177)
        self.check_run_plc.setObjectName(u"check_run_plc")
        self.check_run_plc.setMinimumSize(QSize(43, 21))
        self.check_run_plc.setMaximumSize(QSize(80, 16777215))
        self.check_run_plc.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_run_plc.setStyleSheet(u"QPushButton{\n"
"background: green;\n"
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

        self.horizontalLayout_95.addWidget(self.check_run_plc)

        self.label_156 = QLabel(self.frame_177)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_95.addWidget(self.label_156)

        self.label_run_plc = QLabel(self.frame_177)
        self.label_run_plc.setObjectName(u"label_run_plc")

        self.horizontalLayout_95.addWidget(self.label_run_plc)


        self.verticalLayout_115.addWidget(self.frame_177)

        self.frame_178 = QFrame(self.frame_176)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setMinimumSize(QSize(0, 55))
        self.frame_178.setMaximumSize(QSize(16777215, 55))
        self.frame_178.setFrameShape(QFrame.Box)
        self.frame_178.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_178)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_157 = QLabel(self.frame_178)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_85.addWidget(self.label_157)

        self.line_stop_plc = QLineEdit(self.frame_178)
        self.line_stop_plc.setObjectName(u"line_stop_plc")
        self.line_stop_plc.setMaximumSize(QSize(300, 30))

        self.horizontalLayout_85.addWidget(self.line_stop_plc)

        self.check_stop_plc = QPushButton(self.frame_178)
        self.check_stop_plc.setObjectName(u"check_stop_plc")
        self.check_stop_plc.setMinimumSize(QSize(43, 21))
        self.check_stop_plc.setMaximumSize(QSize(80, 16777215))
        self.check_stop_plc.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_stop_plc.setStyleSheet(u"QPushButton{\n"
"background: green;\n"
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

        self.horizontalLayout_85.addWidget(self.check_stop_plc)

        self.label_158 = QLabel(self.frame_178)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setMaximumSize(QSize(49, 16777215))

        self.horizontalLayout_85.addWidget(self.label_158)

        self.label_stop_plc = QLabel(self.frame_178)
        self.label_stop_plc.setObjectName(u"label_stop_plc")

        self.horizontalLayout_85.addWidget(self.label_stop_plc)


        self.verticalLayout_115.addWidget(self.frame_178)

        self.frame_179 = QFrame(self.frame_176)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setMinimumSize(QSize(500, 55))
        self.frame_179.setMaximumSize(QSize(16777215, 55))
        self.frame_179.setFrameShape(QFrame.Box)
        self.frame_179.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_179)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.label_159 = QLabel(self.frame_179)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_96.addWidget(self.label_159)

        self.line_reject_plc = QLineEdit(self.frame_179)
        self.line_reject_plc.setObjectName(u"line_reject_plc")
        self.line_reject_plc.setMaximumSize(QSize(300, 30))

        self.horizontalLayout_96.addWidget(self.line_reject_plc)

        self.check_reject_plc = QPushButton(self.frame_179)
        self.check_reject_plc.setObjectName(u"check_reject_plc")
        self.check_reject_plc.setMinimumSize(QSize(43, 21))
        self.check_reject_plc.setMaximumSize(QSize(80, 16777215))
        self.check_reject_plc.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_reject_plc.setStyleSheet(u"QPushButton{\n"
"background: green;\n"
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

        self.horizontalLayout_96.addWidget(self.check_reject_plc)

        self.label_160 = QLabel(self.frame_179)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_96.addWidget(self.label_160)

        self.label_reject_plc = QLabel(self.frame_179)
        self.label_reject_plc.setObjectName(u"label_reject_plc")

        self.horizontalLayout_96.addWidget(self.label_reject_plc)


        self.verticalLayout_115.addWidget(self.frame_179)

        self.frame_191 = QFrame(self.frame_176)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setMinimumSize(QSize(500, 55))
        self.frame_191.setMaximumSize(QSize(16777215, 55))
        self.frame_191.setFrameShape(QFrame.Box)
        self.frame_191.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_191)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.label_175 = QLabel(self.frame_191)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setMaximumSize(QSize(136, 16777215))

        self.horizontalLayout_103.addWidget(self.label_175)

        self.spin_delay_plc = QSpinBox(self.frame_191)
        self.spin_delay_plc.setObjectName(u"spin_delay_plc")

        self.horizontalLayout_103.addWidget(self.spin_delay_plc)

        self.line_32 = QFrame(self.frame_191)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.VLine)
        self.line_32.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_103.addWidget(self.line_32)

        self.label_164 = QLabel(self.frame_191)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setMinimumSize(QSize(169, 0))
        self.label_164.setMaximumSize(QSize(151, 16777215))

        self.horizontalLayout_103.addWidget(self.label_164)

        self.spin_duration_plc = QSpinBox(self.frame_191)
        self.spin_duration_plc.setObjectName(u"spin_duration_plc")

        self.horizontalLayout_103.addWidget(self.spin_duration_plc)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_103.addItem(self.horizontalSpacer_11)


        self.verticalLayout_115.addWidget(self.frame_191)

        self.frame_182 = QFrame(self.frame_176)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setMinimumSize(QSize(500, 55))
        self.frame_182.setMaximumSize(QSize(16777215, 55))
        self.frame_182.setFrameShape(QFrame.Box)
        self.frame_182.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_182)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.label_165 = QLabel(self.frame_182)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_109.addWidget(self.label_165)

        self.line_spare_plc = QLineEdit(self.frame_182)
        self.line_spare_plc.setObjectName(u"line_spare_plc")
        self.line_spare_plc.setMaximumSize(QSize(300, 30))

        self.horizontalLayout_109.addWidget(self.line_spare_plc)

        self.check_spare_plc = QPushButton(self.frame_182)
        self.check_spare_plc.setObjectName(u"check_spare_plc")
        self.check_spare_plc.setMinimumSize(QSize(43, 21))
        self.check_spare_plc.setMaximumSize(QSize(80, 16777215))
        self.check_spare_plc.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_spare_plc.setStyleSheet(u"QPushButton{\n"
"background: green;\n"
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

        self.horizontalLayout_109.addWidget(self.check_spare_plc)

        self.label_166 = QLabel(self.frame_182)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_109.addWidget(self.label_166)

        self.label_spare_plc = QLabel(self.frame_182)
        self.label_spare_plc.setObjectName(u"label_spare_plc")

        self.horizontalLayout_109.addWidget(self.label_spare_plc)


        self.verticalLayout_115.addWidget(self.frame_182)

        self.frame_183 = QFrame(self.frame_176)
        self.frame_183.setObjectName(u"frame_183")
        self.frame_183.setMinimumSize(QSize(3, 48))
        self.frame_183.setMaximumSize(QSize(16777215, 46))
        self.frame_183.setFrameShape(QFrame.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_176 = QHBoxLayout(self.frame_183)
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.checkall_plc_btns = QPushButton(self.frame_183)
        self.checkall_plc_btns.setObjectName(u"checkall_plc_btns")
        self.checkall_plc_btns.setMinimumSize(QSize(71, 25))
        self.checkall_plc_btns.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkall_plc_btns.setStyleSheet(u"QPushButton{\n"
"background: green;\n"
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

        self.horizontalLayout_176.addWidget(self.checkall_plc_btns)

        self.save_plc_pathes = QPushButton(self.frame_183)
        self.save_plc_pathes.setObjectName(u"save_plc_pathes")
        self.save_plc_pathes.setMinimumSize(QSize(71, 25))
        self.save_plc_pathes.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_plc_pathes.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_176.addWidget(self.save_plc_pathes)


        self.verticalLayout_115.addWidget(self.frame_183, 0, Qt.AlignHCenter)


        self.verticalLayout_114.addWidget(self.frame_176)

        self.line_20 = QFrame(self.groupBox_13)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_114.addWidget(self.line_20)


        self.verticalLayout_113.addWidget(self.groupBox_13)

        self.line_21 = QFrame(self.frame_175)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_113.addWidget(self.line_21)

        self.groupBox_16 = QGroupBox(self.frame_175)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setMinimumSize(QSize(0, 219))
        self.groupBox_16.setMaximumSize(QSize(16777215, 237))
        self.verticalLayout_116 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.frame_180 = QFrame(self.groupBox_16)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setFrameShape(QFrame.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_180)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_167 = QLabel(self.frame_180)
        self.label_167.setObjectName(u"label_167")

        self.horizontalLayout_86.addWidget(self.label_167)

        self.line_set_value_plc = QLineEdit(self.frame_180)
        self.line_set_value_plc.setObjectName(u"line_set_value_plc")
        self.line_set_value_plc.setMaximumSize(QSize(300, 30))

        self.horizontalLayout_86.addWidget(self.line_set_value_plc)

        self.check_set_value_plc = QPushButton(self.frame_180)
        self.check_set_value_plc.setObjectName(u"check_set_value_plc")
        self.check_set_value_plc.setMinimumSize(QSize(80, 21))
        self.check_set_value_plc.setMaximumSize(QSize(80, 16777215))
        self.check_set_value_plc.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_set_value_plc.setStyleSheet(u"QPushButton{\n"
"background: green;\n"
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

        self.horizontalLayout_86.addWidget(self.check_set_value_plc)


        self.verticalLayout_116.addWidget(self.frame_180)

        self.frame_185 = QFrame(self.groupBox_16)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setMinimumSize(QSize(0, 34))
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_185)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_169 = QLabel(self.frame_185)
        self.label_169.setObjectName(u"label_169")

        self.horizontalLayout_87.addWidget(self.label_169)

        self.label_set_value_plc = QLabel(self.frame_185)
        self.label_set_value_plc.setObjectName(u"label_set_value_plc")

        self.horizontalLayout_87.addWidget(self.label_set_value_plc)


        self.verticalLayout_116.addWidget(self.frame_185)

        self.frame_184 = QFrame(self.groupBox_16)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setMinimumSize(QSize(50, 55))
        self.frame_184.setMaximumSize(QSize(11111111, 55))
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_177 = QHBoxLayout(self.frame_184)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.line_value_set_value_plc = QLineEdit(self.frame_184)
        self.line_value_set_value_plc.setObjectName(u"line_value_set_value_plc")
        self.line_value_set_value_plc.setMinimumSize(QSize(0, 26))
        self.line_value_set_value_plc.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_177.addWidget(self.line_value_set_value_plc)

        self.set_value_plc = QPushButton(self.frame_184)
        self.set_value_plc.setObjectName(u"set_value_plc")
        self.set_value_plc.setMinimumSize(QSize(80, 21))
        self.set_value_plc.setMaximumSize(QSize(80, 16777215))
        self.set_value_plc.setCursor(QCursor(Qt.PointingHandCursor))
        self.set_value_plc.setStyleSheet(u"QPushButton{\n"
"background: green;\n"
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

        self.horizontalLayout_177.addWidget(self.set_value_plc)


        self.verticalLayout_116.addWidget(self.frame_184)


        self.verticalLayout_113.addWidget(self.groupBox_16)


        self.verticalLayout_124.addWidget(self.frame_175)


        self.horizontalLayout_68.addWidget(self.frame_96, 0, Qt.AlignTop)


        self.verticalLayout_22.addWidget(self.frame_92)

        self.stackedWidget.addWidget(self.page_settings)

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
        self.btn_message.setFont(font1)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"")

        self.verticalLayout_94.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font1)
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
        self.btn_logout.setFont(font1)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"")

        self.verticalLayout_94.addWidget(self.btn_logout)


        self.verticalLayout_14.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_95.addWidget(self.bgApp)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.noiseAreaSpinBox.valueChanged.connect(self.bar_noise_filter0_1_top.setValue)
        self.line_new_screw.textChanged.connect(self.label_screw_name.setText)
        self.bar_noise_filter0_1_top.valueChanged.connect(self.noiseAreaSpinBox.setValue)
        self.comboBox_edit_remove.currentTextChanged.connect(self.label_screw_name.setText)
        self.spinBox.valueChanged.connect(self.bar_thresh0_1_top.setValue)
        self.bar_thresh0_1_top.valueChanged.connect(self.spinBox.setValue)
        self.bar_thresh0_1_side.valueChanged.connect(self.spinBox_4.setValue)
        self.spinBox_4.valueChanged.connect(self.bar_thresh0_1_side.setValue)
        self.bar_noise_filter0_1_side.valueChanged.connect(self.spinBox_6.setValue)
        self.spinBox_6.valueChanged.connect(self.bar_noise_filter0_1_side.setValue)
        self.bar_thresh0_6_side.valueChanged.connect(self.spinBox_11.setValue)
        self.spinBox_11.valueChanged.connect(self.bar_thresh0_6_side.setValue)
        self.bar_thresh0_5_side.valueChanged.connect(self.spinBox_10.setValue)
        self.spinBox_10.valueChanged.connect(self.bar_thresh0_5_side.setValue)
        self.bar_thresh0_4_side.valueChanged.connect(self.spinBox_9.setValue)
        self.spinBox_9.valueChanged.connect(self.bar_thresh0_4_side.setValue)
        self.bar_thresh0_3_side.valueChanged.connect(self.spinBox_8.setValue)
        self.spinBox_8.valueChanged.connect(self.bar_thresh0_3_side.setValue)
        self.bar_thresh0_2_top.valueChanged.connect(self.spinBox_12.setValue)
        self.spinBox_12.valueChanged.connect(self.bar_thresh0_2_top.setValue)
        self.bar_noise_filter0_2_top.valueChanged.connect(self.spinBox_13.setValue)
        self.spinBox_13.valueChanged.connect(self.bar_noise_filter0_2_top.setValue)
        self.bar_thresh0_3_top.valueChanged.connect(self.spinBox_5.setValue)
        self.spinBox_5.valueChanged.connect(self.bar_thresh0_3_top.setValue)
        self.bar_noise_filter0_3_top.valueChanged.connect(self.spinBox_14.setValue)
        self.spinBox_14.valueChanged.connect(self.bar_noise_filter0_3_top.setValue)
        self.bar_thresh0_top_cal_page.valueChanged.connect(self.spinBox_16.setValue)
        self.spinBox_16.valueChanged.connect(self.bar_thresh0_top_cal_page.setValue)
        self.bar_noise_filter0_top_cal_page.valueChanged.connect(self.spinBox_15.setValue)
        self.spinBox_15.valueChanged.connect(self.bar_noise_filter0_top_cal_page.setValue)
        self.bar_thresh0_side_cal_page.valueChanged.connect(self.spinBox_19.setValue)
        self.spinBox_19.valueChanged.connect(self.bar_thresh0_side_cal_page.setValue)
        self.bar_noise_filter0_side_cal_page.valueChanged.connect(self.spinBox_20.setValue)
        self.spinBox_20.valueChanged.connect(self.bar_noise_filter0_side_cal_page.setValue)
        self.bar_thresh0_2_side.valueChanged.connect(self.spinBox_7.setValue)
        self.spinBox_7.valueChanged.connect(self.bar_thresh0_2_side.setValue)
        self.bar_thresh0_1_side.valueChanged.connect(self.bar_thresh0_2_side.setValue)
        self.bar_thresh0_1_side.valueChanged.connect(self.bar_thresh0_3_side.setValue)
        self.bar_thresh0_1_side.valueChanged.connect(self.bar_thresh0_4_side.setValue)
        self.bar_thresh0_1_side.valueChanged.connect(self.bar_thresh0_5_side.setValue)
        self.bar_thresh0_1_side.valueChanged.connect(self.bar_thresh0_6_side.setValue)
        self.bar_thresh0_6_side.valueChanged.connect(self.bar_thresh0_1_side.setValue)
        self.bar_thresh0_5_side.valueChanged.connect(self.bar_thresh0_1_side.setValue)
        self.bar_thresh0_4_side.valueChanged.connect(self.bar_thresh0_1_side.setValue)
        self.bar_thresh0_3_side.valueChanged.connect(self.bar_thresh0_1_side.setValue)
        self.bar_thresh0_2_side.valueChanged.connect(self.bar_thresh0_1_side.setValue)
        self.bar_thresh0_4_top.valueChanged.connect(self.spinBox_17.setValue)
        self.spinBox_17.valueChanged.connect(self.bar_thresh0_4_top.setValue)
        self.bar_noise_filter0_4_top.valueChanged.connect(self.spinBox_18.setValue)
        self.spinBox_18.valueChanged.connect(self.bar_noise_filter0_4_top.setValue)
        self.bar_thresh0_5_top.valueChanged.connect(self.spinBox_21.setValue)
        self.bar_noise_filter0_5_top.valueChanged.connect(self.spinBox_22.setValue)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(6)
        self.stackedWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toogle_btn_1.setText("")
#if QT_CONFIG(tooltip)
        self.side_dashboard_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Live", None))
#endif // QT_CONFIG(tooltip)
        self.side_dashboard_btn.setText("")
#if QT_CONFIG(tooltip)
        self.side_tool_setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Tools", None))
#endif // QT_CONFIG(tooltip)
        self.side_tool_setting_btn.setText("")
#if QT_CONFIG(tooltip)
        self.side_camera_setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Camera Settings", None))
#endif // QT_CONFIG(tooltip)
        self.side_camera_setting_btn.setText("")
#if QT_CONFIG(tooltip)
        self.side_calibration_setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Calibration Settings", None))
#endif // QT_CONFIG(tooltip)
        self.side_calibration_setting_btn.setText("")
#if QT_CONFIG(tooltip)
        self.side_users_setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"User Setting", None))
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
#if QT_CONFIG(tooltip)
        self.toogle_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Live", None))
#endif // QT_CONFIG(tooltip)
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
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Top Camera", None))
        self.label_img_top_live.setText("")
        self.btn_enabel_mask_draw_live_side.setText("")
#if QT_CONFIG(tooltip)
        self.btn_save_top_cam_live_page.setToolTip(QCoreApplication.translate("MainWindow", u"save image", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save_top_cam_live_page.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Side Camera", None))
        self.label_img_side_live.setText("")
        self.btn_enabel_mask_draw_live_top.setText("")
#if QT_CONFIG(tooltip)
        self.btn_save_side_cam_live_page.setToolTip(QCoreApplication.translate("MainWindow", u"save image", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save_side_cam_live_page.setText("")
        self.groupBox_29.setTitle(QCoreApplication.translate("MainWindow", u"Camera :", None))
        self.connect_cameras_live_page.setText("")
        self.line_camera_status.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Connection Status", None))
        self.disconnect_cameras_live_page.setText("")
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"PLC :", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.plc_status_live_page.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"Mode :", None))
        self.plc_mode_live_page.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Reject :", None))
        self.plc_reject_live_page.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Select Screw :", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.history_btn.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_selected_screw_top_live.setText("")
        self.label_selected_screw_side_live.setText("")
        self.start_capture_live_page.setText(QCoreApplication.translate("MainWindow", u"Start Detect", None))
        self.stop_capture_live_page.setText(QCoreApplication.translate("MainWindow", u"Stop Detect", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Top Camera Table :", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Side Camera Table :", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Own : Radco-Vision", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.edit_remove_btn.setText(QCoreApplication.translate("MainWindow", u"Edit/Remove", None))
        self.edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.remove_screw_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.save_new_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Current :", None))
        self.label_screw_name.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_status_mode.setText("")
        self.label_warning_tool_page.setText("")
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Top Camera", None))
        self.checkbox_page0_1_top.setText("")
        self.btn_page0_1_top.setText(QCoreApplication.translate("MainWindow", u"Main", None))
        self.checkbox_page0_2_top.setText("")
        self.btn_page0_2_top.setText(QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.checkbox_page0_3_top.setText("")
        self.btn_page0_3_top.setText(QCoreApplication.translate("MainWindow", u"Defect", None))
        self.checkbox_page0_4_top.setText("")
        self.btn_page0_4_top.setText(QCoreApplication.translate("MainWindow", u"Edge crack", None))
        self.checkbox_page0_5_top.setText("")
        self.btn_page0_5_top.setText(QCoreApplication.translate("MainWindow", u"centerality", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Side Camera", None))
        self.checkbox_page0_1_side.setText("")
        self.btn_page0_1_side.setText(QCoreApplication.translate("MainWindow", u"Main", None))
        self.checkbox_page0_2_side.setText("")
        self.btn_page0_2_side.setText(QCoreApplication.translate("MainWindow", u" Lenght", None))
        self.checkbox_page0_3_side.setText("")
        self.btn_page0_3_side.setText(QCoreApplication.translate("MainWindow", u" Male Thread ", None))
        self.checkbox_page0_4_side.setText("")
        self.btn_page0_4_side.setText(QCoreApplication.translate("MainWindow", u" Diameter ", None))
        self.checkbox_page0_5_side.setText("")
        self.btn_page0_5_side.setText(QCoreApplication.translate("MainWindow", u"Screw Head", None))
        self.checkbox_page0_6_side.setText("")
        self.btn_page0_6_side.setText(QCoreApplication.translate("MainWindow", u"Defect", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Top camera", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.line_img_path0_1_top.setText("")
        self.btn_load_image0_1_top.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_set_img0_1_top.setText(QCoreApplication.translate("MainWindow", u"Set Image", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Side Camera :", None))
        self.btn_connect_camera0_1_top.setText(QCoreApplication.translate("MainWindow", u"Connect and Grab", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Rect 1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Rect 2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.checkbox_thresh_inv0_1_top.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Noise filter", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Area Name :", None))
        self.btn_add_region0_2_top.setText("")
        self.btn_remove_region0_2_top.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Drawing ..........", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.checkbox_thresh_inv0_2_top.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Noise Filter", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Select Shape Type", None))
        self.check_circle_2_top.setText(QCoreApplication.translate("MainWindow", u"Circle", None))
        self.check_rect_2_top.setText(QCoreApplication.translate("MainWindow", u"Rectangle", None))
        self.check_hexagonal_2_top.setText(QCoreApplication.translate("MainWindow", u"Hexagonal", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Diameter :", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Min :", None))
        self.label_min_diameter_2_top.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Max :", None))
        self.label_max_diameter_2_top.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Limit Diameter ", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"District  Distanse :", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Min :", None))
        self.label_min_district_2_top.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Max :", None))
        self.label_max_district_2_top.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Limit District Distanse :", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"Distanse Corner :", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Min :", None))
        self.label_min_corner_2_top.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Max :", None))
        self.label_max_corner_2_top.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Limit Distanse Corner :", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.btn_draw_complete0_2_top.setText(QCoreApplication.translate("MainWindow", u"Complete", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Area Name :", None))
        self.btn_add_region0_3_top.setText("")
        self.btn_remove_region0_3_top.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Circle 1 :", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Radius :", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Circle 2 :", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Radius :", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.checkbox_thresh_inv0_3_top.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Noise filter", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Area Threshold   :  ", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Area", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_min_area_3_top.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_max_area_3_top.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.checkbox_thresh_inv0_4_top.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Noise filter", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Select Shape Type", None))
        self.check_circle_4_top.setText(QCoreApplication.translate("MainWindow", u"Circle", None))
        self.check_rect_4_top.setText(QCoreApplication.translate("MainWindow", u"Rectangle", None))
        self.check_hexagonal_4_top.setText(QCoreApplication.translate("MainWindow", u"Hexagonal", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Area Thresh", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Crack Areas", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_min_area_4_top.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_max_area_4_top.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.checkbox_thresh_inv0_5_top.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"Noise filter", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Distance between centers :   ", None))
        self.label_distance_centers_5_top.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"Lenght :", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Side camera", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.line_img_path0_1_side.setText("")
        self.btn_load_image0_1_side.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_set_img0_1_side.setText(QCoreApplication.translate("MainWindow", u"Set Image", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Side Camera :", None))
        self.btn_connect_camera0_1_side.setText(QCoreApplication.translate("MainWindow", u"Connect and Grab", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Rect 1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.checkbox_thresh_inv0_1_side.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Noise filter", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Side Lenght", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Rect 1", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Lenght :", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Min :", None))
        self.label_min_lenght_2_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Max :", None))
        self.label_max_lenght_2_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Avg :", None))
        self.label_avg_lenght_2_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Lenght :", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Male Thread", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"Rect 1", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Jump Threshold :", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Thread length :", None))
        self.label_thread_lenght_3_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Count Male Thread :", None))
        self.label_count_thread_3_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Thread Step", None))
        self.label_step_distance_3_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Include Nafi :", None))
        self.checkbox_navel_3_side.setText(QCoreApplication.translate("MainWindow", u"Nafi", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Side Diameter", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Area Name :", None))
        self.btn_add_region0_4_side.setText("")
        self.btn_remove_region0_4_side.setText("")
        self.groupBox_26.setTitle("")
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Diameter :", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Min :", None))
        self.label_min_diameter_4_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Max :", None))
        self.label_max_diameter_4_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Avg :", None))
        self.label_avg_diameter_4_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Diameter X: :", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.btn_complete_area_4_side.setText(QCoreApplication.translate("MainWindow", u"    Complete    ", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Screw Head", None))
        self.groupBox_27.setTitle("")
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"top/bottom edge:", None))
        self.btn_top_5_side.setText(QCoreApplication.translate("MainWindow", u"Top", None))
        self.btn_bottom_5_side.setText(QCoreApplication.translate("MainWindow", u"Bottom", None))
        self.checkbox_belt_5_side.setText(QCoreApplication.translate("MainWindow", u"From Belt", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Head :", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Min :", None))
        self.label_min_head_height_5_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Max :", None))
        self.label_max_head_height_5_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Avg :", None))
        self.label_avg_head_height_5_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Head Height :", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Jump Threshold  :", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Side Damage", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Area Name :", None))
        self.btn_add_region0_6_side.setText("")
        self.btn_remove_region0_6_side.setText("")
        self.groupBox_28.setTitle("")
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Area     :", None))
        self.label_area_6_side.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.btn_complete_area_6_side.setText(QCoreApplication.translate("MainWindow", u"    Complete    ", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.prev_page_btn.setText("")
        self.save_btn_page_grab.setText(QCoreApplication.translate("MainWindow", u"Save/Exit", None))
        self.next_page_btn.setText("")
        self.label_image_grab_page.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Pos :", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.label_x_pos_tool_page.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.label_y_pos_tool_page.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Color :", None))
        self.label_color_value.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.img_color_value.setText("")
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"Show Mask :", None))
        self.btn_enabel_mask_draw.setText("")
#if QT_CONFIG(tooltip)
        self.fullscreen_cam_grab_2.setToolTip(QCoreApplication.translate("MainWindow", u"clear all", None))
#endif // QT_CONFIG(tooltip)
        self.fullscreen_cam_grab_2.setText("")
#if QT_CONFIG(tooltip)
        self.fullscreen_page_tools.setToolTip(QCoreApplication.translate("MainWindow", u"Full screen", None))
#endif // QT_CONFIG(tooltip)
        self.fullscreen_page_tools.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cam01 TOP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cam02 Side", None))
        self.camera01_btn.setText("")
        self.camera02_btn.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Cameras", None))
        self.cameraname_label.setText(QCoreApplication.translate("MainWindow", u"No Camera Selected", None))
        self.ultra_setting_btn.setText(QCoreApplication.translate("MainWindow", u"Ulta Settings", None))
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
        self.camera_setting_reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.camera_setting_connect_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.play_camera_setting_btn.setText("")
        self.pause_camera_setting_btn.setText("")
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Folder Name :", None))
        self.camera_setting_message_label.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Top Camera", None))
        self.camera_setting_picture_top.setText("")
        self.camera_setting_get_top_camera.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.fullscreen_cam_top_btn.setText("")
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Side Camera", None))
        self.camera_setting_picture_side.setText("")
        self.camera_setting_get_side_camera.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.fullscreen_cam_side_btn.setText("")
        self.camera_setting_tools_page.setText(QCoreApplication.translate("MainWindow", u"Tools Page", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"Top Camera :", None))
        self.btn_connect_top_cal_page.setText("")
        self.btn_disconnect_top_cal_page.setText("")
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.connection_status_top_cal_page.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.camera_top_cal_page.setText("")
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.checkbox_thresh_inv0_top_cal_page.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Noise filter", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"Input Dimention :", None))
        self.btn_calibration_top_cal_page.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Pixel Size :", None))
        self.label_top_calibration.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_save_value_top_cal_page.setText("")
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"Side Camera :", None))
        self.btn_connect_side_cal_page.setText("")
        self.btn_disconnect_side_cal_page.setText("")
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.connection_status_side_cal_page.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.camera_side_cal_page.setText("")
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.checkbox_thresh_inv0_side_cal_page.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"Noise filter", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"Input Dimention :", None))
        self.btn_calibration_side_cal_page.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"Pixel Size :", None))
        self.label_side_calibration.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_save_value_side_cal_page.setText("")
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
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Appearance Settings", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Main Path  :          ", None))
        self.line_main_path.setText(QCoreApplication.translate("MainWindow", u"capture_images", None))
        self.tool_btn_main_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Style", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Font-Style", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Font-Size", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.label_language.setText("")
        self.setting_appearance_apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Settings", None))
        self.general_setting_appearance_message_label.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Default Sizes :", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Top camera:", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Resolution :", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Side camera :", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Resolution :", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.btn_set_szies.setText(QCoreApplication.translate("MainWindow", u"Apply Settings", None))
        self.setting_defect_message_label.setText("")
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"PLC IP (OPC) :", None))
        self.plc_ip_line.setText(QCoreApplication.translate("MainWindow", u"opc.tcp://127.0.0.1:8081", None))
        self.plc_ip_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"opc.tcp://127.0.0.1:8081", None))
        self.btn_save_ip_plc.setText("")
        self.plc_warnings.setText("")
        self.connect_plc_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.options_plc_btn.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.disconnect_plc_btn.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"PLC NodeID Addresses :", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Run :", None))
        self.check_run_plc.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Value :", None))
        self.label_run_plc.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Stop :", None))
        self.check_stop_plc.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"Value :", None))
        self.label_stop_plc.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Reject :", None))
        self.check_reject_plc.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Value :", None))
        self.label_reject_plc.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Start time delay :", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Duration of being on :", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"Spare :", None))
        self.check_spare_plc.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Value :", None))
        self.label_spare_plc.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.checkall_plc_btns.setText(QCoreApplication.translate("MainWindow", u"Check All", None))
        self.save_plc_pathes.setText(QCoreApplication.translate("MainWindow", u"Save All", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Set PLC Value", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"Addresses :", None))
        self.check_set_value_plc.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"Current Value :", None))
        self.label_set_value_plc.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.set_value_plc.setText(QCoreApplication.translate("MainWindow", u"Set Value", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

