import time
import logging
from utils import *
import re
import more_itertools
from functools import cache
from my_utils import read_aoc_data

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

def unfold(gear_string, arrangements):
    orig_str = gear_string
    orig_a = arrangements
    for n in range(4):
        if n != 4:
            gear_string += '?'
        gear_string = gear_string + orig_str
        arrangements = arrangements + orig_a
    
    return (gear_string, arrangements)

@functools.cache
def find_recursive_matches(gear_string, arrangements):
    print(arrangements)
    logging.debug('gear string: {}, arrangements: {}'.format(gear_string, arrangements))
    
    arr_list = []
    if '-' in arrangements:
        arr_list = list(map(int, arrangements.split('-')))
    elif arrangements != '':
        arr_list = [int(arrangements)]
    else:
        arr_list = []
        
    total_remaining = sum(arr_list)
    gears_remaining = gear_string.count('#')
    symbols_remaining = gears_remaining + gear_string.count('?')

    if gears_remaining > total_remaining or symbols_remaining < total_remaining:
        return 0
    
    if total_remaining == 0:
        return 1
    
    if gear_string[0] == '.':
        return find_recursive_matches(gear_string[1:], arrangements)

    if gear_string[0] == '#':
        match = re.search('[#?]{{{}}}'.format(arr_list[0]), gear_string)
        if match and match.start() == 0:        
            if len(arr_list) == 1 and len(gear_string) == arr_list[0]:
                return 1
            print(gear_string)
            print(match.end())
            if gear_string[match.end()] == '#':
                return 0
            return find_recursive_matches(gear_string[match.end() + 1:], '-'.join(map(str, arr_list[1:])))
        return 0
    
    # gear_string must start with ? at this point
    return find_recursive_matches(gear_string[1:], arrangements) + find_recursive_matches('#' + gear_string[1:], arrangements)

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

def part_b(input):
    counter = 0
    for row in input:
        (gear_string, arrangements) = parse_row(row)
        
        # unfold!
        (gear_string, arrangements) = unfold(gear_string, arrangements)
        
        result = find_recursive_matches(gear_string, '-'.join(map(str, arrangements)))
        logging.info('{} matches found for gear string {} and arrangements {}'.format(result, gear_string, arrangements))
        counter += result
    print(find_recursive_matches.cache_info())
    return counter

def execute():
    input_data = read_aoc_data(12, 2023)
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