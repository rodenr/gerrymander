import sys
import csv
import itertools



##########################
# Add On if valid config
def addOn(myList, length):
  newMaster=[]
  for district in myList:
    newDist=list(district)
    tmpDist=[]
    for index in newDist:
      x=index[0]
      y=index[1]
      if (x,y-1) not in newDist and y-1 >=0:
        tmpDist=list(newDist)
        tmpDist.append((x, y-1))
        tmpDist.sort()
        if tmpDist not in newMaster: newMaster.append(tmpDist)
      
      if (x, y+1) not in newDist and y+1 <=length:
        tmpDist=list(newDist)

        tmpDist.append((x, y+1))
        tmpDist.sort()
        if tmpDist not in newMaster: newMaster.append(tmpDist)

      if (x-1, y) not in newDist and x-1 >=0:
        tmpDist=list(newDist)

        tmpDist.append((x-1,y))
        tmpDist.sort()
        if tmpDist not in newMaster: newMaster.append(tmpDist)

      if (x+1, y) not in newDist and x+1 <=length:
        tmpDist=list(newDist)

        tmpDist.append((x+1, y))
        tmpDist.sort()
        if tmpDist not in newMaster: newMaster.append(tmpDist)

  for move in newMaster:
    #if (0,0) in move:
    reflectDist=[]
    for index in move:
      x = index[0]
      y = index[1]
      reflectDist.append((length-y, length-x))
    reflectDist.sort()
    if reflectDist not in newMaster:
      newMaster.append(reflectDist)

  return newMaster


##################################################

##################################################

def validConfig(thing):
  storage = [thing.pop()]

  while len(thing) != 0:

    #flag=False
    count = 0

    chained = list(storage)
    chainLen = len(chained)

    for d in chained:
      # if statements check for valid coordinates of d's neighbors
      #   that are not yet popped off of thing
      if (d[0],d[1]-1) in thing:
        storage.append((d[0],d[1]-1))
        thing.remove((d[0],d[1]-1))

      if (d[0],d[1]+1) in thing:
        storage.append((d[0],d[1]+1))
        thing.remove((d[0],d[1]+1))


      if (d[0]-1,d[1]) in thing:
        storage.append((d[0]-1,d[1]))
        thing.remove((d[0]-1,d[1]))

      if (d[0]+1,d[1]) in thing:
        storage.append((d[0]+1,d[1]))
        thing.remove((d[0]+1,d[1]))

    if len(storage) == len(chained):
      return False
  return True



# Reads input file to get matrix
# Dimensions are taken from this to make permutations of valid configurations

neighborhood = []

f = open(sys.argv[1], 'r')

for line in f:
  neighborhood.append(line.rsplit())

dimension = range(0,4) 

arrays = [dimension, dimension]

these=list(itertools.product(*arrays))

those=list(itertools.combinations(these, 4))

#print len(those)
master = []
for this in those:
  tmp = list(this)
  if not validConfig(tmp): #== len(neighborhood):
    those.remove(this)
  else:
    #sort = list(this)#.sort()
    #sort.sort()
    #if sort not in master:
    master.append(this)

newMaster = addOn(master, 4)
sixMaster = addOn(newMaster, 5)    
sevMaster = addOn(sixMaster, 6)
supMaster = addOn(sevMaster, 7)

masterList = []
for move in supMaster:
  masterList.append(list(itertools.chain(*list(move))))


with open(sys.argv[2], "wb") as f:
      writer = csv.writer(f)
      writer.writerows(masterList)

'''
thefile = open(sys.argv[2], 'w')
for item in master:
  print>>thefile, item
  '''
