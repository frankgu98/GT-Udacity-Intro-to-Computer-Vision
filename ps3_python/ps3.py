# ps3
import os
import numpy as np
from numpy.linalg import inv
import cv2
import timeit
import matplotlib.pyplot as plt
import random
from ps3_funcs import *

### 1 ###
"""
# a.

world_points = parse_points("input/pts3d-norm.txt")
image_points = parse_points("input/pts2d-norm-pic_a.txt")
A = get_homo_eq_matrix(world_points, image_points)
M = get_camera_param_matrix_from_params(get_camera_params(A))
print(M)
'''
[[-0.45827554  0.29474237  0.01395746 -0.0040258 ]
 [ 0.05085589  0.0545847   0.54105993  0.05237592]
 [-0.10900958 -0.17834548  0.04426782 -0.5968205 ]]
'''
world_point = np.array(world_points[-1])
image_point = np.array(image_points[-1])
pred_image_point = np.matmul(M, to_homogeneous(world_point))
pred_image_point = to_cartesian(pred_image_point)
print(pred_image_point)
'''
[ 0.14190608 -0.45184301]
'''
residual = np.linalg.norm(image_point - pred_image_point)
print(residual)
'''
0.0015621360462176514
'''

# b.

world_points = parse_points("input/pts3d.txt")
image_points = parse_points("input/pts2d-pic_b.txt")
indices = list(range(20))
M_8 = get_best_camera_param_matrix(8, indices)
print(M_8)
'''
5.345103705317429
15.386851466524934
4.182384062038564
7.0725659516055295
5.338242626916406
3.8539964824851047
8.952278708925483
4.066785101324378
2.614320429365316
8.494973362999971

[[ 7.09348787e-03 -4.18302030e-03 -1.33262929e-03 -8.24228921e-01]
 [ 1.57326484e-03  1.02902163e-03 -7.45013557e-03 -5.66132565e-01]
 [ 7.78740105e-06  3.77314210e-06 -1.93031901e-06 -3.46037733e-03]]
'''

M_12 = get_best_camera_param_matrix(12, indices)
print(M_12)
'''
4.3209306139931645
3.7848133173020804
3.3057026771297973
5.3181322548338965
3.3802650552521163
4.000620939619093
2.8242061955079656
2.868423709910261
3.147786850542939
3.266082766457191

[[ 7.02921949e-03 -4.14074797e-03 -1.10049743e-03 -8.24285020e-01]
 [ 1.54358974e-03  1.04940852e-03 -7.35570967e-03 -5.66053897e-01]
 [ 7.66660511e-06  3.79196913e-06 -1.54961398e-06 -3.44012231e-03]]
'''

M_16 = get_best_camera_param_matrix(16, indices)
print(M_16)
'''
4.618899414359271
3.870490641944431
3.3703515325846083
4.978319747887886
3.9392316224503903
3.2511868007835525
4.017863255703056
3.7766698578510107
3.4104678492545863
3.9169467729373695

[[ 6.89338957e-03 -3.97093230e-03 -1.37102107e-03 -8.27992708e-01]
 [ 1.53913916e-03  1.02367399e-03 -7.24401001e-03 -5.60620756e-01]
 [ 7.56793006e-06  3.71024599e-06 -1.95585483e-06 -3.37420191e-03]]
'''

# 8 point calibration had the largest residuals and larger variance of residuals, likely due to non linearities of camera having larger effect overall on matrix (or generally "bad" points affecting matrix more than in other cases)
# 16 point calibration had very consistent but higher than expected residuals, possibly due to overfitting slightly every time (since most points are used)
# 12 points seemed to be just right and had the matrix with minimum residuals and had most residuals less than those of the 16 point calibration
"""

# c.
M = np.array([[ 7.02921949e-03, -4.14074797e-03, -1.10049743e-03, -8.24285020e-01],
 [ 1.54358974e-03,  1.04940852e-03, -7.35570967e-03, -5.66053897e-01],
 [ 7.66660511e-06,  3.79196913e-06, -1.54961398e-06, -3.44012231e-03]])
Q = M[:, :3]
m_4 = M[:, 3]
C = -1 * np.matmul(inv(Q), m_4)
print(C)
'''
[302.95640472 307.13405837  30.43834092]
'''