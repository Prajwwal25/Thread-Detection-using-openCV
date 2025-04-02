import cv2
import numpy as np

# Load Image
img = cv2.imread('prediction_image2.jpg')

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert to Grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Adaptive Thresholding
thresh_img = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 5)

# Morphological Operations to clean small noise
kernel = np.ones((3, 3), np.uint8)
thresh_img = cv2.morphologyEx(thresh_img, cv2.MORPH_CLOSE, kernel, iterations=2)

# Find Contours
contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a copy of the image for drawing
processed_img = img.copy()

# Fine-Tune Contour Filtering
min_area = 50  # Small noise filtering
max_area = 2000  # Avoid detecting large blobs

valid_contours = []
for c in contours:
    area = cv2.contourArea(c)
    if min_area < area < max_area:
        valid_contours.append(c)

# Assign different colors for each thread
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), 
          (255, 0, 255), (0, 255, 255), (128, 0, 128), (0, 128, 128)]

# Draw bounding boxes only for correctly detected threads
for idx, c in enumerate(valid_contours):
    x, y, w, h = cv2.boundingRect(c)
    
    # Condition to eliminate very thin bounding boxes (false detections)
    if w > 5 and h > 5:
        color = colors[idx % len(colors)]  # Cycle through colors
        cv2.rectangle(processed_img, (x, y), (x + w, y + h), color, 2)

# Count total number of detected threads
thread_count = len(valid_contours)

# Display thread count on the image
cv2.putText(processed_img, f"Threads: {thread_count}", (50, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

# Save and Show Results
cv2.imwrite("processed_threads.jpg", processed_img)
cv2.imshow("Processed Image", processed_img)

# Print thread count
print(f"Total Number of Threads Detected: {thread_count}")

cv2.waitKey(0)
cv2.destroyAllWindows()
