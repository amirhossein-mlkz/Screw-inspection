import numpy
cimport numpy
cimport cython
from libc.math cimport cos

cdef float pi = 3.14159




ctypedef numpy.int32_t DTYPE_int32
ctypedef numpy.uint8_t DTYPE_uint8
ctypedef numpy.float32_t DTYPE_float32

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def fill_gap(numpy.ndarray[DTYPE_uint8, ndim=2] img, int gap):

    cdef int i,j
    cdef int img_h = img.shape[0]
    cdef int img_w = img.shape[1]
    cdef int start, end
    cdef bool find_gap = FALSE

    cdef numpy.ndarray[DTYPE_uint8, ndim=2] res = numpy.zeros((img_h, img_w), dtype = numpy.uint8)

    for i in range(img_h):
        for j in range(img_w):
            if img[i,j] == 0 and img[i,j-1] == 255 find_gap == FALSE:
                start = j
            elif 

        total = 0
        for w in range(window):
            total += arr[i+w]
        total = total / window
        res[i] = total
    
    return res



@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def moving_avrage_float(numpy.ndarray[DTYPE_float32, ndim=1] arr, int window):

    cdef float total
    cdef int i,w
    cdef int arr_shape = arr.shape[0]
    cdef numpy.ndarray[DTYPE_float32, ndim=1] res = numpy.zeros((arr_shape - window,), dtype = numpy.float32)
    #res = numpy.zeros((arr_shape - window,), dtype = numpy.int32 )

    for i in range(arr_shape - window):
        total = 0
        for w in range(window):
            total += arr[i+w]
        total = total / window
        res[i] = total
    
    return res




@cython.boundscheck(False)
@cython.wraparound(False)
def extract_points(numpy.ndarray[DTYPE_uint8, ndim=2] img, int thresh, int perspective_angle):

    cdef long long int total_sum
    cdef int total_count, last_j
    cdef int i,j, point_idx = 0
    cdef int img_h = img.shape[0]
    cdef int img_w = img.shape[1]
    cdef numpy.ndarray[DTYPE_int32, ndim=2] res_pts = numpy.zeros( (img_w, 2), dtype = numpy.int32 ) 
    cdef float perspective = cos(perspective_angle * pi / 180)

    #limit search corespond to previous point
    cdef int range_y = 50
    cdef int y_range_low = 0
    cdef int y_range_max = img_h
    for i in range(img_w):
        total_sum = 0
        total_count = 0

        for j in range(y_range_low, y_range_max):
            if img[j,i] > thresh:
                
                # remove noise 
                if total_count>0 and total_count<3 and j - last_j > 5:
                    total_count = 1
                    total_sum = j
                    last_j = j
                else:
                    total_count +=1
                    total_sum += j
                    last_j = j

        if total_count > 2:
            res_pts[point_idx,0] = i
            res_pts[point_idx,1] = int((total_sum / total_count) / perspective)

            y_range_low = max(0, res_pts[point_idx,1] - range_y)
            y_range_max = min(img_h, res_pts[point_idx,1] + range_y)

            point_idx+=1
        else:
            y_range_low = 0
            y_range_max = img_h

    
    return res_pts[:point_idx]


# @cython.boundscheck(False)
# @cython.wraparound(False)
# def extract_points_left(numpy.ndarray[DTYPE_uint8, ndim=2] img, int thresh, int perspective_angle ):

#     cdef int total_count, last_j
#     cdef int i,j, point_idx = 0
#     cdef int img_h = img.shape[0]
#     cdef int img_w = img.shape[1]
#     cdef numpy.ndarray[DTYPE_int32, ndim=2] res_pts = numpy.zeros( (img_w, 2), dtype = numpy.int32 ) 
#     cdef float perspective = cos(perspective_angle * pi / 180)



#     for i in range(img_h):
#         total_count = 0
#         for j in range(img_w):
#             if img[i,j] > thresh:
                
#                 if total_count == 0:
#                     last_j = j
#                     total_count+=1
                
#                 elif total_count > 0 and total_count < 3 and j - last_j > 5:
#                     total_count = 1
#                     last_j = j
#                 else:
#                     total_count +=1
#                     last_j = j
                
