import time
import logging
from utils import *
from my_utils import read_aoc_data

def calculate_target_mapping(source_number, mapping_lists):
    for index in range(len(mapping_lists)):
        l = mapping_lists[index]
        target_range_start = l[0]
        source_range_start = l[1]
        range_length = l[2]
        if source_number >= source_range_start and source_number <= source_range_start + range_length - 1:
            return (source_number - source_range_start + target_range_start)
    
    return source_number

def construct_seed_array(input):
    return lmap(lambda x: int(x), input[0].split(' ')[1::])

def populate_mapping_dictionaries(input, mapping_dict, name_dict, reverse_name_dict):
    current_target = ''
    for index in range(2, len(input)):
        s = input[index]
        if s == '':
            continue
        parsed_entry = s.split(' ')[0]
        if not parsed_entry.isdigit():
            parsed_mapping_names = parsed_entry.split('-')
            source = parsed_mapping_names[0]
            target = parsed_mapping_names[2]
            name_dict[source] = target
            reverse_name_dict[target] = source
            current_target = target
            mapping_dict[target] = []
        else:
            parsed_mapping_values = lmap(lambda x: int(x), s.split(' '))
            mapping_dict[current_target].append(parsed_mapping_values)

def solution_impl(input, seed_array):
    mapping_dictionary = {}
    name_dictionary = {}
    reverse_name_dictionary = {}
    
    populate_mapping_dictionaries(input, mapping_dictionary, name_dictionary, reverse_name_dictionary)

    current_key = 'seed'
    lowest = None
    
    for seed in seed_array:
        current_map_value = seed
        while (current_key in name_dictionary):
            target = name_dictionary[current_key]
            current_map_value = calculate_target_mapping(current_map_value, mapping_dictionary[target])
            current_key = target
        
        if lowest is None or current_map_value < lowest:
            lowest = current_map_value
        
        current_key = 'seed'

    return lowest

# solution functions
def part_a(input):
    seed_array = construct_seed_array(input)
    return solution_impl(input, seed_array)

def part_b(input):
    seed_array = construct_seed_array(input)
    mapping_dictionary = {}
    reverse_name_dictionary = {}
    name_dictionary = {}
   
    populate_mapping_dictionaries(input, mapping_dictionary, name_dictionary, reverse_name_dictionary)
    
    # TODO: WIP - this currently wrong
    current_key = 'location'
    for potential_location in range(min(seed_array), max(flatten(mapping_dictionary[current_key])), 1):
        current_map_value = potential_location
        
        while (current_key in reverse_name_dictionary):
            target = reverse_name_dictionary[current_key]
            
            if target == 'seed':
                for seed_index in range(0, len(seed_array), 2):
                   
                    if current_map_value >= seed_array[seed_index] and current_map_value <= (seed_array[seed_index] + seed_array[seed_index + 1]):
                        return potential_location
                    else:
                        break
            else:
                current_map_value = calculate_target_mapping(current_map_value, mapping_dictionary[target])
            
            current_key = target
        
        current_key = 'location'
    return -1

    # TODO: this is correct, but it's a brute force approach and it needs to be optimized
    lowest = None
    current_key = 'seed'
    
    for index in range(0, len(seed_array), 2):
        for seed in range(seed_array[index], seed_array[index] + seed_array[index + 1], 1):
            current_map_value = seed

            while (current_key in name_dictionary):
                target = name_dictionary[current_key]
                current_map_value = calculate_target_mapping(current_map_value, mapping_dictionary[target])
                current_key = target

            if lowest is None or current_map_value < lowest:
                lowest = current_map_value
        
            current_key = 'seed'
    return lowest

def execute():
    input_data = read_aoc_data(5, 2023)
    start_time = time.perf_counter()
    print(part_a(input_data))
    end_time = time.perf_counter()
    print(f"part_a perf: {(end_time - start_time):02f}")
    start_time = time.perf_counter()
    print(part_b(input_data))
    end_time = time.perf_counter()
    print(f"part_b perf: {(end_time - start_time):02f}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, 
                        format='%(asctime)s %(funcName)s %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()