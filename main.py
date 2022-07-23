# Kaidun (by HktOverload)

from cmu_112_graphics import *

from scenes import *
from viewport import *

def appStarted(app):
    app.camCtr = [2, 2, 2]
    app.camRoll = (pi/2)
    app.scene = CubeScene
    app.viewer = Viewport(
        Camera(app.camCtr, roll=app.camRoll),
        lambda app: app.scene.allGeometry(app),
    )
    # The size changed from undefined to something, didn't it?
    sizeChanged(app)

def sizeChanged(app):
    # These are just shorthands
    app.w, app.h = app.width, app.height
    app.cx, app.cy = app.w//2, app.h//2

def keyPressed(app, event):
    step, angleStep = 0.2, (pi/16)
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
    elif event.key == 'q':
        app.camRoll -= angleStep
    elif event.key == 'f':
        app.camRoll += angleStep

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.w, app.h, fill='#000')
    app.viewer.cam = Camera(app.camCtr, roll=app.camRoll)
    app.viewer.render(app, canvas)

if __name__ == '__main__':
    runApp(
        width=1920//2, height=1080//2,
        title='Game Window',
    )
