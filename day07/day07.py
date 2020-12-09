from input import I,INV

vis = set()
res = ['shiny gold']
while res:
  curr,res = res,[]
  for c in curr:
    for t in INV[c]:
      if t not in vis:
        vis.add(t)
        res.append(t)

print(vis)
print(len(vis))
