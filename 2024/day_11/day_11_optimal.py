"""
https://www.reddit.com/r/adventofcode/comments/1hbm0al/comment/m1hcyko/
- cache results for same numbers by using hashmap where hashmap[num] = count
- this allows for 1 computation for each unique number and then a simply operation for how many of each unique number exists

init hashmap with each unique num and counts for frequency of each num

loop blink number of times:
    init temp hashmap
    loop over each key, val in main hashmap:
        do the operations for each key, except set value to val
    set main hashmap to temp one

- this creates a new hashmap on each blink
- each hashmap contains the numbers for each stone and the counts for each number
- this makes it so only 1 operation is needed per unique stone and the count can be used to keep track of the total amounts
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

def main(blinks: int):
    hashmap = {num: 1 for num in array}
    
    for _ in range(blinks):
        new_hashmap = defaultdict(int)
        
        for num, count in hashmap.items():
            if num == 0:
                new_hashmap[1] += count
            elif (num_digits := num_digits_of(num)) % 2 == 0:
                # split digits
                half_length = (num_digits // 2)
                divisor = 10 ** half_length
                
                left_half = num // divisor
                right_half = num % divisor
                
                new_hashmap[left_half] += count
                new_hashmap[right_half] += count
            else:
                new_hashmap[num * 2024] += count
                
        hashmap = new_hashmap
    
    return sum(hashmap.values())
    
part_1_res = main(25)
print('part 1:', part_1_res)

part_2_res = main(75)
print('part 2:', part_2_res)