from termcolor import colored

def create2DListOfMoves():
    permValues = ["0 ","A","B","C","D","E","F","G","H","I","J","1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10",(5,5),(5,6),(6,5),(6,6),(1,1),(10,10),(1,10),(10,1)]
    letters = ["A","B","C","D","E","F","G","H","I","J"]
    moves = []
    for i in range(11):
        temp = []
        for j in range(11):
            toAdd = "0"
            if (j == 0) and (i != 0):
                if i == 10:
                    toAdd = str(i)
                else:
                    toAdd = str(i) + " "
            if (len(letters) > 0) and (i == 0) and (j != 0):
                toAdd = letters.pop(0)
            if (i == 0) and (j == 0):
                toAdd = "0 "
            temp.append(toAdd)
        moves.append(temp)
    return moves,permValues

def printMoves(copy1):
    for row in copy1:
        for item in row:
            if item == "M":
                print(colored(item,'red'),end=' ')
            elif item == "X":
                print(colored(item,'green'),end=' ')
            elif item == "0":
                print(colored(item,'white'),end=' ')
            elif item == "0 ":
                print("\n"+colored(item,'red'),end=' ')
            else:
                print(colored(item,'blue'),end=' ')
        print()
    print()

def createTempList(copy2):
    temp = []
    for copy_value in copy2:
        temp.append(copy_value)
    return temp
