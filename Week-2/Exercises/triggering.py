# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Rectangles 200")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a 50px-radius blue Rectangle 
circle_green = stimuli.Rectangle(size=(50,50),colour=(0,255,0),position=(0,0))

circle_red = stimuli.Rectangle(size=(50,50),colour=(255,0,0),position=(-400,0))
# Start running the experiment
control.start(subject_id=1)

# Present the circle 
#put the rectangles on the board
circle_green.present(clear=True, update=False)

circle_red.present(clear=False, update=True)

#wait for a second 
exp.clock.wait(1000)
#start the run of the red rectangle
while circle_red.position[0] + 50 != circle_green.position[0]:
    #move the red 
    circle_red.move((2,0))
    #update the board
    circle_red.present(clear=True, update=False)
    circle_green.present(clear=False, update=True)

#start the run of the green rectangle
#3 times faster than the red rectangle
#which still feels causal
while circle_green.position[0] < 350:
    circle_green.move((6,0))
    circle_red.present(clear=True, update=False)
    circle_green.present(clear=False, update=True)

#wait for a second 
exp.clock.wait(1000)

# End the current session and quit expyriment
control.end()
