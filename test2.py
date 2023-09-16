
# import cv2
# import numpy as np
    
 
# # Reading an image in default mode
# Img = np.zeros((512, 512, 3), np.uint8)
    
# # Window name in which image is displayed
# window_name = 'Image'
   
# # Center coordinates
# center_coordinates = (220, 150)
  
# # Radius of circle
# radius = 100
   
# # Red color in BGR
# color = (255, 133, 233)
   
# # Line thickness of -1 px
# thickness = -1
   
# # Using cv2.circle() method
# # Draw a circle of red color of thickness -1 px
# image = cv2.circle(Img, center_coordinates, radius, color, thickness)
# start_point = (70, 50)
# thickness=5
# end_point = (180, 200)
# color = (0, 133, 0)
# image=cv2.line(image, start_point, end_point, color, thickness) 
# start_point = (180, 200)
# thickness=5
# end_point = (250, 230)
# color = (0, 133, 0)
# image=cv2.line(image, start_point, end_point, color, thickness) 
# start_point = (250, 230)
# thickness=5
# end_point = (600, 230)
# color = (0, 133, 0)
# image=cv2.line(image, start_point, end_point, color, thickness) 
# mask = cv2.inRange(image, (255, 133, 233), (255, 133, 233))
# img = image[:,:,:]


# # Displaying the image
# cv2.imshow('org', image)
# cv2.waitKey(0)
# cv2.imshow('mask', mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2

img = cv2.imread('sample images/temp_top/6.bmp')
cv2.imshow('a',img)
cv2.waitKey(0)