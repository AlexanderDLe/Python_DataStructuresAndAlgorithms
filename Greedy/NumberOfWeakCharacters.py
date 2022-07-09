'''

  1996. The Number of Weak Characters in the Game
  
'''

from bisect import bisect_left, insort_left
from collections import defaultdict


class SolutionTooSlow:
  def numberOfWeakCharacters(self, properties):
    ATDMap = defaultdict(list)
    for attack, defense in properties:
      insort_left(ATDMap[attack], defense)
    
    weakChars = 0
    properties.sort()
    sortedAttacks = sorted(list(set([x[0] for x in properties])))
    
    for i in range(len(properties)):
      currAttack, currDef = properties[i]
      
      nextAttackIndex = bisect_left(sortedAttacks, currAttack) + 1
      if nextAttackIndex == len(sortedAttacks): break
      
      for j in range(nextAttackIndex, len(sortedAttacks)):
        nextAttack = sortedAttacks[j]
        greatestDef4Atk = ATDMap[nextAttack][-1]
        
        if currAttack < nextAttack and currDef < greatestDef4Atk:
          weakChars += 1
          break
    
    return weakChars
      

class SolutionRef:
  def numberOfWeakCharacters(self, properties):
    properties.sort()
    result, maxDef = 0, -1
    ATDMap = defaultdict(list)
    
    for attack, defense in properties:
      ATDMap[attack] += [defense]
      
    for attack in sorted(list(ATDMap.keys()), reverse=True):
      defenses = ATDMap[attack]
      
      for defense in defenses:
        if defense < maxDef: result += 1
        
      for defense in defenses:
        maxDef = max(maxDef, *defenses)
      
    return result

class Solution:
  def numberOfWeakCharacters(self, properties):
    ATD = defaultdict(list)
    properties.sort(reverse=True)
    result = 0
    maxDefense = -1
    
    for attack, defense in properties:
      ATD[attack].append(defense)
      
    for attack in sorted(list(ATD.keys()), reverse = True):
      candidateDefenses = ATD[attack]
      
      # maxDefense will be associated with the higher attack scores
      # Due to the reverse sort in the beginning
      for defense in candidateDefenses:
        if defense < maxDefense: result += 1
      
      maxDefense = max(maxDefense, *candidateDefenses)
    
    return result
      
    
      


def runSolution():
  solution = Solution()
  print(solution.numberOfWeakCharacters(properties = [[5,5],[6,3],[3,6]]))
  print(solution.numberOfWeakCharacters(properties = [[1,5],[10,4],[4,3]]))
  print(solution.numberOfWeakCharacters(properties = [[2,2],[3,3]]))
  print(solution.numberOfWeakCharacters([[10,1],[5,1],[7,10],[4,1],[5,9],[6,9],[7,2],[1,10]]))
  pass
runSolution()
