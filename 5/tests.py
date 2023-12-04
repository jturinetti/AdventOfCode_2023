import unittest
from problem import *

class Tests(unittest.TestCase):

    def test_part_a(self):
        expected_result = 'result'
        sample_data = 'data'
        result = part_a(sample_data)
        self.assertEqual(result, expected_result)

    def test_part_b(self):
        expected_result = 'result'
        sample_data = 'data'
        result = part_b(sample_data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()