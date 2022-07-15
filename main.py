# Kaidun (by HktOverload)

from cmu_112_graphics import *

def appStarted(app):
    sizeChanged(app)

def sizeChanged(app):
    app.w, app.h = app.width, app.height
    app.cx, app.cy = app.w//2, app.h//2

def redrawAll(app, canvas):
    canvas.create_rectangle(
        int(1 / 4 * app.w),
        int(1 / 4 * app.h),
        int(3 / 4 * app.w),
        int(3 / 4 * app.h),
    )

if __name__ == '__main__':
    runApp(
        width=1920//2, height=1080//2,
        title='Game Window',
    )
