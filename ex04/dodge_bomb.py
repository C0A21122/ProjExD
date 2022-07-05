import pygame
import sys

def main():
    pygame.display.set_caption("逃げろ！こうかとん")    #ウィンドウの名前
    screen = pygame.display.set_mode((1600,900))       #ウィンドウサイズ
    screen_rect = screen.get_rect()
    bg_iamge = pygame.image.load("ex04/fig/pg_bg.jpg")  #背景
    bg_rect = bg_iamge.get_rect()
    screen.blit(bg_iamge, bg_rect)

    clock = pygame.time.Clock()
    clock.tick(0.5)

    while True:
        screen.blit(bg_iamge, bg_rect)
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