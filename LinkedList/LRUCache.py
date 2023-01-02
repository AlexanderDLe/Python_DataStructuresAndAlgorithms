'''

  146. LRU Cache

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import ListNode, createList

#+ REFERENCE +#
class LRUCacheRef:
  class DoublyListNode:
    def __init__(self, key, val):
      self.key = key
      self.val = val
      self.prev = None
      self.next = None
      
  def __init__(self, capacity):
    self.nodeMap = {}
    self.head = self.DoublyListNodeRef(0, 0)
    self.tail = self.DoublyListNodeRef(0, 0)
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
    
    node = self.DoublyListNodeRef(key, value)
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
    

class LRUCache:
  
  class DoublyListNode:
    def __init__(self, key, val):
      self.key = key
      self.val = val
      self.prev = None
      self.next = None
      
    def detach(self):
      self.prev.next = self.next
      self.next.prev = self.prev
      self.prev = None
      self.next = None
      
    def attach(self, prev, next):
      self.prev = prev
      self.next = next
      prev.next = self
      next.prev = self
      
      
  def __init__(self, capacity):
    self.capacity = capacity
    self.count = 0
    self.head = self.DoublyListNode(0, 0)
    self.tail = self.DoublyListNode(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head
    self.nodeMap = {}
    
  def put(self, key, value):
    # If node already exists, just update
    if key in self.nodeMap:
      node = self.nodeMap[key]
      node.val = value
      self.renew(node)
      return
    
    # If not doesn't exist, create node and map entry
    node = self.DoublyListNode(key, value)
    self.nodeMap[key] = node
    
    # If capacity reached, remove last node - otherwise just add
    if self.count < self.capacity:
      self.push(node)
      self.count += 1
    else:
      self.pop()
      self.push(node)
  
  def get(self, key):
    if key not in self.nodeMap: return -1
    
    self.renew(self.nodeMap[key])
    return self.nodeMap[key].val
  
  def push(self, node):
    node.attach(self.head, self.head.next)
  
  def pop(self):
    poppedNode = self.tail.prev
    poppedNode.detach()
    del self.nodeMap[poppedNode.key]
  
  def renew(self, node):
    node.detach()
    self.push(node)
  

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

