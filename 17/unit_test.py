import unittest
import pytest
import logging
from my_utils import *
from problem import part_a, part_b

class Tests(unittest.TestCase):
    test_data = parse_multi_line_input('')  # ADD THIS FROM PROBLEM STATEMENT

    @pytest.mark.timeout(10)
    def test_part_a(self):
        expected_result = 'val'     # REPLACE WITH CORRECT SAMPLE VALUE (PART A)
        result = part_a(self.test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b(self):
        expected_result = 'val'     # REPLACE WITH CORRECT SAMPLE VALUE (PART B)
        result = part_b(self.test_data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()