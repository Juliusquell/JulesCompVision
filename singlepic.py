import cv2
import numpy as np

# Load the image
img = cv2.imread('/home/julius/workspace/JulesCompVision/blume.JPG')

size = (500,500,1)
img_cut = np.zeros(size)
img_cut = img[500:999, 200:699, 2]

noise = np.random.normal(125 ,120 , [200, 200])
factor = 1
noise_scaled = noise * factor

# print(img_cut.shape)
# print(img_cut[:,:,0])


# Display the image
cv2.imshow("Image", noise)

# Wait for the user to press a key
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
