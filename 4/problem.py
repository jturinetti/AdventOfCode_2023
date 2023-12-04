from aocd import get_data   # to retrieve puzzle inputs
from utils import *

# for parsing input text files if necessary
def read_input_file(filename):
    input_file = open(filename, 'r')
    return input_file.readlines()

def get_winning_numbers(card_data):
    input_data = card_data[10:]
    split_data = input_data.split('|')
    left_set = {s for s in split_data[0].split(' ') if s != ''}
    right_set = {s for s in split_data[1].split(' ') if s != ''}
    return left_set.intersection(right_set)

# solution functions
def part_a(input):
    total = 0
    for card in input:        
        winners = get_winning_numbers(card)
        if len(winners) > 0:
            total += (2 ** (len(winners) - 1))
    return total

def part_b(input):
    input_rows = len(input)
    card_counts = [1] * input_rows
    for index in range(len(input)):
        card = input[index]
        winners = get_winning_numbers(card)        
        if len(winners) > 0:
            end_index = index + len(winners)
            cur = index + 1
            while (cur <= end_index):
                card_counts[cur] += card_counts[index]
                cur += 1
    return sum(card_counts)

problem_data = get_data(day=4, year=2023)
split_input = problem_data.splitlines()

# call part_a and part_b below
print(part_a(split_input))
print(part_b(split_input))