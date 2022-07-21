# Kaidun (by HktOverload)

from geom import *

def halfCube():
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

