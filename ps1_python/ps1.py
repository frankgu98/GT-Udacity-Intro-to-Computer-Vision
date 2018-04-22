from cv2 import * # BGR FORMAT
from numpy import *
from numpy import cos as npcos, sin as npsin
from matplotlib import pyplot as plt
from timeit import default_timer
from ps1_funcs import *


'''
### 1 ###

img_gray = cvtColor(imread("input/ps1-input0.png"), COLOR_BGR2GRAY)
edges = Canny(img_gray, 100, 150).astype(float)/255 # seemingly only works on uint8
imwrite("output/ps1-1-a-1.png", (255*edges).astype(uint8))



### 2 ###

# a.
hough_acc = normalize(hough_lines_acc(edges), None, 0, 255, NORM_MINMAX).astype(uint8)
imwrite("output/ps1-2-a-1.png", hough_acc)


# b.
hough_acc = cvtColor(imread("output/ps1-2-a-1.png"), COLOR_BGR2GRAY).astype(float)/255
peaks_and_locs = hough_peaks_and_locs(hough_acc, 12)
for peak_and_loc in peaks_and_locs:
	circle(hough_acc, peak_and_loc[1][::-1], 6, 1, 1)
imwrite("output/ps1-2-b-1.png", normalize(hough_acc, None, 0, 255, NORM_MINMAX).astype(uint8))


# c.
img_lines = hough_lines_draw(img_gray, [peak_and_loc[1] for peak_and_loc in peaks_and_locs])
imwrite("output/ps1-2-c-1.png", img_lines)


# d.
# used default params for everything, worked fine for basic application



### 3 ###

# a.
img_gray = cvtColor(imread("input/ps1-input0-noise.png"), COLOR_BGR2GRAY)
img_gray_smoothed = GaussianBlur(img_gray, (21, 21), 0) # maybe smooth operators instead?
imwrite("output/ps1-3-a-1.png", img_gray_smoothed)


# b.
edges_gray = Canny(img_gray, 100, 150) # seemingly only works on uint8
imwrite("output/ps1-3-b-1.png", edges_gray)

edges_gray_smoothed = Canny(img_gray_smoothed, 40, 50) # seemingly only works on uint8
imwrite("output/ps1-3-b-2.png", edges_gray_smoothed)


# c.
hough_acc = hough_lines_acc(edges_gray_smoothed, theshold = 0.7*amax(edges_gray_smoothed))
peaks_and_locs = hough_peaks_and_locs(hough_acc, 12)
hough_acc = cvtColor(normalize(hough_acc, None, 0, 255, NORM_MINMAX).astype(uint8), COLOR_GRAY2BGR) # to draw green circles
for peak_and_loc in peaks_and_locs:
	circle(hough_acc, peak_and_loc[1][::-1], 6, (0, 255, 0), 1)
imwrite("output/ps1-3-c-1.png", hough_acc)

img_lines = hough_lines_draw(img_gray, [peak_and_loc[1] for peak_and_loc in peaks_and_locs])
imwrite("output/ps1-3-c-2.png", img_lines)



### 4 ###

# a.
img_gray = cvtColor(imread("input/ps1-input1.png"), COLOR_BGR2GRAY)
img_gray_smoothed = GaussianBlur(img_gray, (11, 11), 0) # maybe smooth operators instead?
imwrite("output/ps1-4-a-1.png", img_gray_smoothed)


# b.
edges_gray_smoothed = Canny(img_gray_smoothed, 40, 50) # seemingly only works on uint8
imwrite("output/ps1-4-b-2.png", edges_gray_smoothed)


# c.
hough_acc = hough_lines_acc(edges_gray_smoothed.astype(float)/255)
peaks_and_locs = hough_peaks_and_locs(hough_acc, 8) # seemingly 2 lines for each desired line, 180 deg apart, 1 is off screen
hough_acc = cvtColor(normalize(hough_acc, None, 0, 255, NORM_MINMAX).astype(uint8), COLOR_GRAY2BGR) # to draw blue circles
for peak_and_loc in peaks_and_locs:
	circle(hough_acc, peak_and_loc[1][::-1], 6, (0, 255, 0), 1) # reverse since circle() uses x, y but uout is in row, col
imwrite("output/ps1-4-c-1.png", hough_acc)

img_lines = hough_lines_draw(img_gray, [peak_and_loc[1] for peak_and_loc in peaks_and_locs])
imwrite("output/ps1-4-c-2.png", img_lines)


# d.
# used default params but needed to find double intended lines due to symmetry, also had to take sobel_mag < 0.45*amax(sobel_mag) as crit points due to noise



### 5 ###

# a.
img_gray = cvtColor(imread("input/ps1-input1.png"), COLOR_BGR2GRAY)
img_gray_smoothed = GaussianBlur(img_gray, (11, 11), 0) # maybe smooth operators instead?
imwrite("output/ps1-5-a-1.png", img_gray_smoothed)

edges_gray_smoothed = Canny(img_gray_smoothed, 40, 50) # seemingly only works on uint8
imwrite("output/ps1-5-a-2.png", edges_gray_smoothed)

radius = 28

hough_acc = hough_circles_acc(edges_gray_smoothed, radius, img_gray_smoothed)


peaks_and_locs = hough_peaks_and_locs(hough_acc, 5, threshold = 0.2*amax(hough_acc)) # seemingly 2 lines for each desired line, 180 deg apart, 1 is off screen

img_circles = cvtColor(normalize(img_gray, None, 0, 255, NORM_MINMAX).astype(uint8), COLOR_GRAY2BGR) # to draw blue circles
for peak_and_loc in peaks_and_locs:
	circle(img_circles, peak_and_loc[1][::-1], radius, (0, 255, 0), 1)
imwrite("output/ps1-5-a-3.png", img_circles)


# b.
img_gray = cvtColor(imread("input/ps1-input1.png"), COLOR_BGR2GRAY)
img_gray_smoothed = GaussianBlur(img_gray, (11, 11), 0)
imwrite("output/ps1-5-b-1.png", img_gray_smoothed)

edges_gray_smoothed = Canny(img_gray_smoothed, 40, 50) # seemingly only works on uint8
imwrite("output/ps1-5-b-2.png", edges_gray_smoothed)

peaks_and_params = find_circles(edges_gray_smoothed, (20, 50), img_gray_smoothed, 15)
img_circles = cvtColor(normalize(img_gray, None, 0, 255, NORM_MINMAX).astype(uint8), COLOR_GRAY2BGR) # to draw blue circles
for peak_and_params in peaks_and_params:
	row, col, radius = peak_and_params[1]
	circle(img_circles, (col, row), radius, (0, 255, 0), 1)
imwrite("output/ps1-5-b-3.png", img_circles)



### 6 ###

# a.
img_gray = cvtColor(imread("input/ps1-input2.png"), COLOR_BGR2GRAY)
img_gray_smoothed = GaussianBlur(img_gray, (11, 11), 0)

edges_gray_smoothed = Canny(img_gray_smoothed, 40, 50) # seemingly only works on uint8

hough_acc = hough_lines_acc(edges_gray_smoothed.astype(float)/255)
peaks_and_locs = hough_peaks_and_locs(hough_acc, 20) # seemingly 2 lines for each desired line, 180 deg apart, 1 is off screen

img_lines = hough_lines_draw(img_gray, [peak_and_loc[1] for peak_and_loc in peaks_and_locs])
imwrite("output/ps1-6-a-1.png", img_lines)

# b.
# also finding other seemingly weaker lines

# c.



### 7 ###

# a.
img_gray = cvtColor(imread("input/ps1-input2.png"), COLOR_BGR2GRAY)
img_gray_smoothed = GaussianBlur(img_gray, (11, 11), 0)

edges_gray_smoothed = Canny(img_gray_smoothed, 40, 50) # seemingly only works on uint8

peaks_and_params = find_circles(edges_gray_smoothed, (20, 50), img_gray_smoothed, 15)
img_circles = cvtColor(normalize(img_gray, None, 0, 255, NORM_MINMAX).astype(uint8), COLOR_GRAY2BGR) # to draw blue circles
for peak_and_params in peaks_and_params:
	row, col, radius = peak_and_params[1]
	circle(img_circles, (col, row), radius, (0, 255, 0), 1)
imwrite("output/ps1-7-a-1.png", img_circles)

# b.

# c.
'''


### 8 ###

# a.
img_gray = cvtColor(imread("input/ps1-input3.png"), COLOR_BGR2GRAY)
img_gray_smoothed = GaussianBlur(img_gray, (11, 11), 0)

edges_gray_smoothed = Canny(img_gray_smoothed, 40, 50) # seemingly only works on uint8

peaks_and_params = find_circles(edges_gray_smoothed, (20, 50), img_gray_smoothed, 15)
img_shapes = cvtColor(normalize(img_gray, None, 0, 255, NORM_MINMAX).astype(uint8), COLOR_GRAY2BGR) # to draw blue circles
for peak_and_params in peaks_and_params:
	row, col, radius = peak_and_params[1]
	circle(img_shapes, (col, row), radius, (0, 255, 0), 1)

hough_acc = hough_lines_acc(edges_gray_smoothed.astype(float)/255)
peaks_and_locs = hough_peaks_and_locs(hough_acc, 20) # seemingly 2 lines for each desired line, 180 deg apart, 1 is off screen

img_shapes = hough_lines_draw(img_shapes, [peak_and_loc[1] for peak_and_loc in peaks_and_locs])
imwrite("output/ps1-8-a-1.png", img_shapes)

waitKey(0)
destroyAllWindows()