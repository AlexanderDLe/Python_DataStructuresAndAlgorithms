'''

  * NON-CONTIGUOUS

  arr = [9, 8, 7, 6, 5]
         ^  
  
  DP  = [1, 0, 0, 0, 0]
  count = 1

  --------------------------------------------------------

  arr = [9, 8, 7, 6, 5]
            ^  
  
  8 is less than 9. So we add 8 to subarrays with 9
  [9, 8]
  
  8 is itself a subarray
  [8]
  
  DP  = [1, 2, 0, 0, 0]
  count = 3

  --------------------------------------------------------

  arr = [9, 8, 7, 6, 5]
               ^  
  
  7 is less than 8. So we create all subarrays with the subarrays with 8 and add 7.
  [9,8,7], [8,7]
  
  7 is also less than 9, so we create subarrays with the result of 9 as well.
  [9,7]
  
  7 is itself a subarray.
  [7]
  
  DP  = [1, 2, 4, 0, 0]
  count = 6

  --------------------------------------------------------

  arr = [9, 8, 7, 6, 5]
                  ^  
  
  6 is less than 7. So we add 6 to all subarrays with 7
  [9,8,7,6], [8,7,6], [7,6]
  
  6 is also less than 8, so we add 6 to all subarrays with 8
  [9,8,6], [8,6]
  
  6 is also less than 9, so we add 6 to all subarrays with 9
  [9, 6]
  
  6 is itself a subarray.
  [6]
  
  DP  = [1, 2, 4, 7, 0]
  count = 6

  --------------------------------------------------------

  Return the number of contiguous subarrays with elements in strictly decreasing order.

'''


from collections import defaultdict

class Solution:
  def countSubarrays(self, nums):
    n = len(nums)
    arr = n * [1]
    count = 1
    # print(arr)
    
    for i in range(1, n):
      for j in range(i - 1, -1, -1):
        # print(nums[i], nums[j])
        if nums[i] < nums[j]:
          arr[i] += arr[j]
        # print(arr)
      
      count += arr[i]
    
    return count

def runSolution():
  solution = Solution()
  print(solution.countSubarrays([9, 8, 7, 6, 5]))
  # print(solution.countSubarrays([10, 10, 10]))
  pass
runSolution()
