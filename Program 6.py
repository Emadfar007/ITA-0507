import cv2
import numpy as np
image = cv2.imread(r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png")
if image is None:
    print("Image not found!")
else:
    kernel = np.ones((5, 5), np.uint8)
    eroded = cv2.erode(image, kernel, iterations=1)
    cv2.imshow("Original Image", image)
    cv2.imshow("Eroded Image", eroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
