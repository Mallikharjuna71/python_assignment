import numpy

def lin_alg(arr):
    return round(numpy.linalg.det(numpy.array(arr)), 2)
