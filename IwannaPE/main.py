import pygame, asyncio, sys, numpy #Open Packages
from pygame.locals import *

class Client:
    def __init__(self, title='I wanna be the Python Engine!', size=(640, 480), background_color=(100, 100, 100)):
        pygame.init()
        self.SURFACE = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        clock = pygame.time.Clock()
        
        font = pygame.font.SysFont(None, 50)
        self.Title = font.render(str(title), True, (0, 0, 0))
        TitleWidth = self.Title.get_rect().width
        TitleX = (size[0] - TitleWidth) / 2

        self.Start = font.render("game start", True, (0, 0, 0))
        
        self.GameLoopType = 'IwannaPE_menu'

        self.GameLoop = True

        while self.GameLoop:
            #画面の初期化
            self.SURFACE.fill(background_color)
            
            #特殊キーの入力判定
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.SURFACE.blit(self.Title, (TitleX, 100))
            self.SURFACE.blit(self.Start, (TitleX, 200))
            
            pygame.display.update()
            clock.tick(60)
