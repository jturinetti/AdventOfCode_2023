import time
import logging
from utils import *
from my_utils import read_aoc_data

def parse_input(input):
    galaxy_coords = []
    empty_rows = []
    empty_cols = []
    for row_index in range(len(input)):
        found = False
        for col_index in range(len(input[row_index])):
            if input[row_index][col_index] == '#':
                galaxy_coords.append((row_index, col_index))
                found = True
        if not found:
            empty_rows.append(row_index)
    
    # find empty columns
    for col_index in range(len(input[0])):
        found = False
        for row in input:
            if row[col_index] == '#':
                found = True

        if not found: 
            empty_cols.append(col_index)
    
    return (galaxy_coords, empty_rows, empty_cols)

def get_distance(coord_1, coord_2, empty_rows, empty_cols, expansion_factor):
    # return math.sqrt((coord_2[0] - coord_1[0])**2 + (coord_2[1] - coord_1[1])**2)
    # use Manhattan distance for this
    raw_sum = abs((coord_2[0] - coord_1[0])) + abs(coord_2[1] - coord_1[1])
    expanded_rows = (expansion_factor - 1) * len(list(filter(lambda r: (coord_1[0] > r > coord_2[0]) or (coord_2[0] > r > coord_1[0]), empty_rows)))
    expanded_cols = (expansion_factor - 1) * len(list(filter(lambda c: (coord_1[1] > c > coord_2[1]) or (coord_2[1] > c > coord_1[1]), empty_cols)))
    
    return raw_sum + expanded_cols + expanded_rows

def solution_impl(galaxy_coords, empty_rows, empty_cols, expansion_factor):
    sum = 0
    cur_galaxy = 0
    while cur_galaxy < len(galaxy_coords) - 1:
        for other_galaxy in range(cur_galaxy + 1, len(galaxy_coords)):
            val = get_distance(galaxy_coords[cur_galaxy], galaxy_coords[other_galaxy], empty_rows, empty_cols, expansion_factor)
            logging.debug('{} and {}: {}'.format(galaxy_coords[cur_galaxy], galaxy_coords[other_galaxy], val))
            sum += val
        cur_galaxy += 1
    return sum

# solution functions
def part_a(input):
    (galaxy_coords, empty_rows, empty_cols) = parse_input(input)
    return solution_impl(galaxy_coords, empty_rows, empty_cols, 2)

def part_b(input, expansion_factor = 1000000):
    (galaxy_coords, empty_rows, empty_cols) = parse_input(input)
    return solution_impl(galaxy_coords, empty_rows, empty_cols, expansion_factor)

def execute():
    input_data = read_aoc_data(11, 2023)
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