from ast import Not
from cv2 import cvtColor
from backend import mathTools, cvTools, Utils
import cv2
import numpy as np


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

        thresh = json.get_thresh(page_name, subpage_name)
        noise_filter = json.get_noise_filter( page_name, subpage_name )
        inv_state = json.get_thresh_inv(page_name, subpage_name)
        circels_roi = json.get_circels_roi(page_name, subpage_name)
    
        mask_roi = cvTools.circels2mask(img.shape[:2], circels_roi)
        thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        
        if main_roi_mask is not None:
            thresh_img = cv2.bitwise_and(thresh_img, main_roi_mask)
        
        res[subpage_name] = np.copy( thresh_img )
    return res


def preprocessing_top_img( img, json, direction):
    thresh = json.get_thresh('1_{}'.format( direction ), None )
    noise_filter = json.get_noise_filter( '1_{}'.format( direction ), None  )
    rect_roi_main = json.get_rect_roi( '1_{}'.format( direction ), None )
    inv_state = json.get_thresh_inv('1_{}'.format( direction ), None )
    
    mask_roi = cvTools.rects2mask(img.shape[:2], [rect_roi_main])
    thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
    thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
    #--------------------------------------------------------------------------------------
    #correct rotation
    #--------------------------------------------------------------------------------------
    thresh_img, img, div_pt = cvTools.centerise_top(thresh_img, img )
    thresh_img = cvTools.mask_bigest_contour(thresh_img)


    return img, thresh_img, div_pt

#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________
#
#
#
#
#
#
#
#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________


def preprocessing_side_img( img, json, direction):
    thresh = json.get_thresh('1_{}'.format( direction ), None )
    noise_filter = json.get_noise_filter( '1_{}'.format( direction ), None  )
    rect_roi_main = json.get_rect_roi( '1_{}'.format( direction ), None )
    inv_state = json.get_thresh_inv('1_{}'.format( direction ), None )
    
    mask_roi = cvTools.rects2mask(img.shape[:2], [rect_roi_main])
    thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
    thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
    #--------------------------------------------------------------------------------------
    #correct rotation
    #--------------------------------------------------------------------------------------
    mask_unbelt, _ = cvTools.remove_belt( thresh_img,rect_roi_main, thresh=0.7 )
    angle, _ = cvTools.correct_rotation_angle(mask_unbelt)
    thresh_img = cvTools.rotate_image(thresh_img,  angle   )
    img = cvTools.rotate_image(img,  angle   )

    thresh_img, img, _ = cvTools.centerise_side( thresh_img, img )
    return img, thresh_img, angle



def proccessing_body_lenght( img, mask, jsondb, draw=None):
    page_name = '2_side'
    subpage_name = None
    
    rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name)
    limits = jsondb.get_limit('lenght', page_name, subpage_name)

    res_dict = set_dict('body length', -2, -2, -2, limits )        
    if Utils.is_rect(rect_roi_2):
        left_pts, right_pts = cvTools.find_vertical_edges(mask, rect_roi_2)
        if len(left_pts) > 0 and len(right_pts) > 0:
            min_dist, max_dist, avg_dist, _ = mathTools.horizontal_distance( left_pts, right_pts )
            
            res_dict = {
                'name': 'body length',
                'limit_min': limits['min'],
                'limit_max': limits['max'],
                'min': min_dist,
                'max': max_dist,
                'avg': avg_dist
                 }

            
            if draw is not None:
                color=(30,200,0)
                draw = cvTools.draw_vertical_point( draw , [left_pts, right_pts], color=color, thicknes=5 )
                idx = len(left_pts)//2
                draw = cv2.line( draw, tuple(left_pts[idx]), tuple(right_pts[idx]), color=color, thickness=3   )
        
        else:
            res_dict = {
                'name': 'body length',
                'limit_min': limits['min'],
                'limit_max': limits['max'],
                'min': -1,
                'max': -1,
                'avg': -1,
            }


            

    if draw is None:
        draw = np.copy( img )
    

    return [res_dict], draw
        
    

    
