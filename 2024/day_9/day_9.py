from dotenv import load_dotenv
import os
from collections import defaultdict

load_dotenv()
DAY = 9
BASE_PATH = (os.getenv('BASE_PATH') or "") + f"day_{DAY}/"
INPUT_FILE = BASE_PATH + f"day_{DAY}_input.txt"
EXAMPLE_FILE = BASE_PATH + f"day_{DAY}_example.txt"

def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        return file.read()
    
input_line = parse_input_file(EXAMPLE_FILE)
print(input_line)

def main(part: int):
    ...

part_1_res = main(part=1)
# print('part 1:', part_1_res)