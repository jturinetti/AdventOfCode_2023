import unittest
import pytest
import logging
from problem import part_a, part_b, parse_multiple_races, parse_single_race

class Tests(unittest.TestCase):
    test_data = '''Time:      7  15   30    
Distance:  9  40  200'''.splitlines()

    @pytest.mark.timeout(10)
    def test_part_a(self):
        expected_result = 288
        result = part_a(self.test_data)
        logging.debug('expected result: {}'.format(expected_result))
        logging.debug('actual result: {}'.format(result))
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b(self):
        expected_result = 71503
        result = part_b(self.test_data)
        logging.debug('expected result: {}'.format(expected_result))
        logging.debug('actual result: {}'.format(result))
        self.assertEqual(result, expected_result)

    def test_parse_multiple_races(self):
        result = parse_multiple_races(self.test_data)
        self.assertEqual(len(result), 3)
        self.assertTupleEqual(result[0], (7, 9))
        self.assertTupleEqual(result[1], (15, 40))
        self.assertTupleEqual(result[2], (30, 200))

    def test_parse_single_race(self):
        result = parse_single_race(self.test_data)
        self.assertEqual(len(result), 1)
        self.assertTupleEqual(result[0], (71530, 940200))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()