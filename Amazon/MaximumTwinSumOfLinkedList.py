'''

  2130. Maximum Twin Sum of a Linked List

  Evens:
          s       f
  1 > 2 > 3 > 4 
  
  Odds:
          s       f
  1 > 2 > 3 > 4 > 5
  
'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode as Node, createList
from _utils import printLinkedList

class Solution:
  def pairSum(self, head):
    maxSum = 0
    
    r, q, s, f = None, None, head, head
    
    while f and f.next:
      r = q
      q = s
      s = s.next
      f = f.next
      q.next = r
      if f: f = f.next
      
    if f:
      maxSum = s.val
      s = s.next
      
    while q and s:
      maxSum = max(maxSum, q.val + s.val)
      q = q.next
      s = s.next
    
    return maxSum
  
  
  
def runSolution():
  evens = createList([5,4,2,1])
  odds = createList([5,4,3,2,1])

  solution = Solution()
  print(solution.pairSum(evens))
  print(solution.pairSum(odds))

runSolution()