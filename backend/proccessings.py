from ast import Not
from cv2 import cvtColor
from backend import mathTools, cvTools, Utils,cvToolsCython
from scipy.signal import convolve2d
import cv2
import numpy as np
import time

def set_dict(name, value_min, value_avg , value_max, limits):
    res_dict = {'name': name,
                'limit_min': limits['min'],
                'limit_max': limits['max'],
                'min': value_min,
                'max': value_max,
                'avg': value_avg,
                 }
    return res_dict


def get_general_masks(img, json, page_name, main_roi_mask=None):
    res = {}
    for subpage_name in json.get_subpages(page_name):
        if subpage_name == 'none':
            continue 

        thresh_min = json.get_thresh_min(page_name, subpage_name)
        thresh_max = json.get_thresh_max(page_name, subpage_name)
        noise_filter = json.get_noise_filter( page_name, subpage_name )
        circels_roi = json.get_circels_roi(page_name, subpage_name)
    
        mask_roi = cvTools.circels2mask(img.shape[:2], circels_roi)
        

        thresh_img = cvTools.threshould_minmax(img, thresh_min, thresh_max, mask_roi)


        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        
        if main_roi_mask is not None:
            thresh_img = cv2.bitwise_and(thresh_img, main_roi_mask)
        
        res[subpage_name] = np.copy( thresh_img )
    return res



def preprocessing_sensor_detection(img , thresh_min,thresh_max,area_thresh,rect_roi,draw = None):
    
    roi = img[rect_roi[0][1]:rect_roi[1][1],
              rect_roi[0][0]:rect_roi[1][0]]
    if not len(roi):
        return False,-1, img


    thresh_img = cvTools.threshould_minmax(roi, thresh_min, thresh_max)

    area = np.count_nonzero(thresh_img)

    if draw is not None:
        draw = Utils.mask_viewer(roi.copy(), thresh_img)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        img[rect_roi[0][1]:rect_roi[1][1],\
              rect_roi[0][0]:rect_roi[1][0]] = draw
    
    cross_flag = False
    if area > area_thresh:
        cross_flag = True

    return cross_flag, area, img



