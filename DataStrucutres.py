class TreeNode:
  def __init__(self, val=0, left=None, right=None, parent=None):
    self.val = val
    self.left = left
    self.right = right
    self.parent = parent
    self.L = left
    self.R = right
    self.P = parent
    
  def __repr__(self):
    return f'Node:{self.val}'


class ListNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.value = val
    self.left = left
    self.right = right
    self.prev = left
    self.next = right
    self.random = None
    
    
def createList(arr):
  head = ListNode(arr[0])
  curr = head
  
  for i in range(1, len(arr)):
    curr.next = ListNode(arr[i])
    curr = curr.next
  
  return head
