import cv2
from cv2 import circle
from cv2 import contourArea
import numpy as np

THRESH_C = 7



def threshould(img, thresh , mask_roi = None, inv=False):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    if inv:
        _,mask = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY_INV)
    else:
        _,mask = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3))
    
    #mask = cv2.erode(mask, kernel, iterations=3)
    #mask = cv2.dilate(mask, kernel, iterations=3)
    
    
           
    if mask_roi is not None:
        mask = cv2.bitwise_and( mask, mask , mask=mask_roi)
    return mask




def adp_threshould(img, bsize , c,  mask_roi = None, thresh_inv = False):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    
    cv2.imshow('img', img)

    #img = clahe.apply(img)
    img = cv2.blur(img,(5,5))
    
    cv2.imshow('cl', img)
    bsize = bsize//2
    bsize = bsize * 2 + 1
    
    if thresh_inv:
        mask = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV    , bsize, c )
    else:
        mask = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY    , bsize, c )
    # grad_x = cv2.Sobel(img, cv2.CV_64F, 1,0 , ksize=3)
    # grad_y = cv2.Sobel(img, cv2.CV_64F, 0,1 , ksize=3)
    
    # abs_grad_x = cv2.convertScaleAbs(grad_x)
    # abs_grad_y = cv2.convertScaleAbs(grad_y)
    
    
    # mask = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    # _,mask = cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY)
    
    # cv2.imshow('mask', mask)
    # kernel = np.ones((3,3))
    
    
    
    
    

           
    if mask_roi is not None:
        mask = cv2.bitwise_and( mask, mask , mask=mask_roi)
    
    cv2.imshow('fres_mask', mask)   
    cv2.waitKey(30)
    return mask





def filter_noise_area(mask, noise_filter=0):
    
    h,w = mask.shape[:2]
    area = h * w
    noise_area = area / 10 * (noise_filter/100) #Optioanl Formula
    cnts,_ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    res_cnts = list( filter(lambda x: cv2.contourArea(x)>noise_area , cnts) )
    res_mask = np.zeros_like(mask)
    res_mask = cv2.drawContours(res_mask, res_cnts, -1, 255,-1)
    return res_mask





def rects2mask(img_size, rects, defualt=255):
    mask = np.zeros(img_size, dtype=np.uint8)
    if len(rects) == 0:
        mask+= defualt
    for rect in rects:
        pt1, pt2 = rect
        mask = cv2.rectangle(mask, tuple(pt1), tuple(pt2), 255, thickness=-1)
    return mask



def mask_area( img_size, out_shape, inner_shape, shape_type):
    mask = np.zeros(img_size, dtype=np.uint8)
    draw_func = shapes_drawer( shape_type, color=255, thickness=-1)
    mask = draw_func( mask , [out_shape] )
    
    draw_func = shapes_drawer( shape_type, color=0, thickness=-1)
    mask = draw_func( mask , [inner_shape] )
    
    return mask
    
    
    
    
def shapes_drawer(shape_type, color, thickness=-1):
    def func(img, shapes):
        if shape_type == 'circle':
            for shape in shapes:
                center , radius = shape
                res = cv2.circle(img, tuple(center) , radius, color=color , thickness=thickness)
        
        elif shape_type == 'rect':
            for shape in shapes:
                pt1 , pt2 = shape
                res = cv2.rectangle(img , tuple(pt1) , tuple([pt2]) , color=color, thickness=thickness)
        
        elif shape_type == 'poly':
            shapes = np.array(shapes).reshape((-1,1,2))
            res = cv2.drawContours( img, shapes, -1, color=color, thickness=thickness)
            
        return res
    return func


def crop_rect(img, rect):
    [[x1,y1], [x2,y2]] = rect
    crop = img[y1:y2 , x1:x2]
    return np.copy( crop )





def extract_bigest_contour(mask):
    cnts,_ = cv2.findContours(mask , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts.sort( key = lambda x:cv2.contourArea(x) , reverse=True)
    return cnts[0]        



if __name__ == '__main__':
    
    mask_img = cv2.imread('mask.jpg', 0)
    img = cv2.imread( 'img.jpg' , 0 )
    # cv2.imshow('m',mask_area)
    # cv2.imwrite('mask.jpg', mask_area)
    # cv2.waitKey(30)
    mask = adp_threshould( img , 11, 11 , None )
    #mask = cvTools.filter_noise_area(mask , noise_filter )
    
    
    
    #img = Utils.mask_viewer(img, mask)
    
    cnts,_ = cv2.findContours(mask , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts.sort( key = lambda x:cv2.contourArea(x) , reverse=True)
    
    hull=cv2.convexHull (cnts[0])
    cv2.drawContours (img , [hull] ,0, (0,0,255) , thickness=5)
    
    cv2.waitKey(0)
    # cv2.imshow('mask_area', mask_area )