def preprocessing_1_top_img( img, json,draw = None, centerise=True):
    tt1 = time.time()
    page_name = '1_top'
    subpage_name = None
    algo_name = json.get_multi_option( page_name, subpage_name, 'algo' )
    rect_roi_main = json.get_rect_roi( '1_top', None )
    mask_roi = cvTools.rects2mask(img.shape[:2], [rect_roi_main])
    
    if algo_name == 'thresh_algo':
        thresh_min = json.get_thresh_min(page_name, subpage_name)
        thresh_max = json.get_thresh_max(page_name, subpage_name)
        noise_filter = json.get_noise_filter( page_name, subpage_name )
        belt_margin = json.get_numerical_parm(page_name, subpage_name, 'belt_edge_margin')
        

        thresh_img = cvTools.threshould_minmax(img, thresh_min, thresh_max, mask_roi)

        thresh_img = cv2.morphologyEx(thresh_img, cv2.MORPH_OPEN,
                           (2,2), iterations=1)
        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)



    elif algo_name == 'edge_algo':

        edge_thresh = json.get_numerical_parm(page_name, subpage_name, 'edge_thresh')
        belt_margin = json.get_numerical_parm(page_name, subpage_name, 'belt_edge_margin')

        gray = None
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()
        thresh_img = cvToolsCython.derivative_threshould(gray.astype(np.int32), edge_thresh)
        thresh_img = cv2.bitwise_and(thresh_img, thresh_img, mask= mask_roi)
        
        # if belt_margin >0:
        #     l_belt = json.get_numerical_parm('0_top', None, 'lbelt')
        #     r_belt = json.get_numerical_parm('0_top', None, 'rbelt')

        #     pts_l = cvToolsCython.find_belt_edge_neighbor_point(thresh_img , l_belt ,np.array(rect_roi_main,dtype='int32'),belt_margin,kernel_w=5,kernel_h=5,thresh=7 )
        #     pts_r = cvToolsCython.find_belt_edge_neighbor_point(thresh_img , r_belt ,np.array(rect_roi_main,dtype='int32'),belt_margin,kernel_w=5,kernel_h=5,thresh=7 )
            

        #     thresh_img=cvToolsCython.remove_belt_edge_line(thresh_img,pts_l)
        #     thresh_img=cvToolsCython.remove_belt_edge_line(thresh_img,pts_r)
    pts_l = None
    pts_r = None
    if belt_margin >0:
        l_belt = json.get_numerical_parm('0_top', None, 'lbelt')
        r_belt = json.get_numerical_parm('0_top', None, 'rbelt')
        

        left_top_pt1, left_bottom_pt1 = cvTools.find_screw_edge_point(thresh_img, l_belt-belt_margin)
        left_top_pt2, left_bottom_pt2 = cvTools.find_screw_edge_point(thresh_img, l_belt+belt_margin)
        right_top_pt1, right_bottom_pt1 = cvTools.find_screw_edge_point(thresh_img, r_belt-belt_margin)
        right_top_pt2, right_bottom_pt2 = cvTools.find_screw_edge_point(thresh_img, r_belt+belt_margin)
        
        if left_top_pt1 and left_top_pt2 and right_top_pt1 and right_top_pt2:
            pts_l = [ [left_top_pt1,left_top_pt2], [left_bottom_pt1, left_bottom_pt2]]
            pts_r = [ [right_top_pt1, right_top_pt2], [right_bottom_pt1, right_bottom_pt2]]

            pts_l = np.array(pts_l).astype(np.int32)
            pts_r = np.array(pts_r).astype(np.int32)

            thresh_img=cvToolsCython.remove_belt_edge_line(thresh_img,pts_l)
            thresh_img=cvToolsCython.remove_belt_edge_line(thresh_img,pts_r)
        
        # cv2.imshow('a', thresh_img)
        # cv2.waitKey(20)

    d_parm1 = json.get_numerical_parm(page_name, subpage_name, 'd_parm1')
    e_parm2 = json.get_numerical_parm(page_name, subpage_name, 'e_parm2')
    d_parm3 = json.get_numerical_parm(page_name, subpage_name, 'd_parm3')
    e_parm4 = json.get_numerical_parm(page_name, subpage_name, 'e_parm4')

    t1 = time.time()
    thresh_img = cv2.dilate(thresh_img , np.ones((3,3)),iterations = d_parm1)
    thresh_img = cv2.erode(thresh_img , np.ones((3,3)),iterations = e_parm2)
    thresh_img = cv2.dilate(thresh_img , np.ones((3,3)),iterations = d_parm3)
    thresh_img = cv2.erode(thresh_img , np.ones((3,3)),iterations = e_parm4)
    t2=time.time()-t1
    
    

    #--------------------------------------------------------------------------------------
    #correct rotation
    #--------------------------------------------------------------------------------------
    if centerise:
        if draw is not None:
            _, draw, div_pt = cvTools.centerise_top(thresh_img, draw )

        thresh_img, img, div_pt = cvTools.centerise_top(thresh_img, img )

        if belt_margin >0:            
            if pts_l is not None:
                pts_l[:,:,0] =  pts_l[:,:,0] + div_pt[0]
                pts_l[:,:,1] =  pts_l[:,:,1] + div_pt[1]
            if pts_r is not None:
                pts_r[:,:,0] =  pts_r[:,:,0] + div_pt[0]
                pts_r[:,:,1] =  pts_r[:,:,1] + div_pt[1]

    thresh_img = cvTools.mask_bigest_contour(thresh_img)
    if draw is not None:
        draw = Utils.mask_viewer(draw, thresh_img)
        if belt_margin >0 and pts_r is not None and pts_l is not None:
            for i in range(2):
                for j in range(2):
                    cv2.circle(draw, tuple(pts_l[i,j]), 5, color=(0,255,0), thickness=-1)
                    cv2.circle(draw, tuple(pts_r[i,j]), 5, color=(0,255,0), thickness=-1)


    t2 = time.time()-tt1
    print('preprocessing_1_top_img',t2)


    return img, thresh_img, draw

#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________
#
#
    



