import os
import time

import cv2
import numpy as np
from PySide6.QtCore import Signal, QMutex, QObject

#from backend.Camera.dorsaPylon import Camera, Collector
#from Constants import Constant

# from ctypes import windll #new


# timeBeginPeriod = windll.winmm.timeBeginPeriod #new
# timeBeginPeriod(1) #new




class cameraWorker(QObject):
    success_grab_signal = Signal(np.ndarray)
    success_grab_signal = Signal()

    grabb_image_error = Signal()
    finished = Signal()

    


    def __init__(self, camera, timeout = 2000):
        super().__init__()
        self.camera = camera
        self.grabbing = True
        self.new_camera = None
        self.timeout = timeout


    def change_camera(self, new_camera):
        self.new_camera = new_camera

    
    def grabber(self,):
        # t = 0
        self.time = time.time()
        self.fps = 0
        self.test_timer = time.time()
        while self.grabbing:
            try:
                if self.new_camera:
                    self.camera = self.new_camera
                    self.new_camera = None

                if (time.time() - self.time) * 1000 > self.timeout:
                    self.grabb_image_error.emit()
                    self.time = time.time()

                #if self.camera.Status.is_grabbing():
                if self.camera.camera.IsGrabbing():
                    #ret, img = self.camera.getPictures(img_when_error=None)
                    ret, img = self.camera.getPictures()
                    if ret:
                        self.success_grab_signal.emit()
                  
                            
                    self.time = time.time()
                
                else:
                    self.time = time.time()
                
                
                

            except Exception as e:
                pass
                #print('camera Error happend in thread while !', repr(e))
            
            time.sleep(0.008)

        print('end of Camra Thread While')
        self.finished.emit()

