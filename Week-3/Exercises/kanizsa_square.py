# Import the main modules of expyriment
from expyriment import design, control, stimuli, misc

grey = misc.constants.C_GREY
white = misc.constants.C_WHITE
black = misc.constants.C_BLACK
control.set_develop_mode()
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Week3-1")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)
ww, wl = exp.screen.size
size_square = ww*0.25
size_circle = ww*0.05
# Create a 50px-radius blue Rectangle 
square1 = stimuli.Rectangle(size=(size_square,size_square),
                            colour=grey,
                            position=(0,0))

def create_circs(white=2, balck=2, size=size_circle, postion = size_square):
    pos = []
    for x in (size_square*0.5,-size_square*0.5):
        for y in (size_square*0.5,-size_square*0.5):
            pos.append((x,y))
    
    circs = []

# Start running the experiment
control.start(subject_id=1)


square1.present(clear=True, update=True)



exp.keyboard.wait()

control.end()