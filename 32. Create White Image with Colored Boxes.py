import cv2
import numpy as np

# Get image size from user
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create a white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Box size = 1/10 of image
box_h = height // 10
box_w = width // 10

# Black box - Top Left
image[0:box_h, 0:box_w] = [0, 0, 0]

# Blue box - Top Right
image[0:box_h, width-box_w:width] = [255, 0, 0]

# Green box - Bottom Left
image[height-box_h:height, 0:box_w] = [0, 255, 0]

# Red box - Bottom Right
image[height-box_h:height, width-box_w:width] = [0, 0, 255]

# Display image
cv2.imshow("Colored Boxes", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
