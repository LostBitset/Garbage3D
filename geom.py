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

# A camera matrix (no rotation for now)
def makeCMat(ctr, a, b, c):
    return Mat([
        cos(a)*cos(b), sin(a)*cos(b), -sin(b),
        (cos(a)*sin(b)*sin(c))-(sin(a)*cos(c)),
        (sin(a)*sin(b)*sin(c))+(cos(a)*cos(c)),
        cos(b)*sin(c),
        (cos(a)*sin(b)*cos(c))+(sin(a)*sin(c)),
        (sin(a)*sin(b)*cos(c))-(cos(a)*sin(c)),
        cos(b)*cos(c),
        *neg(ctr),
    ], 3, 4)


class Camera(object):
    __slots__ = 'ctr', 'yaw', 'pitch', 'roll', 'mat'
    def __init__(self, ctr, yaw=0, pitch=0, roll=(pi/2)):
        self.ctr = ctr
        self.yaw, self.pitch, self.roll = yaw, pitch, roll
        self.mat = makeCMat(ctr, -yaw, -pitch, -roll)

    # Perform a perspective transform
    def persp(self, v):
        homogenous2D = self.mat * toH(v)
        return pDiv(homogenous2D)

    # Get the camera's image plane (a single z value for now)
    def imPlane(self):
        return self.ctr[2]

if __name__ == '__main__':
    cam = Camera([1, 1, 2])
    print(cam.persp([0, 0, 4]))
