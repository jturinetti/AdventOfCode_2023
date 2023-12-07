import time
import logging
from utils import *
from my_utils import read_aoc_data

low_to_high_card_ranking = '23456789TJQKA'
low_to_high_card_ranking_with_jokers = 'J23456789TQKA'

# rank seeds
FIVE_OF_A_KIND_RANK = 600000000
FOUR_OF_A_KIND_RANK = 500000000
FULL_HOUSE_RANK = 400000000
THREE_OF_A_KIND_RANK = 300000000
PAIRS_RANK = 100000000

def rank_hand(hand, joker_count, card_ranking_map):
    rank = 0
    hand_breakdown = set((x, hand.count(x)) for x in hand)
    # 5 of a kind
    if joker_count == 5 or any(x[1] + joker_count == 5 for x in hand_breakdown if joker_count == 0 or x[0] != 'J'):
        rank = FIVE_OF_A_KIND_RANK
    # 4 of a kind
    elif any(x[1] + joker_count == 4 for x in hand_breakdown if joker_count == 0 or x[0] != 'J'):
        rank = FOUR_OF_A_KIND_RANK
    else:
        # count pairs for reference
        pair_count = len(list(filter(lambda x: x[1] == 2 and (joker_count == 0 or x[0] != 'J'), hand_breakdown)))

        # cannot have more than 2 jokers at this point; we would have hit 4 or 5 of a kind blocks above
        if joker_count == 2:
            rank = THREE_OF_A_KIND_RANK
        elif joker_count == 1:
            if pair_count == 2:
                rank = FULL_HOUSE_RANK
            elif pair_count == 1:
                rank = THREE_OF_A_KIND_RANK
            else:
                rank = PAIRS_RANK
        elif joker_count == 0:
            # no jokers, standard checks
            if any(x[1] == 3 for x in hand_breakdown):
                if pair_count == 1:
                    rank = FULL_HOUSE_RANK
                else:
                    rank = THREE_OF_A_KIND_RANK
            elif pair_count > 0:
                rank = pair_count * PAIRS_RANK        

    # add value based on card order for high card hands and ties
    for n in range(5):
        rank += (14**(5 - n)) * (card_ranking_map.find(hand[n]) + 1)

    return rank

def ranking_func(e):
    hand = e.split(' ')[0]
    return rank_hand(hand, 0, low_to_high_card_ranking)

def ranking_func_with_jokers(e):
    hand = e.split(' ')[0]
    joker_count = hand.count('J')
   
    return rank_hand(hand, joker_count, low_to_high_card_ranking_with_jokers)

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