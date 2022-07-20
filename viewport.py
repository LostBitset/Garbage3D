# Kaidun (by HktOverload)

from geom import *

class Viewport(object):
    __slots__ = 'cam', 'wld', 'pxSize'
    def __init__(self, cam, wld, pxSize=(1920//2, 1080//2)):
        self.cam = cam
        self.wld = wld
        self.pxSize = pxSize
    
    def render(self, canvas):
        for g in self.wld.visibleGeom(self.cam.imPlane()):
            memo = {
                i: self.cam.persp(g.verts[i]) \
                    for i in range(len(g.verts))
            }
            for tri in g.tris:
                self.renderTriAt(canvas, [
                    memo[i] for i in tri
                ])
    
    def renderTriAt(self, canvas, in2D):
        sX, sY = self.pxSize[0]//2, self.pxSize[1]//2
        def f(coord): # Converts from world-space to screen space
            return (
                int(coord[0] * sX + sX),
                int(coord[1] * sY + sY),
            )
        canvas.create_polygon(
            *f(in2D[0]), *f(in2D[1]), *f(in2D[2]),
            fill='', outline='blue',
        ) 
