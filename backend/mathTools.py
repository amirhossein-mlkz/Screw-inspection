import numpy as np
import math


def horizontal_distance( pts1,pts2, decimals=2):
    dist = np.round( abs(pts1[:,0] - pts2[:,0]) , decimals )
    min_dist = dist.min()
    max_dist = dist.max()
    avg_dist = np.round( dist.mean(), decimals )
    
    return min_dist, max_dist, avg_dist, dist



def vertical_distance( pts1,pts2, decimals=2):
    dist = np.round( abs(pts1[:,1] - pts2[:,1]) , decimals )
    min_dist = dist.min()
    max_dist = dist.max()
    avg_dist = np.round( dist.mean(), decimals )
    
    return min_dist, max_dist, avg_dist, dist
    



def thread_step_distance(pts, decimals=2):
    pts1 = np.copy(pts[:-1])
    pts2 = np.copy(pts[1:])
    return horizontal_distance(pts1, pts2, decimals)