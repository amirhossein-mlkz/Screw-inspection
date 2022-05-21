

# from sqlalchemy import false, true
import database
import datetime

import os


class dataBaseUtils():
    def __init__(self) :
        self.db=database.dataBase('root','password','localhost','screw')

        self.page_1='screw_page_1'
        self.table_cameras = 'camera_settings'
        self.table_general_settings = 'settings'
        self.camera_id = 'id'
        self.setting_tabel = 'settings'
        self.general_settings_id = 'id'

    #________________________________________________________________
    #
    #________________________________________________________________
    def search_user(self,input_user_name):
        try:
            record = self.db.search( self.table_user , 'user_name', input_user_name )[0]
            #print('asd',record)
            return record
        except:
            return []


    def search_camera_by_ip(self, input_camera_ip):
        try:
            record = self.db.search( self.table_cameras , 'ip_address', input_camera_ip)[0]
            #print('asd',record)
            return record
        except:
            return []


    def search_camera_by_serial(self, input_camera_serial):
        try:
            record = self.db.search( self.table_cameras , 'serial_number', input_camera_serial)[0]
            #print('asd',record)
            return record
        except:
            return []
    

    def load_cam_params(self, input_camera_id):
        try:
            record = self.db.search( self.table_cameras , 'id', input_camera_id )[0]
            #print('camera info:', record)
            return record
        except:
            return []

    def update_cam_params(self, input_camera_id, input_camera_params):
        try:
            for camera_param in input_camera_params.keys():
                res = self.db.update_record(self.table_cameras, camera_param, str(input_camera_params[camera_param]), self.camera_id, input_camera_id)
            return res
        except:
            return False


    def update_general_setting_params(self, input_setting_params):
        try:
            for param in input_setting_params.keys():
                res = self.db.update_record(self.table_general_settings, param, str(input_setting_params[param]), self.general_settings_id, '0')
            return res
        except:
            return False

    def load_general_setting_params(self):
        try:
            record = self.db.search( self.table_general_settings , self.general_settings_id, '0' )[0]
            #print('camera info:', record)
            return record
        except:
            return []



    def load_users(self):
        try:
            users=self.db.get_all_content('users')

            return users
        
        except:

            return []


    def remove_users(self,users_name):

        for i in range(len(users_name)):
            
            self.db.remove_record(col_name='user_name',id=users_name[i],table_name='users')

    def add_user(self,parms):
        data=(parms['user_name'],parms['password'],parms['role'])
        print(data)
        try:
            self.db.add_record(data, table_name='users', parametrs='(user_name,password,role)', len_parameters=3)
            return 'True'
        
        except:
            return 'Databas Eror'

    
    def search_user_by_user_name(self, input_user_name):
        try:
            record = self.db.search( self.table_user , 'user_name', input_user_name)[0]
            #print('asd',record)
            return record
        except:
            return []


    def add_screw(self,parms):
        data=(parms['name'],0,0)
        print(data)
        try:
            self.db.add_record(data, table_name=self.page_1, parametrs='(name,roi,threshold)', len_parameters=3)
            return 'True'
        
        except:
            return 'Databas Eror'
    def search_page_1(self,name):
        # try:
            record = self.db.search( self.page_1 , 'name', name,int_type=False)
            return record
        # except:
        #     return []

  


    def get_dataset_path(self):
        record =self.db.search(table_name=self.setting_tabel,param_name='id',value=0)[0 ]
        return record['parent_path']






if __name__ == '__main__':
    db = dataBaseUtils()
    # records = db.load_coil_info(996)
    # db.get_camera_setting()
    #db.set_dataset_path('G:/dataset/')
    # print(db.get_dataset_path())

    # db.get_path(['997', 'up', (5, 5)])
    # pass

    # db.load_cam_params('1')

    # x=db.load_users()

    # user=['ali']

    # db.remove_users(user)

    data={'name':'asghar'}

    db.add_screw(data)

    x=db.search_page_1('asghar')
    print('x',x)

    # x=db.get_dataset_path()

    # print(x)