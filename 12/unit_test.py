import unittest
import pytest
import logging
from my_utils import *
from problem import part_a, part_b

class Tests(unittest.TestCase):

    @pytest.mark.timeout(10)
    def test_part_a_1(self):
        expected_result = 1
        result = part_a(['???.### 1,1,3'])
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_a_2(self):
        expected_result = 4
        result = part_a(['.??..??...?##. 1,1,3'])
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_a_3(self):
        expected_result = 1
        result = part_a(['?#?#?#?#?#?#?#? 1,3,1,6'])
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_a_4(self):
        expected_result = 1
        result = part_a(['????.#...#... 4,1,1'])
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_a_5(self):
        expected_result = 4
        result = part_a(['????.######..#####. 1,6,5'])
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_a_6(self):
        expected_result = 10
        result = part_a(['?###???????? 3,2,1'])
        self.assertEqual(result, expected_result)

    # @pytest.mark.timeout(10)
    # def test_part_b(self):
    #     expected_result = -1
    #     result = part_b(self.test_data)
    #     self.assertEqual(result, expected_result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()