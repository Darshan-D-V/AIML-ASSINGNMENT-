import cv2
import numpy as np

# Load image
image = cv2.imread("C:\\Users\\Darshan D V\\Desktop\\image.jpg")

# Print shape
print("Image Shape:", image.shape)

# Print pixel values (first 5 pixels)
print("Sample Pixel Values:\n", image[0:5, 0:5])

# Split channels
blue, green, red = cv2.split(image)

print("Blue Channel Shape:", blue.shape)
print("Green Channel Shape:", green.shape)
print("Red Channel Shape:", red.shape)