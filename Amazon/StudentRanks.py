'''
  My thought is also like the password one and possibly more like for this solution for #828 
  https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/224001/C%2B%2B-Solution-8ms-by-"Contribution" to come up with a O(n) one. But I also agree this one is more complicated in how to define whether the rank makes a contribute. I am not sure whether my solution is correct, but I'm sharing for references and please feel free to correct me if I am wrong.
  
  Given an array ranks of ranks of students in a school.
  
  All students need to be split into groups k. 
  Find the total 'imbalance' of all groups. 
  An imabalance of a group can be found as:

  Sorting each group in the order of their ranks.
  A group contributes to imbalance if any 2 students 
  in the sorted array have a rank difference of more than 1.

  Find the total sum of imbalance of all such groups.

  This is the example that was given :
  [4,1,3,2]

  [1]       contributes 0 to imbalance
  [2]       contributes 0 to imbalance
  [3]       contributes 0 to imbalance
  [4]       contributes 0 to imbalance
  [4,1]     contributes 1 to imbalance
  [4,3]     contributes 0 to imbalance
  [4,2]     contributes 1 to imbalance
  [4,1,3,2] contributes 0 to imbalance
  [1,3]     contributes 1 to imbalance
  [1,2]     contributes 0 to imbalance
  [3,2]     contributes 0 to imbalance

  Answer = 1 + 1 + 1 = 3


  -------------------------------------------------------------------------------------------

  Rules:

  1. Get an subarray of any possible size k (1 <= k <= n)

  2. Sort this subarray

  3. Find the imbalance of this subarray.

  4. Imbalance is defined as, for each element a[i] at index i, a[i] - a[i - 1] > 1
     Then a[i] contributes 1 imbalance. 
     
     Example: for subarry [1,5,4,7], after sorting it's [1,4,5,7]. 

     curr - prev > 1 ? contribute 1 : contribute 0

     4 - 1 > 1 = true  (contribute 1)
     5 - 4 > 1 = false (contribute 0)
     7 - 4 > 1 = true  (contribute 1)

     contribution for this subarrray = 2

  5. Find the total imbalance of all possible subarray

  -------------------------------------------------------------------------------------------

  1. To simplify the question and to avoid duplications, for each rank[i], we only focus on 
  whether it could be a contribution as a[i-1]
  
  Example: [1, 3, 5, 4, 2] 

  For 3, we only focus on [3, 5] as a contribution instead of [1, 3]. ie. Consider only next elements

  -------------------------------------------------------------------------------------------

  2. We can find a potential boundary of the possible subarrays that rank[i] could 
  make contribution to by expanding from i to left and to right, and stop as we encounter the 
  value rank[i] + 1. 
  
  In this way, we could get left and right boundary of possible start points. 

  Example:     1   3   5   4   2
              <--- 3 --->

                           v---------------- for ranks[i] = 4, ranks[i] = 1 is in index 2 (5)
  LBoundary:  -1  -1  -1   2   1
  RBoundary:   4   3   5   5   5
                   ^------------------------ for ranks[i] = 3, ranks[i] + 1 is in index 3 (4)
               ^---------------------------- for ranks[i] = 1, ranks[i] + 1 is in index 4 (2)
  
  For instance, if we focus on 3, the left boundary should be -1 and the right boundary should 
  be 3 (exclusive) since rank[3] = 4. Since if we include 4 in the sub array, 3 could not contribute 
  as a[i-1], since there must be a[i] - a[i-1] == 1 after sorting
  
  -------------------------------------------------------------------------------------------
  
  TIP: WHY DO WE USE THESE BOUNDARIES?

  Example:     1   3   5   4   2

  In the above example, the right boundary for 3 is 4 (index 3). Why?

  Because when 3 reaches 4, 4 will prevent it from contributing to any more imbalances.
  Example:

  3  5     <--- 5 - 3 > 1 = TRUE,  3 can contribute
  3  6     <--- 5 - 3 > 1 = TRUE,  3 can contribute
  3  4     <--- 4 - 3 > 1 = FALSE, 3 can no longer contribute
  3  4  6  <--- 4 - 3 > 1 = FALSE, 3 still can't contribute because it is blocked by 4 (3 + 1)

  -------------------------------------------------------------------------------------------

  3. Next, get a subarray with potential elements that our current rank could contribute to. 
  
  For instance, for 3 it is [1, 3, 5]. If we look from i and consider the start value of the 
  possible subarray that contains 3, it could be 1 or 3. And similarly the end of possible 
  sub array, it could be 3 or 5. 
  
  So there are 2 * 2 possibilities [1, 3], [3], [3, 5], [1, 3, 5]
  
  -------------------------------------------------------------------------------------------

  4. We know there are some invalid results that 3 could not contribute as a[i-1] since we 
  must ensure at least one element greater than 3 exists. 
  
  For instance, [3,5], [1,3,5] 

  are the sub arrays that 3 would contribute 1 as a[i-1], but not [1, 3] and 3. 
  
  So we would need to know index of 
  
  next_great_element_left[i]  (say, j)
  next_great_element_right[i] (say, k)
  
  If we could not find such an element, we would use -1 for left and n for right in convenience to represent.

  Example:     1   3   5   4   2
  LeftNGE     -1  -1  -1   2   3
  RightNGE     1   2   5   5   5
  
  -------------------------------------------------------------------------------------------

  5. We would further know the invalid subarray count is (i - j) * (k - i). 
  
  For our example [1, 3, 5], j = -1, k = 2, so the invalid array count should be 2 * 1 = 2, which 
  should be excluded from the value we get from #2. Since we are setting the boundary in #2. based 
  on value rank[i] + 1, we know the next great element index must be within the boundary. 
  
  Since if there are all smaller elements we will directly go to the boundary we found.
  
  -------------------------------------------------------------------------------------------

  Python initial implementation of O(n^2), which i directly used a while loop to find the next great elements: 
  https://leetcode.com/playground/Lq2bHp9T

  We could further improve the part of finding next_great_element based on solution similar to #496 , and 
  this should decrease time complexity to O(n):

'''

