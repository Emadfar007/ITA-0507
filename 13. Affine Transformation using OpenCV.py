import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png")

if image is None:
    print("Image not found!")
else:
    rows, cols = image.shape[:2]

    # Select three points from the original image
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

    # Select corresponding points in the transformed image
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    # Compute the affine transformation matrix
    matrix = cv2.getAffineTransform(pts1, pts2)

    # Apply the affine transformation
    transformed = cv2.warpAffine(image, matrix, (cols, rows))

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transformed Image", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
