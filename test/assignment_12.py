import unittest
from python_assignment.src.assignment_12.util import lin_alg
class Test(unittest.TestCase):
    def test_mutate(self):
        arr = [[1.1, 1.1], [1.1, 1.1]]
        self.assertEqual(lin_alg(arr),0.0)
