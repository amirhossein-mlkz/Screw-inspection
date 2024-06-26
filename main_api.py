#################################
#//////////////////////////////
#
#   stackwidget1-->
#               page_dashboard   (main_page)
#               page_users_setting
#               page_camera_setting
#               page_settings
#               page_tools (stackwidget2)-->      
#                               page_grab  (page)
#                               page_tool_1 (page_1)
#                               page_tool_2 (page_2)
#
#   set functions in *set image here 
#
#   push_ptn  =  *_btn   exam roi_grab_btn
#   others = label_*     exam spinBox_grab_page_x
#
#
#//////////////////////////////
################################
print('API')
from datetime import datetime

import threading
from functools import partial
from typing import Optional


import numpy as np


import database_utils
import cv2

# import login_UI
import confirm_UI
from backend import camera_funcs, colors_pallete, confirm_window_messages, mainsetting_funcs\
                    , user_login_logout_funcs, user_management_funcs, Screw, Utils, Drawing, cvTools, mathTools, proccessings,plc_modbus

from backend.mouse import Mouse
from backend import camera_connection #2 as camera_connection
from backend.threadRunner import threadRunner
from backend import cvToolsCython
from database import defualtScrew

from full_screen_UI import FullScreen_UI
import texts

from database import dbUtils, screwDB
import platform
from Keys import set_dimensions
from PySide6.QtCore import QDateTime as sQDateTime
from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import QThread as sQThread
from backend.cameraThread import cameraWorker
import threading


# from PyQt5.QtCore import 
import time
from PySide6.QtCore import QTimer as sQTimer
# from PyQt5.QtCore import QTimer

from history_UI import UI_history_window

# from backend import cvToolsCython   



DEBUG = False
DEBUG_PROCCESSING_THREAD = False

