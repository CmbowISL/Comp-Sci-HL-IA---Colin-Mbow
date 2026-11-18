# The player, WASD to move
import pygame
from game_configs import CH_color
from player_configs import PLAYER_SPEED
from game.character import Character

class Player(Character):
    color = CH_color

    def __init__(self, pos):
        super().__init__(pos, PLAYER_SPEED)

    def update(self, dt, world):
        keys = pygame.key.get_pressed() # Keys being held down
        direction = pygame.Vector2(keys[pygame.K_d] - keys[pygame.K_a], # 1 = right, -1 = left, 0 = neither or both
                                   keys[pygame.K_s] - keys[pygame.K_w]) # 1 = down, -1 = up
        self.move(direction, dt, world.walls)
