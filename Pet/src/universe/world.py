from . import map as world_map
from . import pet
from ..globals import project_types as GLOB



class World(object):


    def __init__(self
        ):
        self._alive_pets = []
        self._dead_pets = []
        self._map = world_map.Map()
        self._food_readiness = 0.1

        self._initialize()


    def epoch(self,
        steps_number
        ):
        self._initialize()
        for _ in range(steps_number):
            self.step()


    def get_map(self
        ):
        return self._map


    def get_pets(self
        ):
        return (self._alive_pets, self._dead_pets)


    def refresh(self
        ):
        self._initialize()


    def set_pets(self,
        alive_pets,
        dead_pets = None
        ):
        self._alive_pets = alive_pets
        self._dead_pets = [] if dead_pets is None else dead_pets


    def step(self
        ):
        new_coords = self._calculate_new_coordinates()
        self._feed_pets(new_coords)
        self._move_pets(new_coords)
        self._dec_food_reserve()
        self._generate_food()


    def _calculate_new_coordinates(self
        ):
        new_coords = []
        for pet in self._alive_pets:
            (x, y) = pet.get_coordinates()
            area = self._map.get_visible_area(x, y)
            (dx, dy) = pet.calculate_direction(area)
            x = self._map.move_x(x, dx)
            y = self._map.move_y(y, dy)
            new_coords.append((x, y))

        return new_coords


    def _dec_food_reserve(self
        ):
        i_pet = 0

        while i_pet < len(self._alive_pets):
            if not self._alive_pets[i_pet].sub_food(GLOB.FOOD_CONSUMPTION):
                self._dead_pets.append((self._alive_pets[i_pet]))
                del self._alive_pets[i_pet]
                (x, y) = self._dead_pets[-1].get_coordinates()
                self._map.set_square_value(x, y, GLOB.SQUARE_TYPE_EMPTY)
            else:
                i_pet += 1


    def _feed_pets(self,
        new_coords
        ):
        was_feeded = True

        while was_feeded:
            was_feeded = False
            for i in range(len(new_coords)):
                (x, y) = new_coords[i]
                value = self._map.get_square_value(x, y)
                if 0 < value and value < GLOB.SQUARE_TYPE_EMPTY:
                    self._alive_pets[i].add_food(1)
                    self._map.set_square_value(x, y, value - 1)
                    if value == 1:
                        self._map.set_square_value(x, y, GLOB.SQUARE_TYPE_EMPTY)
                    else:
                        was_feeded = True


    def _generate_food(self
        ):
        self._food_readiness += GLOB.FOOD_GROW_SPEED
        while self._food_readiness > 1:
            self._map.set_random_square_value(GLOB.FOOD_SQUARE_PORTION)
            self._food_readiness -= 1


    def _initialize(self
        ):
        self._alive_pets = []
        self._dead_pets = []
        self._map = world_map.Map()

        for _ in range(GLOB.PETS_INITIONAL_NUMBER):
            self._alive_pets.append(pet.Pet())
            (x, y) = self._map.set_random_square_value(GLOB.SQUARE_TYPE_PET)
            self._alive_pets[-1].set_coordinates(x, y)

        for _ in range(GLOB.FOOD_INITIONAL_SQUARES_NUMBER):
            self._map.set_random_square_value(GLOB.FOOD_SQUARE_PORTION)


    def _move_pets(self,
        new_coords
        ):
        for i in range(len(new_coords)):
            (x, y) = self._alive_pets[i].get_coordinates()
            self._map.set_square_value(x, y, GLOB.SQUARE_TYPE_EMPTY)
            (x, y) = new_coords[i]
            self._alive_pets[i].set_coordinates(x, y)

        for coord in new_coords:
            self._map.set_square_value(coord[0], coord[1], GLOB.SQUARE_TYPE_PET)