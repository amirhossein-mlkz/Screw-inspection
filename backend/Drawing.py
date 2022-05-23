from dis import dis
from re import S
from turtle import Shape, color

import numpy as np
import cv2



COLOR_MAP = {
    'line' : (255,100,0),
    'point': (0,100,200),
    'drawing_line': (0,0,255),
    'drawing_point': (0,0,255)
}

THICKNeSS_MAP = {
    'line' : 6,
    'point' : 12,
    'drawing_line': 6,
    'drawing_point': 12
}

THRESH = 30

class drawShape:
    #______________________________________________________________________________________________________
    #args:
    #   img_size | format = (h,w)
    #______________________________________________________________________________________________________
    def __init__(self, points_count, max_shape_count=1000, color_map=COLOR_MAP, thikness_map = THICKNeSS_MAP):
        self.img_size = (640,480)
        self.points_count = points_count
        self.color_map = color_map
        self.thickness_map = thikness_map
        self.max_shape_count = max_shape_count
        
        self.count_backup = self.points_count
        self.float_point_idx = {'x':0 , 'y':0 }
        self.is_editing = False
        self.points = [] #list of points where mouse clicked 
        self.shapes = []

        self.image = self.init_image()
    
    def set_img_size(self, img_size):
        self.img_size = img_size
    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def init_image(self):
        return np.zeros(self.img_size + (3,), dtype=np.uint8)
    
    #______________________________________________________________________________________________________
    #action:
    #   append complete points into self.shapes
    #args:
    #   points  |  format=[[(int x, int y) , string 'fix' ] , ... ]
    #______________________________________________________________________________________________________
    def save_shape(self,points):

            
        decoded_shape = self.shape_decoder(points)
        self.shapes.append(decoded_shape)
        if len(self.shapes) > self.max_shape_count:
            self.shapes.pop(0)
        self.points = []
        
        
    #______________________________________________________________________________________________________
    #action:
    #   convert points to a good format for specific shape like center and radius in circle
    #args:
    #   points  |  format=[ (int x1, int y1) , (x2,y2), ... ]
    #______________________________________________________________________________________________________
    def shape_decoder(self, points):
        return points
    #______________________________________________________________________________________________________
    #action:
    #   convert normalize pt ( 0< x,y <1 ) to real pixel cordinate ( 0 < x < w , 0 < y < h )
    #args:
    #   pt  |  format=(float x, float y)
    #______________________________________________________________________________________________________
    def denormalize(self, pt):
        x,y = pt
        x, y = int( x * self.img_size[1] ), int( y * self.img_size[0])
        return x, y
        
    #______________________________________________________________________________________________________
    #action:
    #   calculate area of shapes
    #args:
    #   pt  |  format=(float x, float y)
    #______________________________________________________________________________________________________
    def area(self, shape, shapes_type):
        pass
    
    
    #______________________________________________________________________________________________________
    #action:
    #   calculate distance beetwen to points
    #args:
    #   pt1  |  format=(int x, int y)
    #   pt2  |  format=(int x, int y)
    #______________________________________________________________________________________________________
    def distance(self,pt1,pt2):
        dist = ( (pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 ) ** 0.5
        return dist
    
    
    #______________________________________________________________________________________________________
    #exp:
    #   got shape and point and return True if point be inside the shape. O.w return False
    #args:
    #
    #______________________________________________________________________________________________________
    def check_point_inside(self, pt, shape):
        return False   
    
    #______________________________________________________________________________________________________
    #action:
    #   check drawing is finsh or not. if the number of points
    #   be equal to self.points_count it means drawing is finished
    #args:
    #   None
    #return 
    #   state   | format: bool | True means drawing is finished
    #______________________________________________________________________________________________________
    def check_finish(self):
        if len(self.points) == self.points_count:
            return True
        return False
    
    
    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def click(self, pt):
        pt = self.denormalize(pt)
        
        if not self.check_editing(pt, self.shapes):
            self.add_fix_point(pt)
            
    #______________________________________________________________________________________________________
    #exp:
    #   add fix point in self.points if it is empty or
    #   replace fix point instead of float point if self.points is not full yet
    #args:
    #   pt  |  format=(float x, float y)
    #______________________________________________________________________________________________________
    def add_fix_point(self, pt):
        x,y = pt
                
        #first point shoud be fix point
        if len( self.points ) == 0:
            self.points_count = self.count_backup
            self.points.append([x,y])#this point is fix
        
        # if there are more than one points,and there is one float point
        # we replace fix point instead of it
        elif self.float_point_idx['x'] is not None:
            self.points[ self.float_point_idx['x'] ][0] = x
            self.points[ self.float_point_idx['y'] ][1] = y
        
        #check finish drawing condition
        if self.check_finish():
            #if drawing is finished we save shape and make self.points empty
            self.save_shape(self.points)
            self.points = []
        
        else:
            #if drawing need conitune, we set float point idx equal to last index for both x and y
            self.float_point_idx['x'] = -1
            self.float_point_idx['y'] = -1
            self.points.append([x,y])#this point reserved for float point

            

    
    #______________________________________________________________________________________________________
    #exp:
    #   set float point
    #args:
    #   pt  |  format=(float x, float y)
    #______________________________________________________________________________________________________
    def set_float_point(self, pt):
        x,y = self.denormalize(pt)
        if len(self.points) > 1:
            self.points[ self.float_point_idx['x'] ][0] = x
            self.points[ self.float_point_idx['y'] ][1] = y
        
    
    
    
    #______________________________________________________________________________________________________
    #action:
    #   check click is for editing shapes or add new point
    #args:
    #   None
    #return 
    #   state   | format: bool | True means drawing is finished
    #______________________________________________________________________________________________________
    def check_editing(self, pt, shapes, thresh=THRESH):
        return False
    
    
    # def editing(self, pt):
    #     pt = self.denormalize(pt)
    #     if len(self.points) == 0 and self.is_editing == False:
    #         for shape in self.shapes:
    #             state, info = self.editing_condition(pt, shape)
                
    #         print( self.check_is_editing(pt, self.shapes))
        
    
    #______________________________________________________________________________________________________
    #exp:
    #   return list of coordinate of points
    #args:
    #  None
    #return:
    #   return list of points | format: list [(x1,y1), (x2,y2)]
    #______________________________________________________________________________________________________
    def get_points(self):
        res = []
        for pt in self.points:
            res.append(pt)
        return res
    #______________________________________________________________________________________________________
    #exp:
    #   remove last fix point from self.points and if self.points contain at least one point,
    #   add float point in self.points
    #args:
    #   pt  |  format=(float x, float y)
    #______________________________________________________________________________________________________
    def remove_last_point(self, pt):
        pt = self.denormalize(pt)
        remove_done = False
        while not remove_done and len(self.points)>0:
            if self.points[-1][1] == 'fix':
                remove_done = True
            self.points.pop()

        if len(self.points) > 0:
            self.points.append([pt, 'float'])
        
    
    #______________________________________________________________________________________________________
    #exp:
    #   got point and if the point be inside of one shape, remove that
    #args: 
    #   pt | format: (x,y)
    # ______________________________________________________________________________________________________
    def remove_shape(self, pt):
        #check we don't drawing
        pt = self.denormalize(pt)
        #if point be inside of more than one shape, we wanna remove smallest one
        self.shapes.sort(key=lambda x:self.area(x))
        
        for i in range(len(self.shapes)):
            if self.check_point_inside(pt, self.shapes[i]):
                self.shapes.pop(i)
                break
                
    
    
    #______________________________________________________________________________________________________
    #exp:
    #   check if we are drawing, delete point, O.w delete shape
    #args: 
    #   pt | format: (x,y)
    # ______________________________________________________________________________________________________
    def remove_points_or_shape(self,pt):
        if len(self.points) == 0:
            self.remove_shape(pt)
        
        else:
            self.remove_last_point(pt)
    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def draw_points(self, img, points, color=(0,255,0) , radius=5):
        for pt in points:
            cv2.circle( img, tuple(pt) , radius , color , thickness=-1 )
        return img



    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def draw_shapes(self):
        pass


    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def draw_points_as_shape(self):
        pass
    
    
    #______________________________________________________________________________________________________
    #
    #______________________________________________________________________________________________________
    def draw_corners(self):
        pass
    
    
    
    def get_image(self, image=None):

        if image is None:
            image = self.init_image()
        image = self.draw_points_as_shape(image, 
                                            self.points,
                                            line_color=self.color_map['drawing_line'],
                                            point_color=self.color_map['drawing_point'],
                                            line_thickness=self.thickness_map['drawing_line'],
                                            point_thickness=self.thickness_map['drawing_point'])
        
 
        image = self.draw_shapes(  image,
                                    self.shapes,
                                    line_color=self.color_map['line'],
                                    point_color=self.color_map['point'],
                                    line_thickness=self.thickness_map['line'],
                                    point_thickness=self.thickness_map['point'])
        return image
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------


class drawCircel(drawShape):
    
    def __init__(self, img_size, color_map=COLOR_MAP, thikness_map = THICKNeSS_MAP):
        points_count = 2
        drawShape.__init__(self, points_count, color_map=color_map, thikness_map = thikness_map)   
    

    #______________________________________________________________________________________________________
    #exp:
    #   calculate area
    #args
    #   shape  | format: ( center, radius )
    #______________________________________________________________________________________________________
    def area(self, shape):
        center, radius = shape
        return np.pi * radius**2
    
    #______________________________________________________________________________________________________
    #exp:
    #   got shape and point and return True if point be inside the shape. O.w return False
    #args'
    #   pt     | format: (x,y)
    #   shape  | format: ( center, radius )
    #______________________________________________________________________________________________________
    def check_point_inside(self, pt, shape):
        center , radius = shape
        dist = self.distance( center, pt)
        if dist<=radius:
            return True
        return False    
    #______________________________________________________________________________________________________
    #exp:
    #   convert points into radius and center for circle
    #args
    #   points  | format: [(int x1, int y1), (x2, y2), ....]
    #______________________________________________________________________________________________________
    def shape_decoder(self,points):
        cx,cy = points[0]
        arc_x, arc_y = points[1]
        radius = ((arc_x-cx)**2 + (arc_y-cy)**2)**0.5
        radius = int(radius)
        return (cx,cy), radius
    
    
    #______________________________________________________________________________________________________
    #exp:
    #   convert circel into to points
    #args
    #   shape  | format: ((cx,cy) , radius)
    #______________________________________________________________________________________________________
    def shape_encoder(self,shape):
        center, radius = shape
        cx,cy = center
        pt1 = [cx,cy]
        pt2 = [cx,cy + radius]
        
        points = [pt1,pt2]
        return points
    
        
    #______________________________________________________________________________________________________
    #action:
    #   check click is for editing shapes or add new point
    #args:
    #   None
    #return 
    #   state   | format: bool | True means drawing is finished
    #______________________________________________________________________________________________________
    def check_editing(self, pt, shapes, thresh=THRESH):
        for shape in shapes:
            center, radius = shape
            r2 = self.distance( center , pt)
            dist = abs(radius - r2)
            if dist < thresh:
                #for edit radius in circle we should edit second point
                self.float_point_idx['x'] = 1
                self.float_point_idx['y'] = 1
                self.points = self.shape_encoder(shape)
                self.points[1] = list(pt)
                self.shapes.remove(shape)
                return True
        return False
            
            
            
    #______________________________________________________________________________________________________
    #args: 
    #   drawing shapes
    #args:
    #   img: input image
    #   shapes  | format = [((cx,cy), radius), ((,),) , ....]
    #   color: color of shape
    #______________________________________________________________________________________________________
    def draw_shapes(self, img, shapes, line_color=(255,0,0), point_color=(0,255,100) , line_thickness=3, point_thickness=6):
        res = np.copy(img)
        for shape in shapes:
            center, radius = shape
            res = cv2.circle( img, center, radius, line_color, thickness=line_thickness)
        return res
    
        #______________________________________________________________________________________________________
    #exp:
    #   convert circel into to points
    #args
    #   shape  | format: ((cx,cy) , radius)
    #______________________________________________________________________________________________________
    def shape_encoder(self,shape):
        center, radius = shape
        cx,cy = center
        pt1 = [cx,cy]
        pt2 = [cx,cy + radius]
        
        points = [pt1,pt2]
        return points
    
        
    #______________________________________________________________________________________________________
    #action:
    #   check click is for editing shapes or add new point
    #args:
    #   None
    #return 
    #   state   | format: bool | True means drawing is finished
    #______________________________________________________________________________________________________
    def check_editing(self, pt, shapes, thresh=THRESH):
        for shape in shapes:
            center, radius = shape
            r2 = self.distance( center , pt)
            dist = abs(radius - r2)
            if dist < thresh:
                #for edit radius in circle we should edit second point
                self.float_point_idx['x'] = 1
                self.float_point_idx['y'] = 1
                self.points = self.shape_encoder(shape)
                self.points[1] = list(pt)
                self.shapes.remove(shape)
                return True
        return False
    #______________________________________________________________________________________________________
    #args: 
    #   drawing points as shape shapes
    #args:
    #   img: input image
    #   points  | foramt: [(x1,y1) ,(x2,y2), ...]
    #______________________________________________________________________________________________________
    def draw_points_as_shape(self, img, points, line_color=(255,0,0), point_color=(0,255,100) , line_thickness=3, point_thickness=6):
        if len(points) == self.points_count:
            shape = self.shape_decoder(points)
            return self.draw_shapes(img, [shape], line_color, point_color, line_thickness, point_thickness)
        
        else:
            return img
        
        










class drawRect(drawShape):
    
    def __init__(self, color_map=COLOR_MAP, thikness_map = THICKNeSS_MAP):
        points_count = 2
        drawShape.__init__(self, points_count, color_map=color_map, thikness_map = thikness_map)   
    

    
    #______________________________________________________________________________________________________
    #exp:
    #   calculate area
    #args
    #   shape  | format: [ pt1, pt2 ]
    #______________________________________________________________________________________________________
    def area(self, shape):
        pt1,pt2 = shape
        w = abs( pt2[0] - pt1[0] )
        h = abs( pt2[1] - pt1[1] )
        return w*h
    #______________________________________________________________________________________________________
    #exp:
    #   got shape and point and return True if point be inside the shape. O.w return False
    #args'
    #   pt     | format: (x,y)
    #   shape  | format: ( center, radius )
    #______________________________________________________________________________________________________
    def check_point_inside(self, pt, shape):
        (min_x,min_y) , (max_x,max_y) = shape
        if min_x < pt[0] < max_x and min_y < pt[1] < max_y:
            return True
        return False    
    #______________________________________________________________________________________________________
    #exp:
    #   convert points into [(minx,miny),(max,maxy)]
    #args
    #   points  | format: [(int x1, int y1), (x2, y2), ....]
    #______________________________________________________________________________________________________
    def shape_decoder(self,points):
        minx = min( points[0][0], points[1][0] )
        maxx = max( points[0][0], points[1][0] )
        miny = min( points[0][1], points[1][1] )
        maxy = max( points[0][1], points[1][1] )
        return [[minx,miny],[maxx, maxy]]
    
        
        
    #______________________________________________________________________________________________________
    #exp:
    #   convert circel into to points
    #args
    #   shape  | format: ((cx,cy) , radius)
    #______________________________________________________________________________________________________
    def shape_encoder(self,shape):
        return shape
    
        
    #______________________________________________________________________________________________________
    #action:
    #   check click is for editing shapes or add new point
    #args:
    #   None
    #return 
    #   state   | format: bool | True means drawing is finished
    #______________________________________________________________________________________________________
    def check_editing(self, pt, shapes, thresh=THRESH):
        for shape in shapes:
            
            for i in range(2):
                for j in range(2):
                    corner = shape[i][0], shape[j][1]
                    dist = self.distance( corner , pt)
                    if dist < thresh:
                        #for edit radius in circle we should edit second point
                        self.float_point_idx['x'] = i
                        self.float_point_idx['y'] = j
                        self.points = self.shape_encoder(shape)
                        self.shapes.remove(shape)
                        return True
        return False
            
            
    #______________________________________________________________________________________________________
    #args: 
    #   drawing shapes
    #args:
    #   img: input image
    #   shapes  | format = [[pt1,pt2] , [,] , ...
    #   color: color of shape
    #______________________________________________________________________________________________________
    def draw_shapes(self, img, shapes, line_color=(255,0,0), point_color=(0,255,100) , line_thickness=3, point_thickness=6):
        res = np.copy(img)
        for shape in shapes:
            pt1, pt2 = shape
            res = cv2.rectangle( img, pt1, pt2, line_color, thickness=line_thickness)
            
            #draw corner
            for i in range(2):
                for j in range(2):
                    res = cv2.circle(res, (shape[i][0], shape[j][1]), point_thickness, point_color, thickness=-1)
        return res
    
    
    #______________________________________________________________________________________________________
    #args: 
    #   drawing points as shape shapes
    #args:
    #   img: input image
    #   points  | foramt: [(x1,y1) ,(x2,y2), ...]
    #______________________________________________________________________________________________________
    def draw_points_as_shape(self, img, points, line_color=(255,0,0), point_color=(0,255,100) , line_thickness=3, point_thickness=6):
        if len(points) == self.points_count:
            shape = self.shape_decoder(points)
            return self.draw_shapes(img, [shape], line_color, point_color, line_thickness, point_thickness)
        
        else:
            return img











class drawPath(drawShape):
    
    def __init__(self, img_size,points_count = np.inf, color_map=COLOR_MAP, thikness_map = THICKNeSS_MAP):
        drawShape.__init__(self, points_count, color_map=color_map, thikness_map = thikness_map) 
        #self.buffer = self.points_count

    
    #______________________________________________________________________________________________________
    #exp:
    #   calculate area
    #args
    #   shape  | format: ( center, radius )
    #______________________________________________________________________________________________________
    def distance_point_from_path(self, shape, pt):
        dists = []
        pt = np.array(pt)
        for i in range( len(shape) - 1):
            pt1 = np.array(shape[ i ])
            pt2 = np.array(shape[ i + 1 ])
            d = np.linalg.norm(np.cross(pt2-pt1, pt1-pt))/np.linalg.norm(pt2-pt1)
            dists.append(d)
        return np.array(dists).min()
    
            
            
    #______________________________________________________________________________________________________
    #exp:
    #   got point and if the point be inside of one shape, remove that
    #args: 
    #   pt | format: (x,y)
    # ______________________________________________________________________________________________________
    def remove_shape(self, pt):
        if len(self.shapes) > 0:
            #check we don't drawing
            pt = self.denormalize(pt)
            #if point be inside of more than one shape, we wanna remove smallest one
            self.shapes.sort(key=lambda x:self.distance_point_from_path(x, pt))
            
            if self.distance_point_from_path(self.shapes[0], pt) < 15:
                self.shapes.pop(0)
                    
    
    #______________________________________________________________________________________________________
    #action:
    #   check drawing is finsh or not. if the number of points
    #   be equal to self.points_count it means drawing is finished
    #args:
    #   None
    #return 
    #   state   | format: bool | True means drawing is finished
    #______________________________________________________________________________________________________
    def check_finish(self):
        if len(self.points) == self.points_count:
            return True
        if len(self.points)>=2 and self.distance( self.points[-1] , self.points[-2] ) < 30:
            return True
        return False
    #______________________________________________________________________________________________________
    #exp:
    #   nothing do
    #args
    #   points  | format: [(int x1, int y1), (x2, y2), ....]
    #______________________________________________________________________________________________________
    def shape_decoder(self,points):
        if len(self.points)>=3 and self.distance( self.points[-1] , self.points[-2] ) < 30:
            points.pop()
        return points
            
    
    
    #______________________________________________________________________________________________________
    #exp:
    #   convert circel into to points
    #args
    #   shape  | format: ((cx,cy) , radius)
    #______________________________________________________________________________________________________
    def shape_encoder(self,shape):
        return shape
    
        
    #______________________________________________________________________________________________________
    #action:
    #   check click is for editing shapes or add new point
    #args:
    #   None
    #return 
    #   state   | format: bool | True means drawing is finished
    #______________________________________________________________________________________________________
    def check_editing(self, pt, shapes, thresh=THRESH):
        for shape in shapes:
            for i,corner in enumerate(shape):
                dist = self.distance( corner , pt)
                if dist < thresh:
                    #for edit radius in circle we should edit second point
                    self.float_point_idx['x'] = i
                    self.float_point_idx['y'] = i
                    self.points = self.shape_encoder(shape)
                    self.shapes.remove(shape)
                    self.count_backup = self.points_count
                    return True
        return False
            
    #______________________________________________________________________________________________________
    #args: 
    #   drawing shapes
    #args:
    #   img: input image
    #   shapes  | format = [((cx,cy), radius), ((,),) , ....]
    #   color: color of shape
    #______________________________________________________________________________________________________
    def draw_shapes(self, img, shapes, line_color=(255,0,0), point_color=(0,255,100) , line_thickness=3, point_thickness=6):
        res = np.copy(img)
        for shape in shapes:  
            for i in range(len(shape)-1):
                pt1 = shape[i]
                pt2 = shape[i+1]
                #draw line
                res = cv2.line( res, pt1, pt2, line_color, line_thickness)

                #draw corner
                res = cv2.circle( res, pt1, point_thickness, point_color, thickness=-1)
            res = cv2.circle( res, pt2, point_thickness, point_color, thickness=-1)
        return res
    

    #______________________________________________________________________________________________________
    #args: 
    #   drawing points as shape shapes
    #args:
    #   img: input image
    #   points  | foramt: [(x1,y1) ,(x2,y2), ...]
    #______________________________________________________________________________________________________
    def draw_points_as_shape(self, img, points, line_color=(255,0,0), point_color=(0,255,100) , line_thickness=3, point_thickness=6):
        if len(points) >=2:
            shape = self.shape_decoder(points)
            return self.draw_shapes(img, [shape], line_color, point_color, line_thickness, point_thickness)
        
        else:
            return img 
        







class drawPoly(drawShape):
    
    def __init__(self, img_size,points_count = np.inf, color_map=COLOR_MAP, thikness_map = THICKNeSS_MAP):
        drawShape.__init__(self, points_count, color_map=color_map, thikness_map = thikness_map)   

    #______________________________________________________________________________________________________
    #exp:
    #   calculate area
    #args
    #   shape  | format: ( center, radius )
    #______________________________________________________________________________________________________
    def area(self, shape):
        return cv2.contourArea( shape )
    
    #______________________________________________________________________________________________________
    #exp:
    #   got shape and point and return True if point be inside the shape. O.w return False
    #args'
    #   pt     | format: (x,y)
    #   shape  | format: ( center, radius )
    #______________________________________________________________________________________________________
    def check_point_inside(self, pt, shape):
        res = cv2.pointPolygonTest( shape, pt, False )
        if res>0:
            return True
        return False
    #______________________________________________________________________________________________________
    #action:
    #   check drawing is finsh or not. if the number of points
    #   be equal to self.points_count it means drawing is finished
    #args:
    #   None
    #return 
    #   state   | format: bool | True means drawing is finished
    #______________________________________________________________________________________________________
    def check_finish(self):
        
        if len(self.points) == self.points_count:
            return True
        
        #self.points -> [[(x1,y1), 'fix'], [(x2,y2), 'fix'], ...]
        if len(self.points)>2 and self.distance( self.points[-1] , self.points[0] ) < 10:
            return True
        
        if len(self.points)>2 and self.distance( self.points[-1] , self.points[-2] ) < 10:
            return True
        
        return False
    #______________________________________________________________________________________________________
    #exp:
    #   nothing do
    #args
    #   points  | format: [(int x1, int y1), (x2, y2), ....]
    #______________________________________________________________________________________________________
    def shape_decoder(self,points):
        #if last point is near to first point we remove it    
        if len(points)>2 and self.distance( points[-1] , points[0] ) < 10:
            points.pop()
            
        #if last point is near previous point we remove it    
        if len(points)>2 and self.distance( points[-1] , points[-2] ) < 10:
            points.pop()
            
        points = np.array(points)
        points = points.reshape(-1,1,2)
        return points
        

    
    #______________________________________________________________________________________________________
    #exp:
    #   convert circel into to points
    #args
    #   shape  | format: ((cx,cy) , radius)
    #______________________________________________________________________________________________________
    def shape_encoder(self,shape):
        return shape.reshape((-1,2)).tolist()
    
        
    #______________________________________________________________________________________________________
    #action:
    #   check click is for editing shapes or add new point
    #args:
    #   None
    #return 
    #   state   | format: bool | True means drawing is finished
    #______________________________________________________________________________________________________
    def check_editing(self, pt, shapes, thresh=THRESH):
        for shape in shapes:
            for i,corner in enumerate(shape):
                corner = corner[0]
                dist = self.distance( corner , pt)
                if dist < thresh:
                    #for edit radius in circle we should edit second point
                    self.float_point_idx['x'] = i
                    self.float_point_idx['y'] = i
                    self.points = self.shape_encoder(shape)
                    self.shapes.remove(shape)
                    self.count_backup = self.points_count
                    self.points_count = len(self.points)
                    return True
        return False
            
            
    #______________________________________________________________________________________________________
    #args: 
    #   drawing shapes
    #args:
    #   img: input image
    #   shapes  | format = [((cx,cy), radius), ((,),) , ....]
    #   color: color of shape
    #______________________________________________________________________________________________________
    def draw_shapes(self, img, shapes, line_color=(255,0,0), point_color=(0,255,100) , line_thickness=3, point_thickness=6):
        res = np.copy(img)
        for shape in shapes:  
            cv2.drawContours(res, [shape], 0, line_color, thickness=line_thickness)

            #draw corners
            for point in shape:
                point = point[0]
                cv2.circle(res, point, point_thickness, color=point_color, thickness=-1)
        
           
        return res
    

    #______________________________________________________________________________________________________
    #args: 
    #   drawing points as shape shapes
    #args:
    #   img: input image
    #   points  | foramt: [(x1,y1) ,(x2,y2), ...]
    #______________________________________________________________________________________________________
    def draw_points_as_shape(self, img, points, line_color=(255,0,0), point_color=(0,255,100) , line_thickness=3, point_thickness=6):
        if len(points) >=2:
            shape = self.shape_decoder(points)
            return self.draw_shapes(img, [shape], line_color, point_color, line_thickness, point_thickness)
        
        else:
            return img     
        
        

if __name__ == '__main__' and False:
    import mouseCV
    cv2.namedWindow('image')
    mouse = mouseCV.Mouse('image')
    img_size = (480,640)
    drawer = drawRect()
    drawer.set_img_size((480,640))
    
    
    while(1):
        x , y = mouse.x/img_size[1] , mouse.y /img_size[0]
        status = mouse.get_status()
        
        if status == mouseCV.LEFT_DOWN:
            drawer.click((x,y))
        
        if status == mouseCV.RIGHT_DOWN:
            drawer.remove_points_or_shape((x,y))

        if status == mouseCV.MOVE:
            drawer.set_float_point((x,y))
        
        #points = drawer.get_points()
        #shapes = drawer.shapes
        
        
        
        cv2.imshow('image',drawer.get_image())
        if cv2.waitKey(8) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    
    
