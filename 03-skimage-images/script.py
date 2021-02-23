import skimage.io
import skimage.viewer

image = skimage.io.imread(fname="flowers-before.jpg")
skimage.io.imsave(fname="flowers-after.jpg",arr=image)
