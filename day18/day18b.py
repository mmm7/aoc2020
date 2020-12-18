from input import I

def app(lastop, stack, num):
  if lastop == '*': stack.append(num)
  elif lastop == '/': stack.append(1/num)
  elif lastop == '-': stack.append(int(stack.pop()-num))
  elif lastop == '+': stack.append(stack.pop()+num)

def collapse(stack):
  num = 1
  while stack[-1] != '(':
    num *= stack.pop(-1)
  stack.pop(-1)
  return stack.pop(-1),num

def ev(s):
  stack = ['*','(']
  num = 1
  lastop = '*'
  for c in s+'*':
            #print(c,num,lastop, stack)
            if c == ' ': continue
            if c.isdigit():
                num = int(c)
                continue
            if c == '(':
                stack += [lastop, '(']
                lastop = '*'
                continue
            if c == ')':
              app(lastop, stack, num)
              lastop, num = collapse(stack)
            app(lastop, stack, num)
            num,lastop = 0,c
  return collapse(stack)[1]

assert ev('(1+2)') == 3, ev('(1+2)')
assert ev('1 + 2 * 3 + 4 * 5 + 6') == 231
assert ev('1 + (2 * 3) + (4 * (5 + 6))') == 51
assert ev('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340

print('2--->', sum(map(ev,I)))
