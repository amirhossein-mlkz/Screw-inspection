

def create_defult_screw(ui_obj):
    self = ui_obj

    self.defaults = {

    '0_top':{
            'spin_lbelt_0_top': (self.spin_lbelt_0_top, 100),
            'spin_rbelt_0_top':(self.spin_rbelt_0_top, 200),
            'spin_angle_0_top':(self.spin_angle_0_top, 0 ),
                    
        },
    '1_top':
        {   
            
            'spin_roi_x1_1_top' : (self.spin_roi_x1_1_top,0),
            'spin_roi_y1_1_top' : (self.spin_roi_y1_1_top,0),
            'spin_roi_x2_1_top' : (self.spin_roi_x2_1_top,100),
            'spin_roi_y2_1_top' : (self.spin_roi_y2_1_top,100),


            
            'check_thresh_algo_1_top':(self.check_thresh_algo_1_top, True),
            'check_edge_algo_1_top':(self.check_edge_algo_1_top, False),

            'spin_belt_edge_margin':(self.spin_belt_edge_margin, 0),
            'bar_edge_thresh0_1_top':(self.bar_edge_thresh0_1_top, 5),
            
            'bar_thresh_max0': (self.bar_thresh_max0_1_top, 255),
            'bar_thresh_min0': (self.bar_thresh_min0_1_top, 0),
            'bar_noise_filter0': (self.bar_noise_filter0_1_top, 0),
            'spin_d_parm1':(self.spin_d_parm1_1_top, 0 ),
            'spin_e_parm2':(self.spin_e_parm2_1_top, 0 ),
            'spin_d_parm3':(self.spin_d_parm3_1_top, 0 ),
            'spin_e_parm4':(self.spin_e_parm4_1_top, 0 ),

        },


        '2_top':
        {
            'bar_thresh_max0_2_top':(self.bar_thresh_max0_2_top, 255),
            'bar_thresh_min0_2_top':(self.bar_thresh_min0_2_top, 0),
            'bar_noise_filter0_2_top':(self.bar_noise_filter0_2_top,0),
            'check_hexagonal_2_top':(self.check_hexagonal_2_top,False),
            'check_circle_2_top':(self.check_circle_2_top,True),
            'check_circle_2_top': (self.check_rect_2_top,False),
        },

        '1_side':
        {


            'spin_roi_x1_1_side' : (self.spin_roi_x1_1_side,0),
            'spin_roi_y1_1_side' : (self.spin_roi_y1_1_side,0),
            'spin_roi_x2_1_side' : (self.spin_roi_x2_1_side,100),
            'spin_roi_y2_1_side' : (self.spin_roi_y2_1_side,100),



            'bar_thresh0_1_side': (self.bar_thresh0_1_side,0),
            'bar_noise_filter0_1_side':(self.bar_noise_filter0_1_side,0),
            'checkbox_thresh_inv0_1_side': (self.checkbox_thresh_inv0_1_side,True),
            'bar_noise_filter0_1_side': (self.bar_noise_filter0_1_side,0),
        },


        '2_side':
        {
            'spin_roi_x1_2_side' : (self.spin_roi_x1_2_side,0),
            'spin_roi_y1_2_side' : (self.spin_roi_y1_2_side,0),
            'spin_roi_x2_2_side' : (self.spin_roi_x2_2_side,100),
            'spin_roi_y2_2_side' : (self.spin_roi_y2_2_side,100),
        },
        '3_side':
        {
            'spin_roi_x1_3_side' : (self.spin_roi_x1_3_side,0),
            'spin_roi_y1_3_side' : (self.spin_roi_y1_3_side,0),
            'spin_roi_x2_3_side' : (self.spin_roi_x2_3_side,100),
            'spin_roi_y2_3_side' : (self.spin_roi_y2_3_side,100),
            'spin_jump_thresh_3_side':(self.spin_jump_thresh_3_side,5),
        },
        '4_side':
        {
            'spin_roi_x1_4_side' : (self.spin_roi_x1_4_side,0),
            'spin_roi_y1_4_side' : (self.spin_roi_y1_4_side,0),
            'spin_roi_x2_4_side' : (self.spin_roi_x2_4_side,100),
            'spin_roi_y2_4_side' : (self.spin_roi_y2_4_side,100),
        },

        '5_side':
        {
            'spin_roi_x1_5_side' : (self.spin_roi_x1_5_side,0),
            'spin_roi_y1_5_side' : (self.spin_roi_y1_5_side,0),
            'spin_roi_x2_5_side' : (self.spin_roi_x2_5_side,100),
            'spin_roi_y2_5_side' : (self.spin_roi_y2_5_side,100),
            'check_top_5_side' : (self.check_top_5_side,True),
            'check_top_5_side' : (self.checkbox_belt_5_side,False),
            'spin_jump_thresh_5_side' : (self.spin_jump_thresh_5_side,10),

        },
        '6_side':
        {
            'spin_roi_x1_6_side' : (self.spin_roi_x1_6_side,0),
            'spin_roi_y1_6_side' : (self.spin_roi_y1_6_side,0),
            'spin_roi_x2_6_side' : (self.spin_roi_x2_6_side,100),
            'spin_roi_y2_6_side' : (self.spin_roi_y2_6_side,100),

        },
    }


   