import sys

ll = list(sys.stdin)

R={}
while True:
  l = ll.pop(0).strip()
  if not l: break
  num, ruless = l.split(':')
  if ruless.find('"') != -1:
    R[int(num)] = ruless.replace('"',' ').strip()
    continue
  v = []
  rules=ruless.split('|')
  for r in rules:
    v.append([int(x) for x in r.split()])
  R[int(num)] = v

I=[]
for l in ll:
  l = l.strip()
  I.append(l)
