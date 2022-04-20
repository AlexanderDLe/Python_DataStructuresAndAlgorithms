'''

  1004. Max Consecutive Ones III

  -----------------------------------------------

  k = 2

  0  0  0
  |   | <--- If all are zeroes, we can flip them and expand our window up to k times

  
  -----------------------------------------------

  k = 2

  0  1  0
  |      | <--- If we encounter a 1, we can expand the window to account for it

  -----------------------------------------------

  k = 2

  0  1  0  0  0
        |      | <--- If we pass the 1, we don't have to shrink our window, but keep
                      track of the k flips we have used. In this case, k = -1 (ie. 2 - 3 = -1)

'''

def longestOnes(nums, k):
  L = 0
  R = 0
  maxLen = 0

  while R < len(nums):
    if nums[R] == 0: k -= 1
    R += 1

    if k < 0:
      if nums[L] == 0: k += 1
      L += 1

    maxLen = max(maxLen, R - L)

  return maxLen


print(longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))