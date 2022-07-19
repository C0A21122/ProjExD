
import pygame as pg
import tkinter as tk
import tkinter.messagebox as tkms
import random 

WINDOW_SIZE = pg.Rect(0, 0, 600, 700)


class Screen():
    
    def __init__(self, title, window):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(window)              
        self.rct = self.sfc.get_rect()     

class Racket():

    def __init__(self, color, scr_w, scr_h):
        self.sfc = pg.Surface((scr_w, scr_h))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.rect(self.sfc, color, (scr_w/2, scr_h-20, 100, 10), 5)  
        self.rct = self.sfc.get_rect()
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, racket_pos, scr:Screen):
        self.rct.centerx = racket_pos
        self.rct.centery = WINDOW_SIZE.bottom - 30
        key_states = pg.key.get_pressed()
        if key_states == [pg.K_LEFT]:
            self.rct.centerx -= 1
        if key_states == [pg.K_RIGHT]:
            self.rct.centerx += 1
        self.rct.clamp_ip(WINDOW_SIZE)
        self.blit(scr)

class Ball():
    
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color,(size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy
        self.bomb_count = 1
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


"""class Blocks():

    def __init__(self, color, scr: Screen):
        self.sfc = pg.Surface()
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.rect(self.sfc, color,(200, 500), 5)
        self.rct = self.sfc.get_rect() # Rect"""

def main():
    clock = pg.time.Clock()

    #ウィンドウ
    pg.display.set_caption("ブロック崩し")
    scr = Screen("ブロック崩し",
                    (600, 700))

    rckt = Racket((255, 255, 255),scr.rct.width, scr.rct.height)
    racket_pos = int(scr.rct.width / 2)
    bl = Ball((255, 255, 255),
                10,
                (+1, +1),
                scr)
    """blc = Blocks((255, 255, 255),
                    20)"""
    
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        rckt.update(racket_pos, scr)
        bl.update(scr)

        pg.display.update()
        clock.tick(60)

def check_bound(rct, scr_rct):
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right :
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom:
        tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()       #ゲームの開始
    main()
    pg.quit()       #ゲーム終了

