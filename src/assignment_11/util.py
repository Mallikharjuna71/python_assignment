import numpy

def max_of_min(array):
    array = numpy.array(array)
    mn = numpy.min(array, axis=1)
    return numpy.max(mn)