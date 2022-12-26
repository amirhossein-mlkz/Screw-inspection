
import sys


from PyQt5.QtGui import * 

from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PyQt5.QtGui import QPainter

import numpy as np
import threading
import time
from PyQt5.QtGui import QPainter
import os

# from regex import F
import main_api
import cv2
from app_settings import Settings
from functools import partial

import numpy as np


import resources


from PySide6.QtGui import QImage as sQImage    # should change
from PySide6.QtGui import QPixmap as sQPixmap   # should change


import texts
from backend import Utils
import Keys

from history_UI import UI_history_window


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


        self.login_flag = True
        self.camera_connect_flag = True

        #   Define and set UI_KEYS

        Keys.object_dict_builder(self)


        self.side_buttons = [self.side_camera_setting_btn, self.side_tool_setting_btn\
                            ,self.side_users_setting_btn,self.side_general_setting_btn\
                                , self.side_dashboard_btn,self.side_calibration_setting_btn]

        # camera variable parameters ids in the camera-settings section of the UI 
        self.camera_params = [self.gain_spinbox, self.expo_spinbox, self.width_spinbox\
                            , self.height_spinbox, self.offsetx_spinbox, self.offsety_spinbox\
                            ,self.trigger_combo, self.maxbuffer_spinbox, self.packetdelay_spinbox\
                                , self.packetsize_spinbox, self.transmissiondelay_spinbox, self.ip_lineedit, self.serial_number_combo, self.camera_setting_connect_btn]
        

        self.dict_camera_params = {

                'serial_number': self.serial_number_combo,
                'trigger_mode':self.trigger_combo,
                'expo_value':self.expo_spinbox,
                'gain_value':self.gain_spinbox,
                'height':self.height_spinbox,
                'width':self.width_spinbox,
                'offsetx_value':self.offsetx_spinbox,
                'offsety_value':self.offsety_spinbox,
            # 'pxvalue_a':
            # 'pxvalue_b':
            # 'pxvalue_c':

        }


        self.main_login_btn.setIcon(sQPixmap.fromImage(sQImage('images/login_white.png')))
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Screw - Utils"

        self.setWindowTitle(title)

        self.toogle_btn_1.clicked.connect(partial(self.leftmenu))
        self.toogle_btn_2.clicked.connect(partial(self.leftmenu))

        self.set_combo_boxes_2()

        self.sides=['top','side']
        self.main_pages_name_dict=['page_dashboard',
                                    'page_tools',
                                    'page_camera_seting',
                                    'page_calibration',
                                    'page_users_setting',
                                    'page_settings'
                                    ]

        self.tool_pages_name_dict={'1':'1_top','2':'2_top','3':'3_top','4':'4_top','5':'5_top','6':'1_side','7':'2_side','8':'3_side','9':'4_side','10':'5_side','11':'6_side'}
        self.pages_dircetion_dict={'1':'top','2':'top','3':'top','4':'top','5':'top','6':'side','7':'side','8':'side','9':'side','10':'side','11':'side'}
        self.roi_name=['x1','y1','x2','y2']
        self.limit_types=['min','max']

        self.combo_exist={'1_top':False,'2_top':True,'3_top':True,'4_top':False,'5_top':True,'1_side':False,'2_side':False,'3_side':False,'4_side':True,'5_side':False,'6_side':True}

        
        self.tool_btn_bar_side={'lenght':self.frame_36,'btn_male':self.btn_page0_3_side,'Male_Thread':self.frame_78,'btn_lenght':self.btn_page0_2_side,'Diameter':self.frame_79,'screw_head':self.frame_104,'side_damage':self.frame_112,'side_btn_damage':self.btn_page0_6_side}
        self.tool_btn_bar_top={'area':self.frame_34,'measurment':self.frame_34,'btn_measurment':self.btn_page0_2_top,'defect_top':self.frame_53,'btn_defect_top':self.btn_page0_3_top,'edge_crack':self.frame_190,'btn_edge_crack':self.btn_page0_4_top,'btn_5_top':self.btn_page0_5_top,'btn_5_top2':self.frame_212}

        self.side_btn_stylesheet="QPushButton:enabled {background-color: rgb(255,255,255);color: black;}QPushButton:disabled{background-color:rgb(50,50,50);color: white;}"
        
        self.clear_side_btns(1)

        # self.get_sub_page_name()


        # self.enable_bar_btn_side()
        # self.enable_bar_btn_top()

        self.get_activate_pages(direction='side')
        # self.enable_bar_btn_tool_page('top',enable=False)
        # self.enable_bar_btn_tool_page('side',enable=False)
        # print('1')
        # self.enable_bar_btn_tool_page('side',enable=True)
        # print('2')
        
        # SET LANGUAGE
        #//////////////////////////////////////////////
        # self.set_language()
        self.language = 'en'
        self._old_pos = None
        self.editmode=False

        # Live page


        self.col_parms=['name','min','max','avg','limit_min','limit_max']
        self.set_header_live_table(self.table_live_top_live_page,self.col_parms)

        self.col_parms=['name','min','max','avg','limit_min','limit_max']
        self.set_header_live_table(self.table_live_side_live_page,self.col_parms)

        self.set_color_value_image_tool_page(value=50)


        self.img_top=cv2.imread('images/defualt.jpg')
        self.img_side=cv2.imread('images/defualt.jpg')



        self.set_list_pack_items('sub_pages', ['flanch', 'head'], page_name='5_top')

        # self.set_activate_pages('checkbox_page0_4_top',True)
        self.set_deactive_all_pages()


        #change_language

        self.combo_change_language.currentTextChanged.connect(self.change_language)

        # self.logger.create_new_log(message='UI object for train app created.')
        # self.load_lang()
        self.capture_mode_flag = 'general'
        
    def load_lang(self):
        # lan=api.load_language()
        self.set_language(self.language)

    def set_language(self,name):
        """set language
        Args:
            name (string): input language from api
        Returns: None
        """

        self.combo_change_language.setCurrentText(name)
        self.change_language()

    def change_language(self):
        """Change language in ui and update image
        Returns: None
        """
        if self.combo_change_language.currentText()=='English':
            self.language = 'en'
            # api.language = 'en'
            img_path=('images/english.png')


        else:
            self.language='fa'
            # api.language = 'fa'
            img_path=('images/persian.png')

        pixmap = QPixmap(img_path)
        self.label_language.setPixmap(pixmap)
        
        # self.set_image_label(self.label_language, img)
        # image = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)
        # self.label_language.setPixmap(QPixmap.fromImage(image))
        texts.set_title(self, self.language)
        # self.logger.create_new_log(message='cahange language.')


    


    # method called by timer
    def update_images(self):

        api.set_images()


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
        self.side_calibration_setting_btn.clicked.connect(self.buttonClick)

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
        self.btn_page0_3_top.clicked.connect(self.buttonClick)
        self.btn_page0_4_top.clicked.connect(self.buttonClick)
        self.btn_page0_5_top.clicked.connect(self.buttonClick)
        self.btn_page0_1_side.clicked.connect(self.buttonClick)
        self.btn_page0_2_side.clicked.connect(self.buttonClick)
        self.btn_page0_3_side.clicked.connect(self.buttonClick)
        self.btn_page0_4_side.clicked.connect(self.buttonClick)
        self.btn_page0_5_side.clicked.connect(self.buttonClick)
        self.btn_page0_6_side.clicked.connect(self.buttonClick)
        self.next_page_btn.clicked.connect(self.buttonClick)
        self.prev_page_btn.clicked.connect(self.buttonClick)



        # Page 1_top

        self.btn_load_image0_1_top.clicked.connect(self.buttonClick)
        self.btn_connect_camera0_1_top.clicked.connect(self.buttonClick)


        # page 2_top

        

        self.btn_add_region0_2_top.clicked.connect(self.buttonClick)
        self.btn_remove_region0_2_top.clicked.connect(self.buttonClick)

        # self.btn_set_corner0_2_top.clicked.connect(self.buttonClick)
        self.btn_draw_complete0_2_top.clicked.connect(self.buttonClick)

        # page 3_top

        self.btn_add_region0_3_top.clicked.connect(self.buttonClick)
        self.btn_remove_region0_3_top.clicked.connect(self.buttonClick)


        # page 1_side

        self.btn_load_image0_1_side.clicked.connect(self.buttonClick)  
        self.btn_connect_camera0_1_side.clicked.connect(self.buttonClick)



        # page 4_side  btn_add_area0_4_side

        self.btn_add_region0_4_side.clicked.connect(self.buttonClick)
        self.btn_remove_region0_4_side.clicked.connect(self.buttonClick)
        self.btn_complete_area_4_side.clicked.connect(self.buttonClick)

        # page 5_side

        #???????????????/
        #self.check_out0_5_side.clicked.connect(lambda:self.check_in_out(self.check_out0_5_side.objectName()))
        #self.check_in0_5_side.clicked.connect(lambda:self.check_in_out(self.check_in0_5_side.objectName()))


        # page 6_side  
        self.btn_add_region0_6_side.clicked.connect(self.buttonClick)      
        self.btn_remove_region0_6_side.clicked.connect(self.buttonClick)      
        self.btn_complete_area_6_side.clicked.connect(self.buttonClick)        

        # page_setting_camera
        self.ultra_setting_btn.clicked.connect(self.buttonClick)  
        self.camera_setting_tools_page.clicked.connect(self.buttonClick)  

        # page setting_main

        self.tool_btn_main_path.clicked.connect(self.buttonClick)  
        

    def close_win(self):

        ret = self.show_question('Warning',texts.WARNINGS['close_win'][self.language])
        if ret:
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

        string=['English', 'Persian']
        self.combo_change_language.addItems(string)

        camera_serials = ['20407477','0']
        self.serial_number_combo.addItems(camera_serials)


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

    # General settings

    def load_sizes(self,parms,side):

        print('parms',parms)

        for parms_key in parms.keys():
            if (parms_key=='x') or (parms_key=='y'):
                try:
                    obj = self.lines['size']['{}'.format(side)]['line_{}_cam_{}_resolution'.format(side, parms_key)]
                    obj.setText(parms[parms_key])
                except:
                    pass      #  line_top_live_min_x

    def get_sizes_parms(self):
        side_parms={}
        list=['x','y']
        # for side in self.sides:
        for _,line_name in enumerate(self.lines['size']['side']):
            print('line_name',line_name)
            text=eval('self.{}.text()'.format(line_name))
            side_parms.update({list[_]:text}) 

        top_parms={}
        for _,line_name in enumerate(self.lines['size']['top']):
            print('line_name',line_name)
            text=eval('self.{}.text()'.format(line_name))
            top_parms.update({list[_]:text}) 
        return side_parms,top_parms





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



          
    def  open_file_dialog(self,set_label,foldername=False):

        if foldername:
            filepath=QFileDialog.getExistingDirectory(self,"Choose Directory")
            # filepath = QFileDialog.get(self, 'Select a Folder')
            print(filepath)
            set_label.setText(filepath)

        else:
            filepath = QFileDialog.getOpenFileName(self, 'Select a File')
            print(filepath)
            set_label.setText(filepath[0])



    def clear_side_btns(self,current_page):

        self.white_side_images_path=['images/setting_main_window/dashboard_orange.png','images/setting_main_window/tools_setting_orange.png',\
            'images/setting_main_window/camera_setting_orange.png','images/setting_main_window/calibration_setting_orange.png','images/setting_main_window/users_setting_orange.png','images/setting_main_window/general_setting_orange.png']

        self.side_buttons = [ self.side_dashboard_btn, self.side_tool_setting_btn,self.side_camera_setting_btn\
                    ,self.side_calibration_setting_btn,self.side_users_setting_btn,self.side_general_setting_btn,]

        for i in range(len(self.side_buttons)):

            self.set_img_btns(self.side_buttons[i],self.white_side_images_path[i])

        # current_idx=self.stackedWidget.currentIndex()
        # print('current_idx',current_idx)
        # print('current_idx',current_idx,str(self.white_side_images_path[current_idx]).replace('_white',''))

        self.set_img_btns(self.side_buttons[current_page],self.white_side_images_path[current_page].replace('_orange','_white'))

    def edit_mode(self):
        if self.editmode==False:
            self.animation_move(self.frame_24,300)
            self.animation_move(self.frame_23,0)
            self.stackedWidget_2.setCurrentIndex(1)
            self.set_label(self.label_status_mode,texts.MESSEGES['Edit Mode'][self.language])
            self.editmode=True
            self.enable_bar_btn_tool_page('top',enable=True)
            self.enable_bar_btn_tool_page('side',enable=True)
            self.frame_size(self.frame_save_btns,57)
            #self.tool_btn_clear() #useless
            screw=[]
            screw.append(self.comboBox_edit_remove.currentText())  
            self.set_combo_boxes(self.comboBox_edit_remove,screw)
            # self.set_button_enable_or_disable(self.comboBox_edit_remove,enable=False)
            self.change_mode()


    def change_mode(self):
        
        if self.editmode:
            value=False
        else:
            value=True
            
        self.edit_btn.setEnabled(value)
        self.remove_screw_btn.setEnabled(value)
        self.add_btn.setEnabled(value)
        self.edit_remove_btn.setEnabled(value)
        # self.remove_screw_btn.setEnabled(value)
        
        self.btn_page0_1_top.setEnabled(not(value))
        self.btn_page0_1_side.setEnabled(not(value))
        

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()



        if btnName =='side_camera_setting_btn' and self.stackedWidget.currentWidget()!=self.page_camera_setting:

            self.clear_side_btns(current_page=2)

            self.stackedWidget.setCurrentWidget(self.page_camera_setting)
            self.frame_size_width(self.frame_210,100000,width=True,max_width=True)
            self.frame_size_width(self.frame_209,100000,width=True,max_width=True)
            self.frame_size(self.camera_setting_tools_page,0)


            self.capture_mode_flag = 'general'
            self.line_path_top_cam_live_page_2.setEnabled(True)

        
        if btnName =='side_dashboard_btn' and self.stackedWidget.currentWidget()!=self.page_dashboard:
            self.clear_side_btns(current_page=0)

            self.stackedWidget.setCurrentWidget(self.page_dashboard)

        if btnName =='side_users_setting_btn' :

            self.clear_side_btns(current_page=4)


            self.stackedWidget.setCurrentWidget(self.page_users_setting)


        if btnName =='side_tool_setting_btn' :
            self.clear_side_btns(current_page=1)


            self.stackedWidget.setCurrentWidget(self.page_tools)

        
        if btnName =='side_general_setting_btn' :
            self.clear_side_btns(current_page=5)

            self.stackedWidget.setCurrentWidget(self.page_settings)


        
        if btnName =='side_calibration_setting_btn' :
            self.clear_side_btns(current_page=3)

            self.stackedWidget.setCurrentWidget(self.page_calibration)



        if btnName =='edit_remove_btn' :
            if self.editmode==False:
                self.animation_move(self.frame_24,300)
                self.enable_bar_btn_tool_page(False)
                #self.tool_btn_clear() #useless
                # self.editmode=True
            else :
                self.set_warning(texts.WARNINGS['EDIT_MODE'][self.language],'tool_page',level=2)
        if btnName =='add_btn' :

            if self.editmode==False:

                self.animation_move(self.frame_23,300)
            
            else :
                self.set_warning(texts.WARNINGS['EDIT_MODE'][self.language],'tool_page',level=2)


        if btnName =='camera01_btn':
            self.set_label(self.cameraname_label,'Top')
            print('adswd',cv2.imread('images/camtop_actived.png'))
            self.change_btn_icon(self.camera01_btn,'images/camtop_actived.png')
            self.change_btn_icon(self.camera02_btn,'images/camside.png')

        if btnName =='camera02_btn':
            self.set_label(self.cameraname_label,'Side')
            self.change_btn_icon(self.camera02_btn,'images/camside_actived.png')
            self.change_btn_icon(self.camera01_btn,'images/camtop.png')

        if btnName =='save_new_btn' :

            self.animation_move(self.frame_23,300)
            

        if btnName =='edit_btn' :
            # if self.
            print('editmode',self.editmode)
            # self.edit_mode()


        if btnName =='next_page_btn' :
            if self.editmode:
                i=self.stackedWidget_2.currentIndex()
                self.stackedWidget_2.setCurrentIndex(i+1)


        if btnName =='prev_page_btn' :

            if self.editmode:

                i=self.stackedWidget_2.currentIndex()
                print(i)
                self.stackedWidget_2.setCurrentIndex(i-1)

        if btnName =='btn_page0_1_top' :
            #self.tool_btn_clear() #useless

            self.stackedWidget_2.setCurrentWidget(self.page_1_top)
            # self.btn_page0_1_top.setStyleSheet(self.side_btn_stylesheet)



        if btnName =='btn_page0_2_top' :
            #self.tool_btn_clear() #useless

            self.stackedWidget_2.setCurrentWidget(self.page_2_top)
            # self.btn_page0_2_top.setStyleSheet(self.side_btn_stylesheet)

        if btnName =='btn_page0_3_top' :
            #self.tool_btn_clear() #useless

            self.stackedWidget_2.setCurrentWidget(self.page_3_top)
            self.btn_page0_3_top.setStyleSheet(self.side_btn_stylesheet)

        if btnName =='btn_page0_4_top' :
            #self.tool_btn_clear() #useless

            self.stackedWidget_2.setCurrentWidget(self.page_4_top)
            self.btn_page0_4_top.setStyleSheet(self.side_btn_stylesheet)


        if btnName =='btn_page0_5_top' :
            #self.tool_btn_clear() #useless

            self.stackedWidget_2.setCurrentWidget(self.page_5_top)
            self.btn_page0_5_top.setStyleSheet(self.side_btn_stylesheet)


        if btnName =='btn_page0_1_side' :
            #self.tool_btn_clear() #useless

            self.stackedWidget_2.setCurrentWidget(self.page_1_side)
            self.btn_page0_1_side.setStyleSheet(self.side_btn_stylesheet)

        if btnName =='btn_page0_2_side' :
            #self.tool_btn_clear() #useless

            self.stackedWidget_2.setCurrentWidget(self.page_2_side)    
            self.btn_page0_2_side.setStyleSheet(self.side_btn_stylesheet)

        if btnName =='btn_page0_3_side' :
            #self.tool_btn_clear() #useless

            self.stackedWidget_2.setCurrentWidget(self.page_3_side)    
            self.btn_page0_3_side.setStyleSheet(self.side_btn_stylesheet)

        if btnName =='btn_page0_4_side' :
            #self.tool_btn_clear() #useless

            self.stackedWidget_2.setCurrentWidget(self.page_4_side)
            self.btn_page0_4_side.setStyleSheet(self.side_btn_stylesheet)

        if btnName =='btn_page0_5_side' :
            #self.tool_btn_clear() #useless

            self.stackedWidget_2.setCurrentWidget(self.page_5_side)
            self.btn_page0_5_side.setStyleSheet(self.side_btn_stylesheet)

        if btnName =='btn_page0_6_side' :
            #self.tool_btn_clear() #useless
            self.stackedWidget_2.setCurrentWidget(self.page_6_side)
            self.btn_page0_6_side.setStyleSheet(self.side_btn_stylesheet)

        if btnName =='btn_load_image0_1_top' :

            self.open_file_dialog(self.line_img_path0_1_top)
        
        if btnName =='btn_load_image0_1_side' :

            self.open_file_dialog(self.line_img_path0_1_side)
          
        if btnName =='set_top_image_btn' :
            pass

        if btnName=='btn_add_region0_2_top':
            self.frame_size(self.frame_52,1000)

        if btnName=='btn_remove_region0_2_top':
            self.frame_size(self.frame_52,0)

        if btnName=='btn_add_region0_3_top':
            self.frame_size(self.frame_193,1000)

        if btnName=='btn_remove_region0_3_top':
            self.frame_size(self.frame_193,0)

        if btnName=='btn_add_region0_4_side':
            self.frame_size(self.frame_141,310)

        if btnName=='btn_remove_region0_4_side':
            self.frame_size(self.frame_141,0)
      

        # if btnName=='btn_set_corner0_2_top':
        #     self.frame_size(self.groupBox_12,70)

        if btnName=='btn_draw_complete0_2_top':
            self.frame_size(self.frame_52,0)


        if btnName=='btn_add_area0_4_side':
            # print('asdawdwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
            self.frame_size(self.frame_141,310)


        if btnName=='btn_complete_area_4_side':
            self.frame_size(self.frame_141,0)

        if btnName=='btn_add_region0_6_side':
            self.frame_size(self.frame_143,310)

        if btnName=='btn_remove_region0_6_side':
            self.frame_size(self.frame_143,0)

        if btnName=='btn_complete_area_6_side':
            self.frame_size(self.frame_143,0)   

        if btnName=='ultra_setting_btn':
            print('ultra',self.frame_10.height())
            if self.frame_10.height()==0:
                self.frame_size(self.frame_10,460)   
            else:
                self.frame_size(self.frame_10,0)  

        if btnName=='btn_connect_camera0_1_top':
            self.clear_side_btns(current_page=2)

            self.stackedWidget.setCurrentWidget(self.page_camera_setting)

            self.frame_size_width(self.frame_210,0,width=True,both_width=True)
            self.frame_size_width(self.frame_209,5000,width=True,max_width=True)
            self.frame_size(self.camera_setting_tools_page,30)
            self.line_path_top_cam_live_page_2.setText(self.label_screw_name.text())

            self.capture_mode_flag = 'edit_page'
            self.line_path_top_cam_live_page_2.setEnabled(False)

        if btnName=='btn_connect_camera0_1_side':
            self.clear_side_btns(current_page=2)

            self.stackedWidget.setCurrentWidget(self.page_camera_setting)

            self.frame_size_width(self.frame_209,0,width=True,both_width=True)
            self.frame_size_width(self.frame_210,100000,width=True,max_width=True)
            self.frame_size(self.camera_setting_tools_page,30)

            self.line_path_top_cam_live_page_2.setText(self.label_screw_name.text())

            self.capture_mode_flag = 'edit_page'
            self.line_path_top_cam_live_page_2.setEnabled(False)


        if btnName=='camera_setting_tools_page':

            self.clear_side_btns(current_page=1)
            self.stackedWidget.setCurrentWidget(self.page_tools)

        if btnName=='tool_btn_main_path':
            self.open_file_dialog(self.line_main_path,foldername=True)


    def tool_btn_clear(self):

        for i in (self.combo_exist):
            try:
                obj_name=eval('self.btn_page0_{}'.format(i))
                # obj_name.setStyleSheet("QPushButton:disabled{background-color:rgb(50,50,50);}")
            except:
                pass



    def frame_size(self,f_name,size,both=True):


        height=f_name.height()

        if height!=size:
            f_name.setMaximumHeight(size)
            f_name.setMinimumHeight(size)
    def frame_size_width(self,f_name,size,width=False,both_width=False,min_width=False,max_width=False):
        if width:
            width=f_name.width()
            if both_width:
                f_name.setMaximumWidth(size)
                f_name.setMinimumWidth(size)        
            elif max_width:
                f_name.setMaximumWidth(size)
            elif min_width:
                f_name.setMinimumWidth(size)





    


    def set_label(self,label_name,msg,color=False):
        msg = str( msg )
        label_name.setText(msg)

        if color:
            label_name.setStyleSheet("color:{}".format(color))
 
    def get_label(self,label_name):

        return label_name.text()


    def clear_image_label(self,label_name):
        label_name.clear()


    def set_image_label(self,label_name, img, height_percent=None, width_percent=None):

        page_name = self.get_main_page_idx(page_name=True)

        max_h, max_w = None, None
        if height_percent is None or width_percent is None:
            if page_name in self.scales.keys():
                height_percent, width_percent = self.scales[page_name]
                win_h, win_w = self.app_size()
                max_h = int( win_h * height_percent )
                max_w = int( win_w * width_percent )
        
        if max_h is not None and max_w is not None:
            try:
                h, w, ch = img.shape
            except:
                h,w = img.shape
                ch=3
            scale_h = max_h/h
            scale_w = max_w/w
            scale = min( scale_h, scale_w)
            img = cv2.resize(img, None, fx=scale, fy=scale)

        try:
            h, w, ch = img.shape
        except:
            h,w = img.shape
            ch = 3
        bytes_per_line = ch * w  
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        convert_to_Qt_format = sQImage(img.data, w, h, bytes_per_line, sQImage.Format_RGB888)

        label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))
        


    def change_btn_icon(self, btn, image):
        icon = QIcon()
        icon.addPixmap(QPixmap(image), QIcon.Normal, QIcon.On)
        btn.setIcon(icon)




    def set_image_page_tool_labels(self,img):
        self.set_image_label(self.label_image_grab_page,img)
        self.img_page_tool=img
    

    def clear_image_page_tool_labels(self):
        self.clear_image_label(self.label_image_grab_page)
        #self.img_page_tool=img


    def set_img_btns(self,btn_name,img_path):
        btn_name.setIcon(sQPixmap.fromImage(sQImage('{}'.format(img_path))))
    
    def clear_new_scew_line(self):
        self.line_new_screw.text = ''



    
    def get_line_scraw_name(self):
        return self.line_new_screw.text().strip().capitalize()


    def clear_line_scraw_name(self):
        self.line_new_screw.setText('')


    def camera_select_radios_connect(self, func):
        self.connect_cam_top_btn.clicked.connect( func )
        self.connect_grab_side_camera.clicked.connect( func )


    def get_setting_page_idx(self,direction=False,page_name=False):
        
        idx = self.stackedWidget_2.currentIndex()  
        if direction:
            return self.pages_dircetion_dict[str(idx)]
        
        if page_name:
            return self.tool_pages_name_dict[str(idx)]
            
         
        else:
            return idx
        

    def get_main_page_idx(self,direction=False,page_name=False):
        
        idx = self.stackedWidget.currentIndex()  
        if direction:
            return self.main_pages_name_dict[idx]
        
        if page_name:
            return self.main_pages_name_dict[idx]
            
         
        else:
            return idx

    def set_button_enable_or_disable(self, names, enable=True):
        for name in names.values():
            name.setEnabled(enable)


    def enable_bar_btn_tool_page(self,direction, enable=True ):
        if direction == 'top':
            self.set_button_enable_or_disable(self.tool_btn_bar_top,enable)
        if direction == 'side':
            self.set_button_enable_or_disable(self.tool_btn_bar_side,enable)


    def get_activate_pages(self,direction):

        checked_btns=[]

        for page_name in self.tool_pages_name_dict.values():
            x=self.checkboxes['page']['checkbox_page0_{}'.format(page_name)].isChecked()
            if x:
                if direction in page_name:
                    checked_btns.append(page_name)
        return checked_btns

    def set_activate_pages(self,list,bool):
        for name in list:
            check_box=self.checkboxes['page']['checkbox_page0_{}'.format(name)]
            check_box.setChecked(bool)

    def set_deactive_all_pages(self):

        for page_name in self.tool_pages_name_dict.values():
            check_box=self.checkboxes['page']['checkbox_page0_{}'.format(page_name)]
            check_box.setChecked(False)


    #Combobox utils ----------------------------------------------------------------  
    def get_sub_page_name(self,page_name = None):
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            combo_exist=self.combo_exist[page_name]  
            if combo_exist:
                if self.get_selected_list_pack_count('sub_pages') == 0:
                    return 'none'
                return self.get_selected_list_pack_item('sub_pages')
            else:
                return None
                          
    def get_combobox_text(self,name, page_name = None, idx=0):
            
            
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            try:
                combo_object=self.combo_boxes['{}'.format(name)]['combo_{}{}_{}'.format(name, idx, page_name)]
                str=combo_object.currentText()

                return str
            except:
                return None
    def set_combobox_text(self,name,list_data, page_name = None ,idx=0):
            
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            
            self.combo_boxes['{}'.format(name)]['combo_{}{}_{}'.format(name, idx, page_name)].addItems(list_data)


    #-----------------------------------------------------------------------------
    def get_selected_list_pack_item(self, name, page_name=None, idx=0):
        if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
        return self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['combo'].currentText()
    
    def set_selected_list_pack_item(self, name, item, page_name=None, idx=0):
        if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
        return self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['combo'].setCurrentText(str(item))
    
    def get_selected_list_pack_count(self, name, page_name=None, idx=0):
        if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
        return self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['combo'].count()
    

    def set_list_pack_items(self, name, items, page_name=None, idx=0):
        if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
        self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['combo'].blockSignals(True)
        self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['combo'].clear()
        self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['combo'].addItems(items)
        self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['combo'].blockSignals(False)
        
    def get_list_pack_input(self, name, page_name=None, idx=0):
        if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
        
        return self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['input'].text().lower()
        
    
    def set_list_pack_input(self, name, text, page_name=None, idx=0):
        if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
        
        return self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['input'].setText(text)
    
    
    
    def connect_list_pack(self, name, func, idx=0):
        
        for page_name in self.tool_pages_name_dict.values():
            
            try:
                self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['add_btn'].clicked.connect(func('add'))
                self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['remove_btn'].clicked.connect(func('remove'))
            except:
                pass

            try:
                self.list_packs['lp_{}{}_{}'.format( name, idx, page_name )]['combo'].currentTextChanged.connect(func('select'))
            except:
                pass
    
    
    #info labels ----------------------------------------------------------------            
    def set_stetting_page_label_info(self, data, page_name = None):
        if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
        
        for name, value in data.items():
            obj = self.labels['show_infoes'][page_name][ 'label_{}_{}'.format(name, page_name) ]
            obj.setText( str(value) )
    
    #Slider utils ----------------------------------------------------------------            
    def get_sliders_value(self,name, page_name = None, idx=0):
            
            
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            
            x=self.sliders['{}'.format(name)]['bar_{}{}_{}'.format(name, idx, page_name)].value()
            return x

    def set_sliders_value(self,name,value, page_name = None ,idx=0):
            
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            
            obj = self.sliders['{}'.format(name)]['bar_{}{}_{}'.format(name, idx, page_name)]
            #obj.blockSignals(True)
            obj.setValue(value)
            #obj.blockSignals(False)


    def set_sliders_defualt(self, name, value=0):
        for name,obj in self.sliders[name]:
            obj.setValue(value)


    def connect_sliders(self,name,func):
        # self.connect_slider_ui()

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
                obj.blockSignals(True)
                obj.setValue(data[roi_name])
                obj.blockSignals(False)
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
        for page_name in self.tool_pages_name_dict.values():

            for roi_name in self.roi_name:
            
                try:
                    
                    obj = self.spins['roi'][roi_name]['spin_roi_{}_{}'.format(roi_name,page_name)]
                    obj.valueChanged.connect(func('{}'.format(roi_name)))

                except:
                    pass
            
    
    #///////////////////////////////////////////////////////////////////////////// 
    #Limit Utils ---------------------------------------------

    def set_limit_value(self,data, page_name = None):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
        
        # print('page_name:set',page_name,self.spins['roi'][0]['spin_roi_{}_{}'.format(0,page_name)])
        for limit_type in data.keys():
            for name, value in data[limit_type].items():    
                try:
                    obj = self.spins['limit'][limit_type][page_name]['spin_{}_{}_{}'.format(limit_type,name, page_name)]
                    obj.blockSignals(True)
                    obj.setValue( value )   
                    obj.blockSignals(False)
                except:
                    pass
            
            
            
            
    def get_limit_value(self, page_name = None):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
        
        dict_values = {}
        for limit_type in self.limit_types:
            dict_values.update( { limit_type : {} } )
            for name, obj in self.spins['limit'][limit_type][page_name].items():
                try:
                    name = name[ len( 'spin_' + limit_type + '_' ) : ] #spin_min_lenght_2_side -> lenght_2_side
                    name = name[ : name.rfind(page_name) - 1 ] #lenght_2_side -> lenght ( -1 is for '_' after name )
                    value = obj.value()
                    dict_values[limit_type].update( {name:value} )
                except:
                    pass
        
        return dict_values
    
    
    
    def connect_limit_spin(self, func):
        
        for limit_type in self.limit_types:
            for page_name in self.spins['limit'][limit_type].keys():
                for name, obj in self.spins['limit'][limit_type][page_name].items():
                    #spin_min_lenght_2_side
                    try:
                        name = name[ len( 'spin_' + limit_type + '_' ) : ] #spin_min_lenght_2_side -> lenght_2_side
                        name = name[ : name.rfind(page_name) - 1 ] #lenght_2_side -> lenght ( -1 is for '_' after name )
                        obj.valueChanged.connect(func( limit_type, name ))
                    except:
                        pass

                


    # Spin Utils -------------------------------------------------
    def set_spins_parms_value(self, name, value, page_name = None):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
        try:
            obj = self.spins['parms'][page_name]['spin_{}_{}'.format(name, page_name)]
            obj.blockSignals(True)
            obj.setValue(value)   
            obj.blockSignals(False)
        except:
            pass
                

    def get_spins_parms_value(self, name, page_name = None):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
        try:
            obj = self.spins['parms'][page_name]['spin_{}_{}'.format(name, page_name)]
            return obj.value()   
        except:
            return 0


    def connect_spins_parm(self, func):
        for page_name in self.spins['parms'].keys():
            for name, obj in self.spins['parms'][page_name].items():
                try:
                    name = name[ len( 'spin_') : ] #spin_jump_thresh_5_side -> jump_thresh_5_side
                    name = name[ : name.rfind(page_name) - 1 ] #jump_thresh_5_side -> jump_thresh ( -1 is for '_' after name )
                    obj.valueChanged.connect(func( name ))
                except:
                    pass




    #Checkbox utils -----------------------------------------------------------------------------------        
    def check_in_out(self,name):
        if name=='check_out0_5_side':

            self.check_out0_5_side.setChecked(True)
            self.check_in0_5_side.setChecked(False)

            self.selected_area='out'

        elif name=='check_in0_5_side':

            self.check_rect0_2_top.setChecked(False)
            self.check_in0_5_side.setChecked(True)
            self.check_out0_5_side.setChecked(False)

            self.selected_area='in'

        return self.selected_area
    #//////////////////////////////////////////////////////////////////////////////////////////////
    #Checkbox utils -----------------------------------------------------------------------------------        
    def get_checkbox_value(self, name, page_name = None, idx=0):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
   
        if name in ['thresh_inv', 'page']:
            obj = self.checkboxes[name]['checkbox_{}{}_{}'.format(name, idx, page_name)]
        else:
            obj = self.checkboxes['other'][page_name]['checkbox_{}_{}'.format(name, page_name)]
        return obj.isChecked()


    def set_checkbox_value(self, name, value:bool,  page_name = None, idx=0):

        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)
   
        if name in ['thresh_inv', 'page']:
            obj = self.checkboxes[name]['checkbox_{}{}_{}'.format(name, idx, page_name)]
        else:
            obj = self.checkboxes['other'][page_name]['checkbox_{}_{}'.format(name, page_name)]
        
        obj.blockSignals(True)
        obj.setChecked( value )
        obj.blockSignals(False)
        
        
    def checkbox_connect(self, name, func, idx=0):
        if name == 'other':
            for page_name in self.checkboxes['other'].keys():
                for obj_name,obj in self.checkboxes['other'][page_name].items():
                    name = obj_name[ len( 'checkbox_') : ] #spin_jump_thresh_5_side -> jump_thresh_5_side
                    name = name[ : name.rfind(page_name) - 1 ] #jump_thresh_5_side -> jump_thresh ( -1 is for '_' after name )
                    obj.toggled.connect(func( name )) 

        else:
            for page_name in self.tool_pages_name_dict.values():

                try:
                
                    obj = self.checkboxes[name]['checkbox_{}{}_{}'.format(name, idx, page_name)]
                    
                    obj.toggled.connect( func(name) )
                except:
                    pass

    #//////////////////////////////////////////////////////////////////////////////////////////////
    
    def set_line_value(self, name, value, page_name = None, idx=0):
            
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            
            obj = self.lines['{}'.format(name)]['line_{}{}_{}'.format(name, idx, page_name)]
            obj.blockSignals(True)
            obj.setText(value)
            obj.blockSignals(False)
    
    
    def get_line_value(self, name, page_name = None, idx=0):          
            if page_name is None:
                page_name =self.get_setting_page_idx(page_name=True)
            
            obj = self.lines['{}'.format(name)]['line_{}{}_{}'.format(name, idx, page_name)]
            return obj.text()
        
        
    
    def connect_line(self, name, func, idx=0):
        
        for page_name in self.tool_pages_name_dict.values():
            obj = self.lines['{}'.format(name)]['line_{}{}_{}'.format(name, idx, page_name)]
            obj.textChanged.connect(func)
    
    #//////////////////////////////////////////////////////////////////////////////////////////////
    def set_multi_options_value(self, group_name, option_name, change_size=False, page_name=None):
        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)

        for name, obj in self.multi_options[ page_name ][ group_name ]['options'].items():
            if name == option_name:
                obj.blockSignals(True)
                obj.setChecked( True )
                obj.blockSignals(False)
            else:
                obj.blockSignals(True)
                obj.setChecked( False )
                obj.blockSignals(False)

        if change_size:
            obj = self.multi_options[ page_name ][ group_name ]['frame']['obj']
            size_ = self.multi_options[ page_name ][ group_name ]['frame']['size']
            self.frame_size( obj, size_)


    def get_multi_options_value(self, name, option_name, page_name=None):
        if page_name is None:
            page_name =self.get_setting_page_idx(page_name=True)

        for name, obj in self.multi_options[ page_name ][ option_name ]['options'].items():
            if obj.isChecked():
                return name


    def connect_multi_options(self, func ):
        
        for page_name in self.multi_options.keys():
            for option_name in self.multi_options[ page_name ].keys():
                for name, obj in self.multi_options[ page_name ][ option_name ]['options'].items():
                    obj.clicked.connect( func(option_name, name) )



    # def check_mask_type(self,name,change_size=False):

    #     print('name',name)

    #     if name=='check_rect0_2_top':

    #         self.check_rect0_2_top.setChecked(True)
    #         self.check_circle0_2_top.setChecked(False)
    #         self.check_mask0_2_top.setChecked(False)

    #         self.stackedWidget_3.setCurrentIndex(1)


    #         self.selected_mask_type='rect'

    #     elif name=='check_circle0_2_top':

    #         self.check_rect0_2_top.setChecked(False)
    #         self.check_circle0_2_top.setChecked(True)
    #         self.check_mask0_2_top.setChecked(False)
    #         self.stackedWidget_3.setCurrentIndex(0)

    #         self.selected_mask_type='circle'
    #         print('0'*30)

    #     elif name=='check_mask0_2_top':

    #         self.check_rect0_2_top.setChecked(False)
    #         self.check_circle0_2_top.setChecked(False)
    #         self.check_mask0_2_top.setChecked(True)
    #         self.stackedWidget_3.setCurrentIndex(1)

    #         self.selected_mask_type='poly'

    #     if change_size:
    #         self.frame_size(self.frame_54,50)

    #//////////////////////////////////////////////////////////////////////////////////////////////
    def connect_btn(self, name, func, idx=0):
        for page_name in self.tool_pages_name_dict.values():
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
            name, idx = self.deasmble_name_and_idx( name )
            if name in ['thresh_inv', 'navel'] :
                self.set_checkbox_value(name,value,page_name,idx=idx)
                
            elif name in ['thresh', 'noise_filter'] :
                self.set_sliders_value(name, value, page_name, idx=idx)
                
            elif name in  ['img_path'] :
                self.set_line_value(name, value, page_name,idx=idx)

            elif name in ['jump_thresh', 'min_area', 'max_area']:
                self.set_spins_parms_value(name, value)
                
            elif 'roi' in name:
                self.set_roi_value(Utils.rect_list2dict(value), page_name)
            
            elif 'limit' in name:
                self.set_limit_value(value, page_name)

            elif 'shape_type' in name:
                self.set_multi_options_value( name, value )



            
            
                
    
    
    
    def deasmble_name_and_idx(self,inpt):
        for i in range(len(inpt)):
            if inpt[i] in '0123456789':
                break
            
            if i == (len(inpt) - 1):
                return inpt,0
        return inpt[:i] , inpt[i:]
  
    def set_header_live_table(self,table_name,headers):
        table_name.setHorizontalHeaderLabels(headers)
        table_name.setRowCount(0)
        table_name.verticalHeader().setVisible(True)
        table_name.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def clear_table(self,table_name):
        """Clear table of selected Images in Data aquization page
        """
        for i in range(table_name.rowCount()):
            table_name.removeRow(0)

    def set_live_table(self,table_name,values=False):
        self.clear_table(table_name)
        table_item = QTableWidgetItem()
        str1=[]
        if values:
            table_name.setRowCount(len(values))
            for id,page_value in enumerate(values):
                limit_min=page_value['limit_min']
                limit_max=page_value['limit_max']
                for col_id , col_value in enumerate(self.col_parms) :
                    table_item = QTableWidgetItem(str(page_value[col_value]))
                    table_name.setItem(id,col_id,table_item)
                    if col_id==0:
                        table_item.setBackground(QBrush(QColor("#17202A")))

                        # self.set_color_table_name_col(table_item,page_value[col_value],limit_min,limit_max)
                    else:
                        self.set_color_table(table_item,page_value[col_value],limit_min,limit_max)
                    if col_id==4 or col_id==5:
                        table_item.setBackground(QBrush(QColor("#808080")))    
                    if page_value[col_value]==-1 or page_value[col_value]==-2:
                        table_item.setBackground(QBrush(QColor("#D4AC0D")))

        table_name.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            # table_name.item(1, 1).setText("Put here whatever you want!")

    def set_color_table(self,table_item,value=0,limit_min=0,limit_max=0):
        # print('limit_min , max',value,limit_min,limit_max)
        if value<limit_min or value>limit_max:
            # print('min')
            table_item.setBackground(QBrush(QColor("#E74C3C")))
        else:
            # print('else')
            table_item.setBackground(QColor('#239B56'))                       


    def set_selected_image_live_page(self,direction,img):

        self.set_image_label(self.lives['labels']['selected_img'][direction],img)


    def set_main_image_live_page(self,direction,img):

        self.set_image_label(self.lives['labels']['live_img'][direction],img)

        
    def get_plc_ip(self):
        return self.plc_ip_line.text()



    def set_color_value_image_tool_page(self,value=False,img=None):
        if value:
            self.set_label(self.label_color_value,value)
        if img is not None:
            self.set_image_label(self.img_color_value,img)


    def update_mouse_position_tool_page(self,pts):
        self.set_label(self.label_x_pos_tool_page,pts[0])
        self.set_label(self.label_y_pos_tool_page,pts[1])


    def is_drawing_mask_enabel(self):
        return self.btn_enabel_mask_draw.isChecked()




    def get_plc_parms(self):

        limit_1=self.line_run_plc.text()
        limit_2=self.line_stop_plc.text()
        line_down_motor_plc=self.line_reject_plc.text()
        spare_plc=self.line_spare_plc.text()
        # line_spare_plc=self.line_spare_plc.text()
        # line_detect_sensor_plc=self.line_detect_sensor_plc.text()
        delay_plc=str(self.spin_delay_plc.value())
        duration_plc=str(self.spin_duration_plc.value())
    
        return{'run_plc':limit_1,'stop_plc':limit_2,'reject_plc':line_down_motor_plc,\
            'delay_plc':delay_plc,'duration_plc':duration_plc,'spare_plc':spare_plc}











    def set_tools_defualt(self):
        self.set_sliders_defualt('thresh', 0)
        self.set_sliders_defualt('noise_filter', 0)
    

    def set_calibration(self,top_calibration=False,side_calibration=False):

        if top_calibration:
            self.label_top_calibration.setText(str(top_calibration))

        if side_calibration:
            self.label_side_calibration.setText(str(side_calibration))


    def get_calibration_parms(self):   
        calibration_params = {}
        calibration_params['top_calibration'] =  self.label_top_calibration.text()
        calibration_params['side_calibration'] =  self.label_side_calibration.text()
        return calibration_params

    def app_size(self):
        w = self.centralwidget.width()
        h = self.centralwidget.height()
        return h,w

    def set_camera_parms(self, parms):


        for parm in self.dict_camera_params.keys():

            if parm=='serial_number' or parm == 'trigger_mode':

                self.dict_camera_params[parm].setCurrentText(parms[parm])


            else:
                self.dict_camera_params[parm].setValue(int(parms[parm]))


    def get_camera_setting_parms(self):
        camera_params = {}
        camera_params['gain_value'] = self.gain_spinbox.value()
        camera_params['expo_value'] = self.expo_spinbox.value()
        camera_params['width'] = self.width_spinbox.value()
        camera_params['height'] = self.height_spinbox.value()
        camera_params['offsetx_value'] = self.offsetx_spinbox.value()
        camera_params['offsety_value'] = self.offsety_spinbox.value()
        camera_params['trigger_mode'] = self.trigger_combo.currentText()
        camera_params['serial_number'] = '0' if self.serial_number_combo.currentText()=='No Serial' else self.serial_number_combo.currentText()
        return camera_params


    def get_current_direction_camera_setting(self):
        return str(self.cameraname_label.text()).lower()

    def connect_camera_setting_event(self, func):
        for parm,obj in self.dict_camera_params.items():
            if parm in ['trigger_mode', 'serial_number']:
                
                obj.currentTextChanged.connect( func )
            else:
                obj.textChanged.connect(func)




if __name__ == "__main__":
    app = QApplication()
    win = UI_main_window()
    # apply_stylesheet(app,theme='dark_cyan.xml')
    api = main_api.API(win)
    win.show()
    #api.set_images2()
    sys.exit(app.exec())
    