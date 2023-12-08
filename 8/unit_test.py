import unittest
import pytest
import logging
from problem import part_a, part_b

class Tests(unittest.TestCase):
    part_a_test_data = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''.splitlines()
    
    part_a_2_test_data = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''.splitlines()

    part_b_test_data = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''.splitlines()

    @pytest.mark.timeout(10)
    def test_part_a(self):
        expected_result = 2
        result = part_a(self.part_a_test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_a(self):
        expected_result = 6
        result = part_a(self.part_a_2_test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b(self):
        expected_result = 6
        result = part_b(self.part_b_test_data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()