'''

  1762. Buildings With an Ocean View

'''

def findBuildings(heights):
  n = len(heights)
  maxHeight = 0

  result = []
  for i in range(n - 1, -1, -1):
    height = heights[i]

    if height > maxHeight:
      result.append(i)
      maxHeight = height

  result.reverse()
  return result



print(findBuildings([4,2,3,1]))
print(findBuildings([4,3,2,1]))
print(findBuildings([1,2,3,4]))