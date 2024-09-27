
import unittest

from python_assignment.src.assignment_2.util import runner_up_score

class MyTestCase(unittest.TestCase):

    def test_something(self):
        scores = [6, 8, 9, 4, 2, 10]
        self.assertEqual(runner_up_score(scores), 9)  # add assertion here

if __name__ == '__main__':
    unittest.main()
