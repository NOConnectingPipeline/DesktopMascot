import cv2

class Capture() :
    def __init__(self, master, filepath):
        self.master = master
        self.filepath = filepath

    def new_capture(self) :
        capture = cv2.VideoCapture(self.filepath)
        return capture