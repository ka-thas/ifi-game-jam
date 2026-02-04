import pygame

from .options import *

class Boulder:
    def __init__(self):
        self.size = (50, 50)
        self.x = random.randint(self.size[0] // 2, WIDTH - self.size[0] // 2)
        self.y = 0
        self.color = RED
        self.speed = PLAYER_SPEED
        self.rect = pygame.Rect(self.x - self.size[0] // 2, self.y - self.size[1] // 2, self.size[0], self.size[1])
        

    def draw(self, screen):
        # circle
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.size[0] // 2)

    def get_rect(self):
        self.rect.topleft = (self.x - self.size[0] // 2, self.y - self.size[1] // 2)
        return self.rect
    