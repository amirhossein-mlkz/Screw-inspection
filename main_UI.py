# import os
# import PySide6

# dirname = os.path.dirname(PySide6.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

# from PySide6.QtWidgets import *

import sys
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

        # dashboard button ids
        # self.dash_buttons = [self.camera_setting_btn,self.calibration_setting_btn, self.plc_setting_btn\
        #                     , self.defect_setting_btn, self.users_setting_btn, self.level2_setting_btn\
        #                     ,self.general_setting_btn, self.storage_setting_btn]
        # side-bar button ids
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
        title = "SABA - settings"

        self.setWindowTitle(title)

        self.toogle_btn_1.clicked.connect(partial(self.leftmenu))
        self.toogle_btn_2.clicked.connect(partial(self.leftmenu))

        self.set_combo_boxes_2()

        self.camera_params = [self.gain_spinbox, self.expo_spinbox, self.width_spinbox\
                            , self.height_spinbox, self.offsetx_spinbox, self.offsety_spinbox\
                            ,self.trigger_combo, self.maxbuffer_spinbox, self.packetdelay_spinbox\
                                , self.packetsize_spinbox, self.transmissiondelay_spinbox, self.ip_lineedit, self.serial_number_combo, self.camera_setting_connect_btn]

        
        

        
        # SET LANGUAGE
        #//////////////////////////////////////////////
        # self.set_language()
        self.language = 'en'

        self._old_pos = None


        # Page Tool Image Labels
        # //////////////////////////
        self.image_labels={
            'page_grab':self.label_image_grab_page
        }        


        
        



    # def showPassword(self, show):
    #     echo=str(self.password.echoMode()).split(".", 4)[-1]


        

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



    # Label Dorsa
        # ///////////////////////////////////////////////     

    #///////////////////// LANGUAGE
    # def set_language(self):
    #     print(detect_lenguage.language())
    #     if detect_lenguage.language()=='Persian(فارسی)':
    #         detect_lenguage.main_window(self)
    
 
    # ///////////////////////////////////////////////     

    def leftmenu(self):


        width=self.leftMenuBg.width()
        # self.stackedWidget_defect.setCurrentWidget(self.page_no)
        # self.stackedWidget_defect.setMaximumHeight(60)
        # x=self.stackedWidget_defect.height()
        #print('height',height)
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
            # self.group.addAnimation(self.right_box)
            self.group.start()    
            #print('no ani')
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
            # self.group.addAnimation(self.right_box)
            self.group.start()    
            #print('no ani')
 


    def animation_move(self,label_name,lenght):

        width=label_name.width()
        # self.stackedWidget_defect.setCurrentWidget(self.page_no)
        # self.stackedWidget_defect.setMaximumHeight(60)
        # x=self.stackedWidget_defect.height()
        #print('height',height)
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
        # self.add_btn.clicked.connect(self.buttonClick)
        self.grab_load_btn.clicked.connect(self.buttonClick)
        self.tool1_btn.clicked.connect(self.buttonClick)
        self.tool2_btn.clicked.connect(self.buttonClick)
        self.tool3_btn.clicked.connect(self.buttonClick)
        self.next_page_btn.clicked.connect(self.buttonClick)
        self.prev_page_btn.clicked.connect(self.buttonClick)



        # Page grab select image

        self.load_image_btn.clicked.connect(self.buttonClick)
        self.set_image_btn.clicked.connect(self.buttonClick)


        self.camera1_select_radio.clicked.connect(self.check_camera_selected_direction)
        self.camera2_select_radio.clicked.connect(self.check_camera_selected_direction)




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


    def selected_camera(self,s):
        

        for i in range(1,25):
            if i<13:
                eval('self.camera%s_btn_2'%i).setIcon(QIcon('images/camtop.png'))
            else:
                eval('self.camera%s_btn_2'%i).setIcon(QIcon('images/cambtm.png'))

        cam_num=s

        if int(s)<13:
            eval('self.camera%s_btn_2'%cam_num).setIcon(QIcon('images/camtop_actived.png'))

        else :
            eval('self.camera%s_btn_2'%cam_num).setIcon(QIcon('images/cambtm_actived.png'))





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
        msg = QMessageBox.question(self, title, message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            return True
        if msg == QMessageBox.No:
            return False
        
        

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



    # Page Grab

    def get_parms_screw_page_grab(self):

        dic={}
        dic.update({'name':self.label_screw_name.text()})
        dic.update({'threshold':self.horizontalSlider_grab.value()})
        dic.update({'x1':self.spinBox_grab_page_x_rect1.value()})
        dic.update({'y1':self.spinBox_grab_page_y_rect1.value()})
        dic.update({'x2':self.spinBox_grab_page_x_rect2.value()})
        dic.update({'y2':self.spinBox_grab_page_y_rect2.value()})

        #print('dic',dic)

        return dic
    
    
    def set_roi_parms_screw_page_grab(self, data):
        self.spinBox_grab_page_x_rect1.setValue( data['x1'] )
        self.spinBox_grab_page_y_rect1.setValue( data['y1'] )
        self.spinBox_grab_page_x_rect2.setValue( data['x2'] )
        self.spinBox_grab_page_y_rect2.setValue( data['y2'] )
        #print('dic',dic)

    
    def roi_input_page_grab_connect(self,func):
        self.spinBox_grab_page_x_rect1.valueChanged.connect(func('x1'))
        self.spinBox_grab_page_y_rect1.valueChanged.connect(func('y1'))
        self.spinBox_grab_page_x_rect2.valueChanged.connect(func('x2'))
        self.spinBox_grab_page_y_rect2.valueChanged.connect(func('y2'))
        
    def  open_file_dialog(self,set_label):

        filepath = QFileDialog.getOpenFileName(self, 'Select a File')
        print(filepath)
        set_label.setText(filepath[0])


    def set_loaded_parms_page_grab(self,parms):        
        self.horizontalSlider_grab.setValue(int(parms['main_thresh']))
        self.line_image_address.setText(str(parms['img_path']))
        self.spinBox_grab_page_x_rect1.setValue( parms['main_roi'][0][0] )
        self.spinBox_grab_page_y_rect1.setValue( parms['main_roi'][0][1] )
        self.spinBox_grab_page_x_rect2.setValue( parms['main_roi'][1][0] )
        self.spinBox_grab_page_y_rect2.setValue( parms['main_roi'][1][1] )


    def check_camera_selected_direction(self):
        
        # checking if it is checked
        if self.camera1_select_radio.isChecked():
                
            # changing text of label
            # self.label.setText("It is now checked")
            self.camera1_select_radio.setChecked(True)
            #print('cam 1 select')
            self.selected_camera_name='camera1'
            return 'top'
        
        else:
            self.camera2_select_radio.setChecked(False)
            #print('cam 2 select')
            self.selected_camera_name='camera2'
            return 'side'









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

            self.animation_move(self.frame_24,300)

        if btnName =='add_btn' :

            self.animation_move(self.frame_23,300)

        if btnName =='save_new_btn' :

            self.animation_move(self.frame_23,300)
            self.stackedWidget_2.setCurrentIndex(1)

        if btnName =='edit_btn' :

            self.animation_move(self.frame_24,300)
            self.stackedWidget_2.setCurrentIndex(1)

        if btnName =='next_page_btn' :

            i=self.stackedWidget_2.currentIndex()
            print(i)
            self.stackedWidget_2.setCurrentIndex(i+1)


        if btnName =='prev_page_btn' :

            i=self.stackedWidget_2.currentIndex()
            print(i)
            self.stackedWidget_2.setCurrentIndex(i-1)


        if btnName =='grab_load_btn' :

            self.stackedWidget_2.setCurrentWidget(self.page)


        if btnName =='tool1_btn' :

            self.stackedWidget_2.setCurrentWidget(self.page_1)


        if btnName =='tool2_btn' :

            self.stackedWidget_2.setCurrentWidget(self.page_2)


        if btnName =='tool3_btn' :

            self.stackedWidget_2.setCurrentWidget(self.page_3)
                
        
        if btnName =='load_image_btn' :

            self.open_file_dialog(self.line_image_address)
          
        if btnName =='set_image_btn' :
            pass
            #self.set_image_label(self.label_3,cv2.imread(self.line_image_address.text()))              





        # if btnName =='camera1_btn_11':
        if btnName[:6] == 'camera' and btnName != 'camera_setting_btn':
            camera_id = btnName[6:8]
            #self.left_bar_clear()
            #self.Data_auquzation_btn.setStyleSheet("background-image: url(:/icons/images/icons/graber.png);background-color: rgb(212, 212, 212);color:rgp(0,0,0);")
            if not self.camera_setting_apply_btn.isEnabled() or (self.cameraname_label.text()!='No Camera Selected' and self.cameraname_label.text()[-2:]!=camera_id):
                
                self.cameraname_label.setText('Cam%s' % camera_id)
                #self.change_camera_btn_icon(camera_id, active=True)
                self.camera_setting_apply_btn.setEnabled(True)
                self.camera_setting_connect_btn.setStyleSheet("background-color:{}; border:Transparent".format(colors_pallete.successfull_green))
                self.set_button_enable_or_disable(self.camera_params, enable=True)
            else:
                self.disable_camera_settings()
                #self.change_camera_btn_icon(camera_id, active=False)

        

        
        
                

        
    def disable_camera_settings(self):
        self.cameraname_label.setText('No Camera Selected')
        self.camera_setting_apply_btn.setEnabled(False)
        self.camera_setting_connect_btn.setStyleSheet("background-color:{}; border:Transparent".format(colors_pallete.disabled_btn))
        self.set_button_enable_or_disable(self.camera_params, enable=False)
        

    
    def set_button_enable_or_disable(self, names, enable=True):
        
        for name in names:
            name.setEnabled(enable)


    def set_label(self,label_name,msg):
    
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

        list_image_labels=list(self.image_labels.values())
        for i in range(len(list_image_labels)):
            self.set_image_label(list_image_labels[i],img)




    def change_camera_btn_icon(self, camera_id, active=False):
        image_active_id = 'images/cambtm_actived.png' if int(camera_id)>12 else 'images/camtop_actived.png'    

        for cam_id in camera_funcs.all_camera_ids:
            image_deactive_id = 'images/cambtm.png' if int(cam_id)>12 else 'images/camtop.png'
            eval('self.camera%s_btn' % cam_id).setIcon(QIcon(image_deactive_id))
            
        if active:    
            eval('self.camera%s_btn' % camera_id).setIcon(QIcon(image_active_id))

    
    
    
    def clear_new_scew_line(self):
        self.line_new_screw.text = ''

    
        

    def get_screw_image_path(self):
        return self.line_image_address.text()

    
    def get_line_scraw_name(self):
        return self.line_new_screw.text().strip().capitalize()




    def camera_select_radios_connect(self, func):
        self.camera1_select_radio.clicked.connect( func )
        self.camera2_select_radio.clicked.connect( func )




if __name__ == "__main__":
    app = QApplication()
    win = UI_main_window()
    # apply_stylesheet(app,theme='dark_cyan.xml')
    api = main_api.API(win)
    win.show()
    sys.exit(app.exec())
    