import unittest
import pytest
import logging
from problem import part_a, part_b

class Tests(unittest.TestCase):
    test_data = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.splitlines()

    @pytest.mark.timeout(10)
    def test_part_a(self):
        expected_result = 114
        result = part_a(self.test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b(self):
        expected_result = 2
        result = part_b(self.test_data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()