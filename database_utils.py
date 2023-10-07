
sql_mode='sqlite'

if sql_mode=='mysql':
# from sqlalchemy import false, true
    import database.database as database
if sql_mode=='none':
    from database.database_const import CAMERA_INFO,USERS,GENERAL_SETTINGS,PLC_IP,PLC_PARMS
if sql_mode=='sqlite':
    import sqlite3
    import database_sqlite

class dataBaseUtils():
    def __init__(self,user_name='root',password='') :
        # password='@mm@9398787515AmmA'
        if sql_mode=='mysql':
            self.db=database.dataBase(user_name,password,'localhost','screw')

        if sql_mode=='none':
            self.db=None
        
        if sql_mode == 'sqlite':
            self.db = database_sqlite.dataBase('screw_sqlite')


        self.page_grab='screw_page_grab'
        self.table_cameras = 'camera_settings'
        self.table_general_settings = 'settings'
        self.camera_id = 'id'
        self.setting_tabel = 'settings'
        self.general_settings_id = 'id'
        self.size='size'
        self.plc='plc_setting'
        self.history='history'
        self.sensor_detection='sensor_detection'

    #________________________________________________________________
    #
    #________________________________________________________________
    def search_user(self,input_user_name):

        if sql_mode=='none':
            return []

        # if sql_mode=='sqlite':
        #     record = self.db.search( self.table_user , 'user_name', input_user_name )
        #     #print('asd',record)
        #     return record     

        try:
            record = self.db.search( self.table_user , 'user_name', input_user_name )[0]
            #print('asd',record)
            return record
        except:
            print('Error search_user')
            return []


    def search_camera_by_ip(self, input_camera_ip):

        if sql_mode=='none':
            return []

        # if sql_mode=='sqlite':
        #     record = self.db.search( self.table_cameras , 'ip_address', input_camera_ip)
        #     #print('asd',record)
        #     return record

        try:
            record = self.db.search( self.table_cameras , 'ip_address', input_camera_ip)[0]
            #print('asd',record)
            return record
        except:
            print('Error search_camera_by_ip')

            return []


    def search_camera_by_serial(self, input_camera_serial):


        if sql_mode=='none':
            return []

        # if sql_mode=='sqlite':
        #     record = self.db.search( self.table_cameras , 'serial_number', input_camera_serial)
        #     return record

        try:
            record = self.db.search( self.table_cameras , 'serial_number', input_camera_serial)[0]
            #print('asd',record)
            return record
        except:
            print('Error search_camera_by_serial')
            return []
    

    def load_cam_params(self, input_camera_id):
        if input_camera_id == 'top':
            input_camera_id=1
        elif input_camera_id =='side':
            input_camera_id = 2


        if sql_mode=='none':
           
            return CAMERA_INFO

        # if sql_mode=='sqlite':
        #     record = self.db.search( self.table_cameras , 'id', input_camera_id )
        #     print('camera info:', record)
        #     return record

        try:
            record = self.db.search( self.table_cameras , 'id', input_camera_id )[0]

            return record
        except:
            print('Error load_cam_params')

            return []

    def update_cam_params(self, input_camera_id, input_camera_params):
        if sql_mode=='none':
            return True

        # if sql_mode=='sqlite':

        #     for camera_param in input_camera_params.keys():
        #         res = self.db.update_record(self.table_cameras, camera_param, str(input_camera_params[camera_param]), self.camera_id, input_camera_id)
        #     return res


        try:
            for camera_param in input_camera_params.keys():
                res = self.db.update_record(self.table_cameras, camera_param, str(input_camera_params[camera_param]), self.camera_id, input_camera_id)
            return res
        except:
            print('Error update_cam_params')

            return False


    def update_general_setting_params(self, input_setting_params):

        if sql_mode=='none':
            return True

        try:
            for param in input_setting_params.keys():
                res = self.db.update_record(self.table_general_settings, param, str(input_setting_params[param]), self.general_settings_id, '0')
            return res
        except:
            print('Error update_general_setting_params')

            return False

    def load_general_setting_params(self):

        if sql_mode=='none':
            return GENERAL_SETTINGS


        # if sql_mode=='sqlite':
        #     record = self.db.search( self.table_general_settings , self.general_settings_id, '0' )[0]
        #     print('camera info:', record)
        #     return record
        try:
            record = self.db.search( self.table_general_settings , self.general_settings_id, '0' )[0]
         
            return record
        except:
            print('Except load_general_setting_params')
            return []



    def load_users(self):

        if sql_mode=='none':
            return USERS

        try:
            users=self.db.get_all_content('users')
            print('users',users)
            return users
        
        except:
            print('Error load_users')

            return []


    def remove_users(self,users_name):

        if sql_mode=='none':
            return True


        for i in range(len(users_name)):
            
            self.db.remove_record(col_name='user_name',id=users_name[i],table_name='users')

    def add_user(self,parms):

        if sql_mode=='none':
            return True


        data=(parms['user_name'],parms['password'],parms['role'])
        #print(data)
        try:
            self.db.add_record(data, table_name='users', parametrs='(user_name,password,role)', len_parameters=3)
            return 'True'
        
        except:
            print('Error add_user')
            return 'Databas Eror'

    
    def search_user_by_user_name(self, input_user_name):

        if sql_mode=='none':
            return []     


        if sql_mode =='sqlit':

            record = self.db.search( self.table_user , 'user_name', input_user_name)
            return record

        try:
            record = self.db.search( self.table_user , 'user_name', input_user_name)[0]
            return record
        except:
            print('Error search_user_by_user_name')

            return []




    def get_size_table(self,label_name):
        # record = self.db.search( self.table_user , 'user_name', input_user_name)[0]
        record=self.db.search(self.size,'name',label_name)
        return record

    def set_size_table_side(self,parms):

        for key,value in parms.items():
            # print('key',key,'value',value)
            self.db.update_record(self.size,key,value,'name','side')

    def set_size_table_top(self,parms):

        for key,value in parms.items():
            # print('key',key,'value',value)
            self.db.update_record(self.size,key,value,'name','top')


    def load_plc_parms(self):

        if sql_mode=='none':
            return PLC_PARMS   

        try:

            parms=self.db.get_all_content(self.plc)
        
            return parms
        except:
            print('Except load_plc_parms')
            return []


    def load_plc_ip(self):

        if sql_mode=='none':
            return PLC_IP    

        if sql_mode=='sqlit':

            ip=self.db.search( self.setting_tabel , 'id', 0 )
            # print('ip',ip)
            return ip['plc_ip']
        try:
            ip=self.db.search( self.setting_tabel , 'id', 0 )[0]
            # print('ip',ip)
            return ip['plc_ip']
        except:
            print('Error load_plc_ip')
            return 'Null'

    def save_plc_ip(self,ip):

        if sql_mode=='none':
            return True  

        res = self.db.update_record(self.setting_tabel, 'plc_ip',ip, 'id', '0')


    def update_plc_parms(self, plc_parms):
        if sql_mode=='none':
            return True  
        try:
            for _,param in enumerate(plc_parms.keys()):
                # update_record(self,table_name,col_name,value,id,id_value):
                i=_+1
                #print('_',i,'   ',param,str(plc_parms[param]))
                
                res = self.db.update_record(self.plc, 'path', str(plc_parms[param]), 'name',str(param))

            return res
        except:
            print('Error update_plc_parms')

            return False


    def load_calibration_parms(self):

        if sql_mode=='none':
            return(GENERAL_SETTINGS['top_calibration'],GENERAL_SETTINGS['side_calibration'])

        # if sql_mode=='sqlite':
        #     record = self.db.search( self.setting_tabel , 'id', 0)
        #     print('asd',record)
        #     return (record['top_calibration'],record['side_calibration'])

        try:
            record = self.db.search( self.setting_tabel , 'id', 0)[0]
          
            return (record['top_calibration'],record['side_calibration'])
        except:
            print('Error load_calibration_parms')

            return []



    def save_top_calibration(self,value):

        self.res = self.db.update_record(self.setting_tabel, 'top_calibration', str(value) ,'id','0')
        return self.res

    def save_side_calibration(self,value):

        self.res = self.db.update_record(self.setting_tabel, 'side_calibration', str(value) ,'id','0')
        return self.res


    def set_language(self,name):
        if sql_mode=='none':
            return True
        self.db.update_record(self.setting_tabel, 'language',str(name), 'id', '0')


    def load_language(self):
        if sql_mode=='none':
            return 'english'

        # if sql_mode=='sqlite':
        #     record = self.db.search( self.setting_tabel , 'id', '0' )
        # # print(record)
        #     return record['language']

        record = self.db.search( self.setting_tabel , 'id', '0' )[0]
        # print(record)
        return record['language']


    def load_history(self):

        if sql_mode=='none':
            record={'id': 0, 'all_screw': 0, 'defect': 0}
            return record

        # if sql_mode=='sqlite':
        #     record = self.db.search( self.setting_tabel , 'id', '0' )
        # # print(record)
        #     return record['language']

        record = self.db.search( self.history , 'id', '0' )
      
        return record[0]

    def update_history(self,all,defect):

        res = self.db.update_record(self.history, 'all_screw',str(all), 'id','0')
        res = self.db.update_record(self.history, 'defect', defect, 'id','0')





    def load_senser_detection(self):


        if sql_mode=='none':
            record={'x1': 0,'x2': 0,'y1': 0,'y2': 0,'area': 0,'thresh_min': 0,'thresh_max': 0,}
            return record

        # if sql_mode=='sqlite':
        #     record = self.db.search( self.setting_tabel , 'id', '0' )
        # # print(record)
        #     return record['language']

        record = self.db.search( self.sensor_detection , 'id', '0' )
      
        return record[0]


    def set_senser_detection(self,values):
        if sql_mode=='none':
            return True
        for _,param in enumerate(values.keys()):
            res = self.db.update_record(self.sensor_detection, param, str(values[param]), 'id','0')








