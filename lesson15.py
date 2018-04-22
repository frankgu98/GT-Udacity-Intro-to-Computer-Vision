'''
Coordinate System
-optical centre of projection (COP) at origin 
-pretend image plane is in front of COP
	-avoids flipping that happens in real cameras
	-no techincally possible in reality but only a model
-camera looks down -z axis (to keep RHR)
-point in world has ray go from it to COP which will intersect imaging/projection plane (PP)
-distance between COP and PP is d (z coord -d due to camera looking down -z axis)
-0 is centre of image (not top left)

Modelling Projection
-(x, y, z) -> (-d*x/z, -d*y/z, -d) -> (-d*x/z, -d*y/z) (on PP, no z coord)
-object further away are smaller in image
-4x3 matrix (for operating on 3D points)

Homogeneous Coordinates
-Division by z above is not linear
	-since z is not constant
-trick: add another coordinate, homogeneous coordinate
	-(x, y, z) -> [x, y, z, 1]
-converting homogeneous to non homogeneous
	-[x, y, z, w] -> (x/w, y/w, z/w)
	-makes homogeneous coords invariant under scaling
		ex [2, 4, 2] represents same point as [1, 2, 1]

Perspective Projection
-can be made into matrix operation using homogeneous coordinates
-see 3A-L2-6
-f is focal length (no longer d)
	-distance from COP to image plane
	-(x, y, z) -> (-f*x/z, -f*y/z, -f) -> (-f*x/z, -f*y/z) (on PP, no z coord)
-due to properties of homogeneous coordinates, scaling projection matrix doesn't change it's output on the image plane (scaling factor is divided out when converting to image coordinates)

Geometric Properties of Perspective Projection
-points go to points
-lines go to lines
	ie. plane intersection
-polygons go to polygons

Parallel Lines
-parallel lines in scene (almost always) meet at vanishing point in image
	-ex. railroad tracks
-seen in math where "starting/reference point" of line doesn't matter, as lines go to inf, they converge to a given point on image plane
	-UNLESS lines don't move in z (closer or towards image plane)
		-ie. they stay paralell to image plane so their projections look the same, parallel
	-will depend on direction of lines in world and orientation of camera

Vanishing Points
-sets of parallel lines on the same plane lead to colinear vanishing points
	-line with vainshing points is called horizon for that plane
		-not necessarily vertical
-hard to align vanishing points properly
-3 point perspective
	-cube in air will have 3 vanishing points (for realistic perspective)

Human Vision
-muller-lyer illusion

Other Models
-special cases of perspective projection
	-orthographic/parallel projection
		-distance from COP is infinite (and objects are also kinda infinite)
		-(x, y, z) -> (x, y)
	-weak perspective
		-perspective effects but between objects but not within an object
		-(x, y, z) -> (f*x/z_0, f*y/z_0) for all (x, y, z) on a given object with a defined scale factor, z_0
			-each object has it's own scale factor