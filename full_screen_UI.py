from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *

ui, _ = loadUiType("full_screen.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

from PySide6.QtGui import QImage as sQImage    # should change
from PySide6.QtGui import QPixmap as sQPixmap   # should change

class FullScreen_UI(QMainWindow, ui):
    global widgets
    widgets = ui
    x=0

    def __init__(self):
        super(FullScreen_UI, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()

        self.checkBox_ontop.stateChanged.connect(lambda:self.check_box_state(self.checkBox_ontop))
        self._old_pos = None


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        self.maxiButton.clicked.connect(self.maxmize_minimize)

    def win_set_geometry(self, left=100, top=600, width=800, height=600):
        self.setGeometry(left, top, width, height)

    def minimize(self):
        self.showMinimized()

    def close_win(self):
        self.close()

    def maxmize_minimize(self):
        
        if self.isMaximized():
            self.showNormal()
            # self.sheet_view_down=data_grabber.sheetOverView(h=129,w=1084,nh=12,nw=30)
        else:
            self.showMaximized()


    def check_box_state(self,b):
            print(b.isChecked())
            if b.isChecked() == True:
                flags = Qt.WindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
                # QtCore.Qt.WindowStaysOnTopHint
                self.setWindowFlags(flags)
                self.show()
            else:
                flags = Qt.WindowFlags(Qt.FramelessWindowHint)
                self.setWindowFlags(flags)
                self.show()



    def show_image_(self,img):
        self.n_image.setPixmap(QPixmap.fromImage(
            QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)))


    def show_image(self,img):

        try:
            if len(img.shape)==3:
                h, w, ch = img.shape
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            else:
                h,w = img.shape
                ch = 3
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        except:
            print('Error show_image')

        bytes_per_line = ch * w  
        
        
        convert_to_Qt_format = sQImage(img.data, w, h, bytes_per_line, sQImage.Format_RGB888)

        self.n_image.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))

        
# api = labeling_api.labeling_API(win)
import cv2
if __name__ == "__main__":
    img = cv2.imread('images/capture_eror.jpg')
    # cv2.imshow('asd',img)
    # cv2.waitKey(0)
    app = QApplication()
    win = FullScreen_UI()
    win.show()
    win.show_image(img)
    sys.exit(app.exec())
