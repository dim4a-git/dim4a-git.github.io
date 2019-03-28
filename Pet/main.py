import brain
import world

def main():
    brain.Brain()
    w = world.World()
    batch_min = 0
    batch_aver = 0
    batch_max = 0
    batch_size = 20

    for i in range(1000):
        w.epoch(100)
        (a, d) = w.get_pets()
        history = []
        for p in d:
            (areas, directions) = p.get_history()
            history.append({"areas": areas, "directions": directions})
        lifes_lengths = brain.Brain().train(history)

        batch_min += lifes_lengths["min_length"]
        batch_max += lifes_lengths["max_length"]
        batch_aver += lifes_lengths["average_length"]

        if i % batch_size == batch_size - 1:
            print(int(i / batch_size + 1),
                  int(batch_min / batch_size),
                  int(batch_aver / batch_size),
                  int(batch_max / batch_size))
            batch_max = batch_aver = batch_min = 0

    print("End")

main()
