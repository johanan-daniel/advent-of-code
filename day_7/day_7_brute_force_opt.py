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

def valid(target: int, operands: list[int], part: int) -> bool:
    if len(operands) == 1:
        return operands[0] == target
    
    if valid(target, [operands[0] + operands[1]] + operands[2:], part):
        return True
    elif valid(target, [operands[0] * operands[1]] + operands[2:], part):
        return True
    elif part == 2 and valid(target, [int(str(operands[0]) + str(operands[1]))] + operands[2:], part):
        return True
    
    return False

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