from dotenv import load_dotenv
import os

load_dotenv()

DAY = 2
BASE_PATH = (os.getenv('BASE_PATH') or "") + f"/2025/day_{DAY}/"

INPUT_FILE = BASE_PATH + f"day_{DAY}_input.txt"
EXAMPLE_FILE = BASE_PATH + f"day_{DAY}_example.txt"

def parse_input(filename: str):
    with open(filename) as file:
        ranges = file.read().strip().split(',')
        output = []
        for range in ranges:
            endpoints = range.split('-')
            output.append([int(endpoints[0]), int(endpoints[1])])
        
        return output

ranges = parse_input(EXAMPLE_FILE)

def part_1():
    total = 0

    for start, end in ranges:
        for id in range(start, end + 1):
            id_str = str(id)
            if len(id_str) % 2 == 1:
                continue
                
            half_len = len(id_str) // 2
                
            if id_str[:half_len] == id_str[half_len:]:
                total += int(id_str)
        
    return total

part_1_res = part_1()
print(part_1_res)