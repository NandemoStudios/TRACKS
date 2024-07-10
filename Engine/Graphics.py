import pygame


class Graphics:

    def __init__(self, screen):
        self.screen = screen

    def draw_circle(self, x, y, radius, **kwargs):
        center = pygame.Vector2(x, y)
        if 'color' in kwargs:
            color = kwargs.get('color')
        else:
            color = 'black'
        pygame.draw.circle(self.screen, color, center, radius)