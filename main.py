# Main.py

import pygame
import game_configs
from UI import menus


# Initial stuff:
pygame.init()

fonts = {
    "title": pygame.font.Font(None, 90),
    "button": pygame.font.Font(None, 36),
    "normal": pygame.font.Font(None, 30),
    "small": pygame.font.Font(None, 22),
}

MAIN_MENU = "main_menu"
PLAYING = "playing"
PAUSED = "paused"
SETTINGS = "settings"
GAME_OVER = "game_over"
menu = menus.main_menu(fonts)


screen = pygame.display.set_mode((game_configs.WIDTH, game_configs.HEIGHT))
pygame.display.set_caption(game_configs.TITLE)
clock = pygame.time.Clock()

# Starting game
state = MAIN_MENU
world = None # World is created when the match starts
running = True
dt = 0

# Game loop
while running:
    # Events have to be read every frame or the window won't show/respond
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        command = menu.handle_event(event)
        if command == "quit":
            running = False

    menu.draw(screen)

    pygame.display.flip()
    dt = clock.tick(game_configs.FPS) / 1000 # Seconds since last frame

pygame.quit()
