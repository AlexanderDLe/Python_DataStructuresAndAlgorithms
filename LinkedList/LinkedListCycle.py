'''

  141. Linked List Cycle

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode, createList

class Solution:
  def hasCycle(self, head):
    s = f = head
    
    while f and f.next:
      s = s.next
      f = f.next
      if f: f = f.next
      
      if s == f: return True
    
    return False
  

def runSolution():
  head = createList([1,2,3,4,5])
  head.next.next.next.next = head.next
  solution = Solution()
  print(solution.hasCycle(head))
  pass
runSolution()

