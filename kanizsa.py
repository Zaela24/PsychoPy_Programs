# Slightly modified version of Kanisza.py from www.programmingvisualillusionsforeveryone.online

from psychopy import visual, event, core

_win_size = [1000, 1000]

win = visual.Window(
    color=[1, 1, 1],  # white
    units="pix",
    size=_win_size,
    allowGUI=False,
    fullscr=False
)

circle = visual.Circle(
    win,
    radius=80,
    fillColor=[-1, -1, -1],  # black
    lineColor=None
)

line = visual.Line(
    win,
    units="pix",
    lineColor=[-1, -1, -1],  # black
    lineWidth=2
)
# set line.start and line.end

square = visual.Rect(
    win,
    width=200,
    height=200,
    fillColor=[1, 1, 1],  # white
    lineColor=None
)

scale = visual.RatingScale(
    win,
    pos=[0, -360],
    low=10,
    high=100,
    textSize=0.5,
    lineColor=[-1, -1, -1],  # black
    tickHeight=False,
    scale=None,
    showAccept=False,
    singleClick=True
)

info = visual.TextStim(
    win,
    pos=[0, -385],
    text="",
    height=18,
    color=[-1, -1, -1]  # black
)

x = 100  # variable to make it easy to change all circPos
circPos = [[-x, -x], [-x, x], [x, x], [x, -x]]

done = False

while not done:
    circle.setPos(circPos[0])
    circle.draw()
    circle.setPos(circPos[1])
    circle.draw()
    circle.setPos(circPos[2])
    circle.draw()
    circle.setPos(circPos[3])
    circle.draw()

    line.draw()
    square.draw()
    info.draw()
    scale.draw()
    win.flip()

    if not scale.noResponse:  # i.e. new scale selection
        rad = scale.getRating()
        circle.radius = rad
        info.text = str(rad)
        scale.reset()

    if event.getKeys(keyList=['escape']):  # ESC key
        done = True

win.close()
core.quit()
