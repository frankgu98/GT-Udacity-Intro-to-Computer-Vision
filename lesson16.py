'''
Stereo
-multiple views

Why Multiple Views
-structure and depth are ambigious from a single view
-problem comes from perspective projection, points on same ray appear in same spot on image but may be further or closer  in reality

How do Humans see in 3D
-cues
	-perspective effects
	-shading
	-texture
	-focus/defocus
		-can use how focus changes as aperture changes
	-motion

Stereo
-image from 1 eye is slightly different from other eye
	-can be thought of as recovering depth from motion between eyes
	-infer 3D shape of scene from multiple viewpoints

Basic Idea
-2 slightly different images can give sense of depth from how t hey move

Random Dot Stereograms
-do humans fuse then recognition vs recognition then fuse
	-fuse then recognition (shown by experiment)
	-not based on high level recognition

Estimating Depth with Stereo
-need to consider
	-camera pose
	-image point correspondences

Geometry for a Simple Stereo Simple
-assume image planes are exactly coplanar, known camera parameters
-baseline (separation of camera) B, focal length f, P in scene, Z away from COP, x_L is distance in left camera of point to origin (positive), x_R is distance in right camera of point to origin (negative)
-see #B-L1-9
-Z = f*B/(x_L - x_R)
-x_L - x_R is called disparity
	-inverse relationship with depth
-x_L - x_R = 0 means Z is inf (or generally far away)
	-ex. moon/sun/stars that seem to follow you

Depth from Disparity
-disparity of a point in scene is essentially vector between that point appearing in 2 images
-can make disparity map (D(x, y)), closer values are brighter/higher disparity