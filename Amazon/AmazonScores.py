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

    rank = 2
    lvls = 3
    
'''

import heapq
import math

def scoringRef(scores, cutOffRank, num):
  scores.sort(reverse = True)
  print(scores)

  lvls =  0
  rank = 0
  prev = 0

  for score in scores:
    if score == 0: break
    if rank >= cutOffRank: break

    lvls += 1
    if score is not prev: 
      rank += 1
      prev = score

  return lvls

def scoring(scores, cutOffRank, num):
  scores.sort(reverse=True)
  print(scores)
  
  prev = float('inf')
  rank = 0
  lvls = 0
  
  for score in scores:
    if score == 0: break
    
    if score != prev:
      prev = score
      rank += 1
      if rank > cutOffRank: break
    
    lvls += 1
    
  return lvls


print(scoring([10, 10, 15, 7, 7, 5, 3], 3, 7))