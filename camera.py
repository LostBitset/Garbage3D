# Kaidun (by HktOverload)

from geom import *

def perspective(flen):
    return Mat([
        1, 0, 0,
        0, 1, 0,
        0, 0, (1/flen),
        0, 0, 0,
    ], 3, 4)

class Camera(object):
    __slots__ = 'ctr', 'flen', 'rot', 'rotP', 'imPlane'
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
        normal = self.rot * [0, 0, 1]
        self.imPlane = Plane(self.ctr, normal)

    # Perform a perspective transform
    def persp(self, v):
        v = add(v, neg(self.ctr))
        homogenous2D = self.rotP * toH(v)
        return pDiv(homogenous2D)

    # Check if a vertex is visible
    def isVisible(self, v):
        return self.imPlane.side(v) > (10**-6)
