# Kaidun (by HktOverload)

from cmu_112_graphics import *

from lighting import *
from scenes import *
from viewport import *

def appStarted(app):
    app.scene = CubeScene
    app.viewer = Viewport(
        Camera([2, 2, 2], roll=(pi/2)),
        lambda app: app.scene.allGeometry(app),
        lighting=[ PointLight([1, 2, 2], 3.5), ],
    )
    app.timerDelay = 1000//30 # 30 fps
    # The size changed from undefined to something, didn't it?
    sizeChanged(app)

def sizeChanged(app):
    # These are just shorthands
    app.w, app.h = app.width, app.height
    app.cx, app.cy = app.w//2, app.h//2

def keyPressed(app, event):
    app.scene.onEvent(app, ('kb/p', event.key))

def mousePressed(app, event):
    app.scene.onEvent(app, ('mouse/p', event.x, event.y))

def mouseMoved(app, event):
    app.scene.onEvent(app, ('mouse/to', event.x, event.y))

def timerFired(app):
    app.scene.onEvent(app, ('timer/fired',))

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.w, app.h, fill='#000')
    app.viewer.render(app, canvas)
    app.scene.drawOverlay(app, canvas)

if __name__ == '__main__':
    runApp(
        width=1920//2, height=1080//2,
        title='Game Window',
    )
