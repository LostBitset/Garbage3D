# (by HktOverload)

from camera import *
from geom import *

# Check if all items of an iterable are in a container
def allIn(itr, container):
    for i in itr:
        if i not in container:
            return False
    return True

defaultSize = (1920//2, 1080//2)

class Viewport(object):
    __slots__ = 'cam', 'geomsrc', 'lighting', 'pxSize'
    def __init__(self, cam, geomsrc, lighting=[], pxSize=defaultSize):
        self.cam = cam
        self.geomsrc = geomsrc
        self.lighting = lighting
        self.pxSize = pxSize
    
    def render(self, app, canvas):
        tasks = []
        for geom, render in (self.geomsrc)(app):
            memo, visible = {}, set()
            for i in range(len(geom.verts)):
                memo[i] = self.cam.persp(geom.verts[i])
                if memo[i][-1] == 0.0: continue
                memo[i] = pDiv(memo[i])
                if self.cam.isVisible(geom.verts[i]):
                    visible.add(i)
            for idx, tri in enumerate(geom.tris):
                if allIn(tri, visible):
                    tasks.append((
                        centroid([ geom.verts[i] for i in tri ]),
                        render, (self, canvas, [
                            memo[i] for i in tri
                        ], idx, geom.data),
                    ))
        tasks.sort(
            key = lambda x: \
                -math.hypot(*add(x[0], neg(self.cam.ctr)))
        )
        for _, render, args in tasks:
            render(*args)
