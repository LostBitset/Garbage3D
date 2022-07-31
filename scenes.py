# (by HktOverload)

import abc

from chunks import *

from scene_geometry import *
from scene_components import *

import rendering as r
import lighting as l

class Scene(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def onEvent(cls, app, event):
        # Called when an event occurs
        # These don't use the same format as tkinter
        # For example, pressing 'r' is encoded as ('kb/p', 'r')
        # Moving the mouse to (0, 0) is encoded as ('mouse/to', 0, 0)
        pass

    @classmethod
    def allGeometry(cls, app):
        # A list containing (Geom, Renderer) tuples for everything
        # within this scene
        # Basically just a geomsrc
        # This is not an abstract method because implementing it
        # is optional, not every scene has 3D geometry
        return []

    @classmethod
    def drawOverlay(cls, app, canvas):
        # A procedure to draw any non-3D elements that go on top
        # of the 3D part of the scene
        # This is not an abstractmethod because implementing it
        # is completely optional
        pass

class CubeScene(Scene):

    @classmethod
    def onEvent(cls, app, event):
        moveCamera(app, event)
        adjustLight(app, event)
        app.viewer.lighting[0].ctr = app.viewer.cam.ctr

    @classmethod
    def allGeometry(cls, app):
        return app.chunks.loaded(
            *app.viewer.cam.ctr[:2],
            2
        )
