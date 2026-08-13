import cv2

# Read the original image
image = cv2.imread(r"C:\Users\fimra\OneDrive\Pictures\Screenshots\Screenshot 2026-07-09 100612.png")

# Read the watermark image
watermark = cv2.imread(r"C:\Users\fimra\OneDrive\Pictures\watermark.png")

if image is None or watermark is None:
    print("Image not found!")
else:
    # Resize watermark
    watermark = cv2.resize(watermark, (200, 100))

    # Select position
    x, y = 20, 20

    # Insert watermark
    image[y:y+100, x:x+200] = watermark

    # Display the result
    cv2.imshow("Watermarked Image", image)

    # Save the output
    cv2.imwrite("watermarked_image.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
