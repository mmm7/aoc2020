from input import I


def step(MEM, acc, pc):
  instr,d = MEM[pc]
  #print(acc,pc,instr,d)
  if instr == 'nop': return (acc, pc+1)
  if instr == 'acc': return (acc+d, pc+1)
  if instr == 'jmp': return (acc, pc+d)
  assert False, instr

def run(MEM, last, acc, pc):
  while True:
    if pc == len(MEM): return ('end', pc, acc)
    if pc > len(MEM): return ('seg', pc, acc)
    if pc < 0: return ('seg', pc, acc)
    if last[pc] is not None: return ('loop', pc, acc)
    last[pc] = acc
    acc, pc = step(MEM, acc, pc)

N = len(I)
last = [None] * N
print(run(I,last,0,0))

for x in range(N):
  if I[x][0]=='acc': continue
  if not last[x]: continue
  other = ('nop', 'jmp')[I[x][0]=='nop']
  other, I[x][0] = I[x][0], other
  mylast = last.copy()
  oldacc, mylast[x] = mylast[x], None
  res = run(I,mylast,oldacc,x)
  if res[0]=='end': print(res)
  other, I[x][0] = I[x][0], other
