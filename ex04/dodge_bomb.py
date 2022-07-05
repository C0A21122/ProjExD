import random
import pygame
import sys

def main():
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
    vx =1
    vy =1
    bomb_image = pygame.Surface((100,100))   #描画用surface(幅,高さ)を生成する
                                                #四角が生成される
    pygame.draw.circle(bomb_image, (255, 0, 0),  #色
                                    (50, 50),  #位置
                                    10)       #半径
    bomb_rect = bomb_image.get_rect()
    bomb_rect.centerx = random.randint(0, screen_rect.width) #ウィンドウの外に出ない乱数
    bomb_rect.centery = random.randint(0, screen_rect.height)
    bomb_image.set_colorkey((0,0,0)) #黒色を透過

    while True:
        screen.blit(bg_iamge, bg_rect)  #背景の貼り付け

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        key_list = pygame.key.get_pressed() #辞書
        if key_list[pygame.K_UP] == True:   #UPキーのとき
            tori_rect.centery -= 1
        if key_list[pygame.K_DOWN] == True: #DOWNキーのとき
            tori_rect.centery += 1
        if key_list[pygame.K_RIGHT] == True:#RIGHTキーのとき
            tori_rect.centerx += 1
        if key_list[pygame.K_LEFT] == True: #LEFTキーのとき
            tori_rect.centerx -= 1 
        screen.blit(tori_img, tori_rect)    #こうかとんの貼り付け

        ##爆弾の移動
        bomb_rect.move_ip(vx,vy)
        screen.blit(bomb_image, bomb_rect)  #爆弾の貼り付け
    
        pygame.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
    sys.exit()