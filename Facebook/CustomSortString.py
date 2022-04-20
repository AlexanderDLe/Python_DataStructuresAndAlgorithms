'''

  791. Custom Sort String

'''
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from _utils import printDict

def customSortString(order, s):
  charFreq = {}
  for char in s:
    charFreq[char] = charFreq.get(char, 0) + 1

  result = ''
  for char in order:
    if char in charFreq:
      result += char * charFreq[char]
      del charFreq[char]


  for char in charFreq:
    result += char * charFreq[char]

  return result




print(customSortString('cba', 'abccd'))
print(customSortString('cbafg', 'abcd'))