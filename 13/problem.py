import time
import logging
from utils import *
import itertools
from my_utils import read_aoc_data

def check_row_equivalence(grid, left_index, right_index):    
    if left_index < 0 or right_index == len(grid):
        return True
    
    if grid[left_index] == grid[right_index]:
        left_index -= 1
        right_index += 1
        return check_row_equivalence(grid, left_index, right_index)

    return False

def check_col_equivalence(grid, row_index, left_index, right_index):
    if left_index < 0 or right_index == len(grid[0]):
        return True
    
    if row_index == len(grid):
        left_index -= 1
        right_index += 1
        row_index = 0
        return check_col_equivalence(grid, row_index, left_index, right_index)
    
    if grid[row_index][left_index] == grid[row_index][right_index]:
        row_index += 1
        return check_col_equivalence(grid, row_index, left_index, right_index)

    return False

def solve_grid(grid, orig):
    # look for 2 identical rows
    logging.debug('looking at rows')
    for key, group in itertools.groupby(grid, lambda x: x): 
        if len(list(group)) > 1:
            for r in range(len(grid) - 1):
                if grid[r] == key and grid[r] == grid[r + 1]:
                    if check_row_equivalence(grid, r, r + 1):
                        if orig is None or orig != ('row', r + 1):
                            logging.debug('ROW FOUND! row index {}'.format(r))
                            return ('row', r + 1)
                          
    # if no identical rows, look at columns
    logging.debug('looking at columns')
    is_found = False
    col_index = 0
    row_index = 0
    while not is_found and col_index < len(grid[0]) - 1:
        if grid[row_index][col_index] == grid[row_index][col_index + 1]:
            row_index += 1
        else:
            row_index = 0
            col_index += 1
       
        if row_index == len(grid):            
            is_found = check_col_equivalence(grid, 0, col_index, col_index + 1)
            if is_found:
                if orig is None or orig != ('col', col_index + 1):
                    logging.debug('COLUMN FOUND! col index {}'.format(col_index + 1))
                    return ('col', col_index + 1)
                else:
                    is_found = False
            row_index = 0
            col_index += 1    

    return None

def fix_smudge(grid, row, col):
    gl = list(grid[row])
    if gl[col] == '.':
        gl[col] = '#'
    else:
        gl[col] = '.'
    ret = ''.join(gl)
    logging.debug(ret)
    return ret

# solution functions
def part_a(input):
    current_grid = []
    row_result = 0
    col_result = 0
    
    for x in range(len(input)):
        if input[x] == '':
            result = solve_grid(current_grid, None)
            if result[0] == 'row':
                row_result += result[1]
            else:
                col_result += result[1]
            current_grid = []
        else:
            current_grid.append(input[x])
    
    # process final grid
    result = solve_grid(current_grid, None)
    if result[0] == 'row':
        row_result += result[1]
    else:
        col_result += result[1]

    return col_result + (100 * row_result)

def part_b(input):
    current_grid = []
    row_result = 0
    col_result = 0
    
    for x in range(len(input)):
        if input[x] == '':
            original_mirror_loc = solve_grid(current_grid, None)
            logging.debug('current mirror spot: {}'.format(original_mirror_loc))
            result = None

            r = 0
            c = 0
            
            while result is None or result == original_mirror_loc:
                temp_grid = current_grid.copy()
                logging.debug('  smudge index {}, {}'.format(r, c))
                temp = fix_smudge(current_grid, r, c)
                temp_grid[r] = temp
                logging.debug('  orig grid: {}'.format(current_grid))
                logging.debug('  temp grid: {}'.format(temp_grid))
                result = solve_grid(temp_grid, original_mirror_loc)
                c += 1
                if c == len(temp_grid[0]):
                    r += 1
                    c = 0
            if result[0] == 'row':
                row_result += result[1]
            else:
                col_result += result[1]
            current_grid = []
        else:
            current_grid.append(input[x])
    
    original_mirror_loc = solve_grid(current_grid, None)
    logging.debug('current mirror spot: {}'.format(original_mirror_loc))
    result = None

    r = 0
    c = 0
    
    while result is None or result == original_mirror_loc:
        temp_grid = current_grid.copy()
        logging.debug('  smudge index {}, {}'.format(r, c))
        temp = fix_smudge(current_grid, r, c)
        temp_grid[r] = temp
        logging.debug('  orig grid: {}'.format(current_grid))
        logging.debug('  temp grid: {}'.format(temp_grid))
        result = solve_grid(temp_grid, original_mirror_loc)
        c += 1
        if c == len(temp_grid[0]):
            r += 1
            c = 0
    if result[0] == 'row':
        row_result += result[1]
    else:
        col_result += result[1]
    current_grid = []

    return col_result + (100 * row_result)

def execute():
    input_data = read_aoc_data(13, 2023)
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