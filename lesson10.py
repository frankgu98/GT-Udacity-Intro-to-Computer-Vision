'''
Generalized Hough Transform
-non analytic models
	-parameters express variations in pose or scale of a fixed but arbitrary shape (fomr a template)
-visual code-word based features
	-not edges but detected templates learned from models

Generalized Hough Transform
-works by usign a Hough Table (or R Table)
	-Training: given a shape (assuming no rotation)
		1. At each boundrary point, compute a displacement vector, r, to a reference point
		2. Measure the gradient angle, θ at the boundrary point
		3. store r in a table indexed by θ
	-Recognition: as you go through the image
		1. At each edge point, measure the gradient angle, θ
		2. Look up all displacements, r, asigned to that θ
		3. vote for reference point at each of those displacements

Generalized Hough Transform Algorithm
-if orientation is known
	for each edge point:
		compute gradient direction θ
		retrieve displacement vectors r to vote for reference point
	find peak in Hough space (x, y)
		-represents reference point with most votes
-if orientation is unknown
	for each edge point:
		for each possible orientation θ*
			compute gradient direction θ
			θ' = θ - θ*
			retrieve displacement vectors r to vote for reference point
	find peak in Hough space (x, y, θ*)
		-represents reference point with most votes
-could also add another parameter, s, for scale, amking Hough space (x, y, θ*, s)

Hough Transform with Visual Codewords
-instead of edges, use feature patches (visual codewords)
-make Hough table that contains displacement vectors to a reference indexed by a feature patch (visual codewords)
-to get visual codewords (essentially building hough table)
	1. build codebook of patches around extracted interest points using clustering
	2. get intereset points in image and map patch around each interest point to closest (most similar) codebook entry
	3. for each codeword, store all displacements to full object's reference point