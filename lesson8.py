'''
Parametric Model
-can represent a class of instances where each instance is defined by a value of the parameters
-to fit (ie. to find it in an image)
	-choose parametric model to represent a set of features
		-ie. think about how to go from parameters to actual thing being represented
	-membership criterion is not local
		-ie. can't determine if a point belongs to a model by only looking at point
	-computational ocmplexity is important
		-ie. not feasible to examine every possible parameter setting 

Line Fitting
-difficulties (ie. why we can't just find edges)
	-extra edge points (clutter), multiple possible models
	-only some parts of line are detected and other parts are missing
	-noise in measured edge points, orientations

Voting
-general technique where we let features vote for all model that are compatible with it
	1. iterate through features (edge points), letting them cast votes for model parameters that fit it
	2. look for model parameters that receive a lot of votes
-how it works
	-noise and clutter features will cast votes too but will typically be inconsistent with majority given by good features
		-ie. their votes will be spread out and not let a "candidate" be chose
	-allows for some features not being observed since model can span multiple fragments that do vote for it

Fitting Lines
-need to answer:
	-given points that belong to a line, what is the line?
	-how many lines are there?
	-which points belong to which lines?
-Hough Transform
	-voting technique that answers above questions
	-main idea
	 	1. each edge point votes for compatible lines (any lines that go through it)
		2. look for lines with a lot of votes
	-keeping track of which points voted for which lines tells you which points belong to which lines

Hough Space
-ie Hough Parameter Space
-line in image corresponds to point in Hough Space
	- y = m_0 * x + b_0 in Cartesian Space -> (m_0, b_0) in Hough Space
-point in image (x_0, y_0) corresponds to line in Hough Space
	- y_0 = m*x_0 + b  ->  b = -x_0 * m + y_0
-if we have another point in image space (x_1, y_1)
	-line in Hough space is b = -x_1 * m + y_1
-the line that is consisten with both (x_0, y_0) and (x_1, y_1) is given by the intersection of the 2 corresponding lines in Hough Space
	-since that Hough space point is the image space line that is consistent with being on both points
-so voting works by separating Hough space into binsd and counting number of Hough space lines going through each bin (Which is a vote for that bin)
	1. let each edge point in image space vote for a set of possible parameters in Hough space
	2. Accumulate votes into discrete bin
	3. Parameters with most votes indicate line in image space
-will use polar representation of line due to limitations of y=m*x+b

Polar Representation of Lines
-2 parameters
	-d: perpendicular distance from line to origin
	-θ: angle perpendigular makes with x axis
		-could also be angle line makes with x axis
	-if d can be positive or negative, θ can be 0 to 180, if d is only positive, θ can be 0 to 360
-it can be shown that for any (x, y), x*cosθ + y*sinθ = d
-now point in image space is sinusoidal segment in Hough space
	-so, votes are intersecting sinusoids in a certain range of d, θ (since actually would be infinitely many such bins)

Hough Transform Algorithm
-Use polar parameterization: x*cosθ - y*sinθ = d and a Hough Accumulator Array (vote tabulator)
1. Initialize H[d][θ] = 0
2. For each edge point in E(x, y) (edge points) in the image (voting)
	for θ in 0 to 180
		d = x*cosθ + y*sinθ
		h[d][θ]+=1
3. Find values of (d, θ) where H[d][θ] is maximum
4. The detected line in the image is d = x*cosθ + y*sinθ
-space complexity
	-for n dimension and k bins, we need k^n bins 
-time complexity
	-for m=number of edge points, O(m)
-more intersections = longer line
-to find more meaningful lines we could
	-in looking for hough peaks
		-increase threshold for hough peaks
			-increase min length of line (by increasing number of pixels that voted for that line)
		-neighbourhood size
			-size of neighbourhood (of Hough Accumulator Array) where local max is being considered
			-means that similar lines will be combined/surpressed
	-in filling in gaps in line segments
		-could increase min length between segments
			-focusses on longer lines
-need to do more steps to find line segments from lines

Impact of Noise
-small amounts of noise can spread out peaks and throw Hough transform algorithm off
	-could smooth Hough space output (with the sinusoids)
	-then find rough peak area
	-then do Hough transform again focusing only on that area (ie. set of lines in image)
-with only noise/complete garbage
	-need to consider when a peak is real

Extensions to Hough Transform
-using the gradient
	1. Initialize H[d][θ] = 0
	2. For each edge point in E(x, y) (edge points) in the image (voting)
		θ = gradient at (x, y) // perp to edge = θ of line (draw it out), could also keep for loop and use range of θ's around this value
		d = x*cosθ - y*sinθ
		h[d][θ]+=1
	3. Find values of (d, θ) where H[d][θ] is maximum
	4. The detected line in the image is d = x*cosθ - y*sinθ
-more votes for stronger edges
-change sampling of d, θ (changing bin size)
	-coarse bins -> fine arrays only in those areas/for those lines
-same procedure can be used for any other shape	