import numpy as np

def str_to_matrix(s):
    return np.array(np.mat(s), dtype = float, order = "C")
