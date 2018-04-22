'''
Derivative of 2D Gaussian Filter
	-to do the previous derivative of the filter trick in 2D, we have to specift the direction of the derivative
		-ie do IⓍ(gⓍh_x) instead of (IⓍg)Ⓧh_x
			-I is image, g is gaussian smoothing function, h_x is gradient operator in x
		-this is faster since g and h_x are typically small compared to I so fewer operations are done
		-also can reuse gⓍh_x
		-for the resulting derivative of the smoothing filter filter, be careful if it should be used for correlation of convolution
			-if it's increasing at 0 going in the positive direction of the picture, it's for correlation
				-ex. for (gⓍh_x) if the right side has a peak and the left side has a valley, it's for correlation
				-y direction will be problematic
	-for smaller sigma, fine and larger variations will be detected
	-for larger sigma, only larger variations will be detected

Getting Edges from Gradients
	in general:
		1. Smoothing derivative (to suppress noise) and computing gradient
		2. Thresholding to find regions of "significant" gradient
		3. "Thinning" to get localized edge pixels
			-ie. define exact edge pixels from fat gradient
		4. Connect edge pixels (if you want a conntected contour)

Canny edge operator
	1. Filter image with derivative of Gaussian
	2. Find magnitude and orientation of gradient
	3. Threshold gradient
	4. Non-maximum suppression
		-ie. thinning
		-thin multi-pixel wide ridges to single pixel width
		-"if i've got a bunch of points that exceed a threshold locally, pulls out the points that exceeds it the most"
			-works by taking "cross-section" of gradient that exceeds threshhold along that gradient direction and taking the local maximum
				-may need to compare interpolated points
	5. Linking and thresholding (hysteresis)
		-define 2 thresholds, low and high
		-use high threshold (done earlier) to start edge curves and low threshold to continue them
		1. Apply a high threshold to detect strong edge pixels
		2. Link strong edge pixels to find strong edges
		3. Apply a low threshold to find weak but plausible edges
		4. Extend strong edges to follow weak edge pixels
			-does not extend edges with only weak pixels
			-assumes that true edges will have at least some strong pixels in them
	-better than most operators at finding edges that one would want for future processing
	-sigma can be specified which has the effect described above
	-fairly resilient to noise
	-most frequently used

Single 2D Edge Detection Filter
	-another way to get edges is to use equivalent of d2H/dx2 (sombrero) in 2D
	-can take multiple derivatives in multiple directions, but for this, simply use laplacian
		-ie. for f as image, h as gaussian filter use: ∇2f = d2f/dx2 + d2f/dy2

