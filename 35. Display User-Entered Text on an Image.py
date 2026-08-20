import cv2
import numpy as np

# Get image size
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create a white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Get text from user
text = input("Enter text: ")

# Add text to the image
cv2.putText(
    image,
    text,
    (50, height // 2),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)

# Display image
cv2.imshow("Text on Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
