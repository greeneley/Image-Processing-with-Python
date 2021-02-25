"""
 * Program to practice with OpenCV drawing methods.
"""
import skimage
import numpy as np
import random
from skimage.viewer import ImageViewer
import random
# create the black canvas
image = np.zeros(shape=(600, 800, 3), dtype="uint8")

# WRITE YOUR CODE TO DRAW ON THE IMAGE HERE
rr, cc = skimage.draw.circle(random.randint(0, 600), 250, radius=100)
image[rr, cc] = [0, 0, 255]
rr, cc = skimage.draw.line(random.randint(0, 600), random.randint(0, 800), random.randint(0,600), random.randint(0,800))
image[rr, cc] = [0, 255, 0]

# display the results
viewer = ImageViewer(image)
viewer.show()
