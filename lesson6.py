'''
-edges in an image are important and convey a lot of info

Causes of Edges
	-surface normal discontinuity
		-ie. faces meeting
	-depth discontinuity
		-ie. faces turns away into something behind it
	-surface colour discontinuity
		-ie. reflectance due to colour/texture change on a surface
		-ie. change in reflectance function
		-illumination discontinuity
		-ie. shading

Edge Detection
	-convert function/image into a reduced set of pixels that are important elements of the picture
	-edges are steep cliff when images are surface plotted
	-so to detect edges look for neighbourhood with strong signs of change
		-how big is neighbourhood?
		-what is a change?
			-derivatives

Derivatives and Edges
	-finding edges is usually done by finding peaks in derivatives
		-found by filtering
		-filter image with operator to find peaks in derivatives

Differential Operators
	-differential operators: when applied to image returns some derivatives
		-we should use correlation when computing gradients so it's easier to know which direction derivatives are going
	-model operators as kernels that compute image gradient function
	-threshhold the resulting gradient function to pick edge pixels
	-gradient: vectors containing partial derivatives of a function
		-▽f =  [df/dx, df/dy]
		-direction of gradient is given by direction most rapid ascent in intensity
	-discrete gradient: for discrete data, have to approximate with finite differences
		-right derivative
			-df/dx = (f(x+1, y) - f(x, y)) / 1 = f(x+1, y) - f(x, y)
			-as if ε = 1
			-stepping to right
			-can tell image is of right derivative by looking how it resonds to changes mostly in x vs changes mostly in y
				-ie. edges are up to down vs left to right
	-kernel or left/right derivative
		- H = [[ 0, 0],
		       [-1, 1],
		       [ 0, 0]]
		-no middle pixel!
	-can get middle by taking average of H above as left and right derivatives wrt a point (reference is entry with -1, then entry with 1)
		- H = [[   0, 0,  0],
			   [ -.5, 0, .5],
			   [   0, 0,  0]]
	-ex. Sobel Gradient
		- S_x = .125 * [[-1, 0, 1],
			   			[-2, 0, 2],
			   			[-1, 0, 1]]
		- S_y = .125 * [[ 1,  2,  1],
			   			[ 0,  0,  0],
			   			[-1, -2,  1]]
		-also looks at area around reference pixel
			-takes advatange of usually relatively continuous images
			-reduces noise?
	-ex. Prewitt
	-ex. Roberts

Real Data
	-simply applying differential operators will not let you find peaks
		-noise will make gradient +/- all over the place
	-need to smooth function F with filter H, then apply differential operator
		-ie. G = d/dx (HⓍF) = dH/dx Ⓧ F
		-using associative and differentiation properties of convolution
	-this leads to edges at peaks, to find peaks, need to diffentiate again
		-ie. B = d/dx (G) = d/dx (dH/dx Ⓧ F) = d2H/dx2 Ⓧ F
		-now edges are where a strong slope meets 0
		-general 0 means constant or linear in original image which are not edges
		-for gaussian H, d2H/dx2 resembles an upside down sombrero