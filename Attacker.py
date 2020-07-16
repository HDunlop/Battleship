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
        elif m3[y_coord][x_coord] != "0":
            return False
    return True

def definePossiblePositionsForEveryShip(s2,m2,p1):
    for s in s2:
        for i in range(1,11):
            for j in range(1,11):
                for c in range(2):
                    if c == 0:
                        x = i
                        y = j
                    else:
                        x = j
                        y = i
                    if checkIfSizeFits(s.size,m2,(x,y),0):
                        temp = []
                        for k in range(s.size):
                            temp.append((x,y+k))
                        if s.name not in p1:
                            p1[s.name] = [temp]
                        else:
                            p1[s.name].append(temp)
                    if checkIfSizeFits(s.size,m2,(x,y),1):
                        temp = []
                        for k in range(s.size):
                            temp.append((x+k,y))
                        if s.name not in p1:
                            p1[s.name] = [temp]
                        else:
                            p1[s.name].append(temp)
                    if checkIfSizeFits(s.size,m2,(x,y),2):
                        temp = []
                        for k in range(s.size):
                            temp.append((x,y-k))
                        if s.name not in p1:
                            p1[s.name] = [temp]
                        else:
                            p1[s.name].append(temp)
                    if checkIfSizeFits(s.size,m2,(x,y),3):
                        temp = []
                        for k in range(s.size):
                            temp.append((x-k,y))
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
    for _ in range(10000):
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
        return starter.pop(0)

    counter = 0
    end = False
    while not end:
        counter += 1
        print("\nWhile loop "+str(counter))
        possibleLocations = {}
        possibleLocations = definePossiblePositionsForEveryShip(s1,m1,possibleLocations)
        possibleLocations = checkPossibleShipPositionsOverlap(s1,possibleLocations)
        locationFrequencies = loopRandomLocations(possibleLocations,h1)

        mostFrequent = [None,-math.inf]
        for loc,fre in locationFrequencies.items():
            if (fre > mostFrequent[1]) and (loc not in h1) and (m1[loc[1]][loc[0]] != "M"):
                mostFrequent = [loc,fre]

        if mostFrequent[0] != None:
            print("Final decision: "+str(mostFrequent))
            end = True
            return mostFrequent[0]
