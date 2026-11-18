# Things the player and the NPC both have, so it only has to be written once
import pygame
from game_configs import WIDTH, HEIGHT, BLACK
from player_configs import CHARACTER_RADIUS

class Character:
    color = BLACK

    def __init__(self, pos, speed):
        self.pos = pygame.Vector2(pos)
        self.radius = CHARACTER_RADIUS * WIDTH # Fractions turned into pixels for this window size
        self.speed = speed * WIDTH

    def move(self, direction, dt, walls): # Move in a direction and slide along walls
        if direction.length_squared() == 0: # Not moving
            return
        velocity = direction.normalize() * self.speed * dt # normalize() so going diagonally isn't faster

        # Moving one axis at a time is what lets it slide along a wall instead of getting stuck on it
        self.pos.x += velocity.x
        self.wall_collisions(walls, velocity.x, 0)
        self.pos.y += velocity.y
        self.wall_collisions(walls, 0, velocity.y)

        # Staying inside the window
        self.pos.x = max(self.radius, min(WIDTH - self.radius, self.pos.x))
        self.pos.y = max(self.radius, min(HEIGHT - self.radius, self.pos.y))

    def wall_collisions(self, walls, dx, dy): # Push it back out of any wall it walked into
        r = self.radius
        for wall in walls:
            rect = wall.rect
            # Collides as a square even though it's drawn as a circle, simpler maths and feels the same
            touching = (self.pos.x + r > rect.left and self.pos.x - r < rect.right
                        and self.pos.y + r > rect.top and self.pos.y - r < rect.bottom)
            if not touching:
                continue
            if dx > 0: # Was moving right, so put it back on the left side of the wall
                self.pos.x = rect.left - r
            elif dx < 0:
                self.pos.x = rect.right + r
            if dy > 0: # Was moving down, so put it back on the top side of the wall
                self.pos.y = rect.top - r
            elif dy < 0:
                self.pos.y = rect.bottom + r
