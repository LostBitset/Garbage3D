# Kaidun (by HktOverload)

from linalg import *
from math import sin, cos, pi

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

def perspective(flen):
    return Mat([
        1, 0, 0,
        0, 1, 0,
        0, 0, (1/flen),
        0, 0, 0,
    ], 3, 4)

class Camera(object):
    __slots__ = 'ctr', 'flen', 'rot', 'rotP'
    def __init__(self, ctr, flen=1, yaw=0, pitch=0, roll=(pi/2)):
        self.ctr = ctr
        self.flen = flen
        self.rot = rotMat(yaw, pitch, roll)
        rotH = Mat([
            *self.rot.col(0), 0,
            *self.rot.col(1), 0,
            *self.rot.col(2), 0,
            0, 0, 0, 1,
        ], 4, 4)
        self.rotP = perspective(flen) @ rotH

    # Perform a perspective transform
    def persp(self, v):
        v = add(v, neg(self.ctr))
        homogenous2D = self.rotP * toH(v)
        return pDiv(homogenous2D)

    # Get the camera's image plane (a single z value for now)
    def imPlane(self):
        normal = self.rot * [0, 0, 1]
        pt = add(self.ctr, sc(normal, self.flen))
        return Plane(pt, normal)

if __name__ == '__main__':
    cam = Camera([1, 1, 2])
    print(cam.persp([0, 0, 4]))
