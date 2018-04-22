'''
Assumptions (for now)
-parallel (ie. co-planar) image planes
-same focal length
-horizontal epipolar lines
-epipolar lines are at same y
-NORMALLY (irl) would need to rectify images

Correspondence
-need more constraints (other than epipolar constraint)
-these are soft constraints (vs epipolar constraint which is hard constraint)
	-similarity
	-uniqueness
	-ordering
	-disparity gradient is limited (sorta continuous)
-assume
	-most points are in both images
	-image regions for matches are similar in appearance
-dense correspondence
	-finding match everywhere
	-for each pixel/window in left image, compare it to windows in right image and pick window in right that is most similar/least different
		-can use SSD (least different)
			-may have problems with chaning brightness between 2 images
		-can use normalized correlation (most similar)

Correspondence Problem
-problems
	-can have ambiguous match if 
		-window doesn't contain any defining/significant texture
		-window only has lines in the same direction as epipolar lines
			ex. only horizontal lines with assumptions above since horizontal lines would lead to multiple matches along their length
		-wondow is too bright/dark

Effect of Window Size
-could try to fix ambigous match with bigger window size
	-also has problems
-pick window size based on expected image

Uniqueness Constraint
-uniqueness
	-no more than 1 match in right image for each point in left image
	-no more than 1 due to occlusion
		-ex. can only see a pixel in 1 image due to edges of an object

Ordering Constraint
-a, b, c, ... in left should be a, b, c, ... in right
	-only true for single solid surface
-transparent objects
	-see 3B-L3-8
	-not often
-occlusion
	-specifically narrow occluding surface
	-see 3B-L3-8
	-more often

Disparity Between 2 Strips
-simple approach
	-get difference between matching blocks in 2 related strips

Stereo Reseults
-window search isn't great around edges
-better solutions
	-go beyond individual correspondence assignments and optimize all correspondence assignments
		-scanline at a time (DP)
		-full 2D grid (graph cuts)

Dynamic Programming Formulation
-see 3B-L3-11
-can get streaks (since only doing scanline by scanline)

Coherent Stereo on 2D Grid
-can't use DP
-what defines a good stereo correspondence
	1. Match quality
		-want each pixel to find a good appearance match in other image
	2. Smoothness
		-if 2 pixels are adjacent, they usually have similar depth (and similar disparity)
-energy minimization problem
	-has 2 terms
		-data term: square of differences (similar to before)
		-smoothness term: only looking at window of neighbours in disparity image
			-uses ρ function which penalizes roughness up to a max
	-total energy is linear combination of 2 terms
	-want to find minimum total energy
		-done by graph cuts algorithm

Further Challenges
-textureless areas
-occlusions
-violations of brightness contraints (specular reflection)
-really large baselines
-camera clibration erros