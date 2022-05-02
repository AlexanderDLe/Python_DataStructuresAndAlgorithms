'''

  818. Race Car

'''

from collections import deque


class Solution:
  def racecar(self, target):
    # 1. Initialize double ended queue as (moves, position, velocity)
    queue = deque([(0, 0, 1)])
    
    while queue:
      moves, pos, vel = queue.popleft()

      if pos == target: return moves

      # Always consider moving the car in the direction it is already going
      queue.append((moves + 1, pos + vel, 2 * vel))
      
      # Only consider changing the direction if one of the following conditions is true
      # 1. The car is driving away from the target
      # 2. The car will pass the target in the next move
      passingRight = pos + vel > target and vel > 0
      passingLeft  = pos + vel < target and vel < 0
      if passingRight or passingLeft:
        queue.append((moves + 1, pos, -vel / abs(vel)))
  
  
def runSolution():
  solution = Solution()
  print(solution.racecar(3))
  print(solution.racecar(6))
  pass
runSolution()