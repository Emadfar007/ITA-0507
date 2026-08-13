import cv2

image = cv2.imread(
    r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png"
)

if image is None:
    print("Image not found!")
else:
    roi = image[20:120, 20:120]
    copied = roi.copy()

    image[150:250, 150:250] = copied

    cv2.imshow("Original with Pasted ROI", image)
    cv2.imshow("Cropped ROI", roi)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
