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
        self.rot = rotMat(yaw, pitch, roll)
        self.setupRot()

    def setupRot(self):
        rotH = Mat([
            *self.rot.col(0), 0,
            *self.rot.col(1), 0,
            *self.rot.col(2), 0,
            0, 0, 0, 1,
        ], 4, 4)
        self.rotP = perspective(self.flen) @ rotH
        self.setupImPlane()

    def setupImPlane(self):
        normal = self.rot.t() * [0, 0, 1]
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
        self.rot = rotMat(yaw, pitch, roll) @ self.rot
        self.setupRot()

    # Move the camera along a given axis in it's own coordinate space
    def move(self, ax, mod):
        self.translate(
            [ mod if i == ax else 0 for i in range(3) ]
        )

    # Translate the camera with respect to where it is facing
    def translate(self, v):
        self.ctr = add(self.ctr, self.rot.t() * v)
        self.setupImPlane()
