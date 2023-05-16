import pygame

from random import choice


class Powerup(pygame.sprite.Sprite):

    __effects = ("grow", "shrink", "multi", "laser", "super", "catch", "1up", "next", "energy")

    H_SIZE = 24
    V_SIZE = 16
    SPEED = 3

    def __init__(self, effect: str = None, effects: list = None, position: tuple = (-100, -100)):
        super().__init__()

        if effect is None:
            if not effects:
                effect = choice(self.__effects)
            else:
                effect = choice(effects)
        self.effect = effect

        self.image = pygame.image.load(f"./img/powerup_{self.effect}.png")
        self.image = pygame.transform.scale(self.image, (self.H_SIZE, self.V_SIZE))

        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        # when the powerup is first displayed, it moves downwards from creation until
        self.move()

    def move(self):
        self.rect.move_ip(0, self.SPEED)
