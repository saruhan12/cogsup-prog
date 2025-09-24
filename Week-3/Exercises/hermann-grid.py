# Import the main modules of expyriment
from expyriment import design, control, stimuli, misc

grey = misc.constants.C_GREY
white = misc.constants.C_WHITE
black = misc.constants.C_BLACK
control.set_develop_mode()
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
#exp = design.Experiment(name = "Week3-4", background_colour=grey)

# Initialize the experiment: Must be done before presenting any stimulus
#control.initialize(exp)

#control.start(subject_id=1)

def hermann_grid(size = 50, color=black, space = 10, rows = 5, cols=5, back_color=white):
    exp = design.Experiment(name = "Week3-4", background_colour=back_color)
    control.initialize(exp)

    # Initialize the experiment: Must be done before presenting any stimulus
    starting_col =   ((size+space)*cols-space)*0.5 - size*0.5
    starting_line =  ((size+space)*rows-space)*0.5 - size*0.5
    squares = []
    for r in range(rows):
        for c in range(cols):
            square = stimuli.Rectangle(size=(size,size),
                                        colour=color,
                                        position=(-starting_col+c*(space + size), starting_line-r*(space+size)))
            squares.append(square)
    control.start(subject_id=1)
    for i, sq in enumerate(squares):
        if i == 0:
            sq.present(clear=True,update=False)
        elif i == len(squares)-1:
            sq.present(clear=False,update=True)
        else:
            sq.present(clear=False, update=False)


    exp.keyboard.wait()

    control.end()

        


hermann_grid()