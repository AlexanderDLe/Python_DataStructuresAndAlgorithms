'''

  You are an uncle and you want to buy as many gifts as you can for your nephew.
  You are given a list of daysAndGifts, in which you can choose to buy that gift on
  that day if you have enough money. 
  
  Your wealth increases $1 per day and you start at day 0.

  You are given the following arguments:
  - [int, int]: daysAndGifts (corresponding day and cost of gift that can be bought),
  
  - You start with 0 money
  - You accumulate 1 dollar every day
  - At each [day, gift] you have the option to buy the gift
  
  Example:
  
  DaysAndGifts = [[3,3], [5,4], [8, 3]]

  Day 3: 
  You accumulate 3 over 3 days for a total of $3 and you can buy the gift. 
  After buying you have 0 money.
  
  Day 5:
  You accumulate 2 over 2 days for a total of $2 but you can't buy the gift. 
  You end the day with $2.
  
  Day 8:
  You accumulate 3 more days for a total of $5 and you can buy the gift for $3.
  
  The maximum number of gifts you can buy is 2.
  
  Time Complexity: O(indexes * moneys^2 * costs^2)
  
'''

class Solution:
  def main(self, daysAndGifts):
    n = len(daysAndGifts)
    DP = {}
    
    def DFS(index, prevMoney):
      if (index, prevMoney) in DP: return DP[(index, prevMoney)]
      if index == n: return 0
      
      currDay = daysAndGifts[index][0]
      prevDay = daysAndGifts[index - 1][0] if index != 0 else 0
      currMoney = prevMoney + (currDay - prevDay)
      giftCost = daysAndGifts[index][1]      
      
      gifts = 0
      # Decision 1: Buy gift
      if giftCost <= currMoney:
        gifts = 1 + DFS(index + 1, currMoney - giftCost)
        
      # Decision 2: Do not buy gift
      gifts = max(gifts, DFS(index + 1, currMoney))
      
      DP[(index, prevMoney)] = gifts
      return gifts
      
    result = DFS(0, 0)
    print(DP)
    return result
      


  
def runSolution():
  solution = Solution()
  print(solution.main([[3,3], [5,4], [8, 3]]))
  print(solution.main([[100, 100], [101, 3], [102, 3]]))
  pass
runSolution()

