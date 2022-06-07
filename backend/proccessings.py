from backend import mathTools, cvTools, Utils



#___________________________________________________________________________________________________________________________
#
#
#
#
#
#
#
#
#
#
#
#___________________________________________________________________________________________________________________________


def preprocessing_img_json( img, json, direction):
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






def preprocessing_empty(thresh_img, jsondb, img=None):
    return [], img





tools_dict = {
            '1_side': preprocessing_empty,
            '2_side': proccessing_body_lenght,
            '3_side': proccessing_thread_male,
            '4_side': proccessing_side_diameters,
            '5_side': preprocessing_empty,
            '6_side': preprocessing_side_damage,
        }
