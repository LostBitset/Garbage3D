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
        for geom, render in (self.geomsrc)(app):
            memo, visible = {}, set()
            for i in range(len(geom.verts)):
                memo[i] = self.cam.persp(geom.verts[i])
                if memo[i][-1] == 0.0: continue
                memo[i] = pDiv(memo[i])
                if self.cam.isVisible(geom.verts[i]):
                    visible.add(i)
            for tri in geom.tris:
                if allIn(tri, visible):
                    render(self, canvas, [
                        memo[i] for i in tri
                    ])
