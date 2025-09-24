# Import the main modules of expyriment
from expyriment import design, control, stimuli, misc

grey = misc.constants.C_GREY
white = misc.constants.C_WHITE
black = misc.constants.C_BLACK
control.set_develop_mode()
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Week3-3", background_colour=grey)

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

control.start(subject_id=1)
def kanizsa_rectangle(scaling=4/3, rec_scale=0.25, circ_scale=0.05):
    ww, wl = exp.screen.size
    #rectangle width 
    width_rectangle = ww*rec_scale
    #rectangle length 
    length_rectangle = width_rectangle*(1/scaling)
    #circle radius
    size_circle = ww*circ_scale
    square1 = stimuli.Rectangle(size=(width_rectangle,length_rectangle),
                                colour=grey,
                                position=(0,0))

    def create_circs( length = length_rectangle, width = width_rectangle, size = size_circle):
        pos = []
        for x in (width*0.5,-width*0.5):
            for y in (length*0.5,-length*0.5):
                pos.append((x,y))
        
        circs = []
        for k in pos:
            if k[1] > 0: #look at y position if above 0 then black else then white
                circle = stimuli.Circle(radius= size,
                                        colour=black, 
                                        position=k )
                circs.append(circle)
            else:
                circle = stimuli.Circle(radius= size,
                                        colour=white, 
                                        position =k)
                circs.append(circle)
        return circs


    circles = create_circs()

    # Start running the experiment
    for i,k in enumerate(circles):
        if i == 0:
            k.present(clear=True,update=False)
        else:
            k.present(clear=False,update=False)
        

    square1.present(clear=False, update=True)
    exp.clock.wait(1000)

circle_scales = [0.05,0.06,0.07]
rec_scales =  [0.25,0.27,0.3]
aspects = [3/4,2/3,3/2,4/3,8/7]

for aspect in aspects:
    for rec_sc in rec_scales:
        for circ_sc in circle_scales:
            kanizsa_rectangle(scaling=aspect, rec_scale=rec_sc,circ_scale=circ_sc)


control.end()