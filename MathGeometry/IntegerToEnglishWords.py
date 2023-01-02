'''
  
  273. Integer to English Words

'''

class SolutionRef:
  def numberToWords(self, num):
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

  
class Solution:
  def numberToWords(self, num):
    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    BILLION  = 1000000000
    MILLION  = 1000000
    THOUSAND = 1000
    HUNDRED  = 100
    
    def intToString(n):
      if n >= BILLION : return intToString(n // BILLION)  + ' Billion '  + intToString(n % BILLION)
      if n >= MILLION : return intToString(n // MILLION)  + ' Million '  + intToString(n % MILLION)
      if n >= THOUSAND: return intToString(n // THOUSAND) + ' Thousand ' + intToString(n % THOUSAND)
      if n >= HUNDRED : return intToString(n // HUNDRED)  + ' Hundred '  + intToString(n % HUNDRED)
      if n >= 20      : return tens[int(n // 10)] + intToString(n % 10)
      if n >= 1       : return ones[int(n)]
      return ''
    
    if num == 0: return 'Zero'
    return intToString(num)
    

  
  
def runSolution():
  solution = Solution()
  print(solution.numberToWords(123))
  print(solution.numberToWords(12345))
  print(solution.numberToWords(1234567))
  pass
runSolution()