if __name__ == '__main__':
    db = dataBaseUtils(user_name='root',password='password')
    v= db.load_senser_detection()
    print(v)
    v = {'x1': 4, 'y1': 1, 'x2':1, 'y2':1, 'area':1, 'thresh_min': 1, 'thresh_max': 1, 'id': 0}
    db.set_senser_detection(v)
    v= db.load_senser_detection()
    print(v)
    # db.load_cam_params(0)
    # db.load_general_setting_params()
    # db.update_history(5,3)
    # db.load_history()
    # db.load_cam_params(2)
    # db.db.update_record('plc_setting', 'path',' asdasd', 'name','run')
    # x=db.load_calibration_parms()
    # print(x)
    # x=db.load_calibration_parms()
    # print(x)
    # db.save_top_calibration(70)
    # x=db.load_calibration_parms()
    # print(x)  
    # db.save_side_calibration(90.885)
    # x=db.load_calibration_parms()
    # print(x)  
    # db.get_size_table('side_live')
    # parms={'min_x':10,'min_y':20,'max_x':30,'max_y':40}
    # db.set_size_table_side(parms)
    # db.get_size_table('side_live')
    # db.get_size_table('top_live')
    # parms={'min_x':10,'min_y':20,'max_x':30,'max_y':40}
    # db.set_size_table_top(parms)
    # db.get_size_table('top_live')
    # x=db.load_plc_parms()
    # x=db.load_plc_ip()
    # print(x)
    # db.save_plc_ip('asdw')
    # x=db.load_plc_ip()
    # print(x)
    # x=db.get_size_table('top')
    # print(x)
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

    #data={'name':'asghar'}

    #db.add_screw(data)

    #x=db.search_page_1('asghar')
    #print('x',x)

    # x=db.get_dataset_path()

    # print(x)
