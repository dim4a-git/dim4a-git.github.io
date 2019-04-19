import numpy as np
import tkinter

from ..globals import project_types as GLOB
from ..universe import brain
from ..universe import world


pix_per_square = 20
offset_length = 10


def draw_reach_map(
    ):
    brain.Brain().set_direction_choice_type(GLOB.DIRECTION_CHOICE_STRICT)
    width = GLOB.WORLD_WIDTH
    height = GLOB.WORLD_HEIGHT
    epoch_length = GLOB.PET_FOOD_RESERVE + GLOB.FOOD_SQUARE_PORTION
    reach_map = np.zeros((height, width))
    (cx, cy) = (int(width / 2), int(height / 2))

    for y in range(height):
        for x in range(width):
            if x == cx and y == cy:
                reach_map[y][x] = 1
            w = world.World()
            w_map = w.get_map()
            w_map.set_map(np.zeros((height, width)))
            w_map.get_map().fill(GLOB.SQUARE_TYPE_EMPTY)
            w_map.set_square_value(cx, cy, GLOB.SQUARE_TYPE_PET)
            w._alive_pets[0].set_coordinates(cx, cy)
            w_map.set_square_value(x, y, GLOB.FOOD_SQUARE_PORTION)
            for _ in range(epoch_length):
                w.step()
            if w_map.get_square_value(x, y) != GLOB.FOOD_SQUARE_PORTION:
                reach_map[y][x] = 1

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, {"width": width * pix_per_square + 2 * offset_length,
                                   "height": height * pix_per_square + 2 * offset_length,
                                   "bg": "white"})
    canvas.pack()
    _draw_map(canvas, reach_map)
    root.mainloop()


def _draw_map(
    canvas,
    ratio_map
    ):
    (height, width) = ratio_map.shape

    for i in range(height + 1):
        canvas.create_line(
            offset_length, i * pix_per_square + offset_length,
            width * pix_per_square + offset_length, i * pix_per_square + offset_length)
    for i in range(width + 1):
        canvas.create_line(
            i * pix_per_square + offset_length, offset_length,
            i * pix_per_square + offset_length, height * pix_per_square + offset_length)

    for y in range(height):
        for x in range(width):
            red = int(255 * ratio_map[y][x])
            blue = 255 - red
            canvas.create_rectangle(
                x * pix_per_square + offset_length + 1,
                y * pix_per_square + offset_length + 1,
                (x + 1) * pix_per_square + offset_length - 1,
                (y + 1) * pix_per_square + offset_length - 1,
                outline="#{0:02x}00{1:02x}".format(red, blue),
                fill="#{0:02x}00{1:02x}".format(red, blue)
            )
