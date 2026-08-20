import cv2
import numpy as np

# Get image size from user
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create a white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Find center of image
center = (width // 2, height // 2)

# Draw circle
cv2.circle(image, center, 100, (0, 0, 255), 3)

# Display image
cv2.imshow("Circle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
