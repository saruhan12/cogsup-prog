from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

fixation.present()
t0 = exp.clock.time

exp.clock.wait(1000)
#text.present() is not spontaneous so presenting before the 
#calculation of the fixation time causes it to appear as 1.008 seconds
#text.present()
t1 = exp.clock.time
fix_duration = (t1 - t0)/1000
#presenting the text after fixation time is calculated doesnt interfere with it
text.present()

exp.clock.wait(1000)

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()