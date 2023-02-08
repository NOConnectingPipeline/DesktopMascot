#cd デスクトップ/program-warehouse/python-lesson/DesktopMascot
import tkinter as tk
from motion import Motion
import sys
import threading

#sys.setrecursionlimit(67108864)
#threading.stack_size(1024*1024)

root = tk.Tk()
if __name__ == "__main__":
    app = Motion(filepath = './animations/sans.gif', master = root)
    app.mainloop()