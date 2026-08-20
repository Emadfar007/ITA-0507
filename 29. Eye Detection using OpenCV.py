import cv2

# Load face and eye classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# Read the image
image = cv2.imread(
    r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-08-20 104547.png"
)

if image is None:
    print("Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # Detect eyes inside each face
    for (x, y, w, h) in faces:
        face_gray = gray[y:y+h, x:x+w]
        face_color = image[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            face_gray,
            scaleFactor=1.1,
            minNeighbors=5
        )

        # Draw rectangles around eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                face_color,
                (ex, ey),
                (ex + ew, ey + eh),
                (0, 255, 0),
                2
            )

    print("Eyes detected:", len(eyes) if len(faces) > 0 else 0)

    # Display result
    cv2.imshow("Eye Detection", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