def preprocessing_0_top_img( img, json, draw=None):
    page_name = '0_top'
    subpage_name = None

    lbelt = json.get_numerical_parm(page_name, subpage_name, 'lbelt')
    rbelt = json.get_numerical_parm(page_name, subpage_name, 'rbelt')
    angle = json.get_numerical_parm(page_name, subpage_name, 'angle')
    detection_type  = json.get_checkbox(page_name,subpage_name,'detection_type')

    img = cvTools.rotate_image(img.copy(),angle=angle)
 


    rect_roi = json.get_rect_roi( '0_top', None )
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    if detection_type:
        if len(rect_roi) == 2:
            if len(rect_roi[0]) ==2 and len(rect_roi[1]) ==2:
                y1 = rect_roi[0][1]
                y2 = rect_roi[1][1]

                x1 = rect_roi[0][0]
                x2 = rect_roi[1][0]

                x_mid = (x2 - x1) //2 + x1

                crop_belt_left = gray[y1:y2 , x1:x_mid]
                crop_belt_left = crop_belt_left.astype(np.int32)

                crop_belt_right = gray[y1:y2 , x_mid:x2]
                crop_belt_right = crop_belt_right.astype(np.int32)


                left_ds = crop_belt_left[:,:-1] - crop_belt_left[:,1:]
                #left_ds = np.mean(left_ds, axis=0)
                if len(left_ds):
                    lbelt = int(np.argmax(left_ds, axis=1).mean())
                    lbelt = lbelt + x1
                    json.set_numerical_parm(page_name, subpage_name, 'lbelt', lbelt)

                right_ds = (crop_belt_right[:,:-1] - crop_belt_right[:,1:]) * -1
                if len(right_ds):
                    rbelt = int(np.argmax(right_ds, axis=1).mean())
                    rbelt = rbelt + x_mid
                    json.set_numerical_parm(page_name, subpage_name, 'rbelt', rbelt)


            

    
    if draw is not None:
        draw = cvTools.rotate_image(draw,angle=angle)
        draw[:,lbelt-1:lbelt+2] = [0,0,255]
        draw[:,rbelt-1:rbelt+2] = [0,255,0]
       

    else:
        draw = np.copy( img )

    return img ,draw



    #--------------------------------------------------------------------------------------
    #correct rotation
    #--------------------------------------------------------------------------------------
    thresh_img, img, div_pt = cvTools.centerise_top(thresh_img, img )
    thresh_img = cvTools.mask_bigest_contour(thresh_img)


    return img, thresh_img, div_pt
#
#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________


def preprocessing_side_img( img, json, rotation=True, centerise=True):
    thresh = json.get_thresh('1_side', None )
    noise_filter = json.get_noise_filter('1_side', None  )
    rect_roi_main = json.get_rect_roi( '1_side', None )
    inv_state = json.get_thresh_inv('1_side', None )
    
    img = cvTools.preprocess(img)

    mask_roi = cvTools.rects2mask(img.shape[:2], [rect_roi_main])
    thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
    thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
    #--------------------------------------------------------------------------------------
    #correct rotation
    #--------------------------------------------------------------------------------------
    angle = None

    if rotation:    
        mask_unbelt, _ = cvTools.remove_belt( thresh_img,rect_roi_main, thresh=0.7 )
        angle, _ = cvTools.correct_rotation_angle(mask_unbelt)
        if angle==None:
            return img,thresh_img,None

        thresh_img = cvTools.rotate_image(thresh_img,  angle   )
        img = cvTools.rotate_image(img,  angle   )

    if centerise:
        thresh_img, img, _ = cvTools.centerise_side( thresh_img, img )

    return img, thresh_img, angle



