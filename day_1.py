from collections import Counter
import heapq
from typing import List

"""
Part 1:
- parse numbers into two separate lists per column
- sort each list
- for each item from both lists:
  - calculate distance of two nums
  - add to total
- return total

Part 2:
- init hashmap
- init total to 0
- loop over each num in list2:
  - count frequneecy in hashmap
- loop over each num in list1:
  - multiply by freq (or 0)
  - add onto total
- return total
"""

def parse_input_file(filename: str, list_1: List[int], list_2: List[int]):
  with open(filename, 'r') as file:
    for file_line in file:
      line = file_line.strip()
      split = line.split('   ')
      list_1.append(int(split[0]))
      list_2.append(int(split[1]))

def get_total_dist(list1: List[int], list2: List[int]) -> int:
  total_dist = 0
  for i in range(len(list1)):
    num1 = list1[i]
    num2 = list2[i]
    
    dist = abs(num1 - num2)
    total_dist += dist

  return total_dist

def get_similarity_score(list1: List[int], list2: List[int]) -> int:
  hashmap = {}
  total = 0
  
  for num in list2:
    hashmap[num] = hashmap.get(num, 0) + 1
  
  for num in list1:
    prod = num * hashmap.get(num, 0)
    total += prod
    
  return total

FILENAME = "day_1_input.txt"
list_1 = []
list_2 = []

parse_input_file(FILENAME, list_1, list_2)

# part 1
list_1.sort()
list_2.sort()
part1 = get_total_dist(list_1, list_2)
print("part 1:", part1)

# part 2
part2 = get_similarity_score(list_1, list_2)
print('part 2:', part2)