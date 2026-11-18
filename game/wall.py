# Class for walls
import pygame

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height) # Blocks movement, bullets and what can be seen
