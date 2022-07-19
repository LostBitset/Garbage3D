# Kaidun (by HktOverload)

from cmu_112_graphics import *

from worlds import *
from viewport import *

def appStarted(app):
    app.camCtr = [0, 0, -1]
    app.world = CubeWld()
    app.viewer = Viewport(Camera(app.camCtr), app.world)
    # The size changed from undefined to something, didn't it?
    sizeChanged(app)

def sizeChanged(app):
    # These are just shorthands
    app.w, app.h = app.width, app.height
    app.cx, app.cy = app.w//2, app.h//2

def keyPressed(app, event):
    step = 0.2
    if event.key == 'a':
        app.camCtr[0] -= step
    elif event.key == 'd':
        app.camCtr[0] += step
    elif event.key == 'w':
        app.camCtr[1] -= step
    elif event.key == 's':
        app.camCtr[1] += step
    elif event.key == 'e':
        app.camCtr[2] -= step
    elif event.key == 'c':
        app.camCtr[2] += step

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.w, app.h, fill='#000')
    app.viewer.cam = Camera(app.camCtr)
    app.viewer.render(canvas)

if __name__ == '__main__':
    runApp(
        width=1920//2, height=1080//2,
        title='Game Window',
    )
