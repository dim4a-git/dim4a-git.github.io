import numpy as np
import random

import project_types as GLOB



class Map(object):


    def __init__(self
        ):
        self._map = np.zeros((GLOB.WORLD_HEIGHT, GLOB.WORLD_WIDTH))
        self._map.fill(GLOB.SQUARE_TYPE_EMPTY)


    def get_square_value(self,
        x,
        y
        ):
        return self._map[y, x]


    def get_visible_area(self,
        centre_x,
        centre_y
        ):
        size = 2 * GLOB.PET_VIEW_RADIUS + 1
        area = np.zeros((size, size))
        for y in range(size):
            for x in range(size):
                cy = (centre_y + GLOB.WORLD_HEIGHT - GLOB.PET_VIEW_RADIUS + y) % GLOB.WORLD_HEIGHT
                cx = (centre_x + GLOB.WORLD_WIDTH - GLOB.PET_VIEW_RADIUS + x) % GLOB.WORLD_WIDTH
                area[y, x] = self._map[cy, cx]

        return area


    def height(self
        ):
        return GLOB.WORLD_HEIGHT


    def move_x(self,
        x,
        dx
        ):
        return (x + GLOB.WORLD_WIDTH + dx) % GLOB.WORLD_WIDTH


    def move_y(self,
        y,
        dy
        ):
        return (y + GLOB.WORLD_HEIGHT + dy) % GLOB.WORLD_HEIGHT


    def set_random_square_value(self,
        value
        ):
        x = random.randint(0, GLOB.WORLD_WIDTH - 1)
        y = random.randint(0, GLOB.WORLD_HEIGHT - 1)

        while self._map[y, x] != GLOB.SQUARE_TYPE_EMPTY:
            x = random.randint(0, GLOB.WORLD_WIDTH - 1)
            y = random.randint(0, GLOB.WORLD_HEIGHT - 1)

        self._map[y, x] = value

        return (x, y)


    def set_square_value(self,
        x,
        y,
        value
        ):
        self._map[y, x] = value


    def width(self
        ):
        return GLOB.WORLD_WIDTH
