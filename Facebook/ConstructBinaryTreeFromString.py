'''

  536. Construct Binary Tree from String

'''
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode
from _utils import preorderTraversal

def str2TreeRef(s):
  n = len(s)

  def isNum(index):
    return s[index].isnumeric() or s[index] == '-'

  def createNode(start, end):
    num = ''
    while start < n and isNum(start):
      num += s[start]
      start += 1
    
    if num == '': return None

    node = TreeNode(int(num))
    stack = []
    newStart = start
    leftNode = True

    for i in range(start, end):
      char = s[i]

      if char == '(': 
        stack.append(char)

      elif char == ')':
        stack.pop()
        if len(stack) == 0:
          if leftNode == True:
            node.left = createNode(newStart + 1, i)
            leftNode = False
          else:
            node.right = createNode(newStart + 1, i)

          newStart = i + 1

    return node

  return createNode(0, len(s))

def str2Tree(s):
  ix = s.find('(')

  if ix < 0: return TreeNode(int(s)) if s else None

  balance = 0
  for jx, char in enumerate(s):
    if char == '(': balance += 1
    if char == ')': balance -= 1
    if jx > ix and balance == 0: break

  root = TreeNode(int(s[:ix]))
  root.left  = str2Tree(s[ix + 1:jx])
  root.right = str2Tree(s[jx + 2: -1])
  return root


preorderTraversal(str2Tree('4(2(3)(1))(6(5))'))
preorderTraversal(str2Tree('4(2(3)(1))(6(5)(7))'))
preorderTraversal(str2Tree('-4(2(3)(1))(6(5)(7))'))
preorderTraversal(str2Tree('4'))
preorderTraversal(str2Tree(''))