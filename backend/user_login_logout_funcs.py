from PySide6.QtGui import QPixmap as sQPixmap
from PySide6.QtGui import QImage as sQImage

from backend import confirm_window_messages


# logged-out icon
loggedout_icon = 'images/login_white.png'
loggedin_icon = 'images/logout_white.png'


#---------------------------------------------------------------------------------------------------------------------------


# function for changing UI buttons enabled or disabled given the user login/logout
def set_app_buttons_enable_or_disable(names, enable=True):
    for name in names:
        name.setEnabled(enable)


# logout user
def logout_user(ui_obj, confirm_ui_obj):
    # disabling all buttons (sections) in the UI
    # set_app_buttons_enable_or_disable(ui_obj.dash_buttons, False)
    # set_app_buttons_enable_or_disable(ui_obj.side_buttons, False)
    # flag to determine user is loggedin or not
    ui_obj.login_flag = False
    # change icon
    ui_obj.main_login_btn.setIcon(sQPixmap.fromImage(sQImage(loggedout_icon)))
    # go to dashboard section to restrict access
    ui_obj.stackedWidget.setCurrentWidget(ui_obj.page_dashboard)
    # close confirmation window
    confirm_ui_obj.close()


# authenticating the user on login
def authenticate_user(ui_obj, login_ui_obj, login_api_obj):
    # authenticate user
    allowed, user_info = login_api_obj.login()
    # user authenticated given username and password
    if allowed: 
        # close login window
        login_ui_obj.close()
        # flag to determine user is loggedin or not
        ui_obj.login_flag = True
        # enabling all buttons (sections) in the UI
        # set_app_buttons_enable_or_disable(ui_obj.dash_buttons, True)
        # set_app_buttons_enable_or_disable(ui_obj.side_buttons, True)
        # change icon
        ui_obj.main_login_btn.setIcon(sQPixmap.fromImage(sQImage(loggedin_icon)))


# running and showing user login window
def run_login_window(ui_obj, login_ui_obj, confirm_ui_obj):
    # chcek whereas user is logged in or not
    if not ui_obj.login_flag:
        login_ui_obj.show()
    else: # user logged in
        confirm_ui_obj.msg_label.setText(confirm_window_messages.logout_confirm_message)
        # load conformation window to confirm logging out
        confirm_ui_obj.show()



