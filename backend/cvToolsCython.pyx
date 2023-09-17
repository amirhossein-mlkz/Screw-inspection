import numpy
cimport numpy
cimport cython
from libc.math cimport abs





ctypedef numpy.int32_t DTYPE_int32
ctypedef numpy.int64_t DTYPE_int64
ctypedef numpy.uint8_t DTYPE_uint8
ctypedef numpy.float32_t DTYPE_float32

#ctypedef (numpy.ndarray[DTYPE_uint8, ndim=2] , numpy.ndarray[DTYPE_int32, ndim=2]) RES_remove_belt_edge_TYPE

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def belt_detection(numpy.ndarray[DTYPE_uint8, ndim=2] img, int thresh, int win_size, char* side):

    cdef int i=0,j=0
    cdef int start=0, stop=0, step=0
    cdef int h = img.shape[0]
    cdef int w = img.shape[1]
    cdef numpy.ndarray[DTYPE_int32, ndim=2] res = numpy.zeros((2,2), dtype = numpy.int32)
    cdef numpy.ndarray[DTYPE_int32, ndim=2] pts = numpy.zeros((win_size,2), dtype = numpy.int32)


    if side[0] == "l":
        start = 0
        stop = w
        step = 1
    
    elif side[0] == 'r':
        start = w-1
        stop = 0
        step = -1


    for j in range(0,win_size): 
        for i in range(start,stop, step):
            if abs(img[j,i] - img[j,i+step] ) > thresh:
                pts[j,0] = i
                pts[j,1] = j
                break
    
    res[0] = pts.mean(axis=0).astype(numpy.int32)

    for j in range(0,win_size):
        for i in range(start, stop, step):
            if abs(img[h-1-j,i] - img[h-1-j,i+step] ) > thresh:
                pts[j,0] = i
                pts[j,1] = h-1-j
                break

    res[1] = pts.mean(axis=0).astype(numpy.int32)

    return res


@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def derivative_threshould(numpy.ndarray[DTYPE_int32, ndim=2] img, int thresh):

    cdef int i=0,j=0
    cdef int diff=0
    cdef int diff1=0, diff2 = 0
    cdef int h = img.shape[0]
    cdef int w = img.shape[1]
    cdef numpy.ndarray[DTYPE_uint8, ndim=2] res = numpy.zeros((h,w), dtype = numpy.uint8)
    #res = numpy.zeros((arr_shape - window,), dtype = numpy.int32 )

    for i in range(1,w-1):
        for j in range(1,h-1):
            diff1 = img[j-1,i] - img[j+1, i]
            diff2 = img[j,i-1] - img[j, i+1]
            if diff1 < 0:
                diff1*=-1
            if diff2<0:
                diff2*=-1
            diff = diff2 + diff1
            if diff > thresh:
                res[j,i] = 255
    return res








