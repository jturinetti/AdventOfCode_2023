import time
import logging
from utils import *
from my_utils import *

def slope(cur_symbol, cur_coord, steps_taken):
    if cur_symbol == '<':
        return ((cur_coord[0], cur_coord[1] - 1), steps_taken + 1)
    elif cur_symbol == '>':
        return ((cur_coord[0], cur_coord[1] + 1), steps_taken + 1)
    elif cur_symbol == '^':
        return ((cur_coord[0] - 1, cur_coord[1]), steps_taken + 1)
    elif cur_symbol == 'v':
        return ((cur_coord[0] + 1, cur_coord[1]), steps_taken + 1)
    
    return (cur_coord, steps_taken)

def walk(input, cur_coord, end, steps_taken, seen: set):

    # state stored in queue: (coord, steps_taken, seen_set)
    step_queue = [(cur_coord, steps_taken, seen)]
    max_steps = 0
    while len(step_queue) > 0:
        # take coord and fully traverse down path
        (cur_coord, steps_taken, seen) = step_queue.pop(0)

        while True:
            seen.add(cur_coord)
            steps_taken += 1

            if cur_coord == end:
                break

            # if slope, move to next space
            (cur_coord, steps_taken) = slope(input[cur_coord[0]][cur_coord[1]], cur_coord, steps_taken)

            # find next coords
            surrounding_coords = [
                (up_one(cur_coord), ['.', '>', '<', '^']), 
                (down_one(cur_coord, len(input)), ['.', '>', '<', 'v']), 
                (left_one(cur_coord), ['.', '<', 'v', '^']), 
                (right_one(cur_coord, len(input[0])), ['.', '>', 'v', '^'])]
            next_coords = []
            for c in surrounding_coords:
                if input[c[0][0]][c[0][1]] in c[1] and c[0] not in seen:
                # if input[c[0][0]][c[0][1]] != '#' and c[0] not in seen:
                    next_coords.append((c[0], steps_taken, seen.copy()))
            
            if len(next_coords) == 0:
                steps_taken = -1
                break
            
            cur_coord = next_coords[0][0]
            step_queue = step_queue + next_coords[1:]
        
        if steps_taken > max_steps:
            max_steps = steps_taken

    return max_steps

# solution functions
def part_a(input):
    start = (0, 1)
    end = (len(input) - 1, len(input[0]) - 2)
    return walk(input, start, end, 0, set()) - 1

def part_b(input):
    # TODO
    return

def execute():
    input_data = read_aoc_data(23, 2023)
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