'''

  138. Copy List with Random Pointer

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode as Node, createList
from _utils import printLinkedList


class Solution:
  def copyRandomList(self, head):
    if not head: return None
    
    origs  = []
    copies = []
    
    i = 0
    while head:
      origs.append(head)
      copies.append(Node(head.val))
      if i > 0: copies[i - 1].next = copies[i]
      
      head = head.next
      i += 1
    
    for orig, copy in zip(origs, copies):
      if orig.random == None: continue
      
      randIndex = origs.index(orig.random)
      copy.random = copies[randIndex]
    
    return copies[0]
  

def runSolution():
  n7  = Node(7)
  n13 = Node(13)
  n11 = Node(11)
  n10 = Node(10)
  n1  = Node(1)

  n7.next = n13
  n7.random = None
  n13.next = n11
  n13.random = n7
  n11.next = n10
  n11.random = n1
  n10.next = n1
  n10.random = n11
  n1.next = None
  n1.random = n7

  solution = Solution()
  printLinkedList(n7)
  printLinkedList(solution.copyRandomList(n7))
  pass
runSolution()

