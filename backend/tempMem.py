
import cv2
import numpy as np



class scewSettingMem:
    
    def __init__(self):
        self.path = None
    
    
    
    def set_img_path(self,path):
        self.img_path = path
        self.img = cv2.imread(path)
    
        
    def get_img_path(self):
        return self.img_path
    
    
    
    def get_img(self):
        return np.copy(self.img)

