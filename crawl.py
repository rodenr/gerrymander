import sys
from sys import maxsize
import itertools
import pdb

#############################################
# This function helps determine valid configurations
#   making continuous subsets in the matrix

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

#################################################

#################################
# Invalid Subset Configuration Detection

def badSubset(district):#state, child):
    
  dimension = range(0,8)
  arrays=[dimension, dimension]

  these=list(itertools.product(*arrays))
 
 # matrix = list(state[2])
  #for district in state[1]:
  #  for spot in district:
  #    if spot in these: these.remove(spot)
  for spot in district:
    if spot in these: these.remove(spot)

  if validOther(these) % 8 != 0:
    return True
  else: return False
#################################

#################################
# hopefully this won't be here in the end

def validOther(thing):
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
      return len(storage)#False
  return len(storage)#True
#################################

#################################
# Minmax Algorithm

def minimax(state, childMoveList, depth, maxPlayer):
  if depth != 0 and len(childMoveList) == 0:
    return ['error',[]]
  if depth == 2 and len(state[2]) == 8:
      return [largeUtility(state), list(state[1])]
  if depth == 0 and len(state[2]) == 4:
      return [utility(state),list(state[1])]
  if maxPlayer:
    bestValAndState = [-maxsize,[]]
    for child in childMoveList:

      newChildList = reduction(child, childMoveList)
      
      state[1].append(child)
      valAndState = minimax(state, newChildList, depth-1, False)
      
      if valAndState[0] != 'error':
        #pdb.set_trace()
        if valAndState[0] > bestValAndState[0]:
          bestValAndState = list(valAndState)
  #        print str(depth)+'max' + str(bestValAndState)
        #pdb.set_trace()
        #bestValue = max([val, bestValue])
        
      state[1].remove(child)
    #if depth == 2: pdb.set_trace()
    if bestValAndState[0] == -maxsize: bestValAndState[0] = maxsize
    return bestValAndState

  else:
    bestValAndState = [ maxsize,[]]
#    if len(childMoveList) > 1:
#      for fchild in childMoveList:
#        if not badSubset(state, fchild): childMoveList.remove(fchild)
    for child in childMoveList:

      newChildList = reduction(child, childMoveList)

      state[1].append(child)
      valAndState = minimax(state, newChildList, depth-1, True)

      if valAndState[0] != 'error':
        if valAndState[0] < bestValAndState[0]:
          #if abs(valAndState[0]) == abs(maxsize):
            #pdb.set_trace()
          bestValAndState = list(valAndState)
  #        print str(depth)+'min'+ str(bestValAndState)
        #pdb.set_trace()
        #bestValue = min([val, bestValue])
      state[1].remove(child)

    #if depth == 3: pdb.set_trace()
    if bestValAndState[0] == maxsize: bestValAndState[0] = -maxsize
    return bestValAndState

#################################

#################################
# Reduction Function

# Based on the new child move, remove
#   all move options that overlap this choice

def reduction(child, parentList):
  
  newChildList = []

  for move in parentList:
    flag=True
    for block in child:
      if block in move:
        flag=False
    if flag:
      newChildList.append(move)

  return newChildList

#################################

#################################
# Utility Function
#   When minimax has reached the terminal
#   node for small it returns winner  or 
#   the 4th depth of the large neighborhood 
#   then it returns a heurstic to guess winner

def utility(state):
  # default
  neighborhood = state[2]
  dCount=0
  rCount=0
  tieCount=0
  #pdb.set_trace()
  for district in state[1]:
    d=0
    r=0
    for block in district:
      # Tally the blocks in a district
      if neighborhood[block[0]][block[1]] == 'R':
        r+=1
      if neighborhood[block[0]][block[1]] == 'D':
        d+=1
    # Tally the district wins of the state
    if d>r:
      dCount+=1
    if r>d:
      rCount+=1
    if r==d:
      tieCount+=1
  #if state[1] == [[(1, 1), (1, 2), (2, 1), (2, 2)], [(0, 0), (0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0), (3, 1)], [(1, 3), (2, 3), (3, 2), (3, 3)]]:
  #  pdb.set_trace()

  # If R is maxPlayer return appropriate value
  #pdb.set_trace()
  if state[0] == 'R':
    if dCount > rCount:
      return -1
    if rCount > dCount: return 1
  # If D is the maxPlayer return proper value
  if state[0] == 'D':
    if dCount > rCount:
      return 1
    if rCount > dCount: return -1
  # Exhaustive case
  #if dCount == rCount: return 0
  if dCount == rCount: 
    return 0


####################################################

