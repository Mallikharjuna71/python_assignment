import unittest
from python_assignment.src.assignment_5.util import str_format
class Test(unittest.TestCase):
    def test_mutate(self):
        self.assertEqual(str_format(2), ['1 1 1 1', '2 2 2 10'])
