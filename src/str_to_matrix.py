import numpy as np

def str_to__matrix(s):
    return np.array(np.mat(s), dtype = float, order = "C")
