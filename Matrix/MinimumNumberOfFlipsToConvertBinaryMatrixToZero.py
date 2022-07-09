'''

  1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

'''

from collections import deque


class SolutionRef:
  def minFlips(self, mat):
    rows, cols = len(mat), len(mat[0])
    totalCells = rows * cols
    bitMask = [1 << i for i in range(totalCells)]
    dq = deque([(0, mat)])
    visited = set()
    
    while dq:
      currFlips, matrix = dq.popleft()
    
      if self.solved(matrix):
        return bin(currFlips).count('1')
      
      for k in range(totalCells):
        mask = bitMask[k]
        
        alreadyFlipped = currFlips & mask
        redundantFlip  = currFlips | mask in visited
        
        if not alreadyFlipped and not redundantFlip:
          visited.add(currFlips | mask)
          row = k // cols
          col = k %  cols
          
          matrixCopy = [row[:] for row in matrix]
          for xDir, yDir in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            nextRow, nextCol = row + xDir, col + yDir
            
            if 0 <= nextRow < rows and 0 <= nextCol < cols:
              curr = matrixCopy[nextRow][nextCol]
              matrixCopy[nextRow][nextCol] = 1 if curr == 0 else 0
          
          dq.append((currFlips | mask, matrixCopy))
      
    return -1

  def solved(self, arr):
    return all(all(num == 0 for num in row) for row in arr)
    
class Solution:
  def minFlips(self, mat):
    rows, cols = len(mat), len(mat[0])
    totalCells = rows * cols
    bitmask = [1 << i for i in range(totalCells)]
    queue = deque([(0, mat)])
    visited = set([0])
    
    while queue:
      currFlipped, currMatrix = queue.popleft()
      
      if self.solved(currMatrix): return bin(currFlipped).count('1')
      
      for i in range(totalCells):
        mask = bitmask[i]
        
        alreadyFlipped = currFlipped & mask
        redundantFlip  = currFlipped | mask in visited
        if alreadyFlipped or redundantFlip: continue
        
        row = i // cols
        col = i %  cols
        matrixCopy = [row.copy() for row in currMatrix]
        
        for xDir, yDir in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
          nextRow, nextCol = row + xDir, col + yDir
          
          if 0 <= nextRow < rows and 0 <= nextCol < cols:
            currCell = matrixCopy[nextRow][nextCol]
            matrixCopy[nextRow][nextCol] = 1 if currCell == 0 else 0
          
        nextFlip = currFlipped | mask
        visited.add(nextFlip)
        queue.append((nextFlip, matrixCopy))
    
    return -1

  
  def solved(self, matrix):
    return all(all(num == 0 for num in row) for row in matrix)
    
    
  
def runSolution():
  solution = Solution()
  print(solution.minFlips(
    mat = [[0,0],[0,1]]
  ))
  print(solution.minFlips(
    mat = [[0]]
  ))
  print(solution.minFlips(
    mat = [[1,0,0],[1,0,0]]
  ))
  print(solution.minFlips(
    [[1,0,1],[0,1,0],[1,0,1]]
  ))
  pass
runSolution()