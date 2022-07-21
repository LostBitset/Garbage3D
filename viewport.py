# Kaidun (by HktOverload)

from geom import *

# Returns a subgeometry that corresponds to the part of a tri
# in front of the image plane
# This can be either a tri, a quad, or None if the entire tri
# is behind the image plane
def forceVisible(tri, verts, imPlane):
    return tri # TEMP

class Viewport(object):
    __slots__ = 'cam', 'geomsrc', 'pxSize'
    def __init__(self, cam, geomsrc, pxSize=(1920//2, 1080//2)):
        self.cam = cam
        self.geomsrc = geomsrc
        self.pxSize = pxSize
    
    def render(self, app, canvas):
        imPlane = self.cam.imPlane()
        for g in self.geomsrc(app):
            memo = {
                i: self.cam.persp(g.verts[i]) \
                    for i in range(len(g.verts))
            }
            for tri in g.tris:
                visible = forceVisible(tri, g.verts, imPlane)
                if len(visible) == 3:
                    self.renderTriAt(canvas, [
                        memo[i] for i in visible
                    ])
                elif len(visible) == 4:
                    self.renderQuadAt(canvas, [
                        memo[i] for i in visible
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
