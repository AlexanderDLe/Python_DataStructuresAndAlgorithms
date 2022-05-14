'''

  143. Reorder List


        s     f
  1  2  3  4  
  
  
        s     f
  1  2  3  4  5
  

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode, createList
from _utils import printLinkedList


class Solution:
  def reorderList(self, head):
    s = f = head
    r = q = None
    
    while f and f.next:
      q = s
      s = s.next
      f = f.next
      if f: f = f.next
    
    if f is not None: 
      q = s
      s = s.next
    q.next = None
    q = None
      
    while s:
      r = q
      q = s
      s = s.next
      q.next = r
      
    dum = ListNode(0)
    cur = dum
    p = head
    
    while p:
      cur.next = p
      p = p.next
      cur = cur.next
      
      if q:
        cur.next = q
        q = q.next
        cur = cur.next
    
    return dum.next
  

def runSolution():
  head = createList([1,2,3,4,5])
  solution = Solution()
  printLinkedList(head)
  printLinkedList(solution.reorderList(head))
  pass
runSolution()

