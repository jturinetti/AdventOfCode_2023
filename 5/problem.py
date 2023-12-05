import time
from utils import *
from my_utils import read_aoc_data

def calculate_target_mapping(source_number, mapping_lists):
    for index in range(len(mapping_lists)):
        l = mapping_lists[index]
        target_range_start = l[0]
        source_range_start = l[1]
        range_length = l[2]
        if source_number >= source_range_start and source_number <= source_range_start + range_length - 1:
            # print("YES")
            # print("{} -> {}".format(source_number, l))
            return (source_number - source_range_start + target_range_start)
    
    # print("NO, returning {}".format(source_number))
    return source_number

def construct_seed_array(input, part):
    seed_array = lmap(lambda x: int(x), input[0].split(' ')[1::])
    if (part == 'a'):
        return seed_array
    
    print(seed_array)
    if (part == 'b'):
        expanded_seed_array = []
        for index in range(0, len(seed_array), 2):
            print(index)
            temp = range(seed_array[index], seed_array[index] + seed_array[index + 1], 1)
            print(temp)
            expanded_seed_array.extend(range(seed_array[index], seed_array[index] + seed_array[index + 1], 1))
        # print(expanded_seed_array)
        return expanded_seed_array

def solution_impl(input, seed_array):
    mapping_dictionary = {}
    name_dictionary = {}
    # index into dictionary based on source string
    # determine mapping value
    # find next dictionary based on target string
    current_target = ''
    print(input)
    for index in range(2, len(input)):
        s = input[index]
        # print(s)
        if s == '':
            continue
        parsed_entry = s.split(' ')[0]
        if not parsed_entry.isdigit():
            parsed_mapping_names = parsed_entry.split('-')
            # print(parsed_mapping_names)
            source = parsed_mapping_names[0]
            target = parsed_mapping_names[2]
            name_dictionary[source] = target
            current_target = target
            mapping_dictionary[target] = []
        else:
            parsed_mapping_values = lmap(lambda x: int(x), s.split(' '))
            mapping_dictionary[current_target].append(parsed_mapping_values)

    # print(name_dictionary)
    # print(mapping_dictionary)

    locations = []
    current_key = 'seed'
    
    # print(seed_array)
    for seed in seed_array:
        # print(seed)
        current_map_value = seed
        while (current_key in name_dictionary):
            target = name_dictionary[current_key]
            current_map_value = calculate_target_mapping(current_map_value, mapping_dictionary[target])
            current_key = target
        locations.append(current_map_value)
        current_key = 'seed'
    return min(locations)

# solution functions
def part_a(input):
    seed_array = construct_seed_array(input,'a')
    return solution_impl(input, seed_array)    

def part_b(input):
    seed_array = construct_seed_array(input, 'a')
    # return solution_impl(seed_array)  
    mapping_dictionary = {}
    name_dictionary = {}
    # index into dictionary based on source string
    # determine mapping value
    # find next dictionary based on target string
    current_target = ''
    print(input)
    for index in range(2, len(input)):
        s = input[index]
        # print(s)
        if s == '':
            continue
        parsed_entry = s.split(' ')[0]
        if not parsed_entry.isdigit():
            parsed_mapping_names = parsed_entry.split('-')
            # print(parsed_mapping_names)
            source = parsed_mapping_names[0]
            target = parsed_mapping_names[2]
            name_dictionary[source] = target
            current_target = target
            mapping_dictionary[target] = []
        else:
            parsed_mapping_values = lmap(lambda x: int(x), s.split(' '))
            mapping_dictionary[current_target].append(parsed_mapping_values)
    
    current_key = 'seed'
    
    # TODO: this is a brute force approach and it needs to be optimized
    lowest = None
    for index in range(0, len(seed_array), 2):
        for seed in range(seed_array[index], seed_array[index] + seed_array[index + 1], 1):
            current_map_value = seed
            while (current_key in name_dictionary):
                target = name_dictionary[current_key]
                current_map_value = calculate_target_mapping(current_map_value, mapping_dictionary[target])
                current_key = target
            # locations.append(current_map_value)
            if lowest is None or current_map_value < lowest:
                print(current_map_value)
                lowest = current_map_value
        
            current_key = 'seed'
    return lowest

input_data = read_aoc_data(5, 2023)
start_time = time.perf_counter()
print(part_a(input_data))
end_time = time.perf_counter()
print(f"part_a perf: {(end_time - start_time):02f}")
start_time = time.perf_counter()
print(part_b(input_data))
end_time = time.perf_counter()
print(f"part_a perf: {(end_time - start_time):02f}")