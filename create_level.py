# backend tool for creating level files

import json

from src.core.palette import Palette

# set to the level you're trying to edit
LEVEL = "01"

# set to True to edit the level instead of creating a new one
EDIT = False

"""
PARAMETERS:
"""

CANVAS_H_SIZE = 480
CANVAS_V_SIZE = 720

"""
END OF PARAMETERS
"""

level_data = []
powerups = ["grow", "shrink", "multi", "laser", "super", "catch", "1up", "next", "energy"]
level_data.append(powerups)

palette = Palette()
colours = palette.get_palette()


def draw_line(offset: int = 0):
    for x in range((CANVAS_H_SIZE - offset) // 32):
        brick_x = 32 * x + (16 + offset)
        brick_y = 16 * i + 16

        h_size = 32
        v_size = 16
        position = (brick_x, brick_y)

        # pycharm gives a warning here, but this works as-intended
        level_data.append({
            "h_size": h_size,
            "v_size": v_size,
            "position": position,
            "colour": colours[i]
        })


for i in range(len(colours)):
    if i % 2 == 0:
        draw_line(0)
    else:
        draw_line(16)

try:
    with open(f"./cfg/levels/{LEVEL}.json", "w") as f:
        json.dump(level_data, f)
    print("Done!")

except Exception as ex:
    print(ex)

