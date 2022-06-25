'''

  420. Strong Password Checker

'''



from itertools import groupby

from pkg_resources import require


class Solution:
  lowercase = set('abcdefghijklmnopqrstuvwxyz')
  uppercase = set('ABCDEFGHIJKLMNOPQRSTUFVWXYZ')
  digit     = set('0123456789')
  
  def strongPasswordChecker(self, s):
    # Check rule 2
    replacesRequired = 3
    if any(c in self.lowercase for c in s): replacesRequired -= 1
    if any(c in self.uppercase for c in s): replacesRequired -= 1
    if any(c in self.digit     for c in s): replacesRequired -= 1
    
    # Check rule 1
    requiredInserts = max(0, 6 - len(s))
    requiredDeletes = max(0, len(s) - 20)
    
    # Check rule 3
    # Convert s to list of repititions for us to manipulate
    # For s = '11aaabB', we have groups = [2,3,1,1]
    groups = []
    for _, group in groupby(s):
      groups.append(len(list(group)))
    
    # Apply deletions iteratively and always choose the best one.
    # This should be fine for short passwords.
    # A delete is better the closer it gets us to removing a group of 3.
    # Thus, a group needs to be larger than 3 and minimal wrt modulo 3.
    def applyBestDelete():
        # print(list(enumerate(groups)))
        # print(min(enumerate(groups), key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1]))
        minIndex, _ = min(
            enumerate(groups),
            # Ignore groups of length < 3 as long as others are available.
            key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1],
        )
        groups[minIndex] -= 1
    
    for _ in range(requiredDeletes):
        applyBestDelete()
      
    groupReplacesRequired = sum(group // 3 for group in groups)    
    return (requiredDeletes + max(replacesRequired, groupReplacesRequired, requiredInserts))
  

def runSolution():
  solution = Solution()
  print(solution.strongPasswordChecker("a"))
  print(solution.strongPasswordChecker("aA1"))
  print(solution.strongPasswordChecker("1337C0d3"))
  print(solution.strongPasswordChecker("13333777C000ddddddd3333333"))
  # print(solution.strongPasswordChecker("11aaabB"))
  pass
runSolution()
