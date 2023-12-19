import time
import logging
from typing import Sequence
from utils import *
from my_utils import *

direction_map = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U'
}

def parse_row(input_row):
    split_input = input_row.split(' ')
    return (split_input[0], int(split_input[1]), split_input[2])

def parse_color_ins(color_string):
    length = int(color_string[2:-2], 16)
    direction = direction_map[int(color_string[-2])]
    return (length, direction)

def dig(current_coord, direction, length):
    sub_path = []
    multiplier = 1
    if direction == 'L' or direction == 'D':
        multiplier = -1
    
    final_coord = (0, 0)

    if direction == 'L' or direction == 'R':
        for n in range(length + 1):
            coord = (current_coord[0], current_coord[1] + (multiplier * n))
            sub_path.append(coord)
            final_coord = coord
    elif direction == 'U' or direction == 'D':
        for n in range(length + 1):
            coord = (current_coord[0] + (multiplier * n), current_coord[1])
            sub_path.append(coord)
            final_coord = coord
    return (sub_path, final_coord)

# solution functions
def part_a(input):
    current_coord = (0, 0)
    path = []

    for r in input:
        (direction, length, color) = parse_row(r)
        (sub_path, final_coord) = dig(current_coord, direction, length)
        path = path + sub_path[:-1]        
        current_coord = final_coord
    
    inner_area = calculate_inner_area(path)
    return len(path) + inner_area

def part_b(input):
    current_coord = (0, 0)
    path = []

    for r in input:
        (old_direction, old_length, color) = parse_row(r)
        (length, direction) = parse_color_ins(color)
        (sub_path, final_coord) = dig(current_coord, direction, length)
        path = path + sub_path[:-1]
        current_coord = final_coord

    return picks(path, len(path))

def execute():
    input_data = read_aoc_data(18, 2023)
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