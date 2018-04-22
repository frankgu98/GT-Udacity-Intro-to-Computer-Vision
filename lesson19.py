'''
Modelling Projection
-divided by z to project onto image plane
    -non linear
    -fxied by homogeneous coordinates
-homogeneous coordinates
    -could convert into and from easily and use matrices while in homogeneous coords
    -now points are invariant under scale
-want relate coordinate system of world and camera

Geometric Camera Calibration
-want to know relation between camera coordinates to camera coordinates
-composed of 2 transformations
    -extrinsic parameters (camera pose)
        -arbitrary world coords to camera's 3D coords
    -intrinsic parameters
        -camera's 3D coords to 2D image plane via projection

Rigid Body Transformation
-camera pose has 6 degrees of freedom
        -3 translation, 3 rotation

Notation
-superscript/scanline/macron is "in coordinates of __"
    ex. A⎻X is X in A's coordinates/frame
-translation
    -for 2 translated coordinates systems A and B, point P in A's coords can be transformed into B's coords through
        -vector addition
            - B⎻P = A⎻P + B⎻O_A
        -matrices 
            -see 3C-L1-5
                -1 as bottom rightmost entry
    -commutative

Rotation
-for 2 rotated coordinates systems A and B, point P in A's coords can be transformed into B's coords through
    -rotation operator
        - B⎻P = (B/A)⎻R * A⎻P
            - (B/A)⎻R is frame A in coords of B

R Matrix
-how much each component of A is in each component of B
    -(B/A)⎻R = [B⎻i_A, B⎻j_A, B⎻k_A]
        -orthogonal
        -inverse equals transpose
        -where each basis vector go
-order matters in rotation

Rotation in Homogeneous Coordinates
-done by matrix multiplication
    -see 3C-L1-9
        -1 as bottom rightmost entry

Rigid Transformation
-operators on regular coordinates
    -B⎻P = (B/A)⎻R * A⎻P + B⎻O_A
-matrix multiplication
    -see 3C-L1-10
    -does both at once as a single matrix
        -rotate then offset
    -transformation, T, from B to A is simply inverse of tranformation from A to B
        -(B/A)⎻T = ((A/B)⎻T)^-1

Translation and Rotation
-(C/W)⎻T is called extrinsic parameter matrix
    -decribes how to go from world coords to camera coords
    -still 6 degrees of freedom
