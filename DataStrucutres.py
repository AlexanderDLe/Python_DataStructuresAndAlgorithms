class TreeNode:
  def __init__(self, val=0, left=None, right=None, parent=None):
    self.val = val
    self.left = left
    self.right = right
    self.parent = parent
    self.L = left
    self.R = right
    self.P = parent


class ListNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.value = val
    self.left = left
    self.right = right
    self.prev = left
    self.next = right
    self.random = None