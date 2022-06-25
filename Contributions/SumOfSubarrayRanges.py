'''

  2104. Sum of Subarray Ranges

  You are given an integer array nums. 
  
  The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

  Return the sum of all subarray ranges of nums.

  A subarray is a contiguous non-empty sequence of elements within an array.

  -----------------------------------------------------------------------------------

  Ex1.

  Input: nums = [1,2,3]
  Output: 4

  Explanation: The 6 subarrays of nums are the following:
  [1]      range = largest - smallest = 1 - 1 = 0 
  [2]      range = 2 - 2 = 0
  [3]      range = 3 - 3 = 0
  [1,2]    range = 2 - 1 = 1
  [2,3]    range = 3 - 2 = 1
  [1,2,3]  range = 3 - 1 = 2

  So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

  ----------------------------------------------------------------------------------

  res = sum(A[i] * F(i))
  
  F(i) = the number of subarrays,
  A[i] = the minimum.

  To get F(i), we need to find out:

  left[i]  : the length of strict bigger numbers on the left of A[i],
  right[i] : the length of bigger numbers on the right of A[i].

  Then:
  
  left[i]  + 1 equals to the number of subarray ending with A[i] and A[i] is single minimum.

  right[i] + 1 equals to the number of subarray starting with A[i] and A[i] is the first minimum.

  Finally F(i) = (left[i] + 1) * (right[i] + 1)

  ----------------------------------------------------------------------------------

  Example:
  
  3   1   2   4

  left  + 1 = [1,2,1,1]
  right + 1 = [1,3,2,1]
  
  f = [1,6,2,1]
  res = 3 * 1 + 1 * 6 + 2 * 2 + 4 * 1 = 17

'''

def printAll(arr, PLE, NLE, PGE, NGE):
  print('arr')
  print(arr)
  print('PLE')
  print(PLE)
  print('NLE')
  print(NLE)
  print('PGE')
  print(PGE)
  print('NGE')
  print(NGE)
  
class SolutionRef:  
  def sumOfSubarrayRanges(self, arr):
    getStackTop = lambda st: arr[st[-1]]

    n = len(arr)
    NGE = [-1] * n
    PGE = [-1] * n
    NLE = [-1] * n
    PLE = [-1] * n
    
    st = []
    for i in range(n):
        while st and getStackTop(st) > arr[i]:
            NLE[st[-1]] = i
            st.pop()   
        st.append(i)
        
    st = []
    for i in range(n-1,-1,-1):
        while st and getStackTop(st) >= arr[i]:
            PLE[st[-1]] = i
            st.pop()
        st.append(i)
        
    st = []
    for i in range(n):
        while st and getStackTop(st) < arr[i]:
            NGE[st[-1]] = i
            st.pop()   
        st.append(i)
        
    st = []
    for i in range(n-1,-1,-1): 
        while st and getStackTop(st) <= arr[i]:
            PGE[st[-1]] = i
            st.pop()
        st.append(i)
    
    printAll(arr, PLE, NLE, PGE, NGE)
    
    minRes = 0  
    for i in range(n):
        if PLE[i] == -1: leftDiff = i
        else           : leftDiff = (i - PLE[i]) - 1
            
        if NLE[i] == -1: rightDiff = n - 1 - i
        else           : rightDiff = (NLE[i] - i) - 1
        
        # print(f'arr[i]: {arr[i]} | leftDiff: {leftDiff} | rightDiff: {rightDiff} | ', arr[i] * (leftDiff + 1) * (rightDiff + 1))
        minRes += arr[i] * (leftDiff + 1) * (rightDiff + 1)
    # print(f'minRes: {minRes}')

    maxRes = 0
    for i in range(n):
        if PGE[i] == -1: leftDiff = i
        else           : leftDiff = (i - PGE[i]) - 1
            
        if NGE[i] == -1: rightDiff = n - 1 - i
        else           : rightDiff = (NGE[i] - i) - 1
        
        maxRes += arr[i] * (leftDiff + 1) * (rightDiff + 1)
        
    return maxRes - minRes


'''
    Important note:
    
    Why do we use <= and >= for PLE and PGE but not for NLE and NGE?
    It is because we do not want duplicate results.
    
    [1,3,3]
    PLE = [-1, 0, 0]
    NLE = [3, 2, 3]
    
    [1,3,3]
     ^
    Lesser range: [1,3,3]
    
    [1,3,3]
       ^
    Lesser range: [1,3]   <--- If we extend NLE to [1,3,3], it would
                               be a duplicate of the following range.
    [1,3,3]
         ^
    Lesser range: [1,3,3]
        
      
'''
      
class Solution:
  def sumOfSubarrayRanges(self, nums):
    n = len(nums)
    PLE, NLE, PGE, NGE = self.init(nums, n)
    printAll(nums, PLE, NLE, PGE, NGE)
    minRes = maxRes = 0
    for i in range(n):
      # Calculate min res
      leftLen  = i - PLE[i]
      rightLen = NLE[i] - i
      minRes += nums[i] * (leftLen * rightLen)
      
      # Calculate max res
      leftLen  = i - PGE[i]
      rightLen = NGE[i] - i
      maxRes += nums[i] * (leftLen * rightLen)
    
    return maxRes - minRes

    
    
  def init(self, nums, n):
    getStackTop = lambda s: nums[s[-1]]
    PLE, PGE = [-1] * n, [-1] * n
    NLE, NGE = [n] * n, [n] * n
    
    Lstack = []
    Gstack = []
    for i, num in enumerate(nums):
      while Lstack and num <= getStackTop(Lstack): Lstack.pop()
      if Lstack: PLE[i] = Lstack[-1]
      Lstack.append(i)
      
      while Gstack and num >= getStackTop(Gstack): Gstack.pop()
      if Gstack: PGE[i] = Gstack[-1]
      Gstack.append(i)
    
    Lstack = []
    Gstack = []
    for i in range(n - 1, -1, -1):
      num = nums[i]
      
      while Lstack and num < getStackTop(Lstack): Lstack.pop()
      if Lstack: NLE[i] = Lstack[-1]
      Lstack.append(i)
      
      while Gstack and num > getStackTop(Gstack): Gstack.pop()
      if Gstack: NGE[i] = Gstack[-1]
      Gstack.append(i)
    
    
    return PLE, NLE, PGE, NGE
    




def runSolution():
  solution = Solution()
  # print(solution.sumOfSubarrayRanges([1,2,3]))
  print(solution.sumOfSubarrayRanges([1,3,3]))
  # print(solution.sumOfSubarrayRanges([5,3,4]))
  # print(solution.sumOfSubarrayRanges([4,-2,-3,4,1]))
  pass
runSolution()