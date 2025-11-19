"""
- find antennas (loop and save coords but group by type)
- loop over each pair:
    - get direction and distance (use euclidean by subtracting rows and cols?)
    - make locations in same direction and distance for each point:
        - if within bounds, add to set
- return length of set
"""

from dotenv import load_dotenv
import os
from collections import defaultdict

load_dotenv()
DAY = 8
BASE_PATH = (os.getenv('BASE_PATH') or "") + f"day_{DAY}/"
INPUT_FILE = BASE_PATH + f"day_{DAY}_input.txt"
EXAMPLE_FILE = BASE_PATH + f"day_{DAY}_example.txt"
EXAMPLE_FILE_2 = BASE_PATH + f"day_{DAY}_example_2.txt"
EXAMPLE_FILE_3 = BASE_PATH + f"day_{DAY}_example_3.txt"

def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        raw_lines = file.read().split('\n')
        matrix = [list(line) for line in raw_lines]
            
    return matrix

matrix = parse_input_file(INPUT_FILE)
num_rows = len(matrix)
num_cols = len(matrix[0])

def find_antennas():
    antennas = defaultdict(list)
    
    for row in range(num_rows):
        for col in range(num_cols):
            point = matrix[row][col]
            if point != '.':
                antennas[point].append((row, col))
    
    return antennas

def in_bounds(coord):
    return coord[0] >= 0 and coord[0] < num_rows and coord[1] >= 0 and coord[1] < num_cols

def main(part: int):
    antennas = find_antennas()
    antinodes = set()
    
    for type in antennas:
        locations = antennas[type]
        
        # loops over each pair
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                coord1 = locations[i]
                coord2 = locations[j]
                
                # coord[0] == y, coord[1] == x
                dx = coord2[1] - coord1[1]
                dy = coord2[0] - coord1[0]
                
                if part == 1:
                    # skip existing antenna
                    up = (coord1[0] - dy, coord1[1] - dx)
                    down = (coord2[0] + dy, coord2[1] + dx)
                elif part == 2:
                    # start at opposite antenna to include them
                    down = (coord1[0] + dy, coord1[1] + dx)
                    up = (coord2[0] - dy, coord2[1] - dx)
                
                while in_bounds(up):
                    antinodes.add(up)
                    up = (up[0] - dy, up[1] - dx)
                    if part == 1:
                        # only go one distance out
                        break
                while in_bounds(down):
                    antinodes.add(down)
                    down = (down[0] + dy, down[1] + dx)
                    if part == 1:
                        # only go one distance out
                        break
    
    return len(antinodes)

part_1_res = main(part=1)
print('part 1:', part_1_res)

part_2_res = main(part=2)
print('part 2:', part_2_res)