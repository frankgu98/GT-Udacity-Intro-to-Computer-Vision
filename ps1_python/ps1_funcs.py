from cv2 import * # BGR FORMAT
from numpy import *
from numpy import cos as npcos, sin as npsin
from matplotlib import pyplot as plt
from timeit import default_timer



# edges doesn't actually be any particular type
# OPTIONAL PARAMS NOT TESTED
def hough_lines_acc(edges, **kwargs): # theta range 0 to 360 to keep everything positive and all indices nice and clear
	if "rho_resolution" in kwargs:
		rho_resolution = kwargs["rho_resolution"]
	else:
		rho_resolution=1
	if "theta_range" in kwargs:
		theta_range = kwargs["theta_range"]
	else:	
		theta_range=(0, 360) # prev used 0:180 but some lines sitll have angles past 180 even in 1 quadrant (ie. pen 2)
	height, width = edges.shape
	n_rhos = int(sqrt(height*height + width*width)/rho_resolution) + 1 # max dist is diagonal
	n_thetas = theta_range[1] - theta_range[0]
	hough_acc = zeros((n_rhos, n_thetas)) # hough accumulator array
	cos_vals = [cos(radians(theta)) for theta in range(theta_range[0], theta_range[1])] # INITIALLY FORGOT TO TURN TUPLE INTO RANGE (WHEN THIS WAS ANOTHER FOR LOOP) -> MOSTLY BLACK IMAGE			
	sin_vals = [sin(radians(theta)) for theta in range(theta_range[0], theta_range[1])] # without precomputed: 20.80417045400003 s, with precomputed: 3.5845322150000243 s
	for r in range(height):
		for c in range(width):
			if edges[r, c] != 0: # allows for edges pics from 0 to 1 or 0 to 255
				for theta in range(theta_range[0], theta_range[1]): # theta as first loop: 34.89897802199994 s, theta as last loop: 3.5845322150000243 s
					rho = int(c*cos_vals[theta] + r*sin_vals[theta])
					hough_acc[rho, theta] += 1
	return hough_acc
# DEBUGGING
# start = default_timer()
# hough_acc = normalize(hough_lines_acc(edges), None, 0, 255, NORM_MINMAX).astype(uint8)
# print(default_timer() - start)

# imshow("hough_acc", hough_acc)
# imshow("edges", edges)
# imshow("img", img)



