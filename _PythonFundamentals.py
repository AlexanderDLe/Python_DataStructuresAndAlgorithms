from functools import cmp_to_key
import heapq
import math
from operator import itemgetter

##################################################
# ?Allow subdirectories to import from parent

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from _utils import *
from DataStrucutres import TreeNode, ListNode

##################################################
# ?Template for Python Solutions

class Solution:
  def func(self, s):
    pass
  
def runSolution():
  solution = Solution()
  print(solution.func('s'))
  pass
runSolution()

###################################################

def listOfDicts():
  my_list = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]

  my_list.sort(key=lambda k : k['name'])
  print(my_list)

  my_list.sort(key=lambda k : k['name'], reverse=True)
  print(my_list)

  my_list.sort(key=lambda k : k['age'])
  print(my_list)
# listOfDicts()
  
def frequencyMap():
  myList = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
  map = {}

  for num in myList:
    map[num] = map.get(num, 0) + 1

  print(map)
# frequencyMap()

def mathFunctions():
  print('--- Math Functions ---')
  
  print('Math.floor of 3.5: ', math.floor(3.5))

  myList = [1,2,3]
  print('myList: ', myList)

  print('Sum of myList: ', sum(myList))

  print('Length of myList: ', len(myList))

  print('Absolute value abs(-5):', abs(-5))
# mathFunctions()

def iterating():
  nums = [2,4,7,2,9]

  # for num in nums:
  #   print(num)

  # for num in nums[1:]:
  #   print(num)

  # range(start, stop, step)
  # start	Optional. An integer number specifying at which position to start. Default is 0
  # stop	Required. An integer number specifying at which position to stop (not included).
  # step	Optional. An integer number specifying the incrementation. Default is 1

  res = ''
  for i in range(len(nums) - 1, -1, -1):
    res += ' ' + str(nums[i])
  print(f'Iterating Backward: {res}')

  res = ''
  for i in range(0, len(nums)):
    res += ' ' + str(nums[i])
  print(f'Iterating forward:  {res}')

  res = ''
  for i in range(2, 4):
    res += ' ' + str(nums[i])
  print(f'Iterating partial:  {res}')
# iterating()

class Node(object):
  def __init__(self, obj) -> None:
    self.obj = obj

  def __repr__(self):
    return f'Node value: {self.obj}'

  def __lt__(self, other: object):
    if self.obj['val'] == other.obj['val']:
      return self.obj['key'] < other.obj['key']
    return self.obj['val'] < other.obj['val']


def priorityQueue():
  items = [
    { 'val': 4, 'key': 4 },
    { 'val': 3, 'key': 5 },
    { 'val': 2, 'key': 2 },
    { 'val': 2, 'key': 1 },
    { 'val': 5, 'key': 2 },
  ]
  
  heap = []
  for item in items:
    heapq.heappush(heap, Node(item))

  print(heap)
  print(heapq.heappop(heap))
  print(heap)
  print(heapq.heappop(heap))
  print(heap)
# priorityQueue()
  
def dictionaries():
  dict = {}
  dict.update({'hi':'hello'})
  dict.update({'hi2':'hello2'})
  dict.update({1: 'test'})

  if 1 in dict: print('yahoo')

  print(dict)
  print(dict.keys())

  dictArr = {'indexes': []}
  print(dictArr['indexes'])

  d1 = { 'd2': { 'd3': {}}}
  print('a' not in d1)
# dictionaries()

def sortDicts():
  orders = {
    'cappuccino': 54,
    'latte': 56,
    'espresso': 72,
    'americano': 48,
    'cortado': 41
  }
  sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
  print(sort_orders)
# sortDicts()

def slicing():
  a = ['abcdefgh', 'abcdefgh' , 'abcdefgh']
  b = [1, 2, 3, 4, 5, 6, 7]
  print(a[0][3:6])
  print(b[2:4])
  print(b[6:10])

  testStr = 'badsrfeawd'
  print(testStr[3:])
# slicing()

def finding():
  string = 'dig1 8 1 5 1'
  print(string.find('1'))
  print(string.find('8 1'))
# finding()

def compare(a, b):
  aCode, bCode = a[0], b[0]
  aFreq, bFreq = a[1]['frequency'], b[1]['frequency']

  if aFreq == bFreq:
    if aCode < bCode: return -1
    else            : return 1

  return bFreq - aFreq
sortedItems = sorted({'testItem': ['asdf']}, key=cmp_to_key(compare))


def mapFunction():
  def addition(n):
      return n + n
    
  # We double all numbers using map()
  numbers = (1, 2, 3, 4)
  result = map(addition, numbers)
  print(list(result))

# mapFunction()



def mySortTester():
  myList = [(2, 'i'), (1, 'hi'), (2, 'heya'), (2, 'hello'), (1, 'bye'), (3, 'cya')]
  print('Given list.')
  print(myList)
  myList.sort(key=itemgetter(1))
  print('Step1. Sort by word first.')
  print(myList)
  print('Step2. Sort by freq next.')
  myList.sort(key=itemgetter(0), reverse=True)
  print(myList)

mySortTester()