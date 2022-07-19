# Kaidun (by HktOverload)

from cmu_112_graphics import *

from worlds import *
from viewport import *

def appStarted(app):
    app.world = CubeWld()
    app.viewer = Viewport(Camera([0, 0, -2]), app.world)
    # The size changed from undefined to something, didn't it?
    sizeChanged(app)

def sizeChanged(app):
    # These are just shorthands
    app.w, app.h = app.width, app.height
    app.cx, app.cy = app.w//2, app.h//2

def redrawAll(app, canvas):
    app.viewer.render(canvas)

if __name__ == '__main__':
    runApp(
        width=1920//2, height=1080//2,
        title='Game Window',
    )
