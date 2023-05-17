import pygame


class Ball(pygame.sprite.Sprite):

    __EFFECTS = ("multi", "catch")
    H_SIZE = V_SIZE = 8
    v_momentum = 2.5
    h_momentum = -0.5

    def __init__(self, size: tuple):
        super().__init__()

        self.powerup = None

        self.DISPLAY_H_SIZE = size[0]
        self.DISPLAY_V_SIZE = size[1]
        
        self.pos_float = (float(self.DISPLAY_H_SIZE / 2), float(self.DISPLAY_V_SIZE / 3))

        self.image = pygame.image.load("./img/ball.png")
        self.image = pygame.transform.scale(self.image, (self.H_SIZE, self.V_SIZE))

        self.rect = self.image.get_rect()
        self.rect.center = (self.DISPLAY_H_SIZE / 2, self.DISPLAY_V_SIZE / 3)
        print(self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.move()
        print(self.pos_float)

    def move(self):
        self.pos_float = (self.pos_float[0] + self.h_momentum, self.pos_float[1] + self.v_momentum)

        self.rect.center = (int(self.pos_float[0]), int(self.pos_float[1]))

        self.check_walls()

    def check_walls(self):
        if self.rect.top > self.DISPLAY_V_SIZE:
            self.kill()

        if self.rect.right == self.DISPLAY_H_SIZE or self.rect.left == 0:
            self.h_momentum *= -1

    def bounce_h(self):
        self.h_momentum *= -1.05
        self.v_momentum *= 1.05

    def bounce_v(self):
        self.v_momentum *= -1.05
        self.h_momentum *= 1.05

    def kill(self):
        super().kill()
