


ERORS={



    

}


WARNINGS={

        'NO_CHOOSEN_IMG': {'fa':' تصویری انتخاب نشده است ',
            'en':' No image selected '},

        'Warning': {'fa':' هشدار ',
            'en':' Warning '},

        'Delete_Screw': {'fa':' آیا از حذف اطمینان دارید ؟ ',
            'en':' Are you sure want to delete '},

        'EDIT_MODE': {'fa':' تصویر را ذخیره کنید ',
            'en':' First Save '},

        'Connection_succssed':{'fa':'ارتباط برقرار شد ',
             'en':'Connection Successfully'},
            
        'Connection_eror':{'fa':'ارتباط برقرار نشد ',
             'en':'Connection_eror'},
        'plc_ip':{'fa':'آی بی آبدیت شد ',
             'en':'PLC IP Updated'},
        'Disconnected':{'fa':'قطع ارتباط ',
             'en':'Disconnected'},
        'Connected':{'fa':'وصل ارتباط ',
             'en':'Connected'},
        'Connection_eror':{'fa':'مشکل ارتباط ',
             'en':'Connection Eror'},
        'Mode_run_plc':{'fa':'حرکت ',
             'en':'Run'},
        'Mode_stop_plc':{'fa':'توقف ',
             'en':'Stop'},
        'path_eror_plc':{'fa':'ادرس اشتباه ',
             'en':'Path Eror'}
}
MESSEGES = {

     'SELECT_IMAGE': {'fa':'دوربین: {} | فریم: {}',
                    'en':'Camera: {} | Frame: {} '},
     'Edit Mode' : {'fa':"حالت تغییر دادن",
                    'en':'Edit Mode'}
                         
}


Titles = {

     

    'credit': {'fa': "تهیه شده توسط تیم : Radco-Vision",
                        'en': 'Own : Radco-Vision'},
    'Top Camera': {'fa': "دوربین بالا",
                        'en': 'Top Camera'},
    'Side Camera': {'fa': "دوربین کنار",
                        'en': 'Side Camera'},

    'Camera :': {'fa': "دوربین :",
                        'en': 'Camera :'},
    'Select Screw :': {'fa': "انتخاب بیچ :",
                        'en': 'Select Screw :'},
    'Select :': {'fa': "انتخاب :",
                        'en': 'Select :'},
    'Table Top Camera :': {'fa': "جدول دوربین بالا :",
                        'en': 'Table Top Camera :'},
    'Table Side Camera :': {'fa': "جدول دوربین کنار :",
                        'en': 'Table Side Camera :'},
    'Scale': {'fa': "نسبت بزرگی",
                        'en': 'Scale'},
     'Camera :': {'fa': "دوربین :",
                        'en': 'Camera :'},
     'Camera :': {'fa': "دوربین :",
                        'en': 'Camera :'},

    'Add': {'fa': "افزودن بیچ",
                        'en': 'Add'},
    'Edit/Remove': {'fa': "وایرایش/حذف",
                        'en': 'Scale'}, 
    'Edit': {'fa': "ویرایش",
                        'en': 'Edit'},
    'Remove': {'fa': "حذف",
                        'en': 'Remove'},
    'Main': {'fa': "اصلی",
                        'en': 'Main'},
    'Measurement': {'fa': "اندازه گیری",
                        'en': 'Measurement'},
    'Defect': {'fa': "عیوب",
                        'en': 'Defect'},
    'Edge crack': {'fa': "عیوب لبه",
                        'en': 'Edge crack'},
    'centerality': {'fa': "مرکزیت",
                        'en': 'centerality'},
    'Lenght': {'fa': "طول",
                        'en': 'Lenght'},
    'Male Thread ': {'fa': "طول بدنه",
                        'en': 'Male Thread '},
    'Diameter': {'fa': "قطر",
                        'en': 'Diameter'},
    'Screw Head': {'fa': "سر بیچ",
                        'en': 'Screw Head'},
    'Defect': {'fa': "عیوب",
                        'en': 'Defect'},
    'Current :': {'fa': "بیچ انتخاب شده :",
                        'en': 'Current :'},
    'Pos :': {'fa': "موقعیت :",
                        'en': 'Pos :'},
     'Color :': {'fa': "رنگ :",
          'en': 'Color :'},
                                            
    }


def set_title(self, lang):
     self.creditsLabel.setText(Titles['credit'][lang])
     self.label_20.setText(Titles['Top Camera'][lang])
     self.label_21.setText(Titles['Side Camera'][lang])
     self.label_29.setText(Titles['Side Camera'][lang])
     self.pushButton_5.setText(Titles['Select :'][lang])
     self.groupBox_29.setTitle(Titles['Camera :'][lang])
     self.groupBox_19.setTitle(Titles['Table Top Camera :'][lang])
     self.groupBox_21.setTitle(Titles['Table Side Camera :'][lang])
     # self.label_54.setText(Titles['Scale'][lang])
     # self.label_168.setText(Titles['Scale'][lang])
#     self.pushButton_5.setText(Titles['Side Camera'][lang])
#     self.pushButton_5.setText(Titles['Side Camera'][lang])
     self.add_btn.setText(Titles['Scale'][lang])
     self.edit_remove_btn.setText(Titles['Edit/Remove'][lang])
     self.edit_btn.setText(Titles['Edit'][lang])
     self.remove_screw_btn.setText(Titles['Remove'][lang])
     self.groupBox_23.setTitle(Titles['Top Camera'][lang])
     self.groupBox_22.setTitle(Titles['Side Camera'][lang])
     self.label_6.setText(Titles['Current :'][lang])
     self.btn_page0_1_top.setText(Titles['Main'][lang])
     self.btn_page0_2_top.setText(Titles['Measurement'][lang])
     self.btn_page0_3_top.setText(Titles['Defect'][lang])
     self.btn_page0_4_top.setText(Titles['Edge crack'][lang])
     self.btn_page0_5_top.setText(Titles['centerality'][lang])
     self.btn_page0_1_side.setText(Titles['Main'][lang])
     self.btn_page0_2_side.setText(Titles['Lenght'][lang])
     self.btn_page0_3_side.setText(Titles['Male Thread '][lang])
     self.btn_page0_4_side.setText(Titles['Diameter'][lang])
     self.btn_page0_5_side.setText(Titles['Screw Head'][lang])
     self.btn_page0_6_side.setText(Titles['Defect'][lang])

     self.label_32.setText(Titles['Pos :'][lang])
     self.label_31.setText(Titles['Color :'][lang])

     


     