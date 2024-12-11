"""
- parse input into two arrays
    - 1 for test values
    - 1 for array of numbers in each equation

- loop over each value & numbers:
    - make multiple arrays of length len(numbers) - 1 for order of operators:
        - use backtracking to to make multiple permutations of the two possibilities
    - test each order and add value to sum if equation result matches
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

def permutations(size: int, part: int) -> list[list[str]]:
    output = []
    
    def backtrack(perm):
        if len(perm) == size:
            output.append(perm.copy())
            return
        
        perm.append('+')
        backtrack(perm)
        perm.pop()
        
        perm.append('*')
        backtrack(perm)
        perm.pop()
        
        if part == 2:
            perm.append('||')
            backtrack(perm)
            perm.pop()
    
    backtrack([])
    return output

def valid(target: int, operands: list[int], perms_operators: list[list[str]], part: int) -> bool:
    for operators in perms_operators:
        total = operands[0]
        for i in range(1, len(operands)):
            op = operators[i - 1]
            num = operands[i]
            
            if op == '+':
                total += num
            elif op == '*':
                total *= num
            elif part == 2 and op == '||':
                total = int(str(total) + str(num))
        
        if total == target:
            return True
    
    return False
            

def part_1():
    total = 0
    
    for i in range(len(targets)):
        perms_operators = permutations(len(equations[i]) - 1, part=1)
        
        if (valid(targets[i], equations[i], perms_operators, part=1)):
            total += targets[i]
    
    return total

def part_2():
    total = 0
    
    for i in range(len(targets)):
        perms_operators = permutations(len(equations[i]) - 1, part=2)
        
        if (valid(targets[i], equations[i], perms_operators, part=2)):
            total += targets[i]
    
    return total

part_1_res = part_1()
print('part 1:', part_1_res)

part_2_res = part_2()
print('part 2:', part_2_res)