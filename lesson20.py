'''
Intrinsic Parameters
-3D camera coords to 2D image plane coords

Ideal vs Real Intrinsic Parameters
-ideal
    -u = f*x/z, v= f*y/z
-real
    -pixels are in arbitrary spatial units
        -u = α*x/z, v = α*y/z
    -pixels aren't necessarily square
        -u = α*x/z, v = ß*y/z
    -don't know origin of our camera pixel coordinates
        -u = α*x/z + u_0, v = ß*y/z + v_0
    -u and v might not be perpendicular
        -v` = v/sinθ, u` = u - v`*cosθ = u - v*cotθ
        -substituting in more ideal u, v into u`, v` to get final u, v
        -u = α*x/z - α*cotθ + u_0, v = ß*y/(z*sinθ) + v_0
            -not ß*cotθ on u???? 
    -total 5 DOF

Improving Intrinsic Parameters
-use homogeneous c
    -p` = ĸ*c⎻p
    -ĸ, made of 5 DOF (can be 3x3 or 3x4)
        -f: focal length (used with aspect ratio to derive pixel sizes)
        -s: skew
        -a: aspect ratio
        -c_x, c_y: offset 
-see 3C-L2-3
-if square pixels, no skew, and optical cenre is in middle
    -made of 1 DOF
        -f: focal length

Combining Extrinsic and Intrinsic Matrices
-going from world to homogeneous image coords
    -p` = ĸ*((C/W)⎻R*(C/W)⎻t)*W⎻p
        -consider (C/W)⎻R * (C/W)⎻t as 3x4 rather than 4x4 since last 1 is dropped
        -ĸ is 3x3
    -M = ĸ*((C/W)⎻R*(C/W)⎻t)

Other Ways to Write Matrix
-projectively similar
    -ie. invariant up to scaling
-see 3C-L2-6
-find m elements

Camera Parameters
-camera (and matrix) is described by 11 DOF
    -extrinsics
        -translation
        -...
    -intrinsics
        -...
-projection equation
    -maps from world to pixel value