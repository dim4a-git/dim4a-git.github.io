import tkinter

import brain
import project_types as GLOB
import world


pix_per_square = 20
offset_length = 10


def animate_world(
    ):
    brain.Brain().set_direction_choice_type(GLOB.DIRECTION_CHOICE_STRICT)
    w = world.World()
    width = w.get_map().width()
    height = w.get_map().height()

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, {"width": width * pix_per_square + 2 * offset_length,
                                   "height": height * pix_per_square + 2 * offset_length,
                                   "bg": "white"})
    canvas.pack()

    for i in range(height + 1):
        canvas.create_line(offset_length, i * pix_per_square + offset_length,
                           width * pix_per_square + offset_length, i * pix_per_square + offset_length)
    for i in range(width + 1):
        canvas.create_line(i * pix_per_square + offset_length, offset_length,
                           i * pix_per_square + offset_length, height * pix_per_square + offset_length)

    def _animate():
        if not _draw_map(canvas, w.get_map()):
            root.destroy()
            return
        root.after(1000, _animate)
        w.step()

    _animate()

    root.mainloop()



def _draw_map(
    canvas,
    world_map
    ):
    is_pet_alive = False

    for y in range(world_map.height()):
        for x in range(world_map.width()):
            value = world_map.get_square_value(y, x)
            canvas.create_rectangle(
                x * pix_per_square + offset_length + 1,
                y * pix_per_square + offset_length + 1,
                (x + 1) * pix_per_square + offset_length - 1,
                (y + 1) * pix_per_square + offset_length - 1,
                outline="white",
                fill="white"
                )
            if value == GLOB.SQUARE_TYPE_PET:
                is_pet_alive = True
                canvas.create_oval(
                    x * pix_per_square + offset_length + 2,
                    y * pix_per_square + offset_length + 2,
                    (x + 1) * pix_per_square + offset_length - 2,
                    (y + 1) * pix_per_square + offset_length - 2,
                    outline="blue",
                    fill="blue"
                    )
            if value < GLOB.SQUARE_TYPE_EMPTY:
                canvas.create_oval(
                    x * pix_per_square + offset_length + 3,
                    y * pix_per_square + offset_length + 3,
                    (x + 1) * pix_per_square + offset_length - 3,
                    (y + 1) * pix_per_square + offset_length - 3,
                    outline="green",
                    fill="green"
                    )


    return is_pet_alive
