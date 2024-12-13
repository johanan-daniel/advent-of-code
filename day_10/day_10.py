"""
Given: integer matrix
Return: integer for sum of scores of all trailheads, a score being how many 9s can be reached on a valid trail from each trailhead

init hashmap of sets
- each item in hashmap is the coord for a trailhead
- each value is a set to store the coords of all 9s reachable from each
init count

dfs(row, col, trailhead, last_val):
    if out of bounds or not 1 + last_val:
        return
    
    if 9:
        if not in set at hashmap[trailhead]:
            increment count
            add to set at hashmap[trailhead]
        return
    
    dfs on neighbors (with current as last_val)

loop over each cell:
    if trailhead:
        start dfs with row, col, trailhead coords, and last set to -1
        
- a visited set is not needed because in order to advance, the current value must be 1 + the last
- also the only time count is added if that summit has not been added to the corresponding trailhead set yet
- therefore, since the order is maintained and the count is controlled by a set, there is no need for a visited set
    - the same coords may be visited if a trail branches and then merges, but that should not affect runtime that much and
        since the count is controlled with a set, there is no chance of duplicate counts
"""

from dotenv import load_dotenv
import os
from collections import defaultdict

load_dotenv()
DAY = 10
BASE_PATH = (os.getenv('BASE_PATH') or "") + f"day_{DAY}/"
INPUT_FILE = BASE_PATH + f"day_{DAY}_input.txt"
EXAMPLE_FILE = BASE_PATH + f"day_{DAY}_example.txt"

def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
        matrix = [[int(char) for char in list(line)] for line in lines]
        return matrix
    
matrix = parse_input_file(INPUT_FILE)
num_rows = len(matrix)
num_cols = len(matrix[0])
# print(matrix)

def main(part: int):
    hashmap = defaultdict(set)
    TRAILHEAD = 0
    SUMMIT = 9
    num_unique = 0
    num_paths = 0
    
    def dfs(row: int, col:int , trailhead: tuple, last_val: int):
        nonlocal num_unique, num_paths
        
        if (row < 0 or col < 0 or row >= num_rows or col >= num_cols
            or matrix[row][col] != last_val + 1):
            return
        
        if matrix[row][col] == SUMMIT:
            num_paths += 1
            
            if (row, col) not in hashmap[trailhead]:
                hashmap[trailhead].add((row, col))
                num_unique += 1
            return

        dfs(row - 1, col, trailhead, matrix[row][col])
        dfs(row + 1, col, trailhead, matrix[row][col])
        dfs(row, col - 1, trailhead, matrix[row][col])
        dfs(row, col + 1, trailhead, matrix[row][col])
    
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == TRAILHEAD:
                dfs(row, col, (row, col), -1)
    
    return num_unique if part == 1 else num_paths

part_1_res = main(part = 1)
print('part 1:', part_1_res)

part_2_res = main(part = 2)
print('part 2:', part_2_res)