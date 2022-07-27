# Kaidun (by HktOverload)

class Scene(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def onEvent(app, event):
        # Called when an event occurs
        # These don't use the same format as tkinter
        # For example, pressing 'r' is encoded as ('kb/p', 'r')
        # Moving the mouse to (0, 0) is encoded as ('mouse/to', 0, 0)
        pass

    @staticmethod
    @abc.abstractmethod
    def allGeometry(app):
        # A list containing (Geom, Renderer) tuples for everything
        # within this scene
        # Basically just a geomsrc
        pass
