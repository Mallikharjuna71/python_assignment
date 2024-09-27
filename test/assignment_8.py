import unittest
from python_assignment.src.assignment_8.util import named_tuples_avg
class Test(unittest.TestCase):
    def test_mutate(self):
        list_of_students = [[92, 2, 'calum', 1], [82, 5, 'scott', 2], [94, 2, 'jason', 3], [55, 8, 'glenn', 4],
                            [82, 2, 'fergus', 5]]

        self.assertEqual(named_tuples_avg(list_of_students),81.0)
