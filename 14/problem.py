import time
import logging
from utils import *
from my_utils import read_aoc_data

def move_rocks(result_grid, num_rocks, stop_coord):
    logging.debug('stop coord: {}'.format(stop_coord))
    for r in range(stop_coord[0] + 1, stop_coord[0] + num_rocks + 1):
        logging.debug('({}, {}) = O'.format(r, stop_coord[1]))
        result_grid[r][stop_coord[1]] = 'O'

def calculate_load(result_grid):
    total = 0
    for r in range(len(result_grid)):
        rocks = result_grid[r].count('O')
        logging.debug('{} rock(s) in row {}'.format(rocks, r))
        logging.debug(result_grid[r])
        total += rocks * (len(result_grid) - r)
        logging.debug('total: {}'.format(total))
    return total

# solution functions
def part_a(input):
    result_grid = [['.' for x in range(len(input[0]))] for y in range(len(input))]
    
    logging.debug('source row length: {}'.format(len(input)))
    logging.debug('result grid row length: {}'.format(len(result_grid)))
    logging.debug('source col length: {}'.format(len(input[0])))
    logging.debug('result grid col length: {}'.format(len(result_grid[0])))    
    
    r = len(input) - 1
    c = 0
    while c < len(input[0]):
        rock_counter = 0
        while r >= 0:
            if input[r][c] == 'O':
                rock_counter += 1

            if r == 0:
                move_rocks(result_grid, rock_counter, (r - 1, c))
            if input[r][c] == '#':
                result_grid[r][c] = '#'
                move_rocks(result_grid, rock_counter, (r, c))
                rock_counter = 0
            
            r -= 1
        c += 1
        r = len(input) - 1
    
    logging.debug('\n' + '\n'.join([''.join([item for item in row]) for row in result_grid]))
    return calculate_load(result_grid)

def part_b(input):
    # TODO
    return

def execute():
    input_data = read_aoc_data(14, 2023)
    start_time = time.perf_counter()
    logging.info('part_a answer: {}'.format(part_a(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_a perf: {(end_time - start_time):02f}s")
    start_time = time.perf_counter()
    logging.info('part_b answer: {}'.format(part_b(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_b perf: {(end_time - start_time):02f}s")

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()