import pygame, asyncio, sys #Open Packages
from pygame.locals import *

class Client:
    def __init__(self, title='I wanna be the Python Engine!', size=(640, 480), background_color=(100, 100, 100)):
        pygame.init()
        self.SURFACE = pygame.display.set_mode(size)
        pygame.display.set_caption(title)

        self.GameLoop = True

        while self.GameLoop:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
