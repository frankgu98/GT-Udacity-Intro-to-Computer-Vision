'''
Hough Transform for Circles
-Circles
	-centre (a, b), radius r
		- (x-a)^2 + (y-b)^2 = r^2
-if we know the circle's radius, the hough space is a, b
	-if we know a point on the circle, it votes for all the a, b that are r around it (since to be on the circle, it has to be r away from the centre (a,b))
	-ie. point in image space is circle in hough space
	-collecting votes should lead to a centre point
	-for an incorrect radius for a given circle, there will be a bright ring of "centres" surrounding the actual circle's centre as smaller/larger circle is somewhat fit to given circle
-if we don't know the radius and we don't know the gradient
	-hough space now has 3 parameters, a, b, r
	-now, each image point votes for an entire cone surface in hough space
	-will be painful/slow due to large voting space
-if we don't know the radius and we know the gradient
	-hough space still has 3 paramaters a, b, r
	-however, voting only happens along 3D line since centre must be on line

Algorithm
for every edge pixel (x, y):
	for every possible radius value (r):
		for every possible gradient value (θ): # or jsut use estimated gradient
			a = x - r*cosθ
			b = y + r*sinθ
			H[a, b, r] += 1

Voting Practical Tips
-minimize irrelevant edges
	-take edge points with significant gradient magnitude
-choose good grid size/discretization
	-too coarse: many false votes
	-too fine: miss shapes (circles, lines, etc)
-can vote for neighbouring bins
	-like smoothing in accumulator array
	-gaussian voting?
-using gradient reduces free params from 3 to 2
-if you want find which points voted for which bins, keeps track of votes

Pros and cons of Hough Transform
-pros
	-all votes processed independently, so can deal with occlusion/partical covering of objects
	-some robustness against noise since noise points are unlikely to consistenly vote for any bin
	-can detect multiple instances of an object in 1 pass
-cons
	-complexity of search time is exponential wrt # or model params
		-even ~4 params will be slow
	-similar but non target shapes can consistenly vote for bins
	-quantization: hard to pick bin size