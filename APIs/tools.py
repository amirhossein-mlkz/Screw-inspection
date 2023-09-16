from backend import cvTools
from backend import Utils
import numpy as np
import cv2
import os
from backend import proccessings
from backend import mathTools

class toolsAPI:


    def __init__(self, ui) -> None:
        self.ui = ui


    def setting_image_updater(self):
        page2finc_dict = {

        '0_top':self.update_image_0_top,
        '1_top':self.update_image_1_top,
        '2_top':self.update_image_2_top,
        '3_top':self.update_image_3_top,
        '4_top':self.update_image_4_top,
        '5_top':self.update_image_5_top,
        
        '1_side':self.update_image_1_side,
        '2_side':self.update_image_2_side,            
        '3_side':self.update_image_3_side,        
        '4_side':self.update_image_4_side,
        '5_side':self.update_image_5_side,               
        '6_side':self.update_image_6_side,

        }
        page_name = self.ui.get_setting_page_idx(page_name = True)

        try:
            page2finc_dict[page_name]()
        except:
            print('Error TOOLS setting_image_updater')
            pass
    


    def update_image_0_top(self):
    
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        img = np.copy(self.current_image_screw)


        lbelt = self.screw_jasons[ direction ].get_numerical_parm(page_name, subpage_name, 'lbelt')
        rbelt = self.screw_jasons[ direction ].get_numerical_parm(page_name, subpage_name, 'rbelt')
        angle = self.screw_jasons[ direction ].get_numerical_parm(page_name, subpage_name, 'angle')

        img = cvTools.rotate_image(img,angle=angle)




        if self.ui.is_drawing_mask_enabel():
            img[:,lbelt-1:lbelt+2] = [0,0,255]
            img[:,rbelt-1:rbelt+2] = [0,255,0]
            # img = Utils.mask_viewer(img, thresh_img)
            # h,w = img.shape[:2]
            # img = cv2.circle(img, (w//2, h//2), 5, (0,255,0) , thickness=-1)

        # img = self.rect_roi_drawing.get_image(img)
        
        self.ui.set_image_page_tool_labels(img)

        # if Utils.is_rect( rect ) and np.count_nonzero(thresh_img) > 100:
        #     self.ui.enable_bar_btn_tool_page( direction, True )
        # else:
        #     self.ui.enable_bar_btn_tool_page( direction, False )



    def update_image_1_top(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        img = np.copy(self.current_image_screw)
        # if not self.tools_live_enable:
        #     img = np.copy(self.current_image_screw)
        # else:
        #     img = self.current_camera_imgs['top']
        




        thresh_min = self.screw_jasons[ direction ].get_thresh_min(page_name, subpage_name)
        thresh_max = self.screw_jasons[ direction ].get_thresh_max(page_name, subpage_name)
        #############

        noise_filter = self.screw_jasons[ direction ].get_noise_filter( page_name, subpage_name )
        rect = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name)
        # inv_state = self.screw_jasons[ direction ].get_thresh_inv(page_name, subpage_name)
        

        img = cvTools.preprocess(img)

        mask_roi = cvTools.rects2mask(img.shape[:2], [rect])
        
        #thresh mode
        thresh_img = cvTools.threshould_minmax(img, thresh_min, thresh_max, mask_roi)
        # thresh_img=cvTools.erode(thresh_img, 5)
        # thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        #thresh_img = cvTools.erode(thresh_img, 3)

        #edge mode
        # thresh_img = cvToolsCython.derivative_threshould(img, 15)
        # thresh_img = cv2.bitwise_and( thresh_img, thresh_img , mask=mask_roi)
        # kernel =np.ones((3,3))
        # thresh_img = cv2.morphologyEx(thresh_img, cv2.MORPH_CLOSE, kernel,iterations =noise_filter)

        # cv2.
        ######################### 
        

        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img)
            h,w = img.shape[:2]
            img = cv2.circle(img, (w//2, h//2), 5, (0,255,0) , thickness=-1)

        img = self.rect_roi_drawing.get_image(img)
        
        self.ui.set_image_page_tool_labels(img)

        if Utils.is_rect( rect ) and np.count_nonzero(thresh_img) > 100:
            self.ui.enable_bar_btn_tool_page( direction, True )
        else:
            self.ui.enable_bar_btn_tool_page( direction, False )
            

    def update_image_2_top(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )

        img = np.copy(self.current_image_screw)
        json = self.screw_jasons[ direction ]
        img, mask_roi_main, _ = proccessings.preprocessing_top_img( img, json, direction  )

        if subpage_name!='none':
            #--------------------------------------------------------------------------------------
            #specific Operation
            #--------------------------------------------------------------------------------------
            thresh_min = self.screw_jasons[ direction ].get_thresh_min(page_name, subpage_name)
            thresh_max = self.screw_jasons[ direction ].get_thresh_max(page_name, subpage_name)
            thresh = self.screw_jasons[ direction ].get_thresh(page_name, subpage_name)
            noise_filter = self.screw_jasons[ direction ].get_noise_filter( page_name, subpage_name )
            inv_state = self.screw_jasons[ direction ].get_thresh_inv(page_name, subpage_name)
            shape_type = self.screw_jasons[ direction ].get_multi_option( page_name, subpage_name, 'shape_type' )
            circel_roi = self.screw_jasons[ direction ].get_circels_roi(page_name, subpage_name)

            mask_roi = cvTools.circels2mask(mask_roi_main.shape, circel_roi)
            mask_roi = cv2.bitwise_and(mask_roi, mask_roi_main)
            #thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
            thresh_img = cvTools.threshould_minmax(img, thresh_min, thresh_max, mask_roi)
            thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
            cnt = cvTools.extract_bigest_contour(thresh_img)
            #--------------------------------------------------------------------------------------
            info = {}
            if shape_type == 'circel':

                diameters = cvTools.circel_measument(cnt)
                info = {'min_diameter' : diameters.min(), 'max_diameter': diameters.max()}
                self.ui.stackedWidget_3.setCurrentIndex(0)
            
            elif shape_type == 'hexagonal':

                c2c , e2e = cvTools.hexagonal_measument(cnt)
                info = { 'min_district': e2e.min(),
                        'max_district': e2e.max(), 
                        'min_corner' : c2c.min(),
                        'max_corner' : c2c.max(),  }
                self.ui.stackedWidget_3.setCurrentIndex(1)

            elif shape_type == 'rect':


                self.ui.stackedWidget_3.setCurrentIndex(1)
            self.ui.set_stetting_page_label_info(info)
            #--------------------------------------------------------------------------------------
            if self.ui.is_drawing_mask_enabel():
                img = Utils.mask_viewer(img, thresh_img)
                img = self.roi_drawings['circel'].get_image(img)
                img = cvTools.draw_cnt(img, cnt, (255,0,0))
                h,w = img.shape[:2]
                img = cv2.circle(img, (w//2, h//2), 5, (0,255,0) , thickness=-1)

        self.ui.set_image_page_tool_labels(img)




    def update_image_3_top(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )

        img = np.copy(self.current_image_screw)
        json = self.screw_jasons[ direction ]
        img, mask_roi, _ = proccessings.preprocessing_top_img( img, json, direction  )
        
        if subpage_name!='none':
            #--------------------------------------------------------------------------------------
            #specific Operation
            #--------------------------------------------------------------------------------------
            thresh = self.screw_jasons[ direction ].get_thresh(page_name, subpage_name)
            noise_filter = self.screw_jasons[ direction ].get_noise_filter( page_name, subpage_name )
            inv_state = self.screw_jasons[ direction ].get_thresh_inv(page_name, subpage_name)
            circels_roi = self.screw_jasons[ direction ].get_circels_roi(page_name, subpage_name)
            min_area_lake = self.screw_jasons[ direction ].get_numerical_parm(page_name, subpage_name, 'min_area')
            
            thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
            thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
            mask_roi = cvTools.donate2mask(thresh_img.shape, circels_roi, 255)
            thresh_img = cv2.bitwise_and(thresh_img, mask_roi)
            
            lakes_cnt, lakes_ares  = cvTools.filter_area(thresh_img, min_area_lake)
            thresh_img = cvTools.polys2mask(thresh_img.shape, lakes_cnt, defualt=0)

            #------------------------------------------------------------------------------------
            if len(lakes_ares) > 0:
                info = {'min_area': lakes_ares.min(), 'max_area':lakes_ares.max()}
            else:
                info = {'min_area': 0, 'max_area':0}
            self.ui.set_stetting_page_label_info(info)
            #------------------------------------------------------------------------------------
            
            if self.ui.is_drawing_mask_enabel():
                img = Utils.mask_viewer(img, thresh_img, color=(0,0,100))
                img = self.roi_drawings['circel'].get_image(img)
                h,w = img.shape[:2]
                img = cv2.circle(img, (w//2, h//2), 5, (0,255,0) , thickness=-1)
                

       
        self.ui.set_image_page_tool_labels(img)




    def update_image_4_top(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )

        img = np.copy(self.current_image_screw)        

        json = self.screw_jasons[ direction ]
        img, mask_roi, _ = proccessings.preprocessing_top_img( img, json, direction  )
        
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        thresh = self.screw_jasons[ direction ].get_thresh(page_name, subpage_name)
        noise_filter = self.screw_jasons[ direction ].get_noise_filter( page_name, subpage_name )
        inv_state = self.screw_jasons[ direction ].get_thresh_inv(page_name, subpage_name)
        circel_roi = self.screw_jasons[ direction ].get_circels_roi(page_name, subpage_name)
        min_area_crack = self.screw_jasons[ direction ].get_numerical_parm(page_name, subpage_name, 'min_area')
        
        mask_roi = cvTools.circels2mask(mask_roi.shape, circel_roi)
        thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        cracks, cracks_area = cvTools.find_edge_crack(thresh_img, min_area_crack, 10 )
        
        #------------------------------------------------------------------------------------
        if len(cracks) > 0:
            info = {'min_area': cracks_area.min(), 'max_area':cracks_area.max()}
        else:
            info = {'min_area': 0, 'max_area':0}
        self.ui.set_stetting_page_label_info(info)
        #------------------------------------------------------------------------------------
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(100,0,0))
            h,w = img.shape[:2]
            img = cv2.circle(img, (w//2, h//2), 5, (0,255,0) , thickness=-1)
            img = cv2.drawContours(img, cracks, -1, (0,0,255), thickness=-1)
            img = self.roi_drawings['circel'].get_image(img)

        
        self.ui.set_image_page_tool_labels(img)


    

    def update_image_5_top(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw)

        json = self.screw_jasons[ direction ]
        img, mask_roi, _ = proccessings.preprocessing_top_img( img, json, direction  )
        
        if subpage_name!='none':
            #---------1-----------------------------------------------------------------------------
            #specific Operation
            #--------------------------------------------------------------------------------------
            sub_thresh_imgs = proccessings.get_general_masks(img, self.screw_jasons[ direction ], page_name )
            thresh_img = sub_thresh_imgs[subpage_name]
            
            
            cnts = []
            centers = []
            dist = -1
            #------------------------------------------------------------------------------------
            if len(self.screw_jasons[ direction ].get_subpages(page_name)) == 2:
                masks = list(sub_thresh_imgs.values())
                cnts, centers, dist = cvTools.centerise_measurment(masks)
            
            info = {'distance_centers': dist}    
            self.ui.set_stetting_page_label_info(info)
            #------------------------------------------------------------------------------------
            
            if self.ui.is_drawing_mask_enabel():

                img = Utils.mask_viewer(img, thresh_img, color=(0,0,100))
                h,w = img.shape[:2]
                img = cv2.circle(img, (w//2, h//2), 5, (0,255,0) , thickness=-1)

                if len(cnts)>0:
                    img = cv2.drawContours(img, cnts, -1, (0,0,255), thickness=3)
                    for center in centers:
                        img = cv2.circle(img, center, 3, (0,0,255) , thickness=-1)

                img = self.roi_drawings['circel'].get_image(img)

        self.ui.set_image_page_tool_labels(img)
    #____________________________________________________________________________________________________________
    #                                           
    #
    #                                          Image Drawings Function
    #                                                   SIDE
    #
    #____________________________________________________________________________________________________________
    def update_image_1_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        
        img = np.copy(self.current_image_screw)

        ####CHange
        thresh = self.screw_jasons[ direction ].get_thresh(page_name, subpage_name)
        #thresh_min = self.screw_jasons[ direction ].get_thresh_min(page_name, subpage_name)
        #thresh_max = self.screw_jasons[ direction ].get_thresh_max(page_name, subpage_name)


        noise_filter = self.screw_jasons[ direction ].get_noise_filter( page_name, subpage_name )
        rect = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name)
        inv_state = self.screw_jasons[ direction ].get_thresh_inv(page_name, subpage_name)
        
        img = cvTools.preprocess(img)

        mask_roi = cvTools.rects2mask(img.shape[:2], [rect])

        ####Change
        thresh_img = cvTools.threshould(img, thresh, mask_roi, inv_state)
        #thresh_img = cvTools.threshould_minmax(img, thresh_min, thresh_max, mask_roi)
        #########################

        thresh_img = cvTools.filter_noise_area(thresh_img, noise_filter)
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img)
        img = self.rect_roi_drawing.get_image(img)
        
        if Utils.is_rect( rect ) and np.count_nonzero(thresh_img) > 100:
            self.ui.enable_bar_btn_tool_page( direction, True )
        else:
            self.ui.enable_bar_btn_tool_page( direction, False )
        
        self.ui.set_image_page_tool_labels(img)
    
    
    
    def update_image_2_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw)
        
        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_side_img( img, json, direction  )
        
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(50,100,0))
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        rect_roi_2 = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name)
        if Utils.is_rect(rect_roi_2):
            left_pts, right_pts = cvTools.find_vertical_edges(thresh_img, rect_roi_2)
            if len(left_pts) > 0 and len(right_pts) > 0:
                img = cvTools.draw_vertical_point( img , [left_pts, right_pts], color=(0,0,255), thicknes=5 )
                #--------------------------------------------------------------------------------------
                #specific Operation
                #--------------------------------------------------------------------------------------
                min_dist, max_dist, avg_dist, _ = mathTools.horizontal_distance( left_pts, right_pts )

                info = {'min_lenght' : min_dist, 'max_lenght': max_dist, 'avg_lenght': avg_dist}                
                self.ui.set_stetting_page_label_info(info)
                
        img = self.rect_roi_drawing.get_image(img)
        self.ui.set_image_page_tool_labels(img)
        
        
    
    
    def update_image_3_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw)

        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_side_img( img, json, direction  )

        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(200,200,0))
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        rect_roi_2 = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name)
        jump_thresh = self.screw_jasons[ direction ].get_numerical_parm(page_name, subpage_name, 'jump_thresh')
        if Utils.is_rect(rect_roi_2):
            male_thread_h, male_thread_l = cvTools.find_screw_thread_top( thresh_img, rect_roi_2,  min_diff=jump_thresh)
            
            min_d,max_d, avg_d,_ = mathTools.vertical_distance( male_thread_h, male_thread_l )
            _,_,avg_l,_  = mathTools.thread_lenght( male_thread_h )

            info = {'thread_lenght': avg_l,  'count_thread':len(male_thread_h) , 'step_distance':avg_d}
            self.ui.set_stetting_page_label_info(info)
            
            img = cvTools.draw_points(img, male_thread_h, (0,50,150), 5)
            img = cvTools.draw_points(img, male_thread_l, (200,0,200), 5)
        

        img = self.rect_roi_drawing.get_image(img)
        self.ui.set_image_page_tool_labels(img)
        
        

        
    def update_image_4_side(self):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw)

        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_side_img( img, json, direction  )
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(100,30,0))

                
        if subpage_name!='none':
            #--------------------------------------------------------------------------------------
            #specific Operation
            #--------------------------------------------------------------------------------------
            rect_roi_2 = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name)
            if Utils.is_rect(rect_roi_2):
                left_pts, right_pts = cvTools.find_horizental_edges( thresh_img, rect_roi_2)
                if len(left_pts) > 0 and len(right_pts) > 0:
                    img = cvTools.draw_horizental_point( img, [left_pts, right_pts], (0,0,255), thicknes=5 )

                    min_dist, max_dist, avg_dist, _ = mathTools.vertical_distance( left_pts, right_pts )
                    #print(min_dist, max_dist, avg_dist)
                    info = {'min_diameter' : min_dist, 'max_diameter': max_dist, 'avg_diameter': avg_dist}                
                    self.ui.set_stetting_page_label_info(info)       

        img = self.rect_roi_drawing.get_image(img)
        self.ui.set_image_page_tool_labels(img)




    def update_image_5_side(self,):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw)

        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_side_img( img, json, direction  )

        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(50,30,200))

        
        #--------------------------------------------------------------------------------------
        #specific Operation
        #--------------------------------------------------------------------------------------
        rect_roi_2 = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name, )
        jump_thresh = self.screw_jasons[ direction ].get_numerical_parm(page_name, subpage_name, 'jump_thresh')
        edge_direction = self.screw_jasons[ direction ].get_multi_option( page_name, subpage_name, 'edge_direction' )
        from_belt = self.screw_jasons[ direction ].get_checkbox( page_name, subpage_name, 'from_belt')
        print('belt', from_belt)
        print(edge_direction)

        if Utils.is_rect(rect_roi_2):
            left_pts, right_pts = cvTools.find_head_vertival_pts(thresh_img, rect_roi_2, jump_thresh, 0.25, side=edge_direction , from_belt=from_belt)
            if len(left_pts) > 0 and len(right_pts) > 0:
                img = cvTools.draw_vertical_point( img, [left_pts, right_pts], (50,255,0), thicknes=5 )
                img[ rect_roi_2[0][1]:rect_roi_2[1][1], left_pts[0,0] ] =  (50,255,0) #draw full line
                min_dist, max_dist, avg_dist, _ = mathTools.horizontal_distance( left_pts, right_pts )

                info = {'min_head_height' : min_dist, 'max_head_height': max_dist, 'avg_head_height': avg_dist}                
                self.ui.set_stetting_page_label_info(info)           
        

        img = self.rect_roi_drawing.get_image(img)
        self.ui.set_image_page_tool_labels(img)




    def update_image_6_side(self,):
        page_name = self.ui.get_setting_page_idx(page_name = True)
        direction = self.ui.get_setting_page_idx(direction = True)
        subpage_name = self.ui.get_sub_page_name( page_name )
        
        img = np.copy(self.current_image_screw)


        json = self.screw_jasons[ direction ]
        img, thresh_img, _ = proccessings.preprocessing_side_img( img, json, direction  )
        
        if self.ui.is_drawing_mask_enabel():
            img = Utils.mask_viewer(img, thresh_img, color=(100,200,50))

        if subpage_name!='none':
            #--------------------------------------------------------------------------------------
            #specific Operation
            #--------------------------------------------------------------------------------------
            rect_roi_2 = self.screw_jasons[ direction ].get_rect_roi( page_name, subpage_name, )
            if Utils.is_rect(rect_roi_2):
                area = cvTools.get_bigest_area( thresh_img, rect_roi_2 )
                info = {'area': area}
                self.ui.set_stetting_page_label_info(info)
                
                rect_roi_2_mask = cvTools.rects2mask( img.shape[:2], [rect_roi_2] )
                select_mask = cv2.bitwise_and(rect_roi_2_mask, thresh_img)
                img = Utils.mask_viewer(img, select_mask, color=(0,10,250))

        img = self.rect_roi_drawing.get_image(img)
        self.ui.set_image_page_tool_labels(img)
