import cv2
import numpy as np

# Read the image
image = cv2.imread(
    r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png"
)

if image is None:
    print("Image not found!")
else:
    # Convert image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define foreground color levels
    lower = np.array([0, 50, 50])
    upper = np.array([180, 255, 255])

    # Create foreground mask
    mask = cv2.inRange(hsv, lower, upper)

    # Extract foreground
    foreground = cv2.bitwise_and(image, image, mask=mask)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground", foreground)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
