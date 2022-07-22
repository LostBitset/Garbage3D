# Kaidun (by HktOverload)

from linalg import *
from math import sin, cos

def components(vecs, n):
    for i in range(n):
        yield [ v[i] for v in vecs ]

def makeAABB(verts):
    xs, ys, zs = components(verts, 3)
    return (
        [ min(xs), min(ys), min(zs) ],
        [ max(xs), max(ys), max(zs) ],
    )

class Geom(object):
    __slots__ = 'verts', 'tris', 'aabb'
    def __init__(self, verts, tris):
        self.verts = verts # List[Coord3]
        self.tris = tris # Tuple3[IndexInto[self.verts]]
        self.aabb = makeAABB(self.verts) # Tuple2[Coord3]

class Plane(object):
    __slots__ = 'pt', 'normal'
    def __init__(self, pt, normal):
        self.pt = pt
        self.normal = normal
    
    def side(self, v):
        return dot(
            self.normal,
            add(v, neg(self.pt)),
        )

# A camera matrix (coordinate space relative to camera center)
def rotMat(a, b, c):
    return Mat([
        cos(a)*cos(b), sin(a)*cos(b), -sin(b),
        (cos(a)*sin(b)*sin(c))-(sin(a)*cos(c)),
        (sin(a)*sin(b)*sin(c))+(cos(a)*cos(c)),
        cos(b)*sin(c),
        (cos(a)*sin(b)*cos(c))+(sin(a)*sin(c)),
        (sin(a)*sin(b)*cos(c))-(cos(a)*sin(c)),
        cos(b)*cos(c),
    ], 3, 3)
