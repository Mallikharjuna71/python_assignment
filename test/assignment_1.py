import unittest
from python_assignment.src.assignment_1.util import calculating_percentage

class UnitTest(unittest.TestCase):
    def test_calculating_percentage(self):
        self.assertEqual(calculating_percentage(), 77.00 )


if __name__ == 'main':
    unittest.main()