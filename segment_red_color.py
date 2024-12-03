import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image\peppers.jpg')
# Convert BGR to RGB for visualization
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the target red color in RGB space
target_red = np.array([255, 0, 0])  # Pure red

# Define the threshold for segmentation
threshold = 200

# Calculate the Euclidean distance for each pixel
distance = np.sqrt(
    (image_rgb[:, :, 0] - target_red[0])**2 +
    (image_rgb[:, :, 1] - target_red[1])**2 +
    (image_rgb[:, :, 2] - target_red[2])**2
)

# Create a binary mask where distance is within the threshold
mask = distance <= threshold

# Create segmented images for R, G, and B channels
segmented_r = np.zeros_like(image_rgb[:, :, 0])
segmented_g = np.zeros_like(image_rgb[:, :, 1])
segmented_b = np.zeros_like(image_rgb[:, :, 2])

segmented_r[mask] = image_rgb[:, :, 0][mask]
segmented_g[mask] = image_rgb[:, :, 1][mask]
segmented_b[mask] = image_rgb[:, :, 2][mask]

# Combine the channels for the final segmented image
segmented_image = np.zeros_like(image_rgb)
segmented_image[:, :, 0] = segmented_r
segmented_image[:, :, 1] = segmented_g
segmented_image[:, :, 2] = segmented_b

# Plot the results
plt.figure(figsize=(15, 10))

# Original image
plt.subplot(2, 3, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

# Red channel
plt.subplot(2, 3, 2)
plt.imshow(segmented_r, cmap='Reds')
plt.title('Segmented Red Channel')
plt.axis('off')

# Green channel
plt.subplot(2, 3, 3)
plt.imshow(segmented_g, cmap='Greens')
plt.title('Segmented Green Channel')
plt.axis('off')

# Blue channel
plt.subplot(2, 3, 4)
plt.imshow(segmented_b, cmap='Blues')
plt.title('Segmented Blue Channel')
plt.axis('off')

# Final segmented image
plt.subplot(2, 3, 5)
plt.imshow(segmented_image)
plt.title('Final Segmented Image')
plt.axis('off')

# Binary mask
plt.subplot(2, 3, 6)
plt.imshow(mask, cmap='gray')
plt.title('Binary Mask')
plt.axis('off')

plt.tight_layout()
plt.savefig('main_output')
plt.show()
