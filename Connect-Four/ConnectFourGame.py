'''By: Gary Huang
Date : Feb 24,2019
Description: This program is Connect Four Game.'''

import random
BOARD = []
def makingBoard (col, rows):
    '''This function will create a board based off of the user's input using ASCII characters'''
    #For every row it makes a new list and adds spaces
    for indexRow in range (rows):
        row = []
        #Appends all the spaces the list for every column
        for indexCol in range (col):
            row.append(' ')
        BOARD.append(row)
    
def usersMove (BOARD, row, col):
    '''This function is the user's move turn. It will ask the user for a row and column and see if its in range or if the space is occupied.'''
    #Input Validation
    while True:
        try:
            userCol = int(input("What col would you like to move to (1-"+str(col)+"): "))-1
        except ValueError:
            print("Sorry, invalid square. Please try again!\n")
            continue
        if userCol >= 0 and userCol <= col-1:
            if BOARD[0][userCol] == " ":
                break
            else:
                print("Sorry, invalid square. Please try again!\n")            
        else:
            print("Sorry, invalid square. Please try again!\n")
    #Checks for empty space in column
    for i in range (row-1, -1, -1):
        if BOARD[i][userCol] == " ":
            BOARD[i][userCol] = 'X'
            break

def computersMove(BOARD, row, col):
    '''This function will randomly choose the computer's move (ai).'''
    #Loops until a space is found
    while True:
        again = False
        botCol = random.randrange (col)
        for i in range (row-1, -1, -1):
            if BOARD[i][botCol] == " ":
                BOARD[i][botCol] = 'O'
                print ("I choose", i+1, "row", botCol+1,"column.")
                again = True
                break
        #If space found, it breaks
        if again:
            break

def printBoard (col, row):
    '''This function will print the board'''
    #Makes a new list
    rowOne = []
    emptySpace = [' '] * (col+1)
    print (end=' ')
    #Prints the number of columns at the top
    for columns in range (1, col+1):
        print (columns, end = " ")
    #Joins the lists index and puts '|' in between them
    for rows in BOARD:
        rowOne.append('|'+'|'.join(rows)+'|')
    rowTwo = '-'.join (emptySpace) 
    print ()
    #Prints the dashs under the numbers
    print (rowTwo)
    #Prints the dashs in the board
    for rowIndex in range (row):
        print (rowOne[rowIndex])
        print (rowTwo)

def winner (BOARD, col, row):
    '''This function will determine if there is a winner.'''
    #Checking for rows
    sameX = 0
    sameO = 0
    for rows in range (row-1):
        sameX = 0
        sameO = 0        
        for column in range (col):
            #If token is X it will add one and reset O
            if BOARD[rows][column] == 'X':
                sameX += 1
                sameO = 0
            #If token is O it will add one and reset X
            elif BOARD[rows][column] == 'O':
                sameO += 1
                sameX = 0
            #Resets the token
            else:
                sameX = 0
                sameO = 0
            #If 4 in a row the same, returns the value
            if sameX == 4 or sameO == 4:
                return BOARD[rows][column]

    #Checking for columns
    for column in range (col):
        sameX = 0
        sameO = 0        
        for rows in range (row-1):
            #If token is X it will add one and reset O
            if BOARD[rows][column] == 'X':
                sameX += 1
                sameO = 0
            #If token is O it will add one and reset X
            elif BOARD[rows][column] == 'O':
                sameO += 1
                sameX = 0
            #Resets the token
            else:
                sameX = 0
                sameO = 0
            #If 4 in a row the same, reuturns the value
            if sameX == 4 or sameO == 4:
                return BOARD[rows][column]   

    #Checking for diagonals '\'
    for column in range (col):
        try:
            sameX = 0
            sameO = 0            
            for rows in range (row):
                #If token is X it will add one and reset O
                if BOARD[rows][rows+column] == 'X':
                    sameX += 1
                    sameO = 0
                #If token is O it will add one and reset X
                elif BOARD[rows][rows+column] == 'O':
                    sameO += 1
                    sameX = 0
                #Resets the token
                else:
                    sameX = 0
                    sameO = 0
                #If 4 in a row the same, returns the value
                if sameX == 4 or sameO == 4:
                    return BOARD[rows][rows+column]
            
            for rowOne in range (row):
                #If token is X it will add one and resset O
                if BOARD[rowOne+column][rowOne] == 'X':
                    sameX += 1
                    sameO = 0
                #If token is O it will add one and reset X
                elif BOARD[rowOne+column][rowOne] == 'O':
                    sameO += 1
                    sameX = 0
                #Resets the token
                else:
                    sameX = 0
                    sameO = 0
                #If 4 in a row the same, returns the value
                if sameX == 4 or sameO == 4:
                    return BOARD[column+rowOne][rowOne]                  
        except IndexError:
            break

    #Checking for diagonals '/'
    for column in range (col):
        try:
            sameX = 0
            sameO = 0            
            for rows in range (row, -1, -1):
                #If token is X it will add one and reset O
                if BOARD[rows][rows-column] == 'X':
                    sameX += 1
                    sameO = 0
                #If token is O it will add one and reset X
                elif BOARD[rows][rows-column] == 'O':
                    sameO += 1
                    sameX = 0
                #Resets the token
                else:
                    sameX = 0
                    sameO = 0
                #If 4 in a row the same, returns the value
                if sameX == 4 or sameO == 4:
                    return BOARD[rows][rows-column]
            
            for rowOne in range (row):
                #If token is X it will add one and resset O
                if BOARD[column-rowOne][rowOne] == 'X':
                    sameX += 1
                    sameO = 0
                #If token is O it will add one and reset X
                elif BOARD[column-rowOne][rowOne] == 'O':
                    sameO += 1
                    sameX = 0
                #Resets the token
                else:
                    sameX = 0
                    sameO = 0
                #If 4 in a row the same, returns the value
                if sameX == 4 or sameO == 4:
                    return BOARD[column-rowOne][rowOne]                  
        except IndexError:
            break
    
    #Checking for spaces in the board
    space = 0
    for rows in BOARD:
        if ' ' in rows:
            space += 1
    if space == 0:
        return "tie"

