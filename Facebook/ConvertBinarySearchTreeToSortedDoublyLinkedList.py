'''

  426. Convert Binary Search Tree to Sorted Doubly Linked List

  listNode -> 1 <-> 2
                    ^

         4
        /  \
       2    5
      / \
     1   3<

  

'''
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode, ListNode as Node
from _utils import printLinkedList



def treeToList(root):
  if root is None: return root
  head = Node(0)
  curr = head

  def DFS(n):
    if n is None: return
    nonlocal curr

    DFS(n.left)

    node = Node(n.val)
    curr.right = node
    node.left = curr
    curr = curr.right

    DFS(n.right)

  DFS(root)

  curr = head
  while curr and curr.right:
    curr = curr.right
  curr.right = head.right
  head.right.left = curr
  
  return head.right


def buildTree():
  t = TreeNode(4)
  t.left = TreeNode(2)
  t.right = TreeNode(5)
  t.left.left = TreeNode(1)
  t.left.right = TreeNode(3)
  return t

t = buildTree()
print(treeToList(t).val)