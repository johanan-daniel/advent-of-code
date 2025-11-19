from dotenv import load_dotenv
import os

load_dotenv()
base_path = (os.getenv('BASE_PATH') or "") + "day_4/"
INPUT_FILE = base_path + "day_4_input.txt"
EXAMPLE_FILE = base_path + "day_4_example.txt"

def parse_input_file(filename: str):
    output = []
    with open(filename, 'r') as file:
        output = file.read().split('\n')
    return output

input_matrix = parse_input_file(INPUT_FILE)
num_rows = len(input_matrix)
num_cols = len(input_matrix[0])

def part_1(G):
    count = 0
    
    for row in range(num_rows):
        for col in range(num_cols):
            if row + 3 < num_rows and G[row][col] == 'X' and G[row + 1][col] == 'M' and G[row + 2][col] == 'A' and G[row + 3][col] == 'S':
                count += 1
            if row + 3 < num_rows and G[row][col] == 'S' and G[row + 1][col] == 'A' and G[row + 2][col] == 'M' and G[row + 3][col] == 'X':
                count += 1
                
            if col + 3 < num_cols and G[row][col] == 'X' and G[row][col + 1] == 'M' and G[row][col + 2] == 'A' and G[row][col + 3] == 'S':
                count += 1
            if col + 3 < num_cols and G[row][col] == 'S' and G[row][col + 1] == 'A' and G[row][col + 2] == 'M' and G[row][col + 3] == 'X':
                count += 1
                
            if (row + 3 < num_rows and col + 3 < num_cols and 
                G[row][col] == 'X' and G[row + 1][col + 1] == 'M' and G[row + 2][col + 2] == 'A' and G[row + 3][col + 3] == 'S'):
                count += 1
            if (row + 3 < num_rows and col + 3 < num_cols and 
                G[row][col] == 'S' and G[row + 1][col + 1] == 'A' and G[row + 2][col + 2] == 'M' and G[row + 3][col + 3] == 'X'):
                count += 1
                
            if (row - 3 >= 0 and col + 3 < num_cols and 
                G[row][col] == 'X' and G[row - 1][col + 1] == 'M' and G[row - 2][col + 2] == 'A' and G[row - 3][col + 3] == 'S'):
                count += 1
            if (row - 3 >= 0 and col + 3 < num_cols and 
                G[row][col] == 'S' and G[row - 1][col + 1] == 'A' and G[row - 2][col + 2] == 'M' and G[row - 3][col + 3] == 'X'):
                count += 1
    
    return count

def part_2(G):
    count = 0
    
    for row in range(num_rows):
        for col in range(num_cols):
            if (G[row][col] == 'A' and 
                row - 1 >= 0 and row + 1 < num_cols and col - 1 >= 0 and col + 1 < num_cols and
                G[row-1][col-1] == 'M' and G[row+1][col+1] == 'S' and G[row-1][col+1] == 'M' and G[row+1][col-1] == 'S'):
                count += 1
            if (G[row][col] == 'A' and 
                row - 1 >= 0 and row + 1 < num_cols and col - 1 >= 0 and col + 1 < num_cols and
                G[row-1][col-1] == 'M' and G[row+1][col+1] == 'S' and G[row-1][col+1] == 'S' and G[row+1][col-1] == 'M'):
                count += 1
            if (G[row][col] == 'A' and 
                row - 1 >= 0 and row + 1 < num_cols and col - 1 >= 0 and col + 1 < num_cols and
                G[row-1][col-1] == 'S' and G[row+1][col+1] == 'M' and G[row-1][col+1] == 'M' and G[row+1][col-1] == 'S'):
                count += 1
            if (G[row][col] == 'A' and 
                row - 1 >= 0 and row + 1 < num_cols and col - 1 >= 0 and col + 1 < num_cols and
                G[row-1][col-1] == 'S' and G[row+1][col+1] == 'M' and G[row-1][col+1] == 'S' and G[row+1][col-1] == 'M'):
                count += 1
    
    return count

part_1_res = part_1(input_matrix)
print('part 1:', part_1_res)

part_2_res = part_2(input_matrix)
print('part 2:', part_2_res)