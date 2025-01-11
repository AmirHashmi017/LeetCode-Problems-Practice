def isValidSudoku(board):
    ValidSoduko=[0]*10
    for i in range (9):
        for j in range(9):
            if(board[i][j]!='.'):
                index=int(board[i][j])
                ValidSoduko[index]+=1
                if(ValidSoduko[index]>1):
                    return False
        ValidSoduko[:] = [0] * 10
    
    for i in range (9):
        for j in range(9):
            if(board[j][i]!='.'):
                index=int(board[j][i])
                ValidSoduko[index]+=1
                if(ValidSoduko[index]>1):
                    return False
        ValidSoduko[:] = [0] * 10
    
    for i in range(0,9,3):
        for j in range(i,i+3,1):
            for k in range(0,3,1):
                if(board[j][k]!='.'):
                    index=int(board[j][k])
                    ValidSoduko[index]+=1
                    if(ValidSoduko[index]>1):
                        return False
        ValidSoduko[:] = [0] * 10
    for i in range(0,9,3):
        for j in range(i,i+3,1):
            for k in range(3,6,1):
                if(board[j][k]!='.'):
                    index=int(board[j][k])
                    ValidSoduko[index]+=1
                    if(ValidSoduko[index]>1):
                        return False
        ValidSoduko[:] = [0] * 10
    for i in range(0,9,3):
        for j in range(i,i+3,1):
            for k in range(6,9,1):
                if(board[j][k]!='.'):
                    index=int(board[j][k])
                    ValidSoduko[index]+=1
                    if(ValidSoduko[index]>1):
                        return False
        ValidSoduko[:] = [0] * 10
    
    return True

board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))