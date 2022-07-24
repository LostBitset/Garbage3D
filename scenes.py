# Kaidun (by HktOverload)

import abc

from scene_components import *

import rendering as r
import lighting as l

class Scene(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def onEvent(app, event, eventType):
        # Called when an event occurs
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
    def onEvent(app, event, eventType):
        raise NotImplementedError('Event system does not yet exist')

    @staticmethod
    def allGeometry(app):
        return [ r.wireframe(l.lambertian(halfCube()), []) ]
