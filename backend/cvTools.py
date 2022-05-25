import cv2
import numpy as np


def threshould(img, thresh , mask_roi = None):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    _,mask = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3))
    
    mask = cv2.erode(mask, kernel, iterations=3)
    res_mask = cv2.dilate(mask, kernel, iterations=3)
           
    if mask_roi is not None:
        res_mask = cv2.bitwise_and( res_mask, mask_roi)
    return res_mask





def filter_noise_are(mask, noise_filter=0):
    
    h,w = mask.shape[:2]
    area = h * w
    noise_area = area / 10 * (noise_filter/100) #Optioanl Formula
    cnts,_ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    res_cnts = list( filter(lambda x: cv2.contourArea(x)>noise_area , cnts) )
    res_mask = np.zeros_like(mask)
    res_mask = cv2.drawContours(res_mask, res_cnts, -1, 255,-1)
    return res_mask





def rects2mask(img_sizs, rects, defualt=255):
    mask = np.zeros(img_sizs, dtype=np.uint8)
    if len(rects) == 0:
        mask+= defualt
    for rect in rects:
        pt1, pt2 = rect
        mask = cv2.rectangle(mask, tuple(pt1), tuple(pt2), 255, thickness=-1)
    return mask




def crop_rect(img, rect):
    [[x1,y1], [x2,y2]] = rect
    crop = img[y1:y2 , x1:x2]
    return np.copy( crop )