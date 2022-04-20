'''

  986. Interval List Intersections

'''

def handleOverlap(first, second):
  startF, endF = first
  startS, endS = second
  isOverlapping = False

  if startF >= startS and startF <= endS: isOverlapping = True
  if startS >= startF and startS <= endF: isOverlapping = True

  if isOverlapping == False: return None
  return (max(startF, startS), min(endF, endS))

def intervalIntersections(firstList, secondList):
  n1, n2 = len(firstList), len(secondList)
  p1, p2 = 0, 0
  
  result = []
  while p1 < n1 and p2 < n2:
    first = firstList[p1]
    second = secondList[p2]

    overlap = handleOverlap(first, second)
    if overlap != None: result.append(overlap)

    if first[1] < second[1]: p1 += 1
    else                   : p2 += 1

  return result


print(intervalIntersections([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
print(intervalIntersections([[1,3],[5,9]], []))