
from re import T
import cv2
from cv2 import circle
from cv2 import resize
import numpy as np
import pandas as pd
import copy


try:
    from backend import Utils
    from backend import mathTools
except:
    import Utils
    import mathTools   

import time
def time_measure(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        out = func(*args, **kwargs)
        t = time.time() - t
        print(f'time {func.__name__} {t}')
        return out
    return wrapper

THRESH_C = 7



def preprocess(img):
    normalizedImg = np.zeros_like(img)
    normalizedImg = cv2.normalize(img,  normalizedImg, 0, 255, cv2.NORM_MINMAX)
    return normalizedImg

def threshould(img, thresh , mask_roi = None, inv=False):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    if inv:
        _,mask = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY_INV)
    else:
        _,mask = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    #kernel = np.ones((3,3))
    
    #mask = cv2.erode(mask, kernel, iterations=3)
    #mask = cv2.dilate(mask, kernel, iterations=3)
           
    if mask_roi is not None:
        mask = cv2.bitwise_and( mask, mask , mask=mask_roi)
    return mask


def threshould_minmax(img, thresh_min, thresh_max , mask_roi = None):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    _,mask_min = cv2.threshold(img, thresh_min, 255, cv2.THRESH_BINARY)
    _,mask_max = cv2.threshold(img, thresh_max, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((3,3))
    
    mask = cv2.erode(mask, kernel, iterations=3)
    mask = cv2.dilate(mask, kernel, iterations=3)

           
    if mask_roi is not None:
        mask = cv2.bitwise_and( mask_min, mask_max , mask=mask_roi)
    else:
        mask = cv2.bitwise_and( mask_min, mask_max)


    return mask


def erode(mask, iteration=3):
    kernel = np.ones((3,3))
    
    mask = cv2.erode(mask, kernel, iterations=iteration)
    mask = cv2.dilate(mask, kernel, iterations=iteration)


def threshould_new(img, thresh , mask_roi = None, inv=False):
    thresh=max(thresh,5)
    if thresh%2==0:
        thresh+=1
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    if inv:
        mask = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,thresh,10)
    else:
        mask = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,thresh,10)
    kernel = np.ones((3,3))
    
    #mask = cv2.erode(mask, kernel, iterations=3)
    #mask = cv2.dilate(mask, kernel, iterations=3)
    
    
           
    if mask_roi is not None:
        mask = cv2.bitwise_and( mask, mask , mask=mask_roi)
    return mask

def morph_correction(mask, iter, kernel_size=3):
    kernel = np.ones((kernel_size,kernel_size))
    mask = cv2.dilate(mask, kernel=kernel, iterations=iter)
    mask = cv2.erode(mask, kernel=kernel, iterations=iter)
    return mask


def cnt_correction(mask, approx=0.005):
    cnt = extract_bigest_contour(mask)
    cntlen=cv2.arcLength (cnt ,True)
    approxCnt=cv2.approxPolyDP(cnt , cntlen*approx, True)
    mask = cv2.drawContours( mask, [approxCnt], 0, 255, thickness=-1)
    return mask


def adp_threshould(img, bsize , c,  mask_roi = None, thresh_inv = False):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    
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


def get_gray_color( img, mouse_pt):
    if img is None:
        return 0
    h,w = img.shape[:2]
    x,y = mouse_pt
    x, y = int( x * w ) , int( y * h )

    if len(img.shape) == 3:
        img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
        #b,g,r = img[y,x]
        #0.299 * r + 0.587 * b + 0.11 * g
    return img[y,x]


def build_gcolor_img( color, res_size=(100,100), color_type='gray'):
    if color_type=='gray':
        res_img = np.zeros( res_size, dtype=np.uint8 )
    elif color_type =='rgb':
        res_img = np.zeros( res_size + (3,), dtype=np.uint8 )
    res_img = res_img + color
    return res_img




def remove_belt(mask, rect_roi, thresh=0.6 , left_margin = 30 , right_margin = 10):
    crop_mask = crop_rect( mask, rect_roi ) 
    h,w = crop_mask.shape
    cols_sum = np.sum(crop_mask, axis = 0) / h / 255
    idxs = np.argwhere( cols_sum > thresh )
    
    if len(idxs)>10:
        start_idx = idxs.min() - left_margin
        end_idx = idxs.max() + right_margin
    
        start_idx += rect_roi[0][0]
        end_idx += rect_roi[0][0]
    
        res_mask = np.copy( mask )
        res_mask[:,start_idx:end_idx] = 0

        return res_mask, (start_idx , end_idx)
    return mask, (0,0)



def filter_noise_area(mask, noise_filter=0):
    
    h,w = mask.shape[:2]
    area = h * w
    noise_area = area / 5 * (noise_filter/100) #Optioanl Formula
    cnts,_ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = list(cnts)
    res_cnts = list( filter(lambda x: cv2.contourArea(x)>noise_area , cnts) )
    res_mask = np.zeros_like(mask)
    res_mask = cv2.drawContours(res_mask, res_cnts, -1, 255,-1)
    return res_mask


