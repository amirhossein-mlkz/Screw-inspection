
import cv2
import numpy as np



def mask_viewer(img,mask, color=(40,127,255)):
    if len(img.shape) == 2:
        img = cv2.merge((img, img, img))

        
    thresh_layer = np.zeros_like(img)
    
    for i in range(3):
        thresh_layer[:,:,i] = color[i]/255 * mask
    
    thresh_layer = thresh_layer.astype(np.uint8)
    res_select = cv2.addWeighted(img,0.4, thresh_layer,0.6, 1)
    
    not_mask = cv2.bitwise_not(mask)
    res_select = cv2.bitwise_and(res_select, res_select, mask = mask)
    res_unselect = cv2.bitwise_and(img, img, mask= not_mask)
    
    return res_select + res_unselect











def rect_list2dict(rect):
    rect_dict = {}
    if len(rect) == 2: 
        if len(rect[0]) == 2 and len(rect[1]) == 2:
            rect_dict['x1'] = rect[0][0]
            rect_dict['y1'] = rect[0][1]
            rect_dict['x2'] = rect[1][0]
            rect_dict['y2'] = rect[1][1]
            return rect_dict
    return {'x1':0, 'y1':0, 'x2':0, 'y2':0}



def rect_dict2list(rect_dict):
    rect = [ [rect_dict['x1'] , rect_dict['y1'] ], 
             [rect_dict['x2'] , rect_dict['y2'] ]
            ]
    
    return rect




def is_rect(rect):
    if len(rect) == 2:
        if len(rect[0]) == 2 and len(rect[1]) == 2:
            return True
    return False
    