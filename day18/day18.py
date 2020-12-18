from input import I

def ev(s):
  st = []
  for c in s:
    if c == ' ': continue
    if c in '(+*':
      st.append(c)
      continue
    if c == ')':
      assert st.pop(-2) == '(', st
      c = str(st.pop(-1))
    if c.isdigit():
      st.append(int(c))
    while True:
      if len(st)<=1: break
      if not isinstance(st[-1], int): break
      if st[-2] != '+' and st[-2] != '*': break

      if st[-2] == '+':
        st = st[:-3] + [st[-1] + st[-3]]
      elif st[-2] == '*':
        st = st[:-3] + [st[-1] * st[-3]]
  return st[0]

assert ev('1 + 2 * 3 + 4 * 5 + 6') == 71
assert ev('1 + (2 * 3) + (4 * (5 + 6))') == 51
assert ev('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632

print('1--->', sum(map(ev,I)))
