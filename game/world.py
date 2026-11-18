from game_configs import WIDTH, HEIGHT
from game.wall import Wall
from game.player import Player

class World:
    def __init__(self, level):
        self.walls = []
        for x, y, width, height in level["walls"]: # Turning the fractions into pixels for this window size
            self.walls.append(Wall(x * WIDTH, y * HEIGHT, width * WIDTH, height * HEIGHT))

        x, y = level["player_spawn"]
        self.player = Player((x * WIDTH, y * HEIGHT)) # Spawn point turned into pixels too

    def update(self, dt):
        self.player.update(dt, self)
