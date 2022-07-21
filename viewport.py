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
        for g in self.geomsrc(app):
            memo, visible = {}, set()
            for i in range(len(g.verts)):
                memo[i] = self.cam.persp(g.verts[i])
                if self.cam.isVisible(g.verts[i]):
                    visible.add(i)
            for tri in g.tris:
                if allIn(tri, visible):
                    self.renderTriAt(canvas, [
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