def filter_area(mask, min_area):
    cnts, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    idxs = np.arange(len(cnts))
    areas  = list( map( lambda x:cv2.contourArea( cnts[x] ), idxs ))
    idxs = list(filter( lambda x:areas[x]>min_area, idxs ))
    
    res_cnts = []
    res_areas = []
    for i in idxs:
        res_cnts.append(cnts[i] )
        res_areas.append(areas[i] )
        
    return res_cnts, np.array( res_areas )


def rects2mask(img_size, rects, defualt=255):
    mask = np.zeros(img_size, dtype=np.uint8)
    if len(rects) == 0:
        mask+= defualt
    for rect in rects:
        if len(rect)==2:
            pt1, pt2 = rect
            if len(pt1) == 2 and len(pt2) == 2:
                mask = cv2.rectangle(mask, tuple(pt1), tuple(pt2), 255, thickness=-1)
    return mask


def circels2mask(img_size, circels , defualt=0):
    mask = np.zeros(img_size, dtype=np.uint8)
    if len(circels) == 0:
        mask+= defualt
    for circel in circels:
        if len(circel)==2:
            center, r = circel
            if len(center):
                mask = cv2.circle(mask, tuple(center), r, 255, thickness=-1)
    return mask


def polys2mask(img_size, cnts , defualt=255):
    mask = np.zeros(img_size, dtype=np.uint8)
    if len(cnts) == 0:
        mask+= defualt
    else:
        mask = cv2.drawContours(mask, cnts, -1, 255, thickness=-1)
    return mask


def shape2mask(img_size, shape, shape_type, default=255):
    if shape_type == 'circel':
        mask = circels2mask(img_size, [shape], default)

    elif shape_type == 'rect':
        mask = rects2mask(img_size, [shape], default)

    elif shape_type == 'poly':
        mask = polys2mask(img_size, [shape], default)

    else:
        mask = np.zeros(img_size, dtype=np.uint8)
        mask = mask + default
    
    return mask


def donate2mask(img_size, circels , defualt=255):
    mask = np.zeros(img_size, dtype=np.uint8)
    if len(circels) == 0:
        mask+= defualt
        return mask

    circels.sort( key = lambda x:x[1], reverse=True ) #sort by radius
    center, r = circels[0]
    mask = cv2.circle(mask, tuple(center), r, 255, thickness=-1)
    if len(circels) == 2:
        center, r = circels[1]
        mask = cv2.circle(mask, tuple(center), r, 0, thickness=-1)

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
    if Utils.is_rect(rect): 
        [[x1,y1], [x2,y2]] = rect
        crop = img[y1:y2 , x1:x2]
        return np.copy( crop )
    return img




