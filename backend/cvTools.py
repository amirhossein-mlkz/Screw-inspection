import cv2
import numpy as np

MAX_NOISE_AREA = 4000


def threshould(img, thresh , mask_roi = None):
    _,mask = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3))
    
    mask = cv2.erode(mask, kernel, iterations=3)
    mask = cv2.dilate(mask, kernel, iterations=3)
    
    cnts,_ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    # res_cnts = list( filter(lambda x: cv2.contourArea(x)>MAX_NOISE_AREA , cnts) )
    # res_mask = np.zeros_like(mask)
    # res_mask = cv2.drawContours(res_mask, res_cnts, -1, 255,-1)
    
    cnts.sort(key = lambda x:cv2.contourArea(x))
    res_mask = np.zeros_like(mask)
    res_mask = cv2.drawContours(res_mask, [cnts[-1]], 0, 255,-1)
    
    if mask_roi is not None:
        res_mask = cv2.bitwise_and( res_mask, mask_roi)
    
    #print(mask_roi)
    #cv2.imshow('mask', mask_roi)
    #cv2.waitKey(5)
    return res_mask




def rects2mask(img_sizs, rects, defualt=255):
    mask = np.zeros(img_sizs, dtype=np.uint8)
    if len(rects) == 0:
        mask+= defualt
    for rect in rects:
        pt1, pt2 = rect
        mask = cv2.rectangle(mask, tuple(pt1), tuple(pt2), 255, thickness=-1)
    return mask