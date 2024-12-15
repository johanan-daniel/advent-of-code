"""
https://www.reddit.com/r/adventofcode/comments/1hbm0al/comment/m1i36gs/
- memoization that caches results for each num per blink
- will recurse to all possibilities, but use cached values if they exist

Main function:
    init sum
    
    for each stone in initial array:
        call recursive function with stone, total blinks, and hashmap for caching
        add output to sum
    
    return sum

Recursive(stone, blinks, cache):
    if blinks is 0:
        return 1
    elif (stone, blinks) in cache:
        return cached value
    elif stone is 0:
        recurse with stone as 1 and decrement blinks
        save output
    elif stone has even digits:
        recurse with each half and decrement blinks
        save sum of outputs
    else:
        recurse with 2024 * digit and decrement blinks
        save output
    
    insert (stone, blinks) into cache with saved output from recursion called as value
    return value
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

def solve(stone, blinks, cache):
    val = 0
    
    if blinks == 0:
        # this is the count for each stone
        # for values that become a single different stone, returns 1
        # for stone that splits in half, it returns the sum of two recursions
        return 1
    elif (stone, blinks) in cache:
        return cache[(stone, blinks)]
    elif stone == 0:
        val = solve(1, blinks - 1, cache)
    elif (num_digits := num_digits_of(stone)) % 2 == 0:
        half_length = (num_digits // 2)
        divisor = 10 ** half_length
        
        left_half = stone // divisor
        right_half = stone % divisor
        val = solve(left_half, blinks - 1, cache) + solve(right_half, blinks - 1, cache)
    else:
        val = solve(stone * 2024, blinks - 1, cache)
    
    # stores first instance of stone at blink level with the count returned
    cache[(stone, blinks)] = val
    
    return val

def main(blinks: int):
    sum_ = 0
    
    cache = {}
    
    for stone in array:
        sum_ += solve(stone, blinks, cache)
    
    return sum_
    
part_1_res = main(25)
print('part 1:', part_1_res)

part_2_res = main(75)
print('part 2:', part_2_res)