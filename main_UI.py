# import os
# import PySide6

# dirname = os.path.dirname(PySide6.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

# from PySide6.QtWidgets import *

import sys
from tabnanny import check
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtGui import *
from matplotlib import image
from pyparsing import col
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QSize, QRegExp
import numpy as np
import threading
import time
from PyQt5.QtGui import QPainter
import os

# from regex import F
import main_api
import cv2
from qt_material import apply_stylesheet
from app_settings import Settings
from functools import partial

import numpy as np

from backend import camera_funcs, user_login_logout_funcs, colors_pallete
import resources


from PySide6.QtGui import QImage as sQImage    # should change
from PySide6.QtGui import QPixmap as sQPixmap   # should change
from PySide6.QtCharts import QChart as sQChart
from PySide6.QtCharts import QChartView as sQChartView
from PySide6.QtCharts import QLineSeries as sQLineSeries
from PySide6.QtCharts import QScatterSeries as sQScatterSeries
from PySide6.QtCharts import QSplineSeries as sQSplineSeries
from PySide6.QtCharts import QValueAxis as sQValueAxis
from PySide6.QtCore import QPointF as sQPointF
from PySide6.QtWidgets import QHBoxLayout as sQHBoxLayout
from PySide6.QtWidgets import QVBoxLayout as sQVBoxLayout
from PySide6.QtWidgets import QScrollBar as sQScrollBar
from PySide6.QtWidgets import QAbstractSlider as sQAbstractSlider
from PySide6.QtWidgets import QSlider as sQSlider
from PySide6.QtWidgets import QLabel as sQLabel
from PySide6 import QtCore as sQtCore
from PySide6.QtGui import QColor as sQColor
from PySide6.QtGui import QBrush as sQBrush
from PySide6.QtGui import QPen as sQPen
from PySide6.QtGui import QPainter as sQPainter
from PySide6.QtGui import QCursor as sQCursor

import texts
from backend import Utils
import Keys
ui, _ = loadUiType("main_window.ui")


