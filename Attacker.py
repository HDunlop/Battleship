import random
import math

def checkPossibleShipPositionsOverlap(s3,p2):
  for _ in range(len(s3)):
    currentShip = s3.pop(0)
    for currentCoords in p2[currentShip.name]:
      end = False
      while not end:
        for currentCoord in currentCoords:
          for otherShip in s3:
            for otherCoord in p2[otherShip.name]:
              if otherCoord == currentCoord:
                p2[currentShip.name].remove(currentCoords)
                end = True
        end = True
    s3.append(currentShip)
  return p2

def checkIfSizeFits(shipSize,m3,coord,direction):
  for f in range(shipSize):
    if direction == 0:
      x_coord = coord[0]
      y_coord = coord[1] + f
    elif direction == 1:
      x_coord = coord[0] + f
      y_coord = coord[1]
    elif direction == 2:
      x_coord = coord[0]
      y_coord = coord[1] - f
    else:
      x_coord = coord[0] - f
      y_coord = coord[1]
    if (x_coord > 10) or (y_coord > 10):
      return False
    elif m3[x_coord][y_coord] != "0":
      return False
  return True

def definePossiblePositionsForEveryShip(s2,m2,p1):
  for s in s2:
    for i in range(1,11):
      for j in range(1,11):
        if checkIfSizeFits(s.size,m2,(i,j),2):
          temp = []
          for k in range(s.size):
            temp.append((i,j+k))
          if s.name not in p1:
            p1[s.name] = [temp]
          else:
            p1[s.name].append(temp)
        if checkIfSizeFits(s.size,m2,(j,i),1):
          temp = []
          for k in range(s.size):
            temp.append((j+k,i))
          if s.name not in p1:
            p1[s.name] = [temp]
          else:
            p1[s.name].append(temp)
  return p1

def checkCurrentBoardState(cs,h3):
  tempCoords = []
  for coords in cs:
    for coord in coords:
      tempCoords.append(coord)
  for hitLocation in h3:
    if hitLocation not in tempCoords:
      return False
  return True

def loopRandomLocations(p3,h2):
  locFre = {}
  #need to review depth of loop
  for _ in range(100):
    current = []
    for ship,coords in p3.items():
      current.append(random.choice(coords))
    if checkCurrentBoardState(current,h2):
      for coords in current:
        for coord in coords:
          if coord not in locFre:
            locFre[coord] = 1
          else:
            locFre[coord] += 1
  return locFre




def decision(m1,s1,h1,starter):
  if (len(starter) >= 1) and (len(h1) == 0):
    print("\nToo early for logic...")
    return starter.pop(0)
  #
  # if hunter[0]:
  #   print("\nTime for some hunting bbbaaabyyyyyyyy!")
  #   choice = (0,0)
  #   print("Final decision: "+str(choice))
  #   return choice
  #   pass
  #
  # elif not hunter[0]:
  if True:
    print("Last position was not a hit")
    possibleLocations = {}
    print("\nCalling 'definePossiblePositionsForEveryShip'...")
    possibleLocations = definePossiblePositionsForEveryShip(s1,m1,possibleLocations)
    print("...returned: \n"+str(possibleLocations))

    print("\nCalling 'checkPossibleShipPositionsOverlap'...")
    possibleLocations = checkPossibleShipPositionsOverlap(s1,possibleLocations)
    print("...returned: \n"+str(possibleLocations))

    print("\nCalling 'loopRandomLocations'...")
    locationFrequencies = loopRandomLocations(possibleLocations,h1)
    print("...returned: \n"+str(locationFrequencies))

    print("\nEntering selection for loop...")
    mostFrequent = [None,-math.inf]
    for loc,fre in locationFrequencies.items():
      if fre > mostFrequent[1]:
        mostFrequent = [loc,fre]
    print("Final decision: "+str(mostFrequent))

    return mostFrequent[0]
