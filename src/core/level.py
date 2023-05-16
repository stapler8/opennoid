from src.objects.brick import Brick
from src.objects.player import Player

import json


class Level:
    bricks = []
    __raw_bricks = []

    def __init__(self, level: str):
        try:
            with open(f"./cfg/levels/{level}.json", "r") as f:
                self.__raw_bricks = json.load(f)

        except Exception as ex:
            print(ex)

        for brick in self.__raw_bricks:
            brk = Brick(
                h_size=brick['h_size'],
                v_size=brick['v_size'],
                position=brick['position'],
                colour=brick['colour']
            )

            self.bricks.append(brk)
