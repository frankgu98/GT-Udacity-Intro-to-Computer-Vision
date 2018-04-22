import numpy as np
import timeit

'''
# attempts at memoization, scales pretty well though
# 2s per row for a 3x3 template, 2.5s per row for a 13x13 template

def template_disparities(template_strip, img_strip, ssd_array, search_width=30):
    template_strip_height, template_strip_width = template_strip.shape
    img_strip_height, img_strip_width = img_strip.shape

    template_height, template_width = (template_strip_height, template_strip_height)
    template_half_width = int(template_width/2)
    template_half_height = int(template_height/2)
    

    best_img_strip_cols = np.zeros(img_strip_width) # for each possible top left col
    for template_strip_col in range(template_strip_width - template_width + 1):
        
        min_ssd = 999999999
        for img_strip_col in range(img_strip_width - template_width + 1):
            # IF GAP IS OVER SEARCH WIDTH
            
            ssd = 0
            for sub_col in range(template_width):
                ssd += ssd_array[template_strip_col + sub_col, img_strip_col + sub_col]
                # if array is -1 that's bad
            if ssd < min_ssd:
                min_ssd = ssd
                best_img_strip_cols[template_strip_col] = img_strip_col
    
    for i in range(template_strip_width - template_width + 1):
        best_img_strip_cols[i] -= i # computes disparities from just column matches
        
    best_img_strip_cols = np.roll(best_img_strip_cols, template_half_width) # all 0 pads are at right but that with comparing top left corners, actual outputs wants comparison of centers so roll over 0s
    return best_img_strip_cols # actually disparities now but not making another array 


# template = np.array([[2, 3, 4], [6, 7, 8], [2, 3, 4]])
# img_strip = np.array([[0, 1, 2, 3, 4], [4, 5, 6, 7, 8], [0, 1, 2, 3, 4]])
# print(template_disparities(template, img_strip, 1))


def disparity_ssd(L, R, search_width=30):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))
    
    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """

    # TODO: Your code here

    template_height, template_width = (3, 3)
    template_half_height = int(template_height/2)
    template_half_width = int(template_width/2)
    img_height, img_width = L.shape
    disparity_map = np.zeros(L.shape)
    ssd_array = -1*np.ones((img_width, img_width))
    half_search_width = int(search_width/2)
    for row in range(template_half_height, img_height - template_half_height):
        start = timeit.default_timer()

        L_strip = L[row - template_half_height: row + template_half_height + 1, :]
        R_strip = R[row - template_half_height: row + template_half_height + 1, :]
        for i in range(img_width): # every template strip col
            for j in range(img_width): # every img strip col
                if np.absolute(i-j) < half_search_width:
                    if ssd_array[i, j] == -1:
                        L_strip_col = L_strip[:, i]
                        R_strip_col = R_strip[:, j]
                        ssd_array[i, j] = np.sum(np.square(R_strip_col - L_strip_col))
                    else:
                        L_strip_old_val = L[row - template_half_height - 1, i]
                        R_strip_old_val = R[row - template_half_height - 1, j]
                        L_strip_new_val = L[row + template_half_height, i]
                        R_strip_new_val = R[row + template_half_height, j]
                        ssd_array[i, j] -= np.square(R_strip_old_val - L_strip_old_val)
                        ssd_array[i, j] += np.square(R_strip_new_val - L_strip_new_val)
        print(ssd_array)
                
        disparity_map[row] = template_disparities(L_strip, R_strip, ssd_array)
        #print(disparity_map[row])
        print(timeit.default_timer() - start)
    return disparity_map


template_strip = np.array([[1, 2, 3], 
                           [5, 6, 7],
                           [1, 2, 3],
                           [2, 4, 6]])
img_strip = np.roll(template_strip, 0)
print(template_strip)
print(img_strip)
print(disparity_ssd(template_strip, img_strip))
'''

# GUARANTEED GOOD

def template_disparity(template, img_strip, template_img_col, search_width = 30):
    img_strip_height, img_strip_width = img_strip.shape
    template_height, template_width = template.shape
    half_template_width = int(template_width/2)
    half_search_width = int(search_width/2)
    best_img_strip_col = 0
    min_ssd = 99999999
    for col in range(half_template_width, img_strip_width - half_template_width):
        if np.absolute(template_img_col - col) > half_search_width:
            continue
        img_cutout = img_strip[:, col - half_template_width: col + half_template_width + 1]
        ssd = np.sum(np.square(template - img_cutout))
        if ssd < min_ssd:
            min_ssd = ssd
            best_img_strip_col = col
    return template_img_col - best_img_strip_col # TODO: RERUN WITH DIFFERENT SUBSTRACTION ORDER

def disparity_ssd(L, R, template_shape = (11, 11), search_width=30):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))
    
    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """

    # TODO: Your code here
    template_height, template_width = template_shape
    template_half_height = int(template_height/2)
    template_half_width = int(template_width/2)
    img_height, img_width = L.shape
    disparity_map = np.zeros(L.shape)

    for row in range(template_half_height, img_height - template_half_height):
        start = timeit.default_timer()
        
        R_strip = R[row - template_half_height: row + template_half_height + 1, :]

        for col in range(template_half_width, img_width - template_half_width):
            L_template = L[row - template_half_height: row + template_half_height + 1, col - template_half_width: col + template_half_width + 1]
            disparity_map[row, col] = template_disparity(L_template, R_strip, col, search_width)
       
        #print(disparity_map[row])
        print(timeit.default_timer() - start)
    return disparity_map

