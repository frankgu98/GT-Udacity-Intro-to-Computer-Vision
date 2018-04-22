'''
-think of M that simply maps from X to x (x = MX)

Calibration Using Known Points
-place a known object in scne
    -identify correspondence between image and scene
    -compute mapping from scene to image
-resection
    -same math
    -have known points in image and world
    -solve for matrix constants

Direct Linear Calibration Homogeneous
-see 3C-L3-3
    -get homogeneous pair of equations for each point
        -could solve by saying all m's are 0 but not useful
    -overconstrained solution, need to use least squared solution
        -minimize ||A*m||
    -m is only defined up to scale, call it m* and solve assuming it's a unit vector
        -solution given by eigenvector of (A^T)*A with smaller eigenvalue
        -need 6 or more points
            -since 11 DOF
        
SVD Trick/Direct Linear Calibration Transform
-see 3C-L3-5 to 3C-L3-7
-By math trick, eigenvector of A.T*A with smallest eigenvalue is m
    -A is matrix of points, m is camera matrix entries

Direct Linear Calibration Transform (non homogeneous)
-easier to understaand
-not as good as SVD trick
-set bot right matrix entry to 1 (essentially dividing matrix by that entry)
-worse numerical stability
    -if that matrix entry was near 0, dividing matrix by near 0 is bad

Direct Linear Calibration Transform
-advantages
    -simple to formulate and solve
    -minimize algebraic error
-disadvantages
    -doesn't directly give camera params
    -approximate
        -ex. misses radial distortion
    -hard to impose constraints
        -ex. if known focal length, don't want to change it
    -doesn't actually minimize right error function

Geometric Error
-what we actually want to minimize
-sum of distances between actual image locations and predicted image locations
-"best" algorithm
    -hartley and zisserman
    1. linear solution
        a. normalize (option)
        b. Direct Linear Transformation
    2. minimize geometric estimate with output of 1.b) as starting point
        -nonlinear optimization

The Pure Way
-M encodes all parameters so we should be able to find things like camera centre from M
-camera centre is null space of M
-see 3C-L3-11

The Easy Way
-formula
-see 3C-L3-12

Multi Plane Calibration
-take a checkerboard and move it around
-used super often
-advantages
    -only requires a plane
    -don't have to know positions/orientations
    -good code easily available