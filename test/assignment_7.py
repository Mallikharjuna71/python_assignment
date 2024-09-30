import unittest

from python_assignment.src.assignment_7.util import date_name
class Test(unittest.TestCase):
    def test_mutate(self):
        self.assertEqual(date_name('08 05 2015'), 'Wednesday')
