'''

  50. Pow(x, n)

  pow(2, 10) -> 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2

  Here we can see that we are doing repeated work. We can easily cut this in half.

  pow(2, 5) * pow(2, 5)

  -------------------------------------------------------------------------------

  If it's negative, we can subract one instance.

  pow(2, 9)

  2 * pow(2, 4) * pow(2, 4)
'''



def myPow(x, n):
  if n == 0 : return 1
  if n == 1 : return x
  if n == -1: return 1/x
  if n % 2 == 0:
    calc = myPow(x, n/2)
    return calc * calc
  if n % 2 == 1:
    return x * myPow(x, n - 1)



print(myPow(2.00000, 10))
print(myPow(2.10000, 3))
print(myPow(2.00000, -2))