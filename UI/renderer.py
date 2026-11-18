# Drawing the game, the map and the player for now
import pygame
from game_configs import BG_color, WALL_color

def draw_world(screen, world): # Draw everything in the match
    screen.fill(BG_color)
    for wall in world.walls:
        pygame.draw.rect(screen, WALL_color, wall.rect)

    player = world.player
    pygame.draw.circle(screen, player.color, player.pos, player.radius) # Draw the player
