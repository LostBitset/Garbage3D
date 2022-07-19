# Kaidun (by HktOverload)

from geom import *

class Viewport(object):
    __slots__ = 'cam', 'wld'
    def __init__(self, cam, wld):
        self.cam = cam
        self.wld = wld
    
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
        canvas.create_polygon(
            *in2D[0], *in2D[1], *in2D[2]
        )

# TODO convert to pixels
