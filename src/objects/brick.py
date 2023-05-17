import pygame

from src.core.palette import Palette
from src.objects.powerup import Powerup

import random


class Brick(pygame.sprite.Sprite):

    palette = Palette()

    def __init__(self,
                 h_size: int = 32,
                 v_size: int = 16,
                 powerup: Powerup = Powerup(),
                 position: tuple = (32, 16),
                 colour: str = ""
                 ):
        super().__init__()

        self.H_SIZE = h_size
        self.V_SIZE = v_size

        self._powerup = powerup

        if not colour:
            colour = random.choice(self.palette.get_palette())

        self.image = pygame.image.load(f"./img/brick_{colour}.png")
        self.image = pygame.transform.scale(self.image, (self.H_SIZE, self.V_SIZE))

        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def destroy(self):
        self.kill()
        return self._powerup, self.rect.center
