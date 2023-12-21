import unittest
import pytest
import logging
from my_utils import *
from problem import part_a, part_b

class Tests(unittest.TestCase):
    test_data_1 = parse_multi_line_input('''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a''')
    
    test_data_2 = parse_multi_line_input('''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output''')

    @pytest.mark.timeout(10)
    def test_part_a_1(self):
        expected_result = 32000000
        result = part_a(self.test_data_1)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_a_2(self):
        expected_result = 11687500
        result = part_a(self.test_data_2)
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