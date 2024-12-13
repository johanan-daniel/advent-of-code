"""
- brute force for each stone

loop n times:
    init new array of stones
    
    loop over given stones:
        based on condition, make new stone and add each new one to array
    
    replace stones with new array

return length of stones array
"""

from dotenv import load_dotenv
import os

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

def main(blinks: int, part: int):
    stones = array.copy()
    
    for _ in range(blinks):
        temp = []
        for num in stones:
            num_digits = num_digits_of(num)
            if num == 0:
                temp.append(1)
            elif num_digits % 2 == 0:
                # split digits
                half_length = (num_digits // 2)
                divisor = 10 ** half_length
                left_half = num // divisor
                right_half = num % divisor
                temp.append(left_half)
                temp.append(right_half)
            else:
                temp.append(num * 2024)
        stones = temp
    
    # print(stones)
    return len(stones)
    

part_1_res = main(75, 1)
print('part 1:', part_1_res)