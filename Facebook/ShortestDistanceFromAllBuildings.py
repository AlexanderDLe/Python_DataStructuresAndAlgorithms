'''

  317. Shortest Distance From All Buildings

'''
from collections import deque
import collections
from itertools import product
import math
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from _utils import printMatrix


def invalidCell(row, col, grid, rows, cols):
  if row < 0 or row >= rows: return True
  if col < 0 or col >= cols: return True
  if grid[row][col] == 1 or grid[row][col] == 2: return True
  return False

def shortestDistance(grid):
  rows = len(grid)
  cols = len(grid[0])

  dirs      = [[-1, 0], [0, 1], [1, 0], [0, -1]]
  distances = [[0] * cols for x in range(rows)]
  buildingCount = 0

  for row, col in product(range(rows), range(cols)):
    if grid[row][col] != 1: continue

    buildingCount += 1
    seen = set()
    queue = deque([(row, col)])
    count = 1
    distance = 0

    while queue:
      while count:
        currRow, currCol = queue.popleft()
        distances[currRow][currCol] += distance

        cell = grid[currRow][currCol]
        if cell != 1 and cell != 2: grid[currRow][currCol] -= 1

        for x, y in dirs:
          nextRow = currRow + x
          nextCol = currCol + y

          if invalidCell(nextRow, nextCol, grid, rows, cols): continue
          if (nextRow, nextCol) in seen: continue

          seen.add((nextRow, nextCol))
          queue.append((nextRow, nextCol))

        count -= 1
      count = len(queue)
      distance += 1

  minDistance = float('inf')
  for row, col in product(range(rows), range(cols)):
    cell = grid[row][col]
    if cell < 0 and abs(cell) == buildingCount:
      minDistance = min(minDistance, distances[row][col])
    
  return minDistance if minDistance != math.inf else -1



print(shortestDistance([
  [1,0,2,0,1],
  [0,0,0,0,0],
  [0,0,1,0,0]
]))

print(shortestDistance([
  [1,0]
]))

print(shortestDistance([
  [1,1],
  [0,1]
]))