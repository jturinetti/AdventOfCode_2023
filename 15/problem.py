import time
import logging
from utils import *
from my_utils import read_aoc_data

def hash_alg(str):
    val = 0
    for c in str:
        ascii = ord(c)
        val += ascii
        val = val * 17
        val = val % 256
    return val

# solution functions
def part_a(input):    
    input_arr = input[0].split(',')
    total = 0
    for code in input_arr:
        total += hash_alg(code)
    return total

def part_b(input):
    hash_map = {}
    input_arr = input[0].split(',')
    for code in input_arr:
        box = 0
        if code[-1] == '-':
            # ends in -
            label = code[:-1]            
            box = hash_alg(label)            
            if box in hash_map:
                hash_map[box] = [x for x in hash_map[box] if x[0] != label]
        else:
            # ends in = NUMBER
            label = code[:-2]
            box = hash_alg(label)
            focal_length = code[-1]
            if box in hash_map:
                is_found = False
                for i in range(len(hash_map[box])):
                    if hash_map[box][i][0] == label:
                        is_found = True                        
                        hash_map[box] = hash_map[box][:i] + [(label, focal_length)] + hash_map[box][i+1:]
                        break
                        
                if not is_found:
                    hash_map[box].append((label, focal_length))
            else:
                hash_map[box] = []
                hash_map[box].append((label, focal_length))

    total = 0
    for k in hash_map.keys():
        for li in range(len(hash_map[k])):
            logging.debug('box {} + 1 * list index {} + 1 * focal length {} at hash_map[key][listindex]'.format(k, li, int(hash_map[k][li][1])))
            total += (k + 1) * (li + 1) * int(hash_map[k][li][1])

    return total

def execute():
    input_data = read_aoc_data(15, 2023)    # replace with correct day and year
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