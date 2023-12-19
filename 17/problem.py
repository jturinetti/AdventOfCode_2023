import time
import logging
from utils import *
from my_utils import *

def calculate_path_changes(input, diff_grid, cur_coord, direction = ''):
    for r in range(1,3):
        diff_grid[cur_coord[0] + r][cur_coord[1]] = diff_grid

# solution functions
def part_a(input):
    diff_grid = generate_empty_grid(len(input), len(input[0]), 0)
    diff_grid[0][0] = int(input[0][0])
    calculate_path_changes(input, diff_grid)
    return

def part_b(input):
    # TODO
    return

def execute():
    input_data = read_aoc_data(17, 2023)
    start_time = time.perf_counter()
    logging.info('part_a answer: {}'.format(part_a(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_a perf: {(end_time - start_time):02f}s")
    start_time = time.perf_counter()
    logging.info('part_b answer: {}'.format(part_b(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_b perf: {(end_time - start_time):02f}s")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()