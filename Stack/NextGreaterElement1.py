'''

  496. Next Greater Element I
  
  1 3 4 2
  
  stack = [4, 3, 1]

'''

class Solution:
  def nextGreaterElement(self, nums1, nums2):
    indexMap = {num: i for i, num in enumerate(nums2)}
    NGE = [-1] * len(nums2)
    stack = []
    
    for i in range(len(nums2) - 1, -1, -1):
      val = nums2[i]
      while stack and val > stack[-1]: stack.pop()
      if stack: NGE[i] = stack[-1]
      stack.append(val)
    
    return list(map(lambda x: NGE[indexMap[x]], nums1))
  
  
def runSolution():
  solution = Solution()
  print(solution.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
  print(solution.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))
  pass

runSolution()