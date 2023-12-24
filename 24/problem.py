import time
import logging
from utils import *
from my_utils import read_aoc_data

def parse(row):
    sr = row.split(' @ ')
    coord_arr = sr[0].split(', ')
    coord = int(coord_arr[0]), int(coord_arr[1]), int(coord_arr[2])
    slope_arr = sr[1].split(', ')
    slope = int(slope_arr[0]), int(slope_arr[1]), int(slope_arr[2])
    return (coord, slope)

# solution functions
def part_a(input):
    bounds_min = 200000000000000
    bounds_max = 400000000000000
    for p1_index in range(len(input)):
        for p2_index in range(p1_index + 1, len(input)):
            (p1_coord, p1_slope) = parse(input[p1_index])
            (p2_coord, p2_slope) = parse(input[p2_index])
            
    return

def part_b(input):
    # TODO
    return

def execute():
    input_data = read_aoc_data(24, 2023)    # replace with correct day and year
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