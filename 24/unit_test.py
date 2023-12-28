import unittest
import pytest
import logging
from my_utils import *
from problem import part_a, part_b

class Tests(unittest.TestCase):
    test_data = parse_multi_line_input('''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3''')

    @pytest.mark.timeout(10)
    def test_part_a(self):
        expected_result = 2
        result = part_a(self.test_data, 7, 27)
        self.assertEqual(result, expected_result)

    # @pytest.mark.timeout(10)
    # def test_part_b(self):
    #     expected_result = 'val'     # REPLACE WITH CORRECT SAMPLE VALUE (PART B)
    #     result = part_b(self.test_data)
    #     self.assertEqual(result, expected_result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()