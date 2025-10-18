from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_BLUE, C_RED, C_GREEN, C_EXPYRIMENT_ORANGE
import random

# setup
exp = design.Experiment(name="Stroop Balanced", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(["block", "trial", "type", "word", "ink", "key", "rt_ms", "ok"])
control.set_develop_mode()

control.initialize(exp)

cols = ["red", "blue", "green", "orange"]
cc = {"red": C_RED, "blue": C_BLUE, "green": C_GREEN, "orange": C_EXPYRIMENT_ORANGE}
key2col = {ord("r"): "red", ord("b"): "blue", ord("g"): "green", ord("o"): "orange"}


texts = {}

for w in cols: 
    texts[w] = {}
    for c in cols: 
        t = stimuli.TextLine(w, text_colour=cc[c])
        t.preload()  # load it now so it’s faster later
        texts[w][c] = t


fix = stimuli.FixCross(size=(150, 150), line_width=8); fix.preload()
oops = stimuli.TextLine("Wrong!", text_colour=C_BLACK); oops.preload()

# make a mismatch mapping per subject by rotating the list
def make_map(subj_id):
    shift = ((subj_id - 1) % 3) + 1   # shift according to subject(presumed 3 for the lab)
    m = {}
    for i, w in enumerate(cols):
        m[w] = cols[(i + shift) % 4]
    return m

def build_blocks(subj_id):
    # get the mismatch color map for this subject
    mismatch_map = make_map(subj_id)
    base_trials = []
    for c in cols:
        base_trials.append({"type": "match", "word": c, "ink": c})
    for w in cols:
        base_trials.append({"type": "mismatch", "word": w, "ink": mismatch_map[w]})

    all_blocks = []
    for block_num in range(1, 9):
        # copy the base list twice to get 16 trials
        trials = base_trials * 2
        random.shuffle(trials)  # mix them up so order is different each time

        # add block and trial numbers
        for i in range(len(trials)):
            trials[i]["block"] = block_num
            trials[i]["trial"] = i + 1

        all_blocks.append(trials)

    return all_blocks

control.start(subject_id=1)
sid = exp.subject
stimuli.TextScreen("Stroop balanced",
                   "Choose the INK COLOR, ignore the word.\n\n"
                   "R = red, B = blue, G = green, O = orange\n\n"
                   "Press any key to start.").present()
exp.keyboard.wait()

for block in build_blocks(1):
    for tr in block:
        fix.present(); exp.clock.wait(500)
        texts[tr["word"]][tr["ink"]].present()
        t0 = exp.clock.time
        key, _ = exp.keyboard.wait(keys=list(key2col.keys()))
        rt = int(exp.clock.time - t0)

        said = key2col.get(key, None)
        ok = int(said == tr["ink"])
        if not ok:
            oops.present(); exp.clock.wait(800)

        exp.data.add([tr["block"], tr["trial"], tr["type"], tr["word"], tr["ink"], key, rt, ok])

control.end()
