import unittest
import numpy as np
from numpy import array
from python_assignment.src.assignment_13.util import mean_varianc_std
class Test(unittest.TestCase):
    def test_mutate(self):
        arr = [[2, 5], [3, 7], [1, 3], [4, 0]]
        result = str((array([3.5, 5. , 2. , 2. ]), array([1.25  , 6.6875]), np.float64(2.0879116360612584))
)
        self.assertEqual(str(mean_varianc_std(arr)),result)
