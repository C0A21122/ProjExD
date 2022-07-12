import pygame as pg
import sys
import random
import tkinter.messagebox as tkm

TIME = 0

class Screen():
    
    def __init__(self, title, window, bgfile):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(window)              #Surface
        self.rct = self.sfc.get_rect()                      #Rect   
        self.bgimage_sfc = pg.image.load(bgfile)            #Surface
        self.bgimage_rct = self.bgimage_sfc.get_rect()      #Rect

    def blit(self):
        self.sfc.blit(self.bgimage_sfc, self.bgimage_rct)

class Bird():

    def __init__(self, bird_img, scale, fxy):
        self.sfc = pg.image.load(bird_img)
        self.sfc = pg.transform.rotozoom(self.sfc,0 ,scale)
        self.rct = self.sfc.get_rect()
        self.rct.center = fxy
        
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
        #sfc.blit(self.sfc, self.rct)

    def upadate(self, scr: Screen):
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]    == True: self.rct.centery -= 1
        if key_states[pg.K_DOWN]  == True: self.rct.centery += 1
        if key_states[pg.K_LEFT]  == True: self.rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: self.rct.centerx += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]    == True: self.rct.centery += 1
            if key_states[pg.K_DOWN]  == True: self.rct.centery -= 1
            if key_states[pg.K_LEFT]  == True: self.rct.centerx += 1
            if key_states[pg.K_RIGHT] == True: self.rct.centerx -= 1
        self.blit(scr)

class Bomb():
    
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
        if self.bomb_count >= 3:
            self.blit()
            self.bomb_count += 1
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

def main():
    clock = pg.time.Clock()

    scr = Screen("たたかえ！こうかとん",
                (1600, 900),
                "ex04/fig/pg_bg.jpg")

    kkt = Bird("ex03/fig/6.png",
                2.0,
                (900,400))

    bm = Bomb((255, 0, 0),
                10,
                (+1, +1),
                scr)

    while True:
        global TIME
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        TIME += pg.time.get_ticks()*1000    #経過時間の取得

        kkt.upadate(scr)
        bm.update(scr)

        

        if kkt.rct.colliderect(bm.rct):
            return 

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right :
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom:
        tate = -1 # 領域外
    return yoko, tate

def game_over():
    tkm.showinfo("ゲームオーバー", f"生存時間{TIME*1000}秒")    #結果表示


if __name__ == "__main__":
    pg.init()
    main()
    game_over()
    pg.quit()
    sys.exit()