# (by HktOverload)

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
        ],
        {
            'wireframe-color': [None, None, None, None, 'red', 'red'],
            'color': [
                0xFF0000, 0xFF0000,
                0x00FF00, 0x00FF00,
                0x0000FF, 0x0000FF,
            ],
        },
    )
