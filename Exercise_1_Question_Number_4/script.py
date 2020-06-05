import numpy as np 
import cv2 

img = np.zeros((400, 400, 3), dtype = "uint8")
cv2.circle(img, (200, 200), 100, (255, 0, 0), 3) 
# triangle = np.array([[[240, 130], [380, 230], [190, 280]]])
diamond = np.array([[[120,200],[200,280],[280,200],[200,120]]]) 
hexagon = np.array([[[80,200],[120,320],[280,320],[320,200],[280,80],[120,80]]])
cv2.polylines(img, [diamond], True, (0,255,0), thickness=3)
cv2.polylines(img, [hexagon], True, (0,255,0), thickness=3)
cv2.imshow('dark', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()