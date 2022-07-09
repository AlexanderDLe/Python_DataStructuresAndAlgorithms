'''

  AlgoExpert Disk Stacking

'''

class Solution:  
  def diskStacking(self, disks):
    n = len(disks)
    disks.sort(key = lambda x: x[2])
    heights = [[x[2], [i]] for i, x in enumerate(disks)]
    
    for i in range(1, n):
      for j in range(i - 1, -1, -1):
        prevDisk, currDisk = disks[j], disks[i]
        
        if self.canStack(prevDisk, currDisk) == False: continue
        
        if heights[j][0] + disks[i][2] > heights[i][0]:
          heights[i][0] = heights[j][0] + disks[i][2]
          heights[i][1] = heights[j][1] + [i]
        
    result = max(heights)
    result = list(map(lambda x: disks[x], result[1]))
    return result
  
  def canStack(self, prevDisk, currDisk):
    for i in range(3):
      if prevDisk[i] >= currDisk[i]: return False
    return True
    
  
def runSolution():
  solution = Solution()
  print(solution.diskStacking(disks = [
    [2, 1, 2],
    [3, 2, 3],
    [2, 2, 8],
    [2, 3, 4],
    [1, 3, 1],
    [4, 4, 5]
  ]))
  print(solution.diskStacking(disks = [[2,1,2],[3,2,3],[2,2,8],[2,3,4],[1,3,1],[4,4,5]]))
  print(solution.diskStacking(disks = [[2,1,2]]))
  pass
runSolution()