from aocd import get_data   # to retrieve puzzle inputs
from aocd import submit     # to submit puzzle solutions
from aocd.models import Puzzle  # object model
import re

# solution functions
def part_a(input):
    max_red = 12
    max_green = 13
    max_blue = 14
    game_id_sum = 0
    for n in range(len(input)):
        # split by colon
        game_input = input[n].split(':')
        game_id = int(game_input[0].split(' ')[1])
        
        red = re.findall('[0-9]+ red', game_input[1])
        blue = re.findall('[0-9]+ blue', game_input[1])
        green = re.findall('[0-9]+ green', game_input[1])

        red_good = all(int(x.split(' ')[0]) <= max_red for x in red)
        blue_good = all(int(x.split(' ')[0]) <= max_blue for x in blue)
        green_good = all(int(x.split(' ')[0]) <= max_green for x in green)

        if red_good and blue_good and green_good:
            game_id_sum += game_id
    return game_id_sum

def part_b(input):
    total = 0
    for n in range(len(input)):
        game_input = input[n].split(':')
        
        red = re.findall('[0-9]+ red', game_input[1])
        blue = re.findall('[0-9]+ blue', game_input[1])
        green = re.findall('[0-9]+ green', game_input[1])

        red_max = max(int(x.split(' ')[0]) for x in red)
        blue_max = max(int(x.split(' ')[0]) for x in blue)
        green_max = max(int(x.split(' ')[0]) for x in green)

        total += (red_max * blue_max * green_max)        
    return total
    

problem_data = get_data(day=2, year=2023)
split_input = problem_data.splitlines()
print(part_a(split_input))
print(part_b(split_input))