def proccessing_thread_male( img, mask, jsondb, draw=None):
    page_name = '3_side'
    subpage_name = None
    rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name)
    jump_thresh = jsondb.get_numerical_parm(page_name, subpage_name, 'jump_thresh')

    thread_lenght = jsondb.get_limit('thread_lenght', page_name, subpage_name)
    thread_distance = jsondb.get_limit('thread_distance', page_name, subpage_name)
    thread_count = jsondb.get_limit('thread_count', page_name, subpage_name)

    result = []
    res_dict_lenght = set_dict('thread_lenght', -2, -2, -2, thread_lenght )
    thread_distance = set_dict('thread_distance', -2, -2, -2, thread_distance )
    thread_count = set_dict('thread_count', -2, -2, -2, thread_count )
    if Utils.is_rect(rect_roi_2):
        male_thread_l, male_thread_h = cvTools.find_screw_thread_top( mask, rect_roi_2,  min_diff=jump_thresh)

        if len(male_thread_h) > 2:
            _,_,lenght_male_avg,_  = mathTools.thread_lenght( male_thread_h )
            res_dict_lenght = {'name' : 'thread male length',
                                'limit_min': thread_lenght['min'],
                                'limit_max': thread_lenght['max'],
                                'min': lenght_male_avg,
                                'max': lenght_male_avg,
                                'avg': lenght_male_avg }
            

            min_s,max_s, avg_s,_  = mathTools.thread_step_distance( male_thread_h )
            
            thread_distance = {'name' : 'thread male distance',
                                'limit_min': thread_distance['min'],
                                'limit_max': thread_distance['max'],
                                'min': min_s,
                                'max': max_s,
                                'avg': avg_s }
             
            min_s,max_s, avg_s,_  = mathTools.thread_step_distance( male_thread_h )
            thread_count = {'name' : 'thread male distance',
                            'limit_min': thread_count['min'],
                            'limit_max': thread_count['max'],
                            'min': len(male_thread_h),
                            'max': len(male_thread_h),
                            'avg': len(male_thread_h) }
            

            if draw is not None:
                draw = cvTools.draw_points(draw, male_thread_h, (0,50,150), 5)
                draw = cvTools.draw_points(draw, male_thread_l, (200,50,0), 5)

        else:
            res_dict_lenght = set_dict('thread_lenght', -1, -1, -1, thread_lenght )
            thread_distance = set_dict('thread_distance', -1, -1, -1, thread_distance )
            thread_count = set_dict('thread_count', -1, -1, -1, thread_count )
    
    
    result.append( thread_distance )
    result.append( res_dict_lenght )
    result.append( thread_count )

    if draw is None:
        draw = np.copy(img)
    return result, draw




        
def proccessing_side_diameters( img, mask, jsondb, draw=None):
    page_name = '4_side'
    results = []

    for subpage_name in jsondb.get_subpages(page_name):

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
                            'min': min_d,
                            'max': max_d,
                            'avg': avg_d }

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




def proccessing_side_head( img, mask, jsondb, draw=None):
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
                'name': 'head height',
                'limit_min': limits['min'],
                'limit_max': limits['max'],
                'min': min_dist,
                'max': max_dist,
                'avg': avg_dist }
            

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


def preprocessing_side_damage( img, mask, jsondb, draw = None):
    page_name = '6_side'
    results = []
    for subpage_name in jsondb.get_subpages(page_name):
        rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name, )
        limits = jsondb.get_limit('damage', page_name, subpage_name)   

        res_dict = set_dict('{} region area'.format( subpage_name ), -2,-2,-2, limits)
        if Utils.is_rect(rect_roi_2):
            area = cvTools.get_bigest_area( mask, rect_roi_2 )
            limit = jsondb.get_limit('damage', page_name, subpage_name)        
            res_dict = {
                        'name' : '{} region area'.format( subpage_name ),
                        'limit_min': limits['min'],
                        'limit_max': limits['max'],
                        'min': area,
                        'max': area,
                        'avg': area }
            
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







