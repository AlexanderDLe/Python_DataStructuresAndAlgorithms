'''

  138. Copy List with Random Pointer

    7 > 13 > 11 > 10
o:  0    1    2    3
c:  7 > 13 > 11 > 10


'''
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode as Node

def copyRandomList(head):
  if head == None: return None
  originals = []
  copies = []
  p = head

  while p != None:
    originals.append(p)
    copies.append(Node(p.val))
    p = p.next

  n = len(originals)
  for i in range(n):
    orig = originals[i]
    copy = copies[i]

    if i < n - 1:
      copy.next = copies[i + 1]  

    if orig.random == None: continue
    randomNodeIndex = originals.index(orig.random)
    copy.random = copies[randomNodeIndex]
  
  return copies[0]



def buildList():
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

  return n7
head = buildList()
print(copyRandomList(head))