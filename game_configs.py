"""
All variables that have a number assigned to them for a specific reason, e.g. WIDTH and HEIGHT
of the window, is stored here. This is only specific to core functionality of the game,
things for specific player and NPC settings will be stored in play_configs.py
"""

import pygame
pygame.display.init()

# Window
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
FPS = 60
title = "Smart NPC CS27"

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

BG_color = WHITE
CH_color = BLACK