def proccessing_body_lenght( img, mask, jsondb, draw=None, calib_value=1):
    page_name = '2_side'
    subpage_name = None
    
    rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name)
    limits = jsondb.get_limit('lenght', page_name, subpage_name)

    res_dict = set_dict('body_length', -2, -2, -2, limits )        
    if Utils.is_rect(rect_roi_2):
        left_pts, right_pts = cvTools.find_vertical_edges(mask, rect_roi_2)
        
        # if len(left_pts) > 0 and len(right_pts) > 0:
        #     left_pts = left_pts[abs(left_pts[:,0]- rect_roi_2[0][0]<200)]
        if len(left_pts) > 20:
            left_pts = left_pts[ len(left_pts )//2 - 10 : len(left_pts)//2 + 10]
            right_pts = right_pts.mean(axis=0).reshape((-1,2)).astype(np.int32)
            min_dist, max_dist, avg_dist, _ = mathTools.horizontal_distance( left_pts, right_pts )
            
            res_dict = {
                'name': 'body_length',
                'limit_min': limits['min'],
                'limit_max': limits['max'],
                'min': round(min_dist * calib_value,2),
                'max': round(max_dist * calib_value,2),
                'avg': round(avg_dist * calib_value,2)
                 }

            
            if draw is not None:
                color=(30,200,0)
                draw = cvTools.draw_vertical_point( draw , [left_pts, right_pts], color=color, thicknes=5 )
                idx = len(left_pts)//2
                if len(right_pts)==1:
                    draw = cv2.line( draw, tuple(left_pts[idx]), (right_pts[0,0], left_pts[idx,1]), color=color, thickness=3   )
                else:
                    draw = cv2.line( draw, tuple(left_pts[idx]), tuple(right_pts[idx]), color=color, thickness=3   )
        
        else:
            res_dict = {
                'name': 'body_length',
                'limit_min': limits['min'],
                'limit_max': limits['max'],
                'min': -1,
                'max': -1,
                'avg': -1,
            }


            

    if draw is None:
        draw = np.copy( img )
    

    return [res_dict], draw
        
    

    
def proccessing_thread_male( img, mask, jsondb, draw=None, calib_value=1):
    page_name = '3_side'
    subpage_name = None
    rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name)
    jump_thresh = jsondb.get_numerical_parm(page_name, subpage_name, 'jump_thresh')
    navel  = jsondb.get_checkbox(page_name,subpage_name,'navel_lenght')
    limit_thread_lenght = jsondb.get_limit('thread_lenght', page_name, subpage_name)
    limit_thread_distance = jsondb.get_limit('thread_distance', page_name, subpage_name)
    limit_navel = jsondb.get_limit('navel_lenght', page_name, subpage_name)
    limit_thread_count = jsondb.get_limit('thread_count', page_name, subpage_name)

    result = []
    dict_lenght = set_dict('thread lenght', -2, -2, -2, limit_thread_lenght )
    dict_thread_distance = set_dict('thread distance', -2, -2, -2, limit_thread_distance )
    dict_thread_count = set_dict('thread count', -2, -2, -2, limit_thread_count )
    dict_navel = set_dict('navel lenght', -2, -2, -2, limit_navel )
    left_xs = None
    if Utils.is_rect(rect_roi_2):

        male_thread_l, male_thread_h = cvTools.find_screw_thread_top( mask, rect_roi_2,  min_diff=jump_thresh)
        
        if len(male_thread_h) > 2:
            if '2_side' in jsondb.get_active_tools() :
                rect_roi_2 = jsondb.get_rect_roi( '2_side', None)
                left_pts, _ = cvTools.find_vertical_edges(mask, rect_roi_2)
                left_xs = left_pts[:,0]

            
            if navel and left_xs is not None and len(left_xs):
                threads = np.vstack((male_thread_l,male_thread_h))
                first_thread_x = np.min(threads[:,0])
                thread_mean_y = int( threads[:,1].mean())

                navel_length = np.abs(left_xs-first_thread_x)
                dict_navel = {'name' : 'navel_lenght',
                                'limit_min': limit_navel['min'],
                                'limit_max': limit_navel['max'],
                                'min' : round(np.min(navel_length) * calib_value,2),
                                'max' : round(np.max(navel_length) * calib_value,2),
                                'avg' : round(np.round( np.average(navel_length) * calib_value ,2),2)
                              }
                
                if draw is not None:
                    cv2.line(draw, (first_thread_x, thread_mean_y),
                                    (int(left_xs.mean()), thread_mean_y),
                                    color=(200,0,0),
                                    thickness=2)

            if left_xs is not None and len(left_xs):
                rightes_thread_x = max( male_thread_h[:,0].max(), male_thread_l[:,0].max())
                lenght_male = rightes_thread_x - left_xs
                #_,_,lenght_male_avg,_  = mathTools.thread_lenght( male_thread_h )
                dict_lenght = {'name' : 'thread_male_length',
                                    'limit_min': limit_thread_lenght['min'],
                                    'limit_max': limit_thread_lenght['max'],
                                    'min': round( lenght_male.min() * calib_value,2),
                                    'max': round(lenght_male.max() * calib_value,2),
                                    'avg': round(lenght_male.mean() * calib_value,2) }
                

            min_s,max_s, avg_s,_  = mathTools.thread_step_distance( male_thread_h )
            
            dict_thread_distance = {'name' : 'thread_male_distance',
                                'limit_min': limit_thread_distance['min'],
                                'limit_max': limit_thread_distance['max'],
                                'min': round( min_s * calib_value,2),
                                'max': round(max_s * calib_value,2),
                                'avg': round(avg_s * calib_value,2) }
             
            min_s,max_s, avg_s,_  = mathTools.thread_step_distance( male_thread_h )
            dict_thread_count = {'name' : 'thread_male_count',
                            'limit_min': limit_thread_count['min'],
                            'limit_max': limit_thread_count['max'],
                            'min': len(male_thread_h),
                            'max': len(male_thread_h),
                            'avg': len(male_thread_h) }
            

            if draw is not None:
                draw = cvTools.draw_points(draw, male_thread_h, (0,50,150), 5)
                draw = cvTools.draw_points(draw, male_thread_l, (200,50,0), 5)

        else:
            dict_lenght = set_dict('thread lenght', -1, -1, -1, limit_thread_lenght )
            dict_thread_distance = set_dict('thread distance', -1, -1, -1, limit_thread_distance )
            dict_thread_count = set_dict('thread count', -1, -1, -1, limit_thread_count )
            if navel:
                dict_navel = set_dict('navel lenght', -1, -1, -1, limit_navel )
    
    result.append( dict_thread_distance )
    result.append( dict_lenght )
    result.append( dict_thread_count )
    if navel:
        result.append( dict_navel )

    if draw is None:
        draw = np.copy(img)
    return result, draw




        
