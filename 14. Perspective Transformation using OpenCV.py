import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png")

if image is None:
    print("Image not found!")
else:
    rows, cols = image.shape[:2]

    # Four points in the original image
    pts1 = np.float32([[50, 50], [300, 50], [50, 300], [300, 300]])

    # Corresponding points in the transformed image
    pts2 = np.float32([[10, 100], [280, 50], [100, 300], [300, 280]])

    # Compute the perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply perspective transformation
    transformed = cv2.warpPerspective(image, matrix, (cols, rows))

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformed Image", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
