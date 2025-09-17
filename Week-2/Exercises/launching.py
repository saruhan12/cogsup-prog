# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Rectangles 200")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a 50px-radius blue Rectangle 
circle1 = stimuli.Rectangle(size=(50,50),colour=(0,255,0),position=(0,0))

circle2 = stimuli.Rectangle(size=(50,50),colour=(255,0,0),position=(-400,0))
# Start running the experiment
control.start(subject_id=1)

# Present the circle 
circle1.present(clear=True, update=False)

circle2.present(clear=False, update=True)
circle2.reposition(new_position=())
# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()
