# Kaidun (by HktOverload)

from geom import *

# Do not import * from this, it will bring only confusion
# This defines rendering-specific top-level functions
# Instead, use the following:
# import rendering as r

# A renderer is simply a function of the type
# (Viewport, Canvas, List3[Coord2]) -> NoneType
# It draws the given tri on the given canvas as the given viewport
# sees it
# However, a renderer ref is usually accompanied by the target geometry
# These are the (Geom, Renderer) pairs
# To make this easier, the rendering functions take geometry and return
# these pairs
# This is done with the @renders decorator
def renders(renderer, **kwargs):
    def inner(geom):
        return geom, lambda *args: renderer(*args, **kwargs)
    return inner

@renders
def wireframe(viewport, canvas, tri, color='blue'):
        sX, sY = viewport.pxSize[0]//2, viewport.pxSize[1]//2
        def f(coord): # Converts from world-space to screen space
            return (
                int(coord[0] * sX + sX),
                int(coord[1] * sY + sY),
            )
        canvas.create_polygon(
            *[ j for i in tri for j in f(i) ],
            fill='', outline=color,
        )
