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

        for index in range(1, b + 1):
            i = random.randrange(0, x)
            j = random.randrange(0, y)

            BOARD[j][i] = 2
            print(f"bomb{index}: BOARD[{j}][{i}]")  # 터미널 확인용 (임시)


class function:
    def count_cell_number(x, y):
        global BOARD_SIZE_X, BOARD_SIZE_Y, BOARD
        count = 0
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < BOARD_SIZE_X and 0 <= ny < BOARD_SIZE_Y:
                if BOARD[ny][nx] == 2:
                    count += 1

        return count

    def return_board():
        global BOARD

        return BOARD

    def return_cell_number(x, y):
        global BOARD

        return BOARD[y][x]
