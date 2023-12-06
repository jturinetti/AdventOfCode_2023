import time
import logging
from utils import *
from my_utils import read_aoc_data

def parse_multiple_races(input):
    return list(zip(ints(input[0]), ints(input[1])))

def parse_single_race(input):
    # probably overly complicated
    return [(int("".join(map(str, ints(input[0])))), int("".join(map(str, ints(input[1])))))]

# brute force solution, which could be replaced by the quadratic formula to improve performance
def solution_impl(races):
    running_total = None
    for index in range(len(races)):
        race_time = races[index][0]
        race_distance = races[index][1]
        counter = 0
        found_start = False
        found_end = False
        charge_hold_time = 1
        while charge_hold_time < race_time and not found_end:
            remaining_time = race_time - charge_hold_time
            if remaining_time * charge_hold_time > race_distance:
                counter += 1
                found_start = True
            elif found_start:
                # short-circuit once we start seeing shorter distances for hold times
                found_end = True
                
            charge_hold_time += 1
        
        if running_total is None:
            running_total = counter
        else:
            running_total = running_total * counter

    return running_total

# solution functions
def part_a(input):   
    races = parse_multiple_races(input)
    logging.debug(races)
    return solution_impl(races)

def part_b(input):
    races = parse_single_race(input)
    logging.debug(races)
    return solution_impl(races)

def execute():
    input_data = read_aoc_data(6, 2023)
    start_time = time.perf_counter()
    logging.info(part_a(input_data))
    end_time = time.perf_counter()
    logging.info(f"part_a perf: {(end_time - start_time):02f}s")
    start_time = time.perf_counter()
    logging.info(part_b(input_data))
    end_time = time.perf_counter()
    logging.info(f"part_b perf: {(end_time - start_time):02f}s")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()