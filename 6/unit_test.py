import unittest
import pytest
import logging
from problem import part_a, part_b

class Tests(unittest.TestCase):
    test_data = ''

    @pytest.mark.timeout(10)
    def test_part_a(self):
        expected_result = 'val'
        result = part_a(self.test_data)
        logging.debug('expected result: {}'.format(expected_result))
        logging.debug('actual result: {}'.format(result))
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b(self):
        expected_result = 'val'
        result = part_b(self.test_data)
        logging.debug('expected result: {}'.format(expected_result))
        logging.debug('actual result: {}'.format(result))
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s %(funcName)s %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()