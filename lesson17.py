'''
Stereo Correspondence Constraints
-general case with calibrated cameras
	-not necessarily coplanar/pointed at same spot
	-for image point p in I (with COP) showing scene point P, where could p` in I` be?
		-could be anywhere along ray of p`
		-recall lines project into lines
		-so line containing COP and p should project into line onto I`
		-line on I` is called epipolar line

Terms
-epipolar line
	-line of possible image points p` on I` that could be p on I
	-given by intersection of epipolar plane and image plane (I or I`)
	-come in pairs
-epipolar constraint
	-point on epipolar line l on I must have a match in epipolar line l` on I`, and every point in epipolar line l` on I` must have its match in epipolar line l on I
		-the pairs previously mentioned 
	-see 3B-L2-3
-baseline
	-line joining COPs
-epipolar plane
	-for a point
	-defined by 2 COPs and that point
-epipole
	-intersection of baseline and image plane
	-every epipolar lines intersects epipole
	-may not be on actual image

Epipolar Constraint
-reduces correspondence problem 1D search on epipolar line

Converging Cameras
-need to consider at least 2 points in each camera
-epipole may not be on actual image

Coplanar Cameras/Parallel Image Planes
-epipolar lines will be parallel
-epipole at infinity