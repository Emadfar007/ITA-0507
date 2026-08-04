import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png")

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Dilate the corner points
    corners = cv2.dilate(corners, None)

    # Mark detected corners in red
    image[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Display the result
    cv2.imshow("Harris Corner Detection", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
