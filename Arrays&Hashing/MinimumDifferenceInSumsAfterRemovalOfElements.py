'''

  2163. Minimum Difference in Sums After Removal of Elements

'''


from heapq import heapify, heappop, heappush, heappushpop


class Solution:
  def minimumDifference(self, nums):
    N = len(nums) // 3
    
    # Build pre-min using minHeap
    left = [-n for n in nums[:N]]
    heapify(left)
    sumLeft = [sum(nums[:N])]
    
    for i in range(N, 2*N):
      heappush(left, -nums[i])
      curr = heappop(left)
      sumLeft.append(sumLeft[-1] + curr + nums[i])
    
  
def runSolution():
  solution = Solution()
  print(solution.minimumDifference(nums = [3,1,2]))
  print(solution.minimumDifference(nums = [7,9,5,8,1,3]))
  pass
runSolution()
