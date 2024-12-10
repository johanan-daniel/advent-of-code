import re
from dotenv import load_dotenv
import os

load_dotenv()
base_path = (os.getenv('BASE_PATH') or "") + "day_3/"
INPUT_FILE = base_path + "day_3_input.txt"
EXAMPLE_FILE_1 = base_path + "day_3_example.txt"
EXAMPLE_FILE_2 = base_path + "day_3_example_2.txt"

def parse_input_file(filename: str):
    output = ''
    with open(filename, 'r') as file:
        output = file.read()
    return output

input_text = parse_input_file(INPUT_FILE)

def part_1():
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    
    total = 0
    for i in range(len(input_text)):
        match = pattern.match(input_text[i:])
        
        if match:
            num_1 = int(match.group(1))
            num_2 = int(match.group(2))
            total += num_1 * num_2
    
    return total

def part_2():
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    
    total = 0
    enabled = True
    for i in range(len(input_text)):
        if (input_text[i : i+7] == "don't()"):
            enabled = False
        elif (input_text[i : i+4] == "do()"):
            enabled = True
        
        if not enabled:
            continue
        
        match = pattern.match(input_text[i:])
        
        if match:
            num_1 = int(match.group(1))
            num_2 = int(match.group(2))
            total += num_1 * num_2
    
    return total
  
part_1_res = part_1()
print('part 1:', part_1_res)

part_2_res = part_2()
print('part 2:', part_2_res)