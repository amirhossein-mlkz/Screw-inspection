
from email.policy import default
import json
import os

import cv2

IMG_PATH_DEF = 'images/defualt.jpg'

class screwJson():
    
    def __init__(self,):
        
        self.setting_key = 'settings'
        
        self.data = {
            
            self.setting_key: 
            {
                
            }
        }

        
        #self.set_img_path('images/test1_0_12.png')
        
    #-----------------------------------------
    def read(self, path, dircetion):
        path = os.path.join(path, dircetion + '.json')
        with open(path) as jfile:
            file = json.load(jfile)
        
        self.data = file
        self.img = cv2.imread( self.get_img_path() )
        

    def write(self,path):    
        path = os.path.join(path, self.data['direction'] + '.json')
        with open(str(path), 'w') as f:
            json.dump(self.data, f ,indent=4, sort_keys=True)
            
    #-----------------------------------------
    def set_name(self,name):
        self.data['name'] = name
    
    def get_name(self):
        return self.data.get('name', '') 
    
    #-----------------------------------------
    def set_img_path(self,path, page=None, subpage = None):
        self.img = cv2.imread(path)
        self.data['img_path'] = path
        if page is not None:
            self.check_and_build_page( page )
            if subpage is not None:
                self.check_and_build_subpage(page, subpage)
                self.data[self.setting_key][page][subpage]['img_path'] = path
            else:
                self.data[self.setting_key][page]['img_path'] = path
            
    
    def get_img_path(self):
        return self.data.get('img_path', IMG_PATH_DEF)
    #-----------------------------------------
    
    def get_img(self):
        return self.img
    
    
    def check_and_build_page(self, page_name):
        if self.data[self.setting_key].get(page_name, None) is None:
            self.data[self.setting_key][page_name] = {}
            
    
    def check_and_build_subpage(self, page_name, subpage):
        if self.data[self.setting_key][page_name].get(subpage, None) is None:
            self.data[ self.setting_key ] [ page_name][ subpage ] = {}
            
    #-----------------------------------------
    def set_value(self, page , subpage, name, value):
        self.check_and_build_page( page )
        if subpage is not None:
            self.check_and_build_subpage(page, subpage)
            self.data[self.setting_key][page][subpage][name] = value
        else:
            self.data[self.setting_key][page][name] = value
    
    
    
    def get_value(self, page , subpage, name, defualt_value):
        settings = self.data[self.setting_key]
        if settings.get(page, None) is None:
            return defualt_value
        else:
            page_setting = settings.get(page)
            if subpage is None:
                return page_setting.get( name, defualt_value )
            
            else:
                if page_setting.get(subpage, None) is None:
                    return defualt_value
                else:
                    return page_setting[subpage].get( name, defualt_value)
    
    #-----------------------------------------
    def set_direction(self, dir):
        self.data['direction'] = dir
    
    def get_direction(self):
        return self.data['direction'] 
    
    #-----------------------------------------
    def set_thresh(self, page, subpage, value, idx=0):
        name = 'thresh{}'.format(idx)
        self.set_value( page, subpage, name, value)
        
        
    def get_thresh(self, page, subpage, idx=0):
        name =  'thresh{}'.format(idx)
        return self.get_value( page, subpage, name, 0)
        
    
    #-----------------------------------------
    def set_thresh_inv(self, page, subpage, value, idx=0):
        name = 'thresh_inv{}'.format(idx)
        self.set_value( page, subpage, name, value)
        
        
        
    def get_thresh_inv(self, page, subpage,  idx=0):
        name = 'thresh_inv{}'.format(idx)
        return self.get_value( page, subpage, name, False)

    #-----------------------------------------
    def set_checkbox(self, page, subpage, name, value, idx=0):
        self.set_value( page, subpage, name, value)
        
        
        
    def get_checkbox(self, page, subpage,name,  idx=0):
        return self.get_value( page, subpage, name, False)
    
    #-----------------------------------------
    def set_noise_filter(self, page, subpage, value, idx=0):
        name = 'noise_filter{}'.format(idx)  
        self.set_value( page, subpage, name, value)
        
        
        
        
    def get_noise_filter(self, page, subpage, idx=0):
        name = 'noise_filter{}'.format(idx)
        return self.get_value( page, subpage, name, 0)
    #-----------------------------------------
    def set_rect_roi(self, page, subpage,  pt1, pt2, idx=0):
        if len(pt1) == 0 or len(pt2) == 0:
                value = []
        else:
            value = [ list(pt1), list(pt2) ]

        name = 'rect_roi{}'.format(idx)
        self.set_value( page, subpage, name, value)
    
    
    
    
    def get_rect_roi(self, page, subpage, idx=0):
        name = 'rect_roi{}'.format(idx)
        return self.get_value( page, subpage, name, [[],[]])
    
    
    #-----------------------------------------
    def set_limits(self, page, subpage,  data):
        name = 'limits'
        self.set_value( page, subpage, name, data)
    
    
    
    
    def get_limits(self, page, subpage):
        name = 'limits'
        return self.get_value( page, subpage, name, {'min':{}, 'max':{}})
    
    
    def get_limit(self, name, page, subpage):
        _name_ = 'limits'
        parms = self.get_value( page, subpage, _name_, {'min':{}, 'max':{}})
        return {'min': parms['min'].get(name,0) , 
                'max': parms['max'].get(name,0)}
    

    #-----------------------------------------
    def set_numerical_parm(self, page, subpage, name,  value ):
        self.set_value( page, subpage, name, value)
        
    def get_numerical_parm(self, page, subpage, name):
        return self.get_value( page, subpage, name, 0)
    #-----------------------------------------
    def get_setting(self, page, subpage):
        settings = self.data[self.setting_key]
        if subpage is None:
            return settings.get( page , {})
        else:
            return settings.get( page , {}).get( subpage, {}  )

    #-----------------------------------------
    def add_subpage(self, page, subpage):
        self.check_and_build_page(page)
        self.check_and_build_subpage(page, subpage)
    
    def remove_subpage(self, page, subpage):
        self.check_and_build_page(page)
        self.data[self.setting_key][page].pop( subpage, None )
    
    def get_subpages(self, page):
        self.check_and_build_page(page)
        return list(self.data[self.setting_key][page].keys())



    def set_active_tools(self, names):
        self.data['active_tools'] = names
    
    def get_active_tools(self):
        return self.data['active_tools'] 
    #     self.dataset_details['basic']=self.main_parms
    #     self.dataset_details['classification']=self.classification_details
    #     self.dataset_details['binary']=self.binary_details

    #         # return {'user_name':user_name,'user_id':user_id,'dataset_name':dataset_name,'path':path,'max_size':max_size}
    #     path=os.path.join(parms['path'],parms['dataset_name'])
    #     self.write(os.path.join(path,str(parms['dataset_name']+'.json')))
    #     try:
    #         pathStructure.create_dataset_stracture(path)
    #     except:
    #         path
    # def write(self,path):    
    #     #print('write',path)
    #     with open(str(path), 'w') as f:
    #         json.dump(self.dataset_details, f,indent=4, sort_keys=True)
    #         # json.dump(self.classification, f,indent=4, sort_keys=True)


        
    # def set_user_name_database(self,name):
    #     self.user_name_database=name
    # #--------------------------------------------------------
    # #
    # #--------------------------------------------------------
    # def set_user(self, name):
    #     self.main_parms['user_name'] = name

    # def set_user_id(self, user_id):
    #     self.main_parms['user_id'] = user_id


    # def set_dataset_name(self, name):
    #     self.main_parms['dataset_name'] = name

    # def set_path(self, path,name):
    #     self.main_parms['path'] = str(path+name)

    # def set_max_size(self, max_size):
    #     self.main_parms['max_size'] = max_size
    
    # def set_create_date(self,date):
    #     self.main_parms['date_created'] = date_funcs.get_date()
    
    # def set_modify_date(self,date):
    #     self.main_parms['date_modify'] = date
    
    # def set_count_defect(self,num):
    #     self.binary_details['count_defect'] = num
    
    # def set_count_perfect(self,num):
    #     self.binary_details['count_perfect'] = num

    # def set_classification_parms(self,defects_list):

    #     self.classification_details['defects_list'] = list(defects_list)

    # def set_parms_classification(self,name,count):

    #     self.classification_details[name] = count

    # ######################################
    # #  Modify        ///////////////

    # def modify_defect(self,reset=False):
    #     file=self.read_modify()
    #     count=file['binary']['count_defect']
    #     if reset:
    #         count=-1
    #     file['binary']['count_defect']=count+1
    #     print('modify',file)
    #     try:
    #         file=self.modify_date(file)
    #     except:
    #         print('eror modify date')
    #         pass
    #     self.write_modify(file)
    
    # def modify_perfect(self,reset=False):
    #     file=self.read_modify()
    #     count=file['binary']['count_perfect']
    #     if reset:
    #         count=-1
    #     file['binary']['count_perfect']=count+1
    #     try:
    #         file=self.modify_date(file)
    #     except:
    #         pass
    #     self.write_modify(file)
    
    # def add_update_classification(self,name,AI=True,number=0):
    #     count=number
    #     file=self.read_modify()

    #     if count !=0:
    #         AI=False

    #     if str(name) in file['classification'].keys():
    #         if AI:
    #             print('ai')
    #             print((file['classification'][name]['count']))
    #             count=int(file['classification'][name]['count'])
    #             count_dict={'count':count+1}
    #             file['classification'][name]=count_dict
    #         else :
    #             count_dict={'count':count}
    #             file['classification'][name]=count_dict

    #     else :
    #         count_dict={'count':count}
    #         name_dict={name:count_dict}
    #         file['classification'].update(name_dict)
    #         print(file)
    #         # self.add_update_classification(name,AI,count)
    #     self.write_modify(file)


    # def read_modify(self):
    #     print('user_name',self.user_name_database)
    #     default_name = self.db.get_default_dataset(self.user_name_database)
    #     print('default_name',default_name)
    #     path = self.db.get_path_dataset(default_name)
    #     path=os.path.join(path,default_name)
    #     print('path',path)
    #     with open(path+'.json') as jfile:
    #         file = json.load(jfile)
    #     return file


    # def modify_date(self,file):
    #     file['basic']['date_modify']=date_funcs.get_datetime()
    #     return file


    # def write_modify(self,file):
    #     path = os.path.join(file['basic']['path'],file['basic']['dataset_name'])
    #     with open(str(path+'.json'), 'w') as f:
    #         json.dump(file, f,indent=4, sort_keys=True)


    





if __name__=='__main__':
    import dbUtils
    path = dbUtils.get_screw_path('pich2')
    screw  = screwJson()
    
    #screw.set_name('aaaaaaa')
    #screw.set_direction('ccccc')
    #screw.write(path)
    path = 'screws\\pich2\\top.json'
    path = 'database\\screws\\Pich2\\top.json'
    
    a = screw.read(path)
    # j = dataset_json()
    # j.set_user_name_database('ali')
    # i=1
    # # j.add_update_classification('ads3',number=11)
    # # for i in range(100):
    # # j.modify_defect()
    # j.modify_perfect()