def buildLeftBoundary(ranks, n):
  LBoundary = [-1] * n
  dict = {}
  for i in range(n):
    rank = ranks[i]
    if (rank + 1) in dict: LBoundary[i] = dict[rank + 1]
    dict[rank] = i
    
  return LBoundary

def buildRightBoundary(ranks, n):
  RBoundary = [n] * n
  dict = {}
  for i in range(n - 1, -1, -1):
    rank = ranks[i]
    if (rank + 1) in dict: RBoundary[i] = dict[rank + 1]
    dict[rank] = i
    
  return RBoundary

def buildLeftNGE(ranks, n):
  LeftNGE = [-1] * n
  stack = []

  for i in range(n):
    rank = ranks[i]
    while stack and rank > ranks[stack[-1]]: stack.pop()
    if stack: LeftNGE[i] = stack[-1]
    stack.append(i)

  return LeftNGE

def buildRightNGE(ranks, n):
  RightNGE = [n] * n
  stack = []

  for i in range(n - 1, -1, -1):
    rank = ranks[i]
    while stack and rank > ranks[stack[-1]]: stack.pop()
    if stack: RightNGE[i] = stack[-1]
    stack.append(i)
  
  return RightNGE

def printData(LBoundary, RBoundary, NGELeft, NGERight):
  print(LBoundary)
  print(RBoundary)
  print(NGELeft)
  print(NGERight)

def studentRanks(ranks):
  n = len(ranks)

  LBoundary = buildLeftBoundary(ranks, n)
  RBoundary = buildRightBoundary(ranks, n)
  NGELeft = buildLeftNGE(ranks, n)
  NGERight = buildRightNGE(ranks, n)
  printData(LBoundary, RBoundary, NGELeft, NGERight)

  result = 0
  for i in range(n):
    countOfStart    = i - LBoundary[i]
    countOfEnd      = RBoundary[i] - i
    totalPossible   = countOfStart * countOfEnd
    smallerSubCount = (i - NGELeft[i]) * (NGERight[i] - i)
    result += (totalPossible - smallerSubCount)

  return result


print(studentRanks([1, 3, 5, 4, 2]))
# print(studentRanks([4,1,3,2]))
# print(studentRanks([8, 3, 6, 2, 4, 1, 7, 9, 5]))