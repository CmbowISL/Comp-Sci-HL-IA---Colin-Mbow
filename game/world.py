from game_configs import WIDTH, HEIGHT
from game.wall import Wall

class World:
    def __init__(self, level):
        self.walls = []
        for x, y, width, height in level["walls"]: # Turning the fractions into pixels for this window size
            self.walls.append(Wall(x * WIDTH, y * HEIGHT, width * WIDTH, height * HEIGHT))

    def update(self, dt): # Nothing moves yet
        pass
