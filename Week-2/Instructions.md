# Session 2: Introduction to Expyriment

## Preliminaries

First, update the Materials folder on your computer with the latest version of our repository. **Make sure to change ```your-path``` to the correct path!**

```bash
cd your-path/Programming/Materials/
git pull
```

Second, copy the Week-2 subfolder from **Materials** to **Assignments**. **Again, make sure to change ```your-path``` to the correct path!**

```bash
cd your-path/Programming/Assignments/
cp -R ../Materials/Week-2 .
```

## First expyriment script
```bash
cd your-path/Programming/Assignments/
cd Week-2/Exercises
python circle.py
```

```python
from expyriment import design, control, stimuli

exp = design.Experiment(name = "Circle")
control.initialize(exp)

fixation = stimuli.FixCross()
fixation.preload()

circle = stimuli.Circle(radius=50)
circle.preload()

control.start()

fixation.present()
exp.clock.wait(1000)

circle.present()
exp.keyboard.wait()

control.end()
```

## Step-by-step explanation of the script
Open **Assignments/Week-2/Exercises/circle.py** in VS Code and comment each line as we go together through the script.

### 1. Import modules

```python
from expyriment import design, control, stimuli
```

Imports Expyriment's main modules:
- **design**: for experiment/session objects
- **control**: for initializing, starting, and ending the experiment
- **stimuli**: for creating visual (and other) stimuli, such as shapes, text, and fixation crosses

### 2. Create the experiment

```python
exp = design.Experiment(name = "Circle")
```

Creates an ```Experiment``` object named "Circle" by calling the **Experiment** class in the **design** module. This object:
- stores the global settings of the experiment
- handles the data and log files, the screen, and the input devices (for instance, the keyboard)

### 3. Initialize the experiment
```python
control.initialize(exp)
```

Initializes the experiment stored in ```exp```:
- Opens the display window
- Presents the startup screen with the countdown—this is there to ensure that the Python interpreter has enough time to start up properly and improves timing accuracy afterwards
- Enables input handling (e.g., keys pressed) and event logging
- Starts an experimental clock for timing purposes

This must be done before any stimulus is presented.

### 4. Create a fixation cross
```python
fixation = stimuli.FixCross()
```

Creates a fixation-cross stimulus of default color and size. At this stage, ```fixation``` is just a Python object and has not been rendered.

### 5. Create a circle
```python
circle = stimuli.Circle(radius=50)
```

Creates a circle with a radius of 50 pixels.

### 6. Start the experiment
```python
control.start(subject_id=1)
```

Starts running the currently active experiment:
- Sets the subject ID to 1
- Creates a data file (more on this later)
- Presents the "Ready" screen

### 7. Present the fixation cross
```python
fixation.present()
```

Displays the fixation cross on screen.

### 8. Wait for 1 second
```python
exp.clock.wait(1000)
```

Waits 1000 ms (1 second), during which the fixation cross remains visible.

### 9. Present the circle
```python
circle.present()
```

Clears the screen and displays the circle stimulus.

### 10. Wait for a key press
```python
exp.keyboard.wait()
```

Waits until the participant presses a key.

### 11. End the experiment
```python
control.end()
```

Since the experiment is over, this quits expyriment:
- Saves data and event files
- Shows the "Ending experiment..." screen
- Closes the display window

## Exercise 1
In **Assignments/Exercises**, you will find a python script called `square.py`. Based on the example script above, create a script that displays the fixation cross for **half a second**, then a **blue** square of length 50 until a key is pressed.

Hint: You might want to have a look at expyriment's [`stimuli.Rectangle`] documentation (https://docs.expyriment.org/expyriment.stimuli.Rectangle.html#expyriment.stimuli.Rectangle). The color of the square can be set when initializing the object (note that expyriment uses British spelling, so use *colour* instead of *color*).

## Exercise 2
Open `two_squares.py`. Write a script that displays two squares side by side, the left one red, the right one green. Leave the fixation cross out. The two squares should be separated by 200 pixels but centered as a whole. Present them on-screen until a key is pressed.

Hints: 
- By default, stimuli are presented at the center of the screen. To modify this, you will need to set the ```position``` attribute of squares either when initializing them, or later (e.g., ```square_1.position = (x, y)``` or ```square_1.reposition(x, y)```)
- Expyriment takes (0, 0) to be the center of the screen and measures space in pixel units
- Mind the arguments you pass to ```present```

## Exercise 3: Causal perception from Michottean launching
Check out the first video at [this link](https://www.jfkominsky.com/demos.html), under **Launching and simple non-causal events**. Duplicate/create a copy of `two_squares.py` in the same **Assignments/Week-2/Exercises** subfolder and rename it to `launching.py`. Modify the code as follows: 
1. Present the two squares side by side for 1 second but modify their positions such that:
    - the red square starts on the left side, 400 pixels left from the center
    - the green square starts at the center
2. Using the ```position``` attribute, animate the left square to move to the left until it reaches the green square. Adjust the speed to approximately match the one in the video.
3. Once the red square reaches the green square, the green square should move to the right, at the same speed and for the same amount of time as the red square.
4. Show this display for 1 second.
5. Add explanatory comments at each step in the script.

**Do you get the impression that the red square causes the green square to move?**

Things to consider:
- How do I move a square to the left at a given speed?
- How do I encode the moment when the red square reaches the green square?

## Exercise 3A: Disrupting the causal perception temporally
Create a copy of ```launching.py``` and rename it to ```launching_disrupt_time.py```. Change the code to introduce a temporal lag between the squares' collision and the movement onset of the green square. First, try out a long delay (```exp.clock.wait(1000)```) and notice how the sense of causality disappears. Gradually shorten this delay until you find the smallest gap at which the event still feels **non-causal**. Leave that value in the code before uploading.

## Exercise 3B: Disrupt the causal perception spatially
Create a copy of ```launching.py``` and rename it to ```launching_disrupt_space.py```. Change the code to introduce a spatial gap between the two squares. Play around with multiple values. Gradually reduce this gap until you find the smallest distance at which the event still feels **non-causal**. Leave that value in the code before uploading.

## Exercise 3C: From launching to triggering
Create a copy of ```launching.py``` and rename it to ```triggering.py```. Make the green square on the right move at a speed three times faster than the square on the left. Does it still look like the red square caused the green square to move?

## Exercise 3D: Optional challenge for the more seasoned programmers among you
Display three consecutive launching events and have the axis of motion be randomly selected each time from a full circle of 360 degrees (Hint: this will require trigonometry).

Credits to [Jonathan Kominsky](https://www.jfkominsky.com) for this problem