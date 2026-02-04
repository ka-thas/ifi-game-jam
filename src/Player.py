from .options import *
from .Projectile import Projectile

class Player:
    def __init__(self):
        self.x = 540
        self.y = 640
        self.size = (50, 50)
        self.color = BLUE
        self.speed = PLAYER_SPEED
        self.last_shot_time = 0

        self.lives = LIVES

    def shoot(self):
        projectile = Projectile(self.x + self.size[0] // 2, self.y)
        return projectile

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.size[0], self.size[1]))