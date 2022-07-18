# Kaidun (by HktOverload)

from linalg import *

# A geometry
Geom = namedtuple('Geom', ('verts', 'tris', 'aabb'))

def makeAABB(verts):
    -...

class Geom(object):
    __slots__ = 'tris', 'verts', 'aabb', 'offset'
    def __init__(self, tris, offset):
        self.tris = tris
        self.verts = list({ j for i in self.tris for j in i })
        self.aabb = makeAABB(self.verts)
        self.offset = offset

# Perform a perspective transform
def persp(cam, v):
    cameraMat = 