# Import the main modules of expyriment
from expyriment import design, control, stimuli

#control.set_develop_mode()
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Week3-1")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)
ww, wl = exp.screen.size
size = ww*0.05
# Create a 50px-radius blue Rectangle 
square1 = stimuli.Rectangle(size=(size,size),
                            colour=(255,0,0),
                            line_width=1,
                            position=(ww/2-size/2,wl/2-size/2))


square2 = square1.copy()
square2.reposition(new_position=(-ww/2+size/2,wl/2-size/2))
square3 = square1.copy()
square3.reposition(new_position=(ww/2-size/2,-wl/2+size/2))
square4 = square1.copy()
square4.reposition(new_position=(-ww/2+size/2,-wl/2+size/2))
# Start running the experiment
control.start(subject_id=1)

square1.present(clear=True, update=False)
square2.present(clear=False, update=False)
square3.present(clear=False, update=False)
square4.present(clear=False, update=True)



exp.keyboard.wait()
control.end()