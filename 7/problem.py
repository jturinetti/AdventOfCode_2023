import time
import logging
from utils import *
from my_utils import read_aoc_data

low_to_high_card_ranking = '23456789TJQKA'
low_to_high_card_ranking_with_jokers = 'J23456789TQKA'

def ranking_func(e):
    hand = e.split(' ')[0]
    rank = 0
    hand_breakdown = set((x, hand.count(x)) for x in hand)
    # 5 of a kind
    if any(x[1] == 5 for x in hand_breakdown):
        rank = 600000000
    # 4 of a kind
    elif any(x[1] == 4 for x in hand_breakdown):
        rank = 500000000
    else:
        # count pairs for reference
        pair_count = len(list(filter(lambda x: x[1] == 2, hand_breakdown)))
        
        if any(x[1] == 3 for x in hand_breakdown):
            # full house
            if pair_count == 1:
                rank = 400000000
            # 3 of a kind
            else:
                rank = 300000000
        # 2 pair or 1 pair?
        elif pair_count > 0:
            rank = pair_count * 100000000

    # add value based on card order for high card hands and ties
    for n in range(5):        
        rank += (14**(5 - n)) * (low_to_high_card_ranking.find(hand[n]) + 1)
    
    return rank

def ranking_func_with_jokers(e):
    hand = e.split(' ')[0]
    rank = 0
    hand_breakdown = set((x, hand.count(x)) for x in hand)
    
    joker_count = next(filter(lambda x: x[0] == 'J', hand_breakdown), ('J', 0))[1]
        
    # 5 of a kind
    if joker_count == 5 or any(x[1] + joker_count == 5 for x in hand_breakdown if x[0] != 'J'):
        rank = 600000000
    # 4 of a kind
    elif any(x[1] + joker_count == 4 for x in hand_breakdown if x[0] != 'J'):
        rank = 500000000
    else:
        # count non-joker pairs for reference
        pair_count = len(list(filter(lambda x: x[1] == 2 and x[0] != 'J', hand_breakdown)))

        if joker_count == 0:
            # normal full house / 3 of a kind check
            if any(x[1] == 3 for x in hand_breakdown):
                # native full house
                if pair_count == 1:
                    rank = 400000000
                # native 3 of a kind
                else:
                    rank = 300000000
            # 2 pair or 1 pair?
            elif pair_count > 0:
                rank = pair_count * 100000000
        else:
            # new check
            if joker_count == 2 and pair_count == 0:
                # 3 of a kind                
                rank = 300000000
            elif joker_count == 1:
                if pair_count == 2:
                    # full house with joker
                    rank = 400000000
                elif pair_count == 1:
                    # 3 of a kind
                    rank = 300000000
                else:
                    # make a pair with joker
                    rank = 100000000

    # add value based on card order for high card hands and ties
    for n in range(5):
        rank += (14**(5 - n)) * (low_to_high_card_ranking_with_jokers.find(hand[n]) + 1)

    return rank

# solution functions
def part_a(input):    
    input.sort(key=ranking_func)
    total = 0
    for n in range(len(input)):
        bid = int(input[n].split(' ')[1])
        total += (n + 1) * bid
    return total

def part_b(input):
    input.sort(key=ranking_func_with_jokers)
    total = 0    
    for n in range(len(input)):
        bid = int(input[n].split(' ')[1])
        total += (n + 1) * bid
    return total

def execute():
    input_data = read_aoc_data(7, 2023)
    start_time = time.perf_counter()
    logging.info('part_a answer: {}'.format(part_a(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_a perf: {(end_time - start_time):02f}s")
    start_time = time.perf_counter()
    logging.info('part_b answer: {}'.format(part_b(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_b perf: {(end_time - start_time):02f}s")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()