####################################################
# utility function for large state
def largeUtility(state):
  # default
  neighborhood = state[2]
  dCount=0
  rCount=0
  tieCount=0
  #pdb.set_trace()
  for district in state[1]:
    d=0
    r=0
    for block in district:
      # Tally the blocks in a district
      if neighborhood[block[0]][block[1]] == 'R':
        r+=1
      if neighborhood[block[0]][block[1]] == 'D':
        d+=1
    # Tally the district wins of the state
    if d>r:
      dCount+=1
    if r>d:
      rCount+=1
    if r==d:
      tieCount+=1

  dimension = range(0,8)
  arrays=[dimension, dimension]

  remaining=list(itertools.product(*arrays))

  for district in state[1]:
    for spot in district:
      if spot in remaining:
        remaining.remove(spot)

  rRemaining = 0
  dRemaining = 0
  for spot in remaining:
    if neighborhood[spot[0]][spot[1]] == 'R':
      rRemaining += 1
    if neighborhood[spot[0]][spot[1]] == 'D':
      dRemaining += 1


  # If R is maxPlayer return appropriate value
  #pdb.set_trace()
  if state[0] == 'R':
    if dCount > rCount:
      if dRemaining >  rRemaining:
        return -2
      if dRemaining == rRemaining:
        return -1
      if dRemaining <  rRemaining:
        return 0


    if rCount > dCount: 
      if rRemaining > dRemaining: 
        return 2
      if rRemaining == dRemaining:
        return 1
      if rRemaining <  dRemaining:
        return 0

    if rCount == dCount:
      if rRemaining > dRemaining:
        return 1
      if rRemaining == dRemaining:
        return 0
      if rRemaining < dRemaining:
        return -1


  # If D is the maxPlayer return proper value
  if state[0] == 'D':
    if dCount > rCount:
      if dRemaining >  rRemaining:
        return 2
      if dRemaining == rRemaining:
        return 1
      if dRemaining <  rRemaining:
        return 0


    if rCount > dCount: 
      if rRemaining > dRemaining: 
        return -2
      if rRemaining == dRemaining:
        return -1
      if rRemaining <  dRemaining:
        return 0

    if rCount == dCount:
      if rRemaining > dRemaining:
        return -1
      if rRemaining == dRemaining:
        return 0
      if rRemaining < dRemaining:
        return 1


####################################################
# Reads input file and maps small/large matrix
neighborhood = []

f = open(sys.argv[1], 'r')

for line in f:
    neighborhood.append(line.rsplit())
#####################################################


#####################################################

# Loads the appropriate move list for small/large matrix

master = []
import csv


if sys.argv[1] == "smallNeighborhood.txt":
  fp = open('master4x4.csv', 'Ur')
  data_list = []
  for line in fp:
    data_list.append(line.strip().split(','))
  fp.close()

  for numList in data_list:
    newList = [(int(numList[0]),int(numList[1])), (int(numList[2]),int(numList[3])), (int(numList[4]),int(numList[5])), (int(numList[6]),int(numList[7]))]
    master.append(newList)
  del data_list
else:
  fp = open('master8x8.csv', 'Ur')
  data_list = []
  for line in fp:
    data_list.append(line.strip().split(','))
  fp.close()

  for numList in data_list:
    newList = [(int(numList[0]),int(numList[1])), (int(numList[2]),int(numList[3])), (int(numList[4]),int(numList[5])), (int(numList[6]),int(numList[7])), (int(numList[8]),int(numList[9])), (int(numList[10]),int(numList[11])), (int(numList[12]),int(numList[13])), (int(numList[14]),int(numList[15]))]
    master.append(newList)
  del data_list
  
  validMaster=[]
  for district in master:
      if not badSubset(district): 
        validMaster.append(district)

#print len(validMaster)

'''

dimension = tuple(range(0, len(neighborhood)))

arrays=[dimension, dimension]

these=list(itertools.product(*arrays))

those=list(itertools.combinations(these, 4))

g = open(sys.argv[2], 'r')

#print len(those)



master = []
for this in those:
  tmp = list(this)
  if not validConfig(tmp): #== len(neighborhood):
    those.remove(this)
  else:
    #pdb.set_trace()
    #sort = list(this)#.sort()
    #sort.sort()
    #if sort not in master:
    master.append(this)

for part in master:
  print part

'''


############################################
# Now the Minimax Biz gets serious

# small neighborhood for R as Max
print '*************************************'
print 'Max=R and Min=D'
print ''
state = ['R',[], neighborhood]

wLT = minimax(state, master, 4, True)
if len(neighborhood) == 4:
  for i in range(1,len(neighborhood)+1):
    print 'District '+str(i)+str(wLT[1][i-1])

  print ''
  if wLT[0] == 1:
    print str(state[0])+' wins the election'
  elif wLT[0] == 0:
    print 'IT IS A TIE'
  elif wLT[0] == -1:
    print str(state[0])+' lost the election'

if len(neighborhood) == 8:
  for i in range(1,len(neighborhood)+1):
    print 'District '+str(i)+str(wLT[1][i-1])

  print ''
  if wLT[0] == 2:
    print str(state[0])+' has a great chance of winning'
  elif wLT[0] == 1:
    print str(state[0])+' has a decent chance of winning'
  elif wLT[0] == 0:
    print 'it is very evenly matched at this point'
  elif wLT[0] == -1:
    print str(state[0])+' has a decent chance of losing'
  elif wLT[0] == -2:
    print str(state[0])+' has a great chance of losing'




# small neighborhood for D as Max
print '*************************************'
print 'Max=D and Min=R'
print ''
state = ['D',[], neighborhood]
wLT = minimax(state, master, 4, True)
if len(neighborhood):
  for i in range(1,len(neighborhood)+1):
    print 'District '+str(i)+str(wLT[1][i-1])

  print ''
  if wLT[0] == 1:
    print str(state[0])+' wins the election'
  elif wLT[0] == 0:
    print 'IT IS A TIE'
  elif wLT[0] == -1:
    print str(state[0])+' lost the election'

if len(neighborhood) == 8:
  for i in range(1,len(neighborhood)+1):
    print 'District '+str(i)+str(wLT[1][i-1])

  print ''
  if wLT[0] == 2:
    print str(state[0])+' has a great chance of winning'
  elif wLT[0] == 1:
    print str(state[0])+' has a decent chance of winning'
  elif wLT[0] == 0:
    print 'it is very evenly matched at this point'
  elif wLT[0] == -1:
    print str(state[0])+' has a decent chance of losing'
  elif wLT[0] == -2:
    print str(state[0])+' has a great chance of losing'

'''
print master[0]
for pos in master[0]:
  print neighborhood[pos[0]][pos[1]]
  '''
