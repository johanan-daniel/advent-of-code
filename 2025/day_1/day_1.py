from dotenv import load_dotenv
import os

load_dotenv()

DAY = 1
BASE_PATH = (os.getenv('BASE_PATH') or "") + f"/2025/day_{DAY}/"

INPUT_FILE = BASE_PATH + f"day_{DAY}_input.txt"
EXAMPLE_FILE = BASE_PATH + f"day_{DAY}_example.txt"

def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
        return lines

def convert_rotations_to_int(rotations: list[str]):
    output = []
    
    for rotation in rotations:
        num = int(rotation[1:])

        if rotation[0] == 'L':
            output.append(-num)
        else:
            output.append(num)
        
    return output

split_input = parse_input_file(INPUT_FILE)
rotations_as_int = convert_rotations_to_int(split_input)

def part_1():
    # print(split_input)
    # print(rotations_as_int)
    count = 0
    DIGITS = 100

    start_pos = 50
    pos = start_pos

    for rotation in rotations_as_int:
        pos = (pos + rotation) % DIGITS

        if pos == 0:
            count += 1
    
    return count

part_1_res = part_1()
print('part 1:', part_1_res)