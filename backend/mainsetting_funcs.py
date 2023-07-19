import numpy as np
from PySide6.QtGui import QStandardItem as sQStandardItem
from PySide6.QtGui import QFont as sQFont
from PySide6.QtGui import QColor as sQColor


# font parameters      
font_sizes = ["{:d}".format(x) for x in np.arange(8, 12)]
font_styles = ['Arial', 'Arial Black', 'Forte', 'Gigi', 'jokerman' ,'Times New Roman' , 'Zilla Slab']

# style (theme) and color parameters
app_styles = ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
app_colors = ['#144475', '#CB0000', '#F1CC00','#808080','#282C34']

# language parametrs
app_languages = ['English','Persian(فارسی)']


#---------------------------------------------------------------------------------------------------------------------------

# program appearance functions in main-setting page
#---------------------------------------------------------------------------------------------------------------------------
# assign top appearance parameters to UI
def assign_appearance_existing_params_to_ui(ui_obj):
    # font-size
    # self.ui.setting_fontsize_comboBox.addItems(appearance.font_sizes)
    for font_size in font_sizes:
        item = sQStandardItem(font_size)
        item.setFont(sQFont('Arial', int(font_size)))
        ui_obj.setting_fontsize_comboBox.model().appendRow(item)
    # font-style
    # self.ui.setting_fontstyle_comboBox.addItems(appearance.font_style)
    for font_style in font_styles:
        item = sQStandardItem(font_style)
        item.setFont(sQFont(font_style))
        ui_obj.setting_fontstyle_comboBox.model().appendRow(item)
    # app style (theme)
    ui_obj.setting_style_comboBox.addItems(app_styles)
    # app color
    for app_color in app_colors:
        item = sQStandardItem(app_color)
        item.setBackground(sQColor(app_color))
        ui_obj.setting_color_comboBox.model().appendRow(item)
    # app language
    # ui_obj.setting_language_comboBox.addItems(app_languages)

    # ui_obj.

    # ui_obj.start_capture_live_page.


# get appearance parameters and apply them to UI
def set_appearance_params_to_ui(ui_obj, appearance_params):
    ui_obj.setting_fontsize_comboBox.setCurrentText(str(appearance_params['font_size']))
    ui_obj.setting_fontstyle_comboBox.setCurrentText(appearance_params['font_style'])
    ui_obj.setting_style_comboBox.setCurrentText(appearance_params['window_style'])
    ui_obj.setting_color_comboBox.setCurrentText(appearance_params['window_color'])
    # ui_obj.setting_language_comboBox.setCurrentText(appearance_params['language'])
    # ui_obj.setting_language_comboBox.setCurrentText(appearance_params['parent_path'])

    # ui_obj.large_rect_area_label.setText(str(appearance_params['large_rect_area']))
    # ui_obj.small_rect_area_label.setText(str(appearance_params['small_rect_area']))
    # ui_obj.rect_accuracy_label.setText(str(appearance_params['rect_accuracy']))
    # split_size = appearance_params['split_size'].split(',')
    # try:
    #     ui_obj.splitsizew_spinBox.setValue(int(split_size[0][1:]))
    #     ui_obj.splitsizeh_spinBox.setValue(int(split_size[-1][:-1]))
    #     # ui_obj.defect_colors_number_spin.setValue(int(appearance_params['n_defect_colors']))
    # except:
    #     ui_obj.splitsizew_spinBox.setValue(0)
    #     ui_obj.splitsizeh_spinBox.setValue(0)
        # ui_obj.defect_colors_number_spin.setValue(3)


# get appearance parameters from UI
def get_appearance_params_from_ui(ui_obj):
    appearance_params = {}
    appearance_params['font_size'] = ui_obj.setting_fontsize_comboBox.currentText()
    appearance_params['font_style'] = ui_obj.setting_fontstyle_comboBox.currentText()
    appearance_params['window_style'] = ui_obj.setting_style_comboBox.currentText()
    appearance_params['window_color'] = ui_obj.setting_color_comboBox.currentText()
    # appearance_params['language'] = ui_obj.setting_language_comboBox.currentText()
    appearance_params['parent_path'] = ui_obj.line_main_path.text()
    return appearance_params


