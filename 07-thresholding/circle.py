import skimage.io
from skimage.viewer import ImageViewer
import numpy as np

image = skimage.io.imread(fname="trial-020.jpg")

mask = np.ones(shape=image.shape[0:2], dtype="bool")

circle = skimage.draw.circle(1047, 798, radius=100)
mask[circle] = False
rr,cc = skimage.draw.rectangle(start=(198,204), end=(996,285))
mask[rr,cc] = False
image[mask] = 0
viewer = ImageViewer(image)
viewer.show()