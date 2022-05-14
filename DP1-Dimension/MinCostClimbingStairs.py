'''

  746. Min Cost Climbing Stairs

'''

class Solution:
  def minCostClimbingStairs(self, cost):
    if len(cost) == 0: return 0
    if len(cost) == 1: return cost[0]
    cost.append(0)
    
    for i in range(len(cost) - 2, -1, -1):
      next1 = cost[i + 1]
      next2 = cost[i + 2] if i < len(cost) - 2 else 0      
      cost[i] = cost[i] + min(next1, next2)
    
    return min(cost[0], cost[1])


def runSolution():
  solution = Solution()
  print(solution.minCostClimbingStairs(cost = [10,15,20]))
  print(solution.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))
  pass
runSolution()