def proccessing_side_diameters( img, mask, jsondb, draw=None, calib_value=1):
    page_name = '4_side'
    results = []

    for subpage_name in jsondb.get_subpages(page_name):
        if subpage_name == 'none':
            continue 

        rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name)
        limits = jsondb.get_limit('body_diameter', page_name, subpage_name)
        
        res_dict = set_dict('{} diameter'.format( subpage_name ) , -2, -2, -2, limits )
        if Utils.is_rect(rect_roi_2):
            left_pts, right_pts = cvTools.find_horizental_edges( mask, rect_roi_2)
            if len(left_pts) > 0 and len(right_pts) > 0:

                min_d, max_d, avg_d, _ = mathTools.vertical_distance( left_pts, right_pts )
                
                res_dict = {'name' : '{} diameter'.format( subpage_name ),
                            'limit_min': limits['min'],
                            'limit_max': limits['max'],
                            'min':round( min_d * calib_value,2),
                            'max':round( max_d * calib_value,2),
                            'avg':round( avg_d * calib_value ,2)}

                if draw is not None:
                    color = (200,50,15)
                    draw = cvTools.draw_horizental_point( draw, [left_pts, right_pts], color = color, thicknes=5 )
                    idx = len(left_pts)//2
                    draw = cv2.line( draw, tuple(left_pts[idx]), tuple(right_pts[idx]), color=color, thickness=3   )
                
            
            else:
                res_dict = {'name' : '{} diameter'.format( subpage_name ),
                            'limit_min': limits['min'],
                            'limit_max': limits['max'],
                            'min': -1,
                            'max': -1,
                            'avg': -1 }

                

        results.append( res_dict )
             
    if draw is None:
        draw = np.copy( img )
    
    return results, draw




def proccessing_side_head( img, mask, jsondb, draw=None , calib_value=1):
    page_name = '5_side'
    subpage_name = None
    results = []
    #--------------------------------------------------------------------------------------
    #specific Operation
    #--------------------------------------------------------------------------------------
    rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name, )
    jump_thresh = jsondb.get_numerical_parm(page_name, subpage_name, 'jump_thresh')
    edge_direction = jsondb.get_multi_option( page_name, subpage_name, 'edge_direction' )
    from_belt = jsondb.get_checkbox( page_name, subpage_name, 'from_belt')
    limits = jsondb.get_limit('height', page_name, subpage_name)

    res_dict = set_dict('head height', -2,-2,-2, limits)
    if Utils.is_rect(rect_roi_2):
        left_pts, right_pts = cvTools.find_head_vertival_pts(mask, rect_roi_2, jump_thresh, 0.25, side=edge_direction , from_belt=from_belt)
        
        if len(left_pts) > 0 and len(right_pts) > 0:
            min_dist, max_dist, avg_dist, _ = mathTools.horizontal_distance( left_pts, right_pts )

            res_dict = {
                'name': 'head_height',
                'limit_min': limits['min'],
                'limit_max': limits['max'],
                'min': round(min_dist * calib_value,2),
                'max': round(max_dist * calib_value,2),
                'avg': round(avg_dist * calib_value,2) }
            

            if draw is not None:
                color = (50,255,0) 
                draw = cvTools.draw_vertical_point( draw, [left_pts, right_pts], color, thicknes=5 )
                draw[ rect_roi_2[0][1]:rect_roi_2[1][1], left_pts[0,0] ] =  color#draw full line

        else:
            res_dict = set_dict('head height', -1,-1,-1, limits)

    results.append( res_dict )
    if draw is None:
        draw = np.copy( img )
    
    return results, draw