@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False) # turn off negative index wrapping for entire function
def find_belt_edge_neighbor_point(numpy.ndarray[DTYPE_uint8, ndim=2] img,
                                    int belt_x,
                                    numpy.ndarray[DTYPE_int32, ndim=2] roi,
                                    int margin,
                                    int kernel_w,
                                    int kernel_h,
                                    int thresh):
    cdef int i=0,j=0
    cdef int x_left=0, x_right=0, x=0, y=0
    cdef int left_point_founded_flag = 0
    cdef int right_point_founded_flag = 0
    cdef int count_neighbors = 0
    #cdef numpy.ndarray[DTYPE_uint8, ndim=2] res = numpy.zeros((2,2,2), dtype = numpy.uint8)
    cdef numpy.ndarray[DTYPE_int32, ndim=3] res_pts = numpy.zeros((2,2,2), dtype=numpy.int32)
    for y in range(roi[0,1], roi[1,1]):
        x = belt_x
        x_left = x - margin
        x_right = x + margin
        #-------------found left point of screw near to belt
        if left_point_founded_flag == 0:
            if img[y,x_left] == 255:
                count_neighbors = 0
                for i in range(0,kernel_w):
                    for j in range(0, kernel_h):
                        if img[j + y, x_left - i] == 255:
                            count_neighbors+=1
                if count_neighbors > thresh:
                    res_pts[0, 0, 0] = x_left
                    res_pts[0, 0, 1] = y
                    left_point_founded_flag = 1
        #-------------found right point of screw near to belt
        if right_point_founded_flag == 0:
            if img[y,x_right] == 255:
                count_neighbors = 0
                for i in range(0,kernel_w):
                    for j in range(0,kernel_h):
                        if img[y + j,x_right + i] == 255:
                            count_neighbors+=1
                if count_neighbors > thresh:
                    res_pts[0, 1, 0] = x_right
                    res_pts[0, 1, 1] = y
                    right_point_founded_flag = 1
        if right_point_founded_flag==1 and left_point_founded_flag == 1:
            break
    left_point_founded_flag = 0
    right_point_founded_flag = 0
    y = 0
    for y in range(roi[1,1], roi[0,1], -1):
        x = belt_x
        x_left = x - margin
        x_right = x + margin
        #-------------found left point of screw near to belt
        if left_point_founded_flag == 0:
            if img[y,x_left] == 255:
                count_neighbors = 0
                i = 0
                j = 0
                for i in range(0,kernel_w):
                    for j in range(0, kernel_h):
                        if img[y - j, x_left - i] == 255:
                            count_neighbors+=1
                if count_neighbors > thresh:
                    res_pts[1, 0, 0] = x_left
                    res_pts[1, 0, 1] = y
                    left_point_founded_flag = 1
        # #-------------found right point of screw near to belt
        if right_point_founded_flag == 0:
            if img[y,x_right] == 255:
                count_neighbors = 0
                for i in range(0,kernel_w):
                    for j in range(0,kernel_h):
                        if img[y - j,x_right + i] == 255:
                            count_neighbors+=1
                if count_neighbors > thresh:
                    res_pts[1, 1, 0] = x_right
                    res_pts[1, 1, 1] = y
                    right_point_founded_flag = 1
        if right_point_founded_flag==1 and left_point_founded_flag == 1:
            break
    return res_pts




@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def remove_belt_edge_line(numpy.ndarray[DTYPE_uint8, ndim=2] img,
                     numpy.ndarray[DTYPE_int32, ndim=3] pts):
    
    cdef int h = img.shape[0]
    cdef int w = img.shape[1]
    cdef float slope=0, intercept=0


    cdef numpy.ndarray[DTYPE_int32, ndim=1]  xs1 = numpy.arange( pts[0, 0, 0], pts[0, 1, 0] , dtype=numpy.int32)
    cdef numpy.ndarray[DTYPE_int32, ndim=1]  ys1 = numpy.zeros_like(xs1, dtype=numpy.int32)
    cdef int n1 = 0
    if float(pts[0, 0, 0] - pts[0, 1, 0] ) != 0:
        slope = float(pts[0,0, 1] - pts[0,1,1] ) / float(pts[0, 0, 0] - pts[0, 1, 0] )
        intercept = pts[0, 0,1] - slope * pts[0,0,0]
        ys1 = (xs1 * slope + intercept).astype(numpy.int32)
        n1 = ys1.shape[0]
        for i in range(n1):
            for j in range(0,int(ys1[i])-1):
                img[j, xs1[i]] = 0

    
    cdef numpy.ndarray[DTYPE_int32, ndim=1]  xs2 = numpy.arange( pts[1, 0, 0], pts[1, 1, 0] , dtype=numpy.int32)
    cdef numpy.ndarray[DTYPE_int32, ndim=1]  ys2 = numpy.zeros_like(xs2, dtype=numpy.int32)
    cdef int n2 = 0
    if float(pts[1, 0, 0] - pts[1, 1, 0] ) != 0:
        slope = float(pts[1, 0, 1] - pts[1, 1,1] ) / float(pts[1, 0, 0] - pts[1, 1, 0] )
        intercept = pts[1, 0, 1] - slope * pts[1, 0, 0]
        
        ys2 = (xs2 * slope + intercept).astype(numpy.int32)
        n2 = ys2.shape[0]
        for i in range(n2):
            for j in range(int(ys2[i]), h):
                img[j, xs2[i]] = 0
    
    return img




