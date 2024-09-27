import unittest
from python_assignment.src.assignment_15.util import no_idea
class Test(unittest.TestCase):
    def test_email(self):
        self.assertEqual(no_idea([1, 5, 3], {3, 1}, {5, 7}), 1)
