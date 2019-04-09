import brain
import project_types as GLOB
import world


def test(
    epochs_number
    ):
    brain.Brain().set_direction_choice_type(GLOB.DIRECTION_CHOICE_STRICT)
    w = world.World()
    history = []

    for i in range(epochs_number):
        w.epoch(100)
        (a, d) = w.get_pets()
        for p in d:
            (areas, directions) = p.get_history()
            history.append({"areas": areas, "directions": directions})

    lifes_lengths = brain.Brain().train(history)
    print("{0} {1:.2f} {2}".format(
        int(lifes_lengths["min_length"]),
        lifes_lengths["average_length"],
        int(lifes_lengths["max_length"]))
        )


def train(
    epochs_number,
    batch_size = 0
    ):
    brain.Brain().set_direction_choice_type(GLOB.DIRECTION_CHOICE_MULTINOMIAL)
    w = world.World()
    history = []

    for i in range(epochs_number):
        w.epoch(100)
        (a, d) = w.get_pets()
        for p in d:
            (areas, directions) = p.get_history()
            history.append({"areas": areas, "directions": directions})

        if batch_size != 0 and i % batch_size == batch_size - 1:
            lifes_lengths = brain.Brain().train(history)
            history = []
            print(int(i / batch_size + 1),
                  int(lifes_lengths["min_length"]),
                  int(lifes_lengths["average_length"]),
                  int(lifes_lengths["max_length"]))

    if history != []:
        lifes_lengths = brain.Brain().train(history)
        print("{0} {1:.2f} {2}".format(
            int(lifes_lengths["min_length"]),
            lifes_lengths["average_length"],
            int(lifes_lengths["max_length"]))
            )
