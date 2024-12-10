from dotenv import load_dotenv
import os

load_dotenv()
base_path = (os.getenv('BASE_PATH') or "") + "day_5/"
INPUT_FILE = base_path + "day_5_input.txt"
EXAMPLE_FILE = base_path + "day_5_example.txt"

def parse_input_file(filename: str):
    rules = []
    pages_to_produce = []
    
    with open(filename, 'r') as file:
        input_split = file.read().split('\n\n')
        raw_rules = input_split[0]
        raw_pages = input_split[1]
        
        rules = [(int(item[0]), int(item[1])) for item in raw_rules.split('\n')]
        
        for line in raw_pages.split('\n'):
            pages_to_produce.append([int(page) for page in line.split(',')])
            
    return [rules, pages_to_produce]

rules, pages_to_produce = parse_input_file(EXAMPLE_FILE)
print(rules)
print(pages_to_produce)

"""
- somehow order pages based on rules
- loop over pages_to_proudce:
    - check if prereqs are met
    - update prereq

- topological sort?

- using hashmap, make a directed graph of nodes for each?
- then basically just topological sort using graph
"""