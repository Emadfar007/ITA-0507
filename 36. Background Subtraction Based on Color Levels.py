import cv2
import numpy as np

# Read the image
image = cv2.imread(
    r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png"
)

if image is None:
    print("Image not found!")
else:
    # Convert image from BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color levels for background
    lower = np.array([0, 0, 180])
    upper = np.array([180, 80, 255])

    # Create mask for background
    mask = cv2.inRange(hsv, lower, upper)

    # Remove background
    result = cv2.bitwise_and(image, image, mask=~mask)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Background Removed", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
