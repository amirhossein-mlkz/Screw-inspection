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
                    , user_login_logout_funcs, user_management_funcs, Screw, Utils, Drawing, cvTools

from backend.mouse import Mouse

from full_screen_UI import FullScreen_UI
import texts

from database import database, dbUtils, screwDB

class API:

    def __init__(self,ui):
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
        self.db = database_utils.dataBaseUtils()
        
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
        
        self.image_screw_setting = None
        self.rotate_correction = False
        #-------------------------------------------------------------------------------------------------------------------
        self.ui.set_combo_boxes(self.ui.comboBox_edit_remove, dbUtils.get_screws_list())
        
        
        self.ui.next_page_btn.clicked.connect(self.screw_setting_page_loader)
        self.ui.prev_page_btn.clicked.connect(self.screw_setting_page_loader)
        
        self.mouse.connect_all(self.ui.label_image_grab_page, self.image_setting_mouse_event)
        
        
        
        
        
        # self.ui.btn_negative0_2_top.toggled.connect(self.update_thresh_negative_setting_page2)
        

        #-------------------------------------------------------------------------------------------------------------------

    def test(self):
        pass
        path = 'images/test1_0_12 - Copy.png'
        # self.image_cam_1=cv2.imread('images/imge/dineniso14583.png')
        # self.image_cam_2=cv2.imread('images/imge/Screw-Flat-Head-6-x-1-2-Key-II_1.jpg')
        self.ui.line_image_address0_1_top.setText(path)
        # self.ui.set_image_page_tool_labels(self.ui.camera_1,self.image_cam_1)     
        # self.ui.set_image_page_tool_labels(self.ui.camera_2,self.image_cam_2)     

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
        self.ui.setting_color_comboBox.currentTextChanged.connect(lambda: mainsetting_funcs.update_combo_color(ui_obj=self.ui))
        self.ui.setting_fontstyle_comboBox.currentTextChanged.connect(lambda: mainsetting_funcs.update_combo_fontstyle(ui_obj=self.ui))
        self.ui.setting_fontsize_comboBox.currentTextChanged.connect(lambda: mainsetting_funcs.update_combo_fontsize(ui_obj=self.ui))
        self.ui.setting_appearance_apply_btn.clicked.connect(lambda: self.apply_changed_appearance_params(mode='appearance'))
        self.ui.setting_calibration_apply_btn.clicked.connect(lambda: self.apply_changed_appearance_params(mode='calibration'))
        self.ui.setting_imageprocessing_apply_btn.clicked.connect(lambda: self.apply_changed_appearance_params(mode='imageprocessing'))
        self.ui.setting_defects_apply_btn.clicked.connect(lambda: self.apply_changed_appearance_params(mode='defects'))
        self.ui.side_general_setting_btn.clicked.connect(lambda: self.load_appearance_params_on_start(mainsetting_page=True))

        #Fullscreen
        self.ui.fullscreen_cam_1.clicked.connect(lambda: self.show_full_screen(self.ui.fullscreen_cam_1))
        self.ui.fullscreen_cam2.clicked.connect(lambda: self.show_full_screen(self.ui.fullscreen_cam2))


        #tools page

        self.ui.save_new_btn.clicked.connect(self.add_new_screw)
        self.ui.edit_remove_btn.clicked.connect(self.get_screw_names)
        self.ui.edit_btn.clicked.connect(self.edit_load_screw)
        self.ui.remove_screw_btn.clicked.connect(self.remove_screw)

        self.ui.get_main_parms_screw_top()


        # publice setting-------------------------------------------------------
        self.ui.save_btn_page_grab.clicked.connect(self.save_screw)

        #Page 1_top----------------------------------------------------------
        self.ui.btn_set_image0_1_top.clicked.connect(self.update_main_image_top)
        self.ui.btn_page_1_top.clicked.connect(self.update_main_setting_page_top)
        self.ui.bar_thresh0_1_top.valueChanged.connect(self.update_main_threshould_top)
        self.ui.bar_noise_filter0_1_top.valueChanged.connect(self.update_main_noise_filter_top)
        # self.ui.btn_negative0_1_top.toggled.connect(self.update_main_thresh_negative_top)
        self.ui.checkbox_connect('thresh_inv', self.update_main_thresh_negative_top )
        self.ui.roi_connect(self.main_roi_top_input)        
        
        
        #Page 1_side----------------------------------------------------------
        self.ui.btn_set_image0_1_side.clicked.connect(self.update_main_image_side)
        self.ui.btn_page_1_side.clicked.connect(self.update_main_setting_page_side)
        self.ui.bar_thresh0_1_side.valueChanged.connect(self.update_main_threshould_side)
        self.ui.bar_noise_filter0_1_side.valueChanged.connect(self.update_main_noise_filter_side)
        # self.ui.btn_negative0_1_side.toggled.connect(self.update_main_thresh_negative_side)
        self.ui.roi_connect(self.main_roi_side_input)
        
        self.ui.btn_rotate_correction0_1_side.clicked.connect(self.update_rotated_image)

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

        fullscreen_dict={'fullscreen_cam_1':self.image_cam_1,'fullscreen_cam2':self.image_cam_2}

        self.win_fullscreen = FullScreen_UI(fullscreen_dict[str(cam_num.objectName())])
        # full_screen_obj.show()
        self.win_fullscreen.show()



    

    
    


    def get_screw_names(self):
        self.ui.set_combo_boxes(self.ui.comboBox_edit_remove, dbUtils.get_screws_list())



    #grab_page

    def set_roi_grab_page(self):

        img=cv2.imread('images/upload-big-arrow.png')   # set image here

        self.update_image(self.ui.label_image_grab_page,img)
        


    



