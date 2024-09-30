import unittest
from python_assignment.src.assignment_3.util import mutate_string

class Test(unittest.TestCase):
    def test_mutate(self):
        self.assertEqual(mutate_string(), 'arjun')