# need not be normalized but user needs to make sure that if they give a threshold it accounts for hough_acc's max and min
def hough_peaks_and_locs(hough_acc, num_peaks=1, **kwargs):
	if "threshold" in kwargs:
		threshold = kwargs["threshold"]

	else:
		threshold = 0.5*amax(hough_acc)
	if "neighbourhood_size" in kwargs:
		neighbourhood_size = kwargs["neighbourhood_size"]
		neighbourhood_height = neighbourhood_size[0]
		neighbourhood_width = neighbourhood_size[1]
	else:
		neighbourhood_height = int(float(hough_acc.shape[0])/50 + 0.5) # round up
		neighbourhood_height = neighbourhood_height if neighbourhood_height%2==1 else neighbourhood_height+1 # next odd greater than or equal to 1/50th of image height
		neighbourhood_width = int(float(hough_acc.shape[1])/50 + 0.5)
		neighbourhood_width = neighbourhood_width if neighbourhood_width%2==1 else neighbourhood_width+1
		neighbourhood_size = (neighbourhood_height, neighbourhood_width)
	
	threshold = (float(threshold) - amin(hough_acc))/(amax(hough_acc) - amin(hough_acc)) # normalizes threshold to 0:1
	hough_acc = normalize(hough_acc, None, 0, 1, NORM_MINMAX) # normalizes array to 0:1
	height, width = hough_acc.shape

	sobel_x = Sobel(hough_acc, -1, 1, 0, ksize = 5) # careful between numpy functions and math/regular python functions
	sobel_y = Sobel(hough_acc, -1, 0, 1, ksize = 5) # vertical lines were found better with ksize smaller, bigger kernel probably shifted rho
	sobel_mag = sqrt(square(sobel_x) + square(sobel_y))

	# supressing in neighbourhood
	max_sub_row = int(neighbourhood_height/2)  # max_x -> max value of x, x_max -> max in x OR x's max
	max_sub_col = int(neighbourhood_width/2)
	for row in range(max_sub_row, height - max_sub_row, max_sub_row):
		for col in range(0, width, max_sub_col): # want to wrap or angles (cols) but not distances since 0 deg is "next to" 359 deg but 0 pixels isn't "next to" 359 pixels
			# make into function
			try:
				local_max = amax(hough_acc[row - max_sub_row : row + max_sub_row + 1, (col - max_sub_col) : col + max_sub_col + 1])
			except ValueError: # (col - max_sub_col) is negative
				local_max = amax(hough_acc[row - max_sub_row : row + max_sub_row + 1, (col - max_sub_col)%width :])
				local_max = maximum(local_max, amax(hough_acc[row - max_sub_row : row + max_sub_row + 1, : (col + max_sub_col + 1)%width]))
			found_first_subarray_max = False
			for sub_row in range(-max_sub_row, max_sub_row + 1):
				for sub_col in range(-max_sub_col, max_sub_col + 1):
					if hough_acc[row + sub_row, (col + sub_col)%width] < local_max: # want to surpress at all but 1 of same size but don't want to surpress itself
						hough_acc[row + sub_row, (col + sub_col)%width] = 0
					elif hough_acc[row + sub_row, (col + sub_col)%width] == local_max:
						if found_first_subarray_max:
							hough_acc[row + sub_row, (col + sub_col)%width] = 0
						else:
							found_first_subarray_max = True

	crit_points = where((sobel_mag < 0.65*amax(sobel_mag))) # ideally would be 0 but images are noisy
	peaks = []
	for i in range(crit_points[0].size):
		crit_point = crit_points[0][i], crit_points[1][i]	
		if hough_acc[crit_point] > threshold:
			peaks.append((hough_acc[crit_point], crit_point)) # allows sorting by intensity
	peaks.sort()
	return peaks[-num_peaks:] # biggest few



def hough_lines_draw(img_gray, peak_locs):
	try:
		n_rows, n_cols = img_gray.shape
		img_bgr = cvtColor(img_gray, COLOR_GRAY2BGR)
	except ValueError:
		n_rows, n_cols = img_gray.shape[:2]
		img_bgr = img_gray
	top_horizontal =    array([0, 1, 0])
	left_vertical   =   array([1, 0, 0])
	bottom_horizontal = array([0, 1, -n_rows])
	right_vertical =    array([1, 0, -n_cols])
	
	for rho, theta in peak_locs:
		#convert line from ϱ=xcosθ+ysinθ to y=mx+b
		if theta == 0 or theta == 180: # vertical lines, theta measured from x axis to perp to line
			(x1, y1) = (rho, 0)
			(x2, y2) = (rho, n_rows)
		else:
			m = -1/tan(radians(theta))
			b = rho/sin(radians(theta))
			(x1, y1) = (0, b)
			# only need to compute intersection with opposite edge of image since even if line hites horizontal edge first, it will be cut off when drawing (intersect with opposite edge to ensure line goes across image)
			(x2, y2) = (n_cols, m*n_cols + b)
		line(img_bgr, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 1)
	return img_bgr



