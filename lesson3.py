'''
-noise is hard to remove since we don't know the exact noise function to subract it (also values may be clipped)
Techniques to get rid of noise
	1. moving average OR correlation filtering-uniform weight
		-average pixels near i to get value at i
		-assumptions
			1. true value of pixel is similar to true value of nearby pixels
			2. noise in each pixel is independent
			-makes averaging seem to work since (hopefully) nearby pixels are right colour with a bit of noise that will (hopefully) average to 0
		-not great at smoothing due to hard edges of square and variability which can abuse equal weighting
			will create sharp edges due to sharp on/off nature of filter


	2. weighted moving average OR correlation filtering-nonuniform weight OR crosscorrelation
		-average pixels near i to get value at i with more weight on pixels close to i
		-usualy weight mask (kernel) has odd side length to have centre at desired pixel	 
		-assumption
			1. true value of pixel is most similar to true value of nearest pixels
			2. noise is independent
		-in math: G = HⓍF
			G is cross correlated function/result
			H is kernal/mask/matrix of weights
			F is original function
		-if kernel weights are approximately gaussian (a bit stricter than simply reducing when further away), then kernel can be called gaussian filter
	-mostly just blurs things

Gaussian filters
	-[A] = k*[gaussian(k1, k2)] where k1 and k2 are in range of kernel size wrt reference point
		usually reference point corresponds to centre of kernel as filter goes over image
	-good for proper blurring		
		big kernel == big sigma in kernel (kernel dimensions are noted as kernel size and should be appropriate to sigma)
	-sigma is very important since it defines
	-this sigma is in space, whereas previous sigma for noise was in intensity
'''
from cv2 import *
from numpy import *
from matplotlib import pyplot

img = imread("img.png")
img = img[:, :, 0]
kernel = array([[1, 1, 1, 1, 1],
				[1, 1, 1, 1, 1],
				[1, 1, 1, 1, 1],
				[1, 1, 1, 1, 1],
				[1, 1, 1, 1, 1]]) / 25 
blurred = filter2D(img, -1, kernel)
imshow("img", img)
imshow("blurred", blurred)
waitKey(0)
destroyAllWindows()

				