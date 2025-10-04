from expyriment import design, control, stimuli, misc
from expyriment.misc.constants import K_SPACE

# 1 frame = 16.67ms
FRAME = 16.67

def load(stims):
    for stim in stims:
        stim.preload()
    

def timed_draw(stims,duration):
    clock = misc.Clock()
    t0 = clock.time
    for i,stim in enumerate(stims):
        stim.present(clear=(i==0), update=(i==len(stims)-1))
    t1 = clock.time
    draw_time = t1-t0
    clock.wait(duration - draw_time)
    stimuli.BlankScreen().present()
    return draw_time
    # return the time it took to draw

def present_for(stims,duration=200, between_frames=0):
    clock = misc.Clock()
    time = timed_draw(stims,duration)
    clock.wait(FRAME*between_frames - time if between_frames != 0 else 0)

def add_tags(circles, rad=20):
    colors = [(255,255,0),(255,0,0),(0,255,0)]#yellow,red,green
    tags =[]
    for color, circle in zip(colors, circles):
        tag = stimuli.Circle(radius=rad,colour=color)
        tag.plot(circle)
        tags.append(tag)
    return tags

def make_circles(poses, radius=50,color_tags=False):
    circles=[stimuli.Circle(radius=radius,colour=(0,0,255),position=pos) for _, pos in zip(range(3),poses)]
    tags = add_tags(circles=circles,rad=radius*0.2) if color_tags else []
    return circles, tags

def run_trial(circ_rad=50, ISI = 0, color_tags=False):
    while True:
        positionsA = [(-100+a*(circ_rad+70),0) for a in range(3)]
        positionsB = [positionsA[0]+(3*circ_rad+70, 0), positionsA[1], positionsA[2]]
        
        circs,tags = make_circles(positionsA, radius=circ_rad, color_tags=color_tags)
        load(tags)
        load(circs)
        present_for(circs+tags,between_frames=ISI)
        circs,tags = make_circles(positionsB, radius=circ_rad, color_tags=color_tags)
        load(tags)
        load(circs)
        present_for(circs+tags,between_frames=ISI)
        if exp.keyboard.check(K_SPACE): 
            break
    


""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

experiment_ISI = [0, 18, 18]
experiment_tags = [False, False, True]

for isi, tag in zip(experiment_ISI,experiment_tags):
    run_trial(ISI=isi,color_tags=tag)


control.end()