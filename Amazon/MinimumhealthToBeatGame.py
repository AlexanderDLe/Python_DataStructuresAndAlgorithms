'''

  2214. Minimum Health to Beat Game

'''


class Solution:
  def minimumHealth(self, damage, armor):
    totalDamage = sum(damage)
    maxDamage = max(damage)
    
    mitigatedDamage = max(0, maxDamage - armor)
    
    totalDamageAfterMitigation = totalDamage - maxDamage + mitigatedDamage
    minimumRequireHealth = totalDamageAfterMitigation + 1
    return minimumRequireHealth
    
  
def runSolution():
  solution = Solution()
  print(solution.minimumHealth(damage = [2,7,4,3], armor = 4))
  print(solution.minimumHealth(damage = [2,5,3,4], armor = 7))
  pass
runSolution()
