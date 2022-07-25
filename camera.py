# Kaidun (by HktOverload)

from geom import *
from math import pi

def perspective(flen):
    return Mat([
        1, 0, 0,
        0, 1, 0,
        0, 0, (1/flen),
        0, 0, 0,
    ], 3, 4)

class Camera(object):
    __slots__ = 'ctr', 'flen', 'rot', 'rotP', 'imPlane'
    def __init__(self, ctr, flen=1, **kwargs):
        self.ctr = ctr
        self.flen = flen
        self.setup(**kwargs)
        
    def setup(self, yaw=0, pitch=0, roll=(pi/2)):
        self.rot = (yaw, pitch, roll)
        mat = rotMat(yaw, pitch, roll)
        rotH = Mat([
            *mat.col(0), 0,
            *mat.col(1), 0,
            *mat.col(2), 0,
            0, 0, 0, 1,
        ], 4, 4)
        self.rotP = perspective(self.flen) @ rotH
        normal = mat.t() * [0, 0, 1]
        pt = self.ctr
        self.imPlane = Plane(pt, normal)

    # Perform a perspective transform
    def persp(self, v):
        v = add(v, neg(self.ctr))
        homogenous2D = self.rotP * toH(v)
        return homogenous2D

    # Check if a vertex is visible
    def isVisible(self, v):
        return self.imPlane.side(v) < -0.1

    # Rotate the camera
    def rotate(self, yaw=0, pitch=0, roll=0):
        self.setup(
            yaw=self.rot[0]+yaw,
            pitch=self.rot[1]+pitch,
            roll=self.rot[2]+roll,
        )
