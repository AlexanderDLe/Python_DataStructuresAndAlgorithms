'''

  708. Insert Into a Sorted Circular Linked List

  3 > 5 > 1

  0
'''

import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import ListNode as Node


def insert(head, insertVal):
  # Edge case 1: head is None
  if head == None:
    head = Node(insertVal)
    head.next = head
    return head

  # Edge case 2: no next node
  if head.next == None:
    n = Node(insertVal)
    head.next = n
    n.next = head
    return head

  # Normal case: Attach node in the correct position
  node = Node(insertVal)
  curr = head
  next = head.next

  while curr:
    # If insertVal is between two node values
    if insertVal >= curr.val and insertVal <= next.val:
      curr.next = node
      node.next = next
      return head    

    # If cycle occurs in middle and insertVal is on bound edges or beyond
    if next.val < curr.val and (insertVal <= next.val or insertVal >= curr.val):
      curr.next = node
      node.next = next
      return head

    # If we make a complete cycle
    if next == head:
      curr.next = node
      node.next = next
      return head

    curr = next
    next = next.next



def buildList():
  n = Node(3)
  n.next = Node(4)
  n.next.next = Node(1)
  n.next.next.next = n

  return n
n = buildList()
print(insert(n, 2))