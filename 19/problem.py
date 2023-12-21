from collections.abc import Iterable
import time
import logging
import copy
import collections
from operator import lt, gt
from itertools import *
from utils import *
from my_utils import read_aoc_data

def gen_workflows(input):
    dict = {}
    for r_index in range(len(input)):
        row = input[r_index]
        if row == '':
            return (dict, r_index + 1)
        srow = row[:-1].split('{')
        wf_name = srow[0]
        instructions = srow[1].split(',')
        dict[wf_name] = instructions    

def parse_ratings(ratings):
    rating_dict = {}
    sratings = ratings[1:-1].split(',')
    for r in sratings:
        sr = r.split('=')
        rating_dict[sr[0]] = int(sr[1])
    return rating_dict

def p1_condition(instruction, op_char, op_func, wf_dict, rating_dict, condition_func, min_max):
    # condition; parse and evaluate
    si = instruction.split(':')
    args = si[0].split(op_char)
    
    if op_func(rating_dict[args[0]], int(args[1])):
        if si[1] == 'A' or si[1] == 'R':
            return (si[1], min_max)
        else:
            return traverse_workflow(si[1], wf_dict, rating_dict, condition_func, min_max)    

def p2_condition(instruction, op_char, op_func, wf_dict, rating_dict, condition_func, min_max: dict):
    # condition; parse and evaluate
    si = instruction.split(':')
    args = si[0].split(op_char)
    
    # determine false and true conditions and branch from here
    false_cond = int(args[1])
    true_cond = -1
    true_dict = copy.deepcopy(min_max)
    false_dict = copy.deepcopy(min_max)
    if op_char == '<':
        true_cond = int(args[1]) - 1    # less than
        bounds = true_dict[args[0]][1]
        print('if {} < {}'.format(true_cond, bounds))
        if true_cond < bounds:
            true_dict[args[0]][1] = true_cond
            true_dict[args[0]].sort()
        bounds = false_dict[args[0]][0]
        print('if {} > {}'.format(false_cond, bounds))
        if false_cond > bounds:
            false_dict[args[0]][0] = false_cond
            false_dict[args[0]].sort()       
    elif op_char == '>':
        true_cond = int(args[1]) + 1    # greater than
        bounds = true_dict[args[0]][0]
        print('if {} > {}'.format(true_cond, bounds))
        if true_cond > bounds:
            true_dict[args[0]][0] = true_cond
            true_dict[args[0]].sort()
        bounds = false_dict[args[0]][1]
        print('if {} < {}'.format(false_cond, bounds))
        if false_cond < bounds:
            false_dict[args[0]][1] = false_cond
            false_dict[args[0]].sort()

    if si[1] == 'A':
        return ('A', true_dict)
    
    if si[1] == 'R':
        return ('R', false_dict)
    
    print('recursing to {}'.format(si[1]))
    true_traversal = traverse_workflow(si[1], wf_dict, rating_dict, condition_func, true_dict)
    false_traversal = traverse_workflow(si[1], wf_dict, rating_dict, condition_func, false_dict)
    
    return ('A', [true_traversal[1], false_traversal[1]])

def traverse_workflow(cur_wf, wf_dict, rating_dict, condition_func, min_max = {}):
    print('current workflow: {}'.format(cur_wf))
    instructions = wf_dict[cur_wf]
    for i in instructions:
        # accept or reject
        if i == 'A' or i == 'R':
            return (i, min_max)
        elif '<' in i:
            # condition; parse and evaluate
            ret = condition_func(i, '<', lt, wf_dict, rating_dict, condition_func, min_max)
            if ret is not None:
                return ret

        elif '>' in i:
            # condition; parse and evaluate
            ret = condition_func(i, '>', gt, wf_dict, rating_dict, condition_func, min_max)
            if ret is not None:
                return ret
        else:
            # direct link to another workflow            
            return traverse_workflow(i, wf_dict, rating_dict, condition_func, min_max)
    return ('A', min_max)

def sum_ratings(rating_dict: dict):
    s = 0
    for k in rating_dict.keys():
        s += rating_dict[k]
    return s

# solution functions
def part_a(input):
    total = 0
    (wf_dict, rating_index) = gen_workflows(input)
    for i in range(rating_index, len(input)):
        rating_dict = parse_ratings(input[i])
        result = traverse_workflow('in', wf_dict, rating_dict, p1_condition, {})
        if result[0] == 'A':
            total += sum_ratings(rating_dict)
    return total

def calculate_result(ddict: dict):
    total = 1
    for k in ddict.keys():
        total = total * (ddict[k][1] - ddict[k][0] + 1)
    return total

def calculate(l):
    total = 0    
    for ele in l:
        if isinstance(ele, list):
            total += calculate(ele)
        else:
            total += calculate_result(ele)
    return total

def part_b(input):
    total = 0
    (wf_dict, rating_index) = gen_workflows(input)    
    
    # r = traverse_workflow('in', wf_dict, rating_dict, )
    total = 0
    nums = [1, 4000]
    products = list(product(nums, repeat=4))
    # for grouping in products:
    #     grouping = products[0]
    min_max = {
        'x': [1, 4000],
        'm': [1, 4000],
        'a': [1, 4000],
        's': [1, 4000]
    }    
    
    result = traverse_workflow('in', wf_dict, {}, p2_condition, min_max)       

    if result[0] == 'A':
        print('result: {}'.format(result))
        total += calculate(result[1])
    return total
           

def execute():
    input_data = read_aoc_data(19, 2023)    # replace with correct day and year
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