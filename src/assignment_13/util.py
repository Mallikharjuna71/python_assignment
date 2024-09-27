import numpy
def mean_varianc_std(n):
    array = numpy.array(n)
    return numpy.mean(array, axis=1), numpy.var(array, axis=0),numpy.std(array, axis=None)