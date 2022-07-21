# Kaidun (by HktOverload)

import abc

from scene_components import *

class Scene(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def onEvent(app, event, eventType):
        # Called when an event occurs
        pass

    @staticmethod
    @abc.abstractmethod
    def toGeometry(app):
        # Generates the geometry according to app
        # This can return either the new geometry, or a new scene
        # If the return is an instance of Scene, than that new scene
        # takes control
        pass

class CubeScene(Scene):

    @staticmethod
    def onEvent(app, event, eventType):
        raise NotImplementedError('Event system does not yet exist')

    @staticmethod
    def toGeometry(app):
        return [ halfCube() ]
