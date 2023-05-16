import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):

    """Player Sizes:
    0: Small
    1: Normal
    2: Large
    3: Extra Large
    """
    size = 1
    
    h_size = 64
    v_size = 16

    def __init__(self, size, speed=5):
        super().__init__()
        self.speed = speed

        self.DISPLAY_H_SIZE = size[0]
        self.DISPLAY_V_SIZE = size[1]

        self.image = pygame.image.load("./img/player.png")
        self.image = pygame.transform.scale(self.image, (self.h_size, self.v_size))

        self.rect = self.image.get_rect()
        self.rect.center = (self.DISPLAY_H_SIZE / 2, self.DISPLAY_V_SIZE - 16)

    def move(self, direction: int):
        match direction:
            case 1:
                # up
                pass
            case 2:
                # right
                if self.rect.right <= self.DISPLAY_H_SIZE - 5:
                    self.rect.move_ip(self.speed, 0)
                else:
                    self.rect.move_ip(self.DISPLAY_H_SIZE - self.rect.right, 0)
            case 3:
                # down
                pass
            case 4:
                # left
                if self.rect.left >= 5:
                    self.rect.move_ip(-self.speed, 0)
                else:
                    self.rect.move_ip(-self.rect.left, 0)
            case _:
                raise Exception(f"Direction {direction} must be in range 1-4")

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def grow(self):
        if self.size >= 3:
            return
        self.size += 1
        self.h_size *= 1.5
        self.image = pygame.transform.scale(self.image, (self.h_size, self.v_size))

    def shrink(self):
        if self.size <= 0:
            return
        self.size -= 1
        self.h_size //= 1.5
        self.image = pygame.transform.scale(self.image, (self.h_size, self.v_size))

    def update(self):

        # get input for movement
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.move(1)
        if pressed_keys[K_RIGHT]:
            self.move(2)
        if pressed_keys[K_DOWN]:
            self.move(3)
        if pressed_keys[K_LEFT]:
            self.move(4)
