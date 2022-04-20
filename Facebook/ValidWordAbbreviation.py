'''

  408. Valid Word Abbreviation

'''

def validWordAbbreviation(word, abbr):
  w = 0
  a = 0

  while w < len(word) and a < len(abbr):
    wChar, aChar = word[w], abbr[a]

    if aChar.isnumeric() == False:
      if wChar != aChar: return False
      w += 1
      a += 1
      continue

    if aChar == '0': return False

    if aChar.isnumeric() == True:
      num = ''
      while a < len(abbr) and abbr[a].isnumeric():
        num += abbr[a]
        a += 1
      w += int(num)

  print(w, a)
  return w == len(word) and a == len(abbr)

print(validWordAbbreviation("internationalization", "i12iz4n"))
print(validWordAbbreviation("apple", "a2e"))
print(validWordAbbreviation("internationalization", "i5a11o1"))
print(validWordAbbreviation("a", "01"))