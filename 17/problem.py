import time
import logging
from utils import *
from my_utils import *
from queue import PriorityQueue

def is_valid_node(coord, row_boundary, col_boundary):
    return coord[0] >= 0 and coord[1] >= 0 and coord[0] < row_boundary and coord[1] < col_boundary

# def determine_adj_nodes(input, cur_coord, direction, steps_taken):
def determine_adj_nodes(cur_coord, row_boundary, col_boundary, direction, steps_taken):
    result = []
    dirs = ['R', 'D', 'L', 'U']
    changes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
    cur_dir_index = dirs.index(direction)

    # turn left
    lindex = cur_dir_index - 1
    if lindex < 0: 
        lindex = 3
    new_coord = (cur_coord[0] + changes[lindex][0], cur_coord[1] + changes[lindex][1])
    if is_valid_node(new_coord, row_boundary, col_boundary):
        result.append((new_coord[0], new_coord[1], 1, dirs[lindex]))

    # turn right
    rindex = cur_dir_index + 1
    if rindex > 3:
        rindex = 0
    new_coord = (cur_coord[0] + changes[rindex][0], cur_coord[1] + changes[rindex][1])
    if is_valid_node(new_coord, row_boundary, col_boundary):
        result.append((new_coord[0], new_coord[1], 1, dirs[rindex]))
        
    if steps_taken < 3:
        # can still move forward another step
        new_coord = (cur_coord[0] + changes[cur_dir_index][0], cur_coord[1] + changes[cur_dir_index][1])
        if is_valid_node(new_coord, row_boundary, col_boundary):
            result.append((new_coord[0], new_coord[1], steps_taken + 1, dirs[cur_dir_index]))        

    return result

def calculate_path_changes(input, diff_grid):
    # initial values
    direction = 'R'
    steps_taken = 0
    
    # root node; we start at (0, 0)
    diff_grid[0][0] = 0

    # visited nodes
    seen_nodes = set()
    # remaining nodes
    remaining_nodes = set()

    # priority queue
    pq = PriorityQueue()

    # initialize with root node to start at
    # node structure for set and pq: (weight, (x, y, steps taken, direction))
    pq.put((0, (0, 0, steps_taken, direction)))

    while True:
        # exit condition
        if pq.empty():
            break

        # get next min weight node
        current_node = pq.get()
        logging.debug('current_node: {}'.format(current_node))

        # unpack
        current_node_weight = current_node[0]
        current_node_data = current_node[1]
        current_node_x = current_node_data[0]
        current_node_y = current_node_data[1]
        steps_taken = current_node_data[2]
        direction = current_node_data[3]

        if current_node_data in seen_nodes:
            logging.debug('SKIPPING!  we have seen {}'.format(current_node_data))
            continue

        # return structure: [(x, y, steps taken, direction)]
        adj_nodes = determine_adj_nodes((current_node_x, current_node_y), len(input), len(input[0]), direction, steps_taken)
        logging.debug('adj nodes: {}'.format(adj_nodes))

        for n in adj_nodes:
            logging.debug('adj node: {}'.format(n))
            adj_node_x = n[0]
            adj_node_y = n[1]
            
            adj_node_weight = int(input[adj_node_x][adj_node_y])
            accum_weight = current_node_weight + adj_node_weight
            existing_distance = diff_grid[adj_node_x][adj_node_y]

            if existing_distance is None:
                logging.debug('diff is None; setting {} at {},{}'.format(accum_weight, adj_node_x, adj_node_y))
                diff_grid[adj_node_x][adj_node_y] = accum_weight
            elif accum_weight < existing_distance:
                logging.debug('{} is < existing distance of {}; overwriting diff at {},{}'.format(accum_weight, existing_distance, adj_node_x, adj_node_y))
                diff_grid[adj_node_x][adj_node_y] = accum_weight
            
            if n not in remaining_nodes:
                pq.put((accum_weight, n))
                remaining_nodes.add(n)
                
            logging.debug('priority queue state: {}'.format(pq.queue))

        # add current node to seen nodes set
        seen_nodes.add(current_node_data)    

# solution functions
def part_a(input):
    diff_grid = generate_empty_grid(len(input), len(input[0]), None)
    calculate_path_changes(input, diff_grid)
    logging.debug(grid_string(diff_grid))
    return diff_grid[len(diff_grid) - 1][len(diff_grid[0]) - 1]

def part_b(input):
    # TODO
    return

def execute():
    input_data = read_aoc_data(17, 2023)
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