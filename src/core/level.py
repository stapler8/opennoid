from src.objects.brick import Brick
from src.objects.player import Player

import json

"""
First index of a level .json is ALWAYS the powerup types
"""

class Level:
    bricks = []
    __raw_objects = []
    powerups = []

    def __init__(self, level: str):
        try:
            with open(f"./cfg/levels/{level}.json", "r") as f:
                self.__raw_objects = json.load(f)

        except Exception as ex:
            print(ex)

        self.powerups = self.__raw_objects[0]
        
        for brick in self.__raw_objects[1:]:
            brk = Brick(
                h_size=brick['h_size'],
                v_size=brick['v_size'],
                position=brick['position'],
                colour=brick['colour']
            )

            self.bricks.append(brk)
