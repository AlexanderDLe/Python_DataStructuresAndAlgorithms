'''

  2130. Maximum Twin Sum of a Linked List

    r  q  s     f
    5  4  2  1
    
    r  q  s     f
    5  4  2  1  6

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode, createList
from _utils import printLinkedList

class Solution:
  def pairSum(self, head):
    if not head: return head
    
    s = head
    f = head
    q = None
    r = None
    
    while f and f.next:
      r = q
      q = s
      s = s.next
      f = f.next
      if f: f = f.next
      q.next = r
      
    if f:
      s = s.next
      
    maxSum = 0
    while s:
      maxSum = max(maxSum, s.val + q.val)
      s = s.next
      q = q.next
    
    return maxSum
  
def runSolution():
  l1 = createList([5,4,2,1])
  
  solution = Solution()
  print(solution.pairSum(l1))
  pass
runSolution()