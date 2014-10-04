import itertools

spots='abcdefghijklmnop'

bigGuy=list(itertools.product(spots,spots,spots,spots))

for guy in bigGuy:
  if len(set(guy)) != 4: bigGuy.remove(guy)

print len(bigGuy)
