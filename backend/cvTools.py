from turtle import left
import cv2
from cv2 import circle
from cv2 import contourArea
import numpy as np
import pandas as pd
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








def remove_belt(mask, rect_roi, thresh=0.6 , left_margin = 30 , right_margin = 10):
    crop_mask = crop_rect( mask, rect_roi ) 
    h,w = crop_mask.shape
    cols_sum = np.sum(crop_mask, axis = 0) / h / 255
    idxs = np.argwhere( cols_sum > thresh )
    
    start_idx = idxs.min() - left_margin
    end_idx = idxs.max() + right_margin
    
    start_idx += rect_roi[0][0]
    end_idx += rect_roi[0][0]
    
    res_mask = np.copy( mask )
    res_mask[:,start_idx:end_idx] = 0

    return res_mask, (start_idx , end_idx)




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
        if len(rect)==2:
            pt1, pt2 = rect
            if len(pt1) == 2 and len(pt2) == 2:
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

def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


def correct_rotation_angle(mask , left_or_right='left'):
    
    cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
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
    
    

def side_screw_bounding_rect(mask):
    cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    
    cnts.sort( key = lambda x: cv2.contourArea(x) , reverse = True)
    cnts = cnts[:2]
    points = np.vstack( (cnts[0], cnts[1]) )
    
    x1,y1 = points.min(axis=0)[0]
    x2,y2 = points.max(axis=0)[0]
    
    return (x1,y1) , (x2,y2)



def find_screw_thread(mask , rect_roi,  min_diff = 5, max_bad_iter = 5 ):
    ys, xs = np.nonzero( crop_rect( mask, rect_roi ) )
    pts = np.vstack((xs,ys)).transpose()
    up_edge_pts = np.array ( pd.DataFrame(pts).groupby(0).min().reset_index().values.tolist()) #return point with min y and same x
    
    rezve_pts_h = []
    rezve_pts_l = []
    
    max_pt = up_edge_pts[0]
    min_pt = up_edge_pts[0]
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
    
    start_point = np.array(rect_roi[0])
    rezve_pts_l = rezve_pts_l + start_point
    rezve_pts_h = rezve_pts_h + start_point
    return rezve_pts_l, rezve_pts_h




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

def draw_vertical_point(img, pts_group, color, thicknes=4):
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






def preprocessing_img_json( img, json, direction):
    thresh = json.get_thresh('1_{}'.format( direction ), None )
    noise_filter = json.get_noise_filter( '1_{}'.format( direction ), None  )
    rect_roi_main = json.get_rect_roi( '1_{}'.format( direction ), None )
    inv_state = json.get_thresh_inv('1_{}'.format( direction ), None )
    
    mask_roi = rects2mask(img.shape[:2], [rect_roi_main])
    thresh_img = threshould(img, thresh, mask_roi, inv_state)
    thresh_img = filter_noise_area(thresh_img, noise_filter)
    #--------------------------------------------------------------------------------------
    #correct rotation
    #--------------------------------------------------------------------------------------
    mask_unbelt, _ = remove_belt( thresh_img,rect_roi_main, thresh=0.7 )
    angle, _ = correct_rotation_angle(mask_unbelt)
    thresh_img = rotate_image(thresh_img,  angle   )
    img = rotate_image(img,  angle   )

    return img, thresh_img, angle
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    from matplotlib import pyplot as plt
    
    
    img = cv2.imread('sample images/New folder/31x_1_3.png')
    print('________________________________________________________________________')
    
    rect =[ [20, 60] , [1360, 480] ]
    thresh = 50
    
    mask_roi = rects2mask( img.shape[:2] , [rect] )    
    thresh_mask = threshould(img, thresh, mask_roi=mask_roi, inv=True)
    cv2.imshow( 'thresh_mask_befor_rateton', thresh_mask)
    
    
    #--------------------------------------------------------
    mask_unbelt, belt_pos = remove_belt( thresh_mask )
    angle, box = correct_rotation_angle(mask_unbelt)
    thresh_mask = rotate_image(thresh_mask,  angle   )
    img = rotate_image(img,  angle   )
    
    
    #--------------------------------------------------------
    total_lenght_roi = [ [20, 220] , [1360, 290] ]
    left_pts, right_pts = find_horizental_edges(thresh_mask, total_lenght_roi)
    
    img[ left_pts[:,1] , left_pts[:,0] ] = [0,0,255]
    img[ right_pts[:,1] , right_pts[:,0] ] = [0,0,255]

    img = draw_vertical_point(img, [left_pts, right_pts] , (0,0,255), 2 )
    #--------------------------------------------------------
    radiuse_body_roi = [ [660, 130] , [910, 380] ]
    
    up_pts, down_pts = find_vertical_edges(thresh_mask, radiuse_body_roi)
    
    img = draw_horizental_point(img, [up_pts, down_pts] , (0,255,0), 2 )
    
    
    #--------------------------------------------------------
    rezve_rect_roi = [ [100, 60] , [550, 400] ]
    male_thread_l, male_thread_h = find_screw_thread( thresh_mask, rezve_rect_roi,  min_diff=5)
    
    img = draw_points(img, male_thread_h, (230,200,150), 3)
    img = draw_points(img, male_thread_l, (0,50,200), 3)
    #--------------------------------------------------------
    
    
    
    
        
        
    
    
    
    cv2.imshow( 'thresh_mask', thresh_mask)
    cv2.imshow( 'img', img)
    cv2.waitKey(0)
    pass
    
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
    
    