'''

  432. All O'one Data Structure

'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from _utils import printLinkedList
from collections import Counter

class DoublyLinkedList:
  def __init__(self, val, key = None):
    self.keys = set([key])
    self.freq = val
    self.val = val
    self.prev = None
    self.next = None
  def __repr__(self):
    return f'Node(freq:{self.freq}|{self.keys})'

class AllOne:
  def __init__(self):
    self.nodeMap = {}
    self.counter = Counter()
    self.head = DoublyLinkedList(float('inf'))
    self.tail = DoublyLinkedList(float('-inf'))
    self.head.next = self.tail
    self.tail.prev = self.head    

  def inc(self, key: str):
    if key in self.counter: self.addExisting(key)
    else: self.addNew(key)

  def dec(self, key: str):
    currFreq = self.counter[key]
    currNode = self.nodeMap[currFreq]
    currNode.keys.remove(key)
    newFreq = currFreq - 1
    self.counter[key] -= 1
    
    if newFreq == 0:
      del self.counter[key]
    elif newFreq in self.nodeMap:
      self.nodeMap[newFreq].keys.add(key)
    else:
      newNode = DoublyLinkedList(newFreq, key)
      self.nodeMap[newFreq] = newNode
      self.attachRight(currNode, newNode)
    
    if len(currNode.keys) == 0: 
      self.remove(currNode)
      del self.nodeMap[currFreq]

  def getMaxKey(self):
    node = self.head.next
    if node.freq == float('-inf'): return ''
    return list(node.keys)[0]

  def getMinKey(self):
    node = self.tail.prev
    if node.freq == float('inf'): return ''
    return list(node.keys)[0]
  
  def addExisting(self, key):
    currFreq = self.counter[key]
    currNode = self.nodeMap[currFreq]

    currNode.keys.remove(key)
    newFreq = currFreq + 1
    self.counter[key] += 1
    
    if newFreq in self.nodeMap:
      self.nodeMap[newFreq].keys.add(key)
    else:
      newNode = DoublyLinkedList(newFreq, key)
      self.nodeMap[newFreq] = newNode
      self.attachLeft(currNode, newNode)
    
    if len(currNode.keys) == 0:
      self.remove(currNode)
      del self.nodeMap[currFreq]
    
  
  def addNew(self, key):
    self.counter[key] = 1
    
    if 1 in self.nodeMap: 
      self.nodeMap[1].keys.add(key)
    else:
      newNode = DoublyLinkedList(1, key)
      self.nodeMap[1] = newNode
      self.attachLeft(self.tail, newNode)
  
  def attachRight(self, node, newNode):
    newNode.prev = node
    newNode.next = node.next
    node.next.prev = newNode
    node.next = newNode
    
  def attachLeft(self, node, newNode):
    newNode.next = node
    newNode.prev = node.prev
    node.prev.next = newNode
    node.prev = newNode
  
  def remove(self, node):
    node.prev.next = node.next
    node.next.prev = node.prev
  
  def print(self):
    print(self.counter)
    print(self.nodeMap)
    printLinkedList(self.head)
  


def runSolution():
  allOne = AllOne()
  allOne.inc("hello")
  allOne.inc("goodbye")
  allOne.inc("hello")
  allOne.inc("hello")
  print(allOne.getMaxKey())
  allOne.inc("leet")
  allOne.inc("code")
  allOne.inc("leet")
  allOne.dec("hello")
  allOne.dec("goodbye")
  allOne.inc("leet")
  allOne.inc("code")
  allOne.inc("code")
  print(allOne.getMaxKey())
  allOne.print()
  # ["AllOne","inc",    "inc",       "inc",     "inc","max","inc",  "inc",  "inc",    "dec",  " inc",   "inc",    "inc","getMaxKey"]
  # [[],      ["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]
  pass
runSolution()