from dotenv import load_dotenv
import os

load_dotenv()
DAY = 13
BASE_PATH = (os.getenv('BASE_PATH') or "") + f"day_{DAY}/"
INPUT_FILE = BASE_PATH + f"day_{DAY}_input.txt"
EXAMPLE_FILE = BASE_PATH + f"day_{DAY}_example.txt"

def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        sections = file.read().strip().split('\n\n')
        sections = [section.split('\n') for section in sections]
        machines = []
        
        for section in sections:
            ...
        
        return sections

inputs = parse_input_file(EXAMPLE_FILE)