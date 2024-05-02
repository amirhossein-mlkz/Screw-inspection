
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

        self.data['active_tools'] = []
        #self.set_img_path(IMG_PATH_DEF)

        
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
    def set_img_path(self,path):
        self.img = cv2.imread(path)
        self.data['img_path'] = path

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

    def set_thresh_min(self, page, subpage, value, idx=0):
        name = 'thresh_min{}'.format(idx)
        self.set_value( page, subpage, name, value)


    def get_thresh_min(self, page, subpage, idx=0):
        name =  'thresh_min{}'.format(idx)
        return self.get_value( page, subpage, name, 0)
    
    def get_edge_thresh(self, page, subpage, idx=0):
        name =  'edge_thresh{}'.format(idx)
        return self.get_value( page, subpage, name, 0)
    

    def set_thresh_max(self, page, subpage, value, idx=0):
        name = 'thresh_max{}'.format(idx)
        self.set_value( page, subpage, name, value)
    
    def get_thresh_max(self, page, subpage, idx=0):
        name =  'thresh_max{}'.format(idx)
        return self.get_value( page, subpage, name, 0)
        
    
    #-----------------------------------------
    def set_thresh_inv(self, page, subpage, value, idx=0):
        name = 'thresh_inv{}'.format(idx)
        self.set_value( page, subpage, name, value)
        
        
        
    def get_thresh_inv(self, page, subpage,  idx=0):
        name = 'thresh_inv{}'.format(idx)
        return self.get_value( page, subpage, name, False)



    #-----------------------------------------
    def set_checkbox(self, page, subpage, name, value):
        self.set_value( page, subpage, name, value)
        
        
        
    def get_checkbox(self, page, subpage,name):
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
    def set_circels_roi(self, page, subpage, shapes, idx=0):
        name = 'circels_roi{}'.format(idx)
        if len(shapes):
            shapes.sort(key= lambda x : x[1] )
        self.set_value( page, subpage, name, shapes)

    def get_circels_roi(self, page, subpage, idx=0):
        name = 'circels_roi{}'.format(idx)
        circles = self.get_value( page, subpage, name, [])
        if len(circles):
            circles.sort(key= lambda x : x[1] )
        return circles.copy()
    

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

    def get_subpages_parms_list(self,page):
        self.check_and_build_page(page)
        res = []
        for sub_page, parms in self.data[self.setting_key][page].items():
            res.append(parms)
        return res

    #-----------------------------------------
    def set_active_tools(self, names):
        self.data['active_tools'] = names
    
    def get_active_tools(self):
        return self.data['active_tools'] 
  
    #-----------------------------------------
    
    def set_multi_option(self, page_name, subpage_name, group_name,  option_name):
        #group_name = group_name + 'option'
        self.set_value( page_name, subpage_name, group_name, option_name)

    def get_multi_option(self, page_name, subpage_name, group_name):
        #group_name = group_name + 'option'
        return self.get_value( page_name, subpage_name, group_name, None )


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
