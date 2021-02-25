import skimage.io
from skimage.viewer import ImageViewer
import numpy as np 

image = skimage.io.imread("maize-roots.tif")

viewer = ImageViewer(image)
viewer.show()


mask = np.ones(shape=image.shape[0:2], dtype="bool")