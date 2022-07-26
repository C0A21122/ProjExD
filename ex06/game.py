import pygame as pg
import sys
import tkinter.messagebox as tkm


class Screen: #Screen
    def __init__(self, title, wh,image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)         
        self.rct = self.sfc.get_rect() 
        self.bgi_sfc = pg.image.load(image)       
        self.bgi_rct = self.bgi_sfc.get_rect()           

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bou: #ボールを反射する棒
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)                       
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()                       
        self.rct.center = xy
    
    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr: Screen): #棒の左右移動
        key_states = pg.key.get_pressed() 
        if key_states[pg.K_LEFT] : 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT] : 
            self.rct.centerx += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_LEFT] :
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT] :
                self.rct.centerx -= 1
        
        self.blit(scr)


class Ball: #ボール
    def __init__(self, color ,size, xy, vxy):
        self.sfc = pg.Surface((size*2,size*2)) 
        self.sfc.set_colorkey((0,0,0)) 
        pg.draw.circle(self.sfc, color, (size,size),size)
        self.rct = self.sfc.get_rect() 
        self.rct.center = xy
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr :Screen): #ボールの移動
        self.rct.move_ip(self.vx, self.vy)

        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate

        self.blit(scr)

    def bound(self): #ボールが棒に当たったら反射する処理
        self.vy *= -1.0

#下田,近藤　Line68~79
class Score(): #Score
    def __init__(self, x, y):
        self.sysfont = pg.font.SysFont(None, 25)
        self.score = 0
        (self.x, self.y) = (x, y)

    def draw(self, scr:Screen): #Scoreの表示
        img = self.sysfont.render("SCORE:"+str(self.score), True, (255,255,250))
        scr.sfc.blit(img, (self.x, self.y))

    def add_score(self, x): #Scoreの増加
        self.score += x

#近藤,村田 Line82~98
class Start(): #Start
    def __init__(self, x, y):
        self.sysfont = pg.font.SysFont(None, 25)
        self.score = 0
        (self.x, self.y) = (x, y)

    def draws(self, scr:Screen): #Startの表示
        img = self.sysfont.render("GameStart=s", True, (255,0,0))
        scr.sfc.blit(img, (self.x, self.y))

    def drawr(self, scr:Screen): #restartの表示
        img = self.sysfont.render("Restart=r", True, (255,0,250))
        scr.sfc.blit(img, (self.x, self.y))

    def drawq(self, scr:Screen): #Quitgameの表示
        img = self.sysfont.render("Quitgame=q", True, (0,255,255))
        scr.sfc.blit(img, (self.x, self.y))

#近藤,山口 Line101~112
class Life(): #残機
    def __init__(self, x, y):
        self.sysfont = pg.font.SysFont(None, 25)
        self.life = 3
        (self.x, self.y) = (x, y)

    def draw(self, scr:Screen): #残機の表示
        img = self.sysfont.render("Life:"+str(self.life-1), True, (255,255,250))
        scr.sfc.blit(img, (self.x, self.y))

    def deg_life(self): #残機の減少
        self.life -= 1

#澤井,下田,小嶋 Line115~140
block = []
for i in range(8): #ブロックの情報リスト
    for j in range(10):
        block.append({"x":i*80+5,"y":30+j*40+10,"st":2})


#ブロック関数
def Block(scr:Screen, ball:Ball, score:Score, a):
    for i in range(len(block)):
        x = block[i]["x"]
        y = block[i]["y"]
        st = block[i]["st"]

        if ball.rct.centery <= y+30 and ball.rct.centerx >= x-10 and ball.rct.centerx <= x+60 and (st == 1 or st == 2):
            ball.vy *=-1
            block[i]["st"] -= 1
            if st == 1:
                score.add_score(20)
            else:
                score.add_score(10)    

        #ブロックの表示
        if st == 1:
            pg.draw.rect(scr.sfc, (a/2, a/2, a/2), (x, y, 70, 30))
        if st == 2:
            pg.draw.rect(scr.sfc, (a, a, a), (x, y, 70, 30))


def main():
    clock = pg.time.Clock()
    scr = Screen("ブロックを崩せ", (650, 1000),"fig/black.jpg")
    bou = Bou("fig/bou.jpeg",1,(330,900))
    ball = Ball((255,0,0), 10, (325,500),(+1, +1))
    score = Score(10, 10)
    life = Life(130,10)
    start = Start(230, 10)
    restart = Start(380, 10)
    quit = Start(500, 10)
    a = 0

    while True:
        scr.blit()
        Block(scr, ball, score, a = 255)
        bou.update(scr)
        score.draw(scr)
        life.draw(scr)
        start.draws(scr)
        restart.drawr(scr)
        quit.drawq(scr)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        #近藤,村田,小嶋 Line170~197
        key_states = pg.key.get_pressed() 
        if key_states[pg.K_r] : #キー(r)を押したらリスタート
            return main()

        if key_states[pg.K_q]:  #キー(q)を押したら終了
            return
        
        if key_states[pg.K_s]:  #キー(s)を押したらスタート
            a = 1
        
        if a == 1:  #ゲームの動作可否
            ball.update(scr)

        if bou.rct.colliderect(ball.rct): #ボールが棒に当たったら反射する関数を呼び出す
            ball.bound()

        if ball.rct.bottom > scr.rct.bottom: #床に触れた場合
            life.deg_life()
            ball = None
            a = 0
            if ball == None:
                ball = Ball((255,0,0), 10, (325,500), (+1,+1))

        if life.life == 0: #残機が0ならゲームオーバー
            return tkm.showinfo("ゲームオーバー", f"残機が{life.life}になったのでゲームオーバーです")
        
        if score.score >= 100:
            return tkm.showinfo("ゲームクリア", f"Scoreが{score.score}になりました。ゲームクリアおめでとう！！")

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    global life
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right :
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top or scr_rct.bottom < rct.bottom:
        tate = -1 # 領域外
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()