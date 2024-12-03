import heapq

list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]

def get_total_dist(list1, list2):
  heapq.heapify(list1)
  heapq.heapify(list2)

  total_dist = 0
  while list1 and list2:
    num1 = heapq.heappop(list1)
    num2 = heapq.heappop(list2)
    
    dist = abs(num1 - num2)
    total_dist += dist

  return total_dist