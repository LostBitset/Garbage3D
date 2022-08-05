# (by HktOverload)

from geom import *
from math import pi

# A 3x4 matrix encoding a perspective camera looking up
# and located at the origin
# [: Citation https://en.wikipedia.org/wiki/Camera_matrix :]
def perspective(flen):
    return Mat([
        1, 0, 0,
        0, 1, 0,
        0, 0, (1/flen),
        0, 0, 0,
    ], 3, 4)

# Represents a perspective camera
class Camera(object):
    # ctr <-> Camera center
    # flen <-> Focal length
    # rot <-> Rotation matrix that converts from world coords
    #         to camera coords, where it's facing upwards
    # rotP <-> The rotation matrix but combined with the
    #          matrix defining a the perspective camera,
    #          it converts from 3D homogenous coords (4D)
    #          to 2D homogenous coords (3D), but doesn't
    #          account for the displacement of the camera
    # imPlane <-> A Plane object defining the image plane
    __slots__ = 'ctr', 'flen', 'rot', 'rotP', 'imPlane'
    def __init__(self, ctr, flen=1, **kwargs):
        self.ctr = ctr
        self.flen = flen
        self.setup(**kwargs)
    
    # Define everything that takes optional arguments in
    # __init__
    def setup(self, yaw=0, pitch=0, roll=(pi/2)):
        self.rot = rotMat(yaw, pitch, roll)
        self.setupRot()

    # Setup everything to be in sync with self.rot
    # This should be called whenever self.rot is modified
    def setupRot(self):
        rotH = Mat([
            *self.rot.col(0), 0,
            *self.rot.col(1), 0,
            *self.rot.col(2), 0,
            0, 0, 0, 1,
        ], 4, 4)
        self.rotP = perspective(self.flen) @ rotH
        self.setupImPlane()

    # Setup the image plane to be in sync with self.rot and
    # also self.ctr
    # Whenever self.rot is modified, call setupRot, but if only
    # self.ctr is being changed, call this directly
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
