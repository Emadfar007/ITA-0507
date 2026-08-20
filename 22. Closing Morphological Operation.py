import cv2
import numpy as np

# Read the image
image = cv2.imread(
    r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png"
)

if image is None:
    print("Image not found!")
else:
    # Create kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply Closing
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Closing Image", closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
