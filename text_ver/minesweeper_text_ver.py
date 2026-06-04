import random

BOARD_SIZE_X = 9

BOARD_SIZE_Y = 9

END = 5

BOARD = [[0 for _ in range (BOARD_SIZE_X)] for _ in range (BOARD_SIZE_Y)]

def set_mines():
    for _ in range (10):
        mine_x = random.randint (0, 8)
        mine_y = random.randint (0, 8)
        
        BOARD[mine_x][mine_y] = 2

def count_cell_number (x, y):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1), 
                  (1, -1), (1, 0), (1, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if (0 <= nx < BOARD_SIZE_X and 0 <= ny < BOARD_SIZE_Y):
            if (BOARD[nx][ny] == 2): count += 1
            
    return count
            

def print_board_top (a, status):
    if (status == 'win'):
        print (f"---- Win!!! (Turn : {a}) ----")
        print (f"------------ \U0001F60E -----------")
    elif (status == 'lose'):
        print (f"---- Lose... (Turn : {a}) ----")
        print (f"------------ \U0001F635 ------------")
    else:
        print (f"--------- Turn : {a} ---------")
        print (f"------------ \U0001F642 ------------")

def print_board (a, status):
    print_board_top (a, status)
    
    for i in range (BOARD_SIZE_Y):
        for j in range (BOARD_SIZE_X):
            if (status == 'on play'):
                if (BOARD[i][j] != 1): print ("\U00002B1C", end = '')
                else:
                    if (count_cell_number (i, j) == 0): print ("\U00002B1B", end = '')
                    else:
                        code = str (count_cell_number (i, j)) + "\uFE0F\u20E3"
                        print (code, end = '')
                    
                        print (" ", end = '')
            elif (status == 'lose'):
                if (BOARD[i][j] == 2): print ("\U0001F4A3", end = '')
                elif (BOARD[i][j] == 3): print ("\U0001F7E5", end = '')
                else: print ("\U00002B1C", end = '')
            else:
                if (BOARD[i][j] == 2): print ("\U0001F4A3", end = '')
                elif (count_cell_number (i, j) == 0): print ("\U00002B1B", end = '')
                else:
                    code = str (count_cell_number (i, j)) + "\uFE0F\u20E3"
                    print (code, end = '')
                
                    print (" ", end = '')
        print()

def remove_cell(x, y):
    if (BOARD[x][y] == 1):
        return 0
    elif (BOARD[x][y] == 0):
        BOARD[x][y] = 1
        return 1
    else:
        BOARD[x][y] = 3
        return 3

def main():
    turn = 0
    status = 'on play'
    
    set_mines()
    
    while (True):
        print_board (turn, status)
        
        if (status != 'on play'): break
        else:
            x, y= map (int, input("X, Y : ").split(', '))
            
            if (turn ==  0): BOARD[x - 1][y - 1] = 0
            
            k = remove_cell (x - 1, y - 1)
            
            if (k != 0): turn += 1
            
            if (k == 3): status = 'lose'
            elif (turn == END and k != 3): status = 'win'
    
    return 0
    
if (__name__ == "__main__"): main()