def preprocessing_side_damage( img, mask, jsondb, draw = None , calib_value=1):
    page_name = '6_side'
    results = []
    for subpage_name in jsondb.get_subpages(page_name):
        if subpage_name == 'none':
            continue 
        rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name, )
        limits = jsondb.get_limit('damage', page_name, subpage_name)   

        res_dict = set_dict('{} region area'.format( subpage_name ), -2,-2,-2, limits)
        if Utils.is_rect(rect_roi_2):
            area = cvTools.get_bigest_area( mask, rect_roi_2 )
            limit = jsondb.get_limit('damage', page_name, subpage_name)        
            res_dict = {
                        'name' : '{} region_area'.format( subpage_name ),
                        'limit_min': limits['min'],
                        'limit_max': limits['max'],
                        'min':round( area * (calib_value**2),4),
                        'max':round( area * (calib_value**2),4),
                        'avg':round( area * (calib_value**2),4) }
            
            results.append(res_dict)

            if draw is not None:

                rect_roi_2_mask = cvTools.rects2mask( draw.shape[:2], [rect_roi_2] )
                select_mask = cv2.bitwise_and(rect_roi_2_mask, mask)
                draw = Utils.mask_viewer(draw, select_mask, color=(0,180,220))

    if draw is None:
        draw = np.copy(img)
    
    return results, draw



#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________
#______________________________________________ TOP CAMERA ________________________________________________
#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________


def preprocessing_empty(img, mask, jsondb, draw=None):
    if draw is None:
        draw = np.copy(img)
    return [], draw







def proccessing_top_measurment( img, mask_roi_main, jsondb, draw = None , calib_value=1):
    page_name = '2_top'
    results = []
    for subpage_name in jsondb.get_subpages(page_name):
        if subpage_name == 'none':
            continue 
        # thresh = jsondb.get_thresh(page_name, subpage_name)
        thresh_min = jsondb.get_thresh_min(page_name, subpage_name)
        thresh_max = jsondb.get_thresh_max(page_name, subpage_name)
        noise_filter = jsondb.get_noise_filter( page_name, subpage_name )
        # inv_state = jsondb.get_thresh_inv(page_name, subpage_name)
        shape_type = jsondb.get_multi_option( page_name, subpage_name, 'shape_type' )
        circel_roi = jsondb.get_circels_roi(page_name, subpage_name)
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        mask = cvTools.circels2mask(mask_roi_main.shape, circel_roi)
        mask = cv2.bitwise_and(mask, mask_roi_main)
        thresh_img = cvTools.threshould_minmax(img, thresh_min, thresh_max, mask)
        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        cnt = cvTools.extract_bigest_contour(thresh_img)
        if len(cnt)> 30:
            cnt = cvTools.conture_moving_avg(cnt, 20)

        if draw is not None:
           draw = Utils.mask_viewer(draw, thresh_img)
        
        
        if len(cnt)>0:
            res_dict = {}
            if shape_type == 'circel':
                limit = jsondb.get_limit('diameter', page_name, subpage_name)
                diameters = cvTools.circel_measument(cnt)
                res_dict = {
                        'name' : '{} diameter'.format( subpage_name ),
                        'limit_min': limit['min'],
                        'limit_max': limit['max'],
                        'min': round(diameters.min() * calib_value,2),
                        'max': round(diameters.max() * calib_value,2),
                        'avg': round(np.round(diameters.mean() * calib_value,2) ,2)}
                results.append( res_dict)
                
            
            elif shape_type == 'hexagonal':
                c2c , e2e = cvTools.hexagonal_measument(cnt)
                limit = jsondb.get_limit('district', page_name, subpage_name)
                res_dict = {
                        'name' : '{} district'.format( subpage_name ),
                        'limit_min': limit['min'],
                        'limit_max': limit['max'],
                        'min':round( e2e.min() * calib_value,2),
                        'max':round( e2e.max() * calib_value,2),
                        'avg':round( np.round(e2e.mean() * calib_value,2) ,2)}
                results.append( res_dict )
                #-----------------------------------------------
                limit = jsondb.get_limit('corner', page_name, subpage_name)
                res_dict = {
                        'name' : '{} corner'.format( subpage_name ),
                        'limit_min': limit['min'],
                        'limit_max': limit['max'],
                        'min':round( c2c.min() * calib_value,2),
                        'max':round( c2c.max() * calib_value,2),
                        'avg':round( np.round(c2c.mean() * calib_value,2) ,2)}

                results.append( res_dict )
                


            elif shape_type == 'rect':
                print('shape_type rect Proccessing')


            
            if draw is not None:
                if shape_type == 'circel':
                    draw = cv2.drawContours(draw, [cnt], 0, (0,200,0), thickness=5)
                elif shape_type == 'hexagonal':
                    draw = cv2.drawContours(draw, [cnt], 0, (200,0,0), thickness=5)


        else:
            if shape_type == 'circel':
                limit = jsondb.get_limit('diameter', page_name, subpage_name)
                res_dict = {
                        'name' : '{} diameter'.format( subpage_name ),
                        'limit_min': limit['min'],
                        'limit_max': limit['max'],
                        'min': -1,
                        'max': -1,
                        'avg': -1
                         }
                results.append( res_dict)
                
            
            elif shape_type == 'hexagonal':
                limit = jsondb.get_limit('district', page_name, subpage_name)
                res_dict = {
                        'name' : '{} district'.format( subpage_name ),
                        'limit_min': limit['min'],
                        'limit_max': limit['max'],
                        'min': -1,
                        'max': -1,
                        'avg': -1
                         }
                results.append( res_dict )
                #-----------------------------------------------
                limit = jsondb.get_limit('corner', page_name, subpage_name)
                res_dict = {
                        'name' : '{} corner'.format( subpage_name ),
                        'limit_min': limit['min'],
                        'limit_max': limit['max'],
                        'min': -1,
                        'max': -1,
                        'avg': -1
                         }

                results.append( res_dict )
                


            elif shape_type == 'rect':
                print('shape_type rect Proccessing')


    
    if draw is None:
        draw = np.copy(img)
    return results, draw







