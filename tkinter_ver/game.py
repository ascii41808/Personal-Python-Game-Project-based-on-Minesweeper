import tkinter as tk
from gui import LevelWindow, MainWindow

if __name__ == "__main__":
    root1 = tk.Tk()
    app0 = LevelWindow(root1)
    root1.mainloop()
    root2 = tk.Tk()
    app = MainWindow(root2)
    root2.mainloop()
