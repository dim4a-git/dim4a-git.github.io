import animator
import brain
import trainer

def main():
    brain.Brain()
    file_name = "./brain.model"

    # brain.Brain().load(file_name)

    for i in range(100):
        # animator.animate_world()
        # print(i)
        trainer.train(100)

    brain.Brain().save(file_name)

    print("End")

main()
