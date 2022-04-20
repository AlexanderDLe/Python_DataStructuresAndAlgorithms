'''

  778. Swim in Rising Water

'''

import heapq


class HeapNode:
  def __init__(self, val, row, col) -> None:
    self.val = val
    self.pos = [row, col]

  def __lt__(self, other):
    return self.val < other.val

def swimInWater(grid):
  dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
  n = len(grid)

  def invalidCell(row, col, seen):
    if row < 0 or row == n: return True
    if col < 0 or col == n: return True
    if (row, col) in seen : return True
    return False

  time = 0
  seen = set()
  seen.add((0, 0))
  
  heap = []
  heapq.heappush(heap, HeapNode(grid[0][0], 0, 0))

  while heap:
    node = heapq.heappop(heap)
    val = node.val
    row, col = node.pos
    
    time = max(time, val)
    if row == n - 1 and col == n - 1: break

    for x, y in dirs:
      nextRow = row + x
      nextCol = col + y

      if invalidCell(nextRow, nextCol, seen): continue

      seen.add((nextRow, nextCol))
      heapq.heappush(heap, HeapNode(grid[nextRow][nextCol], nextRow, nextCol))
    
  return time










print(swimInWater([
  [0,2],
  [1,3]
]))
print(swimInWater([
  [0,   1,  2,  3,  4],
  [24, 23, 22, 21,  5],
  [12, 13, 14, 15, 16],
  [11, 17, 18, 19, 20],
  [10,  9,  8,  7,  6]
]))