import pdb
test1 = ((0, 0), (0, 1), (0, 2), (0, 3))
test2 = ((2, 0), (2, 1), (2, 2), (1, 2))
test3 = ((0, 0), (1, 3), (0, 3), (2, 0))

def check(thing):
  flag=False
  pdb.set_trace()
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

print check(test1)
print check(test2)
print check(test3)
