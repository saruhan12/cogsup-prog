from expyriment import design, control, stimuli, misc
import random

def load(stims):
    for stim in stims:
        stim.preload()
    

def timed_draw(stims):
    clock = misc.Clock()
    t0 = clock.time
    for stim in stims:
        stim.present()
    t1 = clock.time
    return t1-t0
    # return the time it took to draw

def present_for(stims, t=1000):
    clock = misc.Clock()
    time = timed_draw(stims)
    clock.wait(t-time)
    pass


""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemneted correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()