'''

  146. LRU Cache

'''
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from _utils import printLinkedList, printDict

class DoublyLinkedList:
  def __init__(self, key, val) -> None:
    self.key = key
    self.value = val
    self.prev = None
    self.next = None
  
  def unlink(self):
    self.prev = None
    self.next = None

class LRUCache:
  def __init__(self, capacity) -> None:
    self.dict = dict()
    self.capacity = capacity
    self.head = DoublyLinkedList(0, 0)
    self.tail = DoublyLinkedList(-1, -1)
    self.head.next = self.tail
    self.tail.prev = self.head

  def get(self, key) -> None:
    if key in self.dict:
      node = self.dict[key]
      self.removeFromList(node)
      self.insertIntoHead(node)
      return node.value
    else:
      return -1

  def put(self, key, val) -> None:
    if key in self.dict:
      node = self.dict[key]
      self.removeFromList(node)
      self.insertIntoHead(node)
      node.value = val
    else:
      if len(self.dict) >= self.capacity:
        self.removeFromTail()
      node = DoublyLinkedList(key, val)
      self.dict[key] = node
      self.insertIntoHead(node)

  def removeFromList(self, node):
    node.prev.next = node.next
    node.next.prev = node.prev

  def insertIntoHead(self, node):
    headNext = self.head.next
    self.head.next = node
    node.prev = self.head
    node.next = headNext
    headNext.prev = node

  def removeFromTail(self):
    if len(self.dict) == 0: return
    tailPrev = self.tail.prev
    self.removeFromList(tailPrev)
    del self.dict[tailPrev.key]




lRUCache = LRUCache(2)
lRUCache.put(1, 1)           # cache is {1=1}
lRUCache.put(2, 2)           # cache is {1=1, 2=2}
# print(lRUCache.get(1))       # return 1
lRUCache.put(3, 3)           # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))       # returns -1 (not found)
lRUCache.put(4, 4)           # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))       # return -1 (not found)
print(lRUCache.get(3))       # return 3
print(lRUCache.get(4))       # return 4