os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
class UI_main_window(QMainWindow, ui):
    global widgets
    widgets = ui

    def __init__(self):

        super(UI_main_window, self).__init__()


        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()


        self.cam_num_old=1

        self.calibration_image = None


        self.login_flag = False
        self.camera_connect_flag = False

        #   Define and set UI_KEYS

        Keys.object_dict_builder(self)


        self.side_buttons = [self.side_camera_setting_btn, self.side_tool_setting_btn\
                            ,self.side_users_setting_btn,self.side_general_setting_btn, self.side_dashboard_btn]

        # camera variable parameters ids in the camera-settings section of the UI 
        self.camera_params = [self.gain_spinbox, self.expo_spinbox, self.width_spinbox\
                            , self.height_spinbox, self.offsetx_spinbox, self.offsety_spinbox\
                            ,self.trigger_combo, self.maxbuffer_spinbox, self.packetdelay_spinbox\
                                , self.packetsize_spinbox, self.transmissiondelay_spinbox, self.ip_lineedit, self.serial_number_combo, self.camera_setting_connect_btn]
        

        self.main_login_btn.setIcon(sQPixmap.fromImage(sQImage('images/login_white.png')))
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Screw - Utils"

        self.setWindowTitle(title)

        self.toogle_btn_1.clicked.connect(partial(self.leftmenu))
        self.toogle_btn_2.clicked.connect(partial(self.leftmenu))

        self.set_combo_boxes_2()

        self.pages_name_dict={'1':'1_top','2':'2_top','3':'1_side','4':'2_side','5':'3_side','6':'4_side'}
        self.pages_dircetion_dict={'1':'top','2':'top','3':'side','4':'side','5':'side','6':'side'}
        self.roi_name=['x1','y1','x2','y2']
        self.limit_name=['min','max']

        self.combo_exist={'1_top':False,'2_top':True,'1_side':False,'2_side':False,'3_side':False,'4_side':True}

        
        self.tool_btn_bar_side={'lenght':self.frame_36,'btn_male':self.btn_page0_3_side,'Male_Thread':self.frame_78,'btn_lenght':self.btn_page0_2_side,'Diameter':self.frame_79,}
        self.tool_btn_bar_top=frames={'area':self.frame_34}


        # self.get_sub_page_name()


        # self.enable_bar_btn_side()
        # self.enable_bar_btn_top()

        # self.get_activate_pages()
        self.enable_bar_btn_tool_page()
        
        # SET LANGUAGE
        #//////////////////////////////////////////////
        # self.set_language()
        self.language = 'en'

        self._old_pos = None


        self.editmode=False


        self.check_mask_type(self.check_circle0_2_top.objectName(),change_size=True)


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



    def leftmenu(self):


        width=self.leftMenuBg.width()

        if width ==0:
    
            # print('if')

            self.left_box = QPropertyAnimation(self.topMenu, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(0)
            self.left_box.setEndValue(11111)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart) 

            self.left_box_2 = QPropertyAnimation(self.leftMenuBg, b"minimumWidth")
            self.left_box_2.setDuration(Settings.TIME_ANIMATION)
            self.left_box_2.setStartValue(0)
            self.left_box_2.setEndValue(60)
            self.left_box_2.setEasingCurve(QEasingCurve.InOutQuart) 
    
            self.left_box_5 = QPropertyAnimation(self.leftMenuBg, b"maximumWidth")
            self.left_box_5.setDuration(Settings.TIME_ANIMATION)
            self.left_box_5.setStartValue(0)
            self.left_box_5.setEndValue(60)
            self.left_box_5.setEasingCurve(QEasingCurve.InOutQuart) 

            self.left_box_3 = QPropertyAnimation(self.toogle_btn_1, b"minimumWidth")
            self.left_box_3.setDuration(Settings.TIME_ANIMATION)
            self.left_box_3.setStartValue(0)
            self.left_box_3.setEndValue(34)
            self.left_box_3.setEasingCurve(QEasingCurve.InOutQuart) 
 
            self.left_box_4 = QPropertyAnimation(self.toogle_btn_2, b"minimumWidth")
            self.left_box_4.setDuration(Settings.TIME_ANIMATION)
            self.left_box_4.setStartValue(34)
            self.left_box_4.setEndValue(0)
            self.left_box_4.setEasingCurve(QEasingCurve.InOutQuart) 


            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.addAnimation(self.left_box_2)
            self.group.addAnimation(self.left_box_3)
            self.group.addAnimation(self.left_box_4)
            self.group.addAnimation(self.left_box_5)

            self.group.start()    

        else :

            # print('else')

            self.left_box = QPropertyAnimation(self.topMenu, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(width)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart) 

            self.left_box_2 = QPropertyAnimation(self.leftMenuBg, b"minimumWidth")
            self.left_box_2.setDuration(Settings.TIME_ANIMATION)
            self.left_box_2.setStartValue(60)
            self.left_box_2.setEndValue(0)
            self.left_box_2.setEasingCurve(QEasingCurve.InOutQuart)

            self.left_box_5 = QPropertyAnimation(self.leftMenuBg, b"maximumWidth")
            self.left_box_5.setDuration(Settings.TIME_ANIMATION)
            self.left_box_5.setStartValue(60)
            self.left_box_5.setEndValue(0)
            self.left_box_5.setEasingCurve(QEasingCurve.InOutQuart)            

            self.left_box_3 = QPropertyAnimation(self.toogle_btn_1, b"minimumWidth")
            self.left_box_3.setDuration(Settings.TIME_ANIMATION)
            self.left_box_3.setStartValue(34)
            self.left_box_3.setEndValue(0)
            self.left_box_3.setEasingCurve(QEasingCurve.InOutQuart) 


            self.left_box_4 = QPropertyAnimation(self.toogle_btn_2, b"minimumWidth")
            self.left_box_4.setDuration(Settings.TIME_ANIMATION)
            self.left_box_4.setStartValue(0)
            self.left_box_4.setEndValue(34)
            self.left_box_4.setEasingCurve(QEasingCurve.InOutQuart) 


            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.addAnimation(self.left_box_2)
            self.group.addAnimation(self.left_box_3)
            self.group.addAnimation(self.left_box_4)
            self.group.addAnimation(self.left_box_5)

            self.group.start()    

 


    def animation_move(self,label_name,lenght,size_zero=False):

        width=label_name.width()

        if width ==0:


            self.animation_box = QPropertyAnimation(label_name, b"minimumWidth")
            self.animation_box.setDuration(Settings.TIME_ANIMATION)
            self.animation_box.setStartValue(0)
            self.animation_box.setEndValue(lenght)
            self.animation_box.setEasingCurve(QEasingCurve.InOutQuart) 


            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.animation_box)
            self.group.start() 

        else :
    
        
            self.animation_box = QPropertyAnimation(label_name, b"minimumWidth")
            self.animation_box.setDuration(Settings.TIME_ANIMATION)
            self.animation_box.setStartValue(lenght)
            self.animation_box.setEndValue(0)
            self.animation_box.setEasingCurve(QEasingCurve.InOutQuart)


            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.animation_box)
            self.group.start() 

        if size_zero and width!=0:

            self.animation_box = QPropertyAnimation(label_name, b"minimumWidth")
            self.animation_box.setDuration(Settings.TIME_ANIMATION)
            self.animation_box.setStartValue(lenght)
            self.animation_box.setEndValue(0)
            self.animation_box.setEasingCurve(QEasingCurve.InOutQuart)


            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.animation_box)
            self.group.start() 

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize_win)
        self.maxiButton.clicked.connect(self.maxmize_minimize)

        self.side_camera_setting_btn.clicked.connect(self.buttonClick)
        self.side_dashboard_btn.clicked.connect(self.buttonClick)

        self.side_tool_setting_btn.clicked.connect(self.buttonClick)
        self.side_general_setting_btn.clicked.connect(self.buttonClick)

        self.camera01_btn.clicked.connect(self.buttonClick)
        self.camera02_btn.clicked.connect(self.buttonClick)

        self.side_users_setting_btn.clicked.connect(self.buttonClick)

        self.add_user_btn.clicked.connect(self.buttonClick)

        self.add_btn.clicked.connect(self.buttonClick)
        self.edit_remove_btn.clicked.connect(self.buttonClick)
        self.save_new_btn.clicked.connect(self.buttonClick)
        self.edit_btn.clicked.connect(self.buttonClick)






        # page tools
        self.btn_page0_1_top.clicked.connect(self.buttonClick)
        self.btn_page0_2_top.clicked.connect(self.buttonClick)
        self.btn_page0_1_side.clicked.connect(self.buttonClick)
        self.btn_page0_2_side.clicked.connect(self.buttonClick)
        self.btn_page0_3_side.clicked.connect(self.buttonClick)
        self.btn_page0_4_side.clicked.connect(self.buttonClick)
        self.next_page_btn.clicked.connect(self.buttonClick)
        self.prev_page_btn.clicked.connect(self.buttonClick)



        # Page 1_main

        self.btn_load_image0_1_top.clicked.connect(self.buttonClick)


        # page 2_main

        

        self.btn_add_area0_2_top.clicked.connect(self.buttonClick)
        self.btn_set_corner0_2_top.clicked.connect(self.buttonClick)
        self.btn_draw_complete0_2_top.clicked.connect(self.buttonClick)

        self.check_rect0_2_top.clicked.connect(lambda:self.check_mask_type(self.check_rect0_2_top.objectName(),change_size=True))
        self.check_circle0_2_top.clicked.connect(lambda:self.check_mask_type(self.check_circle0_2_top.objectName(),change_size=True))
        self.check_mask0_2_top.clicked.connect(lambda:self.check_mask_type(self.check_mask0_2_top.objectName(),change_size=True))


        # page 1_side

        self.btn_load_image0_1_side.clicked.connect(self.buttonClick)  



        # page 4_side  btn_add_area0_4_side

        self.btn_add_area0_4_side.clicked.connect(self.buttonClick)
        self.btn_complete_area_4_side.clicked.connect(self.buttonClick)


    def close_win(self):
        self.close()
        sys.exit()

    def minimize_win(self):
        self.showMinimized()

    def maxmize_minimize(self):
        
        if self.isMaximized():
            self.showNormal()
            # self.sheet_view_down=data_grabber.sheetOverView(h=129,w=1084,nh=12,nw=30)
        else:
            self.showMaximized()



    def set_combo_boxes_2(self):

        x=["Operator", "Admin"]
        self.user_role.addItems(x)


    def set_combo_boxes(self,combo_name,items):

        combo_name.clear()
        combo_name.addItems(items)

    def check_box_state(self,b):

            if b.isChecked() == True:
                b.setText('Enable')
            else:
                b.setText('Disable')


    # User Managment page --------------------------------

 

    def get_user_pass(self):
        self.user_name_value=self.user_name.text()
        self.password_value=self.password.text()

        return self.user_name_value,self.password_value


    def set_login_message(self,text,color):
        self.login_message.setText(text)
        self.login_message.setStyleSheet("color:#{}".format(color))



    def show_mesagges(self,label_name,text,color='green'):
        
        name=label_name

        if text!=None:


            label_name.setText(text)
            label_name.setStyleSheet("color:{}".format(color))       

            threading.Timer(2,self.show_mesagges,args=(name,None)).start()

        else:
            label_name.setText('')





    def show_question(self, title, message):
        msg = QMessageBox.question(self, title, message, QMessageBox.Cancel | QMessageBox.No| QMessageBox.Yes)
        if msg == QMessageBox.Yes:
            return True
        if msg == QMessageBox.No:
            return False
        
    def show_save_question(self, title, message):

        msg = QMessageBox.question(self, title, message, QMessageBox.Cancel| QMessageBox.SaveAll|QMessageBox.Discard)
        if msg == QMessageBox.Cancel:
            return None
        if msg == QMessageBox.SaveAll:
            return True       
        if msg == QMessageBox.Discard:
            return False  

    def show_warning(self, title, message):
        msg = QMessageBox.question(self, title, message,QMessageBox.Ok)
                    

    def set_warning(self, text, name, level=1):                            #Show warning
        waring_labels = {
            'tool_page': self.label_warning_tool_page,
            

        }
        # print('set_warning')
        if text != None:
    
            if level == 1:
                waring_labels[name].setText(' ' + text + ' ')
                waring_labels[name].setStyleSheet('background-color:#20a740;border-radius:10px;color:white')

            if level == 2:
                waring_labels[name].setText(' Warning: ' + text)
                waring_labels[name].setStyleSheet('background-color:#FDFFA9;border-radius:2px;color:black')

            if level == 3:
                waring_labels[name].setText(' EROR : ' + text)
                waring_labels[name].setStyleSheet('background-color:#D9534F;border-radius:2px;color:black')

            threading.Timer(2, self.set_warning, args=(None, name)).start()

        else:
            waring_labels[name].setText('')
            waring_labels[name].setStyleSheet('')



    # Page 1_top

    def get_main_parms_screw_top(self):

        dic={}
        dic.update({'name':self.label_screw_name.text()})
        dic.update({'threshold':self.bar_thresh0_1_top.value()})
        dic.update({'x1':self.spin_roi_x1_1_top.value()})
        dic.update({'y1':self.spin_roi_y1_1_top.value()})
        dic.update({'x2':self.spin_roi_x2_1_top.value()})
        dic.update({'y2':self.spin_roi_y2_1_top.value()})

        return dic
    
    
    def get_main_parms_screw_side(self):
    
        dic={}
        dic.update({'name':self.label_screw_name.text()})
        dic.update({'threshold':self.bar_thresh0_1_side.value()})
        dic.update({'x1':self.spin_roi_x1_1_side.value()})
        dic.update({'y1':self.spin_roi_y1_1_side.value()})
        dic.update({'x2':self.spin_roi_x2_1_side.value()})
        dic.update({'y2':self.spin_roi_y2_1_side.value()})

        return dic
    
    
    
    def set_main_parms_screw_top(self,parms):        
        self.bar_thresh0_1_top.setValue(int(parms['main_thresh']))
        self.line_image_address0_1_top.setText(str(parms['img_path']))
        self.spin_roi_x1_1_top.setValue( parms['main_roi'][0][0] )
        self.spin_roi_y1_1_top.setValue( parms['main_roi'][0][1] )
        self.spin_roi_x2_1_top.setValue( parms['main_roi'][1][0] )
        self.spin_roi_y2_1_top.setValue( parms['main_roi'][1][1] )
        
        
        
    def set_main_parms_screw_side(self,parms):        
        self.bar_thresh0_1_side.setValue(int(parms['main_thresh']))
        self.line_image_address0_1_side.setText(str(parms['img_path']))
        self.spin_roi_x1_1_side.setValue( parms['main_roi'][0][0] )
        self.spin_roi_y1_1_side.setValue( parms['main_roi'][0][1] )
        self.spin_roi_x2_1_side.setValue( parms['main_roi'][1][0] )
        self.spin_roi_y2_1_side.setValue( parms['main_roi'][1][1] )



          
    def  open_file_dialog(self,set_label):

        filepath = QFileDialog.getOpenFileName(self, 'Select a File')
        print(filepath)
        set_label.setText(filepath[0])




    def check_camera_selected_direction(self):
        
        print('adww')









    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()



        if btnName =='side_camera_setting_btn' and self.stackedWidget.currentWidget()!=self.page_camera_setting:

            self.stackedWidget.setCurrentWidget(self.page_camera_setting)
        
        if btnName =='side_dashboard_btn' and self.stackedWidget.currentWidget()!=self.page_dashboard:

            self.stackedWidget.setCurrentWidget(self.page_dashboard)

        if btnName =='side_users_setting_btn' :

            self.stackedWidget.setCurrentWidget(self.page_users_setting)


        if btnName =='side_tool_setting_btn' :

            self.stackedWidget.setCurrentWidget(self.page_tools)

        
        if btnName =='side_general_setting_btn' :

            self.stackedWidget.setCurrentWidget(self.page_settings)

        if btnName =='edit_remove_btn' :
            if self.editmode==False:
                self.animation_move(self.frame_24,300)
                self.enable_bar_btn_tool_page(False)
                # self.editmode=True
            else :
                self.set_warning(texts.WARNINGS['EDIT_MODE'][self.language],'tool_page',level=2)
        if btnName =='add_btn' :

            if self.editmode==False:

                self.animation_move(self.frame_23,300)
            
            else :
                self.set_warning(texts.WARNINGS['EDIT_MODE'][self.language],'tool_page',level=2)

    # def set_warning(self, text, name, level=1):                            #Show warning
    #     waring_labels = {
    #         'tool_page': self.label_warning_tool_page,
        if btnName =='save_new_btn' :

            self.animation_move(self.frame_23,300)
            self.stackedWidget_2.setCurrentIndex(1)

        if btnName =='edit_btn' :
            if self.editmode==False:
                self.animation_move(self.frame_24,300)
                self.animation_move(self.frame_23,0)
                self.stackedWidget_2.setCurrentIndex(1)
                self.set_label(self.label_status_mode,'Edit Mode')
                self.editmode=True
                self.enable_bar_btn_tool_page()
                self.frame_size(self.frame_save_btns,57)


        if btnName =='next_page_btn' :
            i=self.stackedWidget_2.currentIndex()
            print(i)
            self.stackedWidget_2.setCurrentIndex(i+1)


        if btnName =='prev_page_btn' :

            i=self.stackedWidget_2.currentIndex()
            print(i)
            self.stackedWidget_2.setCurrentIndex(i-1)

        if btnName =='btn_page0_1_top' :

            self.stackedWidget_2.setCurrentWidget(self.page_1_top)


        if btnName =='btn_page0_2_top' :

            self.stackedWidget_2.setCurrentWidget(self.page_2_top)


        if btnName =='btn_page0_1_side' :

            self.stackedWidget_2.setCurrentWidget(self.page_1_side)

        if btnName =='btn_page0_2_side' :

            self.stackedWidget_2.setCurrentWidget(self.page_2_side)    

        if btnName =='btn_page0_3_side' :

            self.stackedWidget_2.setCurrentWidget(self.page_3_side)    

        if btnName =='btn_page0_4_side' :

            self.stackedWidget_2.setCurrentWidget(self.page_4_side)


        if btnName =='btn_load_image0_1_top' :

            self.open_file_dialog(self.line_img_path0_1_top)
        
        if btnName =='btn_load_image0_1_side' :

            self.open_file_dialog(self.line_img_path0_1_side)
          
        if btnName =='set_top_image_btn' :
            pass

        if btnName=='btn_add_area0_2_top':
            self.frame_size(self.frame_53,50)

        if btnName=='btn_set_corner0_2_top':
            self.frame_size(self.groupBox_12,70)

        if btnName=='btn_draw_complete0_2_top':
            self.frame_size(self.frame_55,190)


        if btnName=='btn_add_area0_4_side':
            self.frame_size(self.frame_141,310)

        if btnName=='btn_complete_area_4_side':
            self.frame_size(self.frame_141,0)
   
        

    def check_mask_type(self,name,change_size=False):

        print('name',name)

        if name=='check_rect0_2_top':

            self.check_rect0_2_top.setChecked(True)
            self.check_circle0_2_top.setChecked(False)
            self.check_mask0_2_top.setChecked(False)

            self.selected_mask_type='rect'

        elif name=='check_circle0_2_top':

            self.check_rect0_2_top.setChecked(False)
            self.check_circle0_2_top.setChecked(True)
            self.check_mask0_2_top.setChecked(False)

            self.selected_mask_type='circle'

        elif name=='check_mask0_2_top':

            self.check_rect0_2_top.setChecked(False)
            self.check_circle0_2_top.setChecked(False)
            self.check_mask0_2_top.setChecked(True)

            self.selected_mask_type='poly'

        if change_size:
            self.frame_size(self.frame_54,50)


    def frame_size(self,f_name,size,both=True):


        height=f_name.height()

        if height!=size:
            f_name.setMaximumHeight(size)
            f_name.setMinimumHeight(size)


    


    def set_label(self,label_name,msg):
        msg = str( msg )
        label_name.setText(msg)
 
    def get_label(self,label_name):

        return label_name.text()


    def set_image_label(self,label_name, img):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        convert_to_Qt_format = sQImage(img.data, w, h, bytes_per_line, sQImage.Format_RGB888)


        label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))

    def set_image_page_tool_labels(self,img):


        self.set_image_label(self.label_image_grab_page,img)

        self.img_page_tool=img
    
    
    
    def clear_new_scew_line(self):
        self.line_new_screw.text = ''



    
    def get_line_scraw_name(self):
        return self.line_new_screw.text().strip().capitalize()




    def camera_select_radios_connect(self, func):
        self.connect_cam_top_btn.clicked.connect( func )
        self.connect_grab_side_camera.clicked.connect( func )


    def get_setting_page_idx(self,direction=False,page_name=False):

        if direction:
            
            idx=self.stackedWidget_2.currentIndex()
            
            
            return self.pages_dircetion_dict[str(idx)]
        
        if page_name:
            
            
            idx=self.stackedWidget_2.currentIndex()
            return self.pages_name_dict[str(idx)]
            
         
        else:
            return  self.stackedWidget_2.currentIndex()  
        
    def set_button_enable_or_disable(self, names, enable=True):

        print('all name',names)
        
        for name in names.values():
            print('name',name)
            name.setEnabled(enable)


    def enable_bar_btn_tool_page(self,enable=True,top=True,side=True):
        if top:
            self.set_button_enable_or_disable(self.tool_btn_bar_top,enable)
        if side:
            self.set_button_enable_or_disable(self.tool_btn_bar_side,enable)


    def get_activate_pages(self):

        for page_name in self.pages_name_dict.values():
            x=self.checkboxes['page']['checkbox_page0_{}'.format(page_name)].isChecked()
            print(self.checkboxes['page']['checkbox_page0_{}'.format(page_name)],x)


    #Combobox utils ----------------------------------------------------------------  
    def get_sub_page_name(self,page_name = None):

            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            combo_exist=self.combo_exist[page_name]  
            if combo_exist:
                print('exis')
                str=self.get_combobox_text('set_area')
                return str
            else:
                return None
                          
    def get_combobox_text(self,name, page_name = None, count=0):
            
            
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            try:
                combo_object=self.combo_boxes['{}'.format(name)]['combo_{}{}_{}'.format(name, count, page_name)]
                str=combo_object.currentText()

                return str
            except:
                return None
    def set_combobox_text(self,name,list_data, page_name = None ,count=0):
            
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            
            self.combo_boxes['{}'.format(name)]['combo_{}{}_{}'.format(name, count, page_name)].addItems(list_data)


    #Slider utils ----------------------------------------------------------------            
    def get_sliders_value(self,name, page_name = None, count=0):
            
            
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            
            x=self.sliders['{}'.format(name)]['bar_{}{}_{}'.format(name, count, page_name)].value()
            return x

    def set_sliders_value(self,name,value, page_name = None ,count=0):
            
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            
            self.sliders['{}'.format(name)]['bar_{}{}_{}'.format(name, count, page_name)].setValue(value)


    def connect_sliders(self,name,func):

        for obj_name in self.sliders[name]:
        
            self.sliders[name][obj_name].valueChanged.connect(func)

    #///////////////////////////////////////////////////////////////////////////// 
    #ROI utils -----------------------------------------------------------------------------------

    def set_roi_value(self,data, page_name = None):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
        
        # print('page_name:set',page_name,self.spins['roi'][0]['spin_roi_{}_{}'.format(0,page_name)])

        for roi_name in self.roi_name:
            
            try:
                obj = self.spins['roi'][roi_name]['spin_roi_{}_{}'.format(roi_name,page_name)]
                #obj.setUpdatesEnabled(False)
                obj.setValue(data[roi_name])
                #obj.setUpdatesEnabled(True)   
            except:
                pass

    def get_roi_value(self, page_name = None):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
        dict_values={}
        for roi_name in self.roi_name:
            
            try:
                value=self.spins['roi'][roi_name]['spin_roi_{}_{}'.format(roi_name,page_name)].value() 
                dict_values.update({roi_name:value})
            except:
                pass
        
        return dict_values
                

    def roi_connect(self,func):
        for page_name in self.pages_name_dict.values():

            for roi_name in self.roi_name:
            
                try:
                    
                    obj = self.spins['roi'][roi_name]['spin_roi_{}_{}'.format(roi_name,page_name)]
                    obj.valueChanged.connect(func('{}'.format(roi_name)))

                except:
                    pass
            
    
    #///////////////////////////////////////////////////////////////////////////// 
    #Limit Utils ---------------------------------------------

    def set_limit_value(self,data, name, page_name = None):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
        
        # print('page_name:set',page_name,self.spins['roi'][0]['spin_roi_{}_{}'.format(0,page_name)])

        for limit_name in self.limit_name:
            
            try:
                obj = self.spins['limit'][limit_name]['spin_{}_{}_{}'.format(limit_name,name, page_name)]
                obj.setValue(data[limit_name])   
            except:
                pass

    def get_limit_value(self,name,  page_name = None):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
        dict_values={}
        for limit_name in self.limit_name:
            
            try:
                value=self.spins['limit'][limit_name]['spin_{}_{}_{}'.format(limit_name,name, page_name)].value() 
                dict_values.update({limit_name:value})
            except:
                pass
        
        return dict_values
                


    # Spin Utils -------------------------------------------------
    def set_spins_value(self,data, name, page_name = None):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
        
        # print('page_name:set',page_name,self.spins['roi'][0]['spin_roi_{}_{}'.format(0,page_name)])

        # for limit_name in self.limit_name:
            
        try:
            obj = self.spins['spin_{}_{}'.format(name, page_name)]
            obj.setValue(data)   
        except:
            pass

    def get_limit_value(self,name,  page_name = None):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
        dict_values={}
        try:
            value=self.spins['spin_{}_{}'.format(name, page_name)].value() 
            dict_values.update({'value':value})
        except:
            pass
        
        return dict_values
                
   

    #//////////////////////////////////////////////////////////////////////////////////////////////
    #Checkbox utils -----------------------------------------------------------------------------------        
    def get_checkbox_value(self, name, page_name = None, idx=0):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
   

        obj = self.checkboxes[name]['btn_{}{}_{}'.format(name, idx, page_name)]
        return obj.isChecked()


    def set_checkbox_value(self, name, value:bool,  page_name = None, idx=0):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
   

        obj = self.checkboxes[name]['btn_{}{}_{}'.format(name, idx, page_name)]
        obj.setChecked( value )
        
        
    def checkbox_connect(self, name, func, idx=0):
        
        for page_name in self.pages_name_dict.values():

            try:
            
                obj = self.checkboxes[name]['btn_{}{}_{}'.format(name, idx, page_name)]
                
                obj.toggled.connect( func )
            except:
                pass

    #//////////////////////////////////////////////////////////////////////////////////////////////
    
    def set_line_value(self, name, value, page_name = None, idx=0):
            
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            
            obj = self.lines['{}'.format(name)]['line_{}{}_{}'.format(name, idx, page_name)]
            obj.setText(value)
    
    
    def get_line_value(self, name, page_name = None, idx=0):          
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            
            obj = self.lines['{}'.format(name)]['line_{}{}_{}'.format(name, idx, page_name)]
            return obj.text()
        
        
    
    def connect_line(self, name, func, idx=0):
        
        for page_name in self.pages_name_dict.values():
            obj = self.lines['{}'.format(name)]['line_{}{}_{}'.format(name, idx, page_name)]
            obj.textChanged.connect(func)
    

    #//////////////////////////////////////////////////////////////////////////////////////////////
    def connect_btn(self, name, func, idx=0):
        for page_name in self.pages_name_dict.values():
            try:
                obj = self.buttons[str(name)]['btn_{}{}_{}'.format(name, idx, page_name)]
                obj.clicked.connect( func )
            
            except:
                pass
            
    
    #//////////////////////////////////////////////////////////////////////////////////////////////
    def set_setting_page_parms(self, parms, page_name = None):
        
        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)

        for name, value in parms.items():
            if name in ['thresh', 'noise_filter']:
                self.set_sliders_value(name, value, page_name)
            if name in ['roi']:
                self.set_roi_value(Utils.rect_list2dict(value), page_name)
    
    
            if name in ['thresh_inv']:
                self.set_checkbox_value(name,value,page_name)
                
            
            if name in ['img_path']:
                self.set_line_value(name, value, page_name)
                
    

  

if __name__ == "__main__":
    app = QApplication()
    win = UI_main_window()
    # apply_stylesheet(app,theme='dark_cyan.xml')
    api = main_api.API(win)
    win.show()
    sys.exit(app.exec())
    