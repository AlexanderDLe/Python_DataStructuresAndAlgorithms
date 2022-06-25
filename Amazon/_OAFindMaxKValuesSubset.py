'''

  Given an array of size n. 
  
  Let's take s = sum of subset of array, find the maximum k values of s.
  
  For examplke n = 3 arr = {3,5,-1} 
  
  then all subset sums are s = {0,3,5,-1,8,7,2,4} and k = 3 then 
  the top 3 sum values are = {8,7,5}.


'''

from collections import deque
import heapq

class SolutionBruteForce:
  def solve(self, arr, k):
    n = len(arr)
    heap = []
    
    def subsets(index, sum):
      if index >= n:
        if len(heap) < k:
          heapq.heappush(heap, sum)
        elif sum > heap[0]:
          heapq.heappop(heap)
          heapq.heappush(heap, sum)
        return

      subsets(index + 1, sum)
      subsets(index + 1, sum + arr[index])
    
    subsets(0, 0)
    return heap


class Node:
  def __init__(self, val, index):
    self.val = val
    self.index = index
  def __repr__(self):
    return f'({self.val}-{self.index})'
  def __lt__(self, other):
    return self.val > other.val

class SolutionRef:
  def solve(self, arr, k):
    n = len(arr)
    maxSum = 0
    
    for num in arr:
      if num > 0: maxSum += num    
    
    abVals = list(map(lambda x: abs(x), arr))
    abVals.sort()
    
    print(abVals)
    print('')
    
    answer = [maxSum]
    upcoming = [Node(maxSum - abVals[0], 0)]
    
    while len(answer) < k:
      print(upcoming)
      node = heapq.heappop(upcoming)
      nextSum, i = node.val, node.index
      answer.append(nextSum)
      
      if i+1 < n:
        print('added ith: ', nextSum + abVals[i] - abVals[i + 1])
        print('no-added ith: ', nextSum - abVals[i + 1])
        print('')
        heapq.heappush(upcoming, Node(nextSum + abVals[i] - abVals[i + 1], i + 1))
        heapq.heappush(upcoming, Node(nextSum - abVals[i + 1], i + 1))
        
    return answer
  
class Solution:
  def solve(self, arr, k):
    n = len(arr)
    maxSum, absVal = self.init(arr)
    result = [maxSum]
    upcoming = [Node(maxSum - absVal[0], 0)]
    print(absVal)
    
    while len(result) < k and upcoming:
      node = heapq.heappop(upcoming)
      nextSum, i = node.val, node.index
      result.append(nextSum)
      
      if i + 1 < n:
        heapq.heappush(upcoming, Node(nextSum + absVal[i] - absVal[i + 1], i + 1))
        heapq.heappush(upcoming, Node(nextSum - absVal[i + 1], i + 1))
    
    return result
    
  def init(self, arr):
    maxSum = 0
    for num in arr:
      if num > 0: maxSum += num
    
    absVal = list(map(lambda x: abs(x), arr))
    absVal.sort()
    return maxSum, absVal
  
def runSolution():
  solution = SolutionRef()
  print(solution.solve(arr = [3,5,-1], k = 3))
  # print(solution.solve(arr = [3,5,-2], k = 4))
  pass
runSolution()