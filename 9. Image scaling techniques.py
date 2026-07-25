import cv2

# Read the image
image = cv2.imread(r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png")

if image is None:
    print("Image not found!")
else:
    # Resize to a bigger size (2x)
    bigger_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Resize to a smaller size (0.5x)
    smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image", bigger_image)
    cv2.imshow("Smaller Image", smaller_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
