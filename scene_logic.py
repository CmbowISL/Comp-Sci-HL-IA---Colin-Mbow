import pygame
import game_logic

def main_menu(screen):
    screen.fill("Black")

def main(screen, player_pos, dt):
    screen.fill('WHITE') # Background color

    pygame.draw.circle(screen, "black", player_pos, 15) # draw player as a circle over the background

    # Inpute handling & logic for player movement
    game_logic.player_move(player_pos, dt)