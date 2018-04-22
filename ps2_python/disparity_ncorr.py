import timeit
import numpy as np
import cv2


def disparity_ncorr(L, R, template_shape = (11, 11), search_width=30):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))

    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """

    L = L.astype(np.float32)
    R = R.astype(np.float32)
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
            #print(R_strip.shape, L_template.shape)
            comparisons = cv2.matchTemplate(R_strip, L_template, cv2.TM_CCOEFF_NORMED)
            disparity_map[row, col] = col - np.argmax(comparisons)
       
        #print(disparity_map[row])
        print(timeit.default_timer() - start)
    return np.clip(disparity_map, -search_width/2, search_width/2) # could also clip differently based on left vs right being base image

    