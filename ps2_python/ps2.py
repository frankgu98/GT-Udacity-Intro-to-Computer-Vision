# ps2
import os
import numpy as np
import cv2
import timeit
import matplotlib.pyplot as plt
from disparity_ssd import disparity_ssd
from disparity_ncorr import disparity_ncorr


'''
## 1-a
# Read images
L = cv2.imread(os.path.join('input', 'pair0-L.png'), 0) * (1.0 / 255.0)  # grayscale, [0, 1]
R = cv2.imread(os.path.join('input', 'pair0-R.png'), 0) * (1.0 / 255.0)

# Compute disparity (using method disparity_ssd defined in disparity_ssd.py)
start = timeit.default_timer()
D_L = disparity_ssd(L, R)
print(timeit.default_timer() - start)
D_R = disparity_ssd(R, L)

# TODO: Save output images (D_L as output/ps2-1-a-1.png and D_R as output/ps2-1-a-2.png)
# Note: They may need to be scaled/shifted before saving to show results properly

cv2.imwrite("output/ps2-1-a-1.png", cv2.normalize(D_L, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)) # UINT8 NOT INT, PLEASE STOP FORGETTING
cv2.imwrite("output/ps2-1-a-2.png", cv2.normalize(D_R, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)) 

# TODO: Rest of your code here



### 2 ###

# a.
L = cv2.imread("input/pair1-L.png", 0) * (1.0 / 255.0)  # grayscale, [0, 1]
R = cv2.imread("input/pair1-R.png", 0) * (1.0 / 255.0)

start = timeit.default_timer()
D_L = disparity_ssd(L, R, (15, 15), 180)
print(timeit.default_timer() - start)

D_R = disparity_ssd(R, L, (15, 15), 180)


cv2.imwrite("output/ps2-2-a-1.png", cv2.normalize(D_L, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8))

cv2.imwrite("output/ps2-2-a-2.png", cv2.normalize(D_R, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)) 

# b.
# My version detected the objects ok but left a lot of splotches. also some black/white from areas with no corresponding part in right image


### 3 ###

# a.
L = cv2.imread("input/pair1-L.png", 0) * (1.0 / 255.0)  # grayscale, [0, 1]
R = cv2.imread("input/pair1-R.png", 0) * (1.0 / 255.0)

L_noisy = cv2.normalize(L+(np.random.normal(0, .05, L.shape)), None, 0, 1, cv2.NORM_MINMAX)
#cv2.imshow("L_noisy", L_noisy)

start = timeit.default_timer()
D_L = disparity_ssd(L_noisy, R, (15, 15), 160)
print(timeit.default_timer() - start)
D_R = disparity_ssd(R, L_noisy, (15, 15), 160)

cv2.imwrite("output/ps2-3-a-1.png", cv2.normalize(D_L, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8))
cv2.imwrite("output/ps2-3-a-2.png", cv2.normalize(D_R, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)) 
# worse detection, even more splotchy

# b.
L = cv2.imread("input/pair1-L.png", 0) * (1.0 / 255.0)  # grayscale, [0, 1]
R = cv2.imread("input/pair1-R.png", 0) * (1.0 / 255.0)

L_contrast = 1.1*L

start = timeit.default_timer()
D_L = disparity_ssd(L_contrast, R, (15, 15), 160)
print(timeit.default_timer() - start)
D_R = disparity_ssd(R, L_contrast, (15, 15), 160)

cv2.imwrite("output/ps2-3-b-1.png", cv2.normalize(D_L, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8))
cv2.imwrite("output/ps2-3-b-2.png", cv2.normalize(D_R, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)) 
# missed a lot of matches now
'''

'''
### 4 ###

# a.
L = cv2.imread("input/pair1-L.png", 0) * (1.0 / 255.0)  # grayscale, [0, 1]
R = cv2.imread("input/pair1-R.png", 0) * (1.0 / 255.0)

#L_noisy = cv2.normalize(L+(np.random.normal(0, .05, L.shape)), None, 0, 1, cv2.NORM_MINMAX)
#cv2.imshow("L_noisy", L_noisy)

start = timeit.default_timer()
D_L = disparity_ncorr(L, R, (15, 15), 160)
print(timeit.default_timer() - start)
D_R = disparity_ncorr(R, L, (15, 15), 160)

cv2.imwrite("output/ps2-4-a-1.png", cv2.normalize(D_L, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8))
cv2.imwrite("output/ps2-4-a-2.png", cv2.normalize(D_R, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8))
# a lot sharper around edges, still some weird artifacts on left side (stuff which has no match in right image due to occlusion)

# b.

L = cv2.imread("input/pair1-L.png", 0) * (1.0 / 255.0)  # grayscale, [0, 1]
R = cv2.imread("input/pair1-R.png", 0) * (1.0 / 255.0)

L_noisy = cv2.normalize(L+(np.random.normal(0, .05, L.shape)), None, 0, 1, cv2.NORM_MINMAX)
#cv2.imshow("L_noisy", L_noisy)

start = timeit.default_timer()
D_L = disparity_ncorr(L_noisy, R, (15, 15), 160)
print(timeit.default_timer() - start)
D_R = disparity_ncorr(R, L_noisy, (15, 15), 160)

cv2.imwrite("output/ps2-4-b-1.png", cv2.normalize(D_L, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8))
cv2.imwrite("output/ps2-4-b-2.png", cv2.normalize(D_R, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)) 
# also not great actually, edges are there though

L_contrast = 1.1*L

start = timeit.default_timer()
D_L = disparity_ncorr(L_contrast, R, (15, 15), 160)
print(timeit.default_timer() - start)
D_R = disparity_ncorr(R, L_contrast, (15, 15), 160)

cv2.imwrite("output/ps2-4-b-3.png", cv2.normalize(D_L, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8))
cv2.imwrite("output/ps2-4-b-4.png", cv2.normalize(D_R, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)) 
# pretty much no difference compared to ncorr with no contrast
'''


### 5 ###

# a.
L = cv2.imread("input/pair2-L.png", 0) * (1.0 / 255.0)  # grayscale, [0, 1]
R = cv2.imread("input/pair2-R.png", 0) * (1.0 / 255.0)

start = timeit.default_timer()
D_L = disparity_ncorr(L, R, (15, 15), 160)
print(timeit.default_timer() - start)
D_R = disparity_ncorr(R, L, (15, 15), 160)

cv2.imwrite("output/ps2-5-a-1.png", cv2.normalize(D_L, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8))
cv2.imwrite("output/ps2-5-a-2.png", cv2.normalize(D_R, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8))

start = timeit.default_timer()
D_L = disparity_ssd(L, R, (15, 15), 160)
print(timeit.default_timer() - start)
D_R = disparity_ssd(R, L, (15, 15), 160)

cv2.imwrite("output/ps2-5-a-3.png", cv2.normalize(D_L, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8))
cv2.imwrite("output/ps2-5-a-4.png", cv2.normalize(D_R, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8))