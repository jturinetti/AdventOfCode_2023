import time
import logging
from utils import *
from my_utils import read_aoc_data
from math import lcm

def construct_dictionary(mapping_list):
    dict = {}
    for mapping in mapping_list:
        key = mapping[:3]
        val1 = mapping[7:10]
        val2 = mapping[12:15]
        dict[key] = (val1, val2)
    return dict

def navigate_to_next_node(dictionary, key, instruction_char):
    if instruction_char == 'L':
        return dictionary[key][0]
    else:
        return dictionary[key][1]

# solution functions
def part_a(input):
    instructions = input[0]
    dictionary = construct_dictionary(input[2:])
    step_counter = 0
    instruction_index = 0
    current = 'AAA'
    while current != 'ZZZ':
        step_counter += 1
        next_instruction = instructions[instruction_index]
        instruction_index += 1
        if instruction_index == len(instructions):
            instruction_index = 0
        current = navigate_to_next_node(dictionary, current, next_instruction)
    return step_counter

def part_b(input):
    instructions = input[0]
    dictionary = construct_dictionary(input[2:])
    step_counter = 0
    instruction_index = 0
    instruction_tree_index = 0
    current_instruction_list = [x for x in dictionary.keys() if str.endswith(x, 'A')]
    next_instruction = instructions[instruction_index]
    lcm_dict = {}
    while not all(str.endswith(x, 'Z') for x in current_instruction_list):
        current_instruction_list[instruction_tree_index] = navigate_to_next_node(dictionary, current_instruction_list[instruction_tree_index], next_instruction)
        
        if str.endswith(current_instruction_list[instruction_tree_index], 'Z') and instruction_tree_index not in lcm_dict:
            lcm_dict[instruction_tree_index] = step_counter + 1
    
        if len(list(lcm_dict.keys())) == len(current_instruction_list):
            return lcm(*[v for v in lcm_dict.values()])
            
        instruction_tree_index += 1
        if instruction_tree_index == len(current_instruction_list):
            step_counter += 1
            instruction_index += 1
            instruction_tree_index = 0
            if instruction_index == len(instructions):
                instruction_index = 0
            next_instruction = instructions[instruction_index]

    # we should never get to this point; lcm result should be returned first always        
    return step_counter

def execute():
    input_data = read_aoc_data(8, 2023)    # replace with correct day and year
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