"""
Menus include: Main menu, settings, pause menu, and game over.
"""

import pygame
from game_configs import HEIGHT, WIDTH, BG_color, TITLE, BLACK, WHITE
from UI.buttons import Button

class Menu:
    def __init__(self, title, fonts):
        pass
        self.title = title
        self.fonts = fonts

BUTTON_SPACING = 75

class Menu:
    def __init__(self, title, fonts, overlay = False, title_y = HEIGHT // 4,
                 first_widget_y = HEIGHT // 2 - 60):
        self.title = title
        self.fonts = fonts
        self.overlay = overlay # Draw the menu over the game and make the game behind a bit darker
        self.title_y = title_y
        self.widgets = []
        self.next_y = first_widget_y
        self._shade = None

    def add_button(self, text, command):
        self.widgets.append(Button(text, (WIDTH // 2, self.next_y), command,
                                   self.fonts["button"]))
        self.next_y += BUTTON_SPACING

    def handle_event(self, event): # For button
        for widget in self.widgets:
            command = widget.handle_event(event)
            if command is not None:
                return command
        return None

    def draw(self, screen):
        if self.overlay:
            if self._shade is None:     # built once, then reused
                self._shade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                self._shade.fill((0, 0, 0, 170))
            screen.blit(self._shade, (0, 0))
        else:
            screen.fill(BLACK)

        title = self.fonts["title"].render(self.title, True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, self.title_y)))
        for widget in self.widgets:
            widget.draw(screen)


def main_menu(fonts):
    menu = Menu(TITLE, fonts)
    menu.add_button("Start game", "start")
    menu.add_button("Settings", "settings")
    menu.add_button("Exit game", "quit")
    return menu


def pause_menu(fonts):
    menu = Menu("Paused", fonts, overlay=True)
    menu.add_button("Resume", "resume")
    menu.add_button("Settings", "settings")
    menu.add_button("Exit to main menu", "main_menu")
    menu.add_button("Exit game", "quit")
    return menu




