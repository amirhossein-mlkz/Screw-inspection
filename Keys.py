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
                    
                },
                'x2':
                {
                    'spin_roi_x2_1_top': self.spin_roi_x2_1_top , 
                    'spin_roi_x2_1_side': self.spin_roi_x2_1_side ,
                    'spin_roi_x2_2_side' : self.spin_roi_x2_2_side,
                    'spin_roi_x2_3_side' : self.spin_roi_x2_3_side,
                },
                'y1':
                {
                    'spin_roi_y1_1_top': self.spin_roi_y1_1_top , 
                    'spin_roi_y1_1_side': self.spin_roi_y1_1_side,
                    'spin_roi_y1_2_side' : self.spin_roi_y1_2_side,
                    'spin_roi_y1_3_side' : self.spin_roi_y1_3_side,
                },
                'y2':
                {
                    'spin_roi_y2_1_top': self.spin_roi_y2_1_top ,
                    'spin_roi_y2_1_side': self.spin_roi_y2_1_side,
                    'spin_roi_y2_2_side' : self.spin_roi_y2_2_side,
                    'spin_roi_y2_3_side' : self.spin_roi_y2_3_side,
                }
            },
            
            
            
        'limit':{
            'min':{
                'spin_min_lenght_2_side':self.spin_min_lenght_2_side,
                'spin_min_lenght_3_side':self.spin_min_lenght_3_side,
                'spin_min_thread_3_side_2':self.spin_min_thread_3_side_2,
                'spin_min_distance_3_side':self.spin_min_distance_3_side,
                'spin_min_diameter_x_4_side':self.spin_min_diameter_x_4_side,
                'spin_min_diameter_y_4_side':self.spin_min_distance_3_side

            },
            'max':{
                'spin_max_lenght_2_side':self.spin_max_lenght_2_side,
                'spin_max_lenght_3_side':self.spin_max_lenght_3_side,
                'spin_max_thread_3_side_2':self.spin_max_thread_3_side,
                'spin_max_distance_3_side':self.spin_max_distance_3_side,
                'spin_max_diameter_x_4_side':self.spin_max_diameter_x_4_side,
                'spin_max_diameter_y_4_side':self.spin_max_distance_3_side
            }
        },
        'spin_best_3_side':self.spin_best_3_side

    }


    self.checkboxes = {

        'thresh_inv':
        {
            'btn_thresh_inv0_1_top': self.btn_thresh_inv0_1_top,
            'btn_thresh_inv0_2_top': self.btn_thresh_inv0_2_top,
            'btn_thresh_inv0_1_side': self.btn_thresh_inv0_1_side
        },
        'page':
        {
            'checkbox_page0_1_top': self.checkbox_page0_1_top,
            'checkbox_page0_2_top': self.checkbox_page0_2_top,
            'checkbox_page0_1_side': self.checkbox_page0_1_side,
            'checkbox_page0_2_side': self.checkbox_page0_2_side,
            'checkbox_page0_3_side': self.checkbox_page0_3_side,
            'checkbox_page0_4_side': self.checkbox_page0_4_side,
            
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
            'line_name_area0_2_top':self.line_name_area0_2_top,
            'line_name_area0_4_side':self.line_name_area0_4_side
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
                
            },
        'add':
            {
                'btn_add_area0_2_top':self.btn_add_area0_2_top,
                'btn_add_area0_4_side':self.btn_add_area0_4_side,

            },
        'remove':
            {
                'btn_remove_area0_2_top':self.btn_remove_area0_2_top,
                'btn_remove_area0_4_side':self.btn_remove_area0_4_side,

            }    
               
    }

    self.labels={

        'show_values':
            {
                'label_lenght_2_side':self.label_lenght_2_side,
                'label_min_lenght_2_side':self.label_min_lenght_2_side,
                'label_max_lenght_2_side':self.label_max_lenght_2_side,
                'label_avg_lenght_2_side':self.label_avg_lenght_2_side,
                'label_thread_lenght_3_side':self.label_thread_lenght_3_side,
                'label_count_thread_lenght_3_side':self.label_count_thread_3_side,
                'label_step_distance_lenght_3_side':self.label_step_distance_3_side,
                'label_diameter_x_4_side':self.label_diameter_x_4_side,
                'label_diameter_y_4_side':self.label_diameter_y_4_side,
            }

    }

    self.combo_boxes={
        'set_area':
        {
            'combo_set_area0_2_top':self.combo_set_area0_2_top,
            'combo_set_area0_4_side':self.combo_set_area0_4_side,

        }
    }