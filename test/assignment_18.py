import unittest
from python_assignment.src.assignment_18.util import iterator
class Test(unittest.TestCase):
    def test_email(self):
        self.assertEqual(iterator(['a', 'a', 'c', 'd'], 2), 0.833)
