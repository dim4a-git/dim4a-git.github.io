import numpy as np

from .research import tester
from .research import trainer
from .universe import brain
from .utils import animator
from .utils import reachability_map


def animate(
    ):
    while True:
        animator.animate_world()


def build_reach(
    ):
    reachability_map.draw_reach_map()


def research(
    ):
    def gen_log_entry(
        explorer_rate,
        steps_number,
        sample_index,
        aver_life_length
        ):
        return "rate={:.2f} steps={} sample={} aver={:.2f}".format(
            explorer_rate, steps_number, sample_index, aver_life_length
        )

    log_file_name = "test_log.txt"

    explorer_rates = np.arange(0.1, 1.01, 0.1)
    steps_number = 2000
    samples_number = 10
    control_length = 20

    aver = 0

    for i_sample in range(samples_number):
        for rate in explorer_rates:
            brain.Brain().refresh()
            brain.Brain().set_explorer_rate(rate)

            for i_step in range(steps_number):
                trainer.train(100)
                if i_step % control_length == control_length - 1:
                    print(i_step + 1)
                    aver = tester.get_map_reachability_quality()
                    log_entry = gen_log_entry(rate, i_step + 1, i_sample, aver)
                    with open(log_file_name, "a") as f:
                        f.write(log_entry + "\n")

            log_entry = gen_log_entry(rate, steps_number, i_sample, aver)
            brain.Brain().save("Brains/brain" + log_entry + ".model")
            with open(log_file_name, "a") as f:
                f.write("\n")


def test(
    ):
    quality = tester.get_map_reachability_quality()
    print(quality)


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
