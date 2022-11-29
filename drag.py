class Drag() :
    def __init__(self) :
        self.is_mouse_down = False
        self.origin = (0, 0)
        
    def mouseDown(self, event) :
        if event.num == 1 :
            self.origin = (event.x, event.y)
            self.is_mouse_down = True
            
    def mouseRelease(self, event) :
        self.is_mouse_down = False