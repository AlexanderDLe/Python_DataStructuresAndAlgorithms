'''

  909. Snakes and Ladders

  -1, -1, -1, -1, -1, -1
  -1, -1, -1, -1, -1, -1
  -1, -1, -1, -1, -1, -1
  -1, 35, -1, -1, 13, -1
  -1, -1, -1, -1, -1, -1
  -1, 15, -1, -1, -1, -1
  
'''

from collections import deque


class Solution:
  def snakesAndLadders(self, board):
    if not board or not board[0]: return -1
    
    self.n = len(board)
    totalCells = self.n * self.n
       
    queue = deque([1])
    seen  = set()
    moves = 0
    
    while queue:
      qLen = len(queue)
      
      for _ in range(qLen):
        val = queue.popleft()
        if val == totalCells: return moves
        
        # Mistake: val + 7 is upper bound because end pos exclusive
        for nextVal in range(val + 1, val + 7):
          if nextVal > totalCells: break
          if nextVal in seen: continue
          
          seen.add(nextVal)
          
          nextBoardVal = self.getPositionValue(nextVal, board)
          if nextBoardVal == -1: queue.append(nextVal)
          else                 : queue.append(nextBoardVal)
      
      moves += 1
        
    return -1
      
    
  def getPositionValue(self, val, board):
    rowVal = (val - 1)// self.n
    colVal = (val - 1) % self.n

    rightward = rowVal % 2 == 0
    actualRow = self.n - rowVal - 1
    actualCol = colVal if rightward else self.n - colVal - 1
    
    return board[actualRow][actualCol]
  
  
def runSolution():
  solution = Solution()
  # print(solution.snakesAndLadders([
  #   [-1,-1,-1,-1,-1,-1],
  #   [-1,-1,-1,-1,-1,-1],
  #   [-1,-1,-1,-1,-1,-1],
  #   [-1,35,-1,-1,13,-1],
  #   [-1,-1,-1,-1,-1,-1],
  #   [-1,15,-1,-1,-1,-1]
  # ]))
  print(solution.snakesAndLadders([
    [-1,  1,  2,-1],
    [ 2, 13, 15,-1],
    [-1, 10, -1,-1],
    [-1,  6,  2, 8]
  ]))
  # print(solution.snakesAndLadders([
  #   [-1,-1],
  #   [-1, 3]
  # ]))
runSolution()