'''

  287. Find the Duplicate Number

'''

class SolutionTortoiseAndHare:
  def findDuplicate(self, nums):
    s = f = nums[0]
    
    while True:
      s, f = nums[s], nums[nums[f]]
      if s == f: break
    
    s = nums[0]
    while s != f:
      s, f = nums[s], nums[f]
    return s

class SolutionCyclicSort:
  def findDuplicate(self, nums):
    
    for i in range(len(nums)):
      while nums[i] != i + 1:
        val = nums[i]
        if nums[i] == nums[val - 1]: return nums[i]
        nums[i], nums[val - 1] = nums[val - 1], nums[i]
        
    
    return -1


def runSolution():
  solution = SolutionCyclicSort()
  print(solution.findDuplicate([1,3,4,2,2]))
  print(solution.findDuplicate([3,1,3,4,2]))
  print(solution.findDuplicate([18,13,14,17,9,19,7,17,4,6,17,5,11,10,2,15,8,12,16,17]))
  pass
runSolution()

