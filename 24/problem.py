import time
import logging
from utils import *
from my_utils import read_aoc_data

def parse(row):
    sr = row.split(' @ ')
    coord_arr = sr[0].split(', ')
    coord = int(coord_arr[0]), int(coord_arr[1]), int(coord_arr[2])
    slope_arr = sr[1].split(', ')
    slope = int(slope_arr[0]), int(slope_arr[1]), int(slope_arr[2])
    return (coord, slope)

# solution functions
def part_a(input, bounds_min = 200000000000000, bounds_max = 400000000000000):
    counter = 0
    for p1_index in range(len(input)):
        logging.debug('OUTER LOOP INCREMENT ({} of {})'.format(p1_index + 1, len(input)))
        for p2_index in range(p1_index + 1, len(input)):
            (p1_coord, p1_slope_data) = parse(input[p1_index])
            (p2_coord, p2_slope_data) = parse(input[p2_index])
            p1_slope = p1_slope_data[1] / p1_slope_data[0]
            p2_slope = p2_slope_data[1] / p2_slope_data[0]

            # if equal, they are parallel or they coincide
            if p1_slope == p2_slope:
                logging.debug('  SLOPES EQUAL; SKIPPING')
                continue

            logging.debug('p1 coord: {}'.format(p1_coord))
            logging.debug('p1 slope: {}'.format(p1_slope))
            logging.debug('p2 coord: {}'.format(p2_coord))
            logging.debug('p2 slope: {}'.format(p2_slope))

            l1_y_int = p1_coord[1] - (p1_slope * p1_coord[0])
            l2_y_int = p2_coord[1] - (p2_slope * p2_coord[0])
            int_x = (l2_y_int - l1_y_int) / (p1_slope - p2_slope)
            int_y = (int_x * p1_slope) + l1_y_int
            
            logging.debug('  int_x: {}'.format(int_x))
            logging.debug('  int_y: {}'.format(int_y))
            
            if (int_x >= bounds_min and int_y >= bounds_min and int_x <= bounds_max and int_y <= bounds_max):
                if (p1_slope_data[0] < 0 and int_x > p1_coord[0]) or (p1_slope_data[0] > 0 and int_x < p1_coord[0]):
                    logging.debug('PAST X P1')
                    continue
                if (p1_slope_data[1] < 0 and int_y > p1_coord[1]) or (p1_slope_data[1] > 0 and int_y < p1_coord[1]):
                    logging.debug('PAST Y P1')
                    continue
                if (p2_slope_data[0] < 0 and int_x > p2_coord[0]) or (p2_slope_data[0] > 0 and int_x < p2_coord[0]):
                    logging.debug('PAST X P2')
                    continue
                if (p2_slope_data[1] < 0 and int_y > p2_coord[1]) or (p2_slope_data[1] > 0 and int_y < p2_coord[1]):
                    logging.debug('PAST Y P2')
                    continue
                    
                logging.debug('   WITHIN BOUNDS!')
                counter += 1
            else:
                logging.debug('   NOT WITHIN BOUNDS.')
            
    return counter

def part_b(input):
    # TODO
    return

def execute():
    input_data = read_aoc_data(24, 2023)
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