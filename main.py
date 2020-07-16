from termcolor import colored

from DisplayBoard import settingUpColoUUUUrs
from DisplayBoard import action
from DisplayBoard import settingUpBoard
from DisplayBoard import drawCoords

from PlacingShips import defineOptions
from PlacingShips import refineOptionsByProxToEdgeAndCentre

from minorFunctions import create2DListOfMoves
from minorFunctions import printMoves

from ShipClass import Ship

from Attacker import decision

def shipPlacement(size):
    done = False
    while not done:
        options = defineOptions(permValues)
        choice = refineOptionsByProxToEdgeAndCentre(options,size,permValues)
        if choice != None:
            done = True
    return choice


def placeShip(choice,currentShip):
    x = choice[0][0]
    y = choice[0][1]
    shipCoords = []
    for i in range(currentShip.size):
        if choice[1] == 0:
            action(x,y-i,black)
            permValues.append((x,y-i))
            shipCoords.append((x,y-i))
        elif choice[1] == 1:
            action(x+i,y,black)
            permValues.append((x+i,y))
            shipCoords.append((x+i,y))
        elif choice[1] == 2:
            action(x,y+i,black)
            permValues.append((x,y+i))
            shipCoords.append((x,y+i))
        else:
            action(x-i,y,black)
            permValues.append((x-i,y))
            shipCoords.append((x-i,y))
    return shipCoords



def main():
    global moves,permValues,red,blue,black,mapper,sizeBtwn
    moves,permValues = create2DListOfMoves()

    red,blue,black = settingUpColoUUUUrs()
    mapper,sizeBtwn = settingUpBoard()
    drawCoords(moves)

    starter = [
      (5,5),
      (6,6),
      (4,4),
      (7,7),
      (3,3),
      (8,8),
      (7,3)]

    carrier = Ship("Carrier",5)
    battleship = Ship("Battleship",4)
    cruiser = Ship("Cruiser",3)
    submarine = Ship("Submarine",3)
    destroyer = Ship("Destroyer",2)
    remainingShips = [carrier,battleship,cruiser,submarine,destroyer]
    hitCoordinates = []
    didHit = False
    lastHitCoord = (0,0)

    for i in range(len(remainingShips)):
        current = remainingShips[i]
        current.addCoords(placeShip(shipPlacement(current.size),current))

    while True:
        printMoves(moves)
        if didHit:
            pass
        if len(remainingShips) == 0:
            break
        _ = input("Press anything to continue\n")

        attack = decision(moves,remainingShips,hitCoordinates,starter)

        for i in range(len(remainingShips)):
            current = remainingShips[i]
            returnValue = current.checkDidHit(attack)
            if returnValue != 0:
                print(colored("\nAI made a hit!",'green'))
                if not didHit:
                    lastHitCoord = attack
                didHit = True
                hitCoordinates.append(attack)
                action(attack[0],attack[1],red)
                if returnValue != 2:
                    remainingShips.append(current)
                didHit = False
            remainingShips.append(current)

        if not didHit:
            print(colored("\nAI missed",'red'))
            action(attack[0],attack[1],blue)
            moves[attack[1]][attack[0]] = "M"

    print("Game was ended.")

main()
