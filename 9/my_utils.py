from aocd import get_data   # to retrieve puzzle inputs

# for parsing input text files if necessary
def read_input_file(filename):
    input_file = open(filename, 'r')
    return input_file.readlines()

# wrapper to call aocd api to retrieve input for day and year
def read_aoc_data(day, year):
    problem_data = get_data(day=day, year=year)
    return problem_data.splitlines()