#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------


    #____________________________________________________________________________________________________________
    #                                           
    #
    #                                          Screw Settin Public
    #
    #
    #____________________________________________________________________________________________________________
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
            
        #ERROR
        if not flag:
            print('Error! : screw exist already')
        self.update_main_setting_page_top()
    
    
    def save_screw(self):
        flag = self.ui.show_question('Save Screw', 'Are you Sure?')
        try:
            if flag:
                for key in self.screw_jasons.keys():
                    path = dbUtils.get_screw_path( self.screw_jasons[key].get_name() )
                    self.screw_jasons[key].write(path)                
                print('Screw Saved')
                self.ui.editmode=False
        except:
            self.ui.set_warning('Save Eror','tool_page',level=2)
            
            
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
        
        for key in self.screw_jasons.keys():
            self.screw_jasons[key].read(path, key)
        self.update_main_setting_page_top()
        
        
    def image_setting_mouse_event(self,wname):
        page_idx = self.ui.get_setting_page_idx()
        mouse_status = self.mouse.get_status()
        mouse_button = self.mouse.get_button()
        mouse_pt = self.mouse.get_relative_position()

        if page_idx == 1:
            self.update_main_roi_top_mouse(mouse_status, mouse_button , mouse_pt)
            
        elif page_idx == 2:
            self.update_roi_setting_page2_mouse(mouse_status, mouse_button , mouse_pt)

        elif page_idx == 3:
            self.update_main_roi_side_mouse(mouse_status, mouse_button , mouse_pt)
            

    
    def screw_setting_page_loader(self):
        for key in self.roi_drawings.keys():
            self.roi_drawings[ key ].clear()
            
        page_idx = self.ui.get_setting_page_idx()
        if page_idx == 1:
            self.update_main_setting_page_top()
            
        elif page_idx == 2:
            self.update_setting_page2()
    #____________________________________________________________________________________________________________
    #                                           
    #
    #                                           Screw main Settin top
    #
    #
    #____________________________________________________________________________________________________________
    def update_main_setting_page_top(self):
        selected_camera_direction = 'top'
        
        parms = self.screw_jasons[selected_camera_direction].data
        roi_rect = self.screw_jasons[selected_camera_direction].get_main_roi()
        self.ui.set_main_parms_screw_top( parms )
        self.rect_roi_drawing.max_shape_count = 1
        self.rect_roi_drawing.shapes = [ roi_rect ]
        
        
        self.update_main_image_top()
        self.draw_main_setting_page_top_image()
        
    
    
    def draw_main_setting_page_top_image(self):
        
        selected_camera_direction = 'top'
        
        img = self.image_screw_setting
        thresh = self.screw_jasons[ selected_camera_direction ].get_main_thresh()
        noise_filter = self.screw_jasons[ selected_camera_direction ].get_main_noise_filter()
        rect = self.screw_jasons[ selected_camera_direction ].get_main_roi()
        inv_state = self.screw_jasons[ selected_camera_direction ].get_main_thresh_inv()
        
        mask_roi = cvTools.rects2mask(img.shape[:2], [rect])
        thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        
        img = Utils.mask_viewer(img, thresh_img)
        img = self.rect_roi_drawing.get_image(img)
        
        self.ui.set_image_page_tool_labels(img)
        
        

        
    def update_main_threshould_top(self):
        selected_camera_direction = 'top'
        thresh = self.ui.get_sliders_value('thresh')
        self.screw_jasons[ selected_camera_direction ].set_main_thresh(thresh)
        self.draw_main_setting_page_top_image()
    
    
    def update_main_noise_filter_top(self):
        selected_camera_direction = 'top'
        noise_filter = self.ui.bar_noise_filter0_1_top.value()
        self.screw_jasons[ selected_camera_direction ].set_main_noise_filter(noise_filter)
        self.draw_main_setting_page_top_image()
    
    
    
    def update_main_thresh_negative_top(self):
        selected_camera_direction = 'top'
        state = self.ui.get_checkbox_value('thresh_inv')
        self.screw_jasons[ selected_camera_direction ].set_main_thresh_inv(state) 
        self.draw_main_setting_page_top_image()
        
    
    def update_main_image_top(self):
        selected_camera_direction = 'top'
        path = self.ui.get_screw_top_image_path()
        
        if cv2.imread(path) is not None:
            self.screw_jasons[ selected_camera_direction ].set_img_path(path)
            self.image_screw_setting = cv2.imread(path)
            self.rect_roi_drawing.set_img_size( self.image_screw_setting.shape[:2] )
            self.draw_main_setting_page_top_image()
        else:
            print('Error! : image not exist')
        
        
            
            
    def main_roi_top_input(self, name):
        def func():
            selected_camera_direction = 'top'
            
            #data changed in Ui
            data = self.ui.get_roi_value()#ba in keke kar mikarde

            #data saved in json
            rect = self.screw_jasons[selected_camera_direction].get_main_roi()
            print('dataAPI',data)
            rect_dict = Utils.rect_list2dict(rect)
            #update param in jason that changed in UI
            rect_dict[name] = data[name]
            rect = Utils.rect_dict2list(rect_dict)
            
            self.rect_roi_drawing.update_shape(shape_idx=0,  shape=rect)
            self.draw_main_setting_page_top_image()
            
            self.screw_jasons[selected_camera_direction].set_main_roi(pt1=rect[0], pt2=rect[1])
        return func




    def update_main_roi_top_mouse(self, mouse_status, mouse_button, mouse_pt):
        self.rect_roi_drawing.qtmouse_checker( mouse_status, mouse_button, mouse_pt )
        
        shapes = self.rect_roi_drawing.shapes
        if len(shapes) > 0:
            rect = shapes[0]
            rect_dict = Utils.rect_list2dict(rect)
            self.ui.set_roi_value(rect_dict)
            
            selected_camera_direction = 'top'
            self.screw_jasons[selected_camera_direction].set_main_roi( pt1=rect[0], pt2=rect[1] )
        
        self.draw_main_setting_page_top_image()
        
        
        
        
        
    #____________________________________________________________________________________________________________
    #                                           
    #
    #                                           Screw main Settin side
    #
    #
    #____________________________________________________________________________________________________________
    def update_main_setting_page_side(self):
        selected_camera_direction = 'side'
        
        parms = self.screw_jasons[selected_camera_direction].data
        roi_rect = self.screw_jasons[selected_camera_direction].get_main_roi()
        self.ui.set_main_parms_screw_side( parms ) 
        self.rect_roi_drawing.max_shape_count = 1
        self.rect_roi_drawing.shapes = [ roi_rect ]
        
        
        self.update_main_image_side()
        self.draw_main_setting_page_side_image()
        
    
    
    def draw_main_setting_page_side_image(self):
        
        selected_camera_direction = 'side'
        
        img = self.image_screw_setting
        thresh = self.screw_jasons[ selected_camera_direction ].get_main_thresh()
        noise_filter = self.screw_jasons[ selected_camera_direction ].get_main_noise_filter()
        rect = self.screw_jasons[ selected_camera_direction ].get_main_roi()
        inv_state = self.screw_jasons[ selected_camera_direction ].get_main_thresh_inv()
        
        mask_roi = cvTools.rects2mask(img.shape[:2], [rect])
        thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        if self.rotate_correction:
            mask_unbelt, belt_pos = cvTools.remove_belt( thresh_img )
    
            angle = cvTools.correct_rotation_angle(mask_unbelt)
            
            img = cvTools.rotate_image(img,  angle  )
            thresh_img = cvTools.rotate_image(thresh_img,  angle )
            rotated_mask = cvTools.rotate_image(mask_unbelt,  angle )
            
    
            pt1,pt2 = cvTools.side_screw_bounding_rect(rotated_mask)
    
            img = cv2.rectangle( img , pt1, pt2, (0,255,0),thickness=6)
        
        img = Utils.mask_viewer(img, thresh_img)
        img = self.rect_roi_drawing.get_image(img)
        
        self.ui.set_image_page_tool_labels(img) 
        
        
    def update_rotated_image(self):
        self.rotate_correction = not( self.rotate_correction )
        self.draw_main_setting_page_side_image()
        
    def update_main_threshould_side(self):
        selected_camera_direction = 'side'
        thresh = self.ui.bar_thresh0_1_side.value()    
        self.screw_jasons[ selected_camera_direction ].set_main_thresh(thresh)
        self.draw_main_setting_page_side_image()
        
    def update_threshould(self):
        page_name=self.ui.get_setting_page_idx(page_name=True)
        direction=self.ui.get_setting_page_idx(direction=True)
        print(page_name,direction)
        print('asdwad')
    
    
    def update_main_noise_filter_side(self):
        selected_camera_direction = 'side'
        noise_filter = self.ui.bar_noise_filter0_1_side.value()  
        self.screw_jasons[ selected_camera_direction ].set_main_noise_filter(noise_filter)
        self.draw_main_setting_page_side_image()
    
    
    
    def update_main_thresh_negative_side(self):
        selected_camera_direction = 'side'
        state = self.ui.btn_negative0_1_side.isChecked()
        self.screw_jasons[ selected_camera_direction ].set_main_thresh_inv(state) 
        self.draw_main_setting_page_side_image()
        
    
    def update_main_image_side(self):
        selected_camera_direction = 'side'
        path = self.ui.get_screw_side_image_path()
        
        if cv2.imread(path) is not None:
            self.screw_jasons[ selected_camera_direction ].set_img_path(path)
            self.image_screw_setting = cv2.imread(path)
            self.rect_roi_drawing.set_img_size( self.image_screw_setting.shape[:2] )
            self.draw_main_setting_page_side_image()
        else:
            print('Error! : image not exist')
        
        
            
            
    def main_roi_side_input(self, name):
        def func():
            selected_camera_direction = 'side'
            
            #data changed in Ui
            data = self.ui.get_main_parms_screw_side()
            #data saved in json
            rect = self.screw_jasons[selected_camera_direction].get_main_roi()
            
            rect_dict = Utils.rect_list2dict(rect)
            #update param in jason that changed in UI
            rect_dict[name] = data[name]
            rect = Utils.rect_dict2list(rect_dict)
            
            self.rect_roi_drawing.update_shape(shape_idx=0,  shape=rect)
            self.draw_main_setting_page_side_image()
            
            self.screw_jasons[selected_camera_direction].set_main_roi(pt1=rect[0], pt2=rect[1])
        return func



    def update_main_roi_side_mouse(self, mouse_status, mouse_button, mouse_pt):
        selected_camera_direction = 'side'
        self.rect_roi_drawing.qtmouse_checker( mouse_status, mouse_button, mouse_pt )
        
        shapes = self.rect_roi_drawing.shapes
        if len(shapes) > 0:
            rect = shapes[0]
            rect_dict = Utils.rect_list2dict(rect)
            self.ui.set_roi_value(rect_dict)
            self.screw_jasons[selected_camera_direction].set_main_roi( pt1=rect[0], pt2=rect[1] )
        
        self.draw_main_setting_page_side_image()
        
           
        
    #____________________________________________________________________________________________________________
    #                                           
    #
    #                                          
    #
    #
    #____________________________________________________________________________________________________________     
        
        
        
    def update_setting_page2(self):
        for key in self.roi_drawings.keys():
            self.roi_drawings[key].max_shape_count = 2
            
        self.update_setting_page2_image()
        self.draw_setting_page2_image()
        
    

    
    def update_setting_page2_image(self):
        selected_camera_direction = 'top'
        
        img_path = self.screw_jasons[ selected_camera_direction ].get_img_path()
        rect = self.screw_jasons[ selected_camera_direction ].get_main_roi()
        
        self.image_screw_setting = cv2.imread(img_path)
        self.image_screw_setting = cvTools.crop_rect(self.image_screw_setting, rect)
        
        for key in self.roi_drawings.keys():
            self.roi_drawings[key].set_img_size( self.image_screw_setting.shape[:2] )

    
    
    def draw_setting_page2_image(self):
        selected_camera_direction = 'top'
        
        img = np.copy(self.image_screw_setting)
        
        
        mask_type = self.ui.selected_mask_type
        shapes = self.roi_drawings[ mask_type ].get_sorted_shapes()
        
        thresh = self.screw_jasons[ selected_camera_direction ].region['thresh']
        noise_filter = self.screw_jasons[ selected_camera_direction ].region['noise_filter']
        thresh_inv = self.screw_jasons[ selected_camera_direction ].region['thresh_inv']
        #outer_shape =  self.screw_jasons[ selected_camera_direction ].region['out']
        #inner_shape = self.screw_jasons[ selected_camera_direction ].region['in']
        #shape_type = self.screw_jasons[ selected_camera_direction ].region['type']
        #rect = self.screw_jasons[ selected_camera_direction ].region['thresh']
        
        if len(shapes) == 2 :
            cv2.imshow('imggg', img)
            cv2.waitKey(10)
            mask_area = cvTools.mask_area(  img.shape[:2], 
                                            shapes[1], 
                                            shapes[0],
                                            mask_type,
                                            )

            #mask = cvTools.adp_threshould( img , thresh, 0 , mask_area, thresh_inv )
            mask  = cvTools.threshould( img, thresh, mask_area, thresh_inv)
            #cvTools.filter_noise_area(mask, noise_filter)
            
            # cnt = cvTools.extract_bigest_contour(mask)
            # cnt = cv2.convexHull (cnt)
            
            #cv2.HoughLines( mask,  )
            
            
            img = Utils.mask_viewer(img, mask)
            
            # 
            # cv2.drawContours (img , [cnt] ,0, (0,0,255) , thickness=5)
            
            

        img = self.roi_drawings[ self.ui.selected_mask_type ].get_image( img )
        self.ui.set_image_page_tool_labels(img)


    def update_roi_setting_page2_mouse(self , mouse_status, mouse_button , mouse_pt):
        
        mask_type = self.ui.selected_mask_type
        self.roi_drawings[ mask_type ].qtmouse_checker( mouse_status, mouse_button, mouse_pt )

        self.draw_setting_page2_image()


    
    def update_threshould_setting_page2(self):
            selected_camera_direction = 'top'
            thresh = self.ui.threshouldSetingPage2_slider.value()
            
            self.screw_jasons[ selected_camera_direction ].set_region_thresh( thresh )
            self.draw_setting_page2_image()
    

    def update_noise_filter_setting_page2(self):
            selected_camera_direction = 'top'
            noise_area = self.ui.page2_noise_filter_top_Slider.value()
            
            self.screw_jasons[ selected_camera_direction ].set_region_noise_filter( noise_area )
            
            print(noise_area)
            self.draw_setting_page2_image()   




    def update_thresh_negative_setting_page2(self):
        selected_camera_direction = 'top'
        state = self.ui.btn_negative0_2_top.isChecked()
        self.screw_jasons[ selected_camera_direction ].set_region_thresh_inv(state) 
        self.draw_setting_page2_image()
    