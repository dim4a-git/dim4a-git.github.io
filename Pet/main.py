import animator
import brain
import trainer


def animate(
    ):
    while True:
        animator.animate_world()


def test(
    ):
    trainer.test(100)


def train(
    brain_file_name
    ):
    i = 0
    while True:
        print(i)
        trainer.train(100)
        if i % 10 == 9:
            brain.Brain().save(brain_file_name)
            print("brain saved")
        i += 1


def main():
    brain.Brain()
    file_name = "./brain.model"

    # brain.Brain().load(file_name)

    # animate()
    # test()
    train(file_name)

    print("End")

main()
