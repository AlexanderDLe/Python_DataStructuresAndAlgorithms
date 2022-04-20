'''

  133. Clone Graph

'''

class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
  if node == None: return None
  nodeMap = {}

  def DFS(n):
    if n.val in nodeMap: return nodeMap[n.val]

    copy = Node(n.val)
    nodeMap[n.val] = copy

    for nb in n.neighbors:
      copy.neighbors.append(DFS(nb))

    return copy


  return DFS(node)


def buildGraph():
  n1 = Node(1)
  n2 = Node(2)
  n3 = Node(3)
  n4 = Node(4)
  n1.neighbors = [n2, n4]
  n2.neighbors = [n1, n3]
  n3.neighbors = [n2, n4]
  n4.neighbors = [n1, n3]
  return n1

print(cloneGraph(buildGraph()))