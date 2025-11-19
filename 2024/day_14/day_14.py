"""
- calculate positions after 100 seconds
- add up number of robots in each quadrant & multiply together
    - need some way to separate grid into quadrants
"""

from dotenv import load_dotenv
import os, re
from collections import defaultdict

load_dotenv()
DAY = 14
BASE_PATH = (os.getenv('BASE_PATH') or "") + f"day_{DAY}/"
INPUT_FILE = BASE_PATH + f"day_{DAY}_input.txt"
EXAMPLE_FILE = BASE_PATH + f"day_{DAY}_example.txt"

POS = 0
VEL = 1
X = 0
Y = 1

def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
        pattern = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
        output = []
        
        for line in lines:
            match = pattern.match(line)
            if match:
                robot = [[int(match[1]), int(match[2])], [int(match[3]), int(match[4])]]
                output.append(robot)
        
        return output

robots = parse_input_file(INPUT_FILE)

def main(y_max, x_max, start_seconds, max_seconds, part):
    quadrants = defaultdict(int)
    x_mid = x_max // 2
    y_mid = y_max // 2
    total = 1
    
    if part == 1:
        start_seconds = max_seconds
    
    for robot in robots:
        x_pos = (robot[POS][X] + start_seconds * robot[VEL][X]) % x_max
        y_pos = (robot[POS][Y] + start_seconds * robot[VEL][Y]) % y_max
        
        if part == 1:
            if (x_pos == x_mid or y_pos == y_mid):
                continue
            quadrants[(x_pos // (x_mid + 1), y_pos // (y_mid + 1))] += 1
        else:
            robot[POS][X] = x_pos
            robot[POS][Y] = y_pos
    
    if part == 1:
        for value in quadrants.values():
            total *= value
        return total

    
    with open(BASE_PATH + 'output.txt', 'a') as file:
        for second in range(start_seconds, max_seconds):
            matrix = [['.'] * x_max for _ in range(y_max)]
            
            for robot in robots:
                x_pos = (robot[POS][X] + robot[VEL][X]) % x_max
                y_pos = (robot[POS][Y] + robot[VEL][Y]) % y_max
                
                robot[POS][X] = x_pos
                robot[POS][Y] = y_pos
                
                if second == max_seconds - 1:
                    if (x_pos == x_mid or y_pos == y_mid):
                        continue
                    quadrants[(x_pos // (x_mid + 1), y_pos // (y_mid + 1))] += 1
                
                # print(x_pos, y_pos, len(matrix), len(matrix[0]))
                matrix[y_pos][x_pos] = '0'
            
            file.write(f'{second + 1} seconds\n')
            for row in matrix:
                file.write(''.join(row) + '\n')
            file.write('\n\n')
    

part_1_res = main(103, 101, 0, 100, part = 1)
# part_1_res = main(7, 11, 0, 100, part = 1)
print('part 1:', part_1_res)

part_2_res = main(103, 101, 0, 100, part = 2)