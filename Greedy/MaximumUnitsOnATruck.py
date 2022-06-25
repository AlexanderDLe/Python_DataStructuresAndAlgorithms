'''

  1710. Maximum Units on a Truck

'''

class Solution:
  def maximumUnits(self, boxTypes, truckSize):
    boxTypes.sort(key=lambda x: -x[1])
    maxUnits = 0
    
    for box, units in boxTypes:
      boxesTaken = min(truckSize, box)
      maxUnits += (boxesTaken * units)
      truckSize -= boxesTaken
      
      if truckSize == 0: break
      
    return maxUnits

def runSolution():
  solution = Solution()
  
  print(solution.maximumUnits(
    boxTypes = [[1,3],[2,2],[3,1]], 
    truckSize = 4
  ))
  print(solution.maximumUnits(
    boxTypes = [[5,10],[2,5],[4,7],[3,9]], 
    truckSize = 10
  ))
  pass
runSolution()
