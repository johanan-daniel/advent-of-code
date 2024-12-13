"""
Given: integer matrix
Return: integer for sum of scores of all trailheads, a score being how many 9s can be reached on a valid trail from each trailhead

init hashmap of sets
- each item in hashmap is the coord for a trailhead
- each value is a set to store the coords of all 9s reachable from each
init count

dfs(row, col, trailhead, visited, last_val):
    if visited or out of bounds or not 1 + last_val:
        return
    
    if 9:
        if not in set at hashmap[trailhead]:
            increment count
            add to set at hashmap[trailhead]
        return
    
    add to visited
    dfs on neighbors (with current as last_val)
    # remove from visited

loop over each cell:
    if trailhead:
        init visited
        start dfs with row, col, trailhead coords, visited, and last set to -1
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
    count = 0
    
    def dfs(row: int, col:int , trailhead: tuple, visited: set[tuple], last_val: int):
        nonlocal count
        
        if ((row, col) in visited
            or row < 0 or col < 0 or row >= num_rows or col >= num_cols
            or matrix[row][col] != last_val + 1):
            return
        
        if matrix[row][col] == SUMMIT:
            if (row, col) not in hashmap[trailhead]:
                hashmap[trailhead].add((row, col))
                count += 1
            return

        dfs(row - 1, col, trailhead, visited, matrix[row][col])
        dfs(row + 1, col, trailhead, visited, matrix[row][col])
        dfs(row, col - 1, trailhead, visited, matrix[row][col])
        dfs(row, col + 1, trailhead, visited, matrix[row][col])
    
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == TRAILHEAD:
                visited = set()
                dfs(row, col, (row, col), visited, -1)
    
    return count

part_1_res = main(part = 1)
print('part 1:', part_1_res)