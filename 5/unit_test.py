import unittest
import pytest
import logging
from problem import part_a, part_b

class Tests(unittest.TestCase):
    test_data = '''seeds: 79 14 55 13
        
seed-to-soil map:
50 98 2
52 50 48
soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15
fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4
water-to-light map:
88 18 7
18 25 70
light-to-temperature map:
45 77 23
81 45 19
68 64 13
temperature-to-humidity map:
0 69 1
1 0 69
humidity-to-location map:
60 56 37
56 93 4'''.splitlines()
    
    @pytest.mark.timeout(10)
    def test_part_a(self):
        expected_result = 35
        result = part_a(self.test_data)
        logging.debug('expected result: {}'.format(expected_result))
        logging.debug('actual result: {}'.format(result))
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b(self):
        expected_result = 46
        result = part_b(self.test_data)
        logging.debug('expected result: {}'.format(expected_result))
        logging.debug('actual result: {}'.format(result))
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s %(funcName)s %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()