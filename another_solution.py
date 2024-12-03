import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. read image
image = cv2.imread('image/peppers.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # convert to RGB format

# 2. split R,G,B channels
R_channel = image_rgb[:, :, 0]
G_channel = image_rgb[:, :, 1]
B_channel = image_rgb[:, :, 2]

# 3. Red area segmentation
# set the mask
red_mask = (R_channel > 150) & (R_channel > G_channel*1.1) & (R_channel > B_channel*1.1)

# segment the image
segmented_image = np.zeros_like(image_rgb)  # Initialize as a blask image
segmented_image[red_mask] = image_rgb[red_mask]  # Just reserve red area

# 4. show the result
plt.figure(figsize=(16, 8))

plt.subplot(2, 3, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(R_channel, cmap='Reds')
plt.title('R Channel')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(G_channel, cmap='Greens')
plt.title('G Channel')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(B_channel, cmap='Blues')
plt.title('B Channel')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(segmented_image)
plt.title('Segmented Red Areas')
plt.axis('off')

plt.tight_layout()
plt.savefig('result')
plt.show()

# 5. contrast
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')


plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.title('Segmented Red Areas')
plt.axis('off')

plt.tight_layout()
plt.show()
