import tkinter as tk
import random

BOARD_SIZE_X = 9
BOARD_SIZE_Y = 9
NUMBER_OF_BOMBS = 10


class board:    
    def set_level(x, y, b):      
        global BOARD_SIZE_X, BOARD_SIZE_Y, NUMBER_OF_BOMBS, BOARD
        
        BOARD_SIZE_X = x
        BOARD_SIZE_Y = y
        NUMBER_OF_BOMBS = b
        
        BOARD = [[0 for _ in range(BOARD_SIZE_X)] for _ in range(BOARD_SIZE_Y)]
            
    def set_board(x, y, b):
        global BOARD
        
        for _ in range(b):
            i = random.randrange(0, y)
            j = random.randrange(0, x)
            
            BOARD[i][j] = 2
            print (f"x = {i}, y = {j}") #터미널 확인용 (임시)
        
class function:
    def count_cell_number (x, y):
        global BOARD_SIZE_X, BOARD_SIZE_Y, BOARD
        count = 0
        directions = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1), 
                    (1, -1), (1, 0), (1, 1)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < BOARD_SIZE_Y and 0 <= ny < BOARD_SIZE_X):
                if (BOARD[nx][ny] == 2): count += 1
        
        return count
    
    def return_cell_text (x, y):
        if (BOARD[x][y] == 2): return "💣"
        else: return (function.count_cell_number (x, y))
        
    def return_board_size():
        global BOARD_SIZE_X, BOARD_SIZE_Y
        
        x = BOARD_SIZE_X
        y = BOARD_SIZE_Y
        return [x, y]
    
    