SQUARE_TYPE_EMPTY = 100
SQUARE_TYPE_PET = 101

DIRECTION_CHOICE_STRICT = 1
DIRECTION_CHOICE_MULTINOMIAL = 2

WORLD_TYPE_SINGLE = 1
WORLD_TYPE_PAIR = 2
WORLD_TYPE_FULL = 3

WORLD_TYPE = WORLD_TYPE_SINGLE

if WORLD_TYPE == WORLD_TYPE_FULL:

    WORLD_WIDTH = 20
    WORLD_HEIGHT = 20

    PET_VIEW_RADIUS = 5
    PET_VIEW_DIAMETER = 2 * PET_VIEW_RADIUS + 1
    PET_FOOD_RESERVE = 10
    PETS_INITIONAL_NUMBER = 20

    FOOD_INITIONAL_SQUARES_NUMBER = 50
    FOOD_GROW_SPEED = 2
    FOOD_CONSUMPTION = 1
    FOOD_SQUARE_PORTION = 6

if WORLD_TYPE == WORLD_TYPE_SINGLE:

    WORLD_WIDTH = 11
    WORLD_HEIGHT = 11

    PET_VIEW_RADIUS = 5
    PET_VIEW_DIAMETER = 2 * PET_VIEW_RADIUS + 1
    PET_FOOD_RESERVE = 5
    PETS_INITIONAL_NUMBER = 1

    FOOD_INITIONAL_SQUARES_NUMBER = 1
    FOOD_GROW_SPEED = 0
    FOOD_CONSUMPTION = 1
    FOOD_SQUARE_PORTION = 2

if WORLD_TYPE == WORLD_TYPE_PAIR:

    WORLD_WIDTH = 11
    WORLD_HEIGHT = 11

    PET_VIEW_RADIUS = 5
    PET_VIEW_DIAMETER = 2 * PET_VIEW_RADIUS + 1
    PET_FOOD_RESERVE = 10
    PETS_INITIONAL_NUMBER = 2

    FOOD_INITIONAL_SQUARES_NUMBER = 10
    FOOD_GROW_SPEED = 1
    FOOD_CONSUMPTION = 1
    FOOD_SQUARE_PORTION = 2
