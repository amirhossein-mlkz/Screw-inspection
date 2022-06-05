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

    self.sliders={
        'thresh':{
            'bar_thresh0_1_top':self.bar_thresh0_1_top,
            'bar_thresh0_2_top':self.bar_thresh0_2_top,
            'bar_thresh0_1_side':self.bar_thresh0_1_side,
        },
        'noise_filter':{
            'bar_noise_filter0_1_top':self.bar_noise_filter0_1_top,
            'bar_noise_filter0_2_top':self.bar_noise_filter0_2_top,
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
            
            
            
        'limit':{
            
            'min':{
                
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
            
            '3_side':{
            'spin_best_3_side':self.spin_best_3_side,
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
            'checkbox_thresh_inv0_1_side': self.checkbox_thresh_inv0_1_side
        },
        'page':
        {
            'checkbox_page0_1_top': self.checkbox_page0_1_top,
            'checkbox_page0_2_top': self.checkbox_page0_2_top,
            'checkbox_page0_1_side': self.checkbox_page0_1_side,
            'checkbox_page0_2_side': self.checkbox_page0_2_side,
            'checkbox_page0_3_side': self.checkbox_page0_3_side,
            'checkbox_page0_4_side': self.checkbox_page0_4_side,
            'checkbox_page0_5_side': self.checkbox_page0_5_side,
            'checkbox_page0_6_side': self.checkbox_page0_6_side,
            
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
                        'label_lenght_2_side':self.label_lenght_2_side,
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
                
                # '4_side':
                #     {
                #         'label_diameter_x_4_side':self.label_diameter_x_4_side,
                #         'label_diameter_y_4_side':self.label_diameter_y_4_side,
                #     }


                '6_side':
                {
                    'label_area_6_side': self.label_area_6_side
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
                
            }
            
            
    
        

    }



    