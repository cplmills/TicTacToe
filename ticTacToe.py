board = [[1,2,3],[4,5,6],[7,8,9]]

def checkScore(board):
    #  check horizontal rows
    if board[0].count('X') == 3 or board[1].count('X') == 3 or board[2].count('X') == 3:
        return "X"
    elif board[0].count('O') == 3 or board[1].count('O') == 3 or board[2].count('O'):
        return "O"
    
    #  check vertical rows
    for i in range(3):
        if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
            return "X"
        elif board[i][0] == 'O' and board[i][0] == 'O' and board[i][0] == "O":
            return "O"

    #  check diagonal rows
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return "O"
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return "O"

    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return "X"
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return "X"

    return "no winner"

def showBoard(board):
    print(f"{board[0]}/n{board[1]}/n{board[2]}")

def main():
    showBoard(board)
    print('score is ' + checkScore([['X','O','X'],[4,5,6],[7,8,9]]))

if __name__ == '__main__':
    main()