def proccessing_top_defect( img, mask_roi_main, jsondb, draw=None , calib_value=1):
    page_name = '3_top'
    results = []
    for subpage_name in jsondb.get_subpages(page_name):    
        if subpage_name == 'none':
            continue    
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        thresh = jsondb.get_thresh(page_name, subpage_name)
        noise_filter = jsondb.get_noise_filter( page_name, subpage_name )
        inv_state = jsondb.get_thresh_inv(page_name, subpage_name)
        circels_roi = jsondb.get_circels_roi(page_name, subpage_name)
        min_area_lake = jsondb.get_numerical_parm(page_name, subpage_name, 'min_area')
        thresh_min = jsondb.get_thresh_min(page_name, subpage_name)
        thresh_max = jsondb.get_thresh_max(page_name, subpage_name)
 
        thresh_img = cvTools.threshould_minmax(img, thresh_min, thresh_max, mask_roi_main)
        thresh_img = cv2.dilate(thresh_img, np.ones((3,3)))
        thresh_img = cv2.erode(thresh_img, np.ones((3,3)))
        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        mask_roi = cvTools.donate2mask(thresh_img.shape, circels_roi, 255)
        thresh_img = cv2.bitwise_and(thresh_img, mask_roi)
        lakes_cnt, lakes_ares  = cvTools.filter_area(thresh_img, min_area_lake)
        #------------------------------------------------------------------------------------

        res_dict = {}
        if len(lakes_ares) > 0:
            res_dict = {
                    'name' : '{} defect'.format( subpage_name ),
                    'limit_min':0,
                    'limit_max': min_area_lake,
                    'min':round( lakes_ares.min() *(calib_value**2),2),
                    'max':round( lakes_ares.max() *(calib_value**2),2),
                    'avg':round( lakes_ares.max() *(calib_value**2),2)}
        else:
            res_dict = {
                    'name' : '{} defect'.format( subpage_name ),
                    'limit_min': 0,
                    'limit_max': min_area_lake,
                    'min': 0,
                    'max': 0,
                    'avg': 0, 
                    }
        results.append(res_dict)
        #------------------------------------------------------------------------------------
        
        if draw is not None:
            draw = cv2.drawContours(draw, lakes_cnt, -1, (0,0,100), thickness=-1)

    if draw is None:
        draw = np.copy(img)    
    return results, draw 







