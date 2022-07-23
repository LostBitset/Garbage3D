# Kaidun (by HktOverload)

from camera import *

# Check if all items of an iterable are in a container
def allIn(itr, container):
    for i in itr:
        if i not in container:
            return False
    return True

class Viewport(object):
    __slots__ = 'cam', 'geomsrc', 'pxSize'
    def __init__(self, cam, geomsrc, pxSize=(1920//2, 1080//2)):
        self.cam = cam
        self.geomsrc = geomsrc
        self.pxSize = pxSize
    
    def render(self, app, canvas):
        (self.geomsrc(app)[0][1])(
            self, canvas,
            [
                self.cam.persp(i) for i in \
                    [(0, 0, 0), (0.1, 0, 0), (0, 0, 0.1)]
            ],
        )
        print(self.cam.isVisible([0, 0, 0]))
        for geom, render in (self.geomsrc)(app):
            memo, visible = {}, set()
            for i in range(len(geom.verts)):
                memo[i] = self.cam.persp(geom.verts[i])
                if self.cam.isVisible(geom.verts[i]):
                    visible.add(i)
            for tri in geom.tris:
                if allIn(tri, visible):
                    render(self, canvas, [
                        memo[i] for i in tri
                    ])
    
    def renderTriAt(self, canvas, in2D):
        self.renderPolyAt(canvas, in2D)
    
    def renderQuadAt(self, canvas, in2D):
        self.renderPolyAt(canvas, in2D)
    
    def renderPolyAt(self, canvas, in2D):
        sX, sY = self.pxSize[0]//2, self.pxSize[1]//2
        def f(coord): # Converts from world-space to screen space
            return (
                int(coord[0] * sX + sX),
                int(coord[1] * sY + sY),
            )
        canvas.create_polygon(
            *[ j for i in in2D for j in f(i) ],
            fill='', outline='blue',
        )
