'''

  273. Integer to English Words

'''



class Solution:
    def numberToWords(self, n):
      if n == 0: return 'Zero'
      result = self.convert(n)
      return result.strip()
    
    def convert(self, n):
      billion  = 1000000000
      million  = 1000000
      thousand = 1000
      hundred  = 100
      tens    = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
      digits  = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 
                'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
      
      if n >= billion: return self.convert(n//billion)  + ' Billion'  + self.convert(n%billion)
      if n >= million: return self.convert(n//million)  + ' Million'  + self.convert(n%million)
      if n >= thousand:return self.convert(n//thousand) + ' Thousand' + self.convert(n%thousand)
      if n >= hundred: return self.convert(n//hundred)  + ' Hundred'  + self.convert(n%hundred)
      if n >= 20: return ' ' + tens[int(n//10)] + self.convert(int(n%10))
      if n >= 1 : return ' ' + digits[int(n)]
      return ''
    
  
def runSolution():
  solution = Solution()
  print(solution.numberToWords(123))
  print(solution.numberToWords(12345))
  print(solution.numberToWords(1234567))
  pass
runSolution()
