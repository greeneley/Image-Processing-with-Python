"""
 * Python program to apply a mask to an image.
 *
"""
import numpy as np
import skimage
from skimage.viewer import ImageViewer

# Load the original image
image = skimage.io.imread("03-remote-control.jpg")

# Create the basic mask
mask = np.ones(shape=image.shape[0:2], dtype="bool")

# Draw a filled rectangle on the mask image
rr, cc = skimage.draw.rectangle(start=(103,1140), end=(1826,1646))
mask[rr, cc] = False

# Apply the mask and display the result
image[mask] = 0
viewer = ImageViewer(image)
viewer.show()
