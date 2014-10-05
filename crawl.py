import itertools
import pdb


def validConfig(thing):
  flag=False
  storage = [thing.pop()]

  while len(thing) != 0:

    chained = list(storage)
    chainLen = len(chained)

    for d in chained:
      if (d[0],d[1]-1) in thing:
        storage.append((d[0],d[1]-1))
        thing.remove((d[0],d[1]-1))
        flag=True

      if (d[0],d[1]+1) in thing:
        storage.append((d[0],d[1]+1))
        thing.remove((d[0],d[1]+1))
        flag=True



      if (d[0]-1,d[1]) in thing:
        storage.append((d[0]-1,d[1]))
        thing.remove((d[0]-1,d[1]))
        flag=True



      if (d[0]+1,d[1]) in thing:
        storage.append((d[0]+1,d[1]))
        thing.remove((d[0]+1,d[1]))

    
    if len(storage) == len(chained):
      return False
  return True
"""
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
"""

#################################################


arrays=[(0,1,2,3), (0,1,2,3)]

these=list(itertools.product(*arrays))

those=list(itertools.permutations(these, 4))

print len(those)

for this in those:
  tmp = list(this)
  #if tmp[0] == (3,3) and tmp[1] == (3,2) and tmp[3] == (0,0):
    #pdb.set_trace()
  if not validConfig(tmp):
    those.remove(this)


master = those
print len(master)

