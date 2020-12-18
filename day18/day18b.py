import numpy as np

from input import I

def ev(s):
  #print('ev:',s)
  lp,rp,pn = None,None,0
  for i,c in enumerate(s):
    if c == '(':
      if lp is None: lp = i
      pn+=1
    if c == ')':
      pn-=1
      if pn==0:
        rp=i
        break
  if lp is not None:
    #print(s[:lp],'|', s[lp+1:rp],'|', s[rp+1:])
    return ev(s[:lp] + str(ev(s[lp+1:rp])) + s[rp+1:])

  stack = []
  num = 0
  lastop = '*'
  for c in s+'*':
            if c == ' ': continue
            if c.isdigit():
                num = 10*num + int(c)
                continue
            if lastop == '*': stack.append(num)
            elif lastop == '/': stack.append(1/num)
            elif lastop == '-': stack.append(int(stack.pop()-num))
            elif lastop == '+': stack.append(stack.pop()+num)
            num,lastop = 0,c
  return np.prod(stack)

assert ev('1 + 2 * 3 + 4 * 5 + 6') == 231
assert ev('1 + (2 * 3) + (4 * (5 + 6))') == 51
assert ev('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340

print('2--->', sum(map(ev,I)))
