'''

  There are a total of n levels to be played in the Game.
  A player can unlock a level by first completing easier levels.
  completing one level will unlock other level(s).
  The map of level complexity is defined as [B, A],
  where you need to finish level A to play level 1 8 Given hierarchy of game levels and a level X,
  output which all levels you need to finish to unlock level X. e

  For example:

  I)
  [Y,X]
  There are a total of 2 levels to complete.
  1) To choose level Y you should have finished level X.
  2) So the correct sequence order is[X,Y]

  II)
  [[X,W],[Y,W],[Z,X],[Z,Y],[U,V],[V,T]]
  There are a total of 4 levels to complete. 
  To play level Z you should have finished both levels X and Y.
  Both levels X and Y should be completed after you finished level W.
  So one correct course order is [W,X,Y,Z]

  Please give hit to solve this question
  
        W     T  
       / \    |
      X   Y   V
       \ /    |
        Z     U
'''


from collections import Counter, defaultdict, deque


class Solution:
  def unlockLevels(self, prereqs, target):
    childToParents, parentToChildren, inDegrees, sources = self.buildGraphs(prereqs)
    relevantCourses = self.getRelevantCourses(childToParents, target)
    
    queue = deque(list(sources))
    pathToTarget = []
    
    while queue:
      node = queue.popleft()
      if node not in relevantCourses: continue
      pathToTarget.append(node)
      
      for child in parentToChildren[node]:
        inDegrees[child] -= 1
        if inDegrees[child] == 0: 
          queue.append(child)
    
    return pathToTarget
    
  def getRelevantCourses(self, graph, target):
    relevantCourses = set()
    queue = deque([target])
    
    while queue:
      node = queue.popleft()
      relevantCourses.add(node)      
      for parent in graph[node]:
        queue.append(parent)        
    
    return relevantCourses
    
    
  def buildGraphs(self, prereqs):
    childToParents = defaultdict(list)
    parentToChildren = defaultdict(list)
    inDegrees = defaultdict(int)
    sources = set()
    
    for child, parent in prereqs:
      childToParents[child].append(parent)
      parentToChildren[parent].append(child)
      inDegrees[child] += 1
      sources.add(parent)
    
    for parent in list(sources):
      if parent in childToParents: sources.discard(parent)
      
    return childToParents, parentToChildren, inDegrees, sources




def runSolution():
  solution = Solution()
  print(solution.unlockLevels([
    ['Y','X']
  ], 'Y'))
  print(solution.unlockLevels([
    ['X','W'],['Y','W'],['Z','X'],['Z','Y'],['U','V'],['V','T']
  ], 'Z'))
  pass
runSolution()