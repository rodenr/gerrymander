import itertools


def check(thing):
  flag=False
  
  for d in thing:
    if (d[0],d[1]-1) in thing:
      flag=True

    if (d[0],d[1]+1) in thing:
      flag=True

    if (d[0]-1,d[1]) in thing:
      flag=True

    if (d[0]+1,d[1]) in thing:
      flag=True

    if not flag:
      return flag

  return flag

#################################################


arrays=[(0,1,2,3), (0,1,2,3)]

these=list(itertools.product(*arrays))

those=list(itertools.permutations(these, 4))

print len(those)

for this in those:
  if not check(this):
    those.remove(this)


master = those
print master

