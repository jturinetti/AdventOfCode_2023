import time
import logging
from utils import *
from my_utils import read_aoc_data, add, sub

def build_prediction_tree(num_list, math_func, history_index):
    extrapolated_level = []
    for index in range(len(num_list) - 1):
        extrapolated_level.append(num_list[index + 1] - num_list[index])
    if extrapolated_level[1:] == extrapolated_level[:-1]:
        return math_func(num_list[history_index], extrapolated_level[history_index])
    else:
        return math_func(num_list[history_index], build_prediction_tree(extrapolated_level, math_func, history_index))

# solution functions
def part_a(input):
    total = 0
    for row in input:
        history = list(map(int, row.split(' ')))
        total += build_prediction_tree(history, add, -1)
    return total

def part_b(input):
    total = 0
    for row in input:
        history = list(map(int, row.split(' ')))
        total += build_prediction_tree(history, sub, 0)
    return total

def execute():
    input_data = read_aoc_data(9, 2023)
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