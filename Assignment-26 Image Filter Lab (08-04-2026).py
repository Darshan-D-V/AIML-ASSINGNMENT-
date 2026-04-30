import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("C:\\Users\\Darshan D V\\Desktop\\image.jpg")

if img is None:
    print("❌ Image not found")
    exit()

# Convert BGR → RGB (for matplotlib)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 1️⃣ Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2️⃣ Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 3️⃣ Edge Detection
edges = cv2.Canny(blur, 100, 200)

# 📊 Display all images
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.title("Original")
plt.imshow(img_rgb)
plt.axis("off")

plt.subplot(2, 2, 2)
plt.title("Grayscale")
plt.imshow(gray, cmap='gray')
plt.axis("off")

plt.subplot(2, 2, 3)
plt.title("Blur")
plt.imshow(blur, cmap='gray')
plt.axis("off")

plt.subplot(2, 2, 4)
plt.title("Edges")
plt.imshow(edges, cmap='gray')
plt.axis("off")

plt.tight_layout()
plt.show()