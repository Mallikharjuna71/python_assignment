import unittest

from python_assignment.src.assignment_19.util import result
class Test(unittest.TestCase):
    def test_email(self):
        email_list = ['arjun37ca@gmail.com', 'abc@qwe', 'asdfghjoiuytrew']
        self.assertEqual(*result , 'arjun37ca@gmail.com')
