import unittest

from python_assignment.src.assignment_16.util import word_order
class Test(unittest.TestCase):
    def test_email(self):
        result = [('bcdef', 2), ('bcde', 1), ('abcdefg', 1)]
        self.assertEqual(word_order(['bcdef','abcdefg','bcde','bcdef']), result)
