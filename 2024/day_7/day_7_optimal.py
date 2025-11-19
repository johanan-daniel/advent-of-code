"""
- parse input into two arrays
    - 1 for test values
    - 1 for array of numbers in each equation

- loop over each value & numbers:
    - test if valid and update total if so

valid():
    - if only 1 operand left:
        return if it == target
    
    # elif works because changes only take effect on recursive call and once valid, can return
    - recurse with first two operands summed and combined with rest of operands, save output
        - return true if true (can recurse in conditional of if)
    - recurse with first two operands multiplied and rest of operands, save output
        - return true if true
    - if part 2:
        - recurse with first two operands concatenated and rest of operands, save output
            - return true if true
    - return false at end if nothing before returned true
"""

from dotenv import load_dotenv
import os

load_dotenv()
base_path = (os.getenv('BASE_PATH') or "") + "day_7/"
INPUT_FILE = base_path + "day_7_input.txt"
EXAMPLE_FILE = base_path + "day_7_example.txt"

def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        raw_lines = file.read().split('\n')
        lines = [line.split(': ') for line in raw_lines]
        
        targets = [int(line[0]) for line in lines]
        equations = [line[1].split(' ') for line in lines]
        operands: list[list[int]] = []
        for equation in equations:
            operands.append([int(num) for num in equation])
            
    return [targets, operands]

targets, equations = parse_input_file(INPUT_FILE)

def valid(target, operands: list[int], part: int) -> bool:
    if len(operands) == 1:
        return operands[0] == target

    last = operands[-1]
    
    possible_mul = False
    possible_concat = False
    possible_add = valid(target - last, operands[:-1], part)

    # could also do reg division (float) and remove if statement
    if target % last == 0:
        possible_mul = valid(target // last, operands[:-1], part)

    if part == 2:
        next_power_of_10 = 1
        while next_power_of_10 <= last:
            next_power_of_10 *= 10
        # checks if after removing last num and digits for that num, remainder could be valid
        # if 156 and [15,6], takes 156-6 = 150 and since 150%10==0, can do 150//10 = 15 (dividing by 10 removes digits used by 6)
        if (target - last) % next_power_of_10 == 0:
            possible_concat = valid((target - last) // next_power_of_10, operands[:-1], part)

    return possible_mul or possible_add or possible_concat

def part_1():
    total = 0
    
    for i in range(len(targets)):
        if (valid(targets[i], equations[i], part=1)):
            total += targets[i]
    
    return total

def part_2():
    total = 0
    
    for i in range(len(targets)):
        if (valid(targets[i], equations[i], part=2)):
            total += targets[i]
    
    return total

part_1_res = part_1()
print('part 1:', part_1_res)

part_2_res = part_2()
print('part 2:', part_2_res)