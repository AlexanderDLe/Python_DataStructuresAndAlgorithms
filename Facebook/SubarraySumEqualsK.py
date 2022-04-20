'''

  560. Subarray Sum Equals K

  k = 2

  5  5  1  1
0 5 10 11 12

  set = [0, 5, 10, 11, 12]

  -----------------------------------

  k = 0

  1  -1  0
0 1   0  0
     | |      <-- One subarray
     |   |    <-- Two subarrays
        | |   <-- Three subarrays

  Since subarrays can overlap, you need to use a dict to keep track
  of occurences a particular sum


'''

def subarraySum(nums, k):
  sumSet = {0: 1}
  count = 0
  sum = 0

  for num in nums:
    sum += num
    diff = sum - k
    if diff in sumSet: count += sumSet[diff]
    sumSet[sum] = sumSet.get(sum, 0) + 1

  return count

print(subarraySum([1,1,1], 2))
print(subarraySum([1,2,3], 3))
print(subarraySum([1,-1,0], 0))