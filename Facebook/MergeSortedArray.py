'''

  88. Merge Sorted Array

'''

def merge(nums1, m, nums2, n):
  s = m + n - 1
  m -= 1
  n -= 1

  while m >= 0 and n >= 0:
    if nums1[m] > nums2[n]:
      nums1[s], nums1[m] = nums1[m], nums1[s]
      m -= 1
    else:
      nums1[s], nums2[n] = nums2[n], nums1[s]
      n -= 1
    s -= 1
  
  while m >= 0:
    nums1[s], nums1[m] = nums1[m], nums1[s]
    m -= 1
    s -= 1

  while n >= 0:
    nums1[s], nums2[n] = nums2[n], nums1[s]
    n -= 1
    s -= 1

  return nums1



print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(merge(nums1 = [0], m = 0, nums2 = [1], n = 1))