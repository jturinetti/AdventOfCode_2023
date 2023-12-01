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
    total = 0
    for n in range(len(input)):
        line = input[n]       
        numbers = line.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
        print(numbers)
        assembled_number = int(numbers[0] + numbers[len(numbers) - 1])
        print(assembled_number)
        total += assembled_number                           
    return total

def part_b(input):
    total = 0
    for n in range(len(input)):
        line = input[n]
        print(line)
        # replace text numbers
        index = 0
        while index < len(line) - 2:
            if (line[index:index + 3] == 'one'):
                line = line.replace('on', '1', 1)
            elif (line[index:index + 3] == 'two'):
                line = line.replace('tw', '2', 1)
            elif (line[index:index + 5] == 'three'):
                line = line.replace('thre', '3', 1)
            elif (line[index:index + 4] == 'four'):
                line = line.replace('four', '4', 1)
            elif (line[index:index + 4] == 'five'):
                line = line.replace('fiv', '5', 1)
            elif (line[index:index + 3] == 'six'):
                line = line.replace('six', '6', 1)
            elif (line[index:index + 5] == 'seven'):
                line = line.replace('seve', '7', 1)
            elif (line[index:index + 5] == 'eight'):
                line = line.replace('eigh', '8', 1)
            elif (line[index:index + 4] == 'nine'):
                line = line.replace('nin', '9', 1)

            index += 1

        print(line)
        numbers = line.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
        assembled_number = int(numbers[0] + numbers[len(numbers) - 1])
        print(assembled_number)
        total += assembled_number
        print(total)
    return total    

problem_data = get_data(day=1, year=2023)
split_input = problem_data.splitlines()

print(part_a(split_input))
print(part_b(split_input))