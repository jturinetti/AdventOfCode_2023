from aocd import get_data   # to retrieve puzzle inputs
import re

def add_gear_data(input, row, column, number, dictionary):
    if input[row][column] != '*':
        return
    
    key = str(row) + str(column)
    if key in dictionary:
        dictionary[key].append(number)
    else:
        dictionary[key] = [number]

def check_coordinate(input, row, col):
    return input[row][col] != '.' and not str.isdigit(input[row][col])

def check_coordinates(input, coords):
    is_found = False
    index = -1
    result = None
    while (index < len(coords) - 1 and not is_found):
        index += 1
        is_found = check_coordinate(input, coords[index][0], coords[index][1])
    
    if is_found:
        result = coords[index]
    
    return result
        
# TODO: this could be reused to get surrounding coordinates for future problems
def assemble_list_of_coordinates(input_row_index, match_start_index, match_end_index, x_boundary, y_boundary):
    column = max(0, match_start_index - 1)
    row = max(0, input_row_index - 1)
    top_coordinates = [(row, x) for x in range(column, min(match_end_index, x_boundary) + 1, 1) if input_row_index > 0]
    bottom_coordinates = [(min(y_boundary, input_row_index + 1), x) for x in range(column, min(match_end_index, x_boundary) + 1)]
    coords = top_coordinates + bottom_coordinates
    if match_start_index > 0:
        coords.append((input_row_index, column))
    if match_end_index < x_boundary:
        coords.append((input_row_index, match_end_index))
    return coords

# solution functions
def part_a(input):
    total = 0
    
    for row_index in range(len(input)):
        matches = re.finditer('[0-9]+', input[row_index])
        for match in matches:
           
            start_index = match.start()
            end_index = match.end()

            # determine surrounding coordinates to check
            coords = assemble_list_of_coordinates(row_index, start_index, end_index, len(input[row_index]) - 1, len(input) - 1)
            # check around number to see if it should be included
            scan_result = check_coordinates(input, coords)
            
            if (scan_result is not None):
                total += int(match.group(0))
            
    return total   

def part_b(input):
    gear_total = 0

    # dict will contain x/y coords of * and a list of nearby numbers
    dict = {}

    for row_index in range(len(input)):
        matches = re.finditer('[0-9]+', input[row_index])
        for match in matches:
           
            start_index = match.start()
            end_index = match.end()

            # determine surrounding coordinates to check
            coords = assemble_list_of_coordinates(row_index, start_index, end_index, len(input[row_index]) - 1, len(input) - 1)
            # check around number to see if it should be included
            scan_result = check_coordinates(input, coords)
            
            if (scan_result is not None):
                add_gear_data(input, scan_result[0], scan_result[1], match.group(0), dict)

    for key in iter(dict.keys()):
        if len(dict[key]) == 2:
            gear_total += int(dict[key][0]) * int(dict[key][1])
    
    return gear_total

problem_data = get_data(day=3, year=2023)   # change to correct day/year
split_input = problem_data.splitlines()
data_matrix = []
for n in range(len(split_input)):
    data_matrix.append(split_input[n])

print(part_a(data_matrix))
print(part_b(data_matrix))
