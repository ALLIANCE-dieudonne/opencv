import cv2
import numpy as np

image = cv2.imread('assignment-001-given.jpg')

resized_image = cv2.resize(image, (image.shape[1] // 3, image.shape[0] // 3))

img_height, img_width, img_channels = resized_image.shape

top_left = (85, 50)  
bottom_right = (img_width - 90, img_height - 10) 

cv2.rectangle(resized_image, top_left, bottom_right, (0, 255, 0), 3)  

text = 'RAH972U'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1  
font_thickness = 2
text_color = (0, 255, 0)

text_size, baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
text_width, text_height = text_size

text_x = bottom_right[0] - text_width   
text_y = top_left[1] - 10 

overlay = resized_image.copy()

rect_x1 = text_x - 10  
rect_y1 = text_y - text_height - 10  
rect_x2 = text_x + text_width   
rect_y2 = text_y + baseline   

cv2.rectangle(overlay, (rect_x1, rect_y1), (rect_x2, rect_y2), (0, 0, 0), -1)  

cv2.addWeighted(overlay, 0.5, resized_image, 1 - 0.5, 0, resized_image) 

cv2.putText(resized_image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)

cv2.imshow('Resized Image with Transparent Background Text', resized_image)

cv2.waitKey(0)

cv2.imwrite("Final image.jpg", resized_image)

cv2.destroyAllWindows()