def hough_circles_acc(edges, radius, sobel_angles = None): # theta range 0 to 360 to keep everything positive and all indices nice and clear
	height, width = edges.shape
	hough_acc = zeros((height, width)) # hough accumulator array
	cos_vals = [cos(radians(theta)) for theta in range(0, 360)]	
	sin_vals = [sin(radians(theta)) for theta in range(0, 360)]
	if sobel_angles is None:
		sobel_x = Sobel(img, -1, 1, 0, ksize = 3)
		sobel_y = Sobel(img, -1, 0, 1, ksize = 3)
		sobel_angles = degrees(arctan2(sobel_y, sobel_x) + pi).astype(int)
	for r in range(height):
		for c in range(width):
			if edges[r, c] != 0: # allows for edges pics from 0:1 or 0:255
				mid_angle = sobel_angles[r, c]
				for angle in range(mid_angle-35, mid_angle+36):
					dr, dc = (int(radius * sin_vals[angle]), int(radius * cos_vals[angle]))
					if 0 <= r + dr < height and 0 <= c + dc < width:
						hough_acc[r + dr, c + dc] += 1
					if 0 <= r - dr < height and 0 <= c - dc < width:	
						hough_acc[r - dr, c - dc] += 1
	return hough_acc



# need not be normalized but user needs to make sure that if they give a threshold it accounts for hough_acc's max and min
def hough_peaks_and_params_3d(hough_acc, num_peaks=1, **kwargs):
	if "threshold" in kwargs:
		threshold = kwargs["threshold"]
	else:
		threshold = 0.5*amax(hough_acc)
	
	threshold = (float(threshold) - amin(hough_acc))/(amax(hough_acc) - amin(hough_acc)) # normalizes threshold to 0:1
	hough_acc = normalize(hough_acc, None, 0, 1, NORM_MINMAX) # normalizes array to 0:1

	sobel_x = Sobel(hough_acc, -1, 1, 0, ksize = 5)
	sobel_y = Sobel(hough_acc, -1, 0, 1, ksize = 5)
	sobel_r = Sobel(hough_acc, -1, 0, 1, ksize = 5)
	sobel_mag = sqrt(square(sobel_x) + square(sobel_y) + square(sobel_r))
	crit_points = where((sobel_mag < 0.65*amax(sobel_mag))) # ideally would be 0 but images are noisy
	peaks = []

	height, width, depth = hough_acc.shape
	# surpressing in neighbourhood
	for row in range(5, height - 5, 5):
		for col in range(5, width - 5, 5):
			for radius in range(2, depth-2):
				local_max = amax(hough_acc[row-3:row+4, col-3:col+4, radius-1:radius+2])
				found_first_max = False
				for sub_row in range(-3, 4):
					for sub_col in range(-3, 4):
						for sub_radius in range(-2, 3):
							if hough_acc[row+sub_row, col+sub_col, radius+sub_radius] < local_max: # want to surpress at all but 1 of same size but don't want to surpress itself
								hough_acc[row+sub_row, col+sub_col, radius+sub_radius] = 0
							elif hough_acc[row+sub_row, col+sub_col, radius+sub_radius] == local_max:
								if found_first_max:
									hough_acc[row+sub_row, col+sub_col, radius+sub_radius] = 0
								else:
									found_first_max = True
		
	for i in range(crit_points[0].size):
		crit_point = crit_points[0][i], crit_points[1][i], crit_points[2][i]
		if hough_acc[crit_point] > threshold:
			peaks.append((hough_acc[crit_point], crit_point)) # allows sorting by intensity
	peaks.sort()
	return peaks[-num_peaks:] # biggest few



def find_circles(edges, radius_range, img, num_circles):
	min_radius, max_radius = radius_range
	sobel_x = Sobel(img, -1, 1, 0, ksize = 3)
	sobel_y = Sobel(img, -1, 0, 1, ksize = 3)
	sobel_angles = degrees(arctan2(sobel_y, sobel_x) + pi).astype(int)
	size1, size2 = edges.shape
	size3 = max_radius - min_radius # will need to readd
	hough_acc_3d = zeros((size1, size2, size3))
	for radius in range(min_radius, max_radius):
		hough_acc_3d[:, :, radius-min_radius] += hough_circles_acc(edges, radius, sobel_angles)

	peaks_and_params = hough_peaks_and_params_3d(hough_acc_3d, num_circles)
	peaks_and_params = [(peak_and_params[0], peak_and_params[1] + array([0, 0, min_radius])) for peak_and_params in peaks_and_params]
	return peaks_and_params
	#find params with many votes