'''

  332. Reconstruct Itinerary

'''

from collections import Counter, defaultdict, deque
from functools import cmp_to_key
from itertools import product

class SolutionRef:
  def findItinerary(self, tickets):
    tickets.sort()
    
    graph = defaultdict(list)
    for source, destination in tickets:
      graph[source].append(destination)
    
    def DFS(src):
      if len(result) == len(tickets) + 1: return True
      if src not in graph: return False
    
      for i, node in enumerate(graph[src]):
        graph[src].pop(i)
        result.append(node)
        
        if DFS(node): return True
        
        graph[src].insert(i, node)
        result.pop()
      
      return False
    
    result = ['JFK']
    DFS('JFK')
    return result

  
class Solution1:
  def findItinerary(self, tickets):
    tickets.sort()
    
    graph = defaultdict(list)
    for source, dest in tickets:
      graph[source].append(dest)
    
    def DFS(source):
      if len(result) == len(tickets) + 1: return True
      if len(graph[source]) == 0: return False
      
      for i, dest in enumerate(graph[source]):
        result.append(dest)
        graph[source].pop(i)
        
        if DFS(dest): return True
        
        result.pop()
        graph[source].insert(i, dest)
      
      return False
    
    result = ['JFK']
    DFS('JFK')
    return result
  
  
  
class Solution:
  def findItinerary(self, tickets):
    graph = self.buildGraph(tickets)
    result = ['JFK']
    
    def DFS(src):
      if len(result) == len(tickets) + 1: return True
      
      for i, dst in enumerate(graph[src]):
        result.append(dst)
        graph[src].pop(i)
        
        if DFS(dst): return True
        
        result.pop()
        graph[src].insert(i, dst)
      
      return False
    
    DFS('JFK')
    return result
    
    
  def buildGraph(self, tickets):
    tickets.sort()
    graph = defaultdict(list)
    
    for src, dst in tickets:
      graph[src].append(dst)
    
    return graph


  
def runSolution():
  solution = Solution()
  print(solution.findItinerary(
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
  print(solution.findItinerary(
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
  print(solution.findItinerary(
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
  pass
runSolution()