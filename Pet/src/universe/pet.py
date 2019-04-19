from . import brain
from ..globals import project_types as GLOB



class Pet(object):


    def __init__(self,
        x = -1,
        y = -1
        ):
        self._food_reserve = GLOB.PET_FOOD_RESERVE
        self._x = x
        self._y = y
        self._areas = []
        self._brain_directions = []


    def add_food(self,
        food_count
        ):
        # self._food_reserve = min(self._food_reserve + food_count, GLOB.PET_FOOD_RESERVE)
        self._food_reserve += food_count


    def calculate_direction(self,
        visible_area
        ):
        for y in range(GLOB.PET_VIEW_DIAMETER):
            for x in range(GLOB.PET_VIEW_DIAMETER):
                if visible_area[y, x] < GLOB.SQUARE_TYPE_EMPTY:
                    visible_area[y, x] = 2
                else:
                    visible_area[y, x] -= GLOB.SQUARE_TYPE_EMPTY
                # visible_area[y, x] /= 2

        brain_direction = brain.Brain().calculate_direction(visible_area)
        self._areas.append(visible_area)
        self._brain_directions.append(brain_direction)

        return self._build_direction(brain_direction)


    def get_coordinates(self
        ):
        return (self._x, self._y)


    def get_history(self
        ):
        return (self._areas, self._brain_directions)


    def set_coordinates(self,
        x,
        y
        ):
        self._x = x
        self._y = y


    def sub_food(self,
        food_count
        ):
        self._food_reserve -= min(self._food_reserve, food_count)

        return self._food_reserve > 0


    def _build_direction(self,
        brain_direction
        ):
        corr_dir = brain_direction
        dx = int(corr_dir) % 3 - 1
        dy = int(corr_dir / 3) - 1

        return (dx, dy)
