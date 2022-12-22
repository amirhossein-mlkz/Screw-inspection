import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtGui import *
from pyparsing import col
# from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap
from PyQt5.QtGui import QPainter
import numpy as np
import threading
import time
from PyQt5.QtGui import QPainter
import os
import login_api
import cv2
# from qt_material import apply_stylesheet
ui, _ = loadUiType("history_window.ui")


os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
class UI_history_window(QMainWindow, ui):
    global widgets
    widgets = ui

    def __init__(self):

        super(UI_history_window, self).__init__()


        self.setupUi(self)
        self.setWindowTitle('Screw History')



if __name__=='__main__':
    app = QApplication()
    win = UI_history_window()
    # apply_stylesheet(app,theme='dark_cyan.xml')
    api = login_api.API(win)
    win.show()
    sys.exit(app.exec())
    