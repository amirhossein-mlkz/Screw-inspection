
import cv2
import numpy as np

class Scew:
    
    
    def __init__(self,name):
        self.name = name
    
    def set_top_img_path(self,path):
        self.top_img_path = path
        self.top_img = cv2.imread(path)
        
    
    def set_side_img_path(self,path):
        self.side_img_path = path
        self.side_img = cv2.imread(path)
    
    
    def set_side_main_thresh(self, thresh):
        self.side_main_thresh = thresh