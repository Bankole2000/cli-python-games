"""
File: connect4.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Project #1
Task: Connect 4 game
"""

noOfRows = 7  # Set number of rows (must be > 4)
noOfColumns = 7  # Set no of columns (must be > 4)
player1Icon = "X"  # Set player 1 Icon
player2Icon = "0"  # Set Player 2 Icon
# 2d list for field data = Should be noOfRows X noOfColumns
currentField = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
]


# Draw field at the end of the game
def drawField(field):
    practicalField = zip(*field)
    for row in practicalField:
        print(row)


# re-render the board after every turn
def makeBoard(rows, columns, field):
    for i in range(columns * 2):
        if i % 2 == 0:
            print(int(i/2)+1, end="")
        else:
            print(" ", end="")
    print("")
    for row in range(rows * 2 - 1):
        if row % 2 == 0:
            practicalRow = int(row/2)
            for column in range(1, (columns*2)):
                if column % 2 == 1:
                    practicalColumn = int((column - 1)/2)
                    if column != (columns * 2) - 1:
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end="")
        else:
            print("-"*(columns*2-1))
    return True


# render Initial (empty board)
makeBoard(noOfRows, noOfColumns, currentField)


# Check winner after every move
def checkWinner(field, icon):
    # Check horizontally
    for i in range(noOfColumns):
        for j in range(noOfRows - 3):
            if field[j][i] == field[j+1][i] == field[j+2][i] == field[j+3][i] == icon:
                return True

    # Check vertically
    for i in range(noOfColumns - 3):
        for j in range(noOfRows):
            if field[j][i] == field[j][i+1] == field[j][i+2] == field[j][i+3] == icon:
                return True

    # Check Right leaning diagonals
    for i in range(noOfColumns - 3):
        for j in range(noOfRows - 3):
            if field[j][i] == field[j+1][i+1] == field[j+2][i+2] == field[j+3][i+3] == icon:
                return True

    # Check Left leaning diagonals
    for i in range(noOfColumns - 3):
        for j in range(3, noOfRows):
            if field[j][i] == field[j-1][i+1] == field[j-2][i+2] == field[j-3][i+3] == icon:
                return True
    return False


# Check if game is draw (i.e. all spaces full)
def checkDraw(field):
    if any(" " in sublist for sublist in field):
        return False
    else:
        return True


# Function to drop icon to appropriate row in column
def drop(column, field):
    i = noOfRows
    while i >= 0:
        i -= 1
        if field[column][i] == " ":
            return i
            break

    return -1


# Player init - Set first player
player = 1
playerIcon = player1Icon
# Game start
while(True):
    print("Players turn: Player ", player, " - ", playerIcon)
    MoveColumn = int(input(f"Enter a column (1 - {noOfColumns}):\n"))
    while True:
        if MoveColumn not in range(1, noOfColumns+1):
            print(f"This move isn't possible - please retry")
            MoveColumn = int(input(f"Enter the column (1 - {noOfColumns}):\n"))
        else:
            break
    MoveColumn -= 1
    MoveRow = drop(MoveColumn, currentField)
    while True:
        if MoveRow == -1:
            print(f"This Column is full - please retry")
            MoveColumn = int(input(f"Enter the column (1 - {noOfColumns}):\n"))
            MoveColumn -= 1
        else:
            break
        MoveRow = drop(MoveColumn, currentField)
    if player == 1:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = player1Icon
            gameWon = checkWinner(currentField, player1Icon)
            if gameWon:
                drawField(currentField)
                print(f"Game Over: Winner is Player {player} - {player1Icon}")
                break
            player = 2
            playerIcon = player2Icon
        else:
            print("Sorry, can't move there - Please try again")
    else:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = player2Icon
            gameWon = checkWinner(currentField, player2Icon)
            if gameWon:
                drawField(currentField)
                print(f"Game Over: Winner is Player {player} - {player2Icon}")
                break
            player = 1
            playerIcon = player1Icon
        else:
            print("sorry, can't move there - Please try again")
    makeBoard(noOfRows, noOfColumns, currentField)
    # Check if draw
    gameDraw = checkDraw(currentField)
    if gameDraw:
        drawField(currentField)
        print("Game is a Draw")
        break

# Game end
print("Thank you for playing")
