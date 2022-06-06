'''
  https://leetcode.com/discuss/interview-question/1733269/Amazon-OA-sliding-window

  You are hosting a hackathon.
  Each team will have exactly teamSize developers.
  A developer's skill level is denoted by skill[i].

  The difference between the maximum and minimum skill levels within a team cannot 
  exceed a threshold, maxDiff. Determine the maximum number of teams that can be 
  formed from the contestants.

  Example:
  skill = [3, 4, 3, 1, 6, 5]
  teamSize = 3
  maxDiff = 2
  
  At most, 2 teams can be formed: [3, 3, 1] and [4, 6, 5].


  The difference between the maximum and minimum skill levels is 2 in each case, 
  which does not exceed the threshold value of 2.

  --------------------------------------------------------------

  First, it will help to solve the problem by sorting.

  1, 3, 3, 4, 5, 6

  Next, we can use a sliding window approach to determine the teams.
  Sliding window criteria:

  > skill diff must be at most 2
  > Window size must be teamSize

  If criteria is met, we can increment the number of teams (count).

  ---------------------------------------------------------------

  Example Operation

  maxDiff = 2

  1, 3, 4, 5, 5, 6, 7
  |      |
  i      (i + teamSize)

  > i + teamSize is max skill in this window while i is the min skill.
    If diff is greater than maxDiff, then we increment i.

  4 - 1 = 3 <--- Skill gap between max and min

  Skill gap > maxDiff, therefore we increment the window forward. (sorry min skill guy)

  ---------------------------------------------------------------

  1, 3, 4, 5, 5, 6, 7
     |      |
     i      (i + teamSize)

  
  Skill gap = 5 - 3 = 2

  2 === maxDiff. Since we do not exceed maxDiff, this is a valid team. We can increment teamCount.
  teamCount = 1

  ---------------------------------------------------------------

  1, 3, 4, 5, 5, 6, 7
              |      |
              i      (i + teamSize)

  
  Skill gap = 7 - 5 = 2

  2 === maxDiff. Since we do not exceed maxDiff, this is a valid team. We can increment teamCount.
  teamCount = 2
  
'''


def maxNumberOfTeams(skills, teamSize, maxDiff):
  skills.sort()
  teamCount = 0

  i = 0
  while i <= len(skills) - teamSize:
    min = skills[i]
    max = skills[i + teamSize - 1]

    if (max - min > maxDiff):
      i += 1
    else:
      teamCount += 1
      i += teamSize

  return teamCount


print(maxNumberOfTeams([3, 4, 3, 10, 1, 6, 5], 3, 2))
print(maxNumberOfTeams([3, 4, 7, 5, 1, 6, 5], 3, 2))
