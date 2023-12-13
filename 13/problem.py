import time
import logging
from utils import *
import itertools
from my_utils import read_aoc_data

def check_row_equivalence(grid, left_index, right_index):
    
    if left_index < 0 or right_index == len(grid):
        return True
    
    # print('checking row {} and row {}'.format(left_index, right_index))
    if grid[left_index] == grid[right_index]:
        left_index -= 1
        right_index += 1
        return check_row_equivalence(grid, left_index, right_index)

    return False

def check_col_equivalence(grid, row_index, left_index, right_index):
    # print('{}, {}, {}'.format(row_index, left_index, right_index))
    if left_index < 0 or right_index == len(grid[0]):
        return True
    
    if row_index == len(grid):
        left_index -= 1
        right_index += 1
        row_index = 0
        return check_col_equivalence(grid, row_index, left_index, right_index)
    
    # print('checking col {} and col {} in row {}'.format(left_index, right_index, row_index))
    if grid[row_index][left_index] == grid[row_index][right_index]:
        row_index += 1
        return check_col_equivalence(grid, row_index, left_index, right_index)

    return False

def solve_grid(grid, orig):
    # look for 2 identical rows
    print('looking at rows')
    for key, group in itertools.groupby(grid, lambda x: x): 
        if len(list(group)) > 1:
            # print('comparing rows')
            # print(key)
            # print(list(group))
            for r in range(len(grid) - 1):
                if grid[r] == key and grid[r] == grid[r + 1]:
                    # row_index = r
                    if check_row_equivalence(grid, r, r + 1):
                        if orig is None or orig != ('row', r + 1):
                            print('ROW FOUND! row index {}'.format(r))
                            return ('row', r + 1)
                            # break
                    #row_index = grid.index(key)
            # print('row index: {}'.format(row_index))
            # if check_row_equivalence(grid, row_index, row_index + 1):
            #     if orig is None or orig != ('row', row_index + 1):
            #         print('ROW FOUND! row index {}'.format(row_index))
            #         return ('row', row_index + 1)

    # if no identical rows, look at columns
    print('looking at columns')
    is_found = False
    col_index = 0
    row_index = 0
    while not is_found and col_index < len(grid[0]) - 1:
        # print(grid)
        # print(len(grid[0]))
        # print('checking {} {} and {} {}'.format(row_index, col_index, row_index, col_index + 1))
        if grid[row_index][col_index] == grid[row_index][col_index + 1]:
            row_index += 1
        else:
            row_index = 0
            col_index += 1
       
        if row_index == len(grid):            
            is_found = check_col_equivalence(grid, 0, col_index, col_index + 1)
            if is_found:
                # print('you are here')
                # print(orig)
                # print(col_index + 1)
                if orig is None or orig != ('col', col_index + 1):
                    print('COLUMN FOUND! col index {}'.format(col_index + 1))
                    return ('col', col_index + 1)
                else:
                    # print('NOT FOUND!')
                    is_found = False
            row_index = 0
            col_index += 1    

    # print('SHOULD NOT HAPPEN!')
    return None

def fix_smudge(grid, row, col):
    gl = list(grid[row])
    if gl[col] == '.':
        gl[col] = '#'
    else:
        gl[col] = '.'
    ret = ''.join(gl)
    print(ret)
    return ret

# solution functions
def part_b(input):
    current_grid = []
    row_result = 0
    col_result = 0
    
    for x in range(len(input)):
        if input[x] == '':
            # call function
            # print(current_grid)
            original_mirror_loc = solve_grid(current_grid, None)
            print('current mirror spot: {}'.format(original_mirror_loc))
            result = None

            r = 0
            c = 0
            
            while result is None or result == original_mirror_loc:
                temp_grid = current_grid.copy()
                print('  smudge index {}, {}'.format(r, c))
                temp = fix_smudge(current_grid, r, c)
                # print(temp)
                temp_grid[r] = temp
                print('  orig grid: {}'.format(current_grid))
                print('  temp grid: {}'.format(temp_grid))
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
            # return
        else:
            current_grid.append(input[x])
    
    # print(current_grid)
    # result = solve_grid(current_grid, original_mirror_loc)
    # if result[0] == 'row':
    #     row_result += result[1]
    # else:
    #     col_result += result[1]

    original_mirror_loc = solve_grid(current_grid, None)
    print('current mirror spot: {}'.format(original_mirror_loc))
    result = None

    r = 0
    c = 0
    
    while result is None or result == original_mirror_loc:
        temp_grid = current_grid.copy()
        print('  smudge index {}, {}'.format(r, c))
        temp = fix_smudge(current_grid, r, c)
        # print(temp)
        temp_grid[r] = temp
        print('  orig grid: {}'.format(current_grid))
        print('  temp grid: {}'.format(temp_grid))
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
    # return

    return col_result + (100 * row_result)

def part_a(input):
    current_grid = []
    row_result = 0
    col_result = 0
    
    for x in range(len(input)):
        if input[x] == '':
            print(current_grid)
            result = solve_grid(current_grid)
            if result[0] == 'row':
                row_result += result[1]
            else:
                col_result += result[1]
            current_grid = []
        else:
            current_grid.append(input[x])
    
    # process final grid
    print(current_grid)
    result = solve_grid(current_grid)
    if result[0] == 'row':
        row_result += result[1]
    else:
        col_result += result[1]

    return col_result + (100 * row_result)

def execute():
    input_data = read_aoc_data(13, 2023)    # replace with correct day and year
    # start_time = time.perf_counter()
    # logging.info('part_a answer: {}'.format(part_a(input_data)))
    # end_time = time.perf_counter()
    # logging.info(f"part_a perf: {(end_time - start_time):02f}s")
    start_time = time.perf_counter()
    logging.info('part_b answer: {}'.format(part_b(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_b perf: {(end_time - start_time):02f}s")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()