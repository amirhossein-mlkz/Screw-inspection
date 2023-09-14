from PySide6 import QtCore as sQtCore
from functools import partial
import numpy as np
import random

import database_utils
import cv2

import login_UI
# import confirm_UI
from backend import camera_funcs, colors_pallete, confirm_window_messages, mainsetting_funcs\
                    , user_login_logout_funcs, user_management_funcs
import platform

from full_screen_UI import FullScreen_UI


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
        os=platform.platform()
        if os[:5] =='Linux':
            self.db = database_utils.dataBaseUtils(password='password')
        
        else:
            # self.db = database_utils.dataBaseUtils(password='@mm@9398787515AmmA')
            self.db = database_utils.dataBaseUtils(password='root')

        
        #------------------------------------------------------------------------------------------------------------------------
        # start-up functions
        # get available cameras and update database
        self.available_camera_serials = camera_funcs.get_available_cameras_list_serial_numbers()
        camera_funcs.update_available_camera_serials_on_db(db_obj=self.db, available_serials=self.available_camera_serials)
        # assign base parameters to UI
        mainsetting_funcs.assign_appearance_existing_params_to_ui(ui_obj=self.ui)
        # load and apply program appearance params
        self.load_appearance_params_on_start()
        # refresh dashboard

        # function to active the UI buttons functionality
        self.button_connector()


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

        

    # functions
    #------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------------
    # button connector for activating UI buttons functionality
    def button_connector(self):
        
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

        
    # dashboard page
    #------------------------------------------------------------------------------------------------------------------------
    # refresh summary informations on the dashboard page
    def refresh_dashboard_page(self):
        print('dashboard_page')
        # user_management_funcs.show_users_summary_info(ui_obj=self.ui, db_obj=self.db)
        # defect_management_funcs.show_defects_summary_info(ui_obj=self.ui, db_obj=self.db)
        # storage_funcs.show_storage_status(ui_obj=self.ui)

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


    #------------------------------------------------------------------------------------------------------------------------
    

    # camera soft-calibration functions in the calibration setting page
    #------------------------------------------------------------------------------------------------------------------------
  
    #------------------------------------------------------------------------------------------------------------------------


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



    def show_full_screen(self,cam_num):
        self.image_cam_1=cv2.imread('images/icons/240_F_296806337_usQssx5FBitebzcGsaOF5qOltJ4AZfBJ.jpg')
        self.image_cam_2=cv2.imread('images/icons/calibration_setting_white.png')
        fullscreen_dict={'fullscreen_cam_1':self.image_cam_1,'fullscreen_cam_2':self.image_cam_2}
        print('cam_num',fullscreen_dict[str(cam_num.objectName())])

        # full_screen_obj=FullScreen_UI(fullscreen_dict[str(cam_num.objectName())])
        img = cv2.imread('images/icons/240_F_296806337_usQssx5FBitebzcGsaOF5qOltJ4AZfBJ.jpg')
        # cv2.imshow('asd',img)
        # cv2.waitKey(0)
        # app = QApplication()
        # from PyQt5 import QtGui
        # app = QtGui.QApplication
        win = FullScreen_UI(img)
        # full_screen_obj.show()
        win.show()











            

        
        