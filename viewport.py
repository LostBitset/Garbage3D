# Kaidun (by HktOverload)

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
        tris = []
        for i, (geom, render) in enumerate((self.geomsrc)(app)):
            memo, visible = {}, set()
            for j in range(len(geom.verts)):
                memo[i][j] = self.cam.persp(geom.verts[j])
                if memo[i][j][-1] == 0.0: continue
                memo[i][j] = pDiv(memo[i][j])
                if self.cam.isVisible(geom.verts[j]):
                    visible.add(j)
            for idx, tri in enumerate(geom.tris):
                if allIn(tri, visible):
                    tris.append(tri)
        tris.sort(
            key = lambda tri: \
                math.hypot(*add(centroid(tri), neg(self.cam.ctr)))
        )
        for tri in tris:
            render(self, canvas, [
                memo[i][j] for j in tri
            ], idx, geom.data)
