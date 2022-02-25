def print_board(board):
    for row in board:
        print(row)
    print('\n')
        
def col_row_check(column, row):
    if column <= 2 and row <= 2:
        return True
    else:
        return False
    
def win_check(board):
    for Row in board:
        if Row[0] == 0:
            continue
        elif Row[0] == Row[1] == Row[2]:
            return True
        else:
            continue
            
    for Column in range(0,3):
        if board[0][Column] == 0:
            continue
        elif board[0][Column] == board[1][Column] == board[2][Column]:
            return True
        else:
            continue
        
    for Diagonal in range(1,3):
        if Diagonal == 1:
            if board[0][0] == 0:
                continue
            elif board[0][0] == board[1][1] == board[2][2]:
                return True
        
        elif Diagonal == 2:
            if board[0][2] == 0:
                continue
            elif board[0][2] == board[1][1] == board [2][0]:
                return True
            
    return False                            
    
def play_tic_tac_toe():
    board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    move = 1
    print_board(board)         

    while move <= 9:
        #Player turn
        if move % 2 != 0 :
            print('Player one')
            player_number = 1
        else:
            print('Player two')
            player_number = 2
            
        #Row/Column input    
        row = int(input('Choose row (0, 1, 2) '))
        column = int(input('Choose column (0, 1, 2) '))
        
        #Validation
        if col_row_check(column, row) == True:
            if board[row][column] == 0:
                board[row][column] = player_number
                print_board(board)
                move += 1
            else:
                print('Space already occupied')
                continue
        else:
            print('Column and row number should be 0, 1 or 2')
            continue
           
        #Check for winner    
        if move >= 6:
            if win_check(board) == True:
                if move % 2 == 0:
                    print('Player one is winner')
                    break
                elif move % 2 != 0:
                    print('Player two is winner')
                    break
    else:
        print('Tie') 

play_tic_tac_toe()


                           
                
             
