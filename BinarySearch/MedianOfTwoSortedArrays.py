'''

  4. Median of Two Sorted Arrays

'''

class Solution:
  def findMedianSortedArrays(self, nums1, nums2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    
    if len(B) < len(A): A, B = B, A
    
    L, R = 0, len(A) - 1
    
    while True:
      i = (L + R) // 2 # A
      j = half - i - 2
      
      Aleft = A[i] if i >= 0 else float('-inf')
      Aright = A[i + 1] if i+1 < len(A) else float('inf')
      Bleft = B[j] if j >= 0 else float('-inf')
      Bright = B[j + 1] if j+1 < len(B) else float('inf')
      
      if Aleft <= Bright and Bleft <= Aright:
        # Odd
        if total % 2: return min(Aright, Bright)
        # Even
        return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
      
      elif Aleft > Bright:
        R = i - 1
      else:
        L = i + 1
        
      
      
      
      
      
    
  
  
def runSolution():
  solution = Solution()
  print(solution.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
  print(solution.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
  pass
runSolution()
