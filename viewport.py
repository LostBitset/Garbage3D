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

# Represents a viewport into a world with some geometry
# The camera is cam,  geomsrc is a callback that defines
# the geometry, and lighting is a list of Light objects
class Viewport(object):
    __slots__ = 'cam', 'geomsrc', 'lighting', 'pxSize'
    def __init__(self, cam, geomsrc, lighting=[], pxSize=defaultSize):
        self.cam = cam
        self.geomsrc = geomsrc
        self.lighting = lighting
        self.pxSize = pxSize
    
    # Render the scene onto the canvas, one triangle at the time
    # This is done using the Painter's algorithm, which just
    # draws the triangles from farthest to closest, where distance
    # is determined as the distance from the viewer to the centroid
    # of the triangle
    # [: Citation https://en.wikipedia.org/wiki/Painter%27s_algorithm :]
    # It's pretty inefficient because it renders things that are
    # completely occluded, but the alternative is constructing a
    # z-buffer, which would be way slower because all of this is on
    # the CPU (and there isn't much occluded geometry anyway)
    # [: Citation/UnusedAlgorithm https://en.wikipedia.org/wiki/Z-buffering :]
    # Really all of this is incredibly slow because I don't have
    # access to GPU compute
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
