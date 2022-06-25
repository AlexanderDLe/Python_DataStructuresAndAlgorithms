'''

  2214. Minimum Health to Beat Game

  [2,7,4,3] armor = 4
  
  7 is highest damage taken in one round.
  4 is armor value.
  
  MitigatedDamage = 7 - 4 = 3
  
  If 3 was highest damage, then bound is damage.
  MitigatedDamage = 3 - 4 should be 3. max(maxDamage - armor, maxDamage)
  
'''


class SolutionRef:
  def minimumHealth(self, damage, armor):
    totalDamage = sum(damage)
    maxDamage = max(damage)
    
    mitigatedDamage = max(0, maxDamage - armor)
    
    totalDamageAfterMitigation = totalDamage - maxDamage + mitigatedDamage
    minimumRequireHealth = totalDamageAfterMitigation + 1
    return minimumRequireHealth
    
class Solution:
  def minimumHealth(self, damage, armor):
    totalDamage = sum(damage)
    maxDamage = max(damage)
    damageTakenForMax = max(maxDamage - armor, 0)
    damageMitigated = maxDamage - damageTakenForMax
    
    return totalDamage - damageMitigated + 1
    
  
def runSolution():
  solution = Solution()
  print(solution.minimumHealth(damage = [2,7,4,3], armor = 4))
  print(solution.minimumHealth(damage = [2,5,3,4], armor = 7))
  pass
runSolution()
