from aocd import get_data   # to retrieve puzzle inputs
import re

# for parsing input text files if necessary
def read_input_file(filename):
    input_file = open(filename, 'r')
    return input_file.readlines()

def check_if_valid(matrix, x, y):
    return

def check_range(matrix, start_index, end_index):
    return

def add_gear_data(symbol, x, y, number, dictionary):
    if symbol != '*':
        return
    
    key = str(x) + str(y)
    if key in dictionary:
        dictionary[key].append(number)
    else:
        dictionary[key] = [number]


# solution functions
def part_a(input):
    total = 0
    gear_total = 0
    
    # dict will contain x/y coords of * and a list of nearby numbers
    dict = {}

    for row_index in range(len(input)):
        matches = re.finditer('[0-9]+', input[row_index])
        # print(matches)
        for match in matches:
            print(match)
            print(match.group(0))
            start_index = match.start()
            end_index = match.end()

            is_found = False
            x = max(0, start_index - 1)
            y = max(0, row_index - 1)

            # check around number to see if it should be included
            # check above
            if row_index > 0:                
                current = x
                while current <= min(end_index, len(input[row_index]) - 1) and not is_found:
                    print("checking (" + str(current) + " " + str(y) + ")")
                    # check it
                    if input[y][current] != '.' and not str.isdigit(input[y][current]):
                        # include it!
                        print("found " + input[y][current] + " above")
                        is_found = True
                        add_gear_data(input[y][current], y, current, match.group(0), dict)
                    else:
                        current += 1

            # check left
            if start_index > 0 and not is_found:
                print("checking left")
                if input[row_index][x] != '.' and not str.isdigit(input[row_index][x]):
                        # include it!
                        print("found " + input[row_index][x] + " left")
                        is_found = True
                        add_gear_data(input[row_index][x], row_index, x, match.group(0), dict)


            # check below
            if row_index < len(input) - 1 and not is_found:
                current = x
                y = min(len(input) - 1, row_index + 1)
                while current <= min(end_index, len(input[row_index]) - 1) and not is_found:
                    print("checking (" + str(current) + " " + str(y) + ")")
                    # check it
                    if input[y][current] != '.' and not str.isdigit(input[y][current]):
                        # include it!
                        print("found " + input[y][current] + " below")
                        is_found = True
                        add_gear_data(input[y][current], y, current, match.group(0), dict)

                    else:
                        current += 1

            # check right
            if end_index < len(input[row_index]) - 1 and not is_found:
                x = end_index
                print("checking right (" + str(row_index) + ", " + str(x) + "): " + str(input[row_index][x]))
                if input[row_index][x] != '.' and not str.isdigit(input[row_index][x]):
                    # include it!
                    print("found " + input[row_index][x] + " right")
                    is_found = True
                    add_gear_data(input[row_index][x], row_index, x, match.group(0), dict)

 
            if is_found:
                print('including ' + match.group(0))
                total += int(match.group(0))

            

    print(dict)
   

    for key in iter(dict.keys()):
        if len(dict[key]) == 2:
            gear_total += int(dict[key][0]) * int(dict[key][1])
    print(gear_total)
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
