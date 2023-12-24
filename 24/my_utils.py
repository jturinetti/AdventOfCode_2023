import logging
import itertools
from aocd import get_data   # to retrieve puzzle inputs
from shapely.geometry import Point
from shapely.geometry import Polygon

# file parsing utilities
def read_input_file(filename):
    input_file = open(filename, 'r')
    return input_file.readlines()

def parse_multi_line_input(input: str):
    return list(filter(str.strip, input.splitlines()))

# grid utilities
def generate_empty_grid(row_count, col_count, char):
    return [[char for x in range(col_count)] for y in range(row_count)]

# ['123','456'] -> [[1,2,3],[4,5,6]]
def expand_grid_rows(grid):
    return [list(row) for row in grid]

# [[1,2,3],[4,5,6]] -> ['123','456']
def flatten_grid_rows(grid):
    return [''.join(row) for row in grid]

def grid_string(grid):
    return '\n' + '\n'.join([''.join([item for item in row]) for row in grid])

def up_one(coordinate):
    return (max(coordinate[0] - 1, 0), coordinate[1])

def down_one(coordindate, row_count):
    return (min(coordindate[0] + 1, row_count - 1), coordindate[1])

def left_one(coordinate):
    return (coordinate[0], max(coordinate[1] - 1, 0))

def right_one(coordinate, col_count):
    return (coordinate[0], min(coordinate[1] + 1, col_count - 1))

# shape utilities
# determines corner coordinates around an arbitrary shape from a list of coordinates
# TODO: use existing function in shapely or pandas?
def draw_bounding_box(path):
    min_x = None
    min_y = None
    max_x = None
    max_y = None
    for point in path:
        if min_x is None or point[0] < min_x:
            min_x = point[0]
        if min_y is None or point[1] < min_y:
            min_y = point[1]
        if max_x is None or point[0] > max_x:
            max_x = point[0]
        if max_y is None or point[1] > max_y:
            max_y = point[1]
    bounding_box_points = [(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)]
    logging.debug(bounding_box_points)
    return bounding_box_points

# determines number of coordinates within an arbitrary enclosed shape defined by list of coordinates by iterating and evaluating each coordinate one at a time
def calculate_inner_area(path):
    polygon = Polygon(path)
    bounding_box = draw_bounding_box(path)
    area = 0

    for r in range(min(bounding_box, key=lambda x: x[0])[0], max(bounding_box, key=lambda x: x[0])[0]):
        for c in range(min(bounding_box, key=lambda x: x[1])[1], max(bounding_box, key=lambda x: x[1])[1]):
            if (r, c) in path:
                continue

            point = Point(r, c)
            if point.within(polygon):
                area += 1
    return area

# shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
def shoelace(path):
  area = 0
  for (x0, y0), (x1, y1) in itertools.pairwise(path):
    area += (x0 * y1) - (y0 * x1)
  return area / 2.0

# pick's thereom https://en.wikipedia.org/wiki/Pick's_theorem
# returns i + b from equation
def picks(path, perimeter):
  return shoelace(path) + (perimeter / 2.0) + 1

# wrapper to call aocd api to retrieve input for day and year
def read_aoc_data(day, year):
    problem_data = get_data(day=day, year=year)
    return problem_data.splitlines()