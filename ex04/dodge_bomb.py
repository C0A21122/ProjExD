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

    while True:
        screen.blit(bg_iamge, bg_rect)  #背景の貼り付け
        screen.blit(tori_img, tori_rect)#こうかとんの貼り付け

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.update()
        clock.tick(1000)




if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
    sys.exit()