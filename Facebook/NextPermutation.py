'''

  31. Next Permutation

  pivot can start at -1, simply sort array if there is no pivot

  1  2  3  4
        p  s

  ---------------------------------------

  1  2  4  3
     p     s
     
  1  3  4  2
     p     s    <--- swap pivot and swap
     
  1  3  4  2
     p     s    <--- reverse pivot+1:end
     
  1  3  2  4
     p     s    <--- reverse pivot+1:end
'''

def reverse(nums, L, R):
  print(nums,L, R)
  while L < R:
    nums[L], nums[R] = nums[R], nums[L]
    L += 1
    R -= 1

def nextPermutation(nums):
  n = len(nums)
  
  pivot = -1
  for i in range(0, n - 1):
    if nums[i] < nums[i + 1]: pivot = i

  swap = -1
  for i in range(0, n):
    if nums[i] > nums[pivot]: swap = i

  if pivot == -1: 
    nums.sort()
    return

  nums[pivot],nums[swap] = nums[swap],nums[pivot]
  reverse(nums, pivot + 1, n - 1)
  return


print(nextPermutation([1,2,4,3]))
print(nextPermutation([3,2,1]))
print(nextPermutation([1,1,5]))