'''

  891. Sum of Subsequence Widths
  https://leetcode.com/problems/sum-of-subsequence-widths/discuss/768402/Python3-Sort-and-1-pass-derived-from-DP-solution

'''


from collections import defaultdict


class SolutionBF:
  def sumSubseqWidths(self, nums):
    M = 10 ** 9 + 7
    nums.sort()
    DP = defaultdict(int)
    result = 0
    
    for right in nums:
      for left, count in DP.items():
        print(left, right, ' | ', (right - left) * count)
        result += (right  - left) * count
        DP[left] = count * 2
        
      DP[right] += 1

      print(DP)    
    return result
  
  
class SolutionRef1:
  def sumSubseqWidths(self, nums):
    M = 10 ** 9 + 7
    nums.sort()
    totalCount = 0
    totalProd  = 0
    result = 0
    
    for num in nums:
      print('------------')
      print(f'num: {num} | totalCount: {totalCount} | totalProd: {totalProd}')
      print('calc totalCount * num - totalProd :', totalCount * num - totalProd)
      result += totalCount * num - totalProd
      totalCount = 2 * totalCount + 1
      totalProd  = 2 * totalProd + num
      print(f'result: {result}')
    
    return result
    
  
class Solution:
  def sumSubseqWidths(self, nums):
    nums.sort()
    mod = 10 ** 9 + 7
    L, R, D = 0, len(nums) - 1, 1
    ans, Lsum, Rsum = 0, 0, 0
    
    while L < len(nums):
      Lsum += nums[L]
      Rsum += nums[R]
      ans += (Rsum - Lsum) * D
      print(f'Lsum: {Lsum} | Rsum: {Rsum} | ans: {ans} | L: {L} | R: {R} | D: {D}1')
      
      D *= 2
      L += 1
      R -= 1
    
    return ans % mod
    
  
def runSolution():
  solution = Solution()
  # print(solution.sumSubseqWidths([1,2]))
  print(solution.sumSubseqWidths([1,2,3,4]))
  pass
runSolution()