def proccessing_top_edge_crack( img, mask_roi_main, jsondb, draw=None, calib_value=1):
    page_name = '4_top'
    subpage_name = None
    results = []
    #--------------------------------------------------------------------------------------
    #specific Operation
    #--------------------------------------------------------------------------------------


    noise_filter = jsondb.get_noise_filter( page_name, subpage_name )
    inv_state = jsondb.get_thresh_inv(page_name, subpage_name)
    circel_roi = jsondb.get_circels_roi(page_name, subpage_name)
    min_area_crack = jsondb.get_numerical_parm(page_name, subpage_name, 'min_area')

    thresh_min = jsondb.get_thresh_min(page_name, subpage_name)
    thresh_max = jsondb.get_thresh_max(page_name, subpage_name)


    mask_roi = cvTools.circels2mask(mask_roi_main.shape, circel_roi)
    mask_roi=cv2.bitwise_and(mask_roi,mask_roi_main)
    thresh_img = cvTools.threshould_minmax(img, thresh_min, thresh_max, mask_roi)

    thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
    cracks, cracks_area = cvTools.find_edge_crack(thresh_img, min_area_crack, 10 )


    
    res_dict = {}
    #------------------------------------------------------------------------------------
    if len(cracks) > 0:
        res_dict = {
                    'name' : 'edge_crack',
                    'limit_min': 0,
                    'limit_max': 1,
                    'min':round( cracks_area.min() * (calib_value**2),2),
                    'max':round( cracks_area.max() * (calib_value**2),2),
                    'avg':round( cracks_area.max() * (calib_value**2),2)}
    else:
        res_dict = {
                    'name' : 'edge_crack',
                    'limit_min': 0,
                    'limit_max': 1,
                    'min': 0,
                    'max': 0,
                    'avg': 0 }
    results.append(res_dict)
    #------------------------------------------------------------------------------------
    
    if draw is not None:
        draw = cv2.drawContours(draw, cracks, -1, (0,0,255), thickness=-1)

    return results, draw




def proccessing_top_centerise( img, mask, jsondb, draw=None, calib_value=1):
    page_name = '5_top'
    subpage_name = 'flanch'
    results = []
    
    #--------------------------------------------------------------------------------------
    #specific Operation
    #--------------------------------------------------------------------------------------
    sub_thresh_imgs = get_general_masks(img, jsondb, page_name )

    


    limit = jsondb.get_limit('distance', page_name, subpage_name)
            



    res_dict = {}
    centers = []
    dist = -1
    #------------------------------------------------------------------------------------
    if len(sub_thresh_imgs) == 2:
        masks = list(sub_thresh_imgs.values())
        cnts, centers, dist = cvTools.centerise_measurment(masks)
        res_dict = {
                    'name' : 'center_dist',
                    'limit_min': limit['min'],
                    'limit_max': limit['max'],
                    'min':round( dist * calib_value,2),
                    'max':round( dist * calib_value,2),
                    'avg':round( dist * calib_value,2)
                     }

    else:
        res_dict = {
                    'name' : 'center_dist',
                    'limit_min': limit['min'],
                    'limit_max': limit['max'],
                    'min': -1,
                    'max': -1,
                    'avg': -1,
                     }

    results.append(res_dict)
    if draw is not None:
        colors =[(255,0,0),(0,255,0)]
        for i , mask in enumerate(sub_thresh_imgs.values()):
            draw = Utils.mask_viewer(draw, mask,color=colors[i])

        for center in centers:
            draw = cv2.circle(draw, center, 3, (0,0,255) , thickness=-1)

    return results, draw


def calibration_generator(power,):
    def func(value,calibration_num):
        return pow(calibration_num,power)*value

    return func

tools_dict_top = {
            '0_top': preprocessing_empty,
            '1_top': preprocessing_empty,
            '2_top': proccessing_top_measurment,
            '3_top': proccessing_top_defect,
            '4_top': proccessing_top_edge_crack,
            '5_top': proccessing_top_centerise,
        }




tools_dict_side = {
            '1_side': preprocessing_empty,
            '2_side': proccessing_body_lenght,
            '3_side': proccessing_thread_male,
            '4_side': proccessing_side_diameters,
            '5_side': proccessing_side_head,
            '6_side': preprocessing_side_damage,
        }



calib_dict_top = {
            'corner': calibration_generator(1),
            'district': calibration_generator(1),
            'diameter': calibration_generator(1),
            'distance': calibration_generator(1),
        }



calib_dict_side = {
            'body_length': calibration_generator(1),
            'thread_male_distance': calibration_generator(1),
            'thread_male_length': calibration_generator(1),
            'diameter': calibration_generator(1),
            'head_height': calibration_generator(1),
            'region_area': calibration_generator(2),
            'navel_lenght' : calibration_generator(1),
        }





if __name__=='__main__':
    calibration_generator(3)