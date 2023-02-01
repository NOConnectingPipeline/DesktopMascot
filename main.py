#cd デスクトップ/program-warehouse/python-lesson/DesktopMascot
import tkinter as tk
from motion import Motion
import keyboard

root = tk.Tk()
if __name__ == "__main__":
    app = Motion(filepath = './animations/6bfb34d3.gif', master = root)
    app.mainloop()