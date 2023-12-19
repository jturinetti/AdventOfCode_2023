from aocd import get_data   # to retrieve puzzle inputs

# file parsing utilities
def read_input_file(filename):
    input_file = open(filename, 'r')
    return input_file.readlines()

def parse_multi_line_input(input: str):
    return list(filter(str.strip, input.splitlines()))

# grid utilities
def generate_empty_grid(row_count, col_count, char):
    return [[char for x in range(col_count)] for y in range(row_count)]

def flatten_grid_rows(grid):
    return [''.join(row) for row in grid]

def grid_string(grid):
    return '\n' + '\n'.join([''.join([item for item in row]) for row in grid])

def up_one(coordinate):
    return (coordinate[0] - 1, coordinate[1])

def down_one(coordindate):
    return (coordindate[0] + 1, coordindate[1])

def left_one(coordinate):
    return (coordinate[0], coordinate[1] - 1)

def right_one(coordinate):
    return (coordinate[0], coordinate[1] + 1)

# wrapper to call aocd api to retrieve input for day and year
def read_aoc_data(day, year):
    problem_data = get_data(day=day, year=year)
    return problem_data.splitlines()