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
    __slots__ = 'verts', 'tris', 'data', 'aabb'
    def __init__(self, verts, tris, data=None):
        self.verts = verts # List[Coord3]
        self.tris = tris # Tuple3[IndexInto[self.verts]]
        self.data = data # Dict[Str,List[Any]]
        self.aabb = makeAABB(self.verts) # Tuple2[Coord3]

    def translated(self, vec):
        return Geom(
            [ add(vert, vec) for vert in self.verts ],
            self.tris, self.data, self.aabb,
        )

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

def centroid(pts):
    total = ZeroVec
    for i in pts:
        total = add(total, i)
    return sc(total, 1/len(pts))

# Get the normal vector of a surface defined as a triangle
# This could be either positive or negative, depending on the ordering
# of the points
def triNormal(tri):
    [a, b, c] = tri
    b = add(b, neg(a))
    c = add(c, neg(a))
    return norm(cross3(b, c))
