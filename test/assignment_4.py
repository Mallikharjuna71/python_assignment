import unittest
from python_assignment.src.assignment_4.util import merge_the_tools
class Test(unittest.TestCase):
    def test_mutate(self):
        self.assertEqual(merge_the_tools('AABCAAADA', 3), ['AB', 'CA', 'AD'])
