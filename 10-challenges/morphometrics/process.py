import sys
import skimage.io
from skimage.viewer import ImageViewer

filename = sys.argv[1]
sigma_y = float(sys.argv[2])
sigma_x = float(sys.argv[3])

image = skimage.io.imread(fname=filename, as_gray=True)
viewer = ImageViewer(image)
viewer.show()

blurred = skimage.filters.gaussian(
    image, sigma=(sigma_y, sigma_x), truncate=3.5, multichannel=True
)

viewer = ImageViewer(blurred)
viewer.show()
