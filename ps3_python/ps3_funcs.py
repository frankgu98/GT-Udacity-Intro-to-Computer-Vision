import os
import numpy as np
from numpy.linalg import eig
import cv2
import timeit
import matplotlib.pyplot as plt


def parse_points(file_name):
    """Parses points into a list. Works for 2D and 3D. Done this way mostly to see if I could"""
    lines = open(file_name, "r").read().strip().split("\n")
    return list(map(lambda l: tuple(map(float, l.split())), lines))

def get_homo_eq_matrix(points_3D, points_2D):
    """Uses lists of points to build matrix A which represents the homogeneous equations that come from the mapping of points in 3D space to 2D image plane"""
    # need at least 6 points (12 eqs) to solve for 11 camera params
    if len(points_3D) < 6 or len(points_2D) < 6 or len(points_3D) != len(points_2D):
        return -1
    A = np.empty((0, 12))
    for i in range(len(points_3D)):
        X, Y, Z = points_3D[i]
        u, v = points_2D[i]
        eq1 = np.array([X, Y, Z, 1, 0, 0, 0, 0, -u*X, -u*Y, -u*Z, -u])
        eq2 = np.array([0, 0, 0, 0, X, Y, Z, 1, -v*X, -v*Y, -v*Z, -v])
        A = np.vstack((A, eq1, eq2))
    return A

'''
world_points = parse_points("input/pts3d-norm.txt")
image_points = parse_points("input/pts2d-norm-pic_a.txt")
print(world_points)
print(image_points)
print(get_homo_eq_matrix(world_points, image_points))
'''

def get_camera_params(A):
    """Gets matrix entries by math trick: eigenvector of A.T*A with smallest eigenvalue is m"""
    # A is 
    ATA = np.matmul(A.T, A)
    eigenvalues, eigenvectors = eig(ATA)
    col = np.argmin(eigenvalues)  # diagonal so indices will be same
    return eigenvectors[:, col]

def get_camera_param_matrix_from_params(params):
    return np.reshape(params, (3, 4))

def get_camera_param_matrix(points_3D, points_2D):
    return get_camera_param_matrix_from_params(get_camera_params(get_homo_eq_matrix(points_3D, points_2D)))

def to_cartesian(point):
    return point[:-1] / point[-1]

def to_homogeneous(point):
    return np.append(point, 1)

'''
print(to_cartesian(np.array([[1], [1], [2]])))
'''

def get_residual(point1, point2):
    return np.sqrt(np.linalg.norm(np.array(point1) - np.array(point2)))

def get_best_camera_param_matrix(n_cal_points, indices): # assumes at least 20 points total
    min_avg_residual = 99999999
    best_M = None 
    for i in range(10):
        random.shuffle(indices) # can shuffle between tries
        calibration_indices = indices[:n_cal_points]
        M = get_camera_param_matrix([world_points[j] for j in calibration_indices], [image_points[j] for j in calibration_indices])
        avg_residual = 0 # could use average but only comparing
        for j in range(4):
            test_world_point = world_points[indices[-j]] # use last 4 indices
            test_image_point = image_points[indices[-j]]
            pred_image_point = to_cartesian(np.matmul(M, to_homogeneous(test_world_point)))
            avg_residual += get_residual(test_image_point, pred_image_point)
        print(avg_residual)
        if avg_residual < min_avg_residual:
            best_M = M
            min_avg_residual = avg_residual
    return best_M
