import tkinter as tk
import monitor_size as mns
from drag import Drag

class Canvas() :
    def __init__(self, master):
        self.master = master

    def draw_canvas(self) :
        width = mns.getWidth()
        height = mns.getHeight()
        canvas = tk.Canvas(self.master, bg="#003300", width=str(
            width * 3), height=(height * 3))

        # Canvasを配置
        canvas.place(x=-width, y=-height)

        # Canvasのドラッグ設定
        drag = Drag(False, (0, 0), self.master)
        canvas.bind("<Button>", drag.mouseDown)
        canvas.bind("<ButtonRelease>", drag.mouseRelease)
        canvas.bind("<Motion>", drag.mouseMove)

        return canvas
