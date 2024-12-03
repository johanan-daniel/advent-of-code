from collections import Counter
import heapq
from typing import List

def get_total_dist(list1: List[int], list2: List[int]) -> int:
  heapq.heapify(list1)
  heapq.heapify(list2)

  total_dist = 0
  while list1 and list2:
    num1 = heapq.heappop(list1)
    num2 = heapq.heappop(list2)
    
    dist = abs(num1 - num2)
    total_dist += dist

  return total_dist

def parse_input_file(filename: str, list_1: List[int], list_2: List[int]) -> List[List[int]]:
  with open(filename, 'r') as file:
    for file_line in file:
      line = file_line.strip()
      split = line.split('   ')
      list_1.append(int(split[0]))
      list_2.append(int(split[1]))


FILENAME = "day_1_input.txt"
list_1 = []
list_2 = []

parse_input_file(FILENAME, list_1, list_2)
total = get_total_dist(list_1, list_2)
print(total)