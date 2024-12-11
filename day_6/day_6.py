from dotenv import load_dotenv
import os

load_dotenv()
base_path = (os.getenv('BASE_PATH') or "") + "day_6/"
INPUT_FILE = base_path + "day_6_input.txt"
EXAMPLE_FILE = base_path + "day_6_example.txt"

def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        lines = [list(line) for line in file.read().split('\n')]
        return lines

matrix = parse_input_file(EXAMPLE_FILE)
# print(matrix)
num_rows = len(matrix)
num_cols = len(matrix[0])

def find_start():
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == '^':
                return (row, col)
    
    return (0, 0)

def in_bounds(row, col):
    return row >= 0 and col >= 0 and row < num_rows and col < num_cols

def part_1(visited: set):
    row, col = find_start()
    dir = '^'
    
    while True:
        visited.add((row, col))
        
        # move poition in direction
        match dir:
            case '^':
                row -= 1
            case 'v':
                row += 1
            case '>':
                col += 1
            case '<':
                col -= 1
        
        if not in_bounds(row, col):
            break
        
        # if obstacle, restore position and change direction
        if matrix[row][col] == '#':
            match dir:
                case '^':
                    row += 1
                    dir = '>'
                case 'v':
                    row -= 1
                    dir = '<'
                case '>':
                    col -= 1
                    dir = 'v'
                case '<':
                    col += 1
                    dir = '^'
            
    return len(visited)
        
def has_loop():
    row, col = find_start()
    visited = set()
    dir = '^'
    
    while True:
        key = (row, col, dir)
        
        if key in visited:
            return True
        
        visited.add(key)
        
        match dir:
            case '^':
                row -= 1
            case 'v':
                row += 1
            case '>':
                col += 1
            case '<':
                col -= 1
        
        if not in_bounds(row, col):
            break
        
        if matrix[row][col] == '#':
            match dir:
                case '^':
                    row += 1
                    dir = '>'
                case 'v':
                    row -= 1
                    dir = '<'
                case '>':
                    col -= 1
                    dir = 'v'
                case '<':
                    col += 1
                    dir = '^'
            
    return False

def part_2(visited: set):
    count = 0
    for row, col in visited:
        # skip first position
        if matrix[row][col] != '.':
            continue
        
        # test obstacle in each position on path
        matrix[row][col] = '#'
        if (has_loop()):
            count += 1
        matrix[row][col] = '.'
        
    return count
        

visited = set()
part_1_res = part_1(visited)
print('part 1:', part_1_res)

part_2_res = part_2(visited)
print('part 2:', part_2_res)