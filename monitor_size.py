import pyautogui as pg # 別途インストールが必要な場合あり

def getWidth() :
    scr_w = pg.size().width
    return scr_w

def getHeight() :
    scr_h = pg.size().height
    return scr_h