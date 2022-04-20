'''

  65. Valid Number

  -123.456e789

  1. sign
    > Followed by int/decimal - not vice versa
    > Can be reset following e/E
  2. decimal
    > Followed by int
    > cannot follow e/E
    > decimal number can only contain 1 decimal
  3. integer
    > Followed by one or more digits
'''


def isNumber(s):
  exponent = False
  decimal = False
  number = False
  sign = False

  for char in s:
    if char.isnumeric() == True:
      number = True

    elif char == '+' or char == '-':
      if number or decimal or sign: return False
      sign = True

    elif char == '.':
      if exponent or decimal: return False
      decimal = True

    elif char == 'e' or char == 'E':
      if exponent or number: return False
      number = False
      sign = False
      exponent = True
      decimal = False

    else: return False

  if number == False:
    if decimal  == True: return False
    if exponent == True: return False

  return True


print(isNumber("2.e-8"))
print(isNumber('0'))
print(isNumber('e'))
print(isNumber('3e+7'))
print(isNumber('.'))
print(isNumber('53.5e93'))
print(isNumber('e3'))
print(isNumber('+1e+'))
print(isNumber('.1'))