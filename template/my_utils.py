from aocd import get_data   # to retrieve puzzle inputs

# file parsing utilities
def read_input_file(filename):
    input_file = open(filename, 'r')
    return input_file.readlines()

def parse_multi_line_input(input: str):
    return list(filter(str.strip, input.splitlines()))

# wrapper to call aocd api to retrieve input for day and year
def read_aoc_data(day, year):
    problem_data = get_data(day=day, year=year)
    return problem_data.splitlines()