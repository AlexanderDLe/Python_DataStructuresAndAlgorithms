'''

  273. Integer to English Words

'''

def numberToWords(num: int) -> str:
  ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
  tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

  def intToString(n):
    if n >= 1000000000: return intToString(n/1000000000) + " Billion" + intToString(n % 1000000000)
    if n >= 1000000: return intToString(n/1000000) + " Million" + intToString(n % 1000000)
    if n >= 1000: return intToString(n/1000) + " Thousand" + intToString(n % 1000)
    if n >= 100: return intToString(n/100) + " Hundred" + intToString(n % 100)
    if n >= 20: return " " + tens[int(n / 10 - 2)] + intToString(n % 10) 
    if n >= 1: return " " + ones[int(n)]
    return ""

  if num == 0: return 'Zero'
  return intToString(num).strip()


# print(numberToWords(123))
# print(numberToWords(12345))
print(numberToWords(1234567890))
