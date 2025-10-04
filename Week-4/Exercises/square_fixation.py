from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start(subject_id=1)
##the problem is that the fixation instanly updates the buffer 
fixation.present(clear=True, update=True)
exp.clock.wait(500)
#and the square updates the buffer for a second time
#so they do not appear inside each other
#to fix this we can present anoother fixation without updating
fixation.present(clear=True, update=False)
#which would appear inside the square after 0.5 seconds pass
square.present(clear=False, update=True)
exp.keyboard.wait()

control.end()