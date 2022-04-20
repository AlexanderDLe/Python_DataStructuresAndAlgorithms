'''

  23. Merge K Sorted Lists

'''
import heapq
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode
from _utils import printLinkedList

class HeapNode:
  def __init__(self, listNode) -> None:
    self.listNode = listNode

  def __lt__(self, other):
    return self.listNode.val < other.listNode.val

def mergeKLists(lists):
  heap = []

  for list in lists:
    if list != None: heapq.heappush(heap, HeapNode(list))

  dum = ListNode(0)
  curr = dum

  while len(heap) > 0:
    top = heapq.heappop(heap).listNode
    curr.next = top
    curr = curr.next
    top = top.next

    if top != None: heapq.heappush(heap, HeapNode(top))

  return dum.next



def buildLists():
  l1 = ListNode(1)
  l1.next = ListNode(4)
  l1.next.next = ListNode(5)

  l2 = ListNode(1)
  l2.next = ListNode(3)
  l2.next.next = ListNode(4)

  l3 = ListNode(2)
  l3.next = ListNode(6)

  return (l1, l2, l3)

l1, l2, l3 = buildLists()
# printLinkedList(mergeKLists([l1, l2, l3]))
printLinkedList(mergeKLists([]))