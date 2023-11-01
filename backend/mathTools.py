import numpy as np
import math

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def horizontal_distance( pts1,pts2, decimals=2):
    if len(pts1) == 0 or len(pts2) == 0:
        return 0,0,0,[]
    dist = np.round( abs(pts1[:,0] - pts2[:,0]) , decimals )
    print(len(dist))
    try:
        if len(dist) >= 13:
            dist = moving_average(dist, 10)
        elif len(dist) >= 7:
            dist = moving_average(dist, 5)
        elif len(dist) >=4:
            dist = moving_average(dist, 3)
    except:
        pass
    min_dist = dist.min()
    max_dist = dist.max()
    avg_dist = np.round( dist.mean(), decimals )
    
    return min_dist, max_dist, avg_dist, dist



def vertical_distance( pts1,pts2, decimals=2):
    if len(pts1) == 0 or len(pts2) == 0:
        return 0,0,0,[]
    dist = np.round( abs(pts1[:,1] - pts2[:,1]) , decimals )
    min_dist = dist.min()
    max_dist = dist.max()
    avg_dist = np.round( dist.mean(), decimals )
    
    return min_dist, max_dist, avg_dist, dist
    



def thread_step_distance(pts, decimals=2):
    if len(pts) < 2:
        return 0,0,0,[]
    pts1 = np.copy(pts[:-1])
    pts2 = np.copy(pts[1:])
    return horizontal_distance(pts1, pts2, decimals)



def thread_lenght(pts, decimals=2):
    if len(pts) < 2:
        return 0,0,0,[]
    x1 = pts[0][0]
    x2 = pts[-1][0]
    
    return abs(x2-x1) , abs(x2-x1), abs(x2-x1), None




def angle2line(angle, center, lenght):
    a = np.cos(angle * np.pi/180)
    b = np.sin(angle * np.pi/180)

    x0,y0 = center

    x1 = int(x0 + 2*lenght*(-b))
    y1 = int(y0 + 2*lenght*(a))

    x2 = int(x0 - 2*lenght*(-b))
    y2 = int(y0 - 2*lenght*(a))

    return (x1,y1) , (x2,y2)




