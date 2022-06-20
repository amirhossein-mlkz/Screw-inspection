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

from PySide6 import QtCore as sQtCore
from functools import partial
import numpy as np
import random

import database_utils
import cv2

import login_UI
import confirm_UI
from backend import camera_funcs, colors_pallete, confirm_window_messages, mainsetting_funcs\
                    , user_login_logout_funcs, user_management_funcs, Screw, Utils, Drawing, cvTools, mathTools, proccessings

from backend.mouse import Mouse

from full_screen_UI import FullScreen_UI
import texts

from database import database, dbUtils, screwDB
import copy
import platform
from Keys import set_dimensions
class API:

    def __init__(self,ui):
        self.sides=['side','top']
        #------------------------------------------------------------------------------------------------------------------------
        # UIs of the app
        # main settings UI
        self.ui = ui
        # login window UI and API
        self.login_ui = login_UI.UI_main_window()
        # confirmation window UI
        self.confirm_ui = confirm_UI.UI_main_window()

        #------------------------------------------------------------------------------------------------------------------------
        # APIs of the app
        self.login_api = login_UI.login_api.API(self.login_ui)
        
        #------------------------------------------------------------------------------------------------------------------------
        # database module api
        
        os=platform.platform()
        if os[:5] =='Linux':


            self.db = database_utils.dataBaseUtils(password='password')
        
        else:
            self.db = database_utils.dataBaseUtils(password='@mm@9398787515AmmA')
            #self.db = database_utils.dataBaseUtils(password='root')

        #------------------------------------------------------------------------------------------------------------------------
        # start-up functions
        # get available cameras and update database
        self.available_camera_serials = camera_funcs.get_available_cameras_list_serial_numbers()
        # camera_funcs.update_available_camera_serials_on_db(db_obj=self.db, available_serials=self.available_camera_serials)
        # assign base parameters to UI
        mainsetting_funcs.assign_appearance_existing_params_to_ui(ui_obj=self.ui)
        # load and apply program appearance params
        self.load_appearance_params_on_start()
        # refresh dashboard

        # function to active the UI buttons functionality
        self.button_connector()

        self.language='en'
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


        # load image must change

        self.test()
        # self.show_full_screen('fullscreen_cam_1')
        #-------------------------------------------------------------------------------------------------------------------
        
        self.mouse = Mouse()
        self.rect_roi_drawing = Drawing.drawRect()
        self.circle_roi_drawing = Drawing.drawCircel()
        self.poly_roi_drawing = Drawing.drawPoly()
        
        self.roi_drawings = {
            'rect' : self.rect_roi_drawing, 
            'circle': self.circle_roi_drawing,
            'poly' : self.poly_roi_drawing
        }
        
        self.current_image_screw = None
        self.rotate_correction = False
        #-------------------------------------------------------------------------------------------------------------------
        self.ui.set_combo_boxes(self.ui.comboBox_edit_remove, dbUtils.get_screws_list())
        self.load_live_page_infoes()

        self.mouse.connect_all(self.ui.label_image_grab_page, self.image_setting_mouse_event)
        
        
        #???????????????????????????????????????????????//
        #self.proccessing_live(None,None)
        

        # set_load live images
        #self.set_load_imgs_live()
        
        

        #-------------------------------------------------------------------------------------------------------------------

    def test(self):
        pass
        path = 'images/test1_0_12 - Copy.png'

        self.ui.line_img_path0_1_side.setText(path)
  

    # functions
    #------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------------
    # button connector for activating UI buttons functionality
    def button_connector(self):
        
        #--------------------------------------amir---------------------------------------
        
        
        
        
        # login button
        self.ui.main_login_btn.clicked.connect(partial(lambda: user_login_logout_funcs.run_login_window(ui_obj=self.ui, login_ui_obj=self.login_ui, confirm_ui_obj=self.confirm_ui)))

        # camera buttons in the camera-settings section
        for cam_id in camera_funcs.all_camera_ids:
            eval('self.ui.camera%s_btn' % cam_id).clicked.connect(partial(self.load_camera_params_from_db_to_UI))

        # camera-parametrs or UI page change disconnect camera
        # disconnect camera on UI change
        self.ui.serial_number_combo.currentTextChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.gain_spinbox.valueChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.expo_spinbox.valueChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.width_spinbox.valueChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.height_spinbox.valueChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.offsetx_spinbox.valueChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.offsety_spinbox.valueChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.maxbuffer_spinbox.valueChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.packetdelay_spinbox.valueChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.packetsize_spinbox.valueChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.transmissiondelay_spinbox.valueChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.trigger_combo.currentTextChanged.connect(self.disconnect_camera_on_ui_change)
        self.ui.stackedWidget.currentChanged.connect(self.things_to_do_on_stackwidject_change)


        # buttons in the camera-settings section
        self.ui.camera_setting_apply_btn.clicked.connect(partial(self.save_changed_camera_params))
        self.ui.camera_setting_connect_btn.clicked.connect(partial(self.connect_dissconnect_to_camera))
        self.ui.camera_setting_getpic_btn.clicked.connect(partial(self.show_camera_picture))



        # login window and confirm window
        self.login_ui.login_btn.clicked.connect(partial(lambda: user_login_logout_funcs.authenticate_user(ui_obj=self.ui, login_ui_obj=self.login_ui, login_api_obj=self.login_api)))
        self.confirm_ui.yes_btn.clicked.connect(partial(self.confirm_yes))
        self.confirm_ui.no_btn.clicked.connect(partial(self.confirm_ui.close))

        # User managment
        self.ui.side_users_setting_btn.clicked.connect(partial(self.refresh_users_table))
        self.ui.remove_user_btn.clicked.connect(partial(self.remove_users))
        self.ui.create_user.clicked.connect(partial(self.add_user))

        
        # general-settings

        self.ui.btn_set_szies.clicked.connect(self.set_apply_imgs_live)

        self.ui.setting_color_comboBox.currentTextChanged.connect(lambda: mainsetting_funcs.update_combo_color(ui_obj=self.ui))
        self.ui.setting_fontstyle_comboBox.currentTextChanged.connect(lambda: mainsetting_funcs.update_combo_fontstyle(ui_obj=self.ui))
        self.ui.setting_fontsize_comboBox.currentTextChanged.connect(lambda: mainsetting_funcs.update_combo_fontsize(ui_obj=self.ui))
        self.ui.setting_appearance_apply_btn.clicked.connect(lambda: self.apply_changed_appearance_params(mode='appearance'))
        self.ui.setting_calibration_apply_btn.clicked.connect(lambda: self.apply_changed_appearance_params(mode='calibration'))
        self.ui.setting_imageprocessing_apply_btn.clicked.connect(lambda: self.apply_changed_appearance_params(mode='imageprocessing'))
        
        self.ui.side_general_setting_btn.clicked.connect(lambda: self.load_appearance_params_on_start(mainsetting_page=True))

        #Fullscreen  
        self.ui.fullscreen_cam_1.clicked.connect(lambda: self.show_full_screen(self.ui.fullscreen_cam_1))
        self.ui.fullscreen_cam2.clicked.connect(lambda: self.show_full_screen(self.ui.fullscreen_cam2))
        self.ui.fullscreen_page_tools.clicked.connect(lambda: self.show_full_screen(self.ui.fullscreen_page_tools))


        #tools page

        self.ui.save_new_btn.clicked.connect(self.add_new_screw)
        self.ui.edit_remove_btn.clicked.connect(self.get_screw_names)
        self.ui.edit_btn.clicked.connect(self.edit_load_screw)
        self.ui.remove_screw_btn.clicked.connect(self.remove_screw)

        self.ui.get_main_parms_screw_top()


        # publice setting-------------------------------------------------------
        

        #Page 1_top----------------------------------------------------------
      
        
        #self.ui.btn_set_image0_1_top.clicked.connect(self.update_main_image)
        #self.ui.btn_page_1_top.clicked.connect(self.update_setting_page_info)
        
        self.ui.connect_btn('set_img', self.update_main_image )
        self.ui.connect_btn('page', self.update_setting_page_info)     
        self.ui.connect_sliders('thresh',  self.update_threshould)
        self.ui.connect_sliders('noise_filter',  self.update_noise_filter)
        self.ui.checkbox_connect('thresh_inv', self.update_thresh_inv )
        self.ui.connect_list_pack('sub_pages', self.update_list_name )
        self.ui.connect_limit_spin(self.update_limit)
        self.ui.connect_spins_parm(self.update_numerical_parms)
        self.ui.btn_enabel_mask_draw.toggled.connect(self.setting_image_updater)
        self.ui.checkbox_connect('other', self.update_sepc_checkboxes)
        
        self.ui.roi_connect(self.update_roi_input)        
        self.ui.save_btn_page_grab.clicked.connect(self.save_screw)
        
        


        self.ui.side_dashboard_btn.clicked.connect(self.load_live_page_infoes)


        # Live Page

        self.ui.lives['combo_boxes']['screw_list'].currentTextChanged.connect(self.load_screw_live )
        self.ui.btn_capture_screw_live.clicked.connect(self.save_live_image)



        # self.ui.connect_sliders('thresh',self.update_threshould)

        #setting page2
        #self.ui.threshouldSetingPage2_slider.valueChanged.connect(self.update_threshould_setting_page2)   
        #self.ui.page2_noise_filter_top_Slider.valueChanged.connect(self.update_noise_filter_setting_page2)   

        # self.ui.get_sliders('thresh')
        
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
            parms=self.db.get_size_table('{}_live'.format(side))[0]
            #self.ui.load_sizes(parms,'{}'.format(side))
            parms_.append(parms)

        set_dimensions(self.ui,parms_[0],parms_[1])

        
    def set_apply_imgs_live(self):

        side_parms,top_parms=self.ui.get_sizes_parms()

        self.db.set_size_table_side(side_parms)
        self.db.set_size_table_top(top_parms)
        self.set_load_imgs_live()



    #------------------------------------------------------------------------------------------------------------------------   


    # camera functions in the camera setting page
    #------------------------------------------------------------------------------------------------------------------------   
    # # apply camera parameters to camera(s) (in database) on apply button click
    def save_changed_camera_params(self, apply_to_multiple=False):
        # get camera-id and camera params
        camera_id = camera_funcs.get_camera_id(self.ui.cameraname_label.text())
        camera_params = camera_funcs.get_camera_params_from_ui(ui_obj=self.ui)
        # validating camera parameters
        validate, message = camera_funcs.validate_camera_ip(db_obj=self.db, camera_id=camera_id, camera_params=camera_params)
        if not validate:
            self.ui.show_mesagges(self.ui.camera_setting_message_label, message, color=colors_pallete.failed_red)
            return
        # set to database
        checkbox_values = camera_funcs.get_camera_checkbox_values(ui_obj=self.ui)
        # camera checkboxes are not checked
        if checkbox_values == 0 or apply_to_multiple: 
            res = camera_funcs.set_camera_params_to_db(db_obj=self.db, camera_id=camera_id, camera_params=camera_params, checkbox_values=checkbox_values)
            if res:
                self.ui.show_mesagges(self.ui.camera_setting_message_label, 'Settings Applied Successfully', color=colors_pallete.successfull_green)
            else:
                self.ui.show_mesagges(self.ui.camera_setting_message_label, 'Failed to Apply Settings', color=colors_pallete.failed_red)
        # camera checkboxes are checked (apply settings to multiple cameras)
        else: 
            if checkbox_values == 1: # apply to top cameras
                self.confirm_ui.msg_label.setText(confirm_window_messages.setting_topcameras_confirm_message)
            elif checkbox_values == 2: # apply to bottom cameras
                self.confirm_ui.msg_label.setText(confirm_window_messages.setting_bottomcameras_confirm_message)
            elif checkbox_values == 3: # apply to all cameras
                self.confirm_ui.msg_label.setText(confirm_window_messages.setting_allcameras_confirm_message)
            self.confirm_ui.show()


    # get cameras parameters from database given camera-id and apply to UI
    def load_camera_params_from_db_to_UI(self):
        # disconnect camera if connected:
        if self.ui.camera_connect_flag:
            camera_funcs.connect_disconnect_camera(ui_obj=self.ui, db_pbj=self.db, serial_number='0', connect=False, current_cam_connection=self.camera_connection)
            camera_funcs.update_ui_on_camera_connect_disconnect(ui_obj=self.ui, api_obj=self, connect=False)
            if not self.ui.camera_setting_connect_btn.isEnabled():
                self.ui.camera_setting_connect_btn.setStyleSheet("background-color:{}; border:Transparent".format(colors_pallete.disabled_btn))
        # get camera-id and camera params
        camera_id = camera_funcs.get_camera_id(self.ui.cameraname_label.text())
        camera_params = camera_funcs.get_camera_params_from_db(db_obj=self.db, camera_id=camera_id)
        # set to UI
        if len(camera_params) != 0:
            camera_funcs.set_camera_params_to_ui(ui_obj=self.ui, db_obj=self.db, camera_params=camera_params, camera_id=camera_id, available_serials=self.available_camera_serials)

    
    # connect to cameras given entered serial number and camera parameters
    def connect_dissconnect_to_camera(self, calibration=False):
        # get camera parametrs on camera-settings page
        if not calibration:
            camera_serial_number = camera_funcs.get_camera_params_from_ui(ui_obj=self.ui)['serial_number']
        # get camera parametrs on calibration-settings page
        else:
            camera_id = self.ui.comboBox_cam_select_calibration.currentText()
            camera_serial_number = camera_funcs.get_camera_params_from_db(db_obj=self.db, camera_id=camera_id)['serial_number']
        # check if serial is assigned
        if camera_serial_number == '0':
            if not calibration:
                self.ui.show_mesagges(self.ui.camera_setting_message_label, 'No Serial is Assigned', color=colors_pallete.failed_red)
            else:
                self.ui.show_mesagges(self.ui.camera_calibration_message_label, 'No Serial is Assigned, Please Reffer to Camera-Settings', color=colors_pallete.failed_red)
        else:
            # connect to camera
            if not self.ui.camera_connect_flag:
                if not calibration:
                    self.camera_connection = camera_funcs.connect_disconnect_camera(ui_obj=self.ui, db_pbj=self.db, serial_number=camera_serial_number, connect=True, current_cam_connection=None)
                    camera_funcs.update_ui_on_camera_connect_disconnect(ui_obj=self.ui, api_obj=self, connect=True)
                else:
                    self.camera_connection = camera_funcs.connect_disconnect_camera(ui_obj=self.ui, db_pbj=self.db, serial_number=camera_serial_number, connect=True, current_cam_connection=None, calibration=True)
                    camera_funcs.update_ui_on_camera_connect_disconnect(ui_obj=self.ui, api_obj=self, connect=True, calibration=True)
            # disconnect from camera
            else:
                if not calibration:
                    camera_funcs.connect_disconnect_camera(ui_obj=self.ui, db_pbj=self.db, serial_number=camera_serial_number, connect=False, current_cam_connection=self.camera_connection)
                    camera_funcs.update_ui_on_camera_connect_disconnect(ui_obj=self.ui, api_obj=self, connect=False)
                else:
                    camera_funcs.connect_disconnect_camera(ui_obj=self.ui, db_pbj=self.db, serial_number=camera_serial_number, connect=False, current_cam_connection=self.camera_connection, calibration=True)
                    camera_funcs.update_ui_on_camera_connect_disconnect(ui_obj=self.ui, api_obj=self, connect=False, calibration=True)


    # show cameras picture on UI
    def show_camera_picture(self, calibration=False):
        # set soft-calibration buttons enavle/disable
        self.ui.calib_rotate_spinbox.setEnabled(True)
        self.ui.calib_shifth_spinbox.setEnabled(True)
        self.ui.calib_shiftw_spinbox.setEnabled(True)
        self.ui.calib_radio_corsshair.setEnabled(True)
        self.ui.calib_radio_grid.setEnabled(True)
        self.pxcalibration_step = 0
        self.ui.pixelvalue_prev_btn.setEnabled(False)
        self.ui.pixelvalue_next_btn.setEnabled(True)
        #
        while True and self.ui.camera_connect_flag:
            # get picture
            live_image = camera_funcs.get_picture_from_camera(self.camera_connection)
            # set/show picture to UI
            if not calibration:
                camera_funcs.set_camera_picture_to_ui(ui_image_label=self.ui.camera_setting_picture_label, image=live_image)
            else:
                self.apply_calibration_on_image(live_image)
                #cameras.set_camera_picture_to_ui(ui_image_label=self.ui.calib_camera_image, image=live_image)
            cv2.waitKey(self.update_picture_delay) # must change
            if calibration:
                self.ui.calibration_image = cv2.cvtColor(live_image, cv2.COLOR_BGR2GRAY)
                break

    
    # disconnect camera on UI change
    def disconnect_camera_on_ui_change(self):
        if self.ui.camera_connect_flag:
            camera_funcs.connect_disconnect_camera(ui_obj=self.ui, db_pbj=self.db, serial_number='0', connect=False, current_cam_connection=self.camera_connection)
            camera_funcs.update_ui_on_camera_connect_disconnect(ui_obj=self.ui, api_obj=self, connect=False)
            camera_funcs.update_ui_on_camera_connect_disconnect(ui_obj=self.ui, api_obj=self, connect=False, calibration=True)
            self.ui.camera_setting_connect_btn.setStyleSheet("background-color:{}; border:Transparent".format(colors_pallete.disabled_btn))


 

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
        elif mode == 'calibration':
            message_label = self.ui.general_setting_calibration_message_label
            params = mainsetting_funcs.get_calibration_params_from_ui(ui_obj=self.ui)
        elif mode == 'imageprocessing':
            message_label = self.ui.setting_imageprocessing_message_label
            params = mainsetting_funcs.get_image_procesing_params_from_ui(ui_obj=self.ui)
        elif mode == 'defects':
            message_label = self.ui.setting_defect_message_label
            params = mainsetting_funcs.get_defects_params_from_ui(ui_obj=self.ui)
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

    #------------------------------------------------------------------------------------------------------------------------
    # NEW----------------------------------------------------------------


    def show_full_screen(self,cam_num):
        

        # fullscreen_dict={'fullscreen_cam_1':self.image_cam_1,'fullscreen_cam2':self.image_cam_2,'fullscreen_page_tools':self.ui.img_page_tool}
        fullscreen_dict={'fullscreen_page_tools':self.ui.img_page_tool}
        print('cam_num',fullscreen_dict[str(cam_num.objectName())])
        self.win_fullscreen = FullScreen_UI(fullscreen_dict[str(cam_num.objectName())])
        # full_screen_obj.show()
        self.win_fullscreen.show()



    

    
    


    



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
        flag = dbUtils.add_screw(name)
        self.ui.set_combo_boxes(self.ui.comboBox_edit_remove, dbUtils.get_screws_list())
        self.screw_jasons = {'top': screwDB.screwJson() , 'side': screwDB.screwJson() }
        
        for key in self.screw_jasons.keys():
            path = dbUtils.get_screw_path( name )
            self.screw_jasons[key].set_name(name)
            self.screw_jasons[key].set_direction( key )
            self.screw_jasons[key].write(path)
            
        if not flag:
            print('Error! : screw exist already')
        self.update_setting_page_info()
    
    
    def save_screw(self):
        if self.ui.editmode:
            flag = self.ui.show_save_question('Save Screw', 'Do you want to Save screw ?')
        # try:
            if flag:
                for key in self.screw_jasons.keys():
                    
                    activate_tools = self.ui.get_activate_pages(direction = key)
                    print(key, activate_tools)
                    self.screw_jasons[key].set_active_tools(activate_tools)
                    path = dbUtils.get_screw_path( self.screw_jasons[key].get_name() )
                    self.screw_jasons[key].write(path)  
    
                print('Screw Saved')
                self.ui.show_warning('Save Screw','Successfully Save')
                self.ui.editmode=False
                self.ui.set_label(self.ui.label_status_mode,'')   
                self.ui.stackedWidget_2.setCurrentIndex(0)
                # frame_save_btns
                self.ui.frame_size(self.ui.frame_save_btns,0)
                self.ui.tool_btn_clear()
                self.ui.enable_bar_btn_tool_page('top',False)   
                self.ui.enable_bar_btn_tool_page('side',False)  
                self.ui.set_combo_boxes(self.ui.comboBox_edit_remove, dbUtils.get_screws_list())

            if flag==False:

                print('disacrd')
                self.ui.show_warning('Save Screw','Screw Settings Restored')

            if flag==None:

                print('cancel')
            
            # except:
            #     self.ui.set_warning('Save Eror','tool_page',level=2)
            #     self.ui.show_warning('Save Screw','Eror Save')
        else :
            self.ui.show_warning('Save Screw','First Edit Mode')
            
    def remove_screw(self):
        name=self.ui.label_screw_name.text()
        flag = self.ui.show_question('Delete Screw', 'Are you Sure to delete {}?'.format(name))
        if flag:
            dbUtils.remove_screw(name)
            self.ui.set_combo_boxes(self.ui.comboBox_edit_remove, dbUtils.get_screws_list())
            
            
            
    def edit_load_screw(self):
        name = self.ui.comboBox_edit_remove.currentText()
        path = dbUtils.get_screw_path(name)
        self.screw_jasons = {'top': screwDB.screwJson() , 'side': screwDB.screwJson() }
        
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

        self.update_setting_page_info()
        
        
    def image_setting_mouse_event(self,wname):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        mouse_status = self.mouse.get_status()
        mouse_button = self.mouse.get_button()
        mouse_pt = self.mouse.get_relative_position()
        mouse_real_pt=self.mouse.get_position()

        if page_name in ['1_top', '1_side', '2_side', '3_side', '4_side', '5_side', '6_side']:
            shape_type = 'rect'
            max_count = 1        
        
        self.update_roi_mouse(mouse_status, mouse_button , mouse_pt, shape_type, max_count)

        #-------------------------------------------------------------------------
        color = cvTools.get_gray_color( self.current_image_screw, mouse_pt )
        img = cvTools.build_gcolor_img( color, color_type='rgb' )

        self.ui.update_mouse_position_tool_page(mouse_real_pt)
        self.ui.set_color_value_image_tool_page(color,img)

        

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
                
                else:
                    print('Input valid name')
                    
                
            
            elif action == 'remove':
                input_name = self.ui.get_selected_list_pack_item('sub_pages')
                self.screw_jasons[ direction ].remove_subpage(page_name, input_name)
                items = self.screw_jasons[ direction].get_subpages(page_name)
                self.ui.set_list_pack_items( 'sub_pages', items )
            
            self.update_setting_page_info()    

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
        
    
    def update_threshould(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        #---------------------
        if page_name in ['2_side', '3_side', '4_side','5_side','6_side']:
            page_name , subpage_name = '1_side', None
        #---------------------
        thresh = self.ui.get_sliders_value('thresh')
        self.screw_jasons[ direction ].set_thresh( page_name, subpage_name, thresh )   
        self.setting_image_updater()
    
     

    def update_noise_filter(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        noise_filter = self.ui.get_sliders_value('noise_filter')
        self.screw_jasons[ direction ].set_noise_filter( page_name, subpage_name, noise_filter )  
        
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
            print(name, state)
        return func
        
        
    def update_roi_input(self, name):
        def func():
            page_name = self.ui.get_setting_page_idx(page_name = True)
            direction = self.ui.get_setting_page_idx(direction = True)
            subpage_name = self.ui.get_sub_page_name( page_name )
            
            data = self.ui.get_roi_value()
            rect = self.screw_jasons[ direction ].get_rect_roi(page_name, subpage_name)
            
            rect_dict = Utils.rect_list2dict(rect)
            rect_dict[name] = data[name]
            rect = Utils.rect_dict2list(rect_dict)

            #print(self.rect_roi_drawing.shapes)
            self.rect_roi_drawing.update_shape(shape_idx=0,  shape=rect)            
            self.screw_jasons[direction].set_rect_roi( page_name, subpage_name, pt1=rect[0], pt2=rect[1])
            
            self.setting_image_updater()
        return func



    def update_roi_mouse(self, mouse_status, mouse_button, mouse_pt, shape_type, max_count):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        self.roi_drawings[ shape_type ].max_shape_count = max_count
        self.roi_drawings[shape_type].qtmouse_checker( mouse_status, mouse_button, mouse_pt )
        shapes = self.roi_drawings[shape_type].shapes
        if len(shapes) > 0:
            if shape_type == 'rect':
                rect = shapes[0]
                rect_dict = Utils.rect_list2dict(rect)
                self.screw_jasons[direction].set_rect_roi( page_name, subpage_name, pt1=rect[0], pt2=rect[1] )
                self.ui.set_roi_value(rect_dict)
        
        else:
            self.screw_jasons[direction].set_rect_roi( page_name, subpage_name, [],[] )
        self.setting_image_updater()
        
    
    def update_main_image(self):
        direction = self.ui.get_setting_page_idx(direction = True)
        page_name = self.ui.get_setting_page_idx(page_name = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        path = self.ui.get_line_value('img_path')
        
        if cv2.imread(path) is not None:
            self.screw_jasons[ direction ].set_img_path(path, page_name, subpage_name)
            self.current_image_screw = cv2.imread(path)
            self.rect_roi_drawing.set_img_size( self.current_image_screw.shape[:2] )
            self.setting_image_updater()
        else:
            print('Error! : image not exist')
            
        
    
    def update_setting_page_info(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )

        #-----------loade subpages name list --------------------
        if subpage_name is not None:
            items = self.screw_jasons[ direction].get_subpages(page_name)
            if len(items) > self.ui.get_selected_list_pack_count('sub_pages'):
                self.ui.set_list_pack_items( 'sub_pages', items )
                subpage_name = self.ui.get_sub_page_name( page_name )
        #-----------loade limits --------------------

        parms = self.screw_jasons[ direction ].get_setting( page_name, subpage_name )
        self.ui.set_setting_page_parms(parms)
        
        img_path = self.screw_jasons[ direction ].get_img_path()
        self.current_image_screw = cv2.imread(img_path)
        
        for drawer in self.roi_drawings.values():
            drawer.set_img_size( self.current_image_screw.shape[:2] )
        self.load_drawer()
        self.setting_image_updater()
        
        
    
    
    def load_drawer(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        for drawer in self.roi_drawings.values():
            drawer.clear()
        
        for feature_name,value in self.screw_jasons[direction].get_setting( page_name, subpage_name ).items():
            if 'rect_roi' in feature_name:
                if Utils.is_rect(value):
                    self.roi_drawings['rect'].shapes.append( value )
                    
    
    
    def setting_image_updater(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        if page_name == '1_top':
            self.update_image_1_top()
        elif page_name == '1_side':
            self.update_image_1_side()
        
        elif page_name == '2_side':
            self.update_image_2_side()
            
        elif page_name == '3_side':
            self.update_image_3_side()
        
        elif page_name == '4_side':
            self.update_image_4_side()

        elif page_name == '5_side':
            self.update_image_5_side()        
        
        elif page_name == '6_side':
            self.update_image_6_side()
    
    
        
    
    #____________________________________________________________________________________________________________
    #                                           
    #
    #                                          Image Drawings Function
    #
    #
    #____________________________________________________________________________________________________________
    def update_image_1_top(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = self.current_image_screw
        thresh = self.screw_jasons[ direction ].get_thresh(page_name, subpage_name)
        noise_filter = self.screw_jasons[ direction ].get_noise_filter( page_name, subpage_name )
        rect = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name)
        inv_state = self.screw_jasons[ direction ].get_thresh_inv(page_name, subpage_name)
        
        mask_roi = cvTools.rects2mask(img.shape[:2], [rect])
        thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        
        img = Utils.mask_viewer(img, thresh_img)
        img = self.rect_roi_drawing.get_image(img)
        
        self.ui.set_image_page_tool_labels(img)

        if Utils.is_rect( rect ) and np.count_nonzero(thresh_img) > 100:
            self.ui.enable_bar_btn_tool_page( direction, True )
        else:
            self.ui.enable_bar_btn_tool_page( direction, False )
            
            
        
    
    
    def update_image_1_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = self.current_image_screw
        thresh = self.screw_jasons[ direction ].get_thresh(page_name, subpage_name)
        noise_filter = self.screw_jasons[ direction ].get_noise_filter( page_name, subpage_name )
        rect = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name)
        inv_state = self.screw_jasons[ direction ].get_thresh_inv(page_name, subpage_name)
        
        mask_roi = cvTools.rects2mask(img.shape[:2], [rect])
        thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img)
        img = self.rect_roi_drawing.get_image(img)
        
        if Utils.is_rect( rect ) and np.count_nonzero(thresh_img) > 100:
            self.ui.enable_bar_btn_tool_page( direction, True )
        else:
            self.ui.enable_bar_btn_tool_page( direction, False )
        
        self.ui.set_image_page_tool_labels(img)
    
    
    
    def update_image_2_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw)
        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_img_json( img, json, direction  )
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(50,100,0))
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        rect_roi_2 = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name)
        if Utils.is_rect(rect_roi_2):
            left_pts, right_pts = cvTools.find_vertical_edges(thresh_img, rect_roi_2)
            if len(left_pts) > 0 and len(right_pts) > 0:
                img = cvTools.draw_vertical_point( img , [left_pts, right_pts], color=(0,0,255), thicknes=5 )
                #--------------------------------------------------------------------------------------
                #specific Operation
                #--------------------------------------------------------------------------------------
                min_dist, max_dist, avg_dist, _ = mathTools.horizontal_distance( left_pts, right_pts )

                info = {'min_lenght' : min_dist, 'max_lenght': max_dist, 'avg_lenght': avg_dist}                
                self.ui.set_stetting_page_label_info(info)
                
        img = self.rect_roi_drawing.get_image(img)
        self.ui.set_image_page_tool_labels(img)
        
        
    
    
    def update_image_3_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw)
        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_img_json( img, json, direction  )

        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(200,200,0))
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        rect_roi_2 = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name)
        jump_thresh = self.screw_jasons[ direction ].get_numerical_parm(page_name, subpage_name, 'jump_thresh')
        if Utils.is_rect(rect_roi_2):
            male_thread_l, male_thread_h = cvTools.find_screw_thread_top( thresh_img, rect_roi_2,  min_diff=jump_thresh)
            
            min_d,max_d, avg_d,_ = mathTools.vertical_distance( male_thread_h, male_thread_l )
            _,_,avg_l,_  = mathTools.thread_lenght( male_thread_h )

            info = {'thread_lenght': avg_l,  'count_thread':len(male_thread_h) , 'step_distance':avg_d}
            self.ui.set_stetting_page_label_info(info)
            
            img = cvTools.draw_points(img, male_thread_h, (0,50,150), 5)
            img = cvTools.draw_points(img, male_thread_l, (200,0,200), 5)
        
        

        img = self.rect_roi_drawing.get_image(img)
        self.ui.set_image_page_tool_labels(img)
        
        

        
    def update_image_4_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw)
        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_img_json( img, json, direction  )
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(100,30,0))
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        rect_roi_2 = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name)
        if Utils.is_rect(rect_roi_2):
            left_pts, right_pts = cvTools.find_horizental_edges( thresh_img, rect_roi_2)
            if len(left_pts) > 0 and len(right_pts) > 0:
                img = cvTools.draw_horizental_point( img, [left_pts, right_pts], (0,0,255), thicknes=5 )

                min_dist, max_dist, avg_dist, _ = mathTools.vertical_distance( left_pts, right_pts )
                print(min_dist, max_dist, avg_dist)
                info = {'min_diameter' : min_dist, 'max_diameter': max_dist, 'avg_diameter': avg_dist}                
                self.ui.set_stetting_page_label_info(info)       

        img = self.rect_roi_drawing.get_image(img)
        self.ui.set_image_page_tool_labels(img)




    def update_image_5_side(self,):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw)
        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_img_json( img, json, direction  )

        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(50,30,200))
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        rect_roi_2 = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name, )
        jump_thresh = self.screw_jasons[ direction ].get_numerical_parm(page_name, subpage_name, 'jump_thresh')
        if Utils.is_rect(rect_roi_2):
            left_pts, right_pts = cvTools.find_head_vertival_pts(thresh_img, rect_roi_2, jump_thresh, 0.25)
            if len(left_pts) > 0 and len(right_pts) > 0:
                img = cvTools.draw_vertical_point( img, [left_pts, right_pts], (50,255,0), thicknes=5 )

                min_dist, max_dist, avg_dist, _ = mathTools.horizontal_distance( left_pts, right_pts )
                print(min_dist, max_dist, avg_dist)
                info = {'min_head_height' : min_dist, 'max_head_height': max_dist, 'avg_head_height': avg_dist}                
                self.ui.set_stetting_page_label_info(info)           
        

        img = self.rect_roi_drawing.get_image(img)
        self.ui.set_image_page_tool_labels(img)




    def update_image_6_side(self,):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw)
        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_img_json( img, json, direction  )
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(100,200,50))
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        rect_roi_2 = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name, )
        if Utils.is_rect(rect_roi_2):
            area = cvTools.get_bigest_area( thresh_img, rect_roi_2 )
            info = {'area': area}
            self.ui.set_stetting_page_label_info(info)
            
            rect_roi_2_mask = cvTools.rects2mask( img.shape[:2], [rect_roi_2] )
            select_mask = cv2.bitwise_and(rect_roi_2_mask, thresh_img)
            img = Utils.mask_viewer(img, select_mask, color=(0,10,250))

        img = self.rect_roi_drawing.get_image(img)
        self.ui.set_image_page_tool_labels(img)
    # #____________________________________________________________________________________________________________
    # #                                           
    # #
    # #                                           Screw main Settin top
    # #
    # #
    # #____________________________________________________________________________________________________________

    

    # #____________________________________________________________________________________________________________
    # #                                           
    # #
    # #                                                 Live
    # #
    # #
    # #____________________________________________________________________________________________________________
    def load_live_page_infoes(self,):
        self.ui.set_combo_boxes(self.ui.combobox_select_screw_live, dbUtils.get_screws_list())



    def load_screw_live(self):
        name = self.ui.combobox_select_screw_live.currentText()
        path = dbUtils.get_screw_path(name)
        self.screw_jasons = {'top': screwDB.screwJson() , 'side': screwDB.screwJson() }
        for direction in self.screw_jasons.keys():
            self.screw_jasons[direction].read(path, direction)
            img_path = self.screw_jasons[direction].get_img_path()
            img=cv2.imread(img_path)
            self.ui.set_selected_image_live_page(direction,img)




    

    def proccessing_live(self, img, direction):
        img = cv2.imread('sample images/New folder/31x_1_4.png')
        direction = 'side'

        img, thresh_img,_ = proccessings.preprocessing_img_json( img, self.screw_jasons[direction], direction )
        img = Utils.mask_viewer(img, thresh_img, color=(0,100,0))
        results = []
        for active_tool in self.screw_jasons[direction].get_active_tools():
            result, img = proccessings.tools_dict[active_tool]( thresh_img, self.screw_jasons[direction], img )
            results.extend(result)

        results.sort( key = lambda x:x['name'])
        self.ui.set_live_table( self.ui.table_live_live_page, results )
        self.ui.set_main_image_live_page( direction, img )