from cv2 import * # BGR FORMAT
from cv2 import split as imsplit
from numpy import *

### 2 ###

# a.
def swap_r_b(img):
	b, g, r = imsplit(img)
	return merge((r, g, b))

img1 = imread("output/ps0-1-a-1.png")
img2 = imread("output/ps0-1-a-2.png")
swapped1 = swap_r_b(img1)
imwrite("output/ps0-2-a-1.png", swapped1)

# b.
img1_g = img1[:, :, 1]
imwrite("output/ps0-2-b-1.png", img1_g)

# c.
img1_r= img1[:, :, 2]
imwrite("output/ps0-2-c-1.png", img1_r)

# d.
# b more monochrome looking due to larger variations in amount of red in pic and green

'''
### 3 ###

# a.
width1, height1, channels1 = img1.shape
img1_g_centre = img1_g[int(width1/2 - 50) : int(width1/2 + 50), int(height1/2 - 50) : int(height1/2 + 50)]

img2_g = img2[:, :, 1]
width2, height2, channels2 = img2.shape
img2_g[int(width2/2 - 50) : int(width2/2 + 50), int(height2/2 - 50) : int(height2/2 + 50)] = img1_g_centre

imwrite("output/ps0-3-a-1.png", img2_g)


### 4 ###

# a.
print("min of img1_g: ", amin(img1_g))
print("max of img1_g: ", amax(img1_g))
mean = average(img1_g)
std_dev = std(img1_g)
print("mean of img1_g: ", mean)
print("standard deviation of img1_g: ", std_dev)
# computed using numpy

# b.
img1_g_new = (((img1_g - mean)/std_dev)*10 + mean).astype(uint8)
imwrite("ps0-4-b-1", img1_g_new)
'''
# c.
# images from 0 to 1 are way better
img1_g_ls = img1_g[2:, :].astype(float)/255 # not using normalize since that maps from min and max of image to range as opposed to min and max possible in image to range
imwrite("ps0-4-c-1.png", img1_g_ls)

# d.
img1_g = img1_g.astype(float)/255
img1_g_diff = img1_g[:-2, :] - img1_g_ls[:, :] # first 2 and last 2 columns had to be cut out in total (to left shift, and then to match dimensions

img1_g_diff = img1_g_diff

imwrite("ps0-4-d-1.png", img1_g_diff)
# negatives are just darker/more change in negative direction than middle (gray)



### 5 ###

# a.
# not centered around 0 since this is a difference in intensity, centered around .5 (centre of actual image) would increase average intensity in image
noise = random.normal(0, .04, img1_g.shape)
img1_g_noisy = clip(img1_g + noise, 0, 1)
imwrite("ps0-5-a-1", img1_g_noisy)

# b.
img1_b_noisy = clip(img1[:, :, 0].astype(float)/255 + noise, 0, 1)
imwrite("ps0-5-b-1", img1_b_noisy)

# c.
# green channel looks better with noise since more variation in colour intensity