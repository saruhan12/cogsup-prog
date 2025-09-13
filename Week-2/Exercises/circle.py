
from expyriment import design, control, stimuli


exp = design.Experiment(name="Circle")


control.initialize(exp)


fixation = stimuli.FixCross()


circle = stimuli.Circle(radius=50)


control.start(subject_id=1)


fixation.present(clear=True, update=True)


exp.clock.wait(1000)


circle.present(clear=True, update=True)


exp.keyboard.wait()


control.end()