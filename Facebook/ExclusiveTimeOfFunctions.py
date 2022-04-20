'''

  636. Exclusive Time of Functions

  -----------------------------------------------------------

  n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

  log: "0:start:0"

  time = 0
  stack = [0]
  times: {0:0, 1:0}

  Start operation with first log - there is nothing in the stack
  so we can just push it onto the stack.

  -----------------------------------------------------------

  n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

  log: "1:start:2"

  Another start operation. This log will overlap with the previous log.
  Therefore the previous function will temporarily end here - we must
  account for the time that has been expended for the previous function.

  currTime  = 0
  newStart  = 2

  2 - 0 = 2 <--- Add into times dict

  new time = 2

  time = 2
  stack = [0, 1]    <--- Add new function to stack
  times: {0:2, 1:0}

  -----------------------------------------------------------

  n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

  log: "1:end:5"

  function 1 ends. Pop id from stack and subtract end time to current time.
  5 - 2 + 1(zero indexing) = 3

  New time is end time + 1 (we dont' want to include end time again)

  time = 6
  stack = [0]
  times: {0:2, 1:4}

  -----------------------------------------------------------

  n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

  log: "0:end:6"

  function 0 ends. Pop id from stack and subtract end time to current time.
  6 - 6 + 1 = 1

  New time is end time + 1 (we dont' want to include end time again)

  time = 7
  stack = [0]
  times: {0:3, 1:4}

  -----------------------------------------------------------


'''


def exclusiveTimes(n, logs):
  funcDict = {i: 0 for i in range(n)}
  currTime = 0
  idStack  = []

  for log in logs:
    id, command, time = log.split(':')
    id   = int(id)
    time = int(time)

    if command == 'start':
      if idStack:
        topID = idStack[-1]
        funcDict[topID] += time - currTime

      idStack.append(id)
      currTime = time

    if command == 'end':
      topID = idStack.pop()
      funcDict[id] += time - currTime + 1
      currTime = time + 1


  return funcDict.values()


print(exclusiveTimes(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]))
print(exclusiveTimes(n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
print(exclusiveTimes(n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))