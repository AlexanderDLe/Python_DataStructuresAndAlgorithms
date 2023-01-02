'''

  2178. Maximum Split of Positive Even Integers

'''


class SolutionMineTooSlow:
  def maximumEvenSplit(self, finalSum):
    if finalSum % 2 or finalSum == 0: return []
    DP = {}
    
    def DFS(sum, prevInteger, subarr):
      if (sum) in DP: return DP[(sum)]
      if sum == finalSum: return subarr
      if sum >= finalSum: return []
      
      res = []
      for i in range(prevInteger + 2, finalSum + 2, 2):
        subarr.append(i)
        
        arr = DFS(sum + i, i, subarr)
        if len(arr) > len(res): res = arr.copy()
        
        subarr.pop()
      
      DP[(sum)] = res
      return res
    
    result = DFS(0, 0, [])
    print(DP)
    return result
  
  
class SolutionRef:
  def maximumEvenSplit(self, finalSum):
    if finalSum % 2: return []
    
    ans  = []
    curr = 2
    
    while curr <= finalSum:
      ans.append(curr)
      finalSum -= curr
      curr += 2
      print(ans)
      
    ans[-1] += finalSum
    return ans
  
  
class Solution:
  def maximumEvenSplit(self, finalSum):
    if finalSum % 2: return []
    
    result = []
    curr = 2
    
    while curr <= finalSum:
      result.append(curr)
      finalSum -= curr
      curr += 2
    
    result[-1] += finalSum
    return result
    
  
def runSolution():
  solution = Solution()
  print(solution.maximumEvenSplit(finalSum = 12))
  print(solution.maximumEvenSplit(finalSum = 18))
  print(solution.maximumEvenSplit(finalSum = 7))
  print(solution.maximumEvenSplit(finalSum = 28))
  pass
runSolution()