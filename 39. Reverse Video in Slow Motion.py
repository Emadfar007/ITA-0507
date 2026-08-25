import cv2

# Open video
video = cv2.VideoCapture(
    r"C:\Users\fimra\Videos\16480297_3840_2160_24fps.mp4"
)

if not video.isOpened():
    print("Video not found!")
else:
    frames = []

    # Read all frames
    while True:
        ret, frame = video.read()

        if not ret:
            break

        frames.append(frame)

    video.release()

    # Play video in reverse
    for frame in reversed(frames):

        # Resize while maintaining aspect ratio
        h, w = frame.shape[:2]
        max_width = 960
        max_height = 540

        scale = min(max_width / w, max_height / h)

        new_w = int(w * scale)
        new_h = int(h * scale)

        display_frame = cv2.resize(
            frame,
            (new_w, new_h)
        )

        cv2.imshow("Reverse Slow Motion", display_frame)

        # Slow motion
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
