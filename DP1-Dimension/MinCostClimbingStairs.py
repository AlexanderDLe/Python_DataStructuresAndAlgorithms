'''

  746. Min Cost Climbing Stairs

  [10, 15, 20, 0]
               ^ destination, start DP here
  [10, 15, 20, 0]
            
  DP = [0, 0, 0, 0]

  ------------------------------------

  [10, 15, 20, 0]
            ^  ^
            jump
            
  If we make one jump from curr to next, it would cost 20
  
  ------------------------------------

  [10, 15, 20, 0]
        ^   ^  ^
        jump
            
  If we make one jump, it would cost 20
  If we make two jumps, it would cost 15.
  We add the lesser of the two = 15
  
  ------------------------------------

  [10, 15, 20, 0]
   ^   ^   ^
   jump
            
  If we make one jump, it would cost 15
  If we make two jumps, it would cost 20.
  We add the lesser of the two: 25

  [25, 15, 20, 0]
  
  ----
  
  Since we can start at either index 0 or 1, we take the lesser of the two.

  
'''

class SolutionRef:
  def minCostClimbingStairs(self, cost):
    if len(cost) == 0: return 0
    if len(cost) == 1: return cost[0]
    cost.append(0)
    
    for i in range(len(cost) - 2, -1, -1):
      next1 = cost[i + 1]
      next2 = cost[i + 2] if i < len(cost) - 2 else 0      
      cost[i] += min(next1, next2)
    
    return min(cost[0], cost[1])

class Solution:
  def minCostClimbingStairs(self, cost):
    n = len(cost)
    if n == 0: return 0
    if n == 1: return cost[0]
    cost.append(0)

    for i in range(n - 2, -1, -1):
      next1 = cost[i + 1]
      next2 = cost[i + 2] if i < n - 2 else 0
      cost[i] += min(next1, next2)
      
    
    return min(cost[0], cost[1])
    


def runSolution():
  solution = Solution()
  print(solution.minCostClimbingStairs(cost = [10,15,20]))
  print(solution.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))
  pass
runSolution()