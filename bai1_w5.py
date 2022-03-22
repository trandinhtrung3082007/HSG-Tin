import math
import numpy as np

def find_nearest1(array,value):
    idx,val = min(enumerate(array), key=lambda x: abs(x[1]-value))
    return idx

def find_nearest2(array, values):
    indices = np.abs(np.subtract.outer(array, values)).argmin(0)
    return indices

def find_nearest3(array, values):
    values = np.atleast_1d(values)
    indices = np.abs(np.int64(np.subtract.outer(array, values))).argmin(0)
    out = array[indices]
    return indices

def find_nearest4(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx


def find_nearest5(array, value):
    idx_sorted = np.argsort(array)
    sorted_array = np.array(array[idx_sorted])
    idx = np.searchsorted(sorted_array, value, side="left")
    if idx >= len(array):
        idx_nearest = idx_sorted[len(array)-1]
    elif idx == 0:
        idx_nearest = idx_sorted[0]
    else:
        if abs(value - sorted_array[idx-1]) < abs(value - sorted_array[idx]):
            idx_nearest = idx_sorted[idx-1]
        else:
            idx_nearest = idx_sorted[idx]
    return idx_nearest

def find_nearest6(array,value):
    xi = np.argmin(np.abs(np.ceil(array[None].T - value)),axis=0)
    return xi