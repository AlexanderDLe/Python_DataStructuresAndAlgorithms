'''

  Minimum adjacent swaps to sort an array
  [2, 4, 3, 1, 6] -- 4 swaps
  [3, 2, 1] -- 3 swaps
  [4, 7] -- 0 swap
  [7, 4] -- 1 swap

  ---------------

  [2, 4, 3, 1, 6]
  
  [2, 4, 1, 3, 6]
  [2, 1, 4, 3, 6]
  [1, 2, 4, 3, 6]
  [1, 2, 3, 4, 6]

  ----------------------------------------------------------  
  
  Count inversions in an array.
  
  1. What is an inversion?
     [3,2,1]
      ^   ^    3 is larger than 1 despite coming before 1. This is an inversion.
   
  2. If there are no inversions between two adjacent elements, then it is sorted.
     [1,2,3] <--- No inversion between two elements.
     
  3. A single swap of two adjacent elements will reduce the total number of
     inversions in the array by at most 1.
     
     [3,2,1] -> [2,3,1] 1 swap, 1 less inversion.
     
  4. You need to perform at least NI swaps of adjacent elements in order to sort the
     array where NI is the number of inversions in the array.
     
  5. We can always sort the array performing NI swaps of adjacent elements where
     NI is the number of inversions in the array.
  
  6. You can count the number of inversions using a slight modification of merge sort
     where you accumulate the inversions in the merge phase.
   
'''

from collections import defaultdict

class Solution:
  def countSwaps(self, arr):
    n = len(arr)
    temp = [0] * n
    return self.mergeSort(arr, temp, 0, n-1)
  
  def mergeSort(self, arr, temp, left, right):
    print(arr.copy(), temp.copy())
    inv_count = 0
    
    if (right > left):
        # Divide the array into two parts and call
        #_mergeSortAndCountInv()
        # for each of the parts */
        mid = int((right + left)/2)
 
        #Inversion count will be sum of inversions in
        # left-part, right-part and number of inversions
        # in merging */
        inv_count = self.mergeSort(arr, temp, left, mid)
        inv_count += self.mergeSort(arr, temp, mid+1, right)
 
        # Merge the two parts*/
        inv_count += self.merge(arr, temp, left, mid+1, right)
 
    return inv_count
  

  def merge(self, arr, temp, left, mid, right):
    inv_count = 0
    L = left #i is index for left subarray
    M = mid  #j is index for right subarray
    K = left #k is index for resultant merged subarray
 
    
    while (L <= mid - 1) and (M <= right):
        if (arr[L] <= arr[M]):
            temp[K] = arr[L]
            K += 1
            L += 1
        else:
            temp[K] = arr[M]
            K += 1
            M += 1
 
            #this is tricky -- see above explanation/
            # diagram for merge()
            inv_count = inv_count + (mid - L)
 
    # Copy the remaining elements of left subarray
    # (if there are any) to temp
    while (L <= mid - 1):
        temp[K] = arr[L]
        K += 1
        L += 1
 
    # Copy the remaining elements of right subarray
    # (if there are any) to temp
    while (M <= right):
        temp[K] = arr[M]
        K += 1
        M += 1
 
    # Copy back the merged elements to original array
    for L in range(left,right+1,1):
        arr[L] = temp[L]
 
    return inv_count
    

def runSolution():
  solution = Solution()
  print(solution.countSwaps([2, 4, 3, 1, 6]))
  # print(solution.countSwaps([3, 2, 1]))
  # print(solution.countSwaps([4, 7]))
  # print(solution.countSwaps([7, 4]))
  pass
runSolution()