def time_measure(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        out = func(*args, **kwargs)
        t = time.time() - t
        print(f'time {func.__name__} {t}')
        return out
    return wrapper

DEFAULT_SCERW_PATH = 'database\defualt_screw'

class API:

    SAMPLE_IMAGE=False

    run_detect=False

    image_num=0

    #variable for history 

    all_screw=0
    defect_screw =0


    def __init__(self,ui):
        self.ui = ui
        self.win_fullscreen = FullScreen_UI()
        self.prev_time = 0
        self.tools_live_enable = False        
        
        self.current_camera_imgs = {}
        self.sides=['side','top']
        self.during_set_image = False
        self.avrage_mode = True
        #self.image_trigger_mode = False
        
        #------------------------------------------------------------------------------------------------------------------------
        # UIs of the app
        # main settings UI
        
        # login window UI and API
        #self.login_ui = login_UI.UI_main_window()
        # confirmation window UI
        self.confirm_ui = confirm_UI.UI_main_window()

        #------------------------------------------------------------------------------------------------------------------------
        # APIs of the app
        #self.login_api = login_UI.login_api.API(self.login_ui)
        #------------------------------------------------------------------------------------------------------------------------


        #------------------------------------------------------------------------------------------------------------------------
        # database module api
        
        os=platform.platform()
        if os[:5] =='Linux':


            self.db = database_utils.dataBaseUtils(password='password')
        
        else:
            self.db = database_utils.dataBaseUtils(password='@mm@9398787515AmmA')
            #self.db = database_utils.dataBaseUtils(password='root')



        self.plc_reg_on_off_btns = {
            
            'run': self.ui.plc_run_reg_btn,
            'stop': self.ui.plc_stop_reg_btn,
            'reject': self.ui.plc_reject_reg_btn,
        }


        cameras_info = self.db.load_cam_params(1)

        #sensor_detection_page
        self.both_results = {}

        self.rect_roi_drawing_sensor_detection_page = Drawing.drawRect()
        self.load_detection_parms()
        self.trig_done =False
        self.realtime_measurment = False
        #self.set_detection_parms()
        self.cameras = {}
        self.cameraworkers = {}
        self.connect_camera()
        self.available_camera_serials = camera_funcs.get_available_cameras_list_serial_numbers()

        mainsetting_funcs.assign_appearance_existing_params_to_ui(ui_obj=self.ui)
        # load and apply program appearance params
        self.load_appearance_params_on_start()
        # refresh dashboard
        self.language='en'


        # self.test_trig_camera()

        self.play_pause_status=True

        self.calibration_value={}
        
        #------------------------------------------------------------------------------------------------------------------------
        # main UI widget ids list 

        #------------------------------------------------------------------------------------------------------------------------
        # define standalone params
        # flag to chech whereas any user is logged in or not
        self.user_entered = False
        # waitkey
        self.waitkey = 2000
        # update picture waitkey/delay for updating camera picture in video mode
        self.update_picture_delay = 10

        #-------------------------------------------------------------------------------------------------------------------
        
        self.mouse = Mouse()
        self.rect_roi_drawing = { 'top': Drawing.drawRect(), 'side': Drawing.drawRect() }
        self.circle_roi_drawing = { 'top': Drawing.drawCircel(), 'side': Drawing.drawCircel() }
        self.poly_roi_drawing = { 'top': Drawing.drawPoly(), 'side': Drawing.drawPoly() }
        
        self.roi_drawings = {
            'rect' : self.rect_roi_drawing, 
            'circel': self.circle_roi_drawing,
            'poly' : self.poly_roi_drawing
        }
        
        self.current_image_screw = {}
        self.rotate_correction = False

        



        #-------------------------------------------------------------------------------------------------------------------
        self.ui.set_combo_boxes(self.ui.comboBox_edit_remove, dbUtils.get_screws_list())
        self.load_live_page_infoes()

        self.mouse.connect_all(self.ui.label_image_grab_page, self.image_setting_mouse_event)
        self.mouse.connect_all(self.ui.camera_detection_mode_picture, self.image_setting_mouse_event_sensor_detection_page)
        
        self.set_images()


        self.retry_plc_connection=0
        self.plc_value={}
        self.connect_plc()         #check plc status at startup
        self.timer_check_plc = sQTimer()
        self.timer_check_plc.timeout.connect(self.check_plc_status)
        self.timer_check_plc.start(500)

        self.timer_show_plc_parms = sQTimer()
        self.timer_show_plc_parms.timeout.connect(self.show_plc_parms)
        self.timer_show_plc_parms.start(200)
        # Language
        self.load_language()
        self.ui.combo_change_language.currentTextChanged.connect(self.set_language)

        #history

        self.history_obj = UI_history_window()


        #fullscreen
        self.eror_img = cv2.imread('images/capture_eror.jpg')
    

        self.button_connector()
        
        self.set_detection_parms()


        #hide

        self.hide_objs()


        self.set_realtime_measurment()


        print('*Success*'*20)


        #sensor detection page
        



    def button_connector(self):
        
        #--------------------------------------amir---------------------------------------
        
        

        
        # login button
        # self.ui.main_login_btn.clicked.connect(partial(lambda: user_login_logout_funcs.run_login_window(ui_obj=self.ui, login_ui_obj=self.login_ui, confirm_ui_obj=self.confirm_ui)))
        self.ui.reject_btn.clicked.connect(self.start_reject)

        # camera buttons in the camera-settings section
        # for cam_id in camera_funcs.all_camera_ids:
        #     eval('self.ui.camera%s_btn' % cam_id).clicked.connect(partial(lambda: self.load_camera_params_from_db_to_UI(self.)))
        self.ui.btn_tools_live.clicked.connect(self.enable_live_view_for_tools)
        self.ui.camera01_btn.clicked.connect(partial(lambda: self.load_camera_params_from_db_to_UI('top')))
        self.ui.camera02_btn.clicked.connect(partial(lambda: self.load_camera_params_from_db_to_UI('side')))

        self.ui.camera_setting_get_top_camera.clicked.connect(lambda:self.capture_image(direction='top'))
        self.ui.camera_setting_get_side_camera.clicked.connect(lambda:self.capture_image(direction='side'))
        
        self.ui.connect_camera_setting_event(self.load_camera_params_from_UI_to_camera)

        # buttons in the camera-settings section
        self.ui.camera_setting_apply_btn.clicked.connect(partial(self.save_changed_camera_params))



        # login window and confirm window
        #self.login_ui.login_btn.clicked.connect(partial(lambda: user_login_logout_funcs.authenticate_user(ui_obj=self.ui, login_ui_obj=self.login_ui, login_api_obj=self.login_api)))
        self.confirm_ui.yes_btn.clicked.connect(partial(self.confirm_yes))
        self.confirm_ui.no_btn.clicked.connect(partial(self.confirm_ui.close))

        # User managment
        self.ui.side_users_setting_btn.clicked.connect(partial(self.refresh_users_table))
        self.ui.remove_user_btn.clicked.connect(partial(self.remove_users))
        self.ui.create_user.clicked.connect(partial(self.add_user))

        
        # general-settings

        # self.ui.btn_set_szies.clicked.connect(self.set_apply_imgs_live)

        self.ui.setting_color_comboBox.currentTextChanged.connect(lambda: mainsetting_funcs.update_combo_color(ui_obj=self.ui))
        self.ui.setting_fontstyle_comboBox.currentTextChanged.connect(lambda: mainsetting_funcs.update_combo_fontstyle(ui_obj=self.ui))
        self.ui.setting_fontsize_comboBox.currentTextChanged.connect(lambda: mainsetting_funcs.update_combo_fontsize(ui_obj=self.ui))
        self.ui.setting_appearance_apply_btn.clicked.connect(lambda: self.apply_changed_appearance_params(mode='appearance'))

        
        self.ui.side_general_setting_btn.clicked.connect(lambda: self.load_appearance_params_on_start(mainsetting_page=True))

        #Fullscreen  
        self.ui.fullscreen_cam_top_btn.clicked.connect(lambda: self.show_full_screen('top'))
        self.ui.fullscreen_cam_side_btn.clicked.connect(lambda: self.show_full_screen('side'))


        #tools page

        self.ui.save_new_btn.clicked.connect(self.add_new_screw)
        self.ui.edit_remove_btn.clicked.connect(self.get_screw_names)
        self.ui.edit_btn.clicked.connect(self.edit_load_screw)
        self.ui.remove_screw_btn.clicked.connect(self.remove_screw)

        self.ui.get_main_parms_screw_top()


        # publice setting-------------------------------------------------------
        #page_setting

        
        self.ui.side_detection_mode_btn.clicked.connect(self.refresh_sensor_image_page)
        #Page 1_top----------------------------------------------------------
      
        
        self.ui.connect_btn('set_img', self.update_main_image )

        self.ui.line_img_path0_1_side.textChanged.connect(self.update_main_image)
        self.ui.line_img_path0_1_top.textChanged.connect(self.update_main_image)

        self.ui.connect_btn('page', self.update_setting_page_info)     
        self.ui.connect_sliders('thresh',  self.update_slider)
        self.ui.connect_sliders('thresh_min',  self.update_slider)
        self.ui.connect_sliders('thresh_max',  self.update_slider)
        self.ui.connect_sliders('noise_filter',  self.update_slider)
        self.ui.connect_sliders('edge_thresh',  self.update_slider)
        self.ui.checkbox_connect('thresh_inv', self.update_thresh_inv )
        self.ui.connect_list_pack('sub_pages', self.update_list_name )
        self.ui.connect_limit_spin(self.update_limit)
        self.ui.connect_spins_parm(self.update_numerical_parms)
        self.ui.btn_enabel_mask_draw.toggled.connect(self.setting_image_updater)
        self.ui.checkbox_connect('other', self.update_sepc_checkboxes)
        self.ui.connect_multi_options(self.update_muit_options )
        
        self.ui.roi_connect(self.update_roi_input)        
        self.ui.save_btn_page_grab.clicked.connect(self.save_screw)
        
        self.ui.connect_cameras_live_page.clicked.connect(self.connect_camera)
        self.ui.disconnect_cameras_live_page.clicked.connect(self.disconnect_camera_on_ui_change)
        


        self.ui.side_dashboard_btn.clicked.connect(self.load_live_page_infoes)
        self.ui.side_dashboard_btn.clicked.connect(self.load_camera_params_from_db_to_camera)
        self.ui.side_camera_setting_btn.clicked.connect(self.load_camera_params_from_UI_to_camera)
        self.ui.camera_setting_reset_btn.clicked.connect(self.reset_camera_parms_from_db)

        # Live Page

        self.ui.lives['combo_boxes']['screw_list'].currentTextChanged.connect(self.load_screw_live )
        #self.ui.spin_scale_top_cam_live_page.valueChanged.connect(self.size_update_top_cam_live)   
        #self.ui.spin_scale_side_cam_live_page.valueChanged.connect(self.size_update_side_cam_live)   
        

        # PLC settings
        self.ui.btn_save_ip_plc.clicked.connect(self.save_plc_ip)
        self.ui.connect_plc_btn.clicked.connect(self.connect_plc)
        self.ui.disconnect_plc_btn.clicked.connect(self.disconnect_plc)

        # self.ui.check_run_plc.clicked.connect(lambda: self.check_plc_parms(self.ui.check_run_plc.objectName()))
        # self.ui.check_stop_plc.clicked.connect(lambda: self.check_plc_parms(self.ui.check_stop_plc.objectName()))
        # self.ui.check_reject_plc.clicked.connect(lambda: self.check_plc_parms(self.ui.check_reject_plc.objectName()))
        # self.ui.check_spare_plc.clicked.connect(lambda: self.check_plc_parms(self.ui.check_spare_plc.objectName()))




        self.ui.checkall_plc_btns.clicked.connect(self.check_all_plc_parms)
        self.ui.save_plc_pathes.clicked.connect(self.save_plc_parms)
        self.ui.check_set_value_plc.clicked.connect(lambda: self.check_plc_parms(self.ui.check_set_value_plc.objectName()))
        self.ui.set_value_plc.clicked.connect(self.set_plc_value)


        self.load_plc_ip()
        self.load_plc_parms()

        self.ui.start_capture_live_page.clicked.connect(self.start_detection)
        self.ui.stop_capture_live_page.clicked.connect(self.stop_detection)

        #history
        self.ui.history_btn.clicked.connect(self.show_history_win)
        # self.ui.history_btn.clicked.connect(self.show_history_win)
        self.history_obj.reset_btn.clicked.connect(self.reset_history)
        # self.update_history()

        #calibration page

        self.ui.btn_connect_top_cal_page.clicked.connect(lambda:self.show_camera_picture(direction='top'))
        self.ui.btn_connect_side_cal_page.clicked.connect(lambda:self.show_camera_picture(direction='side'))

        self.ui.btn_disconnect_top_cal_page.clicked.connect(lambda:self.disconnect_camera_cal_page(direction='top'))
        self.ui.btn_disconnect_side_cal_page.clicked.connect(lambda:self.disconnect_camera_cal_page(direction='side'))


        self.ui.btn_save_value_top_cal_page.clicked.connect(self.save_calibration_parms_top)
        self.ui.btn_save_value_side_cal_page.clicked.connect(self.save_calibration_parms_side)





        #camera setting page

        self.ui.play_camera_setting_btn.clicked.connect(lambda: self.set_prev_flag(True))
        self.ui.pause_camera_setting_btn.clicked.connect(lambda: self.set_prev_flag(False))

        #save image

        self.ui.btn_save_top_cam_live_page.clicked.connect(lambda:self.capture_image_live(direction='top'))
        self.ui.btn_save_side_cam_live_page.clicked.connect(lambda:self.capture_image_live(direction='side'))

        for name, btn in self.plc_reg_on_off_btns.items():
            btn.clicked.connect(partial(self.plc_on_off_reg(name)))

        from PySide6.QtGui import QFont
        font = QFont()
        font.setPointSize(17)
        self.ui.start_capture_live_page.setFont(font)



        #calibration

        self.load_calibration_parms()

        self.p_is_during = {'top':False,'side':False}
        self.p_finished = {'top':False,'side':False}

        #senor detection page
        self.ui.camera_get_picture_detection_mode.clicked.connect(self.get_picture_detection_page)
        self.ui.thresh_min_detection_page.valueChanged.connect(self.get_picture_detection_page)
        self.ui.thresh_max_detection_page.valueChanged.connect(self.get_picture_detection_page)
        self.ui.btn_save_sensor_detection_page.clicked.connect(self.save_detection_parms)
        

        #yazd 

        self.ui.checkBox_test_live.clicked.connect(self.set_realtime_measurment)


        

    # dashboard page
    #------------------------------------------------------------------------------------------------------------------------
    # refresh summary informations on the dashboard page
    def refresh_dashboard_page(self):
        print('dashboard_page')

    def save_live_image(self):

        screw_name=self.ui.combobox_select_screw_live.currentText()


        img0=np.zeros((500,500),dtype='uint8')
        img1=np.zeros((500,500),dtype='uint8')

        dbUtils.save_screw_image(screw_name,[img0,img1])


    def set_load_imgs_live(self):
        parms_=[]
        for side in self.sides:
            parms=self.db.get_size_table('{}'.format(side))[0]
            self.ui.load_sizes(parms,'{}'.format(side))
            parms_.append(parms)

        self.camera_ratio=parms_


        

    def size_update_top_cam_live(self):
        scale=self.ui.spin_scale_top_cam_live_page.value()
        w=int(self.camera_ratio[1]['x'])
        h=int(self.camera_ratio[1]['y'])
        ratio=w/h

        set_dimensions(self.ui.label_img_top_live,(x*scale),(y*scale*ratio))


    def size_update_side_cam_live(self):
        return 
        scale=self.ui.spin_scale_side_cam_live_page.value()
        x=int(self.camera_ratio[1]['x'])
        y=int(self.camera_ratio[1]['y'])
        ratio=y/x
        set_dimensions(self.ui.label_img_side_live,(x*scale),(y*scale*ratio))



    #------------------------------------------------------------------------------------------------------------------------   
    #
    #
    #
    # 
    #  camera functions in the camera setting page
    #
    #
    #
    #
    # ------------------------------------------------------------------------------------------------------------------------   
    
    def disconnect_camera(self):
        for cam in self.cameras.values():
            if cam.camera is not None:
                cam.stop_grabbing()
            else:
                print('camera error disconnect_camera')



    def camera_trig_side(self,img):
        img = cv2.cvtColor( img, cv2.COLOR_GRAY2BGR)
        self.ui.set_image_label(self.ui.label_img_side_live, img)
        #cv2.imshow('img',img)
        
        #cv2.waitKey(100)



    def connect_camera(self):


        # if self.cameras==None:
        if not self.ui.camera_connect_flag:
            self.init_cameras()
            self.threads = {}
            for direction in self.cameras.keys():
                if self.cameras[direction]:
                    self.cameras[direction].start_grabbing()
                    if self.image_trigger_mode:
                        if self.direction_sensor_mode != direction:
                            continue
                    else:
                        if direction!='top':
                            continue
                    
                    self.cameraworkers[direction] = cameraWorker(self.cameras[direction])
                    self.cameraworkers[direction].success_grab_signal.connect(self.set_images)
                    self.threads[direction] = threading.Thread(target= self.cameraworkers[direction].grabber)
                    self.threads[direction].start()
            self.ui.camera_connect_flag=True
            self.ui.disconnect_cameras_live_page.setEnabled(True)
            self.ui.connect_cameras_live_page.setEnabled(False)
        else:
            print('camera connection already exist')

    # # apply camera parameters to camera(s) (in database) on apply button click
    def save_changed_camera_params(self, apply_to_multiple=False):
        # get camera-id and camera params
        camera_id = camera_funcs.get_camera_id(self.ui.cameraname_label.text())
        print('camera_id',camera_id)
        camera_params = camera_funcs.get_camera_params_from_ui(ui_obj=self.ui)

        res = camera_funcs.set_camera_params_to_db(db_obj=self.db, camera_id=camera_id, camera_params=camera_params)
        if res:
            self.ui.show_mesagges(self.ui.camera_setting_message_label, 'Settings Applied Successfully', color=colors_pallete.successfull_green)
        else:
            self.ui.show_mesagges(self.ui.camera_setting_message_label, 'Failed to Apply Settings', color=colors_pallete.failed_red)



    # get cameras parameters from database given camera-id and apply to UI
    def load_camera_params_from_db_to_UI(self,camera_id):
        parm = self.db.load_cam_params(camera_id)
        self.ui.set_camera_parms(parm)


    def load_camera_params_from_db_to_camera(self,):

        for direction in ['top','side']:
            self.cameras[direction].stop_grabbing()
            parm = self.db.load_cam_params(direction)
            self.cameras[direction].update_parms(parm)
            
            self.cameras[direction].start_grabbing()

            if self.cameras!= None:
                if not self.image_trigger_mode:
                    if self.direction_sensor_mode == direction:
                        try:
                            self.cameras[direction].on_trigger()
                        except:
                            print('eror in set trigger in api')
                    else:
                        try:
                            self.cameras[direction].off_trigger()
                        except:
                            print('eror in set trigger in api')

                else:
                    try:
                        self.cameras[direction].off_trigger()
                    except:
                        print('eror in set trigger in api')




    
    def load_camera_params_from_UI_to_camera(self):
    
        direction = self.ui.get_current_direction_camera_setting()
        parms = self.ui.get_camera_setting_parms()
        self.cameras[direction].update_parms(parms)

    def reset_camera_parms_from_db(self):
        print('reset_camera_parms_from_db')
        direction = self.ui.get_current_direction_camera_setting()
        self.load_camera_params_from_db_to_UI(direction)
        self.load_camera_params_from_UI_to_camera()
        



    # disconnect camera on UI change
    def disconnect_camera_on_ui_change(self):
        if self.ui.camera_connect_flag:
            #print('start disconnection')
            self.stop_detection()
            for direction in self.sides:

                    
                    self.cameras[direction].stop_grabbing()
                    self.cameras[direction].set_capturing(False)
                    try:
                        self.threads[direction].quit()
                    except:
                        print('Error disconnect_camera_on_ui_change')
                        pass

            self.ui.connect_cameras_live_page.setEnabled(True)
            self.ui.disconnect_cameras_live_page.setEnabled(False)
            
            self.cameras={}
            self.ui.camera_connect_flag=False
            print('end disconnection')
            cv2.waitKey(1000)



    #set play or pause flag for camera page
    def set_prev_flag(self,mode):
        print('play-pause')
        self.play_pause_status = mode
        for direction in ['top', 'side']:
            if mode:
                print('start grabbing')
                self.cameras[direction].start_grabbing()
            else:
                print('stop grabbing')
                self.cameras[direction].stop_grabbing()

    # appearance parameters in the general-settings page
    #------------------------------------------------------------------------------------------------------------------------
    # apply user changed appearance parametrs in the general-setting to program and database
    def apply_changed_appearance_params(self, mode='appearance'):
        # get parameters from UI
        if mode == 'appearance':
            message_label = self.ui.general_setting_appearance_message_label
            params = mainsetting_funcs.get_appearance_params_from_ui(ui_obj=self.ui)
            # apply appearance parameters to program
            mainsetting_funcs.apply_appearance_params_to_program(ui_obj=self.ui, confirm_ui_obj=self.confirm_ui, appearance_params=params)
        # update database
        res = mainsetting_funcs.set_mainsetting_params_to_db(db_obj=self.db, apperance_params=params)
        # show validation message
        if res:
            self.ui.show_mesagges(message_label, 'Settings Applied Successfully', color=colors_pallete.successfull_green)

        else:
            self.ui.show_mesagges(message_label, 'Failed to Apply Settings', color=colors_pallete.failed_red)
        

    # load appearance parameters from database on program start
    def load_appearance_params_on_start(self, mainsetting_page=False):
        # load from database
        apperance_params = mainsetting_funcs.get_mainsetting_params_from_db(db_obj=self.db)
        # apply to UI
        mainsetting_funcs.set_appearance_params_to_ui(ui_obj=self.ui, appearance_params=apperance_params)
        if not mainsetting_page:
            mainsetting_funcs.apply_appearance_params_to_program(ui_obj=self.ui, confirm_ui_obj=self.confirm_ui, appearance_params=apperance_params)

    
    #------------------------------------------------------------------------------------------------------------------------


    # user Managment settings in the user management page
    #------------------------------------------------------------------------------------------------------------------------
    # get users from database and apply to users table
    def refresh_users_table(self):
        users_list = user_management_funcs.get_users_from_db(db_obj=self.db)
        user_management_funcs.set_users_on_ui(ui_obj=self.ui, users_list=users_list)


    # remove user(s)
    def remove_users(self):
        # get selected users from UI
        users_list = user_management_funcs.get_users_from_db(db_obj=self.db)
        selected_users = user_management_funcs.get_selected_users(ui_obj=self.ui, users_list=users_list)
        # check not to remove admin users
        if 'Dorsa_admin' in selected_users:
            self.ui.show_mesagges(self.ui.create_user_message, 'Admin user(s) cant be removed', color=colors_pallete.failed_red)
            return
        # remove selected users from database
        res = user_management_funcs.remove_users_from_db(db_obj=self.db, users_list=selected_users)
        # refresh table
        self.refresh_users_table() # must change add confirm btn and show message


    # add new user
    def add_user(self):
        # get users-list from database
        users_list = user_management_funcs.get_users_from_db(db_obj=self.db)
        # get new user-info from UI
        new_user_info = user_management_funcs.get_user_info_from_ui(ui_obj=self.ui)
        ret = user_management_funcs.new_user_info_validation(db_obj=self.db, user_info=new_user_info)
        # validation
        if ret == 'True':
            # add user to database
            if user_management_funcs.add_new_user_to_db(db_obj=self.db, new_user_info=new_user_info) == 'True':
                self.ui.show_mesagges(self.ui.create_user_message, 'New User Created', color=colors_pallete.successfull_green)
                self.refresh_users_table()
                cv2.waitKey(self.waitkey) # must change
                # move add-user window
                self.ui.animation_move(self.ui.frame_add_user, 300)
                # clear new-user fields in UI
                line_edits = [self.ui.user_id, self.ui.user_pass, self.ui.user_re_pass]
                self.ui.clear_line_edits(line_edits)
            else:
                self.ui.show_mesagges(self.ui.create_user_message, str(ret), color=colors_pallete.failed_red)    
        else:
            self.ui.show_mesagges(self.ui.create_user_message, str(ret), color=colors_pallete.failed_red)

    #------------------------------------------------------------------------------------------------------------------------


    # other functions
    #------------------------------------------------------------------------------------------------------------------------      
    # function to connect the confirmation window yes button
    def confirm_yes(self):
        # user logout form
        if self.confirm_ui.msg_label.toPlainText() == confirm_window_messages.logout_confirm_message:
            user_login_logout_funcs.logout_user(ui_obj=self.ui, confirm_ui_obj=self.confirm_ui)
        # apply setting to cameras form
        elif self.confirm_ui.msg_label.toPlainText() == confirm_window_messages.setting_topcameras_confirm_message\
            or self.confirm_ui.msg_label.toPlainText() == confirm_window_messages.setting_bottomcameras_confirm_message\
                or self.confirm_ui.msg_label.toPlainText() == confirm_window_messages.setting_allcameras_confirm_message:
            self.save_changed_camera_params(apply_to_multiple=True)
            # close confirm window
            self.confirm_ui.close()
        # remove defect-group
        elif self.confirm_ui.msg_label.toPlainText() == confirm_window_messages.defects_remove_defect_group_messsage:
            print('id', self.defect_group_id)
            # remove defect-group

            self.refresh_defects_table() # must change add confirm btn and show message
            # close confirm window
            self.confirm_ui.close()
            

    def things_to_do_on_stackwidject_change(self):
        self.disconnect_camera_on_ui_change()
        self.edit_defect = False
        self.edit_defect_group = False

    

    



    #____________________________________________________________________________________________________________
    #                                           
    #
    #                                          Screw Settin Public
    #
    #
    #____________________________________________________________________________________________________________
    def get_screw_names(self):
        self.ui.set_combo_boxes(self.ui.comboBox_edit_remove, dbUtils.get_screws_list())
    
    def update_image(self,label_name,img):
        self.ui.set_image_page_tool_labels(img)
        
    
    
    def add_new_screw(self):
        name = self.ui.get_line_scraw_name()
        self.ui.clear_line_scraw_name()
        name  = name.replace(" ","")
        if len(name)>=3:
            flag = dbUtils.add_screw(name)
            self.ui.set_combo_boxes(self.ui.comboBox_edit_remove, dbUtils.get_screws_list())
            self.ui.comboBox_edit_remove.setCurrentText(name)

            self.screw_jasons = {'top': screwDB.screwJson() , 'side': screwDB.screwJson() }

            for key in self.screw_jasons.keys():
                path = dbUtils.get_screw_path( name )
                self.screw_jasons[key].set_name(name)
                self.screw_jasons[key].set_img_path(screwDB.IMG_PATH_DEF)
                self.screw_jasons[key].set_direction( key )
                self.current_image_screw[key] = cv2.imread(self.screw_jasons[key].get_img_path())
                for drawer in self.roi_drawings.values():
                    drawer[key].set_img_size( self.current_image_screw[key].shape[:2] )
                
                defualtScrew.set_default_all_page(self.screw_jasons[key])

            
            self.ui.set_deactive_all_pages()
            self.ui.edit_mode()

            self.update_setting_page_info()
            #self.update_main_image()
            self.ui.comboBox_edit_remove.setCurrentText(name) 
            
            

            for key in self.screw_jasons.keys():
                self.screw_jasons[key].write(path)

            self.setting_image_updater()

            if not flag:
                self.ui.show_warning(texts.WARNINGS['same_error_title'][self.language], texts.WARNINGS['same_error'][self.language])


            # self.ui.stackedWidget_2.setCurrentIndex(1)
            #self.update_setting_page_info()
            #self.ui.comboBox_edit_remove.S
            
            

            
            
        else:
            self.ui.show_warning(texts.WARNINGS['Name_Error_title'][self.language], texts.WARNINGS['Name_Error'][self.language])



    def save_screw(self):
        if self.ui.editmode:
            flag = self.ui.show_save_question(texts.WARNINGS['Save_Screw_title'][self.language], texts.WARNINGS['Save_Screw'][self.language])
        # try:
            if flag !=None:
                if flag:
                    for key in self.screw_jasons.keys():
                        
                        activate_tools = self.ui.get_activate_pages(direction = key)
                        print(key, activate_tools)
                        self.screw_jasons[key].set_active_tools(activate_tools)
                        path = dbUtils.get_screw_path( self.screw_jasons[key].get_name() )
                        self.screw_jasons[key].write(path)  
    
                    print('Screw Saved')
                    self.ui.show_warning(texts.WARNINGS['Save_Screw_title'][self.language],texts.WARNINGS['Successfully Save'][self.language])
                if not flag:
                    print('disacrd')
                    self.ui.show_warning(texts.WARNINGS['Save_Screw_title'][self.language],texts.WARNINGS['Screw_Settings_Restored'][self.language])
                self.ui.editmode=False
                self.ui.set_label(self.ui.label_status_mode,'')   
                self.ui.set_page_none()
                # frame_save_btns
                self.ui.frame_size_height(self.ui.frame_save_btns,size=0, both_height=True)
                self.ui.tool_btn_clear()
                self.ui.enable_bar_btn_tool_page('top',False)   
                self.ui.enable_bar_btn_tool_page('side',False)  
                self.ui.set_combo_boxes(self.ui.comboBox_edit_remove, dbUtils.get_screws_list())

                self.ui.label_screw_name.setText('-')

                self.ui.change_mode()
                self.ui.clear_image_page_tool_labels()

            # if flag==False:


            #     self.ui.

            if flag==None:

                print('cancel')
            
            # except:
            #     self.ui.set_warning('Save Eror','tool_page',level=2)
            #     self.ui.show_warning('Save Screw','Eror Save')
        else :
            self.ui.show_warning('Save Screw','First Edit Mode')
            
    def remove_screw(self):
        name=self.ui.comboBox_edit_remove.currentText()
        if name!='-':
            flag = self.ui.show_question(texts.WARNINGS['Delete_Screw_title'][self.language],texts.WARNINGS['Delete_Screw'][self.language]+' '+str(name))
            if flag:
                dbUtils.remove_screw(name)
                self.ui.set_combo_boxes(self.ui.comboBox_edit_remove, dbUtils.get_screws_list())
                
            
            
    def edit_load_screw(self):
        name = self.ui.comboBox_edit_remove.currentText()
        self.ui.set_deactive_all_pages()

        if name !='':
            self.ui.edit_mode()
            self.screw_jasons = {'top': screwDB.screwJson() , 'side': screwDB.screwJson() }
            
            path = dbUtils.get_screw_path(name)
            for direction in self.screw_jasons.keys():
                self.screw_jasons[direction].read(path, direction)
                
                #-----------------------------------------
                main_page_name = '1_{}'.format(direction)
                rect = self.screw_jasons[direction].get_rect_roi(main_page_name, None)
                if Utils.is_rect( rect ):
                    self.ui.enable_bar_btn_tool_page( direction, True )          
                
                else:
                    self.ui.enable_bar_btn_tool_page( direction, False )
                #-----------------------------------------
                active_pages=self.screw_jasons[direction].get_active_tools()
                print('active_pages',active_pages)
                self.ui.set_activate_pages(active_pages,True)

                #----------------------------------------------------
                img_path = self.screw_jasons[direction].get_img_path()
                print(img_path)
                self.ui.set_line_value('img_path', img_path)
                self.current_image_screw[direction] = cv2.imread(img_path)
                
                #self.ui.set
                for drawer in self.roi_drawings.values():
                    drawer[direction].set_img_size( self.current_image_screw[direction].shape[:2] )

            self.update_setting_page_info()
            #self.update_main_image()
    
    def setup_drawing_setting(self,page_name,):        

        self.drawing_available = False
        if page_name in ['0_top']:
            self.mouse_roi_shape_type = 'rect'
            self.mouse_roi_max_count = 1   
            self.drawing_available = True

        if page_name in ['1_top', '1_side', '3_side', '4_side', '5_side', '6_side']:
            self.mouse_roi_shape_type = 'rect'
            self.mouse_roi_max_count = 1     
            self.drawing_available = True
        
        elif page_name in ['2_side']:
            self.mouse_roi_shape_type = 'rect'
            self.mouse_roi_max_count = 1
            self.drawing_available = True

        elif page_name in ['3_top']:
            self.mouse_roi_shape_type = 'circel'
            self.mouse_roi_max_count = 2 
            self.drawing_available = True

        elif page_name in ['4_top', '5_top', '2_top']:
            self.mouse_roi_shape_type = 'circel'
            self.mouse_roi_max_count = 1
            self.drawing_available = True

        
    def image_setting_mouse_event(self,wname):
        # self.ui.
        page_name = self.ui.get_setting_page_idx(page_name = True)
        mouse_status = self.mouse.get_status()
        mouse_button = self.mouse.get_button()
        mouse_pt = self.mouse.get_relative_position()
        mouse_real_pt=self.mouse.get_position()
        


        if self.drawing_available:
        
            self.update_roi_mouse(mouse_status, mouse_button , mouse_pt, self.mouse_roi_shape_type , self.mouse_roi_max_count)

        #-------------------------------------------------------------------------
        direction = self.ui.get_setting_page_idx(direction = True)
        color = cvTools.get_gray_color( self.current_image_screw[direction], mouse_pt )
        img = cvTools.build_gcolor_img( color, color_type='rgb' )

        self.ui.update_mouse_position_tool_page(mouse_real_pt)
        self.ui.set_color_value_image_tool_page(color,img)

        
    def image_setting_mouse_event_sensor_detection_page(self,wname):

        mouse_status = self.mouse.get_status()
        mouse_button = self.mouse.get_button()
        mouse_pt = self.mouse.get_relative_position()
        mouse_real_pt=self.mouse.get_position()
        
        self.rect_roi_drawing_sensor_detection_page.max_shape_count = 1
        self.rect_roi_drawing_sensor_detection_page.qtmouse_checker( mouse_status, mouse_button, mouse_pt )

        self.get_picture_detection_page()
    #____________________________________________________________________________________________________________
    #                                           
    #
    #                                           New API
    #
    #
    #____________________________________________________________________________________________________________ 
    
    def update_list_name(self, action):
        def func():
            page_name = self.ui.get_setting_page_idx(page_name = True)
            direction = self.ui.get_setting_page_idx(direction = True)
            if action == 'add':
                input_name = self.ui.get_list_pack_input('sub_pages')
             
                if input_name not in ['', 'none']:

                    self.screw_jasons[ direction ].add_subpage(page_name, input_name)
                    self.ui.set_list_pack_input('sub_pages', '')
                    items = self.screw_jasons[ direction].get_subpages(page_name)
                    self.ui.set_list_pack_items( 'sub_pages', items )
                    self.ui.set_selected_list_pack_item('sub_pages', input_name)

                    defualtScrew.set_default_single_page(self.screw_jasons[direction], page_name, subpage_name=input_name )
                    parms = self.screw_jasons[ direction ].get_setting( page_name, subpage=input_name )
                    self.ui.set_setting_page_parms(parms)
                else:
                    print('Input valid name')
                    
                
            
            elif action == 'remove':
                input_name = self.ui.get_selected_list_pack_item('sub_pages')
                self.screw_jasons[ direction ].remove_subpage(page_name, input_name)
                items = self.screw_jasons[ direction].get_subpages(page_name)
                self.ui.set_list_pack_items( 'sub_pages', items )

            elif action =='select':
                pass
                #subpage_name = self.ui.get_sub_page_name( page_name )
                #parms = self.screw_jasons[ direction ].get_setting( page_name, subpage=subpage_name )
                #self.ui.set_setting_page_parms(parms)

            
            #self.update_setting_page_info()  
            self.refresh_page()  

        return func
    
    


    def update_numerical_parms(self, name):
        def func():
            page_name = self.ui.get_setting_page_idx(page_name = True)
            direction = self.ui.get_setting_page_idx(direction = True)
            subpage_name = self.ui.get_sub_page_name( page_name )

            value = self.ui.get_spins_parms_value(name)

            self.screw_jasons[ direction ].set_numerical_parm(page_name, subpage_name, name, value)
            self.setting_image_updater()
        return func


    
    def update_limit(self, limit_type, name):
        def func():
            page_name = self.ui.get_setting_page_idx(page_name = True)
            direction = self.ui.get_setting_page_idx(direction = True)
            subpage_name = self.ui.get_sub_page_name( page_name )
            
            limits =  self.ui.get_limit_value()

            self.screw_jasons[ direction ].set_limits(page_name, subpage_name, limits)
            #print( self.screw_jasons[ direction ].get_limits(page_name, subpage_name) )
        return func
        
    
    def update_slider(self, feature_name, direction, page_name):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        #---------------------
        if feature_name == 'thresh':
            if page_name in ['2_side', '3_side', '4_side','5_side','6_side']:
                page_name , subpage_name = '1_side', None
            #---------------------
            thresh = self.ui.get_sliders_value('thresh')
            self.screw_jasons[ direction ].set_thresh( page_name, subpage_name, thresh )   
        
        elif feature_name =='thresh_min':
            thresh_min = self.ui.get_sliders_value('thresh_min')
            self.screw_jasons[ direction ].set_thresh_min( page_name, subpage_name, thresh_min )
        
        elif feature_name =='thresh_max':
            thresh_max = self.ui.get_sliders_value('thresh_max')
            self.screw_jasons[ direction ].set_thresh_max( page_name, subpage_name, thresh_max ) 


        elif feature_name == 'noise_filter':
            noise_filter = self.ui.get_sliders_value('noise_filter')
            self.screw_jasons[ direction ].set_noise_filter( page_name, subpage_name, noise_filter )   
        
        else:
            value = self.ui.get_sliders_value(feature_name)
            self.screw_jasons[direction].set_numerical_parm(page_name, subpage_name, feature_name, value)

        self.setting_image_updater()

    
    
    
    def update_thresh_inv(self, name):
        def func():
            page_name = self.ui.get_setting_page_idx(page_name = True)
            direction = self.ui.get_setting_page_idx(direction = True)
            subpage_name = self.ui.get_sub_page_name( page_name )
            
            state = self.ui.get_checkbox_value('thresh_inv')        
            self.screw_jasons[ direction ].set_thresh_inv( page_name, subpage_name, state )
            
            self.setting_image_updater()
        
        return func

    

    def update_sepc_checkboxes(self, name):
        def func():
            page_name = self.ui.get_setting_page_idx(page_name = True)
            direction = self.ui.get_setting_page_idx(direction = True)
            subpage_name = self.ui.get_sub_page_name( page_name )

            state = self.ui.get_checkbox_value(name)        
            self.screw_jasons[ direction ].set_checkbox( page_name, subpage_name, name,  state )
            self.setting_image_updater()
        return func


    
    def update_muit_options(self, group_name, option_name):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )

        self.ui.set_multi_options_value(group_name, option_name)
        self.screw_jasons[ direction ].set_multi_option( page_name, subpage_name, group_name,  option_name )
            
        self.setting_image_updater()
        



    def update_roi_input(self, name):
        def func():
            page_name = self.ui.get_setting_page_idx(page_name = True)
            direction = self.ui.get_setting_page_idx(direction = True)
            subpage_name = self.ui.get_sub_page_name( page_name )
            
            data = self.ui.get_roi_value()


            if self.mouse_roi_shape_type=='rect':

                rect = self.screw_jasons[ direction ].get_rect_roi(page_name, subpage_name)
                
                rect_dict = Utils.rect_list2dict(rect)
                rect_dict[name] = data[name]
                rect = Utils.rect_dict2list(rect_dict)

                #print(self.rect_roi_drawing.shapes)
                self.roi_drawings['rect'][direction].update_shape(shape_idx=0,  shape=rect)            
                self.screw_jasons[direction].set_rect_roi( page_name, subpage_name, pt1=rect[0], pt2=rect[1])
            

            if self.mouse_roi_shape_type=='circel':

                circles = self.screw_jasons[direction].get_circels_roi(page_name,subpage_name)
                idx=0
                if 'x' in name:
                    idx = int(name[1:])-1
                    circles[idx][0][0] = data[name]
                elif 'y' in name:
                    idx = int(name[1:])-1
                    circles[idx][0][1] = data[name]
                elif 'r' in name:
                    idx = int(name[1:])-1
                    circles[idx][1] = data[name]               

                self.roi_drawings['circel'][direction].update_shapes(circles)            
                self.screw_jasons[direction].set_circels_roi( page_name, subpage_name,circles)
                 


            self.setting_image_updater()
        return func



    def update_roi_mouse(self, mouse_status, mouse_button, mouse_pt, shape_type, max_count):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        self.roi_drawings[ shape_type ][direction].max_shape_count = max_count
        self.roi_drawings[shape_type][direction].qtmouse_checker( mouse_status, mouse_button, mouse_pt )
        shapes = self.roi_drawings[shape_type][direction].shapes
        if len(shapes) > 0:
            if shape_type == 'rect':
                rect = shapes[0]
                rect_dict = Utils.rect_list2dict(rect)
                self.screw_jasons[direction].set_rect_roi( page_name, subpage_name, pt1=rect[0], pt2=rect[1] )
                self.ui.set_roi_value('rect_roi', rect_dict)
            
            if shape_type == 'circel':
                self.screw_jasons[direction].set_circels_roi( page_name, subpage_name, shapes=shapes[:max_count] )
                circles = self.screw_jasons[direction].get_circels_roi(page_name, subpage_name)
                for i,circle in enumerate(circles):
                    circle_dict = {}
                    [x,y], r = circle

                    circle_dict[ f'x{i+1}'] = x
                    circle_dict[ f'y{i+1}'] = y
                    circle_dict[ f'r{i+1}'] = r

                    self.ui.set_roi_value('circle_roi', circle_dict)

  


        
        else:
            if shape_type == 'rect':
                self.screw_jasons[direction].set_rect_roi( page_name, subpage_name, [],[] )

            if shape_type == 'circel':
                self.screw_jasons[direction].set_circels_roi( page_name, subpage_name, [] )

        self.setting_image_updater()
        
    
    def update_main_image(self):
        direction = self.ui.get_setting_page_idx(direction = True)
        
        path = self.ui.get_line_value('img_path')
        if cv2.imread(path) is not None:
            self.screw_jasons[ direction ].set_img_path(path)
            self.current_image_screw[direction] = cv2.imread(path)
            print('load image from', path)
        else:
            print('Error! : image not exist')
        

        if self.tools_live_enable:
            self.set_images()

        #set size image into all circel and rectangle drawer for calibration of drawing roi 
        for drawer in self.roi_drawings.values():
            drawer[direction].set_img_size( self.current_image_screw[direction].shape[:2] )
        

        #-----------------------------------------------------------------------
        
        # self.roi_drawings['rect'][direction].set_img_size( self.current_image_screw.shape[:2] )
        self.setting_image_updater()
        
            
        
    
    def update_setting_page_info(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )

        #-----------loade subpages name list --------------------
        if subpage_name is not None:
            items = self.screw_jasons[ direction].get_subpages(page_name)
            # if len(items) > self.ui.get_selected_list_pack_count('sub_pages'):
            self.ui.set_list_pack_items( 'sub_pages', items )
            subpage_name = self.ui.get_sub_page_name( page_name )
        
        activate_tools = self.ui.get_activate_pages(direction = direction)
        self.screw_jasons[direction].set_active_tools(activate_tools)
        #-----------loade limits --------------------
        self.setup_drawing_setting(page_name)
        self.refresh_page()

        #-------------------------------------------
        


    def refresh_page(self,):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )


        parms = self.screw_jasons[ direction ].get_setting( page_name, subpage_name )

        if page_name in ['0_top', '1_side']:
            parms['img_path'] = self.screw_jasons[ direction ].get_img_path() 

        if isinstance(parms,list):
            print('@'*20)
            assert False, f"parms should be dictionary, maybe you didn't define subpage 'none' for {page_name} in defaultScrew.py"
        self.ui.set_setting_page_parms(parms)

        #self.update_main_image()
        

        self.load_drawer()
        self.setting_image_updater()
        
        
    
    
    def load_drawer(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        for drawer in self.roi_drawings.values():
            drawer[direction].clear()
        
        for feature_name,value in self.screw_jasons[direction].get_setting( page_name, subpage_name ).items():
            if 'rect_roi' in feature_name:
                if Utils.is_rect(value):
                    self.roi_drawings['rect'][direction].shapes.append( value )
            
            elif 'circels_roi' in feature_name:
                self.roi_drawings['circel'][direction].shapes.extend( value )
    
    
    def setting_image_updater(self):
        page2finc_dict = {

        '0_top':self.update_image_0_top,
        '1_top':self.update_image_1_top,
        '2_top':self.update_image_2_top,
        '3_top':self.update_image_3_top,
        '4_top':self.update_image_4_top,
        '5_top':self.update_image_5_top,
        
        '1_side':self.update_image_1_side,
        '2_side':self.update_image_2_side,            
        '3_side':self.update_image_3_side,        
        '4_side':self.update_image_4_side,
        '5_side':self.update_image_5_side,               
        '6_side':self.update_image_6_side,

        }
        page_name = self.ui.get_setting_page_idx(page_name = True)

        # try:
        page2finc_dict[page_name]()
        # except:
        #     print('Error main_api setting_image_updater')
        #     pass
    
    def capture_image(self, direction):
        
        def func(direction):
            try:
                img = self.current_camera_imgs[direction]
            except:
                print('Eror capture_image')
                img=cv2.imread('images/capture_eror.jpg')
            if self.ui.capture_mode_flag == 'edit_page':
                f_name=self.ui.label_screw_name.text()
                main_path=self.ui.line_main_path.text()
                path=dbUtils.save_image(img,main_path=main_path,screw_name=f_name,direction=direction)
                self.ui.set_line_value('img_path',path,page_name='1_{}'.format(direction))
                self.update_main_image()
            else:
                f_name=self.ui.line_path_top_cam_live_page_2.text()
                if len(f_name)>2:
                    main_path=self.ui.line_main_path.text()
                    path=dbUtils.save_image(img,main_path=main_path,screw_name=f_name,direction=direction)   
                else:
                    self.ui.show_warning('Eror','Folder Name Should be more than 3 character')       
           


        return func(direction)

    
    def capture_image_live(self, direction):
        # print('asdawdawdawdawcadc'*20)
        def func(direction):
            for direction in ['top','side']:
                try:
                    img=self.cameras[direction].get_img()
                except:
                    print('eror capture image')
                    img=cv2.imread('images/capture_eror.jpg')
                f_name=self.ui.combobox_select_screw_live.currentText()
                main_path=self.ui.line_main_path.text()
            
                path=dbUtils.save_image(img,main_path=main_path,screw_name=f_name,direction=direction)
                print('image saved ',path)

        return func(direction)

    
    #____________________________________________________________________________________________________________
    #                                           
    #
    #                                          Image Drawings Function
    #                                                   TOP
    #
    #____________________________________________________________________________________________________________
    
    def update_image_0_top(self):
    
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        img = np.copy(self.current_image_screw['top'])



        img , draw = proccessings.preprocessing_0_top_img(img ,self.screw_jasons[ direction ],draw=img.copy() )


        if self.ui.is_drawing_mask_enabel():
            draw = self.roi_drawings['rect'][direction].get_image(draw)
            self.ui.set_image_page_tool_labels(draw)

        else:
            self.ui.set_image_page_tool_labels(img)

    def update_image_1_top(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )

        img = np.copy(self.current_image_screw['top'])
        img,draw = proccessings.preprocessing_0_top_img(img,self.screw_jasons[ direction ],img.copy())
        img , thresh_img, draw = proccessings.preprocessing_1_top_img(img,self.screw_jasons[ direction ],draw, centerise=False)

        algorithm = self.screw_jasons[ direction ].get_multi_option( page_name, subpage_name, 'algo' )
        

        #img = cvTools.preprocess(img)
        if algorithm  == 'thresh_algo':
            self.ui.stackedWidget_4.setCurrentIndex(1)
            
        elif algorithm  == 'edge_algo':
            self.ui.stackedWidget_4.setCurrentIndex(0)
            
        
        if self.ui.is_drawing_mask_enabel():
            draw = self.roi_drawings['rect'][direction].get_image(draw)
            self.ui.set_image_page_tool_labels(draw)
            
        else:
            self.ui.set_image_page_tool_labels(img)

        # img = self.rect_roi_drawing.get_image(img)
        
        # self.ui.set_image_page_tool_labels(img)

        # if Utils.is_rect( rect ) and np.count_nonzero(thresh_img) > 100:
        #     self.ui.enable_bar_btn_tool_page( direction, True )
        # else:
        #     self.ui.enable_bar_btn_tool_page( direction, False )
            

    def update_image_2_top(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )

        img = np.copy(self.current_image_screw['top'])
        json = self.screw_jasons[ direction ]

        
        img,_ = proccessings.preprocessing_0_top_img(img,json,None)
        img , mask_roi, draw = proccessings.preprocessing_1_top_img(img,json, )


        results, draw = proccessings.proccessing_top_measurment(img, mask_roi, json, img.copy(), calib_value=self.calibration_value['top'])

        info = {}
        for result in results:
            shape_type = self.screw_jasons[ direction ].get_multi_option( page_name, subpage_name, 'shape_type' )
            if subpage_name in result['name']:
                
                if shape_type == 'circel':
                    info['min_diameter'] = result['min']
                    info['max_diameter'] =  result['max']
                    info['avg_diameter'] =  result['avg']
                    self.ui.stackedWidget_3.setCurrentIndex(0)
                
                elif shape_type == 'hexagonal':
                    if 'corner' in result['name']:
                        info['min_corner'] = result['min']
                        info['max_corner'] = result['max']
                        info['avg_corner'] = result['avg']
                    
                    elif 'district' in result['name']:
                        info['min_district'] = result['min']
                        info['max_district'] = result['max']
                        info['avg_district'] = result['avg']
                    
                    self.ui.stackedWidget_3.setCurrentIndex(1)

                elif shape_type == 'rect':
                    pass
                    self.ui.stackedWidget_3.setCurrentIndex(1)


        self.ui.set_stetting_page_label_info(info)
            #--------------------------------------------------------------------------------------
        if self.ui.is_drawing_mask_enabel():
            h,w = draw.shape[:2]
            draw = cv2.circle(draw, (w//2, h//2), 5, (255,0,0) , thickness=-1)
            draw = self.roi_drawings['circel'][direction].get_image(draw)
            self.ui.set_image_page_tool_labels(draw)
        else:
            self.ui.set_image_page_tool_labels(img)
            




    def update_image_3_top(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )

        img = np.copy(self.current_image_screw['top'])

        
        json = self.screw_jasons[ direction ]

        
        img,_ = proccessings.preprocessing_0_top_img(img,json,None)
        img , mask_roi, draw = proccessings.preprocessing_1_top_img(img,json, )
        results, draw = proccessings.proccessing_top_defect(img, mask_roi, json, img.copy(), calib_value=self.calibration_value['top'])


        info={}
        for result in results:
            if subpage_name in result['name']:
                info = {'min_area': result['min'], 'max_area':result['max']}


        self.ui.set_stetting_page_label_info(info)

        if self.ui.is_drawing_mask_enabel():
            h,w = draw.shape[:2]
            draw = cv2.circle(draw, (w//2, h//2), 5, (255,0,0) , thickness=-1)
            draw = self.roi_drawings['circel'][direction].get_image(draw)
            self.ui.set_image_page_tool_labels(draw)
        else:
            self.ui.set_image_page_tool_labels(img)


        



    def update_image_4_top(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )

        img = np.copy(self.current_image_screw['top'])        

        json = self.screw_jasons[ direction ]



        img,_ = proccessings.preprocessing_0_top_img(img,json,None)
        img , mask_roi, draw = proccessings.preprocessing_1_top_img(img,json, )
        results, draw = proccessings.proccessing_top_edge_crack(img, mask_roi, json, img.copy(), calib_value=self.calibration_value['top'])
       
        info={}
        result =results[0]
        info = {'min_area': result['min'], 'max_area':result['max']}
        self.ui.set_stetting_page_label_info(info)
        #------------------------------------------------------------------------------------

        if self.ui.is_drawing_mask_enabel():

            h,w = draw.shape[:2]
            draw = cv2.circle(draw, (w//2, h//2), 5, (0,255,0) , thickness=-1)
            draw = self.roi_drawings['circel'][direction].get_image(draw)
            self.ui.set_image_page_tool_labels(draw)
            


        else:
            self.ui.set_image_page_tool_labels(img)


    

    def update_image_5_top(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw['top'])

        json = self.screw_jasons[ direction ]

        img,_ = proccessings.preprocessing_0_top_img(img,json,None)
        img , mask_roi, draw = proccessings.preprocessing_1_top_img(img,json, )
        results, draw = proccessings.proccessing_top_centerise(img, mask_roi, json, img.copy() , calib_value=self.calibration_value['top'])
       
        if subpage_name!='none':
            #---------1-----------------------------------------------------------------------------
            #specific Operation
            #---------------------------------------------------------------------------------------        
            info = {'distance_centers': results[0]['avg']}    
            self.ui.set_stetting_page_label_info(info)
            #------------------------------------------------------------------------------------
            
            if self.ui.is_drawing_mask_enabel():

                img = Utils.mask_viewer(img, mask_roi, color=(0,0,100))
                h,w = img.shape[:2]
                img = cv2.circle(img, (w//2, h//2), 5, (0,255,0) , thickness=-1)
                draw = self.roi_drawings['circel'][direction].get_image(draw)

                self.ui.set_image_page_tool_labels(draw)

            else:
                self.ui.set_image_page_tool_labels(img)
    #____________________________________________________________________________________________________________
    #                                           
    #
    #                                          Image Drawings Function
    #                                                   SIDE
    #
    #____________________________________________________________________________________________________________
    def update_image_1_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        
        img = np.copy(self.current_image_screw['side'])

        rect = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name)
        img = cvTools.preprocess(img)
        img, thresh_img, angle = proccessings.preprocessing_side_img(img, self.screw_jasons[direction], rotation=False, centerise=False)
        
        if Utils.is_rect( rect ) and np.count_nonzero(thresh_img) > 100:
            self.ui.enable_bar_btn_tool_page( direction, True )
        else:
            self.ui.enable_bar_btn_tool_page( direction, False )


        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img)
        img = self.roi_drawings['rect'][direction].get_image(img)
        self.ui.set_image_page_tool_labels(img)
    
    
    
    def update_image_2_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw['side'])
        
        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_side_img( img, json  )
                    
        result,img = proccessings.proccessing_body_lenght(img,thresh_img,json,draw=img.copy(), calib_value=self.calibration_value['side'])

        result=result[0]    
        info = {'min_lenght' : result['min'], 'max_lenght': result['max'], 'avg_lenght': result['avg']}  
        self.ui.set_stetting_page_label_info(info)
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(50,100,0))
        img = self.roi_drawings['rect'][direction].get_image(img)
        self.ui.set_image_page_tool_labels(img)
        
        
    
    
    def update_image_3_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw['side'])

        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_side_img( img, json  )


        result,img = proccessings.proccessing_thread_male(img,thresh_img,json,draw=img.copy(), calib_value=self.calibration_value['side'])
        
        info = {'thread_lenght': result[1]['avg'],
                'count_thread': result[2]['avg'] , 
                'step_distance':result[0]['avg'],
                'thread_diameter': result[3]['avg']
                }
        if len(result) == 5:
            info['navel_lenght'] = result[4]['avg']
        self.ui.set_stetting_page_label_info(info)
        
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(200,200,0))
        img = self.roi_drawings['rect'][direction].get_image(img)
        self.ui.set_image_page_tool_labels(img)
        
        

        
    def update_image_4_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw['side'])

        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_side_img( img, json  )
    
        results,img = proccessings.proccessing_side_diameters(img,thresh_img,json,draw=img.copy(), calib_value=self.calibration_value['side'])

        for result in results:
            if subpage_name in result['name']:
                info = {'min_diameter' : result['min'], 'max_diameter': result['max'], 'avg_diameter': result['avg']}                
        self.ui.set_stetting_page_label_info(info)  

        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(100,30,0))  
        img = self.roi_drawings['rect'][direction].get_image(img)
        self.ui.set_image_page_tool_labels(img)




    def update_image_5_side(self,):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw['side'])

        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_side_img( img, json  )
        
        results,img = proccessings.proccessing_side_head(img,thresh_img,json,draw=img.copy(), calib_value=self.calibration_value['side'])

   
        result = results[0]
        info = {'min_head_height' : result['min'], 'max_head_height': result['max'], 'avg_head_height': result['avg']}                
        self.ui.set_stetting_page_label_info(info)       

        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(50,30,200))    
        img = self.roi_drawings['rect'][direction].get_image(img)
        self.ui.set_image_page_tool_labels(img)




    def update_image_6_side(self,):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw['side'])


        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_side_img( img, json  )

        results,img = proccessings.preprocessing_side_damage(img,thresh_img,json,draw=img.copy(), calib_value=self.calibration_value['side'])
        

        for result in results:
            if subpage_name in result['name']:
                info = {'area': result['avg']}
                self.ui.set_stetting_page_label_info(info)
                break
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(100,200,50))
        img = self.roi_drawings['rect'][direction].get_image(img)
        self.ui.set_image_page_tool_labels(img)

    # #____________________________________________________________________________________________________________
    # #                                           
    # #
    # #                                                 Live
    # #
    # #
    # #____________________________________________________________________________________________________________
    def load_live_page_infoes(self,):
        name = self.ui.combobox_select_screw_live.currentText()
        self.ui.set_combo_boxes(self.ui.combobox_select_screw_live, dbUtils.get_screws_list())
        self.ui.combobox_select_screw_live.setCurrentText(name)



    def load_screw_live(self):
        
        name = self.ui.combobox_select_screw_live.currentText()
        name  = name.replace(" ","")
        if len(name)>=3:
            path = dbUtils.get_screw_path(name)
            # if path
            self.screw_jasons = {'top': screwDB.screwJson() , 'side': screwDB.screwJson() }
            for direction in self.screw_jasons.keys():
                self.screw_jasons[direction].read(path, direction)
                img_path = self.screw_jasons[direction].get_img_path()
                img=cv2.imread(img_path)
                if img is None:
                    print('Error load_screw_live')
                    img = np.zeros(shape=(1040,1392),dtype='uint8')
                
                self.ui.set_selected_image_live_page(direction,img)




    

    

















    #@time_measure
    def proccessing_live_side(self, img):
        
       if not self.p_is_during['side']:
            self.p_is_during['side'] = True
            screw_json = self.screw_jasons[ 'side' ]   

            self.worker_p_side  = processingSideWorker(screw_json, img, self.calibration_value['side'])
            self.worker_p_side.complete.connect(self.complete_proccessing)
            self.thread_p_side = threading.Thread(target=self.worker_p_side.run)

            if not DEBUG_PROCCESSING_THREAD:
                self.thread_p_side.start()
            else:
                self.worker_p_side.run()
                print('on DEBUG_PROCCESSING_THREAD')




    #@time_measure
    def proccessing_live_top(self, img):

        if not self.p_is_during['top']:
            self.p_is_during['top'] = True
            screw_json = self.screw_jasons[ 'top' ]

            self.worker_p_top  = processingTopWorker(screw_json, img, self.calibration_value['top'])
            self.worker_p_top.complete.connect(self.complete_proccessing)
            self.thread_p_top = threading.Thread(target=self.worker_p_top.run)
            

            if not DEBUG_PROCCESSING_THREAD:
                self.thread_p_top.start()
            else:
                self.worker_p_top.run()
                print('on DEBUG_PROCCESSING_THREAD')
        


    # PLC ////////////////////////////////////////////////////////////////////
    #________________________________________________________________________________________________________________________
    #
    #                                                          PLC
    #
    #________________________________________________________________________________________________________________________
    def connect_plc(self):
        self.load_plc_ip()
        self.ip=self.ui.get_plc_ip()
        self.my_plc=plc_modbus.plc_modbus(self.ip)
        self.connection_status=self.my_plc.connection()
        if self.connection_status:
            self.load_plc_parms()
            self.ui.frame_size_height(self.ui.frame_175, size = 600, both_height=True)
            
            
            self.ui.show_mesagges(self.ui.plc_warnings,texts.WARNINGS['Connection_succssed'][self.language])
            # self.plc_checker_thread.start_thread()
        else:
            self.ui.frame_size_height(self.ui.frame_175, size= 0, both_height=True)
            self.ui.show_mesagges(self.ui.plc_warnings,texts.WARNINGS['Connection_eror'][self.language],color='red')



    
    def disconnect_plc(self):
        try:
            self.my_plc.disconnect()
            del self.my_plc
        except:
            print('Error disconnect_plc')
            pass
        self.ui.frame_size_height(self.ui.frame_175, size=0, both_height=True)



    def check_plc_status(self):

        try:
            connection_status = self.my_plc.connection()
            if connection_status:
                self.ui.set_label(self.ui.plc_status_live_page,texts.WARNINGS['Connected'][self.language],color='green')
                self.retry_plc_connection=0
            else:
                self.retry_plc_connection+=1
                if self.retry_plc_connection>10:
                    self.ui.set_label(self.ui.plc_status_live_page,texts.WARNINGS['Connection_eror'][self.language],color='red')
        except:
            print('Error check_plc_status')
            self.retry_plc_connection+=1
            if self.retry_plc_connection>10:
                self.ui.set_label(self.ui.plc_status_live_page,texts.WARNINGS['Connection_eror'][self.language],color='red')

        

    def check_spec_plc_parms(self):

        btns=['check_run_plc','check_reject_plc']
        values={}
        for btn in btns:
            value=self.check_plc_parms(btn)

            values.update({btn:value})
        return values  

    def check_all_plc_parms(self):
        # try:
            btns=['check_run_plc','check_stop_plc','check_reject_plc']
            # while self.ui.stackedWidget.currentWidget()==self.ui.page_settings:
                # try:
            # time.sleep(0.5)
            
            for btn in btns:
                # try:
                    value=self.check_plc_parms(btn)
                    self.plc_value.update({btn:value})
                  
                    
            if self.ui.stackedWidget.currentWidget()==self.ui.page_settings:
                threading.Timer(0.3,self.check_all_plc_parms).start()


    def show_plc_parms(self):
        if self.ui.stackedWidget.currentWidget()==self.ui.page_settings:
            for name,value in zip(self.plc_value.keys(),self.plc_value.values()):
                try:
                    name=name.split('_',1)[1]
                    name = name[:-4]
                    label_name=eval('self.ui.label_{}'.format(name))
                    self.ui.set_plc_light(label_name, str(value))
                    self.ui.set_plc_light(label_name,value)
                    self.plc_reg_on_off_style_manager(name, value)
                except:
                    print('Error in show plc_parms')
                    pass

    def check_plc_parms(self,name):

        name=name.split('_',1)[1]
        name = name[:-4]
        path=eval('self.ui.line_{}.text()'.format(name))
     
        value=self.my_plc.get_value(int(path))
        return value
        # label_name=eval('self.ui.label_{}'.format(name))
        # self.ui.set_plc_light(label_name, str(value))
        # self.ui.set_plc_light(label_name,value)
        # self.plc_reg_on_off_style_manager(name, value)
    


    def load_plc_ip(self):
        ip=self.db.load_plc_ip()
        self.ui.plc_ip_line.setText(ip)

    def save_plc_ip(self):

        ip=self.ui.plc_ip_line.text()
        self.db.save_plc_ip(ip)
        
        self.ui.show_mesagges(self.ui.plc_warnings,texts.WARNINGS['plc_ip'][self.language])

    def load_plc_parms(self):

        parms=self.db.load_plc_parms()
        combo_list=[]
        for parm in parms:
            # try:
                
                try:
                    line=eval('self.ui.line_{}'.format(parm['name']))
                    line.setText(parm['path'])
                except:
                    line=eval('self.ui.spin_{}'.format(parm['name']))
                    line.setValue(int(parm['path']))
                combo_list.append(parm['name'])

            # except:
            #     pass
        self.parms=parms
        # print('/'*30,parms)
        # self.ui.comboBox_plc_addresses.addItems(combo_list)
        
    def update_path_plc(self):

        text=self.ui.comboBox_plc_addresses.currentText()
        

        value=eval('self.ui.line_{}.text()'.format(text))

        self.ui.line_set_value_plc.setText(value)


    def save_plc_parms(self):
        plc_parms=self.ui.get_plc_parms()
        # print('plc_parms',plc_parms)
        self.db.update_plc_parms(plc_parms)
        pass

    def set_plc_value(self):
     
        path=self.ui.line_set_value_plc.text()
        value=self.ui.line_value_set_value_plc.text()
        if value == 'True' or value == 'true':
            value = True
        elif value=='false' or value == 'False':
            value = False
        self.my_plc.set_value(int(path), value)
    
    
    def start_reject(self):
        delay = self.ui.spin_delay.value()/1000
        threading.Timer(delay,self.set_plc_reject,args=(True,True)).start()

    def set_plc_reject(self,value=False,again=False):
        print('set_plc_reject')
        path = self.ui.line_reject.text()  #change
        try:
            self.my_plc.set_value(int(path), value)
            # self.my_plc.set_value(path, True)  # if should true after False uncomment this line
        except:
            print('Error in set plc reject')
        if again:
            threading.Timer(self.ui.spin_duration.value()/1000,self.set_plc_reject).start()




    #________________________________________________________________________________________________________________________
    #
    #                                                          
    #
    #________________________________________________________________________________________________________________________



    def load_calibration_parms(self):

        parms=self.db.load_calibration_parms()

        self.ui.set_calibration(parms[0],parms[1])
        self.calibration_value.update({'top':parms[0]})
        self.calibration_value.update({'side':parms[1]})


    def save_calibration_parms(self,top=False,side=False):
        if top:
            self.db.save_top_calibration(top)
        if side:
            self.db.save_side_calibration(side)

        if not self.ui.btn_enabel_mask_draw_live_top.isChecked():
            draw_img_side = self.img_side
        
        draw_img_side = cv2.rotate( draw_img_side, cv2.ROTATE_90_COUNTERCLOCKWISE )

        if not self.ui.btn_enabel_mask_draw_live_side.isChecked():
            draw_img_top = self.img_top
        draw_img_top = cv2.rotate( draw_img_top, cv2.ROTATE_90_COUNTERCLOCKWISE )


            
        self.ui.set_image_label(self.ui.label_img_top_live, draw_img_top)
        self.ui.set_image_label(self.ui.label_img_side_live,draw_img_side)



    def save_calibration_parms_top(self):
        top = self.db.save_top_calibration(self.ui.doubleSpinBox_calibration_top.value())
        

    def save_calibration_parms_side(self):
        side = self.db.save_side_calibration(self.ui.doubleSpinBox_calibration_side.value())



    


    def load_language(self):
        lan=self.db.load_language()
        # self.ui.language=
        self.ui.set_language(lan)

        if lan =='English':
            self.language='en'
        else:
            self.language='fa'


        return lan
        

    def set_language(self):

        lan=self.ui.combo_change_language.currentText()
        print('save')
        self.db.set_language(lan)




    def init_cameras(self):
        cam_ids=[]
        
        for direction in ['top','side']:
            # try:
            cameras_info = self.db.load_cam_params(direction)
                

                    
            self.cameras [ cameras_info['direction'] ] = camera_connection.Collector(cameras_info['serial_number'],
                                                                                        exposure=cameras_info['expo_value'],
                                                                                        gain=cameras_info['gain_value'],
                                                                                        trigger=cameras_info['trigger_mode'],
                                                                                        height=cameras_info['height'],
                                                                                        width=cameras_info['width'],
                                                                                        packet_size=cameras_info['packet_size'],
                                                                                        frame_transmission_delay=cameras_info['transmission_delay'],
                                                                                        delay_packet=cameras_info['interpacket_delay'],
                                                                                        manual=True)
            cam_ids.append(cameras_info['serial_number'])
            # except:                                                                                                 
            #     print('eror in create camera objects')
                # self.cameras [ cameras_info['direction'] ] = None


            self.ui.set_camera_setting_combobox_ids(cam_ids)

    def start_detection(self):

        self.run_detect=True
        self.during_set_image = False
        #load screw image again. becuase maybe some settings chaged
        self.load_screw_live()
        self.load_calibration_parms()   # load calibration parms
        self.set_images()
        
        self.ui.start_capture_live_page.setEnabled(False)
        self.ui.stop_capture_live_page.setEnabled(True)
        self.ui.set_mask_main_page_btns_mode(True)


    def stop_detection(self):

        self.run_detect=False
        self.ui.start_capture_live_page.setEnabled(True)
        self.ui.stop_capture_live_page.setEnabled(False)
        self.ui.set_mask_main_page_btns_mode(False)

        for direction in ['top', 'side']:
            self.p_finished[direction] = False
            self.p_is_during[direction] = False
        
        # try:
        #     self.worker_p_side.deleteLater()
        # except:
        #     pass


    def show_image(self):
        
        # img = np.zeros(shape=(300,300),dtype='uint8')
        img = self.collector.image
        # print('dddd', value)
        cv2.imshow('a',img)
        cv2.waitKey(10)


    #History


    def show_history_win(self):

        history = self.db.load_history()

        # history = self.history

        perfect = int(history['all_screw'])-int(history['defect'])

        self.history_obj.total.setText(str(history['all_screw']))
        self.history_obj.defect.setText(str(history['defect']))
        self.history_obj.perfect.setText(str(perfect))

        self.history_obj.show()


    def update_history(self):

        history = self.db.load_history()

        new_all_screw = int(history['all_screw'])+self.all_screw
        new_defect = int(history['defect']) + self.defect_screw

        self.db.update_history(all=new_all_screw,defect=new_defect)

    def reset_history(self):

        ret = self.ui.show_question('Warning',texts.WARNINGS['reset'][self.language])

        if ret:
            self.db.update_history(all=0,defect=0)
            self.show_history_win()
        


    # show cameras picture on UI
    def show_camera_picture(self, direction):
        eval('self.ui.btn_connect_{}_cal_page'.format(direction)).setEnabled(False)
        eval('self.ui.btn_disconnect_{}_cal_page'.format(direction)).setEnabled(True)
        label = eval('self.ui.camera_{}_cal_page'.format(direction))
        status = eval('self.ui.connection_status_{}_cal_page'.format(direction))
        error_count =0
        while True:
            # try:
            ret , img = self.cameras[direction].getPictures()
            if ret:
                self.ui.set_image_label(label,img)
                # status.setText('Connection Success')
                
                self.set_status_calibration(status=status,message='Connection Success',mode=True)
                if error_count!=0:
                    error_count=0
                
            else:
                
                error_count+=1
                if error_count>=10:
                    # status.setText('Eror Connection')
                    self.set_status_calibration(status=status,message='Eror Connection',mode=False)

                # break                
            # except:
            #     status.setText('Eror Connection')
            #     print('Except show_camera_picture main_api')
            #     break
            # print('asd')
            cv2.waitKey(20)
                
    def set_status_calibration(self,status,message,mode):
        status.setText(message)
        if mode:
            status.setStyleSheet("color: #22824d")
        else:
            status.setStyleSheet("color: #b8182b")
    



    def disconnect_camera_cal_page(self,direction):
        self.cameras[direction].stop_grabbing()
        self.cameras[direction].set_capturing(False)
        eval('self.ui.btn_connect_{}_cal_page'.format(direction)).setEnabled(True)
        eval('self.ui.btn_disconnect_{}_cal_page'.format(direction)).setEnabled(False)

    def set_realtime_measurment(self,):
        # self.realtime_measurment = not(self.realtime_measurment)

        self.realtime_measurment = self.ui.checkBox_test_live.isChecked()
        
        if self.realtime_measurment:
            for direction in ['top', 'side']:
                try:
                    self.cameras[direction].off_trigger()
                except:
                    print(f'Error of trig for {direction}')
        else:
            self.load_camera_params_from_db_to_camera()


    def set_images(self,):
        #correct set image
        t = time.time()
        if not self.ui.camera_connect_flag or  t - self.prev_time < 0.2:
            return
        
        self.prev_time = t
        if not self.during_set_image:
            self.during_set_image = True
        
        #determine other camera that we should grab its image manuly
        # in hordware trigger mode other camera is 'side' always
        #-----------------------------------------------------------------------------
        other_camera = 'side'
        trigger_camera = 'top'

        if self.direction_sensor_mode == 'side':
                other_camera = 'top'
                trigger_camera = 'side'

        if (self.image_trigger_mode and not self.realtime_measurment and
            not self.ui.stackedWidget.currentWidget() in [self.ui.page_detection_mode, self.ui.page_camera_setting]) :
            
            

            self.current_camera_imgs[trigger_camera] = self.cameras[trigger_camera].image.copy()
            #t = time.time()
           
            
            trig,_,_ = proccessings.preprocessing_sensor_detection(self.current_camera_imgs[trigger_camera],
                                                                    **self.sensor_detection_values
                                                                    )
            #t = time.time() - t
            # print('trig image status', trig)
            if not trig:
                self.trig_done = False

            if not trig or self.trig_done:
                self.during_set_image = False
                return

            self.trig_done = True
                    
        else:
            # self.current_camera_imgs[trigger_camera] = self.cameras[trigger_camera].image.copy()
            # self.cameras[trigger_camera].getPictures()
            self.current_camera_imgs[trigger_camera] = self.cameras[trigger_camera].image.copy()
        
        #-----------------------------------------------------------------------------
        # try:
        #     self.cameras[other_camera].off_trigger()
        # except:
        #     if not DEBUG:
        #         print(f"ERROR:  self.cameras[{other_camera}].off_trigger()")
        

        if self.cameras[other_camera]:

            for _ in range(10):
                side_ret,image = self.cameras[other_camera].getPictures()  # temp for get side image
                # time.sleep(0.001)
                if DEBUG:
                    if other_camera == 'side':
                        self.current_camera_imgs[other_camera] = cv2.imread('sample images/temp_side/{}.jpg'.format(np.random.randint(1,4)),0)
                        break
                    else:
                        self.current_camera_imgs[other_camera] = cv2.imread('sample images/temp_top/{}.jpg'.format(np.random.randint(1,4)),0)
                        break
                if side_ret:
                    self.cameras[other_camera].image = image
                    self.current_camera_imgs[other_camera] = image.copy()
                    break
            else:
                self.during_set_image = False
                return
        #-----------------------------------------------------------------------------


        if self.tools_live_enable and self.ui.stackedWidget.currentWidget()==self.ui.page_tools:
            direction = self.ui.get_setting_page_idx(direction = True)
            try:
                img = self.cameras[direction].image
                color_img = img
                if len(color_img.shape)==2:
                    color_img = cv2.cvtColor(color_img, cv2.COLOR_GRAY2BGR)

                self.current_image_screw[direction] = color_img.copy()
                self.current_camera_imgs[direction] = img.copy()

                
            except Eception as e:
                print(str(e))
                pass


            self.setting_image_updater()

        if self.ui.stackedWidget.currentWidget()==self.ui.page_dashboard:
            
            draw_imgs = {
                'top': np.zeros(shape=(1920,1200,3),dtype='uint8'),
                'side': np.zeros(shape=(1920,1200,3),dtype='uint8')}

            results = {
                'top': [],
                'side': []}
            
            proccessing_functions = {
                'side':self.proccessing_live_side,
                'top': self.proccessing_live_top}
            
            for direction in ['top', 'side']:
                #try:   
                    if self.run_detect:
                        #draw_imgs[direction], results[direction] = self.proccessing_live_side(self.current_camera_imgs[direction])
                        proccessing_functions[direction](self.current_camera_imgs[direction])
                        #print(direction, draw_imgs[direction].shape)        
                
                # except:
                   
                #     print('set_images ERROR'*50)
                #     self.current_camera_imgs[direction] = np.zeros(shape=(1920,1200),dtype='uint8')
                #     results[direction] = []
                #     draw_imgs[direction] = np.zeros(shape=(1920,1200,3),dtype='uint8')


                
                


        elif self.ui.stackedWidget.currentWidget()==self.ui.page_camera_setting:

            if self.play_pause_status:
                #print('play')
                for direction in ['top', 'side']:
                    try:
                        self.current_camera_imgs[direction] = self.cameras[direction].image
                    except:
                        self.current_camera_imgs[direction] = np.zeros(shape=(1920,1200),dtype='uint8')


                    self.ui.set_image_label(self.ui.camera_setting_picture[direction], self.current_camera_imgs[direction])

                if self.win_fullscreen.isVisible():
                    self.update_fullscreen_img()
                


        elif self.ui.stackedWidget.currentWidget()==self.ui.page_detection_mode:


            self.get_picture_detection_page()



        self.during_set_image = False