def extract_bigest_contour(mask):
    cnts,_ = cv2.findContours(mask , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = list(cnts)
    cnts.sort( key = lambda x:cv2.contourArea(x) , reverse=True)
    if len(cnts)>0:
        return cnts[0]
    return []     


def mask_bigest_contour(mask):
    cnts,_ = cv2.findContours(mask , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = list(cnts)
    cnts.sort( key = lambda x:cv2.contourArea(x) , reverse=True)
    
    res_mask = np.zeros_like(mask)
    return cv2.drawContours(res_mask, cnts, 0, 255, thickness=-1)
    

def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


def correct_rotation_angle(mask , left_or_right='left'):
    
    cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = list(cnts)
    cnts = list(cnts)
    if len(cnts)==0:
        return None,None
    #sort by area and extract two bigest contour
    cnts.sort( key = lambda x: cv2.contourArea(x) , reverse = True)
    cnts = cnts[:2]
    
    #sort contour from left to right
    cnts.sort( key = lambda x:np.min(x, axis = 0 )[0,0] ) #sort by minimux x in each contour
    if left_or_right == 'left':
        screw_body = cnts[0]
    else:
        screw_body = cnts[-1]
    
    
    box = cv2.minAreaRect(screw_body)
    _,_,angle = box

    points = cv2.boxPoints(box)
    points = np.int0(points)
    if angle > 45:
        angle = angle - 90
    else:
        angle = angle - 0
    return angle, points
    


def centerise_side(mask, img = None):
    ys, xs = np.nonzero( mask )
    ys = np.clip( ys, 0, ys.max() - 50 )
    ys = np.clip( ys, ys.min() + 50 , mask.shape[0])
    
    #beacuse of rotate edge of belt is not flat

    idx = np.argmax(ys)
    belt_x_bottom = xs[idx]
    idx = np.argmin(ys)
    belt_x_top = xs[idx]

    belt_x = min(belt_x_bottom, belt_x_top)
    #mask[:,belt_x]= 255

    crop_roi = mask[ :, belt_x - 100 : belt_x - 50 ]
    
    ys, xs = np.nonzero( crop_roi )
    if len(ys)==0 or len(xs)==0:
        return mask,img,0
    screw_meadile = int(ys.mean())

    h,w = mask.shape[:2]
    div_y = h//2 - screw_meadile

    M = np.float32( [[1, 0, 0 ],
                    [0,1, div_y ]
                    ])

    res_img = cv2.warpAffine(img,M,(w,h))
    res_mask = cv2.warpAffine(mask,M,(w,h))

    return res_mask,res_img, div_y



def centerise_top(mask, img = None):
    cnts, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = list(cnts)
    cnts.sort( key = lambda x:cv2.contourArea(x) , reverse = True )
    if len(cnts) > 0:
        biggest_cnt = cnts[0]
        (x,y), r = cv2.minEnclosingCircle(biggest_cnt )

        h,w = mask.shape[:2]
        div_y = h//2 - y
        div_x = w//2 - x

        M = np.float32( [[1, 0, div_x ],
                        [0, 1, div_y ]
                        ])

        res_img = cv2.warpAffine(img,M,(w,h))
        res_mask = cv2.warpAffine(mask,M,(w,h))
    
    else:
        res_mask = np.copy(mask)
        res_img = np.copy(img)
        div_x, div_y = 0,0

    return res_mask,res_img, (div_x, div_y)



def side_screw_bounding_rect(mask):
    cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    cnts = list(cnts)
    cnts.sort( key = lambda x: cv2.contourArea(x) , reverse = True)
    cnts = cnts[:2]
    points = np.vstack( (cnts[0], cnts[1]) )
    
    x1,y1 = points.min(axis=0)[0]
    x2,y2 = points.max(axis=0)[0]
    
    return (x1,y1) , (x2,y2)



def find_screw_thread_top(mask , rect_roi,  min_diff = 5, max_bad_iter = 5 ):
    
    ys, xs = np.nonzero( crop_rect( mask, rect_roi ) )
    pts = np.vstack((xs,ys)).transpose()
    up_edge_pts = np.array ( pd.DataFrame(pts).groupby(0).min().reset_index().values.tolist()) #return point with min y and same x
    
    
    # mask_test = np.zeros_like(crop_rect( mask, rect_roi ))
    # mask_test[ up_edge_pts[:,1], up_edge_pts[:,0]] = 255
    # cv2.imshow('mask_test',mask_test)
    # cv2.waitKey(10)

    rezve_pts_h = []
    rezve_pts_l = []
    
    max_pt = [0, np.inf]
    min_pt = [0, np.inf * -1 ] 
    iter = 0
    find_max = True
    for i in range(1,len(up_edge_pts)):
        
        #upper y is lower in value
        if find_max:
            if up_edge_pts[i][1] <= max_pt[1]:
                max_pt = up_edge_pts[i]
                iter = 0
            else:
                iter+=1
                
            if iter> max_bad_iter:
                iter = 0
                find_max = False
                min_pt = [max_pt[0] , max_pt[1]]
                
        
        else:
            if up_edge_pts[i][1] >= min_pt[1]:
                min_pt = up_edge_pts[i]
                iter = 0
            
            else:
                iter+=1
            
            if iter > max_bad_iter:
                iter = 0
                find_max = True
                if abs(max_pt[1] - min_pt[1]) >= min_diff:
                    rezve_pts_h.append( [max_pt[0], max_pt[1]] )
                    rezve_pts_l.append( [min_pt[0], min_pt[1]] )
                    max_pt = [min_pt[0] , min_pt[1] ]
    
    rezve_pts_l, rezve_pts_h = np.array(rezve_pts_l), np.array(rezve_pts_h)          
    if len(rezve_pts_h) > 0 and len(rezve_pts_l) > 0:
        start_point = np.array(rect_roi[0])
        rezve_pts_l = rezve_pts_l + start_point
        rezve_pts_h = rezve_pts_h + start_point
        return rezve_pts_l, rezve_pts_h
    
    return [],[]

# def find_screw_thread_top(mask , rect_roi,  min_diff = 5, max_bad_iter = 5, direction='top' ):
#     ys, xs = np.nonzero( crop_rect( mask, rect_roi ) )
#     pts = np.vstack((xs,ys)).transpose()
#     if direction == 'top':
#         edge_pts = np.array( pd.DataFrame(pts).groupby(0).min().reset_index().values.tolist() ) #return point with min y and same x
    
#     points_count = len(edge_pts)
#     mean_y = int(edge_pts[ points_count//2: , 1 ].mean())

#     idx0 = -1
#     idx1 = -1
#     max_pt = [0, np.inf * -1]
#     min_pt = [0, np.inf ] 
    
#     rezve_pts_h = []
#     rezve_pts_l = []
#     what_find = ''
#     for i in range(len(edge_pts)):
         
#         if edge_pts[i][1] > mean_y and what_find=='':
#             what_find = 'low'
#             idx0 = i
        
#         elif edge_pts[i][1] < mean_y and what_find=='':
#             what_find == 'high'
#             idx0 = i
        
#         if what_find == 'high'
        
        
#         if idx0 == -1:
#             idx0 = i
#         else:
#                 idx1 = i
#         #      *        *
#         #     * *      * *
#         #  --*---*----*---*------> mean_y
#         #         *  *     *
#         #          *        *

#         if idx0!=-1 and idx1==-1:
#             if edge_pts[i][1] <= min_pt[1]:
#                 min_pt[1] = edge_pts[i][1]
#                 min_pt[0] = i


#             if edge_pts[i][1] >= max_pt[1]:
#                 max_pt[1] = edge_pts[i][1]
#                 max_pt[0] = i
        
        
#         if idx0 > 0 and idx1 > 0:
#             print(idx0, idx1, max_pt, min_pt, mean_y)
#             if abs(mean_y - max_pt[1]) > min_diff /2:
#                 print('max')
#                 rezve_pts_l.append( copy.copy(max_pt) )
#                 max_pt = [0, np.inf * -1]
            
#             elif abs(mean_y - min_pt[1]) > min_diff /2:
#                 print('min')
#                 rezve_pts_h.append( copy.copy(min_pt) )
#                 min_pt = [0, np.inf ] 
            
#             idx0 = idx1
#             idx1 = -1
    
    
#     rezve_pts_l, rezve_pts_h = np.array(rezve_pts_l), np.array(rezve_pts_h)          
#     if len(rezve_pts_h) > 0 and len(rezve_pts_l) > 0:
#         start_point = np.array(rect_roi[0])
#         rezve_pts_l = rezve_pts_l + start_point
#         rezve_pts_h = rezve_pts_h + start_point
#     return rezve_pts_l, rezve_pts_h #, mean_y + start_point[1]


    

def find_screw_thread_down(mask , rect_roi,  min_diff = 5, max_bad_iter = 5 ):
    ys, xs = np.nonzero( crop_rect( mask, rect_roi ) )
    pts = np.vstack((xs,ys)).transpose()
    up_edge_pts = np.array ( pd.DataFrame(pts).groupby(0).max().reset_index().values.tolist()) #return point with min y and same x
    
    rezve_pts_h = []
    rezve_pts_l = []
    
    max_pt = up_edge_pts[0]
    min_pt = up_edge_pts[0]
    iter = 0
    find_max = True
    for i in range(1,len(up_edge_pts)):
        
        #upper y is lower in value
        if find_max:
            if up_edge_pts[i][1] >= max_pt[1]:
                max_pt = up_edge_pts[i]
                iter = 0
            else:
                iter+=1
                
            if iter> max_bad_iter:
                iter = 0
                find_max = False
                min_pt = [max_pt[0] , max_pt[1]]
                
        
        else:
            if up_edge_pts[i][1] <= min_pt[1]:
                min_pt = up_edge_pts[i]
                iter = 0
            
            else:
                iter+=1
            
            if iter > max_bad_iter:
                iter = 0
                find_max = True
                if abs(max_pt[1] - min_pt[1]) >= min_diff:
                    rezve_pts_h.append( [max_pt[0], max_pt[1]] )
                    rezve_pts_l.append( [min_pt[0], min_pt[1]] )
                    max_pt = [min_pt[0] , min_pt[1] ]
    
    rezve_pts_l, rezve_pts_h = np.array(rezve_pts_l), np.array(rezve_pts_h)          
    if len(rezve_pts_h) > 0 and len(rezve_pts_l) > 0:
        start_point = np.array(rect_roi[0])
        rezve_pts_l = rezve_pts_l + start_point
        rezve_pts_h = rezve_pts_h + start_point
        return rezve_pts_l, rezve_pts_h
    
    return [],[]

def find_head_vertival_pts(mask, rect_roi, jump_thresh = 10, percentage=0.5, side='bottom', from_belt=False):
    crop_mask = crop_rect( mask, rect_roi ) 
    ys, xs = np.nonzero( crop_mask )
    pts = np.vstack((xs,ys)).transpose()
    start_point = np.array(rect_roi[0])

    if len(pts)>50:
        right_pts = np.array ( pd.DataFrame(pts).groupby(1).max().reset_index().values.tolist()) #return point with max x and same y
        right_pts = np.array([right_pts[:,1],right_pts[:,0]]).transpose()
        right_pts = right_pts + start_point

        points_cout = len(right_pts)
        start_top_idx1 = 0
        step = 3
        for i in range(points_cout//2, step, -1):
            if abs( right_pts[i , 0] - right_pts[i-step:i, 0 ].mean()  ) > 15:
                start_top_idx1 = i

        start_top_idx2 = 0
        
        for i in range(points_cout//2, points_cout-step):
            if abs( right_pts[i , 0] - right_pts[i:i+step, 0 ].mean()  ) > 15:
               start_top_idx2 = i

        
        len_top = start_top_idx2 - start_top_idx1
        top_head_pts = right_pts[ int(start_top_idx1 + len_top * (1-percentage)/2) : int(start_top_idx2 - len_top * (1-percentage)/2)]

        #----------------------------------------------------------------------------
        if not from_belt:
            if side == 'top':
                _pts_ = np.array ( pd.DataFrame(pts).groupby(0).min().reset_index().values.tolist()) 
                _pts_ = start_point + _pts_

            else:
                _pts_ = np.array ( pd.DataFrame(pts).groupby(0).max().reset_index().values.tolist()) 
                _pts_ = start_point + _pts_

            points_cout = len(_pts_)
            h_pt2 = _pts_[0]
            step = 3
            for i in range(points_cout-10, step, -1):
                if abs( _pts_[i , 1] - _pts_[i-step:i, 1 ].mean()  ) > jump_thresh:
                    h_pt2 = _pts_[i]
                    break
        
        else:
            h,w = crop_mask.shape
            for i in range(w):
                count_nonzero = 0
                if side == 'top':
                    count_nonzero = np.count_nonzero( crop_mask[:10, i] )
                        
                elif side == 'bottom':
                    count_nonzero = np.count_nonzero( crop_mask[-10:h, i] )
                
                if count_nonzero<7:
                    h_pt2 = [ i + start_point[0]]
                    break

        bottom_head_pts = np.copy(top_head_pts)
        bottom_head_pts[:,0] = h_pt2[0]  
        return bottom_head_pts, top_head_pts
    
    return [],[]


def find_vertical_edges(mask , rect_roi ):
    ys, xs = np.nonzero( crop_rect( mask, rect_roi ) )
    pts = np.vstack((xs,ys)).transpose()
    if len(pts)>50:
        right_pts = np.array ( pd.DataFrame(pts).groupby(1).max().reset_index().values.tolist()) #return point with max x and same y
        right_pts = np.array([right_pts[:,1],right_pts[:,0]]).transpose()

        left_pts = np.array ( pd.DataFrame(pts).groupby(1).min().reset_index().values.tolist()) #return point with max x and same y
        left_pts = np.array([left_pts[:,1],left_pts[:,0]]).transpose()
        
        start_point = np.array(rect_roi[0])
        
        right_pts = right_pts + start_point
        left_pts = left_pts + start_point
        return left_pts, right_pts
    
    return [],[]



def find_horizental_edges(mask, rect_roi):
    ys, xs = np.nonzero( crop_rect( mask, rect_roi ) )
    pts = np.vstack((xs,ys)).transpose()
    if len(pts)>50:
        up_edge_pts = np.array ( pd.DataFrame(pts).groupby(0).min().reset_index().values.tolist()) #return point with min y and same x
        down_edge_pts = np.array ( pd.DataFrame(pts).groupby(0).max().reset_index().values.tolist()) #return point with min y and same x
        
        
        start_point = np.array(rect_roi[0])
        up_edge_pts = up_edge_pts + start_point
        down_edge_pts = down_edge_pts + start_point
        return up_edge_pts, down_edge_pts
    return [], []



def get_bigest_area(mask, rect_roi):
    crop_mask = crop_rect( mask, rect_roi )
    cnts,_ = cv2.findContours(crop_mask , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = list(cnts)
    cnts.sort( key = lambda x:cv2.contourArea(x) , reverse=True)

    cnt_area = cv2.contourArea( cnts[0] ) / 10
    # crop_area = abs((rect_roi[0][0] - rect_roi[1][0]) * (rect_roi[0][1] - rect_roi[1][1]))
    # res = cnt_area / crop_area
    # res = np.round(res, 3)
    return int(cnt_area)


def draw_vertical_point(img, pts_group, color, thicknes=4, close = False):
    for pts in pts_group:
        for i in range(-thicknes//2, thicknes//2):
            img[ pts[:,1], pts[:,0] + i] = color

    return img

def draw_horizental_point(img, pts_group, color, thicknes=4):
    for pts in pts_group:
        for i in range(-thicknes//2, thicknes//2):
            img[ pts[:,1] + i , pts[:,0]] = color
    return img


def draw_points(img, pts, color, radius=4):
    for pt in pts:
        cv2.circle(img, tuple(pt), radius, color, thickness=-1)
    return img


def draw_head_diameter(img, pt1, pt2, color, thickness=3, line_lenght=10):

    x1,y1 = pt1
    img = cv2.line( img, (x1-line_lenght,y1) ,   (x1+line_lenght, y1), color, thickness=thickness  )   
    
    x2,y2 = pt2
    img = cv2.line( img, (x2-line_lenght,y2) ,   (x2+line_lenght, y2), color, thickness=thickness  )

    img = cv2.line( img, pt1, pt2, color, thickness)
    return img


def draw_cnt( img, cnt, color, thickness=5):
    if len(cnt)>0:
        return cv2.drawContours(img, [cnt], 0, color, thickness=thickness)
    else:
        return img



def poly_fit_image(cnt, border=50, draw=True ):
    if len(cnt)>0:
        cnt = np.copy(cnt)
        min_x, min_y = cnt.min(axis=0)[0]
        max_x, max_y = cnt.max(axis=0)[0]

        w = max_x - min_x + border * 2
        h = max_y - min_y + border * 2

        cnt[:,0,0] = cnt[:,0,0] - min_x + border
        cnt[:,0,1] = cnt[:,0,1] - min_y + border
        
        mask = np.zeros((h,w), dtype=np.uint8)
        if draw:
            cv2.drawContours( mask, [cnt], 0, 255, thickness=-1)
        return cnt,  mask
    return [], 0


#@time_measure
def diameters_measurment(mask, cnt, angles):
    M = cv2.moments(cnt)
    center = int(M['m10']/M['m00']) , int(M['m01']/M['m00'])
    r=1000
    corners_dist = []
    for angle in angles:
        line_mask = np.zeros_like(mask)
        pt1, pt2 = mathTools.angle2line(angle, center,  r*1.5)

        cv2.line(line_mask, pt1, pt2, 255,2)
        line_mask = cv2.bitwise_and( line_mask, line_mask, mask=mask)
        corners_dist.append(np.count_nonzero(line_mask))

        # res_img = np.zeros( mask.shape + (3,), dtype=np.uint8)
        # res_img[:,:,0] = mask
        # res_img[:,:,1] = line_mask
        # cv2.imshow('line_mask', res_img)
        # cv2.waitKey(0)

    return np.array(corners_dist)


#@time_measure
def hexagonal_measument(cnt):
    
    cnt, poly_img = poly_fit_image(cnt)
    rect = cv2.minAreaRect(cnt)
    _,_, angle = rect
    if angle > 45:
        angle = angle - 90

    
    poly_img = rotate_image(poly_img, angle)
    diameters1 = diameters_measurment(poly_img, cnt, range(30,180,60))
    diameters2 = diameters_measurment(poly_img, cnt, range(0,180,60))

    if diameters1.mean() < diameters2.mean():
        corner_distance = diameters2
        edge_distance = diameters1
    else:
        corner_distance = diameters1
        edge_distance = diameters2
    
    return corner_distance, edge_distance

#@time_measure
def circel_measument(cnt):
    cnt, poly_img = poly_fit_image(cnt)

    diameters = diameters_measurment(poly_img, cnt, range(0,180,5))
    return diameters


def get_top_region_cnt(img, thresh, thresh_inv, roi_mask):
    thresh_mask = threshould(img, thresh, mask_roi=None, inv= thresh_inv )
    thresh_mask = cv2.bitwise_and( thresh_mask, thresh_mask, mask= roi_mask )
    thresh_mask = filter_noise_area(thresh_mask, 20)

    cnts, hs = cv2.findContours(thresh_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnts = list(cnts)
    cnts.sort( key = lambda x:cv2.contourArea(x) , reverse = True )
        
    biggest_cnt = cnts[0]
    return biggest_cnt
        
#@time_measure
def conture_moving_avg(cnt, w= 10, iter=1):
    xs = cnt[:,0,0]
    ys = cnt[:,0,1]
    for _ in range(iter):
        xs = np.convolve(xs, np.ones(w), 'valid') / w
        ys = np.convolve(ys, np.ones(w), 'valid') / w
    xs = np.expand_dims(xs, axis=-1)
    ys = np.expand_dims(ys, axis=-1)
    res_cnt = np.hstack((xs,ys))
    res_cnt = res_cnt.reshape((-1,1,2)).astype(np.int32)
    return res_cnt

def find_edge_crack(mask, thresh_area, filter_w=10 ):
    cnts,_ = cv2.findContours(mask , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = list(cnts)
    if len(cnts) > 0:
        cnt = cnts[0]        
        #--------------------------
        cnt = conture_moving_avg(cnt, w = filter_w, iter=1)
        #res_cnt = conture_moving_avg(cnt, w = 100, iter=1)
        approx_cnt = cv2.convexHull(cnt)
        #--------------------------
        crack_mask = np.zeros_like(mask)
        crack_mask = cv2.drawContours( crack_mask, [approx_cnt], 0, 255 , thickness=-1)
        crack_mask = cv2.drawContours( crack_mask, [cnt], 0, 0 , thickness=-1)
        #--------------------------
        crack_mask = cv2.erode(crack_mask, np.ones((3,3)), iterations=1)
        crack_mask = cv2.dilate(crack_mask, np.ones((3,3)), iterations=1)
        #--------------------------
        crack_cnts,_ = cv2.findContours( crack_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        crack_cnts = list(filter( lambda x:cv2.contourArea(x) > thresh_area, crack_cnts ))
        #crack_areas.sort( key = lambda x:cv2.contourArea(x), reverse=True)
        crack_areas = np.array(list( map( lambda x:cv2.contourArea(x), crack_cnts ) ))
        return crack_cnts, crack_areas
    return [], []





def centerise_measurment(masks):
    res_cnts = []
    res_centers = []
    for mask in masks:
        cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(cnts) == 0:
            continue
        cnt = cnts[0]
        M = cv2.moments(cnt)
        res_centers.append( (int(M['m10']/M['m00']) , int(M['m01']/M['m00']) ) )
        res_cnts.append(cnt)
    
    dist = -1
    if len(res_centers)==2:
        pt1 =  res_centers[0]
        pt2 =  res_centers[1]
        dist = ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 )**0.5
    return res_cnts, res_centers, np.round(dist,1)


def random_light(img,low=-20,high=20):
    light = np.random.randint(low, high)
    res = np.copy(img).astype(np.int32)
    res = res + light
    res = np.clip(res, 0, 255)
    return res.astype(np.uint8)



if __name__ == '__main__':
    
    img = cv2.imread('sample images/top\Image__2047-01-06__12-02-12.bmp')
    thresh_mask = threshould(img, 150, mask_roi=None, inv=False)
    thresh_mask = filter_noise_area(thresh_mask, 20)


    cracks = find_edge_crack( thresh_mask, thresh_area=200, filter_w=20 )

    
    #cv2.drawContours( img, [cnt], 0, (255,0,0) , thickness=5)
    cv2.drawContours( img, cracks, -1, (0,0,255) , thickness=-1)
    cv2.imshow('img', cv2.resize( img, None, fx=0.75, fy=0.75))
    #cv2.imshow('thresh_mask', cv2.resize( thresh_mask, None, fx=0.75, fy=0.75))
    cv2.waitKey(0)
    # regions = []
    
    # circel_roi = [[860,585], 385 ]
    # thresh_mask = threshould(img, 200, mask_roi=None, inv=False)
    # roi_mask = circels2mask( thresh_mask.shape[0:2], [circel_roi] )
    # thresh_mask = cv2.bitwise_and( thresh_mask, thresh_mask, mask= roi_mask )
    # thresh_mask = filter_noise_area(thresh_mask, 20)
    
    # thresh_mask, img, div_pt = centerise_top(thresh_mask, img )
    
    # #-------------------------------------------------------------------------------------
    # (cx, cy) , r = circel_roi
    # div_x, div_y = div_pt
    # circel_roi = [ [int(cx + div_x) , int(cy + div_y) ] , int(r)]

    # regoins_parms = [ 
    #     { 'thresh':190 , 'thresh_inv' : False }, 
    #     { 'thresh':200 , 'thresh_inv' : True  }, 
    # ]

    
    # regions_roi = [ 
    #     {'type':'circel', 'value':circel_roi},
    #     None,
    # ]
    # regions = [ 

    # ]
    # for i in range(len(regoins_parms)):
        
    #     thresh_mask = threshould(img, regoins_parms[i]['thresh'], mask_roi=None, inv=regoins_parms[i]['thresh_inv'])
    #     roi_mask = shape2mask(thresh_mask.shape[0:2], regions_roi[i]['value'], regions_roi[i]['type'])
    #     thresh_mask = cv2.bitwise_and( thresh_mask, thresh_mask, mask= roi_mask )
    #     thresh_mask = filter_noise_area(thresh_mask, 20)

    #     cnts, hs = cv2.findContours(thresh_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #     cnts = list(cnts)
    #     cnts.sort( key = lambda x:cv2.contourArea(x) , reverse = True )
        
    #     biggest_cnt = cnts[0]
    #     regions.append( biggest_cnt )
        
    #     if i < len(regions_roi) - 1:
    #         if regions_roi[i+1] == None:
    #             regions_roi[i+1] = { 'type':'poly', 'value':biggest_cnt } 

        
    #-------------------------------------------------------------------------------------
    # pts = regions[1]
    # for i in range(20, len(pts)-20):
    #     test_img = np.copy(img)

    #     group1 = pts[i-20:i]
    #     group2 = pts[i:i+20]

    #     group1 = group1.mean(axis=0)[0].astype(np.int32)
    #     group2 = group2.mean(axis=0)[0].astype(np.int32)


    #     m = (group1[1] - group2[1]) / (group1[0] - group2[0] + 1e-5) 
    #     if m == 0:
    #         continue
    #     m = -1/m
    #     c = m * (-pts[i][0][0]) + pts[i][0][1]



    #     pt1 = (0, int(m*0+c))
    #     pt2 = (2000, int(m*2000+c))

    #     cv2.line( test_img, tuple(pt1), tuple(pt2), (0,0,255), thickness=3 )
    #     cv2.circle(test_img, tuple(pts[i][0]), 5, (255,0,0), thickness=-1)
    #     cv2.imshow('test_img', cv2.resize(test_img, None, fx=0.5, fy=0.5))
    #     cv2.waitKey(0)
    # poly_cnt = regions[1]   
    # cd,ed = hexagonal_measument(poly_cnt)     
    # dd = circel_measument(regions[0])
    # a = True
    #cv2.imshow('poly_img', cv2.resize(poly_img, None, fx=0.5, fy=0.5))
    #cv2.waitKey(0)

    #-------------------------------------------------------------------------------------

    

    # cnts, hs = cv2.findContours(thresh_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # hs = hs[0]
    # cnts = list(cnts)
    # res_cnts = []
    # for i in range(2):
    #     idxs = np.arange( 0, len(cnts) ).tolist()
    #     idxs.sort( key = lambda x:cv2.contourArea(cnts[x]) , reverse = True )
    #     biggest_cnt_idx = idxs[0]
    #     res_cnts.append( cnts[ biggest_cnt_idx ] )
    #     #-----------------------------------------
    #     idxs = list( filter( lambda i:hs[i][-1] == biggest_cnt_idx , idxs ) )
    #     if len(idxs) == 0:
    #         break
    #     cnts = np.array(cnts)[idxs].tolist()
    #     hs = hs[idxs]
    # cv2.drawContours( img, regions, -1, (255,0,0) , thickness=5)
    # for i in range(len(regions)):
    #     for point in regions[i]:
    #         cv2.circle( img, tuple(point[0]), 3, (0,0,255), thickness=-1 )
    
    cv2.imshow('img', cv2.resize( img, None, fx=0.75, fy=0.75))
    #cv2.imshow('thresh_mask', cv2.resize( thresh_mask, None, fx=0.75, fy=0.75))
    cv2.waitKey(0)
    #---------------------------------------------------------------------------------------------
    # img = cv2.imread('sample images/New folder/31x_1_2.png')
    # print('________________________________________________________________________')
    
    # rect =[ [20, 60] , [1360, 480] ]
    # thresh = 50
    
    # mask_roi = rects2mask( img.shape[:2] , [rect] )    
    # thresh_mask = threshould(img, thresh, mask_roi=mask_roi, inv=True)
    # cv2.imshow( 'thresh_mask_befor_rateton', thresh_mask)
    
    
    # #--------------------------------------------------------
    # mask_unbelt, belt_pos = remove_belt( thresh_mask, rect )
    # angle, box = correct_rotation_angle(mask_unbelt)
    # thresh_mask = rotate_image(thresh_mask,  angle   )
    # img = rotate_image(img,  angle   )
    # # thresh_mask = rotate_image(thresh_mask,  angle   )

    

    # cv2.imshow('img', img)
    # cv2.imshow('thresh_mask', thresh_mask)
    # thresh_mask, img, _ = centerise_side( thresh_mask, img )
    

    
    


    
    # cv2.imshow('res_img', img)
    # cv2.imshow('res_thresh_mask', thresh_mask)
    # cv2.waitKey(0)
    #--------------------------------------------------------
    # total_lenght_roi = [ [20, 220] , [1360, 290] ]
    # left_pts, right_pts = find_horizental_edges(thresh_mask, total_lenght_roi)
    
    # img[ left_pts[:,1] , left_pts[:,0] ] = [0,0,255]
    # img[ right_pts[:,1] , right_pts[:,0] ] = [0,0,255]

    # img = draw_vertical_point(img, [left_pts, right_pts] , (0,0,255), 2 )
    #--------------------------------------------------------
    # radiuse_body_roi = [ [660, 130] , [910, 380] ]
    
    # up_pts, down_pts = find_vertical_edges(thresh_mask, radiuse_body_roi)
    
    # img = draw_horizental_point(img, [up_pts, down_pts] , (0,255,0), 2 )
    
    
    #--------------------------------------------------------
    # rezve_rect_roi = [ [100, 60] , [550, 400] ]
    # male_thread_l, male_thread_h = find_screw_thread( thresh_mask, rezve_rect_roi,  min_diff=5)
    
    # img = draw_points(img, male_thread_h, (230,200,150), 3)
    # img = draw_points(img, male_thread_l, (0,50,200), 3)
    #--------------------------------------------------------
    # head_roi2 = [[1120,100],[1320,450]]
    # mask2 = np.copy( thresh_mask )
    # bottom_head_pts, top_head_pts = find_head_vertival_pts(mask2, head_roi2, jump_thresh=10)
    # img = draw_vertical_point(img, [top_head_pts, bottom_head_pts], (0,100,200), 3)
    # # up_edge_pts = np.array( pd.Dat
    # #for i in range()
    
    
        
        
    
    
    
    # cv2.imshow( 'thresh_mask', thresh_mask)
    # cv2.imshow( 'img', img)
    # cv2.waitKey(0)
    # pass
    
    #------------
    
    # mask_img = cv2.imread('mask.jpg', 0)
    # img = cv2.imread( 'img.jpg' , 0 )
    # # cv2.imshow('m',mask_area)
    # # cv2.imwrite('mask.jpg', mask_area)
    # # cv2.waitKey(30)
    # mask = adp_threshould( img , 11, 11 , None )
    # #mask = filter_noise_area(mask , noise_filter )
    
    
    
    # #img = Utils.mask_viewer(img, mask)
    
    # cnts,_ = cv2.findContours(mask , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts.sort( key = lambda x:cv2.contourArea(x) , reverse=True)
    
    # hull=cv2.convexHull (cnts[0])
    # cv2.drawContours (img , [hull] ,0, (0,0,255) , thickness=5)
    
    # cv2.waitKey(0)
    # # cv2.imshow('mask_area', mask_area )
    
    
    
    # img = cv2.imread('sample images/test1.jpg')
    
    # mask = threshould(img, 50, None, True)
    # mask_unbelt, belt_pos = remove_belt( mask )
    
    # angle = correct_rotation_angle(mask_unbelt)
    
    # img = rotate_image(img,  angle  )
    # rotated_mask = rotate_image(mask_unbelt,  angle )
    
    
    
    # pt1,pt2 = side_screw_bounding_rect(rotated_mask)
    
    # img = cv2.rectangle( img , pt1, pt2, (255,0,0))
    # #img = cv2.drawContours(img, [rect_cnt], 0, (0,0,255), thickness=5)
    
    
    
    # cv2.imshow('mask1', mask)
    # cv2.imshow('res_mask', mask_unbelt)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # pass
    
    
