'''

  2. Add Two Numbers

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode, createList
from _utils import printLinkedList


class Solution1:
  def addTwoNumbers(self, l1, l2):
    dum = ListNode(0)
    cur = dum
    carry = 0
    
    while carry or l1 or l2:
      val1 = l1.val if l1 else 0
      val2 = l2.val if l2 else 0
      sum = val1 + val2 + carry
      
      carry = sum//10
      sum   = sum %10
      cur.next = ListNode(sum)
      
      if l1: l1 = l1.next
      if l2: l2 = l2.next
      cur = cur.next
      
    
    return dum.next
  
  
class Solution:
  
  '''
    Time Complexity : O(n) 1 Pass through both lists
    Space Complexity: O(n) n is the length of the longest list
  '''
  
  def addTwoNumbers(self, l1, l2):
    dum = ListNode(0)
    curr = dum
    carry = 0
    
    while l1 or l2 or carry:
      val1 = l1.val if l1 != None else 0
      val2 = l2.val if l2 != None else 0
      
      sum = val1 + val2 + carry
      carry = sum // 10
      sum %= 10
      
      curr.next = ListNode(sum)
      curr = curr.next
      
      if l1: l1 = l1.next
      if l2: l2 = l2.next
      
    return dum.next
  

def runSolution():
  l1 = createList([2,4,3])
  l2 = createList([5,6,4])
  
  solution = Solution()
  printLinkedList(solution.addTwoNumbers(l1, l2))
  pass
runSolution()

