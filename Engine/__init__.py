import pygame
from pygame import *
import Engine.Graphics as Graphics

class StartEngine:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.Graphics = Graphics.Graphics(self.screen)
        self.running = True

    def ClearScreen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.screen.fill("White")

    def Tick(self):
        pygame.display.flip()
        self.clock.tick(60)