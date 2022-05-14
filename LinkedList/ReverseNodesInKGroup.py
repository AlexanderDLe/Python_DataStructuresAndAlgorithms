'''

  23. Merge K Sorted Lists
  
'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode, createList
from _utils import printLinkedList


class Solution:
  def reverseKGroup(self, head, k):
    if not head: return head
    
    self.k = k
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    
    while curr and curr.next:
      if self.checkForKNodes(curr) == False: break
      curr = self.reverseKNodes(curr)
    
    return dummy.next
  
  def reverseKNodes(self, start):
    end = p = start.next
    r = q = None
    i = 0
    
    # Mistake: while p because you want p to go out of bounds when reversing
    while i < self.k and p:
      r = q
      q = p
      p = p.next
      q.next = r
      i += 1
      
    end.next = p
    start.next = q
    return end
  
  def checkForKNodes(self, node):
    i = 0
    while i < self.k and node and node.next:
      node = node.next
      i += 1
    return i == self.k
  

def runSolution():
  solution = Solution()
  printLinkedList(solution.reverseKGroup(createList([1,2]), 2))
  printLinkedList(solution.reverseKGroup(createList([1,2,3,4,5]), 2))
  printLinkedList(solution.reverseKGroup(createList([1,2,3,4,5]), 3))
  pass
runSolution()

