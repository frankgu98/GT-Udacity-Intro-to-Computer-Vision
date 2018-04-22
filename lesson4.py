'''
An operator or system H is linear if for f1, f2, a
	1. H(f1+f2) = H(f1) + H(f2)
	2. H(af1) = aH(f1)
	the filtering shown before is linear

Impulse function
	-in discrete world
		function with value 1 at a single location and 0 elsewhere
	-in continuous world
		function with integral over a single point (infinite at point) at 1 and 0 elsewhere

Impulse response
	-"put in" impulse into black box/system, H, what comes out is H's impulse response, h(x)
	-h(x) can describe H since any function input can be thought of as infinite linear combination of shifted impulse functions

Impulse response in images
	-impulse funciton is 1 at a single pixel and 0 elsewhere
	-for G = HⓍF (CORRELATION, L TO R, T TO B), with F as the impulse function will lead to H flipped across diagonal in G
	-for G = H✮F (CONVOLUTION, R TO L, B TO T), with F as impusle function will lead to H correctly oriented in G

Correlation (Ⓧ) vs Convolution (✮)
	-runs rotate kernel 180 and then run it over left to right, top to bot
	-when applying filters/kernels, actually doing convolution, not correlation
	-for symmetric kernels, correlation and convolution are the same
	-computational complexity: O(M^2N^2) where matrices are MxM and NxN
	-G = H✮F = F✮H = F when H is the impulse function
		-ie. the impulse function is the identity of the convolution operator
			-shifted impulse filter will simply shift image by where the 1 is wrt refence point of kernel
	-both operators are shift invariant
		-ie. will operate the same way on same pixels in different parts of image
	-both operators as linear
		-so filtering is also linear
	-both operators are commutative, associative
	-for D being differentiation operator
		-D[f✮g] = D[f]✮g = f✮D[g] 

Separability
	-sometimes you can get square kernel H by convolving row vector r with column vector c
		-ie. c✮r = H
		-called a linearly separable kernel
		-for G = H✮F = (c✮r)✮F = c✮(r✮F), F,G are MxM and H is NxN
			-normally O(M^2N^2), now O(2MN^2)

Boundary issues
	-what to do when filter goes over edge of picture?
		-undefined unless we define it
		-depends on how big do you want output?
			-bigger than image (matlab: full)
				-output as filter just touches image
			-same size as image (matlab: same)
				-output as filter reference pixel enters original image pixels
			-smaller than image (matlab: valid)
				-output when entire filter is in image
	-usually use same size as image
	-how to deal with overhang?
		-clip
			-assume outside image is black
		-wrap around
			-wraps image from opposite side over
			-assumes image is periodic signal
		-copy edge/replicate
			-extend out edge values
			-technically statistacally sketchy but usually fairly acceptable looking (no obvious edge)
		-reflect across edge
			-flip/mirror out edge values
			-also pretty good looking (no obvious edge)
			-more statistically valid since "The distribution of color or intensity values is not likely to change much across a small region, so padding with pixel values along the boundary is a good approximation of what might've actually been there if the image was larger."

Sharpening filter
	-kernel has middle high, sides negative
	-take original (with a bit of extra brightness) and subtracting a blurry version of original
	-ex. H = [[0, 0, 0], - (1/9)*[[1, 1, 1],
			  [0, 2, 0],		  [1, 1, 1],
			  [0, 0, 0]]		  [1, 1, 1]]

			  ^original  ^subtract  ^blurry version of original
	-would it be better with gaussian blurry vs averaging blurry?

Other type of noise
	-gaussian filter works for independent noise centered at 0 (gaussian noise - CLT?) but needs other filters for other types of noise
		-maybe not linear filter
	-salt and pepper noise
		-ie. random pixels replaced with black or white
		-to get rid of outliers (black/white) use median
			-replace reference pixel with median of pixel in kernel
			-also assumes that images don't change pixel value that often/are relatively continuous
			-no new pixel values introduced
			-removes spikes (why it's good for salt and pepper noise and generally random impulses)
			-not linear
			-preserves sharp edges

'''