#                 if total_count>=8:
#                     break


        
#         if total_count>0:
#             res_pts[point_idx,0] = int(last_j / perspective)
#             res_pts[point_idx,1] = i
#             point_idx+=1

#     return res_pts[:point_idx]






@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def calc_slope(numpy.ndarray[DTYPE_int32, ndim=2] arr, int step):
    cdef int half_step = step//2
    cdef float slope
    cdef int i = 0
    cdef int arr_shape = arr.shape[0]
    cdef numpy.ndarray[DTYPE_int32, ndim=2] res = numpy.zeros((arr_shape - half_step * 2,2), dtype = numpy.int32)
    cdef int count = 0
    for i in range(half_step, arr_shape - half_step):
        #print(i, arr_shape, len(res))
        slope = ( arr[ i + half_step, 1] - arr[i - half_step, 1] ) / (( arr[ i + half_step, 0] - arr[i - half_step ,0] )) 
        res[count,0] = arr[i,0]
        #res[count,1] = arr[i,1]
        res[count,1] = int(slope)
        count+=1
        

    return res




@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def gap_and_jump_detetcion(numpy.ndarray[DTYPE_int32, ndim=2] arr, int step, int min_jump, int min_gap):
    cdef int i = 0
    cdef int jump, gap
    cdef int arr_shape = arr.shape[0]
    cdef numpy.ndarray[DTYPE_int32, ndim=2] res = numpy.zeros((arr_shape - step,4), dtype = numpy.int32)
    cdef int count = 0
    for i in range(arr_shape - step):
        jump = numpy.abs(int(( arr[ i + step, 1] - arr[i, 1] ) / ( arr[ i + step, 0] - arr[i ,0] ) ) )
        #jump = numpy.abs(( arr[ i + step, 1] - arr[i, 1] ) - ( arr[ i + step, 0] - arr[i ,0] ) )
        gap = arr[ i + 1, 0] - arr[i, 0]
        print(arr[ i + step], arr[i], jump)
        if  gap>=min_gap:
            res[count,0] = arr[i,0]
            res[count,1] = arr[i,1]
            res[count,2] = 0
            res[count,3] = gap
            count = count + 1
            res[count,0] = arr[i+1,0]
            res[count,1] = arr[i+1,1]
            res[count,2] = 0
            res[count,3] = -gap
            count = count + 1

        elif jump >= min_jump:
            res[count,0] = arr[i,0]
            res[count,1] = arr[i,1]
            res[count,2] = jump
            res[count,3] = 0
            count = count + 1
    
        

    return res[:count]




@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def gap_detection(numpy.ndarray[DTYPE_int32, ndim=2] arr, int min_gap):
    cdef int i = 0
    cdef int gap
    cdef int arr_shape = arr.shape[0]
    cdef numpy.ndarray[DTYPE_int32, ndim=2] res = numpy.zeros((arr_shape,2), dtype = numpy.int32)
    cdef int count = 0
    for i in range(arr_shape):
        gap = arr[ i + 1, 0] - arr[i, 0]
        if  gap>=min_gap:
            res[count,0] = arr[i,0]
            #res[count,1] = arr[i,1]
            res[count,1] = gap
            count = count + 1
            
            #res[count,0] = arr[i+1,0]
            #res[count,1] = arr[i+1,1]
            #res[count,1] = gap
            #count = count + 1
    
        

    return res[:count]




def gap_representation(numpy.ndarray[DTYPE_int32, ndim=2] gap_pts, int img_w, int ignore_space):
    cdef int i = 0
    cdef int j = 0
    cdef int gap_pts_shape = gap_pts.shape[0]
    cdef numpy.ndarray[DTYPE_uint8, ndim=2] res = numpy.zeros((1,img_w), dtype = numpy.uint8)
    cdef int prev_end_point = -1000
    cdef int x1,x2
    for i in range(gap_pts_shape):
        x1 = gap_pts[i,0]
        x2 = x1 + gap_pts[i,1]
        
        if x1 - prev_end_point <= ignore_space:
            x1 = prev_end_point
        prev_end_point = x2

        for j in range(x1,x2):
            res[0,j] = 255
    
    return res



