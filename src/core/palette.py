import pygame

import json


class Palette:

    def __init__(self):
        self._palette = Palette.__load_palette()
        self.get_colour("red")

    def get_colour(self, query):
        if query.lower() not in self._palette.keys():
            return

        # get our RGB values from the colour value
        rgb = tuple(int(i) for i in self._palette[query].split(' '))
        colour = pygame.Color(rgb[0], rgb[1], rgb[2])
        return colour

    def get_palette(self):
        palette = [colour for colour in self._palette.keys()]
        return palette


    @staticmethod
    def __load_palette():
        with open("./cfg/colours.json", "r") as f:
            return json.load(f)
