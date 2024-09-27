import unittest
from python_assignment.src.assignment_11.util import max_of_min
class Test(unittest.TestCase):
    def test_mutate(self):
        self.assertEqual(max_of_min([[2, 5], [3, 7], [1, 3], [4, 0]]),3)