def proccessing_top_measurment( img, mask, jsondb, draw = None):
    page_name = '2_top'
    results = []
    for subpage_name in jsondb.get_subpages(page_name):
        thresh = jsondb.get_thresh(page_name, subpage_name)
        noise_filter = jsondb.get_noise_filter( page_name, subpage_name )
        inv_state = jsondb.get_thresh_inv(page_name, subpage_name)
        shape_type = jsondb.get_multi_option( page_name, subpage_name, 'shape_type' )
        
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
    
        thresh_img = cvTools.threshould(img, thresh, mask, inv_state)
        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        cnt = cvTools.extract_bigest_contour(thresh_img)
        
        
        if len(cnt)>0:
            res_dict = {}
            if shape_type == 'circel':
                limit = jsondb.get_limit('diameter', page_name, subpage_name)
                diameters = cvTools.circel_measument(cnt)
                res_dict = {
                        'name' : '{} diameter'.format( subpage_name ),
                        'limit_min': limit['min'],
                        'limit_max': limit['max'],
                        'min': diameters.min(),
                        'max': diameters.max(),
                        'avg': np.round(diameters.mean(),2) }
                results.append( res_dict)
                
            
            elif shape_type == 'hexagonal':
                c2c , e2e = cvTools.hexagonal_measument(cnt)
                limit = jsondb.get_limit('district', page_name, subpage_name)
                res_dict = {
                        'name' : '{} district'.format( subpage_name ),
                        'limit_min': limit['min'],
                        'limit_max': limit['max'],
                        'min': e2e.min(),
                        'max': e2e.max(),
                        'avg': np.round(e2e.mean(),2) }
                results.append( res_dict )
                #-----------------------------------------------
                limit = jsondb.get_limit('corner', page_name, subpage_name)
                res_dict = {
                        'name' : '{} corner'.format( subpage_name ),
                        'limit_min': limit['min'],
                        'limit_max': limit['max'],
                        'min': c2c.min(),
                        'max': c2c.max(),
                        'avg': np.round(c2c.mean(),2) }

                results.append( res_dict )
                


            elif shape_type == 'rect':
                print('rect')


            
            if draw is not None:
                draw = cv2.drawContours(draw, [cnt], 0, (0,200,0), thickness=5)

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
                print('rect')



    if draw is None:
        draw = np.copy(img)
    return results, draw







def proccessing_top_defect( img, mask, jsondb, draw=None):
    page_name = '3_top'
    results = []
    for subpage_name in jsondb.get_subpages(page_name):        
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        thresh = jsondb.get_thresh(page_name, subpage_name)
        noise_filter = jsondb.get_noise_filter( page_name, subpage_name )
        inv_state = jsondb.get_thresh_inv(page_name, subpage_name)
        circels_roi = jsondb.get_circels_roi(page_name, subpage_name)
        min_area_lake = jsondb.get_numerical_parm(page_name, subpage_name, 'min_area')
        
        thresh_img = cvTools.threshould(img, thresh, mask, inv_state)
        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        mask_roi = cvTools.donate2mask(thresh_img.shape, circels_roi, 255)
        thresh_img = cv2.bitwise_and(thresh_img, mask_roi)
        lakes_cnt, lakes_ares  = cvTools.filter_area(thresh_img, min_area_lake)
        #------------------------------------------------------------------------------------
        res_dict = {}
        if len(lakes_ares) > 0:
            res_dict = {
                    'name' : '{} defect'.format( subpage_name ),
                    'limit_min': 0,
                    'limit_max': 1,
                    'min': lakes_ares.min(),
                    'max': lakes_ares.max(),
                    'avg': lakes_ares.mean() }
        else:
            res_dict = {
                    'name' : '{} defect'.format( subpage_name ),
                    'limit_min': 0,
                    'limit_max': 1,
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







def proccessing_top_edge_crack( img, mask, jsondb, draw=None):
    page_name = '4_top'
    subpage_name = None
    results = []
    #--------------------------------------------------------------------------------------
    #specific Operation
    #--------------------------------------------------------------------------------------
    thresh = jsondb.get_thresh(page_name, subpage_name)
    noise_filter = jsondb.get_noise_filter( page_name, subpage_name )
    inv_state = jsondb.get_thresh_inv(page_name, subpage_name)
    circel_roi = jsondb.get_circels_roi(page_name, subpage_name)
    min_area_crack = jsondb.get_numerical_parm(page_name, subpage_name, 'min_area')
    
    mask_roi = cvTools.circels2mask(mask.shape, circel_roi)
    thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
    thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
    cracks, cracks_area = cvTools.find_edge_crack(thresh_img, min_area_crack, 10 )
    res_dict = {}
    #------------------------------------------------------------------------------------
    if len(cracks) > 0:
        res_dict = {
                    'name' : 'edge crack',
                    'limit_min': 0,
                    'limit_max': 1,
                    'min': cracks_area.min(),
                    'max': cracks_area.max(),
                    'avg': cracks_area.mean() }
    else:
        res_dict = {
                    'name' : 'edge crack',
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




def proccessing_top_centerise( img, mask, jsondb, draw=None):
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
                    'name' : 'center dist',
                    'limit_min': limit['min'],
                    'limit_max': limit['max'],
                    'min': dist,
                    'max': dist,
                    'avg': dist
                     }

    else:
        res_dict = {
                    'name' : 'center dist',
                    'limit_min': limit['min'],
                    'limit_max': limit['max'],
                    'min': -1,
                    'max': -1,
                    'avg': -1,
                     }

    results.append(res_dict)
    if draw is not None:
        for center in centers:
            draw = cv2.circle(draw, center, 3, (0,0,255) , thickness=-1)

    return results, draw




tools_dict_top = {
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
