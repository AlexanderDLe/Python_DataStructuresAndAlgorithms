'''

  19. Remove Nth Node From End of List

  D > 1 > 2 > 3 > 4 > 5
             s        f

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode, createList
from _utils import printLinkedList


class Solution:
  def removeNthFromEnd(self, head, n):
    dum = ListNode(0)
    dum.next = head
    s = f = dum
    
    while n:
      f = f.next
      n -= 1
    
    while f and f.next:
      s = s.next
      f = f.next
    
    s.next = s.next.next
    
    return dum.next
  

def runSolution():
  head = createList([1,2,3,4,5])
  solution = Solution()
  printLinkedList(head)
  printLinkedList(solution.removeNthFromEnd(head, 2))
  pass
runSolution()

