import cv2

# Read the image
image = cv2.imread(r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png")

if image is None:
    print("Image not found!")
else:
    # Rotate the image by 180 degrees
    rotated = cv2.rotate(image, cv2.ROTATE_180)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("180 Degree Rotated Image", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
