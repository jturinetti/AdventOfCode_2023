import unittest
import pytest
import logging
from copy import deepcopy
from my_utils import *
from problem import part_a, part_b, perform_full_cycle

class Tests(unittest.TestCase):
    test_data = parse_multi_line_input('''
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....''')
    
    @pytest.mark.timeout(10)
    def test_part_a(self):
        expected_result = 136
        result = part_a(self.test_data)
        self.assertEqual(result, expected_result)

    @pytest.mark.timeout(10)
    def test_perform_1_full_cycle(self):
        expected_result = parse_multi_line_input('''
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....''')
        result_grid = [['.' for x in range(len(expected_result[0]))] for y in range(len(expected_result))]
        result_grid = perform_full_cycle(self.test_data, result_grid)
        result_grid = flatten_grid_rows(result_grid)
        self.assertEqual(result_grid, expected_result)

    @pytest.mark.timeout(10)
    def test_perform_2_full_cycles(self):
        expected_result = parse_multi_line_input('''
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O''')
        dimensions = (len(expected_result), len(expected_result[0]))
        input_grid = self.test_data
        result_grid = []
        for i in range(0, 2):  
            result_grid = generate_empty_grid(dimensions[0], dimensions[1], '.') 
            result_grid = perform_full_cycle(input_grid, result_grid)
            input_grid = deepcopy(result_grid)            
        
        result_grid = flatten_grid_rows(result_grid)
        self.assertEqual(result_grid, expected_result)

    @pytest.mark.timeout(10)
    def test_perform_3_full_cycles(self):
        expected_result = parse_multi_line_input('''
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O''')
        dimensions = (len(expected_result), len(expected_result[0]))
        input_grid = self.test_data
        result_grid = []
        for i in range(0, 3):
            result_grid = generate_empty_grid(dimensions[0], dimensions[1], '.') 
            result_grid = perform_full_cycle(input_grid, result_grid)
            input_grid = deepcopy(result_grid)            
        
        result_grid = flatten_grid_rows(result_grid)
        self.assertEqual(result_grid, expected_result)

    @pytest.mark.timeout(10)
    def test_part_b(self):
        expected_result = 64
        result = part_b(self.test_data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    unittest.main()