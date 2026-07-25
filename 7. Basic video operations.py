import cv2

# Load the video
video = cv2.VideoCapture(r"C:\Users\fimra\Videos\sample-5s.mp4")  # Replace with your video path

if not video.isOpened():
    print("Error: Unable to open video.")
    exit()

print("Press:")
print("N - Normal Speed")
print("S - Slow Motion")
print("F - Fast Motion")
print("Q - Quit")

speed = 30  # Normal speed (milliseconds)

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Video Processing", frame)

    key = cv2.waitKey(speed) & 0xFF

    if key == ord('s'):      # Slow motion
        speed = 100
    elif key == ord('f'):    # Fast motion
        speed = 10
    elif key == ord('n'):    # Normal speed
        speed = 30
    elif key == ord('q'):    # Quit
        break

video.release()
cv2.destroyAllWindows()
