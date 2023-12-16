import time
import logging
from utils import *
from my_utils import read_aoc_data

def up_one(coordinate):
    return (coordinate[0] - 1, coordinate[1])

def down_one(coordindate):
    return (coordindate[0] + 1, coordindate[1])

def left_one(coordinate):
    return (coordinate[0], coordinate[1] - 1)

def right_one(coordinate):
    return (coordinate[0], coordinate[1] + 1)

dir_dict = {
    'R': right_one,
    'D': down_one,
    'L': left_one,
    'U': up_one
}

def continue_in_direction(coordinate, direction):
    return dir_dict[direction](coordinate)

def navigate_beam_iter(input, starting_coord, starting_direction):
    current_coord = starting_coord
    direction = starting_direction
    beam_queue = [(current_coord, starting_direction)]
    seen_set = set()
    energized_set = set()
    energized_set.add(current_coord)

    while len(beam_queue) > 0:

        (current_coord, direction) = beam_queue.pop(0)
        if (current_coord, direction) in seen_set:
            continue

        seen_set.add((current_coord, direction))

        if 0 <= current_coord[0] < len(input) and 0 <= current_coord[1] < len(input[0]):
            logging.debug('coord {} energized'.format(current_coord))
            energized_set.add(current_coord)
        else:
            continue

        val = input[current_coord[0]][current_coord[1]]
        logging.debug(current_coord)
        logging.debug(len(beam_queue))
        logging.debug(val)

        # need to handle |, -, ., /, \
        if val == '|' and (direction == 'R' or direction == 'L'):
            beam_queue.append((up_one(current_coord), 'U'))
            beam_queue.append((down_one(current_coord), 'D'))
        elif val == '-' and (direction == 'U' or direction == 'D'):
            beam_queue.append((left_one(current_coord), 'L'))
            beam_queue.append((right_one(current_coord), 'R'))
        elif val == '/':
            if direction == 'R':
                beam_queue.append((up_one(current_coord), 'U'))
            elif direction == 'D':
                beam_queue.append((left_one(current_coord), 'L'))
            elif direction == 'L':
                beam_queue.append((down_one(current_coord), 'D'))
            elif direction == 'U':
                beam_queue.append((right_one(current_coord), 'R'))
        elif val == '\\':
            if direction == 'R':
                beam_queue.append((down_one(current_coord), 'D'))
            elif direction == 'D':
                beam_queue.append((right_one(current_coord), 'R'))
            elif direction == 'L':
                beam_queue.append((up_one(current_coord), 'U'))
            elif direction == 'U':
                beam_queue.append((left_one(current_coord), 'L'))
        else:            
            beam_queue.append((continue_in_direction(current_coord, direction), direction))
    return len(energized_set)

# current_coord is the coord we are ENTERING
# def navigate_beam_rec(input, current_coord, direction, beam_id, beam_coord_dict):
#     if beam_id not in beam_coord_dict:
#         beam_coord_dict[beam_id] = set()

#     # check if we cycled?
#     if current_coord in beam_coord_dict[beam_id]:
#         print('i THINK we cycled?')
#         print('beamid: {}'.format(beam_id))
#         print(beam_coord_dict[beam_id])
#         return beam_coord_dict[beam_id]
    
#     # check boundaries
#     if current_coord[0] < 0 or current_coord[0] >= len(input):
#         # row out of bounds
#         return beam_coord_dict[beam_id]
#     if current_coord[1] < 0 or current_coord[1] >= len(input[0]):
#         # col out of bounds
#         return beam_coord_dict[beam_id]

#     val = input[current_coord[0]][current_coord[1]]
#     beam_coord_dict[beam_id].add((current_coord))

#     # need to handle |, -, ., /, \
#     if val == '|' and (direction == 'R' or direction == 'L'):
#         return beam_coord_dict[beam_id].union(navigate_beam_rec(input, up_one(current_coord), 'U', beam_id + 1, {}).union(navigate_beam_rec(input, down_one(current_coord), 'D', beam_id + 2, {})))
#     elif val == '-' and (direction == 'U' or direction == 'D'):
#         return beam_coord_dict[beam_id].union(navigate_beam_rec(input, left_one(current_coord), 'L', beam_id + 1, {}).union(navigate_beam_rec(input, right_one(current_coord), 'R', beam_id + 2, {})))
#     elif val == '/':
#         if direction == 'R':
#             return navigate_beam_rec(input, up_one(current_coord), 'U', beam_id, beam_coord_dict)
#         elif direction == 'D':
#             return navigate_beam_rec(input, left_one(current_coord), 'L', beam_id, beam_coord_dict)
#         elif direction == 'L':
#             return navigate_beam_rec(input, down_one(current_coord), 'D', beam_id, beam_coord_dict)
#         elif direction == 'U':
#             return navigate_beam_rec(input, right_one(current_coord), 'R', beam_id, beam_coord_dict)
#     elif val == '\\':
#         if direction == 'R':
#             return navigate_beam_rec(input, down_one(current_coord), 'D', beam_id, beam_coord_dict)
#         elif direction == 'D':
#             return navigate_beam_rec(input, right_one(current_coord), 'R', beam_id, beam_coord_dict)
#         elif direction == 'L':
#             return navigate_beam_rec(input, up_one(current_coord), 'U', beam_id, beam_coord_dict)
#         elif direction == 'U':
#             return navigate_beam_rec(input, left_one(current_coord), 'L', beam_id, beam_coord_dict)
#     else:
#         return navigate_beam_rec(input, continue_in_direction(current_coord, direction), direction, beam_id, beam_coord_dict)

# solution functions
def part_a(input):
    current_coord = (0, 0)
    direction = 'R'
    
    return navigate_beam_iter(input, current_coord, direction)

def part_b(input):
    grid_rows = len(input)
    grid_cols = len(input[0])
    max_val = 0
    # top and bottom    
    logging.info('scanning across top of grid')
    for c in range(grid_cols):
        coord = (0, c)
        logging.debug(coord)
        ret = navigate_beam_iter(input, coord, 'D')
        if ret > max_val:
            logging.debug('new max: {}'.format(ret))
            max_val = ret    
    logging.info('scanning across bottom of grid')
    for c in range(grid_cols):
        coord = (grid_rows - 1, c)
        logging.debug(coord)
        ret = navigate_beam_iter(input, coord, 'U')
        if ret > max_val:
            logging.debug('new max: {}'.format(ret))
            max_val = ret
    # left and right
    logging.info('scanning across left of grid')
    for r in range(grid_rows):
        coord = (r, 0)
        logging.debug(coord)
        ret = navigate_beam_iter(input, (r, 0), 'R')
        if ret > max_val:
            logging.debug('new max: {}'.format(ret))
            max_val = ret
    logging.info('scanning across right of grid')
    for r in range(grid_rows):
        coord = (r, grid_cols - 1)
        logging.debug(coord)
        ret = navigate_beam_iter(input, (r, grid_cols - 1), 'L')
        if ret > max_val:
            logging.debug('new max: {}'.format(ret))
            max_val = ret
    return max_val

def execute():
    input_data = read_aoc_data(16, 2023)
    start_time = time.perf_counter()
    logging.info('part_a answer: {}'.format(part_a(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_a perf: {(end_time - start_time):02f}s")
    # start_time = time.perf_counter()
    # logging.info('part_b answer: {}'.format(part_b(input_data)))
    # end_time = time.perf_counter()
    # logging.info(f"part_b perf: {(end_time - start_time):02f}s")

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()