'''

  QUESTION:
  
  You are given a tree with N vertices and N-1 edges. 
  Node 1 is the root of the tree.
  
  Each vertex of the given tree is assigned an integer value 
  given in the form of array A. 
  
  All values are distinct.
  
  You can perform the following operation on the tree:
  1. Swap the nodes that are at the same level in the tree.
  2. You need to perform the above operation such that the values, 
     when viewed from left to right at the same level, are in ascending order.

  Determine the minimum number of operations required to make all level values sorted.

  ------------------------------------------------------------------------------------

  Notes
  
  A tree is a connected acyclic graph with no self-loops and multiple edges.
  When you swap 2 nodes, the node along with its subtree gets swapped.
  
  The edges need to be added to a tree in order of input received.
  So, if edges input is (2,10) and (8,2), then if you are traversing children of node 2, 
  you must traverse node 10 first ( if not visited already) as it was present in input first.  
  
  ------------------------------------------------------------------------------------
  
  Example 1

  N = 4
  A= [ 1, 2, 3, 4 ]
  edges = [(1,3),(1,2),(3,4)]
              
  1 is the root. We add nodes from left to right.
  i = 1: We connect 3 to 1.
  i = 2: We connect 2 to 1.
  i = 3: We connect 4 to 3.
  
                  1
                /   \
               3     2        <----- Needs to be sorted in ascending order.
              /
             4

                  1
                /   \
               2     3        
                    /
                   4          Sorted with 1 swap.
  
  
  Now, the tree edges are (1, 2), (1, 3), (3, 4)
  So, Minimum swaps used = 1.
  Note: When you swap the node (2, 3), the parent of 4 will still be 3 as the whole subtree gets swapped.

  ------------------------------------------------------------------------------------

  Example 2

  N = 5
  A=[ 10, 5, 6, 4, 7]
  edges= [(1,3), (1, 2), (3, 4),(2,5)]
  
                      10
                    /    \
                   6      5     <--- Needs to be sorted
                  /      /
                 4      7
                 
                      10
                    /    \
                   5      6
                  /      /
                 7      4       <--- Needs to be sorted
                 
                      10
                    /    \
                   5      6
                  /      /
                 4      7       Sorted with 2 swaps.

  Level 1: Contains only one node with value = 10. So, it is in ascending order.
  Level 2: Contains 2 nodes with values as 6,5. So, you swap these nodes.
  Level 3: Now, level 3 values after the above swap are 7, 4. So, we swap here too.
  Total swaps = 2
  
  ------------------------------------------------------------------------------------
  
  N = 5
  A=[ 10, 5, 6, 4, 7]
  edges= [(1,3), (1, 2), (3, 4),(2,5)]
  
  AdjacencyList?
  {
    10: [6, 5]
    6: [4]
    5: [7]
  }
  
  curr = [6, 5] -> sort -> [5, 6]  
  Get children of [5, 6] in order.
  
  curr = [7, 4] -> sort -> [4, 7]
  Get children of [4, 7] in order.
  
  curr = []
  No children. Finished.
'''

from collections import defaultdict

class Solution:
  def func(self, n, vertices, edges):
    graph = self.initGraph(vertices, edges)
    totalSwaps = 0

    # curr = graph[vertices[0]]
    # minSwaps, sortedArr = self.swapSort(curr)
    
    # while curr:
    #   print('hi')
    #   break
    
    return totalSwaps
  
  def swapSort(self, nums):
    copy = sorted(nums)
    print(copy)
    
    return 0, []
    
  def initGraph(self, vertices, edges):
    graph = {}
    graph[vertices[0]] = []
    
    for i in range(len(edges)):
      x, y = edges[i]
      xVertex, yVertex = vertices[x - 1], vertices[y - 1]
      
      if xVertex in graph:
        graph[xVertex].append(yVertex)
        graph[yVertex] = []
      else:
        graph[yVertex].append(xVertex)
        graph[xVertex] = []
    
    return graph
  
def runSolution():
  solution = Solution()
  print(solution.func(
    n = 4, vertices= [ 1, 2, 3, 4 ], edges = [(1,3),(1,2),(3,4)]))
  print(solution.func(
    n = 5, vertices=[ 10, 5, 6, 4, 7], edges= [(1,3), (1, 2), (3, 4),(2,5)]))
  pass
runSolution()