import tkinter as tk
from logic import board, function

BOARD = []
BOARD_WIDGETS = []


class LevelWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("MINESWEEPER")
        self.root.geometry("240x400+100+100")
        self.root.resizable(False, False)

        self.choose_level(root)

    def select_level_and_destroy(self, root, x, y, b):
        global BOARD
        global BOARD_WIDGETS

        board.set_level(x, y, b)
        board.set_board(x, y, b)

        BOARD = function.return_board()
        BOARD_WIDGETS = [[None for _ in range(x)] for _ in range(y)]

        root.destroy()

    def choose_level(self, root):
        self.p0_label1 = tk.Label(
            self.root, text="게임 레벨 선택", bg="#a9a9a9", font=("Arial", 12)
        )
        self.p0_label1.pack(side="top", fill="x", pady=10)

        self.p0_button_frame = tk.Frame(self.root)
        self.p0_button_frame.pack(side="top", padx=10, pady=10)

        self.p0_easy = tk.Button(
            self.p0_button_frame,
            overrelief="sunken",
            text="초급 : 9 X 9 SIZE, 💣 X 10 ",
            width=30,
            height=2,
            repeatdelay=800,
            repeatinterval=100,
            command=lambda x=9, y=9, b=10: self.select_level_and_destroy(root, x, y, b),
        )

        self.p0_normal = tk.Button(
            self.p0_button_frame,
            overrelief="sunken",
            text="중급 : 12 X 12 SIZE, 💣 X 24 ",
            width=30,
            height=2,
            repeatdelay=800,
            repeatinterval=100,
            command=lambda x=12, y=12, b=24: self.select_level_and_destroy(
                root, x, y, b
            ),
        )

        self.p0_hard = tk.Button(
            self.p0_button_frame,
            overrelief="sunken",
            text="고급 : 20 X 16 SIZE, 💣 X 64 ",
            width=30,
            height=2,
            repeatdelay=800,
            repeatinterval=100,
            command=lambda x=20, y=16, b=64: self.select_level_and_destroy(
                root, x, y, b
            ),
        )

        self.p0_easy.pack(fill="both", anchor="center", pady=30)
        self.p0_normal.pack(fill="both", anchor="center", pady=30)
        self.p0_hard.pack(fill="both", anchor="center", pady=30)


class MainWindow:
    def __init__(self, root):
        global BOARD

        self.root = root
        self.root.title("MINESWEEPER")
        self.root.resizable(False, False)

        BOARD_SIZE_X = len(BOARD[0])
        BOARD_SIZE_Y = len(BOARD)

        self.create_widgets(root, BOARD_SIZE_X, BOARD_SIZE_Y)

    def on_click(self, root, x, y):
        global BOARD_WIDGETS

        target_btn = BOARD_WIDGETS[y][x]

        if function.return_cell_number(x, y) == 2:
            result = "💣"
            target_btn.config(background="#ff2222")
        else:
            result = function.count_cell_number(x, y)
            target_btn.config(background="#a9a9a9")

        self.label3.config(text=result)
        target_btn.config(text=result)
        target_btn.config(state="disabled")

    def create_widgets(self, root, x, y):
        global BOARD_WIDGETS

        menubutton = tk.Menubutton(
            root, text="메뉴", width=2, anchor="w", relief="solid"
        )
        menubutton.pack(side="top", fill="x", ipadx=1)

        menu = tk.Menu(menubutton, tearoff=0)
        menu.add_radiobutton(label="난이도 조절")
        menu.add_separator()

        menubutton["menu"] = menu

        self.label1 = tk.Label(
            self.root, text="첫 번째 상단 라벨입니다.", bg="#a9a9a9", font=("Arial", 12)
        )
        self.label1.pack(side="top", fill="x", pady=2)

        self.label2 = tk.Label(self.root, text="😎", bg="#a9a9a9", font=("Arial", 12))
        self.label2.pack(side="top", fill="x", pady=2)

        self.label3 = tk.Label(self.root, text=" ", bg="#a9a9a9", font=("Arial", 12))
        self.label3.pack(side="bottom", fill="x", pady=2)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side="top", padx=10, pady=10)

        for j in range(y):
            for i in range(x):
                self.btn = tk.Button(
                    self.button_frame,
                    overrelief="sunken",
                    text=" ",
                    width=4,
                    height=2,
                    background="SystemButtonFace",
                    repeatdelay=1000,
                    repeatinterval=10,
                    state="active",
                    command=lambda x_idx=i, y_idx=j: self.on_click(root, x_idx, y_idx),
                )

                self.btn.grid(row=j, column=i)
                BOARD_WIDGETS[j][i] = self.btn
