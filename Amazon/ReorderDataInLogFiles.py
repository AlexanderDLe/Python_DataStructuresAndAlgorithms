'''

  937. Reorder Data in Log Files

'''

class SolutionRef:
  def reorderLogFiles(self, logs):
    digLogs = []
    letLogs = []

    for log in logs:
      word = log.split()[1]

      if word.isnumeric(): digLogs.append(log)
      else               : letLogs.append(log)
      
    # Sort by identifier first
    letLogs.sort(key = lambda log: log.split()[0])

    # Sort by body
    letLogs.sort(key = lambda log: log.split()[1:])

    return letLogs + digLogs

class Solution:
  def reorderLogFiles(self, logs):
    digLogs = []
    letLogs = []
    
    for log in logs:
      word = log.split()[-1]
      if word.isnumeric(): digLogs.append(log)
      else               : letLogs.append(log)
    
    letLogs.sort(key = lambda log: log.split()[0])
    letLogs.sort(key = lambda log: log.split()[1:])
    
    return letLogs + digLogs    
  
def runSolution():
  solution = Solution()
  print(solution.reorderLogFiles(
    ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
  print(solution.reorderLogFiles(
    ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
  pass
runSolution()
