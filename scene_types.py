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
    def allGeometry(app):
        # A list containing (Geom, Renderer) tuples for everything
        # within this scene
        # Basically just a geomsrc
        # This is not an abstract method because implementing it
        # is optional, not every scene has 3D geometry
        return []

    @staticmethod
    def drawOverlay(app, canvas):
    	# A procedure to draw any non-3D elements that go on top
    	# of the 3D part of the scene
    	# This is not an abstractmethod because implementing it
    	# is completely optional
    	pass
