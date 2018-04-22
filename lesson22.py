'''
2D Transformations
-translation
    - x` = x + t
    - or homogeneous matrix multiplications
-euclidean
-similarity
-affine
-projective

Special Projective Transformations
-for 2D images, it's a 3x3 matrix applied to homogeneous coordinates
-see 3D-L1 for matrices
-translation
    -preserves
        -lengths/areas
        -angles
        -orientations
        -lines
            -lines stay lines
-euclidean (rigid body rotation)
    -preserves
        -lengths/areas
        -angles
        -lines
-similarity (trans, rotate, scale)
    -4 DOF
    -preserves
        -lengths/areas
        -angles
        -lines
-affine (trans, rotate, scale, skew)
    -essentially maps any 3 points to any other 3 points
    -6 DOF
    -preserves 
        -parallel lines
        -ratio of areas
        -lines

Projective Transformations
-recall, these are homogeneous coords
-full transformation is called general projective transform/homography
    -8 DOF
    -see 3D-L1-4
    -preserves
        -lines
        -cross ratios

Quiz
-if know a transform is pure translation, then need 1 pair of corresponding points to compute transformation/matrix
    -2 unk, 2 eq (from 2 components in point)
-if know a transformation is affine, then need 3 pairs of points to compute transformation
    -6 unk
-if know a transformation is a homography, then need 4 pairs of points to compute transformation
    -8 unk
-all of this assumes all linear mappings