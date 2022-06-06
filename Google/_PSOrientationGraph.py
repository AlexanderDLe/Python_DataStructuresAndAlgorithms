'''
  https://leetcode.com/discuss/interview-question/2090581/Google-or-Phone-Interview-or-Points-in-2D-Plane

  Input
  P1 N P2
  P2 N P3
  P3 S P1

  Output
  true

  Explanation
  The first statement "point P2 is to the north of point P1" is valid, because that's the only statement we know about any of the points in the 2D plane.
  The second statement "point P3 is to the north of P2" is also valid, as it does not contradicts with any of the previous statements.
  The third statement "point P1 is to the south of P3" is also valid, by transitive property.
'''


from collections import defaultdict, deque


class SolutionRef:
  def canTransform(self, rels):
    setOfPoints = set()
    graphNS, graphEW = defaultdict(list), defaultdict(list)
    
    for rel in rels:
      first, coords, second = rel.split(' ')
      setOfPoints.add(first)
      setOfPoints.add(second)
      if 'N' in coords: graphNS[first].append(second)
      if 'S' in coords: graphNS[second].append(first)
      if 'E' in coords: graphEW[first].append(second)
      if 'W' in coords: graphEW[second].append(first)
              
    def cycleCheck(graph):
      VISITING, VISITED, states = 1, 2, {k:0 for k in setOfPoints}
      
      def detectCycle(node):
        if states[node] == VISITING: return True 
        states[node] = VISITING 

        for nextNode in graph[node]:
          if states[nextNode] != VISITED:
            if detectCycle(nextNode): return True

        states[node] = VISITED 
        return False

      for node in set(graph.keys()):
        if states[node] != VISITED:
          if detectCycle(node): return False
            
      return True
    
    return cycleCheck(graphNS) and cycleCheck(graphEW)
    
  
class Solution:
  def canTransform(self, rels):
    UNVISITED, VISITING, VISITED = 0, 1, 2, 
    graphNS, graphEW, allPoints = self.buildGraph(rels)
    
    def findCycle(graph):
      states = {p:UNVISITED for p in allPoints}
      
      def foundCycle(node):
        if states[node] == VISITING: return True
        states[node] = VISITING
        
        for next in graph[node]:
          if states[next] != VISITED:
            if foundCycle(next): return True
        
        states[node] = VISITED
        return False
    
      for node in list(graph.keys()):
        if states[node] == UNVISITED and foundCycle(node): return False
      
      return True
    
    
    return findCycle(graphNS) and findCycle(graphEW)
  
  def buildGraph(self, rels):
    graphNS, graphEW = defaultdict(list), defaultdict(list)
    allPoints = set()
    
    for rel in rels:
      p1, dir, p2 = rel.split(' ')
      allPoints.add(p1)
      allPoints.add(p2)
      if 'N' in dir: graphNS[p1].append(p2)
      if 'S' in dir: graphNS[p2].append(p1)
      if 'E' in dir: graphEW[p1].append(p2)
      if 'W' in dir: graphEW[p2].append(p1)
    
    return graphNS, graphEW, allPoints
    


def runSolution():
  solution = Solution()
  # print(solution.canTransform(
  #   rels = ['P1 N P2', 'P2 S P3', 'P1 E P3', 'P3 NW P4', 'P5 SW P4', 'P1 W P5', 'P1 NW P3']))
  # print(solution.canTransform(
  #   rels = ['P1 N P2', 'P2 S P3', 'P1 E P3', 'P3 NW P4', 'P5 SW P4', 'P1 W P5']))
  print(solution.canTransform(
    rels = ['P1 N P2', 'P2 N P3', 'P1 S P3']))
  print(solution.canTransform(
    rels = ['P1 N P2', 'P2 N P3', 'P3 S P1']))
  pass
runSolution()