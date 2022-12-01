class Drag() :
    def __init__(self) :
        self.is_mouse_down = False
        self.origin = (0, 0)
        self.master = None
        
    def __init__(self, is_mouse_down, origin, master) :
        self.is_mouse_down = is_mouse_down
        self.origi = origin
        self.master = master
        
    def mouseDown(self, event) :
        if event.num == 1 :
            self.origin = (event.x, event.y)
            self.is_mouse_down = True
            
    def mouseRelease(self, event) :
        self.is_mouse_down = False
        
    def mouseMove(self, event):
        if self.is_mouse_down:
            buf = self.master.geometry().split("+")
            self.setPos(event.x - self.origin[0] + int(buf[1]),
                        event.y - self.origin[1] + int(buf[2]),
                        )
            
    def setPos(self, x, y):
        self.master.geometry("+%s+%s" % (x, y))