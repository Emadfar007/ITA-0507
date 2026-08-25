import cv2
import numpy as np

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Read image
image = cv2.imread(
    r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-08-25 100101.png"
)

if image is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    all_faces = []

    # Detect faces at different rotations
    for angle in [-10, 0, 10, 15]:
        h, w = gray.shape

        M = cv2.getRotationMatrix2D(
            (w // 2, h // 2), angle, 1
        )

        rotated = cv2.warpAffine(
            gray, M, (w, h)
        )

        faces = face_cascade.detectMultiScale(
            rotated,
            scaleFactor=1.05,
            minNeighbors=3,
            minSize=(20, 20)
        )

        # Convert detected coordinates back
        inverse = cv2.invertAffineTransform(M)

        for (x, y, fw, fh) in faces:
            points = np.array([
                [x, y],
                [x + fw, y + fh]
            ], dtype=np.float32)

            points = cv2.transform(
                points.reshape(-1, 1, 2), inverse
            ).reshape(-1, 2)

            x1, y1 = points.min(axis=0).astype(int)
            x2, y2 = points.max(axis=0).astype(int)

            all_faces.append([x1, y1, x2 - x1, y2 - y1])

    # Remove duplicate detections
    boxes = []
    for box in all_faces:
        x, y, w, h = box

        duplicate = False

        for bx, by, bw, bh in boxes:
            cx = x + w // 2
            cy = y + h // 2
            bcx = bx + bw // 2
            bcy = by + bh // 2

            if abs(cx - bcx) < 30 and abs(cy - bcy) < 30:
                duplicate = True
                break

        if not duplicate:
            boxes.append(box)

    print("Number of faces:", len(boxes))

    # Draw rectangles
    for (x, y, w, h) in boxes:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Detection", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
