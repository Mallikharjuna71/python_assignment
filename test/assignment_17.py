import unittest

from python_assignment.src.assignment_17.util import arrange_blocks
class Test(unittest.TestCase):
    def test_arrange_blocks(self):
        self.assertEqual(arrange_blocks([1, 2,3 ,8, 7]), 'No')
