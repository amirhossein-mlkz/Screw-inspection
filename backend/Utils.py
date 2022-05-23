
import cv2
import numpy as np
from backend import cvTools


def threshould_view(img,thresh, color=(40,127,255),  mask_roi = None):
    if len(img.shape) == 2:
        res = cv2.merge((img, img, img))
    else:
        res = np.copy(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    #_,mask = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    mask = cvTools.threshould(img, thresh, mask_roi)
    thresh_layer = np.zeros_like(res)
    
    for i in range(3):
        thresh_layer[:,:,i] = color[i]/255 * mask
    
    thresh_layer = thresh_layer.astype(np.uint8)
    res = cv2.addWeighted(res,0.6, thresh_layer,0.4, 1)
    return res