# get the appearance parameters and apply to program
def apply_appearance_params_to_program(ui_obj, confirm_ui_obj, appearance_params):
    # apply to UI
    ui_obj.line_main_path.setText(appearance_params['parent_path'])
    ui_obj.setStyleSheet('font: %spt "%s"' % (appearance_params['font_size'], appearance_params['font_style'])) # font-size and font-style
    ui_obj.leftMenuFrame.setStyleSheet('background-color:%s;' % (appearance_params['window_color'])) # window color
    ui_obj.contentTopBg.setStyleSheet('background-color:%s;' % (appearance_params['window_color'])) # window color
    ui_obj.topLogoInfo.setStyleSheet('background-color:%s;' % (appearance_params['window_color'])) # window color
    ui_obj.leftBox.setStyleSheet('background-color:%s;' % (appearance_params['window_color'])) # window color
    confirm_ui_obj.background_frame.setStyleSheet('background-color:%s;' % (appearance_params['window_color'])) # confirm window color
    confirm_ui_obj.setStyleSheet('font: %spt "%s"' % (appearance_params['font_size'], appearance_params['font_style'])) # confirm window font-style and font-size
    # ui_obj.setStyle(sQStyleFactory.create(app_style"))
    # must change : style and language should be added


# update combobox visual properties
def update_combo_color(ui_obj):
    current_color = ui_obj.setting_color_comboBox.currentText()
    ui_obj.setting_color_comboBox.setStyleSheet('background:%s' % current_color)

def update_combo_fontstyle(ui_obj):
    current_fontstyle = ui_obj.setting_fontstyle_comboBox.currentText()
    ui_obj.setting_fontstyle_comboBox.setStyleSheet('font-family:"%s"' % current_fontstyle)

def update_combo_fontsize(ui_obj):
    current_fontsize = ui_obj.setting_fontsize_comboBox.currentText()
    ui_obj.setting_fontsize_comboBox.setStyleSheet('font: %spt' % current_fontsize)


# calibration functions in main-setting page
#---------------------------------------------------------------------------------------------------------------------------
# get calibration parameters from UI
def get_calibration_params_from_ui(ui_obj):
    calibration_params = {}
    calibration_params['large_rect_area'] = ui_obj.large_rect_area_label.text()
    calibration_params['small_rect_area'] = ui_obj.small_rect_area_label.text()
    calibration_params['rect_accuracy'] = ui_obj.rect_accuracy_label.text()
    return calibration_params


# image-processing functions in main-setting page
#---------------------------------------------------------------------------------------------------------------------------
# get image processing params from UI
def get_image_procesing_params_from_ui(ui_obj):
    image_procesing_params = {}
    split_size_w = ui_obj.splitsizew_spinBox.value()
    split_size_h = ui_obj.splitsizeh_spinBox.value()
    image_procesing_params['split_size'] = '[%s,%s]' % (split_size_w, split_size_h)
    return image_procesing_params



# other functions to get main-setting parametrs from database
#---------------------------------------------------------------------------------------------------------------------------
# load/get main-setting parameters from database
def get_mainsetting_params_from_db(db_obj, mode='all'):
    params = db_obj.load_general_setting_params()
    if mode == 'all':
        return params
    elif mode == 'px_calibration':
        large_rect_area = params['large_rect_area']
        small_rect_area = params['small_rect_area']
        rect_acc = params['rect_accuracy']
        rect_acc = params['rect_accuracy']
        rect_areas = [large_rect_area, large_rect_area, large_rect_area, small_rect_area, small_rect_area, small_rect_area]
        return rect_areas, rect_acc    


# set main-setting parameters to database
def set_mainsetting_params_to_db(db_obj, apperance_params):
    res = db_obj.update_general_setting_params(apperance_params)
    return res # validation

