import cv2
import pytesseract

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Open video
video = cv2.VideoCapture(
    r"C:\Users\fimra\Videos\16480297_3840_2160_24fps.mp4"
)

if not video.isOpened():
    print("Video not found!")
else:
    # Background subtractor for vehicle detection
    background = cv2.createBackgroundSubtractorMOG2(
        history=500,
        varThreshold=50
    )

    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Detect moving objects
        mask = background.apply(frame)

        # Remove noise
        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT, (5, 5)
        )

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel
        )

        # Find contours
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in contours:

            area = cv2.contourArea(contour)

            if area > 1000:

                x, y, w, h = cv2.boundingRect(contour)

                # Crop detected vehicle
                vehicle = frame[y:y+h, x:x+w]

                if vehicle.size == 0:
                    continue

                # Convert vehicle to grayscale
                gray = cv2.cvtColor(
                    vehicle,
                    cv2.COLOR_BGR2GRAY
                )

                # Extract text using OCR
                text = pytesseract.image_to_string(
                    gray,
                    config="--psm 6"
                ).strip()

                # Draw vehicle rectangle
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                # Display detected text
                if text:
                    cv2.putText(
                        frame,
                        text[:30],
                        (x, max(y - 10, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2
                    )

                    print("Detected Text:", text)

        # Resize for display without stretching
        h, w = frame.shape[:2]

        max_width = 960
        max_height = 540

        scale = min(
            max_width / w,
            max_height / h
        )

        new_w = int(w * scale)
        new_h = int(h * scale)

        display_frame = cv2.resize(
            frame,
            (new_w, new_h)
        )

        cv2.imshow(
            "Vehicle and Text Detection",
            display_frame
        )

        # Press Q to quit
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
