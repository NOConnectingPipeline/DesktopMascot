#cd デスクトップ/program-warehouse/python-lesson/DesktopMascot
import tkinter as tk
from motion import Motion

if __name__ == "__main__":
    root = tk.Tk()
    app = Motion(filepath = './animations/kadai05.webm', master = root)
    app.mainloop()