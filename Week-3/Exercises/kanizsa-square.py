# Import the main modules of expyriment
from expyriment import design, control, stimuli, misc

grey = misc.constants.C_GREY
white = misc.constants.C_WHITE
black = misc.constants.C_BLACK
control.set_develop_mode()
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Week3-2", background_colour=grey)

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)
ww, wl = exp.screen.size
#single square line is %25 of window width
size_square = ww*0.25
#circle radius is %5 of window width
size_circle = ww*0.05
# Create a 50px-radius blue Rectangle 
square1 = stimuli.Rectangle(size=(size_square,size_square),
                            colour=grey,
                            position=(0,0))

def create_circs( length_square = size_square):
    pos = []
    for x in (length_square*0.5,-length_square*0.5):
        for y in (length_square*0.5,-length_square*0.5):
            pos.append((x,y))
    
    circs = []
    for k in pos:
        if k[1] > 0:#look at y position if abouve 0 then black else then white
            circle = stimuli.Circle(radius= ww*0.05,colour=black, position=k )
            circs.append(circle)
        else:
            circle = stimuli.Circle(radius= ww*0.05,colour=white, position =k)
            circs.append(circle)
    return circs


circles = create_circs()

# Start running the experiment
control.start(subject_id=1)
for i,k in enumerate(circles):
    if i == 0:
        k.present(clear=True,update=False)
    else:
        k.present(clear=False,update=False)
    

square1.present(clear=False, update=True)



exp.keyboard.wait()

control.end()