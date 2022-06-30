#################################
#//////////////////////////////
#
#   {btn,bar,line,spin}_objname{count}_pagenum_{top or side}
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
#//////////////////////////////
################################



def object_dict_builder(ui_object):

    self=ui_object

    self.multi_options = {
        '2_top':
        {
            'shape_type':
            {
                'options':{
                    'circel': self.check_circle_2_top,
                    'rect': self.check_rect_2_top,
                    'hexagonal': self.check_hexagonal_2_top,
                },
                'frame':
                {
                    'obj':self.frame_54,
                    'size':50,
                },
            },
        },


        '5_side':
        {
            'edge_direction':
            {
                'options':{
                    'top': self.btn_top_5_side,
                    'bottom': self.btn_bottom_5_side,
                },
                'frame':
                {
                    'obj':self.frame_54,
                    'size':50,
                },
            },
        }


        
    }



    self.sliders={
        'thresh':{
            'bar_thresh0_1_top':self.bar_thresh0_1_top,
            'bar_thresh0_2_top':self.bar_thresh0_2_top,
            'bar_thresh0_3_top':self.bar_thresh0_3_top,
            'bar_thresh0_1_side': self.bar_thresh0_1_side,
            'bar_thresh0_2_side': self.bar_thresh0_2_side,
            'bar_thresh0_3_side': self.bar_thresh0_3_side,
            'bar_thresh0_4_side': self.bar_thresh0_4_side,
            'bar_thresh0_5_side': self.bar_thresh0_5_side,
            'bar_thresh0_6_side': self.bar_thresh0_6_side,
        },
        'noise_filter':{
            'bar_noise_filter0_1_top':self.bar_noise_filter0_1_top,
            'bar_noise_filter0_2_top':self.bar_noise_filter0_2_top,
            'bar_noise_filter0_3_top':self.bar_noise_filter0_3_top,
            'bar_noise_filter0_1_side':self.bar_noise_filter0_1_side,
        }
        
    }
    self.spins={
        'roi':
            {
                'x1':
                {
                    'spin_roi_x1_1_top': self.spin_roi_x1_1_top , 
                    'spin_roi_x1_1_side': self.spin_roi_x1_1_side,
                    'spin_roi_x1_2_side' : self.spin_roi_x1_2_side,
                    'spin_roi_x1_3_side' : self.spin_roi_x1_3_side,
                    'spin_roi_x1_4_side' : self.spin_roi_x1_4_side,
                    'spin_roi_x1_5_side' : self.spin_roi_x1_5_side,
                    'spin_roi_x1_6_side' : self.spin_roi_x1_6_side,
                    
                },
                'x2':
                {
                    'spin_roi_x2_1_top': self.spin_roi_x2_1_top , 
                    'spin_roi_x2_1_side': self.spin_roi_x2_1_side ,
                    'spin_roi_x2_2_side' : self.spin_roi_x2_2_side,
                    'spin_roi_x2_3_side' : self.spin_roi_x2_3_side,
                    'spin_roi_x2_4_side' : self.spin_roi_x2_4_side,
                    'spin_roi_x2_5_side' : self.spin_roi_x2_5_side,
                    'spin_roi_x2_6_side' : self.spin_roi_x2_6_side,
                },
                'y1':
                {
                    'spin_roi_y1_1_top': self.spin_roi_y1_1_top , 
                    'spin_roi_y1_1_side': self.spin_roi_y1_1_side,
                    'spin_roi_y1_2_side' : self.spin_roi_y1_2_side,
                    'spin_roi_y1_3_side' : self.spin_roi_y1_3_side,
                    'spin_roi_y1_4_side' : self.spin_roi_y1_4_side,
                    'spin_roi_y1_5_side' : self.spin_roi_y1_5_side,
                    'spin_roi_y1_6_side' : self.spin_roi_y1_6_side,
                },
                'y2':
                {
                    'spin_roi_y2_1_top': self.spin_roi_y2_1_top ,
                    'spin_roi_y2_1_side': self.spin_roi_y2_1_side,
                    'spin_roi_y2_2_side' : self.spin_roi_y2_2_side,
                    'spin_roi_y2_3_side' : self.spin_roi_y2_3_side,
                    'spin_roi_y2_4_side' : self.spin_roi_y2_4_side,
                    'spin_roi_y2_5_side' : self.spin_roi_y2_5_side,
                    'spin_roi_y2_6_side' : self.spin_roi_y2_6_side,
                }
            },
            
        'circle_roi':{

            'x':{
                'spin_roi_x1_3_top' : self.spin_roi_x1_3_top,
                'spin_roi_x2_3_top' : self.spin_roi_x2_3_top
            },

            'y':{
                'spin_roi_y1_3_top' : self.spin_roi_y1_3_top,
                'spin_roi_y2_3_top' : self.spin_roi_y2_3_top
            },

            'r':{
                'spin_roi_r1_3_top' : self.spin_roi_r1_3_top,
                'spin_roi_r2_3_top' : self.spin_roi_r2_3_top
            }

        },    
            
        'limit':{
            
            'min':{

                '2_top':
                {
                    'spin_min_diameter_2_top': self.spin_min_diameter_2_top,
                    'spin_min_district_2_top': self.spin_min_district_2_top,
                    'spin_min_corner_2_top': self.spin_min_corner_2_top
                },
                
                '2_side':{
                    'spin_min_lenght_2_side':self.spin_min_lenght_2_side,
                },
                
                '3_side':{
                    'spin_min_thread_lenght_3_side':self.spin_min_thread_lenght_3_side,
                    'spin_min_thread_count_3_side':self.spin_min_thread_count_3_side,
                    'spin_min_thread_distance_3_side':self.spin_min_thread_distance_3_side,
                },
                
                '4_side':{
                    'spin_min_body_diameter_4_side':self.spin_min_body_diameter_4_side,    
                    
                },

                '6_side':{
                    'spin_min_damage_6_side':self.spin_min_damage_6_side,    
                    
                },   




            },
            'max':{

                '2_top':
                {
                    'spin_max_diameter_2_top': self.spin_max_diameter_2_top,
                    'spin_max_district_2_top': self.spin_max_district_2_top,
                    'spin_max_corner_2_top': self.spin_max_corner_2_top
                },
                
                '2_side':{
                    'spin_max_lenght_2_side':self.spin_max_lenght_2_side,
                },
                
                '3_side':{
                    'spin_max_thread_lenght_3_side':self.spin_max_thread_lenght_3_side,
                    'spin_max_thread_count_3_side':self.spin_max_thread_count_3_side,
                    'spin_max_thread_distance_3_side':self.spin_max_thread_distance_3_side,
                },
                
                '4_side':{
                'spin_max_body_diameter_4_side':self.spin_max_body_diameter_4_side,
                },

                '6_side':{
                'spin_max_damage_6_side':self.spin_max_damage_6_side,
                
                },


            }
        },


        'parms':{

            '3_top':{
            'spin_min_area_3_top':self.spin_min_area_3_top
            },
            
            '3_side':{
            'spin_jump_thresh_3_side':self.spin_jump_thresh_3_side
            },
        
            '5_side':{
            'spin_jump_thresh_5_side':self.spin_jump_thresh_5_side
            },
        }

    }


    self.checkboxes = {

        'thresh_inv':
        {
            'checkbox_thresh_inv0_1_top': self.checkbox_thresh_inv0_1_top,
            'checkbox_thresh_inv0_2_top': self.checkbox_thresh_inv0_2_top,
            'checkbox_thresh_inv0_3_top': self.checkbox_thresh_inv0_3_top,
            'checkbox_thresh_inv0_1_side': self.checkbox_thresh_inv0_1_side,

        },
        'page':
        {
            'checkbox_page0_1_top': self.checkbox_page0_1_top,
            'checkbox_page0_2_top': self.checkbox_page0_2_top,
            'checkbox_page0_3_top': self.checkbox_page0_3_top,
            'checkbox_page0_1_side': self.checkbox_page0_1_side,
            'checkbox_page0_2_side': self.checkbox_page0_2_side,
            'checkbox_page0_3_side': self.checkbox_page0_3_side,
            'checkbox_page0_4_side': self.checkbox_page0_4_side,
            'checkbox_page0_5_side': self.checkbox_page0_5_side,
            'checkbox_page0_6_side': self.checkbox_page0_6_side,
        },
        'other':
        {
            '3_side':{
                'checkbox_navel_3_side':self.checkbox_navel_3_side,
            },
            
            '5_side':{
                'checkbox_from_belt_5_side': self.checkbox_belt_5_side,
            },
            
        },       
    }
    
    
    
    self.lines = {
        
        'img_path' :
        {
            'line_img_path0_1_side' : self.line_img_path0_1_side,
            'line_img_path0_1_top' : self.line_img_path0_1_top,
            
        },
        'add_area':
        {
            #'line_name_area0_2_top':self.line_name_region0_2_top,
            'line_name_area0_4_side':self.line_name_region0_4_side
        },
        'size':
        {
            'side':
            {
                'line_side_live_min_x':self.line_side_live_min_x,
                'line_side_live_max_x':self.line_side_live_max_x,
                'line_side_live_min_y':self.line_side_live_min_y,
                'line_side_live_max_y':self.line_side_live_max_y,
            },
            'top':
            {
                'line_top_live_min_x':self.line_top_live_min_x,
                'line_top_live_max_x':self.line_top_live_max_x,
                'line_top_live_min_y':self.line_top_live_min_y,
                'line_top_live_max_y':self.line_top_live_max_y,
            }
        }

    }
    
    
    
    
    self.buttons = {
        'set_img':
            {
                'btn_set_img0_1_top' : self.btn_set_img0_1_top,
                'btn_set_img0_1_side' : self.btn_set_img0_1_side,
            },
            
        'page':
            {
                'btn_page0_1_top': self.btn_page0_1_top,
                'btn_page0_2_top': self.btn_page0_2_top,
                'btn_page0_3_top': self.btn_page0_3_top,
                'btn_page0_1_side': self.btn_page0_1_side,
                'btn_page0_2_side': self.btn_page0_2_side,
                'btn_page0_3_side': self.btn_page0_3_side,
                'btn_page0_4_side': self.btn_page0_4_side,
                'btn_page0_5_side': self.btn_page0_5_side,
                'btn_page0_6_side': self.btn_page0_6_side,
                
            },
        'add':
            {
                #'btn_add_area0_2_top':self.btn_add_area0_2_top,
                #'btn_add_area0_4_side':self.btn_add_area0_4_side,

            },
        'remove':
            {
                #'btn_remove_area0_2_top':self.btn_remove_area0_2_top,
                #'btn_remove_area0_4_side':self.btn_remove_area0_4_side,

            }    
               
    }

    self.labels={

        'show_infoes':
            {
                '2_side':
                    {
                        'label_min_lenght_2_side':self.label_min_lenght_2_side,
                        'label_max_lenght_2_side':self.label_max_lenght_2_side,
                        'label_avg_lenght_2_side':self.label_avg_lenght_2_side,
                        
                    },
                
                '3_side':
                    {
                        'label_thread_lenght_3_side':self.label_thread_lenght_3_side,
                        'label_count_thread_3_side':self.label_count_thread_3_side,
                        'label_step_distance_3_side':self.label_step_distance_3_side,
                    },
                
                '4_side':
                    {
                        'label_min_diameter_4_side':self.label_min_diameter_4_side,
                        'label_max_diameter_4_side':self.label_max_diameter_4_side,
                        'label_avg_diameter_4_side':self.label_avg_diameter_4_side,
                    },

                
                '5_side':
                    {
                        'label_min_head_height_5_side':self.label_min_head_height_5_side,
                        'label_max_head_height_5_side':self.label_max_head_height_5_side,
                        'label_avg_head_height_5_side':self.label_avg_head_height_5_side,
                    },


                '6_side':
                {
                    'label_area_6_side': self.label_area_6_side
                },
                
                '2_top':
                {
                
                        'label_min_diameter_2_top':self.label_min_diameter_2_top,
                        'label_max_diameter_2_top':self.label_max_diameter_2_top,
                        'label_min_district_2_top':self.label_min_district_2_top,
                        'label_max_district_2_top':self.label_max_district_2_top,
                        'label_min_corner_2_top':self.label_min_corner_2_top,
                        'label_max_corner_2_top':self.label_max_corner_2_top,
                        
                        #'labe_area_district_2_top':self.labe_area_district_2_top,
                        #'labe_area_corner_2_top':self.labe_area_corner_2_top,

                        
                }
            }

    }

    self.list_packs = {
        

            
            'lp_sub_pages0_4_side': {
                'add_btn': self.btn_add_region0_4_side,
                'remove_btn': self.btn_remove_region0_4_side,
                'input': self.line_name_region0_4_side,
                'combo': self.combo_regions_name0_4_side,
                
            },
            'lp_sub_pages0_6_side': {
                'add_btn': self.btn_add_region0_6_side,
                'remove_btn': self.btn_remove_region0_6_side,
                'input': self.line_name_region0_6_side,
                'combo': self.combo_regions_name0_6_side,
                
            },
            
            'lp_sub_pages0_2_top': {
                'add_btn': self.btn_add_region0_2_top,
                'remove_btn': self.btn_remove_region0_2_top,
                'input': self.line_name_region0_2_top,
                'combo': self.combo_regions_name0_2_top,
            },

            
            'lp_sub_pages0_3_top': {
                'add_btn': self.btn_add_region0_3_top,
                'remove_btn': self.btn_remove_region0_3_top,
                'input': self.line_name_region0_3_top,
                'combo': self.combo_regions_name0_3_top,
            }

            
    }

    self.combo_boxes = {
        'live':{
            'combobox_select_screw_live':self.combobox_select_screw_live,
        }

    }
    
        

    
    self.lives={
        'labels':
        {
            'selected_img':
            {
                'side': self.label_selected_screw_side_live,
                'top' : self.label_selected_screw_top_live,
            },

            'live_img':
            {
                'side': self.label_img_side_live,
                'top':  self.label_img_top_live,
            }

        },
        'combo_boxes':
        {
            'screw_list':self.combobox_select_screw_live
        }
    }




def set_dimensions(ui_object,side_parms,top_parms):
            # f_name.setMaximumHeight(size)
            # f_name.setMinimumHeight(size)
    self=ui_object
    
    # print('parms',parms)
    self.label_img_side_live.setMinimumHeight(int(side_parms['min_x']))
    self.label_img_side_live.setMinimumWidth(int(side_parms['min_y']))
    self.label_img_side_live.setMaximumHeight(int(side_parms['max_x']))
    self.label_img_side_live.setMaximumWidth(int(side_parms['max_y']))

    self.label_img_top_live.setMinimumHeight(int(top_parms['min_x']))
    self.label_img_top_live.setMinimumWidth(int(top_parms['min_y']))
    self.label_img_top_live.setMaximumHeight(int(top_parms['max_x']))
    self.label_img_top_live.setMaximumWidth(int(top_parms['max_y']))
