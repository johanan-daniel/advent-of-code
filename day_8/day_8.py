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

def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        raw_lines = file.read().split('\n')
        matrix = [list(line) for line in raw_lines]
            
    return matrix

matrix = parse_input_file(INPUT_FILE)
num_rows = len(matrix)
num_cols = len(matrix[0])
# print(matrix)

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

def part_1():
    antennas = find_antennas()
    
    antinodes = set()
    
    for type in antennas:
        locations = antennas[type]
        
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                dx = locations[j][1] - locations[i][1]
                dy = locations[j][0] - locations[i][0]
                
                up = (locations[i][0] - dy, locations[i][1] - dx)
                down = (locations[j][0] + dy, locations[j][1] + dx)
                # print(locations[i], locations[j], '-', end=' ')
                if in_bounds(up):
                    # print(up, end=' ')
                    antinodes.add(up)
                if in_bounds(down):
                    # print(down, end='')
                    antinodes.add(down)
                # print()
    
    return len(antinodes)

part_1_res = part_1()
print('part 1:', part_1_res)