# Kaidun (by HktOverload)

import abc

from scene_types import *
from scene_geometry import *
from scene_components import *

import rendering as r
import lighting as l

class CubeScene(Scene):

    @staticmethod
    def onEvent(app, event):
        moveCamera(app, event)
        adjustLight(app, event)
        app.viewer.lighting[0].ctr = app.viewer.cam.ctr

    @staticmethod
    def allGeometry(app):
        return [ r.flat(l.lambertian(halfCube())) ]
