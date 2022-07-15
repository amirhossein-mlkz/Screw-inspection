from ast import Not
from cv2 import cvtColor
from backend import mathTools, cvTools, Utils
import cv2
import numpy as np


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



def proccessing_body_lenght( thresh_img, jsondb, img=None):
    page_name = '2_side'
    subpage_name = None
    
    rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name)
    limits = jsondb.get_limit('lenght', page_name, subpage_name)

    if Utils.is_rect(rect_roi_2):
        left_pts, right_pts = cvTools.find_vertical_edges(thresh_img, rect_roi_2)
        if len(left_pts) > 0 and len(right_pts) > 0:
            min_dist, max_dist, avg_dist, _ = mathTools.horizontal_distance( left_pts, right_pts )

            if img is not None:
                img = cvTools.draw_vertical_point( img , [left_pts, right_pts], color=(0,0,255), thicknes=5 )

    
    res_dict = {'name': 'screw body length',
                'limit_min': limits['min'],
                'limit_max': limits['max'],
                'min': min_dist,
                'max': max_dist,
                'avg': avg_dist }

    return [res_dict], img
        
    

    
def proccessing_thread_male( thresh_img, jsondb, img=None):
    page_name = '3_side'
    subpage_name = None
    rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name)
    
    result = []
    if Utils.is_rect(rect_roi_2):
        male_thread_l, male_thread_h = cvTools.find_screw_thread( thresh_img, rect_roi_2,  min_diff=5)
        
        min_d,max_d, avg_d,_ = mathTools.vertical_distance( male_thread_h, male_thread_l )
        limits = jsondb.get_limit('thread_lenght', page_name, subpage_name)
        res_dict = {'name' : 'thread male length',
                    'limit_min': limits['min'],
                    'limit_max': limits['max'],
                    'min': min_d,
                    'max': max_d,
                    'avg': avg_d }
        result.append( res_dict )

        min_s,max_s, avg_s,_  = mathTools.thread_step_distance( male_thread_h )
        limits = jsondb.get_limit('thread_distance', page_name, subpage_name)
        res_dict = {'name' : 'thread male distance',
                    'limit_min': limits['min'],
                    'limit_max': limits['max'],
                    'min': min_s,
                    'max': max_s,
                    'avg': avg_s }
        result.append( res_dict )

        min_s,max_s, avg_s,_  = mathTools.thread_step_distance( male_thread_h )
        limits = jsondb.get_limit('thread_count', page_name, subpage_name)
        res_dict = {'name' : 'thread male distance',
                    'limit_min': limits['min'],
                    'limit_max': limits['max'],
                    'min': len(male_thread_h),
                    'max': len(male_thread_h),
                    'avg': len(male_thread_h) }

        if img is not None:
            img = cvTools.draw_points(img, male_thread_h, (0,50,150), 3)
            img = cvTools.draw_points(img, male_thread_l, (200,0,200), 3)


        result.append( res_dict )
        return result, img


        #info = {'thread_lenght': avg_d,  'count_thread':len(male_thread_h) , 'step_distance':avg_s}
        #img = cvTools.draw_points(img, male_thread_h, (0,50,150), 3)
        #img = cvTools.draw_points(img, male_thread_l, (200,0,200), 3)

        
def proccessing_side_diameters( thresh_img, jsondb, img=None):
    page_name = '4_side'
    results = []
    for subpage_name in jsondb.get_subpages(page_name):
        rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name)
        if Utils.is_rect(rect_roi_2):
            left_pts, right_pts = cvTools.find_horizental_edges( thresh_img, rect_roi_2)
            if len(left_pts) > 0 and len(right_pts) > 0:
                #img = draw_horizental_point( img, [left_pts, right_pts], (0,0,255), thicknes=5 )
                min_d, max_d, avg_d, _ = mathTools.horizontal_distance( left_pts, right_pts )
                limit = jsondb.get_limit('body_diameter', page_name, subpage_name)
                res_dict = {'name' : '{} diameter'.format( subpage_name ),
                            'limit_min': limit['min'],
                            'limit_max': limit['max'],
                            'min': min_d,
                            'max': max_d,
                            'avg': avg_d }
                

                if img is not None:
                    img = cvTools.draw_horizental_point( img, [left_pts, right_pts], (0,0,255), thicknes=5 )
            
            else:
                res_dict = {
                            'name' : '{} diameter'.format( subpage_name ),
                            'limit_min': limit['min'],
                            'limit_max': limit['max'],
                            'min': -1,
                            'max': -1,
                            'avg': -1 }
            results.append( res_dict )
    
    return results, img




def preprocessing_side_damage( thresh_img, jsondb, img=None):
    page_name = '6_side'
    results = []
    for subpage_name in jsondb.get_subpages(page_name):
        rect_roi_2 = jsondb.get_rect_roi( page_name, subpage_name, )
        if Utils.is_rect(rect_roi_2):
            area = cvTools.get_bigest_area( thresh_img, rect_roi_2 )
            limit = jsondb.get_limit('damage', page_name, subpage_name)        
            res_dict = {
                        'name' : '{} region area'.format( subpage_name ),
                        'limit_min': limit['min'],
                        'limit_max': limit['max'],
                        'min': area,
                        'max': area,
                        'avg': area }
            
            results.append(res_dict)
    
    return results, img






def preprocessing_empty(img, thresh_img, jsondb, draw=None):
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
            '5_side': preprocessing_empty,
            '6_side': preprocessing_side_damage,
        }
