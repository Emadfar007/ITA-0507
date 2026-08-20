import cv2

# Read the image
image = cv2.imread(
    r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png"
)

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Set threshold value
    threshold_value = 127

    # Apply thresholding
    _, segmented = cv2.threshold(
        gray, threshold_value, 255, cv2.THRESH_BINARY
    )

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
