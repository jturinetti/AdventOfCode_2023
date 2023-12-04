from aocd import get_data   # to retrieve puzzle inputs
import re

def add_gear_data(symbol, x, y, number, dictionary):
    if symbol != '*':
        return
    
    key = str(x) + str(y)
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
    gear_total = 0
    test_total = 0
    
    # dict will contain x/y coords of * and a list of nearby numbers
    dict = {}

    for row_index in range(len(input)):
        matches = re.finditer('[0-9]+', input[row_index])
        for match in matches:
           
            start_index = match.start()
            end_index = match.end()

            is_found = False
            column = max(0, start_index - 1)
            row = max(0, row_index - 1)

            # TESTING
            coords = assemble_list_of_coordinates(row_index, start_index, end_index, len(input[row_index]) - 1, len(input) - 1)
            print(coords)

            scan_result = check_coordinates(input, coords)
            if (scan_result is not None):
                test_total += int(match.group(0))

            # check around number to see if it should be included
            # check above
            if row_index > 0:
                current_col = column
                while current_col <= min(end_index, len(input[row_index]) - 1) and not is_found:
                    print("checking (" + str(row) + " " + str(current_col) + ")")
                    if input[row][current_col] != '.' and not str.isdigit(input[row][current_col]):
                        # include it!
                        print("found " + input[row][current_col] + " above")
                        is_found = True
                        add_gear_data(input[row][current_col], row, current_col, match.group(0), dict)
                    else:
                        current_col += 1

            # check left
            if start_index > 0 and not is_found:
                print("checking left (" + str(row_index) + ", " + str(column) + "): " + str(input[row_index][column]))
                if input[row_index][column] != '.' and not str.isdigit(input[row_index][column]):
                        # include it!
                        print("found " + input[row_index][column] + " left")
                        is_found = True
                        add_gear_data(input[row_index][column], row_index, column, match.group(0), dict)


            # check below
            if row_index < len(input) - 1 and not is_found:
                current_col = column
                row = min(len(input) - 1, row_index + 1)
                while current_col <= min(end_index, len(input[row_index]) - 1) and not is_found:
                    print("checking (" + str(row) + " " + str(current_col) + ")")
                    # check it
                    if input[row][current_col] != '.' and not str.isdigit(input[row][current_col]):
                        # include it!
                        # print("found " + input[y][current] + " below")
                        is_found = True
                        add_gear_data(input[row][current_col], row, current_col, match.group(0), dict)

                    else:
                        current_col += 1

            # check right
            if end_index < len(input[row_index]) - 1 and not is_found:
                column = end_index
                print("checking right (" + str(row_index) + ", " + str(column) + "): " + str(input[row_index][column]))
                if input[row_index][column] != '.' and not str.isdigit(input[row_index][column]):
                    # include it!
                    # print("found " + input[row_index][x] + " right")
                    is_found = True
                    add_gear_data(input[row_index][column], row_index, column, match.group(0), dict)

 
            if is_found:
                # print('including ' + match.group(0))
                total += int(match.group(0))

            

    for key in iter(dict.keys()):
        if len(dict[key]) == 2:
            gear_total += int(dict[key][0]) * int(dict[key][1])
    print(gear_total)
    print('returning total...new total is:')
    print(test_total)
    return total

def part_b(input):
    # TODO
    return

problem_data = get_data(day=3, year=2023)   # change to correct day/year
split_input = problem_data.splitlines()
data_matrix = []
for n in range(len(split_input)):
    data_matrix.append(split_input[n])

print(part_a(data_matrix))
