'''

  797. All Paths From Source to Target

'''


class Solution:
  def allPathsSourceTarget(self, graph):
    result = []
    last = len(graph) - 1
    
    def DFS(n, res):
      if n == last:
        result.append(res.copy())
        return
      
      for next in graph[n]:
        res.append(next)
        DFS(next, res)
        res.pop()
    
    DFS(0, [0])
    return result
    
    
  
def runSolution():
  solution = Solution()
  print(solution.allPathsSourceTarget(graph = [[1,2],[3],[3],[]]))
  print(solution.allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]]))
  pass
runSolution()