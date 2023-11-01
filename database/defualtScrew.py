from database.screwDB import screwJson

DEFAULTS_PAGE = {
            '0_top':{
                    'lbelt':100,
                    'rbelt':500,
                    'angle':0,
                    
                },
            
            '1_top':
            {   
                "algo": "thresh_algo",
                'rect_roi0': [[0,0], [100,100]],
                'thresh_min0':0,
                'thresh_max0':255,
                "d_parm1": 0,
                "e_parm2": 0,
                "d_parm3": 0,
                "e_parm4": 0,
                "edge_thresh": 5,
                'belt_edge_margin':0,
                'noise_filter0': 5,
            },

            '2_top':
            {
                "circels_roi": [ [ [100,100], 50 ]],
                "noise_filter0": 5,
                "shape_type": "circel",
                "thresh_max0": 255,
                "thresh_min0": 0


            },

            '3_top':
            {
                "circels_roi": [ [ [100,100], 50 ],[[100,100],30]],
                "noise_filter0": 5,
                "min_area": 10,
                "thresh_max0": 255,
                "thresh_min0": 0

            },
            '4_top':
            {
                "noise_filter0": 5,
                "thresh_max0": 255,
                "thresh_min0": 0
            },
            '5_top':
            {
                "sub_pages": ["Head","Flanch"],
                # "thresh_max0": 250,
                # "thresh_min0": 20,
                # "noise_filter0": 5,
            },

    #---------------------------------------------------
            '1_side':
            {
                'rect_roi0': [[0,0], [100,100]],
                'thresh0': 0,
                'thresh_inv0': True,
                'noise_filter0':0,
            },


            '2_side':
            {
                'rect_roi0': [[0,0], [100,100]],
            },

            '3_side':
            {
                'rect_roi0': [[0,0], [100,100]],
                'jump_thresh':5,
                'navel_lenght': False
            },

            '4_side':
            {
                'rect_roi0': [[0,0], [100,100]],
            },

            '5_side':
            {   
                'rect_roi0': [[0,0], [100,100]],
                "edge_direction": "top",
                "from_belt": True,
                'jump_thresh' : 10,

            },

            '6_side':
            {
                'rect_roi0': [[0,0], [100,100]],

            },
        
}






def set_default_single_page( json:screwJson, page_name:str, subpage_name):
    for featur_name, value in DEFAULTS_PAGE[page_name].items():
        #print(featur_name)
        if 'rect_roi' in featur_name:
            json.set_rect_roi(page_name, subpage_name, value[0], value[1])
        
        elif 'circels_roi' in featur_name:
            json.set_circels_roi(page_name, subpage_name, value)

        elif 'sub_pages' in featur_name:
            print(value)
            for sub_page in value:
                json.add_subpage(page_name,sub_page)

        else:
            json.set_value(page_name, subpage_name, featur_name, value)

    
        


def set_default_all_page(json:screwJson,):
    for page_name in DEFAULTS_PAGE.keys():
        if page_name in ['2_top','3_top','4_top', '4_side', '6_side']:
            subpage_name = 'none'
        else:
            subpage_name = None
        set_default_single_page(json, page_name, subpage_name)
   