import sys

import pygame
from pygame.locals import *

import json
from src.core.palette import Palette
from src.objects.player import Player

settings = {}


palette = Palette()


def import_settings():
    global settings

    with open("cfg/cfg.json", "r") as f:
        settings = json.load(f)


class Noid:
    __objects = {}

    def __init__(self):

        import_settings()

        self._running = True
        self._display_surf = None
        self._size = self.width, self.height = settings["HSize"], settings["VSize"]

        self.FPS = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            Noid.on_cleanup()

    def on_loop(self):

        # update events and objects
        for event in pygame.event.get():
            self.on_event(event)
        for obj in self.__objects.values():
            try:
                obj.update()
            except Exception as ex:
                print(ex)

        self.__objects["player"].draw(self._display_surf)

    def on_render(self):
        pass

    @staticmethod
    def on_cleanup():
        pygame.quit()
        sys.exit(0)

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        player = Player(self._size)
        self.__objects["player"] = player

        while self._running:
            self._display_surf.fill(palette.get_colour("white"))
            self.on_loop()

            pygame.display.update()
            self.FPS.tick(settings["FPS"])


if __name__ == "__main__":
    app = Noid()
    app.on_execute()
