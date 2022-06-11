from math import ceil
board = [[1,2,3],[4,5,6],[7,8,9]]

def checkSpace(space):
    if int(space) in board[ceil(space/3)-1]:
        return True
    else:
        print(f"cant find {space} in board[{ceil(space/3)-1}]")
        return False

def checkScore(board):
    #  check horizontal rows
    if board[0].count('X') == 3 or board[1].count('X') == 3 or board[2].count('X') == 3:
        return "win"
    elif board[0].count('O') == 3 or board[1].count('O') == 3 or board[2].count('O'):
        return "win"
    
    #  check vertical rows
    for i in range(3):
        if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
            return "win"
        elif board[i][0] == 'O' and board[i][0] == 'O' and board[i][0] == "O":
            return "win"

    #  check diagonal rows
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return "win"
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return "win"

    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return "wins"
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return "win"

    allSpacesGone = True
    for s in board:
        for t in s:
            print(f"{t} - {type(t)}")
            if type(t) == 'int':
                allSpacesGone = False
        # if str(s) not in board:
        #     allSpacesGone = True
        # else:
        #     allSpacesGone = False
    if allSpacesGone:
        print("all spaces gone")
        return "drawer"

    return "no winner"

def showBoard(board):
    print()
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print('-+-+-')
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print('-+-+-')
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")
    print()

def main():
    # print('score is ' + checkScore([['X','O','X'],[4,5,6],[7,8,9]]))
    currentPlayer = "X"

    while(checkScore(board)!="win") or (checkScore(board)!="drawer"):
        showBoard(board)
        try:
            space = int(input("Please Choose a Space:"))
        except:
            print("Thanks for Playing")
            break

        if space > 9:
            print("That is not a space")
            continue
        if not checkSpace(space):
            print("That space is not available")
            continue
        rowNum = ceil(space/3) 
        if rowNum-1 == 0:
            modifier = 1
        elif rowNum-1 == 1:
            modifier = 4
        else:
            modifier = 7
        board[rowNum-1][space-1 if space < 4 else space-modifier] = currentPlayer
        print(currentPlayer + checkScore(board))
        currentPlayer = "X" if currentPlayer == "O" else "O"


if __name__ == '__main__':
    main()