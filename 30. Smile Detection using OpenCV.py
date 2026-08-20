import cv2

# Load face and smile classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
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

    smile_count = 0

    # Detect smile inside each face
    for (x, y, w, h) in faces:
        face_gray = gray[y:y+h, x:x+w]
        face_color = image[y:y+h, x:x+w]

        smiles = smile_cascade.detectMultiScale(
            face_gray,
            scaleFactor=1.7,
            minNeighbors=20
        )

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(
                face_color,
                (sx, sy),
                (sx + sw, sy + sh),
                (0, 255, 0),
                2
            )

            cv2.putText(
                face_color,
                "Smile",
                (sx, sy - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            smile_count += 1

    print("Smiles detected:", smile_count)

    # Display result
    cv2.imshow("Smile Detection", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
