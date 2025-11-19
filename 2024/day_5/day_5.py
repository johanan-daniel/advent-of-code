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
        raw_rules, raw_pages  = file.read().split('\n\n')
        
        rules = [rule.split('|') for rule in raw_rules.split('\n')]
        pages_to_produce = [page.split(',') for page in raw_pages.split('\n')]
            
    return [rules, pages_to_produce]

rules, pages_to_produce = parse_input_file(EXAMPLE_FILE)
print(rules)
print(pages_to_produce)

def part_1():
    ...

part_1_res = part_1()
print('part 1:', part_1_res)

"""
- somehow order pages based on rules
- loop over pages_to_proudce:
    - check if prereqs are met
    - update prereq

- topological sort?

- using hashmap, make a directed graph of nodes for each?
- then basically just topological sort using graph

- init hashmap for mapping prereqs for each page
- init hashmap 


# using hashmap, save prereqs for each page
- loop over prereq pairs:
    - add prereq to list for hashmap[page]

- for each list of pages to produce:
    - init visited set
    - init satisfied in hashmap
    
    - loop over each page to produce:
        - add to satisfied hashmap
    - loop over each page to produce:
        - loop over each prereq in prereq hashmap:
            - if 
"""