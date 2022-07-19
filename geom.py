# Kaidun (by HktOverload)

from linalg import *

def components(vecs, n):
    for i in range(n):
        yield [ v[i] for v in vecs ]

def makeAABB(verts):
    xs, ys, zs = components(verts)
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

def makeCMat(ctr):
    return Mat([
        1, 0, 0, 0, 1, 0, 0, 0, 1,
        *neg(ctr),
    ], 3, 4)

class Camera(object):
    __slots__ = 'ctr', 'mat'
    def __init__(self, ctr):
        self.ctr = ctr
        self.mat = makeCMat(self.ctr)

    # Perform a perspective transform
    def persp(self, v):
        homogenous2D = self.mat * toH(v)
        return pDiv(homogenous2D)

if __name__ == '__main__':
    cam = Camera([1, 1, 2])
    print(cam.persp([0, 0, 4]))
