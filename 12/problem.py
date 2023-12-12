import time
import logging
from utils import *
import re
import itertools
import more_itertools
from my_utils import read_aoc_data, parse_multi_line_input

def parse_row(row):
    data = row.split(' ')
    arrangements = data[1].split(',')
    return (data[0], lmap(int, arrangements))

def create_permutation_seed(total_gear_count, existing_gear_count, question_mark_count):
    return str("#" * (total_gear_count - existing_gear_count)) + str("." * (question_mark_count - (total_gear_count - existing_gear_count)))

def create_regex_pattern(arrangement_list):
    template_str = '[.]*'
    for n in range(len(arrangement_list)):
        template_str += "[#]{{{}}}".format(arrangement_list[n])
        if n == len(arrangement_list) - 1:
            template_str = template_str + '[.]*'
        else:
            template_str = template_str + '[.]+'
    return template_str

def find_matches_in_permutations(permutations, gear_string, template_string):
    counter = 0
    for p in permutations:
        new_string = ''
        perm_index = 0
        for c in gear_string:
            if c == '?':
                new_string = new_string + p[perm_index]
                perm_index += 1
            else:
                new_string = new_string + c
        test = re.search(template_string, new_string)
        if test is not None:
            logging.debug('match! {}'.format(new_string))
            counter += 1
    logging.debug('{} has {} arrangement(s)'.format(gear_string, counter))
    return counter

# solution functions
def part_a(input):
    counter = 0
    for row in input:
        (gear_string, arrangements) = parse_row(row)
        q_count = gear_string.count('?')
        existing_gears = gear_string.count('#')
        total_gears = sum(arrangements)
        logging.debug('{} total gears'.format(total_gears))
        logging.debug('{} q_count'.format(q_count))
        perm_str = create_permutation_seed(total_gears, existing_gears, q_count)
        logging.debug('testing {}'.format(list(perm_str)))
        logging.debug('generating permutations')
        perms = more_itertools.distinct_permutations(perm_str, q_count)
        logging.debug('permutations generated')    
        
        template_str = create_regex_pattern(arrangements)
        logging.debug(template_str)        
        counter += find_matches_in_permutations(perms, gear_string, template_str)
    return counter

# WIP: part b needs to be smarter. part a approach is not optimized for this data set
def part_b(input):
    counter = 0
    for row in input:
        (gear_string, arrangements) = parse_row(row)
        
        # unfold!
        orig_str = gear_string
        orig_a = arrangements
        for n in range(4):
            gear_string = gear_string + orig_str
            if n != 4:
                gear_string += '?'
            arrangements = arrangements + orig_a
        logging.debug(gear_string)
        q_count = gear_string.count('?')
        existing_gears = gear_string.count('#')
        total_gears = sum(arrangements)
        
        # TODO

    return -1

def execute():
    input_data = read_aoc_data(12, 2023)    # replace with correct day and year
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