import numpy as np

import animator
import brain
import reachability_map
import trainer


def animate(
    ):
    while True:
        animator.animate_world()


def build_reach(
    ):
    reachability_map.draw_reach_map()


def research(
    ):
    def gen_file_name(
        explorer_rate,
        steps_number,
        sample_index,
        aver_life_length
        ):
        return "brain rate={:.2f} steps={} sample={} aver={:.2f}.model".format(
            explorer_rate, steps_number, sample_index, aver_life_length
        )

    explorer_rates = np.arange(0.1, 1, 0.1)
    steps_number = 2000
    samples_number = 100
    control_length = 20

    for i_sample in range(samples_number):
        for rate in explorer_rates:
            brain.Brain().refresh()
            brain.Brain().set_explorer_rate(rate)
            for i_step in range(steps_number):
                trainer.train(100)
                if i_step % control_length == control_length - 1:
                    aver = trainer.test(100)["average_length"]
                    file_name = gen_file_name(rate, i_step + 1, i_sample, aver)
                    brain.Brain().save(file_name)


def test(
    ):
    trainer.test(100)


def train(
    brain_file_name,
    steps_number = 0
    ):
    i = 0
    while True:
        print(i)
        trainer.train(100)
        if i % 10 == 9:
            brain.Brain().save(brain_file_name)
            print("brain saved")
        i += 1
        if i == steps_number:
            break


def main():
    brain.Brain()
    file_name = "./brain.model"

    # brain.Brain().load(file_name)

    # animate()
    # build_reach()
    research()
    # test()
    # train(file_name)

    print("End")

main()
