'''

  616. Add Bold Tag in String

'''

def addBoldTags(s, words):
  # Initialize boolean array to indicate bold
  bold = [0] * len(s)

  # Populate boolean array
  for word in words:
    start = s.find(word)
    while start != -1:
      for i in range(start, start + len(word)):
        bold[i] = 1
      start = s.find(word, start + 1)
  
  output = []
  i = 0

  # Append bold if first element is bold
  if bold[0] == 1: output.append('<b>')

  for i in range(0, len(bold) - 1):
    curr, next = bold[i], bold[i + 1]
    output.append(s[i])

    if   curr == 0 and next == 1: output.append('<b>')
    elif curr == 1 and next == 0: output.append('</b>')
    i += 1

  # Since we don't iterate to very end, we must take care of end cases here
  output.append(s[-1])
  if bold[-1] == 1: output.append('</b>')
  
  return ''.join(output)


print(addBoldTags(s = "abcxyz123", words = ["abc","123"]))
print(addBoldTags(s = "aaabbcc", words = ["aaa","aab","bc"]))