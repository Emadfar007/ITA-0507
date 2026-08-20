import cv2

# Open the video
video = cv2.VideoCapture(
    r"C:\Users\fimra\Videos\16480297_3840_2160_24fps.mp4"
)

if not video.isOpened():
    print("Video not found!")
else:
    # Create background subtractor
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
            mask, cv2.MORPH_OPEN, kernel
        )

        # Find contours
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in contours:
            area = cv2.contourArea(contour)

            if area > 500:
                x, y, w, h = cv2.boundingRect(contour)

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    "Vehicle",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

        # Resize video for display
        display_frame = cv2.resize(frame, (960, 540))

        cv2.imshow("Vehicle Detection", display_frame)

        # Press Q to exit
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
