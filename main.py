# Main.py

import pygame
import game_configs
from UI import menus
from UI import renderer
from game import levels
from game.world import World


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
    command = None # What was clicked/pressed this frame

    # Events have to be read every frame or the window won't show/respond
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif state == PLAYING:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # Esc pauses the game
                command = "pause"
        else:
            clicked = menu.handle_event(event) # For buttons
            if clicked is not None:
                command = clicked

    # Change state depending on what was clicked/pressed:
    if command == "start":
        world = World(levels.LEVEL_1) # Builds the map
        state = PLAYING
    elif command == "pause":
        menu = menus.pause_menu(fonts)
        state = PAUSED
    elif command == "resume":
        state = PLAYING
    elif command == "main_menu":
        world = None
        menu = menus.main_menu(fonts)
        state = MAIN_MENU
    elif command == "quit":
        running = False

    # Update:
    if state == PLAYING:
        world.update(dt)

    # Draw:
    if world is not None:
        renderer.draw_world(screen, world)
    if state != PLAYING:
        menu.draw(screen) # Pause menu makes the map behind it darker

    pygame.display.flip()
    dt = clock.tick(game_configs.FPS) / 1000 # Seconds since last frame

pygame.quit()