#------------------------------------------------------------------------------------------------------------------------
# NEW----------------------------------------------------------------


    def show_full_screen(self,direction):


        self.full_screen_direction = direction
        self.win_fullscreen.show()
    
    def update_fullscreen_img(self):
        #print('updatessss')
        self.win_fullscreen.show_image(self.current_camera_imgs[self.full_screen_direction])
        #cv2.imshow('a', self.current_camera_imgs[self.full_screen_direction])
        #cv2.waitKey(30)

    def enable_live_view_for_tools(self):
        self.tools_live_enable = not(self.tools_live_enable)

        try:
            if self.tools_live_enable:
                for direction in self.cameras.keys():
                    try:
                        self.cameras[direction].off_trigger()
                    except:
                        print('ERROR: enable_live_view_for_tools off trigger error')

            
            else:
                if not self.image_trigger_mode:
                    self.update_main_image()
                    for direction in self.cameras.keys():
                        if self.direction_sensor_mode == direction:
                            try:
                                self.cameras[direction].on_trigger()
                            except:
                                print('ERROR: enable_live_view_for_tools on trigger error')
                        else:
                            try:
                                self.cameras[direction].off_trigger()
                            except:
                                print('ERROR: enable_live_view_for_tools on trigger error')

        except:
            print('ERROR: set trigger - enable_live_view_for_tools', direction)
        self.update_main_image()
        


    def plc_on_off_reg(self, name):
        def func():
       
            path=eval('self.ui.line_{}.text()'.format(name))
            value=self.my_plc.get_value(int(path))
            self.my_plc.set_value(int(path), not(value))
            self.plc_reg_on_off_style_manager(name, not(value))
            
            
        return func
    
    
    def plc_reg_on_off_style_manager(self, name, value):
        # return
        if not value:
                self.plc_reg_on_off_btns[name].setText('On')
                self.plc_reg_on_off_btns[name].setStyleSheet("QPushButton{background-color: #22824d;color:#ffffff}")
        else:
            self.plc_reg_on_off_btns[name].setText('Off')
            self.plc_reg_on_off_btns[name].setStyleSheet("QPushButton{background-color: #b8182b;color:#ffffff}")

    def check_rejection(self, result: dict):
        for side in result.keys():
            for feature in result[side]:
                if feature['avg'] < 0:
                    continue
                if self.avrage_mode:
                    if feature['avg'] < feature['limit_min'] or feature['avg'] > feature['limit_max']:
                        return True

                else:
                    if feature['min'] < feature['limit_min']:
                        return True
                    
                    if feature['max'] > feature['limit_max']: 
                        return True
                
            # self.his
        return False


    def complete_proccessing(self, direction, results):

        self.p_finished[direction] = True

        #both_results = {}
        self.both_results[direction] = results

        if self.p_finished['top'] and self.p_finished['side']:
        
            worker = {
                'top': self.worker_p_top,
                'side': self.worker_p_side
            }

            for direction in ['top', 'side']:
                draw_img = worker[direction].draw_img

                if not self.ui.btn_enabel_mask_draw_live[direction].isChecked():
                    draw_img = self.current_camera_imgs[direction]
                    # draw_img = cv2.rotate( draw_img, cv2.ROTATE_90_COUNTERCLOCKWISE )


                self.ui.set_live_table( self.ui.table_live_page[direction], self.both_results[direction], avg_mode=self.avrage_mode )
                self.ui.set_image_label( self.ui.label_img_live[direction], draw_img )


            if self.check_rejection( self.both_results) and not self.realtime_measurment:
                print('reject')
                self.start_reject()
            
            self.p_finished['top'] = False
            self.p_finished['side'] = False
            self.p_is_during['top'] = False
            self.p_is_during['side'] = False
            self.both_results = {}


    def get_picture_detection_page(self):
        

        direction,thresh_min,thresh_max,area_thresh=self.ui.ret_selected_camera_sensor_detect_page()
        img = self.current_camera_imgs[direction].copy()
       
        self.rect_roi_drawing_sensor_detection_page.set_img_size( img.shape[:2] )
        shapes = self.rect_roi_drawing_sensor_detection_page.shapes

        if len(shapes)>0:
            flag, area, res = proccessings.preprocessing_sensor_detection(
                img,
                thresh_min=thresh_min,
                thresh_max=thresh_max,
                area_thresh=area_thresh,
                rect_roi=shapes[0],
                draw=True
            )
            #print('flag',flag,'a',area) #print trig
            self.ui.selected_area.setText(str(area))
        else:
            res = img.copy()
        res = self.rect_roi_drawing_sensor_detection_page.get_image(res)
        self.ui.set_image_label(self.ui.camera_detection_mode_picture,res)



    def load_detection_parms(self):

        self.rect_roi_drawing_sensor_detection_page = Drawing.drawRect()

        parms = self.db.load_senser_detection()

        rect_roi = [[parms['x1'],parms['y1']],[parms['x2'],parms['y2']]]

        self.rect_roi_drawing_sensor_detection_page.shapes = [rect_roi]

        self.sensor_detection_values={'rect_roi':rect_roi,
                                      'thresh_min':parms['thresh_min'],
                                      'thresh_max':parms['thresh_max'],
                                      'area_thresh':parms['area']}
        
        self.direction_sensor_mode = parms['direction']
        self.image_trigger_mode = int(parms['sensor'])


    def set_detection_parms(self):

        self.ui.thresh_min_detection_page.setValue(int(self.sensor_detection_values['thresh_min']))
        self.ui.thresh_max_detection_page.setValue(int(self.sensor_detection_values['thresh_max']))
        self.ui.spin_area_detection_page.setValue(int(self.sensor_detection_values['area_thresh']))
        self.rect_roi_drawing_sensor_detection_page.shapes = [self.sensor_detection_values['rect_roi']]
        self.ui.set_trigger_mode(self.image_trigger_mode)
        self.ui.set_camera_sensor_detection_page(self.direction_sensor_mode)


    def save_detection_parms (self):

        if len(self.rect_roi_drawing_sensor_detection_page.shapes)>0:

            [x1,y1],[x2,y2] = self.rect_roi_drawing_sensor_detection_page.shapes[0]
            area = self.ui.spin_area_detection_page.value()
            thresh_min = self.ui.thresh_min_detection_page.value()
            thresh_max = self.ui.thresh_max_detection_page.value()
            image_trigger_mode = self.ui.ret_sensor_mode()
            direction = self.ui.ret_direction_sensor_detect()

            if image_trigger_mode==0 and direction=='side':
                self.ui.set_camera_sensor_detection_page('top')
                return



            values = {'x1':x1,
                    'y1':y1,
                    'x2':x2,
                    'y2':y2,
                    'area':area,
                    'thresh_min':thresh_min,
                    'thresh_max':thresh_max,
                    'sensor':image_trigger_mode,
                    'direction':direction,
                    }
        for direction in ['top', 'side']:
            parm = self.db.load_cam_params(direction)
            if image_trigger_mode == 0:
                if direction == 'side':
                    parm['trigger_mode'] = 'Off'
                elif direction =='top':
                    parm['trigger_mode'] = 'On'
            
            else:
                parm['trigger_mode'] = 'Off'
                
                    
            res = camera_funcs.set_camera_params_to_db(db_obj=self.db, camera_id=parm['id'], camera_params=parm)

        self.db.set_senser_detection(values=values)
        self.load_detection_parms()
        self.load_camera_params_from_db_to_camera()

    def refresh_sensor_image_page(self,):
        self.load_detection_parms()
        self.set_detection_parms()
        self.get_picture_detection_page()







    def hide_objs(self,status=False):
        self.ui.checkbox_page0_0_top.setVisible(status)
        self.ui.checkbox_page0_1_top.setVisible(status)
        self.ui.checkbox_page0_1_side.setVisible(status)
        self.ui.frame_226.setVisible(status)
        self.ui.frame_225.setVisible(status)
        self.ui.frame_201.setVisible(status)   #side calib
        self.ui.frame_206.setVisible(status)   #side calib
        self.ui.frame_155.setVisible(status)   #top calib
        self.ui.frame_196.setVisible(status)   #top calib
        self.ui.reject_btn.setVisible(status)
















