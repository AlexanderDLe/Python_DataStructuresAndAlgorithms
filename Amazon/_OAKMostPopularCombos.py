import heapq

class Node(object):
  def __init__(self, val) -> None:
    self.val = val

  def __repr__(self):
    return f'Node value: {self.val}'

  def __lt__(self, other):
    return self.val < other.val

def kMostPopular(n, popularity, k):
  heap = []
  
  def backtrack(index, sum):
    if index == n:
      print(len(heap))
      if len(heap) < k: 
        heapq.heappush(heap, Node(sum))
      else:
        if sum > heap[0].val:
          heapq.heappop(heap)
          heapq.heappush(heap, Node(sum))
      return

    backtrack(index + 1, sum)
    backtrack(index + 1, sum + popularity[index])
  
  backtrack(0, 0)
  items = []
  for node in heap:
    items.append(node.val)
  
  items.sort(reverse=True)
  return items
  

print(kMostPopular(3, [3,5,-2], 3))