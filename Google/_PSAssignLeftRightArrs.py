'''

  Given an array, we need to construct 2 arrays left and right something like this:

  Ex: Array: [1,3,2]

  Left           Right
  []             [1,3,2]
  [1]            [3,2]
  [1,3]          [2]
  [1,3,2]        []
  [1,2]          [3]
  [3]            [1,2]
  [3,2]          [1]
  .
  .
  . 
  soo on
  
  I couldn't exactly remember the entire output but the let and right arrays have to be built that way.

'''

class Solution:
  def main(self, nums):
    n = len(nums)
    left = []

    def backtrack(index, arr):
      if index == n:
        left.append(arr.copy())
        return
  
      backtrack(index + 1, arr)
      arr.append(nums[index])
      backtrack(index + 1, arr)
      arr.pop()

    backtrack(0, [])
    right = left.copy()[::-1]    
    return (left, right)
      


  
def runSolution():
  solution = Solution()
  print(solution.main([1,3,2]))
  pass
runSolution()