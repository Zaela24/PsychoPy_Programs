#  This program runs a simple McCollough Effect stim for 70 seconds, swapping between a white background and a color
#  background every 10 seconds


from psychopy import visual, core

win = visual.Window(
    size=[400, 400],
    units="pix",
    color=[1, 1, 1]
)

rect = visual.Rect(  # to create black bars within each quadrant
    win,
    width=10,
    height=200,
    lineColor=None,
    fillColor=[-1, -1, -1]  # black
)

color_rect = visual.Rect(  # to create base for coloring of quadrants
    win,
    width=200,
    height=200
)

line = visual.Line(  # to create line between quadrants
    win,
    units="pix",
    start=[0, 200],
    end=[0, -200],
    lineColor=[-1, -1, -1],  # black
    lineWidth=5
)

starting_coords = [[-215, 100], [100, 215],  # top two quadrants
                   [-100, 5], [-5, -100]]  # bottom two quadrants

orientation = [0, 90,  # vertical, horizontal
               90, 0]  # horizontal, vertical

fill = [[-1, 1, -1], [1, -1, -1],  # green, red
        [1, -1, -1], [-1, 1, -1]]  # red, green

fill_coords = [[-100, 100], [100, 100],
               [-100, -100], [100, -100]]

timer = core.CountdownTimer(70)  # 70 to start and end with the black and white version

while timer.getTime() > 0:
    for quadrant in range(4):
        rect.pos = starting_coords[quadrant]
        rect.ori = orientation[quadrant]
        if (int(timer.getTime()) // 10) & 1:  # every 10 seconds swap between color background and white background
            color_rect.fillColor = fill[quadrant]
            color_rect.pos = fill_coords[quadrant]
            color_rect.draw()
        for i in range(10):
            if rect.ori == 0:
                rect.pos += (20, 0)  # shift right
            else:
                rect.pos -= (0, 20)  # shift down
            rect.draw()
        if quadrant & 1:  # since line spans entire width / height, only draw twice (draws every other loop)
            line.draw()
            line.ori = orientation[quadrant]
            line.draw()
    win.flip()

win.close()
core.quit()
