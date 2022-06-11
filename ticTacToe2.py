# Assignment: Week 1 - Tic-Tac-Toe
# CSE 210 - Programming with Classes
# Author: Chris Mills

from numpy import square
import os

def clear_console():
    # clears the screen of previous text
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def showBoard(board):
    clear_console()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")


def checkScore(board):
    #check horizontals
    if (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]):
        return True

    #check verticals
    if (board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]):
        return True

    # check Diagonals
    if (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
        return True

    # are there any spaces left available
    if board.count("X") + board.count("O") == 9:
        return 'draw'


    return False

def main():
    board = [1,2,3,4,5,6,7,8,9]
    currentPlayer = "X"
    showBoard(board)
    while not checkScore(board):
        if checkScore(board) == 'draw':
            break

        try:
            square = int(input("Please Choose a Space:"))-1
        except:
            print("Thanks for Playing")
            break

        if board[square] == "X" or board[square] == "O":
            print("space taken, choose another one")
            continue

        if square > 9:
            print("That is not a space")
            continue

        board[square] = currentPlayer
        currentPlayer = "X" if currentPlayer == "O" else "O"
        showBoard(board)
    if checkScore(board) == "draw":
        print("Sorry! Nobody wins!")
    else:
        print(f"Congratulations Player {'X' if currentPlayer == 'O' else 'O'}!")

if __name__ == '__main__':
    main()
