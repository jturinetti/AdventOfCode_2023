from aocd import get_data   # to retrieve puzzle inputs

# for parsing input text files if necessary
def read_input_file(filename):
    input_file = open(filename, 'r')
    return input_file.readlines()

def read_aoc_data(day, year):
    problem_data = get_data(day, year)
    return problem_data.splitlines()