from PySide6.QtCore import Signal, QThread, QObject
class processingTopWorker(QObject):
    finished = Signal()
    complete = Signal(str, list)

    def __init__(self,screw_json, img, calib_value) -> None:
        super(processingTopWorker, self).__init__()
        self.screw_json = screw_json
        self.img = img
        self.calib_value = calib_value
        self.draw_img = img.copy()
        self.results = []


    @time_measure
    def run(self, ):
        self.results = []
        try:
            self.img, self.draw_img = proccessings.preprocessing_0_top_img(self.img, self.screw_json, self.draw_img)
            self.img , mask_roi, self.draw_img = proccessings.preprocessing_1_top_img(self.img, self.screw_json, self.draw_img, centerise=True)

            for active_tool in self.screw_json.get_active_tools():
                results_tools, self.draw_img = proccessings.tools_dict_top[active_tool]( self.img, mask_roi, self.screw_json, self.draw_img , self.calib_value)

                for i in range(len(results_tools)) :

                    tools_name =results_tools[i]['name']
                    # if ' ' in tools_name:
                    #     tools_name =tools_name.split(' ')[1]
                    # if tools_name in proccessings.calib_dict_top:
                    #     for key,value in results_tools[i].items():
                    #         if key!='name' :
                    #             results_tools[i][key]=round(proccessings.calib_dict_top[tools_name](value,self.calib_value), 2)
                            
                self.results.extend(results_tools)

            self.results.sort( key = lambda x:x['name'])
        except Exception as e:
            print(e)

        finally:
            self.complete.emit('top', self.results)
            self.finished.emit()




