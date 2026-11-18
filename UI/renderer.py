# Drawing the game, only the map for now
import pygame
from game_configs import BG_color, WALL_color

def draw_world(screen, world): # Draw the map
    screen.fill(BG_color)
    for wall in world.walls:
        pygame.draw.rect(screen, WALL_color, wall.rect)
