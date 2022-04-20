'''

  415. Add Strings

'''


def addStrings(num1, num2):
  p = len(num1) - 1
  q = len(num2) - 1
  carry = 0
  result = []

  while p >= 0 or q >= 0 or carry > 0:
    pNum = int(num1[p]) if p >= 0 else 0
    qNum = int(num2[q]) if q >= 0 else 0

    sum = pNum + qNum + carry
    carry = sum // 10
    mod   = sum  % 10
    result.insert(0, mod)

    p -= 1
    q -= 1
  
  return ''.join(map(str, result))


print(addStrings('11', '123'))
print(addStrings('456', '77'))
print(addStrings('0', '0'))