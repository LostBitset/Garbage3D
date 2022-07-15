# Kaidun (by HktOverload)

import abc

class Scene(abc.ABC):

    @abc.abstractmethod
    @staticmethod
    def onEvent(app, event, eventType):
        # Called when an event occurs
        pass
    
    @abc.abstractmethod
    @staticmethod
    def toGeometry(app):
        # Generates the geometry according to app
        # This can return either the new geometry, or a new scene
        # If the return is an instance of Scene, than that new scene
        # takes control
        pass
