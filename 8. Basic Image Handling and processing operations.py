import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png")

if image is None:
    print("Image not found!")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(image, kernel, iterations=1)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Dilated Image", dilated)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
