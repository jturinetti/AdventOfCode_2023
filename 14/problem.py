import time
import logging
from copy import deepcopy
from utils import *
from my_utils import read_aoc_data, generate_empty_grid, grid_string

# TODO - north/south and east/west functions can be consolidated

def move_rocks_north(result_grid, num_rocks, stop_coord):
    logging.debug('moving north, stop coord: {}'.format(stop_coord))
    for r in range(stop_coord[0] + 1, stop_coord[0] + num_rocks + 1):
        logging.debug('({}, {}) = O'.format(r, stop_coord[1]))
        result_grid[r][stop_coord[1]] = 'O'

def scan_rocks_north(input, result_grid):
    r = len(input) - 1
    c = 0
    while c < len(input[0]):
        rock_counter = 0
        while r >= 0:
            if input[r][c] == 'O':
                rock_counter += 1

            if r == 0:
                move_rocks_north(result_grid, rock_counter, (r - 1, c))
            if input[r][c] == '#':
                result_grid[r][c] = '#'
                move_rocks_north(result_grid, rock_counter, (r, c))
                rock_counter = 0
            
            r -= 1
        c += 1
        r = len(input) - 1

def move_rocks_west(result_grid, num_rocks, stop_coord):
    logging.debug('moving west, stop coord: {}'.format(stop_coord))
    for c in range(stop_coord[1] + 1, stop_coord[1] + num_rocks + 1):
        logging.debug('({}, {}) = O'.format(stop_coord[0], c))
        result_grid[stop_coord[0]][c] = 'O'

def scan_rocks_west(input, result_grid):
    r = 0
    c = len(input[0]) - 1
    while r < len(input):
        rock_counter = 0
        while c >= 0:
            if input[r][c] == 'O':
                rock_counter += 1

            if c == 0:
                move_rocks_west(result_grid, rock_counter, (r, c - 1))
            if input[r][c] == '#':
                result_grid[r][c] = '#'
                move_rocks_west(result_grid, rock_counter, (r, c))
                rock_counter = 0
            
            c -= 1
        r += 1
        c = len(input[0]) - 1

def move_rocks_south(result_grid, num_rocks, stop_coord):
    logging.debug('moving south, stop coord: {}'.format(stop_coord))
    for r in range(stop_coord[0] - num_rocks, stop_coord[0]):
        logging.debug('({}, {}) = O'.format(r, stop_coord[1]))
        result_grid[r][stop_coord[1]] = 'O'

def scan_rocks_south(input, result_grid):
    r = 0
    c = 0
    while c < len(input[0]):
        rock_counter = 0
        while r < len(input):
            if input[r][c] == 'O':
                rock_counter += 1

            if r == len(input) - 1:
                move_rocks_south(result_grid, rock_counter, (r + 1, c))
            if input[r][c] == '#':
                result_grid[r][c] = '#'
                move_rocks_south(result_grid, rock_counter, (r, c))
                rock_counter = 0
            
            r += 1
        c += 1
        r = 0

def move_rocks_east(result_grid, num_rocks, stop_coord):
    logging.debug('moving east, stop coord: {}'.format(stop_coord))
    for c in range(stop_coord[1] - num_rocks, stop_coord[1]):
        logging.debug('({}, {}) = O'.format(stop_coord[0], c))
        result_grid[stop_coord[0]][c] = 'O'

def scan_rocks_east(input, result_grid):
    r = 0
    c = 0
    while r < len(input):
        rock_counter = 0
        while c < len(input[0]):
            if input[r][c] == 'O':
                rock_counter += 1

            if c == len(input[0]) - 1:
                move_rocks_east(result_grid, rock_counter, (r, c + 1))
            if input[r][c] == '#':
                result_grid[r][c] = '#'
                move_rocks_east(result_grid, rock_counter, (r, c))
                rock_counter = 0
            
            c += 1
        r += 1
        c = 0

def calculate_load(result_grid):
    total = 0
    for r in range(len(result_grid)):
        rocks = result_grid[r].count('O')
        logging.debug('{} rock(s) in row {}'.format(rocks, r))
        logging.debug(result_grid[r])
        total += rocks * (len(result_grid) - r)
        logging.debug('total: {}'.format(total))
    return total

def perform_full_cycle(input_grid, output_grid):
    dimensions = (len(input_grid), len(input_grid[0]))
    # north
    scan_rocks_north(input_grid, output_grid)
    input_grid = deepcopy(output_grid)  
    output_grid = generate_empty_grid(dimensions[0], dimensions[1], '.')
    logging.debug('grid after north moves: ')
    logging.debug(grid_string(input_grid))
    # west
    scan_rocks_west(input_grid, output_grid)
    input_grid = deepcopy(output_grid)  
    output_grid = generate_empty_grid(dimensions[0], dimensions[1], '.')
    logging.debug('grid after west moves: ')
    logging.debug(grid_string(input_grid))
    # south
    scan_rocks_south(input_grid, output_grid)
    input_grid = deepcopy(output_grid)  
    output_grid = generate_empty_grid(dimensions[0], dimensions[1], '.')
    logging.debug('grid after south moves: ')
    logging.debug(grid_string(input_grid))
    # east
    scan_rocks_east(input_grid, output_grid)
    logging.debug('grid after east moves: ')
    logging.debug(grid_string(output_grid))
    return output_grid

# solution functions
def part_a(input):
    result_grid = generate_empty_grid(len(input), len(input[0]), '.')
    scan_rocks_north(input, result_grid)
    logging.debug(grid_string(result_grid))
    return calculate_load(result_grid)

def part_b(input, num_cycles = 1000000000):
    dimensions = (len(input), len(input[0]))
    result_grid = generate_empty_grid(dimensions[0], dimensions[1], '.')
    cycle_counter = 0
    cycle_detected = False
    updated_grid = []
    hash_map = set()
    hash_list = []
    while cycle_counter < num_cycles:
        logging.debug('CYCLE {} STARTING'.format(cycle_counter + 1))
        
        # perform cycle
        updated_grid = perform_full_cycle(input, result_grid)

        if not cycle_detected:
            # hash it
            hashed_val = hash(''.join([''.join([item for item in row]) for row in updated_grid]))
            logging.debug('hash value: {}'.format(hashed_val))

            # check for cycle
            if hashed_val in hash_map:
                logging.info('CYCLE DETECTED! hash value {} found!'.format(hashed_val))
                cycle_detected = True

                # find index or first instance of hash
                existing_hash_index = 0
                for x in range(len(hash_list)):
                    if hash_list[x] == hashed_val:
                        existing_hash_index = x
                        break

                # find remaining cycles and execute                
                cycle_length = len(hash_list) - existing_hash_index
                not_in_loop = existing_hash_index
                cycles_left = (num_cycles - not_in_loop) % cycle_length

                num_cycles = cycle_counter + cycles_left    # shortens loop                            
            else:
                hash_map.add(hashed_val)
                hash_list.append(hashed_val)
                 

        # update input variable with latest result_grid
        input = deepcopy(updated_grid)
        result_grid = generate_empty_grid(dimensions[0], dimensions[1], '.')
        cycle_counter += 1

    return calculate_load(updated_grid)

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
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()