import unittest
import numpy
from numpy import array
from python_assignment.src.assignment_10.util import floor_ceil_rint
class Test(unittest.TestCase):
    def test_mutate(self):
        result = str((array([1., 2., 3., 4., 5., 6., 7., 8., 9.]), array([ 2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]), array([ 1.,  2.,  3.,  4.,  6.,  7.,  8.,  9., 10.])))

        self.assertEqual(str(floor_ceil_rint([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])), result)

