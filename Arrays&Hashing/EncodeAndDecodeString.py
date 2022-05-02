'''

  271. Encode and Decoded Strings

'''


class CodecRef:
  def encode(self, strs):
    """Encodes a list of strings to a single string.
    """
    # encode(['abc','d','ef']) = '3.1.2#abcdef'
    return ('.'.join(map(lambda s: str(len(s)),strs)))+'#'+(''.join(strs))

  def decode(self, s):
    """Decodes a single string to a list of strings.
    """
    # encode(['abc','d','ef']) = '3.1.2#abcdef'
    delidx=s.find('#')        
    info,content=s[:delidx],s[delidx+1:]
    if not info: return []
    
    cnts=map(int,info.split('.'))
    ans=[]
    start=0
    
    for cnt in cnts:
      ans.append(content[start:start+cnt])
      start+=cnt
    return ans

class Codec:
  def encode(self, strs):
    lens = []
    for s in strs:
      lens.append(str(len(s)))
    return '.'.join(lens) + ':' + ''.join(strs)

  def decode(self, s):
    delimiterIndex = s.find(':')
    lens = s[:delimiterIndex]
    lens = lens.split('.')
    content = s[delimiterIndex + 1:]
    
    if len(lens) == 0: return []
    
    result = []
    start = 0
    for length in lens:
      length = int(length)
      result.append(content[start:start + length])
      start += length
    
    return result

def runSolution():
  codec = Codec()
  print(codec.decode(codec.encode(["Hello","World"])))
  pass
runSolution()
