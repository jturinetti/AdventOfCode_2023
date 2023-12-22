import time
import logging
from copy import deepcopy
from utils import *
from my_utils import *

def find_start(input):
    for r in range(len(input)):
        s_index = input[r].find('S')
        if s_index > -1:
            return (r, s_index)

def should_walk(input, target_coord, cur_coord):
    return target_coord != cur_coord and input[target_coord[0]][target_coord[1]] == '.'

def walk(input: list, start: tuple, steps: int):
    rows = len(input)
    cols = len(input[0])
    set_queue = set()
    set_queue.add((start, steps))
    final_steps = set()

    # visualization
    result_grid = deepcopy(input)
    result_grid = expand_grid_rows(result_grid)
    # *******

    seen_dict = {}

    while len(list(set_queue)) > 0:
        next = set_queue.pop()
        (cur_coord, steps_remaining) = next
        
        if steps_remaining % 2 == 0:
            final_steps.add(cur_coord)
            if result_grid[cur_coord[0]][cur_coord[1]] != 'S':
                result_grid[cur_coord[0]][cur_coord[1]] = 'O'       # visualization

        if steps_remaining == 0:
            continue

        surrounding_coords = [up_one(cur_coord), down_one(cur_coord, rows), left_one(cur_coord), right_one(cur_coord, cols)]
        for c in surrounding_coords:
            if should_walk(input, c, cur_coord):
                if c in seen_dict:
                    if seen_dict[c] >= steps_remaining:
                        # skip this iteration; we've seen this coord before with larger number of steps remaining
                        continue
                    else:
                        seen_dict[c] = steps_remaining
                else:
                    seen_dict[c] = steps_remaining
                set_queue.add((c, steps_remaining - 1))
    
    # visualization
    print(grid_string(result_grid))
    
    return len(list(final_steps))

# solution functions
def part_a(input, steps = 64):
    # find S
    start_coord = find_start(input)
    print('starting position is {}'.format(start_coord))
    return walk(input, start_coord, steps)

def part_b(input, steps = 26501365):
    # TODO
    return

def execute():
    input_data = read_aoc_data(21, 2023)    # replace with correct day and year
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