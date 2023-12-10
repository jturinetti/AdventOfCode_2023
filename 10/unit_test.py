import unittest
import pytest
import logging
from my_utils import *
from problem import part_a, part_b

class Tests(unittest.TestCase):
    @pytest.mark.timeout(10)
    def test_part_a_simple(self):
        test_data = parse_multi_line_input('''
.....
.S-7.
.|.|.
.L-J.
.....''')
        expected_result = 4
        result = part_a(test_data)
        self.assertEqual(result, expected_result)
    
    @pytest.mark.timeout(10)
    
    def test_part_a_complex(self):
        test_data = parse_multi_line_input('''
..F7.
.FJ|.
SJ.L7
|F--J
LJ...''')
        expected_result = 8
        result = part_a(test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b_simple(self):
        test_data = parse_multi_line_input('''
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........''')
        expected_result = 4
        result = part_b(test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b_complex_1(self):
        test_data = parse_multi_line_input('''
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...''')
        expected_result = 8
        result = part_b(test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b_complex_2(self):
        test_data = parse_multi_line_input('''
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L''')
        expected_result = 10
        result = part_b(test_data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()