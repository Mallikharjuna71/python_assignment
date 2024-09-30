import unittest

from python_assignment.src.assignment_9.util import time_delta
class Test(unittest.TestCase):
    def test_mutate(self):
        self.assertEqual(time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000'),25200)
