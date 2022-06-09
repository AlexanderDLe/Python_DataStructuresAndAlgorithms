'''

  146. LRU Cache

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode, createList
from _utils import printLinkedList

#+ REFERENCE +#
class DoublyListNodeRef:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None

class LRUCacheRef:
  def __init__(self, capacity):
    self.nodeMap = {}
    self.head = DoublyListNodeRef(0, 0)
    self.tail = DoublyListNodeRef(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head
    self.capacity = capacity
    self.size = 0

  def get(self, key):
    if key not in self.nodeMap: return -1
    node = self.nodeMap[key]
    self.renew(node)
    return node.val

  def put(self, key, value):
    # Check if node already exists
    if key in self.nodeMap:
      node = self.nodeMap[key]
      node.val = value
      self.renew(node)
      return
    
    node = DoublyListNodeRef(key, value)
    self.nodeMap[key] = node
    
    # Put into list with room
    if self.size < self.capacity:
      self.pushHead(node)
      self.size += 1
      return
    
    # Put into list with no room
    if self.size == self.capacity:
      self.pop()
      self.pushHead(node)
      return
  
  def pushHead(self, node):
    node.prev = self.head
    node.next = self.head.next
    self.head.next = node
    node.next.prev = node
  
  def pluck(self, node):
    node.prev.next = node.next
    node.next.prev = node.prev
    node.prev = None
    node.next = None
  
  def pop(self):
    node = self.tail.prev
    node.prev.next = node.next
    node.next.prev = node.prev
    del self.nodeMap[node.key]
  
  def renew(self, node):
    self.pluck(node)
    self.pushHead(node)
#+ REFERENCE +#
    
    
class DoublyListNode:
  def __init__(self, val):
    self.val = val
    
class LRUCache:
  def __init__(self):
    pass

def runSolution():
  lRUCache = LRUCache(2)
  print(lRUCache.put(1, 1))
  print(lRUCache.put(2, 2))
  print(lRUCache.get(1))
  print(lRUCache.put(3, 3))
  print(lRUCache.get(2))
  print(lRUCache.put(4, 4))
  print(lRUCache.get(1))
  print(lRUCache.get(3))
  print(lRUCache.get(4))
  pass
runSolution()

