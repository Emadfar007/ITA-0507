import cv2

# Load the image
image = cv2.imread(
    r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-08-20 101435.png"
)

if image is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=50,
        param1=100,
        param2=50,
        minRadius=20,
        maxRadius=300
    )

    if circles is not None:
        circles = circles[0].astype(int)

        for x, y, r in circles:
            cv2.circle(image, (x, y), r, (0, 255, 0), 2)
            cv2.putText(
                image, "Watch",
                (x - 30, y - r - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2
            )

        print("Watch detected!")
    else:
        print("Watch not detected!")

    cv2.imshow("Watch Recognition", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
