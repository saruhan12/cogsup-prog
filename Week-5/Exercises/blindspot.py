from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN, K_UP, K_LEFT, K_RIGHT,K_1, K_2, K_SPACE

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial(side="r"):
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
    fixation.preload()
    text = stimuli.TextScreen("Blind Spot", f"Close the {"RIGHT" if side == 'r' else "LEFT"} EYE. Use ARROWS to move, 1 to decrease 2 to increase the size of the circle, when the blind spot is found press SPACE to quit. ---Press SPACE to continue")
    radius = 75
    circle = make_circle(radius)
    pos = (0,0)
    text.present(True,True)
    exp.keyboard.wait() 
    fixation.present(True, False)
    circle.present(False, True)
    while 1:
        pressed, _ = exp.keyboard.wait(keys = [K_DOWN, K_UP, K_LEFT, K_RIGHT, K_1, K_2, K_SPACE])
        if pressed == K_UP:
            circle.move((0,30))
        elif pressed == K_DOWN:
            circle.move((0,-30))
        elif pressed == K_LEFT:
            circle.move((-30,0))
        elif pressed == K_RIGHT:
            circle.move((30,0))
        elif pressed == K_1:
            radius=radius*0.9
            circle = make_circle(radius,circle.position)
        elif pressed == K_2:
            radius=radius*1.3
            circle = make_circle(radius,circle.position)
        elif pressed == K_SPACE:
            break
        fixation.present(True, False)
        circle.present(False, True)
        exp.clock.wait(100)
control.start(subject_id=1)

run_trial()
    
control.end()