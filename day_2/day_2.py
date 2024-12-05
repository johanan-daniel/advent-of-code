from dotenv import load_dotenv
import os

"""
Part 1:
  split each line into a list of numbers
  
  init count
  for each line:
    run is_valid() on each
    increment count if true
  
  return count

Part 2:
  - loop from 0 to end:
    - remove item i from array and check if valid
    - if any are valid, increment count
"""

load_dotenv()
base_path = (os.getenv('BASE_PATH') or "") + "/day_2/"
INPUT_FILE = base_path + "day_2_input.txt"
EXAMPLE_FILE = base_path + "day_2_example.txt"

def parse_input_file(filename: str, list_1):
  with open(filename, 'r') as file:
    for file_line in file:
      line = file_line.strip()
      list_1.append(to_list(line))

def to_list(line: str) -> list[int]:
  output = []
  
  output = [int(string) for string in line.split()]
  
  return output

def is_valid(nums: list[int]) -> bool:
  increasing = True
  decreasing = True
  
  for i in range(1, len(nums)):
    dist = abs(nums[i - 1] - nums[i])
    if dist < 1 or dist > 3:
      return False

    increasing &= nums[i - 1] <= nums[i]
    decreasing &= nums[i - 1] >= nums[i]

  return increasing or decreasing

list_1 = []
parse_input_file(INPUT_FILE, list_1)

def part_1():
  count = 0
  for nums in list_1:
    if (is_valid(nums)):
      count += 1
  
  return count

part_1_res = part_1()
print('part 1:', part_1_res)

def part_2():
  count = 0
  for nums in list_1:
    valid = is_valid(nums)
    
    for i in range(len(nums)):
      valid |= is_valid(nums[:i] + nums[i + 1:])
    
      if valid:
        count += 1
        break
  
  return count

part_2_res = part_2()
print('part 2:', part_2_res)