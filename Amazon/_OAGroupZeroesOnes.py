'''
  Given an array containing only 0 and 1 as its elements. 
  We have to sort the array in such a manner that all the 
  ones are grouped together and all the zeros are grouped 
  together. The group of ones can be either at the start 
  of the array or at the end of the array. 
  
  The constraint while sorting is that every one/zero can 
  be swapped only with its adjacent zero/one. Find the 
  minimum number of moves to sort the array as per the description.
  
  --------------------------------------------------------------
  
  Example:
  input array = [0,1,0,1]
  Final array = [0,0,1,1]
  Minimum moves = 1 (1 at index 1 is swapped with 0 at index 2)

  input array = [1101]
  Final array - [1110]
  Minimum moves = 1 [1 at index 2 is swapped with index 3]

'''

class Solution:
  def group(self, nums):
    return min(self.helper(nums, 0), self.helper(nums, 1))
  
  def helper(self, nums, val):
    totalSwaps = currSwaps = 0
    print('')
    for num in nums:
      if num == val: currSwaps += 1
      else         : totalSwaps += currSwaps
      print(currSwaps, totalSwaps)
    
    return totalSwaps

  
def runSolution():
  solution = Solution()
  print(solution.group(nums = [0,1,0,0]))
  # print(solution.group(nums = [0,1,1,1,0]))
  # print(solution.group(nums = [1,1,0,1]))
  # print(solution.group(nums = [1,1,0,1,1]))
  # print(solution.group(nums = [1,1,1,0,1]))
  # print(solution.group(nums = [1,0,1,0,1]))
  pass
runSolution()