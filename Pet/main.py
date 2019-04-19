import os

import src.globals.project_types as GLOB
import src.tasks as tasks
import src.universe.brain as brain


def main(
    ):
    _initialize()
    file_name = GLOB.DATA_DIR_NAME + "brain.model"

    brain.Brain().load(file_name)

    # tasks.animate()
    tasks.build_reach()
    # tasks.research()
    # tasks.test()
    # tasks.train(file_name)

    print("End")


def _initialize(
    ):
    brain.Brain()
    GLOB.DATA_DIR_NAME = os.path.dirname(os.path.realpath(__file__)) + "/data/"

main()
