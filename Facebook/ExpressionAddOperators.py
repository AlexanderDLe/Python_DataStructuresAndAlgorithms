'''

  282. Expression Add Operators

'''

def addOperatorsRef(s, target):
  n = len(s)

  def backtrack(index, path, resultSoFar, prevNum):
    if index == n and resultSoFar == target: result.append(path)
    if index == n: return

    for i in range(index, n):
      # Skip leading zero number
      if i > index and s[index] == '0': break

      # Get all potential numbers from string. (Ex. from 123 get 1, 12, 123)
      num = int(s[index:i + 1])

      if index == 0:
        # First num pick it without adding any operator
        backtrack(i + 1, path + str(num), resultSoFar + num, num)
      else:
        backtrack(i + 1, path + '+' + str(num), resultSoFar + num, num)
        backtrack(i + 1, path + '-' + str(num), resultSoFar - num, -num)
        backtrack(i + 1, path + '*' + str(num), resultSoFar - prevNum + prevNum * num, prevNum * num) # Can imagine with example: 1+2*3*4
  
  result = []
  backtrack(0, '', 0, 0)
  return result

def addOperators(s, target):
  n = len(s)

  def DFS(index, path, resultSoFar, prev):
    if index == n and resultSoFar == target: result.append(path)
    if index == n: return

    # Get valid permutations of s (ex. 123 into 1, 12, and 123)
    for i in range(index, n):
      if i > index and s[index] == '0': break

      num = int(s[index:i + 1])

      if index == 0:
        DFS(i + 1, path + str(num), resultSoFar + num, num)
      else:
        DFS(i + 1, path + '+' + str(num), resultSoFar + num, num)
        DFS(i + 1, path + '-' + str(num), resultSoFar - num, -num)
        DFS(i + 1, path + '*' + str(num), resultSoFar - prev + (prev * num), num * prev)

  result = []
  DFS(0, '', 0, 0)
  return result


print(addOperators(s = "123", target = 6))
print(addOperators(s = "232", target = 8))
print(addOperators(s = "3456237490", target = 9191))