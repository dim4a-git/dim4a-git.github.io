import numpy as np

from ..globals import project_types as GLOB
from ..universe import brain
from ..universe import pet
from ..universe import world


def get_map_reachability_quality(
    ):
    reach_map = get_squares_reachability()

    return 1.0 * reach_map.sum() / reach_map.size


def get_squares_reachability(
    ):
    brain.Brain().set_direction_choice_type(GLOB.DIRECTION_CHOICE_STRICT)
    width = GLOB.WORLD_WIDTH
    height = GLOB.WORLD_HEIGHT
    reach_map = np.zeros((height, width))
    (cx, cy) = (int(width / 2), int(height / 2))

    for y in range(height):
        for x in range(width):
            if x == cx and y == cy:
                reach_map[y][x] = 1
                continue
            w = world.World()
            w_map = w.get_map()
            w_map.set_map(np.zeros((height, width)))
            w_map.get_map().fill(GLOB.SQUARE_TYPE_EMPTY)
            w_map.set_square_value(x, y, GLOB.FOOD_SQUARE_PORTION)
            w_map.set_square_value(cx, cy, GLOB.SQUARE_TYPE_PET)
            w.set_pets([pet.Pet(cx, cy)])
            for _ in range(GLOB.PET_FOOD_RESERVE):
                w.step()
            if w_map.get_square_value(x, y) != GLOB.FOOD_SQUARE_PORTION:
                reach_map[y][x] = 1

    return reach_map
