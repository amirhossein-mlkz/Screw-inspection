
import cv2
import numpy as np

class Scew:
    
    
    def __init__(self,name):
        self.name = name
    
    def set_img_path(self,path):
        self.img_path = path
        self.img = cv2.imread(path)
        