"""
classes for buttons
"""
import pygame
from game_configs import WHITE, BLACK, GREY, DARK_GREY

class Button:
    def __init__(self, text, center, command, font, size=(300, 56)):
        self.text = text
        self.command = command
        self.font = font
        width = max(size[0], font.size(text)[0] + 40) # Resizing automatically to the screen size
        self.rect = pygame.Rect(0, 0, width, size[1])
        self.rect.center = center

    def handle_event(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 # If the button is clicked do what the button is meant to do
                and self.rect.collidepoint(event.pos)):
            return self.command
        return None

    def draw(self, screen): # Draw it
        hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, GREY if hovered else WHITE, self.rect, border_radius=8)
        pygame.draw.rect(screen, DARK_GREY, self.rect, width=2, border_radius=8)
        label = self.font.render(self.text, True, BLACK)
        screen.blit(label, label.get_rect(center=self.rect.center))