'''

  88. Merge Sorted Array

'''


class Solution:
  
  '''
  
    Time Complexity
    O(n) Iterate through all numbers
    
    Space Complexity
    O(1) Not utilizing any scaling data structures
  
  '''
  
  def merge(self, nums1, m, nums2, n):
    p = m + n - 1
    m -= 1
    n -= 1
    
    while p >= 0:
      if   n < 0: 
        break
      
      elif m < 0:
        nums1[p] = nums2[n]
        n -= 1
        
      elif nums1[m] > nums2[n]:
        nums1[p] = nums1[m]
        m -= 1
        
      elif nums1[m] <= nums2[n]:
        nums1[p] = nums2[n]
        n -= 1
        
      p -= 1
    
    return nums1
  
def runSolution():
  solution = Solution()
  print(solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
  print(solution.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
  print(solution.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))
  pass
runSolution()
