'''

  Parameters:

  scores : List of int
  cutOffRank : int
  num: int (denoting amount of scores)

  You are given a list of integers representing scores of players in a video game. 

  Players can 'level-up' if by the end of the game they have a rank that is at most 
  the cutOffRank. A player's rank is solely determined by their score relative to 
  the other players' scores. 
  

  For example:

  Score : 10 | Rank 1
  Score :  5 | Rank 2
  Score :  3 | Rank 3

  -------------------------------------------------------------------------------

  If multiple players happen to have the same score, then they will all receive the same rank. 
  However, the next player with a score lower than theirs will receive a rank that is offset by this. 
  
  For example:

  Score: 10 | Rank 1
  Score: 10 | Rank 1
  Score: 10 | Rank 1
  Score : 5 | Rank 4

  Finally, any player with a score of 0 is automatically ineligible for leveling-up, regardless of their rank.

  -------------------------------------------------------------------------------

  Return the number of players who are eligible for leveling-up

  As we iterate over the sorted scores, we will increment levels and rank until rank reaches
  the cutoff point.

  Ex: 

  cutoff = 8
  Scores sorted = [10, 10, 15, 7, 7, 5, 3]
                    ^
  rank   = 1
  levels = 1
  prev   = INF
  
  -------------------------------------------------------------------------------

  Return the number of players who are eligible for leveling-up

  Ex: 

  Scores sorted = [10, 10, 15, 7, 7, 5, 3]

  rank 1

  -------------------------------------------------------------------------------

    15   10   10   7   7   5   3
    ^

    rank = 1
    lvls = 1
    
'''

class Solution:
  '''
     1    2   2  4  4  6  7
    [15, 10, 10, 7, 7, 5, 3]  cutOffRank = 3
          ^    
    lvls = 1
    rank = 2
  
  '''
  def scoring(self, scores, cutOffRank):
    scores.sort(reverse = True)
    if len(scores) == 0 or scores[0] == 0: return 0
    
    lvls = 1
    rank = 1
    
    for i in range(1, len(scores)):
      prev, curr = scores[i - 1], scores[i]
      
      # Since the next rank continues despite duplicates, we can
      # get the next ranking via i + 1
      if curr != prev: rank = i + 1   
      if rank > cutOffRank or curr == 0: break
      
      lvls += 1      
    
    return lvls
  
def runSolution():
  solution = Solution()
  print(solution.scoring([15, 10, 10, 7, 7, 5, 3], 3))
  print(solution.scoring([15, 10, 7, 7, 7, 5, 3], 3))
  print(solution.scoring([15, 0], 3))
  print(solution.scoring([0], 3))
  pass
runSolution()