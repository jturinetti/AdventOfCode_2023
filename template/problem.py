# TEMPLATE
from aocd import get_data   # to retrieve puzzle inputs
from aocd import submit     # to submit puzzle solutions
from aocd.models import Puzzle  # object model

# retrieve data
# example:
# get_data(day=X, year=Y)

# submit answer
# examples:
# submit(my_answer, part="a", day=25, year=2017)
# submit(my_answer) - part a or b will be inferred

# models
# puzzle = Puzzle(year=2017, day=20)
# >>> puzzle
# <Puzzle(2017, 20) at 0x107322978 - Particle Swarm>
# >>> puzzle.input_data

# for parsing input text files if necessary
def read_input_file(filename):
    input_file = open(filename, 'r')
    return input_file.readlines()

# solution functions
def part_a(input):
    # TODO
    return

def part_b(input):
    # TODO
    return