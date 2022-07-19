# Kaidun (by HktOverload)

from abc import ABC, abstractmethod

from geom import *

class World(ABC):
    @abstractmethod
    def visibleGeom(self, imPlane):
        pass

def cube():
    return Geom(
        [
            [0, 0, 0], [1, 0, 0], [0, 1, 0], # 0 1 2
            [0, 0, 1], [1, 1, 0], [1, 0, 1], # 3 4 5
            [0, 1, 1], [1, 1, 1],            # 6 7
        ],
        [
            (0, 4, 1), (0, 4, 2), # bottom
            (3, 7, 6), (3, 7, 5), # top
            (0, 5, 3), (0, 5, 1), # front
        ]
    )

class CubeWld(ABC):
    def visibleGeom(self, imPlane):
        yield cube()
