
import random
import pygame
import sys
import tkinter.messagebox as tkm

def main():
    global progress_time

    pygame.display.set_caption("逃げろ！こうかとん")    #ウィンドウの名前
    screen = pygame.display.set_mode((1600,900))       #ウィンドウ
    clock = pygame.time.Clock()
    screen_rect = screen.get_rect()

    #背景
    bg_iamge = pygame.image.load("ex04/fig/pg_bg.jpg")  
    bg_rect = bg_iamge.get_rect()
    screen.blit(bg_iamge, bg_rect)

    #こうかとん
    tori_img = pygame.image.load("ex03/fig/2.png")      
    tori_img = pygame.transform.rotozoom(tori_img,0, 2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400

    #爆弾の作成
    vx, vy = 1, 1
    bomb_image = pygame.Surface((50,50))   #描画用surface(幅,高さ)を生成する
                                                #四角が生成される
    pygame.draw.circle(bomb_image, (255, 0, 0),  #色
                                    (25, 25),  #位置
                                    22)       #半径
    bomb_rect = bomb_image.get_rect()
    bomb_rect.centerx = random.randint(0, screen_rect.width) #ウィンドウの外に出ない乱数
    bomb_rect.centery = random.randint(0, screen_rect.height)
    bomb_image.set_colorkey((0,0,0)) #黒色を透過

   

    while True:
        screen.blit(bg_iamge, bg_rect)  #背景の貼り付け
        
        #生存時間の表示
        progress_time = pygame.time.get_ticks()/1000    #経過時間の取得
        #fonto = pygame.font.Font(None, 80)              
        #char = progress_time
        #txt = fonto.render(str(char), True, (0,0,0))
        #screen.blit(txt, (1450,10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        key_list = pygame.key.get_pressed() #辞書
        #各キーを押したときの反応
        ##領域外にでそうなとき
        if key_list[pygame.K_UP] == True and tori_rect.centery != (screen_rect.top):   
            tori_rect.centery -= 1
        if key_list[pygame.K_DOWN] == True and tori_rect.centery != (screen_rect.bottom):  
            tori_rect.centery += 1
        if key_list[pygame.K_RIGHT] == True and tori_rect.centerx != (screen_rect.right):
            tori_rect.centerx += 1
        if key_list[pygame.K_LEFT] == True and tori_rect.centerx != (screen_rect.left): 
            tori_rect.centerx -= 1 

        """
        if check_bound(tori_rect, screen_rect) != (1, 1):
            tori_rect.center
        """
        screen.blit(tori_img, tori_rect)    #こうかとんの貼り付け

        ##爆弾の移動
        bomb_rect.move_ip(vx,vy)

        #爆弾が領域外に行きそうなとき
        if bomb_rect.centerx == (screen_rect.width) or bomb_rect.centerx == (screen_rect.left):
            vx *= -1
        if bomb_rect.centery == (screen_rect.height) or bomb_rect.centery == (screen_rect.top):
            vy *= -1
        
        screen.blit(bomb_image, bomb_rect)  #爆弾の貼り付け

        pygame.display.update()
        clock.tick(1000)


        #爆弾と接触したか
        if pygame.Rect.colliderect(tori_rect, bomb_rect):
            return

def game_over():    #接触した後
    tkm.showinfo("ゲームオーバー", f"生存時間{progress_time}秒")    #結果表示


"""
def check_bound(rect, sc_rect): #rectはこうかとん、または爆弾  sc_rectはスクリーン
    varx, vary = +1, +1 #領域内

    if rect.left < sc_rect.left or sc_rect.right < rect.right:  #横方向にはみ出たら
        varx = -1
    if rect.top < sc_rect.top or sc_rect.bottom < rect.bottom:  #縦方向にはみ出たら
        vary = -1
    return varx,vary
"""



if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    main()
    game_over()
    pygame.quit()
    pygame.font.quit()
    sys.exit()