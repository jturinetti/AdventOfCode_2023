import time
import logging
from utils import *
from my_utils import read_aoc_data

# solution functions
def part_a(input):
    # TODO
    return

def part_b(input):
    # TODO
    return

def execute():
    input_data = read_aoc_data(6, 2023)    # replace with correct day and year
    start_time = time.perf_counter()
    print(part_a(input_data))
    end_time = time.perf_counter()
    print(f"part_a perf: {(end_time - start_time):02f}")
    start_time = time.perf_counter()
    print(part_b(input_data))
    end_time = time.perf_counter()
    print(f"part_b perf: {(end_time - start_time):02f}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s %(funcName)s %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()