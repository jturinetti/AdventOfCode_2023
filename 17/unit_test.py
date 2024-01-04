import unittest
import pytest
import logging
from my_utils import *
from problem import part_a, part_b

class Tests(unittest.TestCase):
    test_data = parse_multi_line_input('''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533''')

    @pytest.mark.timeout(10)
    def test_part_a(self):
        expected_result = 102
        result = part_a(self.test_data)
        self.assertEqual(result, expected_result)

    # @pytest.mark.timeout(10)
    # def test_part_b(self):
    #     expected_result = 'val'     # REPLACE WITH CORRECT SAMPLE VALUE (PART B)
    #     result = part_b(self.test_data)
    #     self.assertEqual(result, expected_result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()