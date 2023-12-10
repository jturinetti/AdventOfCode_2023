import unittest
import pytest
import logging
from problem import part_a, part_b

class Tests(unittest.TestCase):
    @pytest.mark.timeout(10)
    def test_part_a_simple(self):
        test_data = list(filter(str.strip, '''
.....
.S-7.
.|.|.
.L-J.
.....'''.splitlines()))
        expected_result = 4
        result = part_a(test_data)
        self.assertEqual(result, expected_result)
    
    @pytest.mark.timeout(10)
    
    def test_part_a_complex(self):
        test_data = list(filter(str.strip, '''
..F7.
.FJ|.
SJ.L7
|F--J
LJ...'''.splitlines()))
        expected_result = 8
        result = part_a(test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b_simple(self):
        test_data = list(filter(str.strip, '''
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........'''.splitlines()))
        expected_result = 4
        result = part_b(test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b_complex_1(self):
        test_data = list(filter(str.strip, '''
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...'''.splitlines()))
        expected_result = 8
        result = part_b(test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b_complex_2(self):
        test_data = list(filter(str.strip, '''
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...'''.splitlines()))
        expected_result = 10
        result = part_b(test_data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()