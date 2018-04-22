from cv2 import *
from numpy import *
from matplotlib.pyplot import plot, show


img = imread("img.png")

img_red = img[:, :, 2]

noise = (random.normal(0, 10, img_red.shape)).astype(uint8)+100
imshow("noise", noise)

img_red_noisy = normalize(img_red.astype(float), None, -10, 10, NORM_MINMAX) + noise
img_red_noisy = normalize(img_red_noisy, None, 0, 255, NORM_MINMAX).astype(uint8)
#imshow("img_red_noisy", img_red_noisy)

waitKey(0)
destroyAllWindows()

'''
pixel intensities are usually truncated to 255 so for images I1, I2: I1/2+I2/2 ?= (I1+I2)/2 depending on if the pixels are bright enough
also recall that negative intensities will wrap around to max val (255)

noise types
	-salt and pepper noise
		-white and black pixels
	-impulse noise
		-white pixels
	-gaussian noise
		-add to intensity at each pixel based on gaussian dist

plots image with gaussian noise:
~~~
from cv2 import *
from numpy import *
from matplotlib.pyplot import plot, show


img = imread("img.png")

img_red = img[:, :, 1]
imshow("img_red", img_red)

noise = (random.normal(0, 1, img_red.shape))
print(noise.astype(uint8))
plot(noise[100])
show()

imshow("noise", noise)
img_red_noisy = normalize(img_red.astype(float), None, -10, 10, NORM_MINMAX) + noise
img_red_noisy = normalize(img_red_noisy, None, 0, 255, NORM_MINMAX).astype(uint8) # noramlize twice to allow noise to decrease intensity and avoid wrapping
print(img_red_noisy)
imshow("img_red_noisy", img_red_noisy)

waitKey(0)
destroyAllWindows()
~~~

remember magnitude of sigma wrt range of image
normalize to display, not to compute
'''
