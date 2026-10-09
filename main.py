# Main.py

import pygame
import game_configs

# Game states:

MAIN_MENU = "main_menu"
PLAYING = "playing"
PAUSED = "paused"
SETTINGS = "settings"
GAME_OVER = "game_over"

# Initializing pygame
pygame.init()
screen = pygame.display.set_mode((game_configs.WIDTH, game_configs.HEIGHT))
clock = pygame.time.Clock()

# Starting game
state = MAIN_MENU
world = None # World is created when the match starts
running = True
dt = 0

# Game loop

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
