import time
import logging
from utils import *
from my_utils import read_aoc_data

from shapely.geometry import Point
from shapely.geometry import Polygon

def recurse_pipe(input, seen_points, last_point, row, col):
    next = None

    # check north
    if row > 0 and input[row][col] in ['|', 'L', 'J', 'S'] and input[row - 1][col] in ['F', '7', '|'] and (row - 1, col) != last_point:
        # can proceed north
        # logging.debug('north')
        next = (row - 1, col)
    # check west
    elif col > 0 and input[row][col] in ['-', 'J', '7', 'S'] and input[row][col - 1] in ['-', 'L', 'F'] and (row, col - 1) != last_point:
        # can proceed west
        # logging.debug('west')
        next = (row, col - 1)
    # check south
    elif row < len(input) - 1 and input[row][col] in ['F', '7', '|', 'S'] and input[row + 1][col] in ['|', 'L', 'J'] and (row + 1, col) != last_point:
        # can proceed south
        # logging.debug('south')
        next = (row + 1, col)
    # check east
    elif col < len(input[row]) - 1 and input[row][col] in ['-', 'L', 'F', 'S'] and input[row][col + 1] in ['-', 'J', '7'] and (row, col + 1) != last_point:
        # can proceed east
        # logging.debug('east')
        next = (row, col + 1)
    
    if next is None and last_point is not None:
        return seen_points

    return recurse_pipe(input, seen_points + [next], (row, col), next[0], next[1])

def check_if_contained(input, pipe_path, cache, accumulator, row, col):
    # check north
    # check west
    # check south
    # check east

    # between the pipes up/down
    # '7F', '||', '7L', '7|', '|F', '|L', 'J|', 'JF', 'JL'
    # between the pipes left/right
    # -
    # 7
    # -
    # F
    # -
    # 

    return []

def draw_bounding_box(path):
    min_x = None
    min_y = None
    max_x = None
    max_y = None
    for point in path:
        if min_x is None or point[0] < min_x:
            min_x = point[0]
        if min_y is None or point[1] < min_y:
            min_y = point[1]
        if max_x is None or point[0] > max_x:
            max_x = point[0]
        if max_y is None or point[1] > max_y:
            max_y = point[1]
    bounding_box_points = [(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)]
    logging.debug(bounding_box_points)
    return bounding_box_points
    
# solution functions
def part_a(input):
    s_found = False
    s_row_index = 0
    s_col_index = 0
    while s_row_index < len(input) and s_found == False:
        while s_col_index < len(input[s_row_index]) and s_found == False:
            if input[s_row_index][s_col_index] == 'S':
                s_found = True
                break
            s_col_index += 1
        if s_found == False:
            s_col_index = 0
            s_row_index += 1
    
    print('{}, {}'.format(s_row_index, s_col_index))

    seen_points = [(s_row_index, s_col_index)]

    # test each direction starting from S and keep track of seen indices
    # find one connecting pipe and go from there
    
    # here we go
    pipe_path = recurse_pipe(input, seen_points, None, s_row_index, s_col_index)
    return len(pipe_path) / 2

def part_b(input):
    s_found = False
    s_row_index = 0
    s_col_index = 0
    while s_row_index < len(input) and s_found == False:
        while s_col_index < len(input[s_row_index]) and s_found == False:
            if input[s_row_index][s_col_index] == 'S':
                s_found = True
                break
            s_col_index += 1
        if s_found == False:
            s_col_index = 0
            s_row_index += 1
    
    print('{}, {}'.format(s_row_index, s_col_index))

    seen_points = [(s_row_index, s_col_index)]

    # test each direction starting from S and keep track of seen indices
    # find one connecting pipe and go from there
    
    # here we go
    pipe_path = recurse_pipe(input, seen_points, None, s_row_index, s_col_index)

    # draw box
    bounding_box = draw_bounding_box(pipe_path)

    # iterate through box and check each
    # 6 - 133
    # 1 - 135
    # TODO - make this programmatic
    polygon = Polygon(pipe_path)
    enclosed_spaces = []
    counter = 0
    for r in range(6, 133):
        for c in range(1, 135):
            if (r, c) in pipe_path:
                continue
            if (r, c) in enclosed_spaces:
                continue
            
            point = Point(r, c)
            if polygon.contains(point):
                counter += 1
            # enclosed_spaces += check_if_contained(input, pipe_path, {}, [], r, c)
    
    logging.debug(input)
    # return len(enclosed_spaces)
    return counter

def execute():
    input_data = read_aoc_data(10, 2023)
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