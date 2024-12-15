"""
- dfs over each unvisited cell to find region
- do weird math to find perimeter?
    - on each dfs call, save outputs of calls on neighbors
        - must somehow return if cell was part of region, and how many neighbors of same region

init visited
loop over each cell:
    if not visited:
        start dfs
"""

from dotenv import load_dotenv
import os

load_dotenv()
DAY = 12
BASE_PATH = (os.getenv('BASE_PATH') or "") + f"day_{DAY}/"
INPUT_FILE = BASE_PATH + f"day_{DAY}_input.txt"
EXAMPLE_FILE_1 = BASE_PATH + f"day_{DAY}_example_1.txt"
EXAMPLE_FILE_2 = BASE_PATH + f"day_{DAY}_example_2.txt"
EXAMPLE_FILE_3 = BASE_PATH + f"day_{DAY}_example_3.txt"

def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
        matrix = [list(line) for line in lines]
        return matrix

matrix = parse_input_file(INPUT_FILE)
num_rows = len(matrix)
num_cols = len(matrix[0])
# print(matrix)

def main():
    visited = set()
    iterations = 0
    
    def dfs(row, col, region, measurements):
        nonlocal iterations
        iterations += 1
        if iterations == 1000:
            return False
        
        if (row < 0 or col < 0 or row >= num_rows or col >= num_cols
            or matrix[row][col] != region):
            return False
        
        if ((row, col) in visited):
            return True
        
        visited.add((row, col))
        
        up = dfs(row - 1, col, region, measurements)
        down = dfs(row + 1, col, region, measurements)
        left = dfs(row, col - 1, region, measurements)
        right = dfs(row, col + 1, region, measurements)
        
        measurements[0] += 1
        measurements[1] += 4 - (up + down + left + right)
        return True
    
    price = 0
    
    for row in range(num_rows):
        for col in range(num_cols):
            if (row, col) not in visited:
                measurements = [0,0]
                dfs(row, col, matrix[row][col], measurements)
                price += measurements[0] * measurements[1]
                # print(matrix[row][col], measurements)
    
    return price

part_1_res = main()
print('part 1:', part_1_res)

# part_2_res = main()
# print('part 2:', part_2_res)