class processingSideWorker(QObject):
    finished = Signal()
    complete = Signal(str, list)

    def __init__(self,screw_json, img, calib_value) -> None:
        super(processingSideWorker, self).__init__()
        self.screw_json = screw_json
        self.img = img
        self.calib_value = calib_value
        self.draw_img = img.copy()
        self.results = []
        


    @time_measure
    def run(self,):
        try:
            self.img, mask_roi,_ = proccessings.preprocessing_side_img( self.img, self.screw_json )

            self.draw_img = self.img.copy()
            self.draw_img = Utils.mask_viewer(self.draw_img, mask_roi, color=(0,10,150))
        
            for active_tool in self.screw_json.get_active_tools():
                results_tools, self.draw_img = proccessings.tools_dict_side[active_tool]( self.img, mask_roi, self.screw_json, self.draw_img , self.calib_value )

                # for i in range(len(results_tools)) :

                #     tools_name =results_tools[i]['name']
                #     if ' ' in tools_name:
                #         tools_name =tools_name.split(' ')[1]

                #     if tools_name in proccessings.calib_dict_side:
                #         for key,value in results_tools[i].items():
                #             if key != 'name':
                #                 results_tools[i][key]=round(proccessings.calib_dict_side[tools_name](value,self.calib_value),2)
                self.results.extend(results_tools)

            self.results.sort( key = lambda x:x['name'])

        except Exception as e:
            print(e)

        finally:
            self.complete.emit('side', self.results)
            self.finished.emit()