import unittest
import pytest
import logging
from my_utils import *
from problem import part_a, part_b

class Tests(unittest.TestCase):
    test_data = parse_multi_line_input('''
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....''')

    @pytest.mark.timeout(10)
    def test_part_a(self):
        expected_result = 374
        result = part_a(self.test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b_1(self):
        expected_result = 1030
        result = part_b(self.test_data, 10)
        self.assertEqual(result, expected_result)
    
    @pytest.mark.timeout(10)
    def test_part_b_2(self):
        expected_result = 8410
        result = part_b(self.test_data, 100)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()