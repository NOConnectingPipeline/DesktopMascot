import pyautogui as pg

def getWidth() :
    scr_w = pg.size().width
    return scr_w

def getHeight() :
    scr_h = pg.size().height
    return scr_h