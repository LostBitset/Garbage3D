# Kaidun (by HktOverload)

import abc

from scene_geometry import *
from scene_components import *

import rendering as r
import lighting as l

class Scene(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def onEvent(app, event):
        # Called when an event occurs
        # These don't use the same format as tkinter
        # For example, pressing 'r' is encoded as ('kb/down', 'r')
        # Moving the mouse to (0, 0) is encoded as ('mouse/to', 0, 0)
        pass

    @staticmethod
    @abc.abstractmethod
    def allGeometry(app):
        # A list containing (Geom, Renderer) tuples for everything
        # within this scene
        # Basically just a geomsrc
        pass

class CubeScene(Scene):

    @staticmethod
    def onEvent(app, event):
        moveCamera(app, event)

    @staticmethod
    def allGeometry(app):
        return [ r.flat(l.lambertian(halfCube()), []) ]