def main ():
    '''This is the mainline logic of the program.'''
    #Checks if there are any winners
    try:
        file = open('HallOfFame.txt', 'r')
        print("Here is a list of winners that have beaten me:")
        count = 1
        for line in file:
            print(str(count)+'.', line.strip())
            count += 1
        file.close()
    #If no file is found then...
    except FileNotFoundError:
        print("�No Human Has Ever Beat Me..mwah-ha-ha-ha!")
    #Input validation
    move = ""
    while True:
        choice = input ("Would you like to go first?(y/n): ")
        if choice == 'Y' or choice == 'y':
            move = "First"
            break
        elif choice == 'N' or choice == 'n':
            move = "Second"
            break
    while True:
        try:
            row = int (input ("How many rows(5-7)?: "))
        except ValueError:
            print ("Invalid row.")
            continue
        if row >= 5 and row <= 7:
            break
    while True:
        try:
            col = int (input ("How many columns(6-8)?: "))
        except ValueError:
            print ("Invalid Column")
            continue
        if  col >= 6 and col <= 8:
            break
    makingBoard (col, row)
    printBoard(col, row)
    while True:
        #Alternates between user and ai until the game is over
        if move == "First":
            usersMove (BOARD, row, col)
            move = "Second"
            printBoard(col, row) 
            #Checks for results and prints them if the game is over
            if winner (BOARD, row, col) == 'X':
                print ("Congrats, you are the winner!")
                file = open ("HallOfFame.txt", 'a')
                file.write (input ("Enter your name: \n"))
                file.close()
                break
            elif winner (BOARD, row, col) == 'O':
                print ("Unfortunately, you lost!")
                break
            elif winner (BOARD, row, col) == 'tie':
                print ("Stalemate!")
                break
            printBoard(col, row) 
        elif move == "Second":
            computersMove (BOARD, row, col)
            move = "First"
            printBoard(col, row)
            #Checks for results and prints them if the game is over
            if winner (BOARD, row, col) == 'X':
                print ("Congrats, you are the winner!")
                file = open ("HallOfFame.txt", 'a')
                file.write (input ("Enter your name: \n"))
                file.close()
                break
            elif winner (BOARD, row, col) == 'O':
                print ("Unfortunately, you lost!")
                break
            elif winner (BOARD, row, col) == 'tie':
                print ("Stalemate!")
                break                  
#Calls main
main ()
print ("Good game, see ya next time!")
