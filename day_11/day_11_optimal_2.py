"""
https://www.reddit.com/r/adventofcode/comments/1hbm0al/comment/m1i36gs/
- memoization
"""

from dotenv import load_dotenv
import os
from collections import defaultdict

load_dotenv()
DAY = 11
BASE_PATH = (os.getenv('BASE_PATH') or "") + f"day_{DAY}/"
INPUT_FILE = BASE_PATH + f"day_{DAY}_input.txt"
EXAMPLE_FILE = BASE_PATH + f"day_{DAY}_example.txt"

def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        items = file.read().strip().split(' ')
        array = [int(item) for item in items]
        return array
    
array = parse_input_file(INPUT_FILE)

def num_digits_of(num: int):
    digits = 0
    while num:
        num //= 10
        digits += 1
    return digits

def solve(stone, blinks, memory):
    val = 0
    
    if blinks == 0:
        return 1
    elif (stone, blinks) in memory:
        return memory[(stone, blinks)]
    elif stone == 0:
        val = solve(1, blinks - 1, memory)
    elif (num_digits := num_digits_of(stone)) % 2 == 0:
        half_length = (num_digits // 2)
        divisor = 10 ** half_length
        
        left_half = stone // divisor
        right_half = stone % divisor
        val = solve(left_half, blinks - 1, memory) + solve(right_half, blinks - 1, memory)
    else:
        val = solve(stone * 2024, blinks - 1, memory)
    memory[(stone, blinks)] = val
    
    return val

def main(blinks: int):
    sum_ = 0
    
    memory = {}
    
    for stone in array:
        sum_ += solve(stone, blinks, memory)
    
    return sum_
    
part_1_res = main(25)
print('part 1:', part_1_res)

part_2_res = main(75)
print('part 2:', part_2_res)