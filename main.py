# main file
import pygame
import game_logic

# Pygame start
pygame.init()
WIDTH = 1512
HEIGHT = 861

# Background stuff
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

#Play logic
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('WHITE') # Background color

    pygame.draw.circle(screen, "black", player_pos, 15) # draw player as a circle over the background

    # Inpute handling & logic for player movement
    game_logic.player_move(player_pos, dt)

    running = game_logic.esc_quit(running)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
