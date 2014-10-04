import sys

matrix = []

f = open(sys.argv[1], 'r')

for line in f:
  matrix.append(line.rsplit())

print matrix
